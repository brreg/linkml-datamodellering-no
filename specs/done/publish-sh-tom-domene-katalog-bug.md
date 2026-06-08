# Bug: publish.sh slettar domeneinnhald når generated/<domene>/ er tom

## Symptom

`src/linkml/begrepskatalog/brreg-begrepskatalog/description.md` vert ikkje
inkludert i dokumentasjonsportalen etter at ein køyrer `make publish` lokalt.
Heile `begrepskatalog`-seksjonen forsvinn frå portalen.

## Rotårsak

To relaterte problem samverkar:

### Problem 1 — stale lokal `generated/`-tilstand etter domenenamn-endring

Commit `35647cd9` omdøypte domenekatalogane:

- `src/linkml/begrep/` → `src/linkml/begrepskatalog/`
- `src/linkml/modell/` → `src/linkml/modellkatalog/`

Lokale `generated/`-artefakter (som ligg i `.gitignore`) er ikkje automatisk
oppdaterte ved ei slik namneending. Resultatet er:

```
generated/
├── begrep/                     ← gammalt namn, innhald frå før omdøyping
│   └── brreg-begrep/
├── begrepskatalog/             ← nytt namn, TOM (ingen skjema-underkatalogar)
├── modell/                     ← gammalt namn, innhald frå før omdøyping
│   └── brreg-modelkatalog/
└── modellkatalog/              ← nytt namn, TOM
```

### Problem 2 — publish.sh slettar docs for tomme domene

`publish.sh` Steg 1 (`mkdocs/publish.sh` linje ~200-205) itererer over **alle**
katalogar i `generated/`, inkludert tomme:

```bash
for domain_dir in "$GEN"/*/; do
    [ -d "$domain_dir" ] || continue
    domain=$(basename "$domain_dir")
    find "${DOCS}/${domain}" -mindepth 1 -depth -delete 2>/dev/null || true
    rmdir "${DOCS}/${domain}" 2>/dev/null || true
done
```

Sidan `generated/begrepskatalog/` eksisterer (men er tom), vert
`mkdocs/docs/begrepskatalog/` sletta. I Steg 2 vert ingen ny innhald generert
for `begrepskatalog` (ingen skjema-underkatalogar finst). Portalen manglar då
heile seksjonen — description.md vert aldri lesen.

## Kvifor opptrer det no

Brukaren køyrde `make publish` lokalt etter å ha lagt til
`src/linkml/oreg/register-over-aksjeeiere/description.md`. Dette var den første
lokale `make publish`-køyringa etter at Problem 1 oppstod. CI-portalen viser
ikkje feilen fordi CI alltid genererer alle domene frå scratch.

## Tiltak

### Tiltak 1 — Lokal korttidsfiksing (køyr no)

Regenerer `begrepskatalog` og `modellkatalog` lokalt, og rydd opp stale
katalogar:

```bash
make begrepskatalog
make modellkatalog
rm -rf generated/begrep generated/modell
make publish
```

### Tiltak 2 — Langtidsfiksing i publish.sh (krev endring)

Legg til guard i Steg 1 som hoppar over domenekatalogane utan
skjema-underkatalogar:

```bash
# Steg 1: Rens tidlegare genererte domene-katalogar frå docs/
for domain_dir in "$GEN"/*/; do
    [ -d "$domain_dir" ] || continue
    # Hopp over tomme domene-katalogar (ingen skjema-underkatalogar)
    schema_count=$(find "$domain_dir" -mindepth 1 -maxdepth 1 -type d | wc -l)
    [ "$schema_count" -eq 0 ] && continue
    domain=$(basename "$domain_dir")
    find "${DOCS}/${domain}" -mindepth 1 -depth -delete 2>/dev/null || true
    rmdir "${DOCS}/${domain}" 2>/dev/null || true
done
```

Dette sikrar at ein delvis `generated/`-katalog (t.d. etter `make oreg` utan å
ha regenerert alle domene) ikkje fjernar portal-innhald for domene som ikkje
vart rørt.

### Tiltak 3 — Vurder åtvaring i publish.sh for ukjende domene

Vurder å logge ei åtvaring dersom `generated/<domene>/` inneheld innhald men
`src/linkml/<domene>/` ikkje finst — dette indikerer ein stale artifact frå eit
omdøypt domene:

```bash
if [ ! -d "$REPO_ROOT/src/linkml/$domain" ]; then
    echo "ÅTVARING: $domain finst i generated/ men ikkje i src/linkml/ — stale artefakter?" >&2
fi
```

## Prioritering

| Tiltak | Prioritet | Kompleksitet |
|---|---|---|
| Tiltak 1 (lokal rydding) | Høg — blokkerer lokal utvikling | Låg |
| Tiltak 2 (publish.sh guard) | Medium — førebyggjer gjentak | Låg |
| Tiltak 3 (åtvaring) | Låg — nytteverdi ved neste rename | Låg |
