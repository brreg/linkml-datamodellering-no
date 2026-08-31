# Sanering av `enhetsregisteret-bvrinn`/`enhetsregisteret-bvrinnfelles`-duplikatet

## Bakgrunn

Under arbeidet med
`specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md` (analyse
av BR-katalogar for felles-modellar i `oreg`-domenet) vart det avdekt at
`src/linkml/oreg/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml`
og
`src/linkml/oreg/enhetsregisteret-bvrinnfelles/enhetsregisteret-bvrinnfelles-schema.yaml`
er praktisk tala identiske — eit DRY-brot heilt uavhengig av BR-katalogane
(som den nemnde specen elles handlar om). Brukaren bad (avklaring
31.08.2026, punkt 8) om at saneringa av dette vert handtert som eit eige,
sjølvstendig tiltak.

## Funn

`diff` mellom dei to skjemaa (2091 vs. 2087 linjer) gjev 794 linjer
skilnad, men nesten utelukkande metadata:

- `id`: `https://data.norge.no/oreg/enhetsregisteret-bvrinn` vs.
  `.../enhetsregisteret-bvrinnfelles`
- `version`: `"1.1.2"` (bvrinn) vs. `0.1.0` (bvrinnfelles)
- `title`: bvrinn har ein reell tittel («Enhetsregisteret - BVINN»);
  bvrinnfelles har framleis `'TODO: tittel for enhetsregisteret-bvrinnfelles'`
- `description`: bvrinn har reelt innhald; bvrinnfelles har
  `Generert modell for 'enhetsregisteret_bvrinnfelles'.`
- `endringsdato`/`utgivelsesdato`: ulike datoar
- Prefiks-namn (`enhetsregisteret_bvrinn:` vs. `enhetsregisteret_bvrinnfelles:`)
  gjennomgåande i `class_uri`/`slot_usage`
- `bvrinn` har ein `subsets:`-blokk (`Obligatorisk`/`Anbefalt`/`Valgfri`)
  som `bvrinnfelles` manglar
- `bvrinnfelles` har eit ekstra, ubrukt import:
  `# TODO: endre/legg til imports etter behov` til `dcat-ap-no-schema`
  (jf. `specs/backlog/del-opp-ap-no-profilar-i-moduler.md`, Alternativ 5,
  som alt listar `bvrinnfelles` mellom skjema med denne TODO-en att frå
  `new-modell.sh`-scaffoldinga)

**Alle** 28 lokale `types:`-oppføringar og alle ~38 `classes:`-oppføringane
(klassenamn, felt, `slot_usage`) er bokstaveleg tala like mellom dei to
skjemaa. **Ingen av dei to importerer den andre** — dei er to heilt
sjølvstendige, parallelle kopiar.

**Sannsynleg årsak:** `bvrinnfelles` sin `title`/`description`/`version`
(alle framleis placeholder/TODO-tilstand) tyder på at han vart oppretta
via `make new-modell`-scaffoldinga (truleg med `JSON_SCHEMA=` peika til
ein av dei tidlegare-konverterte JSON Schema-filene i `src/tmp/`,
t.d. `bvrinnfelles_lm_v1.schema.json`) og aldri vart ferdigstilt eller
rekonsiliert med den eksisterande, hand-vedlikehaldne `bvrinn`.

## Vurdering

Dette er det klaraste DRY-brotet i heile `oreg`-domenet — éin komplett,
2000-linjers domenemodell duplisert byte-for-byte. Løysinga er **ikkje**
eit felles-import (slik BR-katalog-typane i søster-specen), men eit val
mellom:

**Alternativ A — slett `bvrinnfelles` heilt.** Dersom `bvrinnfelles` ikkje
har nokon kjende konsumentar (ingen andre skjema importerer han, jf.
`grep -rl enhetsregisteret-bvrinnfelles src/linkml/`), og han berre er eit
restprodukt frå scaffolding, er dette den enklaste og tryggaste løysinga.

**Alternativ B — la `bvrinnfelles` importere `bvrinn`.** Dersom
`bvrinnfelles` er meint å vere eit avgrensa/anna-forma uttrykk for same
domenemodell (t.d. eit undersnitt brukt av eit anna system), bør han
importere `bvrinn` og berre halde på det som faktisk skil dei to, i staden
for å duplisere heile klassesettet.

**Alternativ C — slå saman til éin, og la den andre bli ein alias/redirect.**
Mindre aktuelt gitt at begge har eigne `id`/`class_uri`-namnerom som alt
kan vere i bruk eksternt.

**Tilråding:** start med å avklare bruken av `bvrinnfelles` (§ Nummererte
steg, steg 1) — dette avgjer om alternativ A eller B er riktig. Handlingslista
under føreset at svaret avgjer valet; begge alternativa sine konkrete steg
er skisserte.

## Nummererte steg

1. **Avklar med brukaren:** har `enhetsregisteret-bvrinnfelles` nokon
   kjend bruk/konsument i dag (t.d. eit anna system, ein publisert URI som
   alt er teken i bruk), eller er han eit ufullført scaffolding-resultat
   som trygt kan fjernast? Sjekk òg om `git log` for skjemaet gjev kontekst
   (commit-melding frå då han vart oppretta).
2. **Dersom «ingen kjend bruk» (truleg, jf. TODO-tilstanden):**
   - Slett `src/linkml/oreg/enhetsregisteret-bvrinnfelles/`-katalogen.
   - Sjekk `CODEOWNERS.md`/`.github/CODEOWNERS` for referansar til stien
     og fjern dei.
   - Sjekk `.github/release-please-manifest.json` for ein eksisterande
     versjonsoppføring for `bvrinnfelles` og fjern han om nødvendig
     (samrå med release-please-dokumentasjonen for korrekt framgangsmåte
     — ikkje slett manuelt utan å forstå konsekvensen for tag-historikk).
   - Køyr `make lint`/full generatorpipeline for å stadfeste at ingenting
     anna refererer til `enhetsregisteret_bvrinnfelles`-prefikset.
3. **Dersom «reell bruk finst»:** omformer `bvrinnfelles` til å importere
   `bvrinn` (versjonslåst, jf. `mkdocs/docs/arkitektur/importhierarki.md`
   § «Import på tvers av domenemodellar») og fjern alle duplikate
   klasse-/typedefinisjonar — behald berre det som faktisk skil dei to
   skjemaa. Oppdater `title`/`description`/`version` til reelle verdiar.
4. **Etter gjennomføring:** oppdater denne specen sin «Utført»-seksjon,
   generer commit-melding, og flytt specen til `specs/done/`.

## Akseptansekriterium

- `enhetsregisteret-bvrinnfelles` eksisterer anten ikkje lenger (alternativ
  A), eller importerer `enhetsregisteret-bvrinn` utan duplikate
  klasse-/typedefinisjonar (alternativ B) — verifiserbart med
  `diff`/`grep` mot dagens tilstand.
- `make lint` og full generatorpipeline køyrer grønt for det attverande
  skjemaet/skjemaa.
- Ingen `# TODO`-restar frå scaffolding attende i det attverande skjemaet.

## Relaterte filer

- `src/linkml/oreg/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml`
- `src/linkml/oreg/enhetsregisteret-bvrinnfelles/enhetsregisteret-bvrinnfelles-schema.yaml`
- `specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md` — Funn
  1, der duplikatet opphavleg vart avdekt
- `specs/backlog/del-opp-ap-no-profilar-i-moduler.md` — Alternativ 5,
  dokumenterer TODO-import-scaffoldinga som truleg er årsaka
- `src/assets/scripts/scaffolding/new-modell.sh` — scaffoldinga som truleg
  produserte `bvrinnfelles`
