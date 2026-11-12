#!/usr/bin/env python3
"""Validate every servers/*.json file. Run by the CI on each pull request."""
import json
import sys

from common import load_all, validate


def main():
    bad = 0
    seen = {}
    try:
        servers = load_all()
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return 1
    for path, data in servers:
        errs = validate(path, data)
        if not errs:
            key = (data["ip"].lower(), data["port"])
            if key in seen:
                errs.append(f"duplicate: same ip:port as {seen[key]}")
            seen[key] = path.name
        for e in errs:
            print(f"::error file=servers/{path.name}::{e}")
            print(f"{path.name}: {e}")
        bad += bool(errs)
    print(f"{len(servers)} servers checked, {bad} file(s) with errors")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
