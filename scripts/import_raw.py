#!/usr/bin/env python3
"""Convertit le dump brut de scripts/scrape.js en fichiers servers/<slug>.json.

Usage : python3 scripts/import_raw.py raw.json

La langue n'existe pas sur le site source : elle est deduite de la description
(mots courants) puis, a defaut, du pays du serveur. Elle reste modifiable par PR.
"""
import json
import re
import sys
import unicodedata

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


def detect_lang(text, country):
    t = text.lower()
    if re.search(r"[぀-ヿ]", t): return "ja"
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
    used, seen_addr, n, skipped = set(), set(), 0, 0
    for it in sorted(items, key=lambda x: int(x["id"])):
        ip, port = split_address(it.get("address", ""))
        if not ip or " " in ip:  # ex. "Private Server" : pas d'adresse publique
            skipped += 1
            continue
        it["name"] = (it.get("name") or ip).strip()[:100].rstrip()
        if (ip.lower(), port) in seen_addr:
            skipped += 1
            continue
        seen_addr.add((ip.lower(), port))
        desc = it.get("description", "").strip()
        d = {
            "name": it["name"], "ip": ip, "port": port,
            "description": desc or "Aucune description.",
            "lang": detect_lang(desc, it.get("country", "")),
        }
        if it.get("banner"): d["image"] = it["banner"]
        if it.get("country"): d["country"] = it["country"]
        if it.get("version"): d["version"] = it["version"]
        if it.get("website", "").startswith("http"): d["website"] = it["website"]
        if it.get("discord", "").startswith("http"): d["discord"] = it["discord"]
        if it.get("tags"): d["tags"] = it["tags"]
        d["source"] = f"https://minecraftpocket-servers.com/server/{it['id']}/"
        slug = slugify(it["name"]) or slugify(ip) or f"server-{it['id']}"
        if slug in used:
            slug = f"{slug}-{it['id']}"
        used.add(slug)
        (SERVERS_DIR / f"{slug}.json").write_text(
            json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
    print(f"{n} fichiers ecrits, {skipped} ignores (doublon ip:port ou donnees vides)")


if __name__ == "__main__":
    main(sys.argv[1])
