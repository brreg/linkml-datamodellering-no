# Plan: dokumenter description.md for domenemodell

## Mål

`src/linkml/<domene>/<modell>/description.md` er ei valfri fil som vert
injisert i dokumentasjonsportalen sin `index.md` for skjemaet. Fila er
ikkje nemnt i rettleiingane og er ukjend for nye bidragsytarar.

## Kva fila er og gjer

- **Plassering**: `src/linkml/<domene>/<modell>/description.md` (ved sida av skjemafila)
- **Innhald**: fri Markdown — formål, avgrensing, kontekst, lenker til kjelder
- **Effekt i portalen**: innhaldet vert sett inn i skjema-`index.md` etter
  ER-diagrammet og før klasselista (`publish.sh` `process_schema`-funksjonen,
  linje ~130)
- **Valfri**: manglar fila, skjer ingenting
- **Skriftspråk**: norsk bokmål (same som skjemaet)

## Tiltak

### Tiltak 1 — Legg til avsnitt i `mkdocs/docs/ny-domenemodell.md`

Legg til eit nytt avsnitt **"Legg til skjemaskildring"** etter Steg 1 (Scaffold)
og før Steg 2 (Rediger skjemaet), eller som eige avsnitt under "Tilpass portaldokumentasjonen":

```markdown
## Skjemaskildring (valfri)

Legg til ei `description.md`-fil ved sida av skjemafila for å vise ein
innleiingstekst i portalen:

```
src/linkml/<domene>/<modell>/
└── description.md    ← valfri, injiserast i portal-index etter ER-diagrammet
```

Fila er vanleg Markdown og kan innehalde formålstekst, avgrensingar,
lenkjer til kjelder og anna kontekstuell informasjon. Innhaldet visast
mellom ER-diagrammet og klasselista på skjemaet si portalside.

**Eksempel** (`src/linkml/oreg/register-over-aksjeeiere/description.md`):
> Dette er ein tidleg, førebels overordna forretningsobjektmodell over
> domenet register over aksjeeiere …
```

### Tiltak 2 — Legg til i CLAUDE.md under katalogstruktur

I CLAUDE.md, katalogstruktur-tabellen:

```
src/linkml/
  <domene>/
    <modell>/
      <modell>-schema.yaml
      manifest.yaml
      description.md            ← valfri portaltekst (Markdown, bokmål)
      examples/
```

### Tiltak 3 — Vurder stub i `make new-model`

`make new-model` oppretter scaffold utan `description.md`. Vurder om
scaffolden skal opprette ei tom/stub-fil:

```bash
# src/linkml/<domene>/<modell>/description.md
## Beskriv formål, avgrensing og kontekst for <modell>.
```

Fordel: gjer fila synleg for nye modelleigarar.
Ulempe: legg til ein ekstra fil som mange aldri fyller ut.

**Tilråding**: legg til stub i scaffolden — det er lettare å slette ei tom
fil enn å oppdage at funksjonen finst.

## Prioritet og omfang

| Tiltak | Fil | Prioritet |
|---|---|---|
| Tiltak 1 | `mkdocs/docs/ny-domenemodell.md` | Høg |
| Tiltak 2 | `CLAUDE.md` | Høg |
| Tiltak 3 | `Makefile` (scaffold-mal) | Medium |
