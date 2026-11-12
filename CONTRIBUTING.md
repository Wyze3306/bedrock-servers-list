# Contributing

## Rules

- **Bedrock** servers only, on the default port `19132`.
- `ip` is a **domain name** (e.g. `play.example.com`). Numeric IP addresses are not accepted, and the port is not part of it.
- `name` is the clean server name only: no version numbers, no Discord link, no emojis or decorative symbols, no slogan (`Linesia`, not `★ LINESIA ★ 1.21 | discord.gg/xyz`). When in doubt, use the name from the domain.
- One file per server in `servers/`, named in lowercase with dashes: `my-server.json`.
- `lang` is an ISO 639-1 code: `en`, `fr`, `es`, `pt-BR`... It is the language of the `description`.
- `image` is an `https` URL of a banner or logo.
- No duplicate servers (same `ip`), no illegal, hateful or misleading content.
- Do not edit `servers.json`, `servers.csv` or the README table: they are generated.

## Check locally

```bash
python3 scripts/validate.py
```

## Remove a server

Delete its file from `servers/` in a pull request, or open an issue if you are the owner.

## Re-import from the original site

See the header of [`scripts/scrape.js`](scripts/scrape.js), then run `scripts/import_raw.py` and `scripts/build.py`.
