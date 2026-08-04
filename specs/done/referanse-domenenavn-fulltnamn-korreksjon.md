# Korriger REF → REFERANSE (fullt katalognamn) i domenevising

## Bakgrunn

Følgjer opp `specs/done/referanse-nav-omdoyping.md` og
`specs/done/skjema-tabell-domene-uppercase.md`, som innførte forkortinga `REF`
for referanse-domenet (NAV-meny: "REF - Referansemodeller"; Domener-tabell og
Skjema-tabell i README.md: `[REF]`).

Brukar ombestemte seg: ønskjer **direkte bruk av katalognamnet**
(`REFERANSE`, uppercase av mappenamnet `referanse`) i staden for forkortinga
`REF`, konsekvent med korleis alle andre domene alt vert viste (uppercase av
mappenamn, ingen forkorting). I NAV-menyen skal teksten vere
"REFERANSE - Referansemodellar" (nynorsk plural, jf. skriftspråk-konvensjonen
for mkdocs-portalen — retta frå den tidlegare bokmål-forma "Referansemodeller").

## Steg

### 1. `mkdocs/lib/utils/formatters.sh`

Endre `domain_label()`-casen for `referanse` frå
`"REF - Referansemodeller"` til `"REFERANSE - Referansemodellar"`.

### 2. `README.md` — Domener-tabellen

Endre lenkjetekst frå `[REF](referanse/)` til `[REFERANSE](referanse/)`.

### 3. `src/assets/scripts/makefile/generate-readme-tables.sh` — Skjema-tabellen

`domain_short_label()` hadde eit eige case for `referanse) echo "REF" ;;`.
Sidan ønskt visingsnamn no er identisk med standard-uppercase-oppførselen
(`REFERANSE`), er spesialtilfellet overflødig — fjerna heilt, funksjonen er no
ei rein uppercase-transformasjon for alle domene.

### 4. Regenerer README.md

```bash
./src/assets/scripts/makefile/generate-readme-tables.sh README.md
```

## Handlingsliste

- [x] Oppdater `domain_label()` i `formatters.sh`
- [x] Oppdater Domener-tabellen i README.md
- [x] Fjern `referanse`-spesialtilfellet i `domain_short_label()`
- [x] Regenerer README.md og verifiser Skjema-tabellen

## Utført

- `mkdocs/lib/utils/formatters.sh`: `domain_label()` for referanse endra til `"REFERANSE - Referansemodellar"`
- `README.md`: Domener-tabellen sitt `[REF]` endra til `[REFERANSE]`; Skjema-tabellen regenerert med `REFERANSE` for referansemodell-radene
- `src/assets/scripts/makefile/generate-readme-tables.sh`: fjerna `referanse`-spesialtilfellet i `domain_short_label()` — funksjonen er no rein uppercase for alle domene
