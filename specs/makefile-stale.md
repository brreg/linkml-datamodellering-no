# Stale referanse i Makefile

## Funn

### Linje 287 — utdatert kommentar i `convert-data`

```makefile
# Naming convention: data/<domain>/<name>.yaml → generated/<domain>/<name>/<name>.ttl
```

Kommentaren skildrar den gamle rot-nivå `data/`-strukturen. Den faktiske namnkonvensjonen
koden implementerer er:

```
src/linkml/<domain>/<model>/data/<catalog>/<catalog>.yaml
  → generated/<domain>/<catalog>/<catalog>.ttl
```

Sjølve koden under kommentaren (linje 292 ff.) er korrekt og matchar den faktiske strukturen.

## Tiltaksliste

| # | Linje | Endring | Prioritet |
|---|---|---|---|
| 1 | 287 | Oppdater kommentaren til å vise `src/linkml/<domain>/<model>/data/<catalog>/<catalog>.yaml` | Lav |
