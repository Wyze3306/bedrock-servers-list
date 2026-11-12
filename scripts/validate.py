#!/usr/bin/env python3
"""Valide tous les fichiers servers/*.json. Utilise par la CI sur chaque pull request."""
import json
import sys

from common import load_all, validate, SERVERS_DIR


def main():
    bad = 0
    seen = {}
    try:
        servers = load_all()
    except json.JSONDecodeError as e:
        print(f"JSON invalide : {e}")
        return 1
    for path, data in servers:
        errs = validate(path, data)
        if not errs and isinstance(data.get("port"), int):
            key = (data["ip"].lower(), data["port"])
            if key in seen:
                errs.append(f"doublon : meme ip:port que {seen[key]}")
            seen[key] = path.name
        for e in errs:
            print(f"::error file=servers/{path.name}::{e}")
            print(f"{path.name}: {e}")
        bad += bool(errs)
    print(f"{len(servers)} serveurs verifies, {bad} fichier(s) en erreur")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
