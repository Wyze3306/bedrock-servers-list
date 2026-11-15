#!/usr/bin/env python3
"""Find each server's logo and cover picture and store them in art/.

For every server in servers/*.json, in order of trust:

1. its Discord server (the ``discord`` field, or an invite in the
   description or on the website): the guild icon is the logo, the guild
   banner or invite splash the cover;
2. its website: the largest square icon the page declares (apple-touch-icon,
   icon, web manifest) is the logo, its ``og:image`` / ``twitter:image`` the
   cover;
3. the banner already in ``image`` as a last-resort cover.

Then up to four more wide pictures for the server's page (its gallery):
the Discord splash and banner the cover did not use, the other pictures
its page shares, and the large pictures on the page itself, none of them
a near copy of the cover or of one another.

Logos are written to art/logos/<id>.png (at most 256 px), covers to
art/covers/<id>.jpg and the gallery to art/gallery/<id>-<n>.jpg (at most
640 px wide), and the server file gets ``logo`` / ``cover`` / ``gallery``
URLs pointing at them on raw.githubusercontent.com. A server keeps the art
it already has unless --refresh is given.

Needs Pillow. Run ``python3 scripts/build.py`` afterwards.
"""
import argparse
import concurrent.futures
import hashlib
import html.parser
import io
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

from common import ROOT, load_all

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("fetch_art.py needs Pillow: pip install Pillow")

RAW = "https://raw.githubusercontent.com/Wyze3306/bedrock-servers-list/main/"
ART = ROOT / "art"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
      " Chrome/130.0 Safari/537.36")
MAX_PAGE = 2 << 20
MAX_IMAGE = 8 << 20
LOGO_MIN, LOGO_MAX = 64, 256
COVER_MIN_W, COVER_MAX_W = 360, 640
GALLERY_MIN_W, GALLERY_MAX = 480, 4
# Two pictures this close (bits of a 64-bit average hash) are one picture.
SAME_PICTURE = 6

INVITE_RE = re.compile(
    r"(?:discord\.gg|discord(?:app)?\.com/invite)/([A-Za-z0-9-]{2,32})")
# Sites that are not the server's own: their icon is someone else's.
FOREIGN = ("discord.gg", "discord.com", "linktr.ee", "ign.gg", "t.me",
           "youtube.com", "youtu.be", "instagram.com", "twitter.com", "x.com",
           "facebook.com", "tiktok.com", "minecraftpocket-servers.com",
           "minecraft-mp.com", "topg.org", "github.com", "google.com",
           "sites.google.com", "carrd.co", "wixsite.com", "blogspot.com",
           "aternos.me", "aternos.org", "dc.gg", "minecraftservers-list.com")
# The same picture on this many servers is a host's or a builder's default.
GENERIC = 3


def get(url, limit, accept="*/*"):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": accept})
    with urllib.request.urlopen(req, timeout=10) as r:
        blob = r.read(limit + 1)
        if len(blob) > limit:
            raise ValueError("too large")
        return blob, r.geturl(), r.headers.get_content_charset() or "utf-8"


def foreign(url):
    host = (urllib.parse.urlsplit(url).hostname or "").lower()
    return any(host == h or host.endswith("." + h) for h in FOREIGN)


class Head(html.parser.HTMLParser):
    """The icons, cover candidates and Discord invites of one page."""

    def __init__(self):
        super().__init__()
        self.icons, self.covers, self.manifest = [], [], None
        self.pictures = []

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "link":
            rel = a.get("rel", "").lower().split()
            href = a.get("href", "")
            if not href:
                return
            if "manifest" in rel:
                self.manifest = href
            elif "apple-touch-icon" in rel or "apple-touch-icon-precomposed" in rel:
                self.icons.append((href, _size(a.get("sizes")) or 180))
            elif "icon" in rel:
                self.icons.append((href, _size(a.get("sizes")) or 0))
        elif tag in ("img", "source"):
            src = a.get("data-src") or a.get("src") or ""
            if not src and a.get("srcset"):
                src = a["srcset"].split(",")[-1].strip().split(" ")[0]
            small = any(a.get(k, "").isdigit() and int(a[k]) < GALLERY_MIN_W // 2
                        for k in ("width", "height"))
            if src and not src.startswith("data:") and not small:
                self.pictures.append(src)
        elif tag == "meta":
            key = (a.get("property") or a.get("name") or "").lower()
            if key in ("og:image", "og:image:url", "og:image:secure_url",
                       "twitter:image", "twitter:image:src") and a.get("content"):
                self.covers.append(a["content"])


def _size(sizes):
    best = 0
    for part in (sizes or "").lower().split():
        m = re.fullmatch(r"(\d+)x(\d+)", part)
        if m:
            best = max(best, min(int(m[1]), int(m[2])))
    return best


def open_image(blob):
    """A Pillow image (largest frame of an .ico), or None."""
    try:
        im = Image.open(io.BytesIO(blob))
        if im.format == "ICO":
            sizes = sorted(im.info.get("sizes") or [], key=lambda s: s[0] * s[1])
            if sizes:
                im.size = sizes[-1]
        im.load()
        return im
    except Exception:
        return None


def as_logo(im):
    w, h = im.size
    if min(w, h) < LOGO_MIN or max(w, h) > 3 * min(w, h):
        return None
    im = im.convert("RGBA")
    # A logo drawn on a full transparent canvas: crop to what is drawn.
    box = im.getchannel("A").getbbox()
    if box and (box[2] - box[0]) * (box[3] - box[1]) < 0.85 * w * h:
        im = im.crop(box)
    im.thumbnail((LOGO_MAX, LOGO_MAX), Image.LANCZOS)
    return small_png(im)


def small_png(im):
    """The smaller of the full-colour and 256-colour PNG."""
    best = None
    for pic in (im, im.quantize(256, method=Image.Quantize.FASTOCTREE)):
        out = io.BytesIO()
        pic.save(out, "PNG", optimize=True)
        if best is None or len(out.getvalue()) < len(best):
            best = out.getvalue()
    return best


def as_cover(im):
    w, h = im.size
    if w < COVER_MIN_W or h < 0.3 * w or h > 0.8 * w:
        return None
    im = im.convert("RGB")
    if w > COVER_MAX_W:
        im = im.resize((COVER_MAX_W, round(h * COVER_MAX_W / w)), Image.LANCZOS)
    out = io.BytesIO()
    im.save(out, "JPEG", quality=84, optimize=True, progressive=True)
    return out.getvalue()


def as_gallery(im):
    w, h = im.size
    if w < GALLERY_MIN_W or h < 0.4 * w or h > 0.8 * w:
        return None
    im = im.convert("RGB")
    if w > COVER_MAX_W:
        im = im.resize((COVER_MAX_W, round(h * COVER_MAX_W / w)), Image.LANCZOS)
    out = io.BytesIO()
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    return out.getvalue()


def ahash(blob):
    """The 64-bit average hash of a picture, to tell near copies apart."""
    im = Image.open(io.BytesIO(blob)).convert("L").resize((8, 8), Image.BILINEAR)
    px = list(im.getdata())
    mean = sum(px) / len(px)
    return sum(1 << i for i, v in enumerate(px) if v >= mean)


def same_picture(a, b):
    return bin(a ^ b).count("1") <= SAME_PICTURE


def fetch_image(url):
    try:
        blob, _, _ = get(url, MAX_IMAGE, "image/*")
    except Exception:
        return None
    return open_image(blob)


def discord_art(code):
    """(logo, wide pictures best first) image URLs of one Discord invite."""
    try:
        blob, _, _ = get("https://discord.com/api/v10/invites/"
                         + urllib.parse.quote(code), 1 << 20,
                         "application/json")
        g = json.loads(blob).get("guild") or {}
    except Exception:
        return None, []
    gid, logo, wide = g.get("id"), None, []
    if not gid:
        return None, []
    if g.get("icon"):
        logo = f"https://cdn.discordapp.com/icons/{gid}/{g['icon']}.png?size=512"
    if g.get("banner"):
        wide.append(f"https://cdn.discordapp.com/banners/{gid}/{g['banner']}.png?size=1024")
    if g.get("splash"):
        wide.append(f"https://cdn.discordapp.com/splashes/{gid}/{g['splash']}.jpg?size=1024")
    return logo, wide


def site_art(url):
    """(logo URLs best first, cover URLs, invites, picture URLs) of one
    website."""
    try:
        blob, final, charset = get(url, MAX_PAGE, "text/html")
    except Exception:
        return [], [], [], []
    page = blob.decode(charset, "replace")
    head = Head()
    try:
        head.feed(page)
    except Exception:
        pass
    join = lambda h: urllib.parse.urljoin(final, h.strip())
    icons = [(join(h), s) for h, s in head.icons]
    if head.manifest:
        try:
            mblob, mfinal, _ = get(join(head.manifest), 1 << 20)
            for ic in json.loads(mblob).get("icons") or []:
                if ic.get("src"):
                    icons.append((urllib.parse.urljoin(mfinal, ic["src"]),
                                  _size(ic.get("sizes"))))
        except Exception:
            pass
    icons.append((join("/apple-touch-icon.png"), 1))
    icons.append((join("/favicon.ico"), 0))
    icons = [u for u, _ in sorted(icons, key=lambda x: -x[1])
             if not u.lower().split("?")[0].endswith(".svg")]
    pictures = [join(p) for p in head.pictures
                if not p.lower().split("?")[0].endswith((".svg", ".gif", ".ico"))]
    return (list(dict.fromkeys(icons)), [join(c) for c in head.covers],
            INVITE_RE.findall(page), list(dict.fromkeys(pictures)))


def find_art(server, gallery=True):
    """(logo, cover, [gallery pictures]) of one server, as file contents."""
    logo = cover = None
    invites = INVITE_RE.findall(server.get("discord", "") + " "
                                + server.get("description", ""))
    site = server.get("website", "")
    icons, covers, pictures, wide = [], [], [], []
    if site and not foreign(site):
        icons, covers, more, pictures = site_art(site)
        invites += more
    elif site:
        invites += INVITE_RE.findall(site)
    for code in list(dict.fromkeys(invites))[:3]:
        dlogo, dwide = discord_art(code)
        if dlogo and logo is None:
            im = fetch_image(dlogo)
            logo = as_logo(im) if im else None
        wide += dwide
        if logo and wide:
            break
    for url in icons[:6]:
        if logo:
            break
        im = fetch_image(url)
        logo = as_logo(im) if im else None
    tried = set()
    for url in wide[:1] + covers[:3] + ([server["image"]] if server.get("image") else []):
        if cover:
            break
        tried.add(url)
        im = fetch_image(url)
        cover = as_cover(im) if im else None
    found = []
    if gallery:
        seen = [ahash(cover)] if cover else []
        for url in wide + covers + pictures[:12]:
            if len(found) == GALLERY_MAX:
                break
            if url in tried or foreign(url) and "discordapp" not in url:
                continue
            im = fetch_image(url)
            blob = as_gallery(im) if im else None
            if not blob:
                continue
            h = ahash(blob)
            if any(same_picture(h, o) for o in seen):
                continue
            seen.append(h)
            found.append(blob)
    return logo, cover, found


def drop_generic():
    """Forget the art several servers share: nobody's own."""
    by_hash = {}
    for sub in ("logos", "covers", "gallery"):
        for f in (ART / sub).glob("*"):
            by_hash.setdefault(hashlib.sha1(f.read_bytes()).digest(), []).append(f)
    gone = {f for files in by_hash.values() if len(files) >= GENERIC
            for f in files}
    for path, data in load_all():
        changed = False
        for kind, sub, ext in (("logo", "logos", ".png"),
                               ("cover", "covers", ".jpg")):
            f = ART / sub / (path.stem + ext)
            if f in gone:
                f.unlink()
                if data.pop(kind, None):
                    changed = True
        pics = [ART / "gallery" / u.rsplit("/", 1)[-1]
                for u in data.get("gallery", [])]
        if any(f in gone for f in pics):
            keep = []
            for f in pics:
                if f in gone:
                    f.unlink(missing_ok=True)
                else:
                    keep.append(f)
            write_gallery(path, data, [f.read_bytes() for f in keep])
            changed = True
        if changed:
            save(path, data)
    return len(gone)


def drop_cover_copies():
    """Take out of each gallery the near copies of the server's cover as it
    stands on disk (a cover found on an earlier run may come from another
    source than the one the gallery was compared with)."""
    dropped = 0
    for path, data in load_all():
        cover = ART / "covers" / (path.stem + ".jpg")
        pics = [ART / "gallery" / u.rsplit("/", 1)[-1]
                for u in data.get("gallery", [])]
        if not cover.is_file() or not pics:
            continue
        mark = ahash(cover.read_bytes())
        blobs = [f.read_bytes() for f in pics if f.is_file()]
        keep = [b for b in blobs if not same_picture(ahash(b), mark)]
        if len(keep) != len(pics):
            dropped += len(pics) - len(keep)
            write_gallery(path, data, keep)
            save(path, data)
    return dropped


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")


def write_gallery(path, data, blobs):
    """Store one server's gallery as <id>-0.jpg, <id>-1.jpg..."""
    for old in (ART / "gallery").glob(path.stem + "-*.jpg"):
        if old.stem[len(path.stem) + 1:].isdigit():
            old.unlink()
    urls = []
    for n, blob in enumerate(blobs):
        rel = f"art/gallery/{path.stem}-{n}.jpg"
        (ROOT / rel).write_bytes(blob)
        urls.append(RAW + rel)
    if urls:
        data["gallery"] = urls
    else:
        data.pop("gallery", None)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--refresh", action="store_true",
                    help="look again for servers that already have art")
    ap.add_argument("--gallery", action="store_true",
                    help="also look for servers without a gallery")
    ap.add_argument("--only", nargs="*", help="server ids to process")
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()
    for sub in ("logos", "covers", "gallery"):
        (ART / sub).mkdir(parents=True, exist_ok=True)
    todo = [(p, d) for p, d in load_all()
            if (not args.only or p.stem in args.only)
            and (args.refresh or not (d.get("logo") and d.get("cover"))
                 or args.gallery and not d.get("gallery"))]
    stats = {"logo": 0, "cover": 0, "gallery": 0}

    def one(item):
        path, data = item
        try:
            return path, data, find_art(data)
        except Exception as e:  # one broken site never stops the run
            print(f"{path.stem}: {e}", file=sys.stderr)
            return path, data, (None, None, [])

    with concurrent.futures.ThreadPoolExecutor(args.workers) as pool:
        for n, (path, data, (logo, cover, gallery)) in enumerate(
                pool.map(one, todo), 1):
            changed = False
            for kind, blob, sub, ext in (("logo", logo, "logos", ".png"),
                                         ("cover", cover, "covers", ".jpg")):
                if not blob or (data.get(kind) and not args.refresh):
                    continue
                rel = f"art/{sub}/{path.stem}{ext}"
                (ROOT / rel).write_bytes(blob)
                data[kind] = RAW + rel
                stats[kind] += 1
                changed = True
            if gallery and (args.refresh or not data.get("gallery")):
                write_gallery(path, data, gallery)
                stats["gallery"] += 1
                changed = True
            if changed:
                save(path, data)
            print(f"[{n}/{len(todo)}] {path.stem}: "
                  f"logo={'yes' if logo else '-'} cover={'yes' if cover else '-'}"
                  f" gallery={len(gallery)}", flush=True)
    print(f"{stats['logo']} logos, {stats['cover']} covers, "
          f"{stats['gallery']} galleries written, "
          f"{drop_generic()} generic ones and "
          f"{drop_cover_copies()} copies of a cover dropped")


if __name__ == "__main__":
    main()
