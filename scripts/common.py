"""Shared helpers: loading and validating server files."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVERS_DIR = ROOT / "servers"
SCHEMA_PATH = ROOT / "schema" / "server.schema.json"

DEFAULT_PORT = 19132
ALLOWED = {
    "name", "ip", "port", "description", "lang", "image", "logo", "cover",
    "gallery", "country", "version", "website", "discord", "tags", "source",
}
REQUIRED = ["name", "ip", "port", "description", "lang"]
LANG_RE = re.compile(r"^[a-z]{2}(-[A-Z]{2})?$")
HOST_RE = re.compile(r"^[A-Za-z0-9]([A-Za-z0-9.\-_]*[A-Za-z0-9])?$")
IPV4_RE = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")


def load_all():
    servers = []
    for path in sorted(SERVERS_DIR.glob("*.json")):
        with path.open(encoding="utf-8") as f:
            servers.append((path, json.load(f)))
    return servers


def validate(path, data):
    """Return the list of errors for one server (empty list = valid)."""
    errs = []
    if not isinstance(data, dict):
        return ["the file must contain a JSON object"]
    for key in REQUIRED:
        if key not in data or data[key] in ("", None):
            errs.append(f"missing required field: {key}")
    for key in data:
        if key not in ALLOWED:
            errs.append(f"unknown field: {key}")
    if "name" in data and not (isinstance(data["name"], str) and 1 <= len(data["name"]) <= 100):
        errs.append("name: text of 1 to 100 characters")
    ip = data.get("ip")
    if ip is not None:
        if not isinstance(ip, str) or not HOST_RE.match(ip):
            errs.append("ip: domain name only, without the port")
        elif IPV4_RE.match(ip) or ":" in ip:
            errs.append("ip: numeric IP addresses are not accepted, use a domain name")
        elif "." not in ip:
            errs.append("ip: must be a fully qualified domain name (e.g. play.example.com)")
    port = data.get("port")
    if port is not None and port != DEFAULT_PORT:
        errs.append(f"port: only the default Bedrock port {DEFAULT_PORT} is accepted")
    if isinstance(data.get("description"), str) and len(data["description"]) > 2000:
        errs.append("description: 2000 characters maximum")
    lang = data.get("lang")
    if lang is not None and (not isinstance(lang, str) or not LANG_RE.match(lang)):
        errs.append("lang: ISO 639-1 code, e.g. en, fr, pt-BR")
    for key in ("image", "logo", "cover", "website", "discord", "source"):
        v = data.get(key)
        if v not in (None, "") and not (isinstance(v, str) and v.startswith(("http://", "https://"))):
            errs.append(f"{key}: must be an http(s) URL")
    gallery = data.get("gallery")
    if gallery is not None and not (
            isinstance(gallery, list) and len(gallery) <= 4
            and all(isinstance(u, str) and u.startswith(("http://", "https://"))
                    for u in gallery)):
        errs.append("gallery: list of at most 4 http(s) URLs")
    tags = data.get("tags")
    if tags is not None and not (isinstance(tags, list) and all(isinstance(t, str) for t in tags) and len(set(tags)) == len(tags)):
        errs.append("tags: list of unique strings")
    if not re.fullmatch(r"[a-z0-9][a-z0-9\-]*", path.stem):
        errs.append("file name: lowercase letters, digits and dashes only (e.g. my-server.json)")
    return errs


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)
