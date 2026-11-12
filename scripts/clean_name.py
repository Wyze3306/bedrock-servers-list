"""Turn a raw server MOTD / title into a clean display name.

Raw names scraped from listing sites are full of versions, Discord links,
decorative symbols and "small caps" letters. When the title is empty or generic
("Geyser", "PocketMine-MP Server"...), the real name is taken from the domain.
"""
import html
import re
import unicodedata

SMALL_CAPS = str.maketrans({
    "ᴀ": "a", "ʙ": "b", "ᴄ": "c", "ᴅ": "d", "ᴇ": "e", "ꜰ": "f", "ɢ": "g", "ʜ": "h", "ɪ": "i",
    "ᴊ": "j", "ᴋ": "k", "ʟ": "l", "ᴍ": "m", "ɴ": "n", "ᴏ": "o", "ᴘ": "p", "ǫ": "q", "ʀ": "r",
    "ꜱ": "s", "ѕ": "s", "ᴛ": "t", "ᴜ": "u", "ᴠ": "v", "ᴡ": "w", "ʏ": "y", "ᴢ": "z",
})

TLDS = set("""com net org io gg me xyz fun pro club cc us eu fr de es ru pl br tr id in uk tw jp cn top lol
best ml tk co info biz online site live world games gaming network host cloud app dev ir vn ph mx ar cl
pe it nl se no dk fi cz ro hu gr bg ua kr th my sg au nz ca za sa ae eg ma pt be ch at lv lt ee sk si hr
rs ge kz by uz az tech store shop zone space one pw ws vip wtf ink run fm tv ly gl gs mc""".split())

PREFIXES = {"play", "mc", "www", "bedrock", "pe", "mps", "mcpe", "mcbe", "join", "ip", "server", "s1",
            "oyna", "jogar", "jugar", "mobil", "be", "mpc", "mcps", "en", "store", "hub", "lobby",
            "bd", "bds", "mobile", "connect", "pocket", "mcb", "geyser", "cross", "java"}

# Free hosting / dynamic-DNS providers: the server name is the sub-domain, not the provider.
HOSTING = {"exaroton.me", "aternos.me", "minehut.com", "playit.gg", "mcserv.me", "serveminecraft.net",
           "ddns.net", "duckdns.org", "hopto.org", "zapto.org", "loseyourip.com", "webhop.me", "dedyn.io",
           "bedrock.shulkerboxes.com", "shulkerboxes.com", "ploudos.me", "minecraft.best", "joinmc.link",
           "pebblehost.com", "mcpe.fun", "mcserver.us", "gs.ls", "mcbe.fr", "mclobby.fr", "mcpe.fr",
           "playit.plus", "ply.gg", "dedimc.io", "minerent.io", "cloud-ip.cc", "servegame.com",
           "freeminecraft.me", "gameserver.rocks", "minecraftnoob.com", "hosting.com"}

GENERIC = re.compile(
    r"(?:(?:a|an|my|the) )?(?:(?:minecraft|bedrock|mcpe|mcbe|pocketmine(?:-mp)?|nukkit(?:x)?|powernukkit(?:x)?|"
    r"cloudburst|geyser|dragonfly|altay|steadfast\d*)[ -]?)+(?:server|edition|world)?"
    r"|server|default|new|test|untitled|dedicated server|survival|skyblock|oneblock|prison|anarchy|factions?|pvp|"
    r"lobby|hub|smp|dungeons|parkour|bedwars|minigames|creative|vanilla|a anarchy server|my server|atualizado|updated|online|offline|open|beta|maintenance|(?:bedrock )?dedicated server|a minecraft server.*|"
    r"(?:welcome|currently|come |the greatest|under maintenance|coming soon|loading|hello).*", re.I)
JUNK_SEGMENT = re.compile(r"^(new\s+)?ip\b|^(join|welcome|official|bienvenid\w*|bienvenue|netzwerk)$", re.I)

DOMAIN = re.compile(r"^(?:[\w-]+\.)+([a-z]{2,10})$", re.I)
VERSION_RANGE = re.compile(
    r"(?:(?<![A-Za-z])v(?:er)?\.?\s*|(?<![\w.]))\d{1,2}\.\d{1,3}(?:\.\d{1,3}|\.[xX*])?\+?"
    r"(?:\s*(?:[-–~]|to)\s*\d{1,2}\.\d{1,3}(?:\.\d{1,3}|\.[xX*])?\+?)?", re.I)
VERSION_X = re.compile(r"\b\d{1,2}(?:\.\d+)*[xX]\b")


CYRILLIC_LOOKALIKES = str.maketrans("аеіорсхуѕјԁԛԝАВЕІКМНОРСТХ", "aeiopcxysjdqwABEIKMHOPCTX")


def _fix_homoglyphs(m):
    """Words mixing Latin and Cyrillic letters use Cyrillic look-alikes: map them back to Latin."""
    w = m.group(0)
    if re.search(r"[A-Za-z]", w) and re.search(r"[\u0400-\u04ff]", w) or re.fullmatch(r"[\u0400-\u04ff]+", w) and w.translate(CYRILLIC_LOOKALIKES).isascii():
        return w.translate(CYRILLIC_LOOKALIKES)
    return w


WELCOME = re.compile(r"^(?:bienvenue sur|bienvenido a|bem[- ]vindo (?:ao|a)|welcome to|willkommen auf)\s+", re.I)


def _tld_ok(label):
    return label.lower() in TLDS


def registrable(host):
    """Very small public-suffix heuristic: returns (labels_before_domain, domain)."""
    parts = host.lower().strip(".").split(".")
    if len(parts) <= 2:
        return [], ".".join(parts)
    if len(parts[-1]) == 2 and parts[-2] in {"co", "com", "net", "org", "gov", "edu", "ac", "my", "web", "or", "rf", "us", "go", "ne", "biz", "id", "ac"}:
        n = 3
    else:
        n = 2
    domain = ".".join(parts[-n:])
    for h in HOSTING:
        if host.lower().endswith("." + h) or host.lower() == h:
            n = h.count(".") + 1
            domain = ".".join(parts[-n:])
            break
    return parts[:-n], domain


def _pretty_label(label):
    words = [w for w in re.split(r"[-_]+", label) if w]
    out = []
    for w in words:
        out.append(w if (any(c.isupper() for c in w) and any(c.islower() for c in w)) else _cap_word(w))
    return " ".join(out)


def name_from_host(host):
    before, domain = registrable(host)
    if domain in HOSTING or any(domain.endswith("." + h) or domain == h for h in HOSTING):
        subs = [p for p in before if p not in PREFIXES]
        if subs:
            return _pretty_label(subs[-1])
    return _pretty_label(domain.split(".")[0])


def _strip_domain(seg):
    """'play.boxrealm.net' -> 'boxrealm' ; leaves non-domains untouched."""
    m = DOMAIN.match(seg)
    if not m or not _tld_ok(m.group(1)) or " " in seg:
        return seg
    parts = seg.split(".")[:-1]
    while len(parts) > 1 and parts[0].lower() in PREFIXES:
        parts.pop(0)
    return ".".join(parts) if parts else seg


def _drop_brackets(s):
    def repl(m):
        inner = m.group(1)
        if re.search(r"\d+\.\d+|\blatest\b|[/@_]", inner, re.I) or not re.search(r"[^\W\d_]{2}", inner):
            return " "
        return m.group(0)
    return re.sub(r"[\[\(（【「『{<]([^\]\)）】」』}>]*)[\]\)）】」』}>]", repl, s)


ACRONYMS = {"smp", "pvp", "mc", "pe", "rp", "rpg", "mcpe", "mcbe", "vip", "pk"}


def _cap_word(w):
    lw = w.lower()
    if lw in ACRONYMS:
        return w.upper()
    for suf in ("smp", "pvp", "mc"):
        if lw.endswith(suf) and len(lw) > len(suf) + 2:
            return w[: -len(suf)][:1].upper() + w[: -len(suf)][1:].lower() + suf.upper()
    return w[:1].upper() + w[1:].lower()


def _titlecase_if_shouting(s):
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return s
    if all(c.islower() for c in letters) or (all(c.isupper() for c in letters) and len(letters) > 3):
        return " ".join(_cap_word(w) for w in s.split(" "))
    return s


def clean_name(raw, host):
    s = html.unescape(html.unescape(raw or ""))
    s = s.translate(SMALL_CAPS)
    s = unicodedata.normalize("NFKC", s).replace("\u0307", "").replace("i\u0307", "i")
    s = re.sub(r"[^\W\d_]+", _fix_homoglyphs, s)
    s = re.sub(r"[§&][0-9a-fk-or]", "", s, flags=re.I)
    s = re.sub(r"https?://\S+|(?:discord|dsc)\.(?:gg|com)/\S*|discord\.\S+", " ", s, flags=re.I)
    s = _drop_brackets(s)
    s = VERSION_RANGE.sub(" ", s)
    s = VERSION_X.sub(" ", s)
    # symbols / odd punctuation become separators, letters and digits stay
    chars = []
    for c in s:
        cat = unicodedata.category(c)
        if cat[0] in "LNM" or c in " .'-_&!+@#":
            chars.append(c)
        else:
            chars.append("|")
    s = "".join(chars)
    segments = []
    for part in s.split("|"):
        for seg in re.split(r"\s+-+\s+|\s*-{2,}\s*|\s*_{2,}\s*", part):
            seg = re.sub(r"\s+", " ", seg).strip(" .-_!&+@#'")
            if seg:
                segments.append(seg)
    name = ""
    for seg in segments:
        seg = _strip_domain(WELCOME.sub("", seg))
        if JUNK_SEGMENT.match(seg) or len(re.findall(r"[^\W\d_]", seg)) < 2 and not re.search(r"\d", seg):
            continue
        if GENERIC.fullmatch(seg):
            continue
        name = seg
        break
    name = re.sub(r"\s+", " ", name).strip(" .-_!&+@#'")
    name = re.sub(r"\s+(?:join\b.*|(?:[a-z]\s+)?[a-z]*\s*update\b.*|season\s*\w+.*|s\d+|v\d+|born in\b.*|out now.*)$", "", name, flags=re.I).strip(" .-_!&+@#'")
    name = re.sub(r"\bn\b(?=\s+[A-Z0-9])", " ", name).strip()
    if "." in name and re.search(r"\.[A-Za-z]{2,}", name):  # leftover domain / sentence with a link
        name = ""
    if len(name) <= 3 or re.search(r"[0-9a-f]{12,}", name, re.I):  # acronym or random hash -> use the domain
        name = ""
    if not re.search(r"[A-Za-z0-9]{2}", name):  # empty or non-latin only -> use the domain
        name = name_from_host(host)
    name = _titlecase_if_shouting(name)
    if len(name) > 40:
        name = name[:40].rsplit(" ", 1)[0] if " " in name[:40] else name[:40]
    return name.strip() or name_from_host(host)
