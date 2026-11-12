"""Fonctions communes : chargement et validation des fichiers serveurs."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVERS_DIR = ROOT / "servers"
SCHEMA_PATH = ROOT / "schema" / "server.schema.json"

ALLOWED = {
    "name", "ip", "port", "description", "lang", "image",
    "country", "version", "website", "discord", "tags", "source",
}
REQUIRED = ["name", "ip", "port", "description", "lang"]
LANG_RE = re.compile(r"^[a-z]{2}(-[A-Z]{2})?$")
HOST_RE = re.compile(r"^[A-Za-z0-9]([A-Za-z0-9.\-_]*[A-Za-z0-9])?$|^[0-9a-fA-F:]+$")


def load_all():
    servers = []
    for path in sorted(SERVERS_DIR.glob("*.json")):
        with path.open(encoding="utf-8") as f:
            servers.append((path, json.load(f)))
    return servers


def validate(path, data):
    """Retourne la liste des erreurs pour un serveur (liste vide = OK)."""
    errs = []
    if not isinstance(data, dict):
        return ["le fichier doit contenir un objet JSON"]
    for key in REQUIRED:
        if key not in data or data[key] in ("", None):
            errs.append(f"champ obligatoire manquant : {key}")
    for key in data:
        if key not in ALLOWED:
            errs.append(f"champ inconnu : {key}")
    if "name" in data and not (isinstance(data["name"], str) and 1 <= len(data["name"]) <= 100):
        errs.append("name : texte de 1 a 100 caracteres")
    ip = data.get("ip")
    if ip is not None and (not isinstance(ip, str) or not HOST_RE.match(ip) or ":" in ip and not re.fullmatch(r"[0-9a-fA-F:]+", ip)):
        errs.append("ip : IP ou domaine uniquement (le port va dans le champ port)")
    port = data.get("port")
    if port is not None and (not isinstance(port, int) or isinstance(port, bool) or not 1 <= port <= 65535):
        errs.append("port : entier entre 1 et 65535")
    if isinstance(data.get("description"), str) and len(data["description"]) > 2000:
        errs.append("description : 2000 caracteres maximum")
    lang = data.get("lang")
    if lang is not None and (not isinstance(lang, str) or not LANG_RE.match(lang)):
        errs.append("lang : code ISO 639-1, ex. fr, en, pt-BR")
    for key in ("image", "website", "discord", "source"):
        v = data.get(key)
        if v not in (None, "") and not (isinstance(v, str) and v.startswith(("http://", "https://"))):
            errs.append(f"{key} : doit etre une URL http(s)")
    tags = data.get("tags")
    if tags is not None and not (isinstance(tags, list) and all(isinstance(t, str) for t in tags) and len(set(tags)) == len(tags)):
        errs.append("tags : liste de textes sans doublon")
    expected = path.stem
    if not re.fullmatch(r"[a-z0-9][a-z0-9\-]*", expected):
        errs.append("nom de fichier : minuscules, chiffres et tirets uniquement (ex. mon-serveur.json)")
    return errs


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)
