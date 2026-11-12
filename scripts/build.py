#!/usr/bin/env python3
"""Generate servers.json, servers.csv and the README table from servers/*.json."""
import csv
import json
import re
from collections import Counter

from common import ROOT, load_all

START, END = "<!-- SERVERS:START -->", "<!-- SERVERS:END -->"


def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def main():
    rows = []
    for path, d in load_all():
        rows.append({
            "id": path.stem,
            "name": d["name"], "ip": d["ip"], "port": d["port"], "lang": d["lang"],
            "description": d["description"], "image": d.get("image", ""),
            "country": d.get("country", ""), "version": d.get("version", ""),
            "website": d.get("website", ""), "discord": d.get("discord", ""),
            "tags": d.get("tags", []), "source": d.get("source", ""),
        })
    rows.sort(key=lambda r: r["name"].lower())

    (ROOT / "servers.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with (ROOT / "servers.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["name", "ip", "port", "lang", "country", "version", "tags", "website", "discord", "image", "description"])
        for r in rows:
            w.writerow([r["name"], r["ip"], r["port"], r["lang"], r["country"], r["version"],
                        ";".join(r["tags"]), r["website"], r["discord"], r["image"],
                        r["description"].replace("\n", " ")])

    langs = Counter(r["lang"] for r in rows)
    lines = [f"**{len(rows)} servers** · languages: " +
             ", ".join(f"`{l}` {n}" for l, n in langs.most_common(12)), "",
             "| Server | IP | Port | Lang | Description |",
             "|---|---|---|---|---|"]
    for r in rows:
        name = f"[{esc(r['name'])}]({r['website']})" if r["website"] else esc(r["name"])
        desc = esc(r["description"])
        desc = desc[:117] + "..." if len(desc) > 120 else desc
        lines.append(f"| {name} | `{r['ip']}` | `{r['port']}` | {r['lang']} | {desc} |")
    block = START + "\n" + "\n".join(lines) + "\n" + END

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if START in readme:
        readme = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, readme, flags=re.S)
    else:
        readme = readme.rstrip() + "\n\n" + block + "\n"
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(f"{len(rows)} servers written")


if __name__ == "__main__":
    main()
