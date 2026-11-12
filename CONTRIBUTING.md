# Contribuer

## Règles

- Serveurs **Bedrock** uniquement (port par défaut `19132`).
- Un fichier par serveur dans `servers/`, nommé en minuscules avec des tirets : `mon-serveur.json`.
- `ip` contient uniquement l'IP ou le domaine, le port va dans `port`.
- `lang` est un code ISO 639-1 : `fr`, `en`, `es`, `pt-BR`...
- `image` : URL `https` d'une bannière ou d'un logo.
- Pas de serveur dupliqué (même `ip` et `port`), pas de contenu illégal, haineux ou trompeur.
- N'éditez pas `servers.json`, `servers.csv` ni le tableau du README : ils sont générés.

## Vérifier en local

```bash
python3 scripts/validate.py
```

## Retirer un serveur

Supprimez son fichier dans `servers/` par pull request, ou ouvrez une issue si vous êtes le propriétaire.

## Réimporter depuis le site d'origine

Voir l'en-tête de [`scripts/scrape.js`](scripts/scrape.js) puis `scripts/import_raw.py`.
