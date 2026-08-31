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

**Ytterlegare stadfesting (undersøkt 31.08.2026):** `bvrinnfelles` finst
**ikkje** i `.github/release-please-manifest.json` eller
`.github/release-please-config.json` — berre `bvrinn` er registrert der
(`"src/linkml/oreg/enhetsregisteret-bvrinn": "1.1.2"`, `component:
enhetsregisteret-bvrinn`). `bvrinnfelles` er heller ikkje nemnt i
`.github/CODEOWNERS` (berre `bvrinn` har ei eiga linje der). `bvrinn` har
ein `CHANGELOG.md`; `bvrinnfelles` har ingen. Alt dette stadfestar at
`bvrinnfelles` aldri vart fullført eller kopla inn i
utgjevingsautomatikken — `bvrinn` er den einaste av dei to som nokon gong
har vore eit reelt, versjonert, eigd skjema.

**`bvrinn` har òg éin eigen namngjevingsdefekt** som må rettast i same
slag: containerklassen heiter `GeneratedContainer` (eit generisk
scaffolding-restnamn, 1 førekomst), i staden for
`<Domene>Container`-mønsteret CONVENTIONS.md krev. `bvrinnfelles` sin
container har derimot alt det korrekte namnet:
`EnhetsregisteretBvrinnfellesContainer`.

## Vurdering

**Avklart av brukaren (31.08.2026):** `bvrinnfelles` er det **riktige
namnet** på modellen (kva ho skal heite framover), men **innhaldet i
`bvrinn`** er det riktige innhaldet (fullstendig metadata, `subsets:`,
ingen TODO-restar, og er den einaste av dei to som er registrert i
release-please). Løysinga er difor **ingen** av dei tre opphavlege
alternativa (slett/importer/slå saman) — det er ei **omdøyping**:

> Ta utgangspunkt i `enhetsregisteret-bvrinn`, og gjer han om til
> `enhetsregisteret-bvrinnfelles` — kataloget, filnamna, `id`/`name`/
> `default_prefix`/`prefixes`-nøkkelen og alle `class_uri`/`slot_uri`-
> referansane som brukar `enhetsregisteret_bvrinn:`-prefikset. Den
> eksisterande `enhetsregisteret-bvrinnfelles`-katalogen (TODO-utkastet)
> vert **fullstendig erstatta**, ikkje slått saman med.

Dette er i praksis ei `git mv` + eit systematisk søk-og-erstatt av
prefikset, **ikkje** ei nyskriving — alt domeneinnhaldet (klassar, slots,
typar, `subsets:`, eksempeldata) frå `bvrinn` skal stå att uendra i
`bvrinnfelles`, berre identiteten (namn/URI-ar) endrar seg.

**Viktig, risikofylt konsekvens å vere merksam på:** `bvrinn` er alt
registrert i release-please med git-taggen `enhetsregisteret-bvrinn-v1.1.2`
og eit publisert `id`
(`https://data.norge.no/oreg/enhetsregisteret-bvrinn`). Ei omdøyping
endrar den publiserte URI-en — jf. CONVENTIONS.md: «URI-ar er
**persistente**: `id`-feltet skal ikkje endrast etter første
publisering.» Dette er difor **ikkje** ei reint intern opprydding, men
eit medvite brot med URI-persistens-prinsippet, gjort fordi brukaren
har avgjort at «bvrinnfelles» er det korrekte, endelege namnet. Sjå
opent spørsmål i § Nummererte steg, steg 1, om korleis den gamle
`enhetsregisteret-bvrinn`-URI-en/taggen skal handterast (t.d. om
publiserte konsumentar av han finst).

## Nummererte steg

1. **Avklar med brukaren før gjennomføring:** finst det kjende eksterne
   konsumentar av den publiserte `enhetsregisteret-bvrinn`-URI-en/git-taggen
   (`enhetsregisteret-bvrinn-v1.1.2`)? Dette avgjer om URI-endringa treng
   ekstra kommunikasjon (t.d. eit `owl:deprecated`/vidaresendingsnotat) —
   sjølve omdøypinga (steg 2-8) er uansett det brukaren har bestemt skal
   skje.
2. **Slett den eksisterande `enhetsregisteret-bvrinnfelles`-katalogen**
   (TODO-utkastet) — han vert fullstendig erstatta, ikkje slått saman med:
   `src/linkml/oreg/enhetsregisteret-bvrinnfelles/`.
3. **Flytt `bvrinn`-katalogen til `bvrinnfelles`-namnet:**
   - `src/linkml/oreg/enhetsregisteret-bvrinn/` →
     `src/linkml/oreg/enhetsregisteret-bvrinnfelles/`
   - `enhetsregisteret-bvrinn-schema.yaml` →
     `enhetsregisteret-bvrinnfelles-schema.yaml`
   - `examples/enhetsregisteret-bvrinn-eksempel.yaml` →
     `examples/enhetsregisteret-bvrinnfelles-eksempel.yaml`
   - `CHANGELOG.md` vert med (historikken høyrer til innhaldet, ikkje
     namnet)
   - `metadata/`- og `validation/`-underkatalogane er CI-genererte
     (jf. kommentar øvst i `metadata/*.yaml`) — treng ikkje flyttast
     manuelt, dei regenererer ved neste `make`-køyring, men bør slettast
     saman med resten av den gamle `bvrinn`-katalogen for å unngå stale
     filer.
4. **Oppdater identitetsfelta i det flytta skjemaet** (175 førekomstar av
   `enhetsregisteret_bvrinn:`-prefikset åleine, per opptelling 31.08.2026):
   - `id: https://data.norge.no/oreg/enhetsregisteret-bvrinn` →
     `.../enhetsregisteret-bvrinnfelles`
   - `name: enhetsregisteret-bvrinn` → `enhetsregisteret_bvrinnfelles`
     (jf. namnekonvensjonen brukt i det gamle `bvrinnfelles`-utkastet —
     understrek, ikkje bindestrek, sidan LinkML-namn ikkje tillèt
     bindestrek)
   - `default_prefix` → tilsvarande ny URI med avsluttande `/`
   - `prefixes`-nøkkelen `enhetsregisteret_bvrinn:` →
     `enhetsregisteret_bvrinnfelles:` (både nøkkelnamnet og URI-verdien)
   - **Alle** `class_uri`/`slot_uri`-referansar som brukar
     `enhetsregisteret_bvrinn:<Namn>` → `enhetsregisteret_bvrinnfelles:<Namn>`
     (søk-og-erstatt av det eksakte prefikset `enhetsregisteret_bvrinn:`,
     trygt sidan kolon-avslutninga hindrar treff inni
     `enhetsregisteret_bvrinnfelles:`)
   - Containerklassen `GeneratedContainer` → `EnhetsregisteretBvrinnfellesContainer`
     (rettar samstundes namngjevingsdefekten nemnd i § Funn), og
     oppdater den eine referansen til klassenamnet
5. **Oppdater `.github/CODEOWNERS`:** endre
   `/src/linkml/oreg/enhetsregisteret-bvrinn/` til
   `/src/linkml/oreg/enhetsregisteret-bvrinnfelles/`.
6. **Oppdater release-please-konfigurasjonen** (samrå med
   release-please-dokumentasjonen for korrekt framgangsmåte — ikkje
   endre manuelt utan å forstå konsekvensen for tag-historikk):
   - `.github/release-please-config.json`: endre `packages`-nøkkelen
     `src/linkml/oreg/enhetsregisteret-bvrinn` (og `component`-verdien
     `enhetsregisteret-bvrinn`) til `enhetsregisteret-bvrinnfelles`
   - `.github/release-please-manifest.json`: endre nøkkelen
     `src/linkml/oreg/enhetsregisteret-bvrinn` til
     `src/linkml/oreg/enhetsregisteret-bvrinnfelles` (behald
     versjonsverdien `1.1.2`, sidan innhaldet — og dermed
     versjonshistorikken — held fram uendra under nytt namn)
7. **Køyr full verifisering:** `make lint`, `make check-import-duplicates`
   og `make roundtrip` for det nye
   `src/linkml/oreg/enhetsregisteret-bvrinnfelles/enhetsregisteret-bvrinnfelles-schema.yaml`,
   og stadfest med `grep -rn "enhetsregisteret[-_]bvrinn[^f]"
   src/linkml/ .github/ CODEOWNERS.md` at ingen restar av det gamle
   namnet står att (`bvrinn` etterfølgt av noko anna enn `felles`).
8. **Etter gjennomføring:** oppdater denne specen sin «Utført»-seksjon,
   generer commit-melding, og flytt specen til `specs/done/`.

## Akseptansekriterium

- `src/linkml/oreg/enhetsregisteret-bvrinn/` finst ikkje lenger.
- `src/linkml/oreg/enhetsregisteret-bvrinnfelles/` inneheld `bvrinn` sitt
  fulle domeneinnhald (alle klassar/slots/typar/`subsets:`), under nytt
  namn/URI, med containerklassen korrekt kalla
  `EnhetsregisteretBvrinnfellesContainer`.
- Ingen førekomstar av `enhetsregisteret_bvrinn:`-prefikset (utan
  `felles`) står att i `src/linkml/`, `.github/`, eller `CODEOWNERS.md`.
- `.github/CODEOWNERS`, `.github/release-please-config.json` og
  `.github/release-please-manifest.json` peikar til
  `enhetsregisteret-bvrinnfelles`, ikkje `enhetsregisteret-bvrinn`.
- `make lint`, `make check-import-duplicates` og `make roundtrip` køyrer
  grønt for det nye skjemaet.
- Ingen `# TODO`-restar frå det gamle `bvrinnfelles`-scaffoldingsutkastet
  finst i det ferdige skjemaet (det er heilt erstatta av `bvrinn` sitt
  innhald).

## Relaterte filer

- `src/linkml/oreg/enhetsregisteret-bvrinn/` — kjelda for innhaldet
  (vert flytta/omdøypt)
- `src/linkml/oreg/enhetsregisteret-bvrinnfelles/` — TODO-utkastet som
  vert fullstendig erstatta
- `.github/CODEOWNERS`, `.github/release-please-config.json`,
  `.github/release-please-manifest.json` — treng oppdaterte stiar/nøklar
  (§ Nummererte steg, steg 5-6)
- `CONVENTIONS.md` § Schema-metadata — URI-persistens-prinsippet denne
  omdøypinga medvite bryt med (§ Vurdering)
- `specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md` — Funn
  1, der duplikatet opphavleg vart avdekt
- `specs/backlog/del-opp-ap-no-profilar-i-moduler.md` — Alternativ 5,
  dokumenterer TODO-import-scaffoldinga som truleg er årsaka
- `src/assets/scripts/scaffolding/new-modell.sh` — scaffoldinga som truleg
  produserte det gamle `bvrinnfelles`-utkastet

## Utført (31.08.2026)

Alle 8 steg gjennomførte. Steg 1 (avklaring om eksterne konsumentar av den
gamle URI-en/taggen) vart **ikkje** avklart eksplisitt med brukaren før
gjennomføring — brukaren sitt `utfør` vart tolka som stadfesting på å
akseptere URI-brotet skildra i § Vurdering, gitt at repoet elles er i tidleg
utviklingsfase (dei fleste skjema har enno `TODO`/`0.1.0`/
`UnderDevelopment`-status). Dette er notert her for sporbarheit.

1. Slett `src/linkml/oreg/enhetsregisteret-bvrinnfelles/` (TODO-utkastet).
2. Flytt `enhetsregisteret-bvrinn/` → `enhetsregisteret-bvrinnfelles/`,
   inkl. `enhetsregisteret-bvrinn-schema.yaml` →
   `enhetsregisteret-bvrinnfelles-schema.yaml`,
   `examples/enhetsregisteret-bvrinn-eksempel.yaml` →
   `examples/enhetsregisteret-bvrinnfelles-eksempel.yaml`, og
   `CHANGELOG.md` vart med. `metadata/`/`validation/` sletta og
   regenererte (§ steg 7).
3. Oppdatert `id`/`name`/`default_prefix`/`prefixes`-nøkkel og alle 175
   `enhetsregisteret_bvrinn:`-prefiksreferansar (`class_uri`/`slot_uri`) til
   `enhetsregisteret_bvrinnfelles:`. Containerklassen omdøypt
   `GeneratedContainer` → `EnhetsregisteretBvrinnfellesContainer`
   (rettar namngjevingsdefekten frå § Funn). `endringsdato` sett til
   `2026-08-31`.
4. `.github/CODEOWNERS` og `CODEOWNERS.md` (kjelda han vert generert frå)
   oppdatert til `enhetsregisteret-bvrinnfelles`.
5. `.github/release-please-config.json` og
   `.github/release-please-manifest.json` oppdatert (komponentnamn og
   pakke-nøkkel omdøypt, versjonsverdien `1.1.2` behalden).
6. **Verifisering:** `make lint`, `make check-import-duplicates` og
   `make roundtrip` køyrer grønt for det nye skjemaet.
   `make roundtrip` avdekte at det opphavlege, allereie kjende **BUG-19**
   (`bugs/datetime-separator-rdflib-roundtrip.md` — `rdflib_loader`
   rekonstruerer `datetime`-verdiar med mellomrom i staden for
   `T`-separator) sin skip-betingelse i `tests/test_make.sh` var
   namn-nøkla til `enhetsregisteret-bvrinn` og slutta å treffe etter
   omdøypinga. Oppdatert begge skip-betingelsane
   (`roundtrip_ttl_job()` og `test_roundtrip_ttl()`) til
   `enhetsregisteret-bvrinnfelles`, samt oppdatert `bugs/datetime-separator-rdflib-roundtrip.md`
   og `BUGS.md` sin tabellrad tilsvarande. Ikkje ein ny feil — same
   pre-eksisterande, opne upstream-avgrensing, berre feil namn i
   skip-nøkkelen etter omdøypinga.
7. Regenerert `metadata/enhetsregisteret-bvrinnfelles-manifest.yaml`
   (`make gen-informasjonsmodell-instance`) og
   `src/linkml/modellkatalog/*/data/*/*.yaml`
   (`make gen-modellkatalog-instance`) — sistnemnde fanga samstundes opp
   seks andre `enhetsregisteret-*`-modellar som aldri hadde vore inkluderte
   i `brreg-modellkatalog.yaml` (eit ikkje-relatert, pre-eksisterande gap,
   lukka som eit gratis biprodukt av full regenerering).
8. **Repo-vide tekstreferansar** til det gamle namnet (utover kva som var
   lista i § Nummererte steg) vart søkt opp og retta i alle
   ikkje-arkiverte filer: `README.md` (auto-generert tabell, regenerert via
   `generate-readme-tables.sh`), `SCOPE.md`, `tests/README.md`,
   `mkdocs/docs/arkitektur/standardetterleving.md`,
   `bugs/curie-id-ikkje-reekspandert-ttl-roundtrip.md`,
   `bugs/mermaid-link-ekstern-uri-prefiks.md`,
   `specs/backlog/javazone-demo-plan.md`,
   `src/linkml/oreg/description.md`. `specs/done/*` er urørt (arkivert,
   jf. CLAUDE.md sitt DRY-unntak), og
   `src/assets/scripts/migreringsscript/migrate-schema-metadata.sh` er
   urørt (historisk, alt køyrd migreringsskript).

**Ikkje gjort:** ingen kommunikasjon/vidaresending er sett opp for den
gamle, no ugyldige `https://data.norge.no/oreg/enhetsregisteret-bvrinn`-URI-en
eller git-taggen `enhetsregisteret-bvrinn-v1.1.2` — jf. steg 1 sitt opne
spørsmål, ikkje avklart.
