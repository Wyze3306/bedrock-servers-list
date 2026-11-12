#!/usr/bin/env python3
"""Convert the raw dump from scripts/scrape.js into servers/<slug>.json files.

Usage: python3 scripts/import_raw.py raw.json

Only clean entries are kept:
  - default Bedrock port 19132 only
  - domain names only (no numeric IP addresses)
  - names are cleaned (versions, Discord links, symbols removed; real name taken
    from the domain when the title is generic)
  - servers sharing the same cleaned name and domain are merged

The language does not exist on the source site: it is guessed from the
description (common words), then from the server country. Fix it by PR if wrong.
"""
import html
import json
import re
import sys
import unicodedata

from clean_name import clean_name, name_from_host, registrable
from common import SERVERS_DIR

COUNTRY_LANG = {
    "United States of America": "en", "United Kingdom": "en", "Canada": "en", "Australia": "en",
    "New Zealand": "en", "Ireland": "en", "Singapore": "en", "India": "en", "South Africa": "en",
    "Philippines": "en", "Malaysia": "en", "Hong Kong": "en",
    "France": "fr", "Belgium": "fr", "Luxembourg": "fr", "Switzerland": "fr",
    "Germany": "de", "Austria": "de", "Spain": "es", "Mexico": "es", "Argentina": "es", "Chile": "es",
    "Colombia": "es", "Peru": "es", "Venezuela": "es", "Brazil": "pt-BR", "Portugal": "pt",
    "Italy": "it", "Netherlands": "nl", "Poland": "pl", "Russia": "ru", "Russian Federation": "ru",
    "Ukraine": "uk", "Turkey": "tr", "Indonesia": "id", "Vietnam": "vi", "Thailand": "th",
    "Japan": "ja", "South Korea": "ko", "Korea, Republic of": "ko", "China": "zh", "Taiwan": "zh",
    "Saudi Arabia": "ar", "United Arab Emirates": "ar", "Egypt": "ar", "Morocco": "ar",
    "Sweden": "sv", "Norway": "no", "Denmark": "da", "Finland": "fi", "Czech Republic": "cs",
    "Romania": "ro", "Hungary": "hu", "Greece": "el", "Bulgaria": "bg",
}

STOPWORDS = {
    "en": "the and you your with for our server join play are this that from have will new best".split(),
    "fr": "le la les des une est pour que vous dans sur avec nous notre serveur rejoins rejoignez bienvenue et".split(),
    "es": "el los las una para que con por del servidor unete bienvenido nuestro jugar tu y".split(),
    "pt": "para que com uma voce nosso servidor entre jogar bem vindo os das não".split(),
    "de": "der die das und ist für mit auf dich unser willkommen spielen nicht ein".split(),
    "ru": "и в на для с по сервер это мы наш играть вас".split(),
    "tr": "ve bir için sunucu bize katıl oyun en da ile bu".split(),
    "id": "dan yang untuk server ini dengan kami bermain di kamu bergabung".split(),
    "it": "il lo la gli per che con una nostro unisciti benvenuto giocare e di".split(),
    "pl": "i w na dla z serwer nasz graj do się jest".split(),
}

IPV4 = re.compile(r"^\d{1,3}(?:\.\d{1,3}){3}$")


def detect_lang(text, country):
    t = text.lower()
    if re.search(r"[\u3041-\u309f\u30a1-\u30fa]", t): return "ja"
    if re.search(r"[가-힯]", t): return "ko"
    if re.search(r"[一-鿿]", t): return "zh"
    if re.search(r"[؀-ۿ]", t): return "ar"
    if re.search(r"[฀-๿]", t): return "th"
    words = re.findall(r"[\w'’]+", t)
    if len(words) >= 5:
        scores = {l: sum(w in set(sw) for w in words) for l, sw in STOPWORDS.items()}
        best = max(scores, key=scores.get)
        if scores[best] >= 3 and (best == "en" or scores[best] > scores["en"]):
            return "pt-BR" if best == "pt" and country == "Brazil" else best
    return COUNTRY_LANG.get(country, "en")


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def split_address(addr):
    addr = addr.strip()
    m = re.match(r"^(.*?):(\d{1,5})$", addr)
    if m and not (addr.count(":") > 1 and not addr.startswith("[")):
        return m.group(1).strip("[]"), int(m.group(2))
    return addr, 19132


def main(path):
    raw = json.load(open(path, encoding="utf-8"))
    items = raw.values() if isinstance(raw, dict) else raw
    SERVERS_DIR.mkdir(exist_ok=True)
    stats = {"port": 0, "numeric_ip": 0, "invalid": 0, "duplicate": 0}
    used, seen_addr, seen_name, seen_desc, n = set(), set(), set(), {}, 0
    for it in sorted(items, key=lambda x: int(x["id"])):
        ip, port = split_address(it.get("address", ""))
        if not ip or " " in ip or not re.fullmatch(r"[A-Za-z0-9.\-_]+", ip):
            stats["invalid" if not (ip and ":" in ip) else "numeric_ip"] += 1  # "Private Server", IPv6...
            continue
        if port != 19132:
            stats["port"] += 1
            continue
        if IPV4.match(ip):
            stats["numeric_ip"] += 1
            continue
        ip = ip.lower()
        if (ip, port) in seen_addr:
            stats["duplicate"] += 1
            continue
        seen_addr.add((ip, port))
        desc = html.unescape(html.unescape(it.get("description", ""))).strip()
        name = clean_name(it.get("name", ""), ip)
        domain = registrable(ip)[1]
        if (name.lower(), domain) in seen_name:  # same network exposed on several sub-domains
            stats["duplicate"] += 1
            continue
        prev = seen_desc.get(name.lower())
        if prev is not None:
            if any(desc[:80] == p for p in prev):  # same network under another domain
                stats["duplicate"] += 1
                continue
            name = name_from_host(ip)  # same title but a different server: use its own domain
            if (name.lower(), domain) in seen_name or name.lower() in seen_desc:
                stats["duplicate"] += 1
                continue
        seen_name.add((name.lower(), domain))
        seen_desc.setdefault(name.lower(), []).append(desc[:80])
        d = {
            "name": name, "ip": ip, "port": port,
            "description": desc or "No description provided.",
            "lang": detect_lang(desc, it.get("country", "")),
        }
        if it.get("banner"): d["image"] = it["banner"]
        if it.get("country"): d["country"] = it["country"]
        if it.get("version"): d["version"] = it["version"]
        if it.get("website", "").startswith("http"): d["website"] = it["website"]
        if it.get("discord", "").startswith("http"): d["discord"] = it["discord"]
        if it.get("tags"): d["tags"] = it["tags"]
        d["source"] = f"https://minecraftpocket-servers.com/server/{it['id']}/"
        slug = slugify(name) or slugify(ip) or f"server-{it['id']}"
        if slug in used:
            slug = f"{slug}-{it['id']}"
        used.add(slug)
        (SERVERS_DIR / f"{slug}.json").write_text(
            json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
    print(f"{n} files written. Skipped: {stats}")


if __name__ == "__main__":
    main(sys.argv[1])
