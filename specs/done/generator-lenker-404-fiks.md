# Fiks 404 på Generator-kolonne-lenker til COMMANDS.md

## Bakgrunn

Generator-kolonnene i tabellane "Genererte artefakter", "Genererte
begrepskatalogar" og "Genererte modellkatalogar" i README.md lenkjer til
`COMMANDS.md#enkeltartefakter` / `COMMANDS.md#vedlikehald` (relativ sti,
seksjonsanker).

**To problem:**

1. **404 på publisert portal:** `mkdocs/publish.sh` (Steg 3) kopierer README.md
   til `docs/index.md` nesten uendra — men `COMMANDS.md` vert aldri kopiert til
   `docs/`. Relative lenker til `COMMANDS.md` finn difor ingen fil på
   `https://brreg.github.io/linkml-datamodellering-no/` og gir 404. (På GitHub
   sjølv fungerer relativ lenkje frå README.md, sidan begge filene ligg i
   repo-rota — problemet syner seg berre på portalen.)
2. **Feil/upresist anker:** Dei fleste radene peikar til det generiske
   seksjonsankeret `#enkeltartefakter` eller `#vedlikehald` i staden for det
   konkrete kommandoankeret. COMMANDS.md har alt eksplisitte
   `<a id="gen-jsonld-context">`-ankerpunkt per kommando (linje 146-176) — desse
   vert ikkje brukte.

**Løysing:** Same mønster som alt brukt for `SCOPE.md`/`BUGS.md`/`PRINCIPLES.md`
andre stader i README.md — absolutt GitHub blob-URL
(`https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#<anker>`)
med det konkrete per-kommando-ankeret.

## Steg

### 1. README.md — "Genererte artefakter"-tabellen (manuelt vedlikehalden, linje 235-251)

Erstatt kvar `COMMANDS.md#enkeltartefakter` / `COMMANDS.md#vedlikehald` med
`https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#<kommando>`,
der `<kommando>` er kommandoen sjølv (t.d. `gen-jsonld-context`,
`gen-informasjonsmodell-instance`).

### 2. `generate-readme-tables.sh` — begrepskatalog- og modellkatalog-tabellane

Linje 127 og 159: erstatt
`[\`gen-begrepskatalog-instance\`](COMMANDS.md#vedlikehald)` og
`[\`gen-modellkatalog-instance\`](COMMANDS.md#vedlikehald)` med tilsvarande
absolutt URL + konkret anker
(`#gen-begrepskatalog-instance` / `#gen-modellkatalog-instance`).

### 3. Regenerer README.md

```bash
./src/assets/scripts/makefile/generate-readme-tables.sh README.md
```

## Handlingsliste

- [x] Rett Generator-kolonna i "Genererte artefakter"-tabellen i README.md
- [x] Rett `generate-readme-tables.sh` (begrepskatalog + modellkatalog)
- [x] Regenerer README.md og verifiser at alle Generator-lenker peikar til absolutt URL med korrekt anker

## Utført

- `README.md`: alle 16 Generator-lenker i "Genererte artefakter"-tabellen endra til absolutt GitHub-URL med konkret per-kommando-anker
- `src/assets/scripts/makefile/generate-readme-tables.sh`: `generate_begrepskatalog_table()` og `generate_modellkatalog_table()` brukar no absolutt URL med konkret anker
- README.md regenerert — begrepskatalog-/modellkatalog-tabellane oppdaterte
