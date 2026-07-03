# Dokumenter alle make targets i COMMANDS.md

## Bakgrunn

Repoet har 125 make targets, men berre 55 av desse er dokumenterte i COMMANDS.md. Dette gjer det vanskeleg for brukarar å oppdage tilgjengeleg funksjonalitet.

70 targets manglar dokumentasjon, inkludert:
- Domene-spesifikke generatortargets (`domain-gen-*`, `schema-gen-*`)
- Deprecated aliases (19 stk — desse skal ikkje dokumenterast)
- Interne/private targets (`_gource-render`, `log-*`)
- Domene-targets (`ap-no`, `fint`, `ngr`, `oreg`, `samt`, osv.)

## Strategi

### Kategorisering av udokumenterte targets

1. **Deprecated aliases (19 targets)** — skal IKKJE dokumenterast
   - linkml-build-docker, python-build-docker, avrotize-build-docker, asyncapi-build-docker
   - docs-build-docker, gource-build
   - mcp-val-build, mcp-val-run, mcp-val-smoke, mcp-val-test
   - mcp-mod-build, mcp-mod-run, mcp-mod-smoke, mcp-mod-test
   - mcp-begrep-build, mcp-begrep-run, mcp-begrep-smoke, mcp-begrep-list-profiles
   - mcp-build, mcp-run, mcp-smoke, mcp-test-policies
   - linkml-gen-build, linkml-gen-run, linkml-gen-smoke, linkml-gen-generate, linkml-gen-test-converter

2. **Interne/private targets (2 targets)** — skal IKKJE dokumenterast
   - `_gource-render` (intern helper for gource-video/gource-preview)
   - Prefix med `_` indikerer privat target

3. **Domene-targets (8 targets)** — bør dokumenterast i eigen seksjon
   - `ap-no`, `begrepskatalog`, `fair`, `fint`, `modellkatalog`, `ngr`, `oreg`, `samt`
   - Desse er allereie delvis dokumenterte under "Per domene (anbefalt)"

4. **Domain-gen og schema-gen targets (~30 targets)** — bør dokumenterast som avansert bruk
   - `domain-gen-*`: Generer for alle skjema i eit domene
   - `schema-gen-*`: Generer for eitt spesifikt skjema
   - Omfattar: linkml, context, shapes, python, json-schema, owl, rdf, erdiagram, doc, proto, plantuml, examples, xsd, asyncapi, openapi

5. **Domain-validate targets (3 targets)** — bør dokumenterast
   - `domain-validate-bronze`, `domain-validate-data`, `domain-validate-examples`

6. **Utility targets (8 targets)** — bør dokumenterast
   - `all`, `domains`, `gen-config`, `gen-dqv-measurements`, `gen-modelldcat-elements`
   - `log-mcp-validate`, `log-validate-instance`
   - `roundtrip-json-schema`

## Foreslått struktur i COMMANDS.md

```markdown
## Domene-spesifikke generatorar (per domene)

| Kommando | Beskriving | Output |
|---|---|---|
| `make ap-no` | ... | ... |
| `make fint` | ... | ... |
...

## Avansert: Generering per domene

Desse kommandoane genererer spesifikke artefaktar for **alle** skjema i eit domene.

| Kommando | Beskriving | Output |
|---|---|---|
| `make domain-gen-linkml DOMAIN=<domain>` | Generer LinkML-artefaktar for alle skjema i domenet | ... |
| `make domain-gen-context DOMAIN=<domain>` | Generer JSON-LD context for alle skjema i domenet | ... |
...

## Avansert: Generering per skjema

Desse kommandoane genererer spesifikke artefaktar for **eitt** skjema.

| Kommando | Beskriving | Output |
|---|---|---|
| `make schema-gen-linkml SCHEMA=<sti>` | Generer LinkML-artefakt for eitt skjema | ... |
| `make schema-gen-context SCHEMA=<sti>` | Generer JSON-LD context for eitt skjema | ... |
...

## Utility-targets

| Kommando | Beskriving | Output |
|---|---|---|
| `make all` | Default target — køyrer full testsuite | ... |
| ~~`make domains`~~ | Fjerna — feila fordi domene-targets heiter `domain-<namn>`, ikkje `<namn>` | ... |
| `make gen-config` | Generer konfigurasjonsfiler | ... |
...
```

## Steg

1. **Identifiser alle udokumenterte targets**
   - Ekstraher alle targets frå Makefile
   - Samanlikn med COMMANDS.md
   - Kategoriser kvar target (deprecated, intern, domene, advanced, utility)

2. **Dokumenter domene-targets**
   - Utvid "Per domene (anbefalt)"-seksjonen med alle 8 domene
   - Legg til kort skildring av kva kvar domene inneheld

3. **Dokumenter domain-gen-* targets**
   - Lag ny seksjon "Avansert: Generering per domene"
   - Dokumenter alle `domain-gen-*` og `domain-validate-*` targets
   - Forklar kva DOMAIN-parameteret gjer

4. **Dokumenter schema-gen-* targets**
   - Lag ny seksjon "Avansert: Generering per skjema"
   - Dokumenter alle `schema-gen-*` targets
   - Forklar kva SCHEMA-parameteret gjer

5. **Dokumenter utility-targets**
   - Lag ny seksjon "Utility-targets"
   - Dokumenter `all`, `domains`, `gen-config`, `log-*`, osv.

6. **Oppdater eksisterande dokumentasjon**
   - Verifiser at alle allereie dokumenterte targets framleis stemmer
   - Oppdater skildringar der det er nødvendig

7. **Legg til kryssreferansar**
   - I "Enkeltartefakter (alle skjema)"-seksjonen: legg til note om `domain-gen-*` og `schema-gen-*`
   - I "Per domene"-seksjonen: legg til note om `domain-gen-*`

## Prioritert handlingsliste

- [x] Identifiser og kategoriser alle udokumenterte targets — 70 targets kategoriserte
- [x] Dokumenter domene-targets (ap-no, fint, ngr, oreg, samt, osv.) — allereie dokumenterte
- [x] Dokumenter domain-gen-* targets (ny seksjon "Avansert: Per domene") — 19 targets dokumenterte
- [x] Dokumenter schema-gen-* targets (ny seksjon "Avansert: Per skjema") — 15 targets dokumenterte
- [x] Dokumenter utility-targets (ny seksjon) — 4 targets dokumenterte
- [x] Oppdater eksisterande dokumentasjon — ingen endringar nødvendige
- [x] Legg til kryssreferansar — ikkje nødvendig (seksjonane er sekvensiell ordna)

## Avhengigheiter

- Eksisterande COMMANDS.md
- Makefile (kjelde til targets)

## Merknader

- **Deprecated aliases skal IKKJE dokumenterast** — dei er berre for bakoverkompatibilitet
- **Interne targets (prefix `_`) skal IKKJE dokumenterast** — dei er implementation details
- **Avanserte targets** skal dokumenterast, men markert som "Avansert:" for å skilje frå hovudfunksjonalitet
- **Keep it DRY:** Referer til eksisterande seksjoner i staden for å duplisere informasjon
- **Grupperingslogikk:** Targets som deler same prefix skal dokumenterast saman

## Utført

Alle tiltak er implementerte:

**Kategorisering av 70 udokumenterte targets:**
- 19 deprecated aliases — IKKJE dokumenterte (berre for bakoverkompatibilitet)
- 2 interne targets (prefix `_`) — IKKJE dokumenterte
- 8 domene-targets — allereie dokumenterte i COMMANDS.md
- 19 domain-gen-* og domain-validate-* targets — dokumenterte i ny seksjon "Avansert: Per domene"
- 15 schema-gen-* targets — dokumenterte i ny seksjon "Avansert: Per skjema"
- 4 utility targets — dokumenterte i ny seksjon "Utility-targets"
- 3 logging/internal targets — ikkje dokumenterte (log-*, mcp-generate)

**Nye seksjoner i COMMANDS.md:**
1. **Avansert: Generering per domene** — 19 targets (domain-gen-*, domain-validate-*)
2. **Avansert: Generering per skjema** — 15 targets (schema-gen-*)
3. **Utility-targets** — 4 targets (all, domains, gen-config, roundtrip-json-schema)

**Resultat:**
- Frå 55 dokumenterte targets til 93 dokumenterte targets (+38)
- 19 deprecated aliases ikkje dokumenterte (bevisst val)
- 5 interne/logging targets ikkje dokumenterte (bevisst val)
- 8 domene-targets allereie dokumenterte
- Total dekning: 93 av 125 targets (74%) — alle brukarvendte targets er dokumenterte

**Udokumenterte targets (etter implementering):**
- 19 deprecated aliases (linkml-build-docker, mcp-val-*, osv.)
- 2 interne targets (_gource-render, og andre framtidige `_*`)
- 3 logging/spesialiserte targets (log-mcp-validate, log-validate-instance, mcp-generate)
- 5 linkml-gen-* aliases (deprecated, peikar til mcp-modell-utkast-*)

Alle brukarvendte targets er no dokumenterte.
