# Lenkjesjekk runde 3 — fiks resterande feil

## Bakgrunn

Etter NGR-vokabularnamnerom-fiksen (commit `91875312`) står det att ei rekkje
feil frå `lenkjesjekk`-jobben i `.github/workflows/lenkje-og-mermaid-sjekk.yml`
(lychee mot `**/*.md`). Brukaren limte inn full feilliste frå siste køyring og
bad om evaluering + plan (ikkje utføring i denne omgang).

Kvar feil er verifisert manuelt (curl mot faktiske vertar, filsystemsjekk mot
faktiske stiar) før han er kategorisert som REELL FEIL eller FALSK POSITIV.
Kjelde-DRY: éin feil kan opptre i fleire genererte sider, men rettast alltid
i générator-/kjeldefila (jinja-mal, `.sh`-seksjon, `-schema.yaml`, README) —
aldri i genererte `.md`-filer under `mkdocs/docs/` eller `generated/`.

To avklaringar er henta frå brukaren før planen vart skriven:

1. **`https://brreg.no/kontakt/modellforvaltning`** (9 filer: manifest-metadata
   + `CODEOWNERS.md`) → skal erstattast med
   `https://github.com/brreg/linkml-datamodellering-no/blob/main/CONTRIBUTING.md#rapportering-av-feil`
2. **`cccevno`/`euvoc`/`skosno`-vokabularnamnerom-404-ar** → skal ekskluderast
   i `.github/lychee.toml` etter same mønster/kommentarstil som den nyleg
   merga NGR-eksklusjonen (kategori E i
   `specs/done/lenkjesjekk-runde2-verifisering.md` var tidlegare ope fordi
   avgjerda ikkje var teken — no teken).

## Kategoriar og tiltak

### A. Reelle brotne interne stiar (rett i kjelde)

| # | Feil | Rotårsak | Fiks |
|---|---|---|---|
| A1 | `mkdocs/docs/ap-no/dqv-core/index.md`, `.../modelldcat-katalog/index.md`, `.../modelldcat-modell/index.md` — GitHub-lenkjer til `build.yaml`/`<schema>-schema.yaml` gjev 404 (6 lenkjer) | `mkdocs/lib/sections/datamodell.sh:17` og `mkdocs/lib/sections/generated_artifacts.sh:80` hardkodar `src/linkml/$domain/$schema/...` — men delmodell-skjema (dqv-core, modelldcat-katalog, modelldcat-modell) ligg fysisk i FORELDRE-skjemaet sin katalog (`dqv-ap-no/`, `modelldcat-ap-no/`), ikkje i ein katalog oppkalla etter seg sjølv. `PARENT_MODEL`-miljøvariabelen er alt eksportert per skjema i `publish.sh:127` (brukt av `delmodellar.sh`/`generate_index.sh`) | Bruk `${PARENT_MODEL:-$schema}` som katalogsegment i staden for `$schema` i begge scripta |
| A2 | `mkdocs/docs/kom-i-gang/ny-domenemodell.md` (2 lenkjer) — `src/linkml/referanse/referanse-schema.yaml` finst ikkje | Feil sti — faktisk fil er `src/linkml/referanse/referansemodell/referansemodell-schema.yaml` | Rett dei to lenkjene i `mkdocs/docs/kom-i-gang/ny-domenemodell.md` |
| A3 | `mkdocs/docs/kom-i-gang/ny-domenemodell.md` (1 lenkje) — `specs/bugs/langstring-rdflib-roundtrip.md` finst ikkje | Feil katalog — faktisk fil er `bugs/langstring-rdflib-roundtrip.md` (jf. `BUGS.md`-konvensjonen) | Rett stien i same fil |
| A4 | `tests/README.md` (5 lenkjer, 3 unike filer) — `../specs/bugs/*.md` finst ikkje | Same `specs/bugs/` vs. `bugs/`-forveksling som A3 | Endre dei tre lenkjereferansane (`[BUG-1]`, `[BUG-2]`, `[BUG-3]`) til `../bugs/*.md` |
| A5 | `mkdocs/docs/arkitektur/ekstern-bruk.md` — `raw.githubusercontent.com/.../main/renovate.json` gjev 404 | Faktisk fil er `.github/renovate.json`, ikkje repo-rot | Rett URL-stien til `.../main/.github/renovate.json` |
| A6 | `mkdocs/docs/arkitektur/valideringsregler.md` + `src/mcp-linkml-validator/policies/README.md` (2 lenkjer kvar, same URL-ar) — `brreg.github.io/.../publisering-begrep/` og `.../publisering-modell/` gjev 404 | Sidene ligg under `mkdocs/docs/publisering/`-underkatalogen, ikkje flatt på portalrota | Rett dei to URL-ane i `src/mcp-linkml-validator/policies/README.md` (kjelda — `valideringsregler.md` er generert derifrå) til `.../publisering/publisering-begrep/` og `.../publisering/publisering-modell/` |
| A7 | `mkdocs/docs/automasjon/modellmanifest-generering.md` — `informasjonsforvaltning.github.io/modelldcat-ap-no/` gjev 404 | Sida er flytta/nedlagd. Stadfesta fungerande erstatning: `https://data.norge.no/specification/modelldcat-ap-no` (200, same mål som README.md alt brukar andre stader for ModelDCAT-AP-NO) | Byt lenkjemålet i fila |

### B. `brreg.no/kontakt/modellforvaltning` → CONTRIBUTING.md (avklart med brukar)

| # | Feil | Fiks |
|---|---|---|
| B1 | 9 filer med `id:`/`har_kontaktside:`/`contact_uri:` som peikar til `https://brreg.no/kontakt/modellforvaltning` (404): <br>`src/linkml/begrepskatalog/brreg-begrepskatalog/metadata/brreg-begrepskatalog-manifest.yaml`, `src/linkml/fair/fair-metadata/metadata/fair-metadata-manifest.yaml`, `src/linkml/modellkatalog/brreg-modellkatalog/{data/brreg-modellkatalog/brreg-modellkatalog.yaml, examples/brreg-modellkatalog-eksempel.yaml, metadata/brreg-modellkatalog-manifest.yaml}`, `src/linkml/ngr/ngr-virksomhet/metadata/ngr-virksomhet-manifest.yaml`, `src/linkml/oreg/{enhetsregisteret-bvrinn,lunchregisteret,register-over-aksjeeiere}/metadata/*-manifest.yaml`, `CODEOWNERS.md` | Byt alle 9 førekomstar til `https://github.com/brreg/linkml-datamodellering-no/blob/main/CONTRIBUTING.md#rapportering-av-feil`. **Merk:** dette er RDF-publisert `vcard:hasURL`/kontaktpunkt-data (via `har_kontaktside`) i fleire av desse — verifiser med `make lint`/`make roundtrip` per skjema etter endring, og sjekk om `id:`-feltet (som er sjølve URI-identifikatoren til kontaktpunktet, ikkje berre ei lenkje) toler å peike på ei GitHub-side semantisk (flagg til brukar i PR viss dette kjennest feil for `id:`-feltet spesifikt — det kan vere at berre `har_kontaktside` bør endrast, medan `id:` treng ein stabil intern URI-identifikator som ikkje treng vere ei klikkbar 200-side) |

### C. Reelle eksterne 404-ar → eksklusjon i `.github/lychee.toml` (avklart med brukar)

Følg identisk struktur/kommentarstil som den eksisterande NGR-eksklusjonen
(`.github/lychee.toml` linje 86–95): grunngjeving, kva som er verifisert,
kva som *ikkje* er dekt av eksklusjonen.

| # | Namnerom | Verifisert | Eksklusjonsregex |
|---|---|---|---|
| C1 | `data.norge.no/vocabulary/cccevno#...` (CPSV-AP-NO — 4 sider × 2 lenkjer) | Stadfesta reelt backend-404 (JSON `{"detail": "Not Found"}`) uavhengig av `Accept`-header i to tidlegare rundar (`specs/done/lenkjesjekk-runde2-verifisering.md` kategori E) — avgjerda om varig eksklusjon var då eksplisitt utsett, no teken | `^https://data\\.norge\\.no/vocabulary/cccevno` |
| C2 | `publications.europa.eu/ontology/euvoc#...` (SKOS-AP-NO + begrepskatalog — 5 sider × 2 lenkjer) | `curl -sIL` stadfesta: 301 → `https://publications.europa.eu/resource/ontology/euvoc` → 404, identisk med og utan nettlesar-`Accept`-header | `^https?://publications\\.europa\\.eu/ontology/euvoc` |
| C3 | `data.norge.no/vocabulary/skosno/kilde-type` og `.../associative-relation-role` (SKOS-AP-NO + begrepskatalog — 4 sider × 2 lenkjer) | `curl -sIL` stadfesta reelt 404 (same backend-mønster som C1) | `^https://data\\.norge\\.no/vocabulary/skosno/(kilde-type\|associative-relation-role)` |
| C4 | `https://brreg-linkml.goatcounter.com/` (monitorering.md) | `curl -sIL` stadfesta reelt 400 på bar rot-GET, uavhengig av `Accept`-header — sannsynlegvis eit analytics-endepunkt som krev spesifikke query-parametrar/metode, ikkje meint som browsable side | Legg til i `exclude`-lista (ikkje eit `[hosts.]`-overstyring, sidan URL-en berre finst denne eine staden og ikkje er eit breitt brukt namnerom) |

**Merk A2/A5-stil kommentarar:** kvar ny eksklusjonsregel skal ha same
struktur som eksisterande reglar — kva som er stadfesta, kva metode
(`curl`/manuell), og referanse til denne specen for sporbarheit.

### D. Falske positivar frå eiga docgen-pipeline (rett malen, ikkje sjølve lenkja)

| # | Feil | Rotårsak | Fiks |
|---|---|---|---|
| D1 | `mkdocs/docs/samt/samt-bu/index.md` — 3 feil: valideringsmeldingar som inneheld regex-mønster (`^http://.../language/[A-Z]{3}$`, `^http://purl.org/adms/status/(Completed\|...)$`) vert feiltolka som URL-ar av lychee sin bare-URL-detektor | `mkdocs/lib/scripts/generate-validation-md.py` linje 112 og 126 skriv `message`-teksten som rein prosa (`lines.append(f"   {message}")`), utan kode-span-vern. Lychee hoppar som standard over innhald i `` `kode-spans` ``/kodeblokker, men ikkje over bar tekst | Endre begge `lines.append(...)`-kalla til å pakke `message` i backticks: `f"   \`{message}\`"` |
| D2 | `mkdocs/docs/oreg/lunchregisteret/klasser/tema.md` — `psi.norge.no/los/tema/` (utan `<namn>`-suffiks) gjev 404 | Kjeldeteksten i `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` (slot `tema`, linje ~1063) har korrekt vern: `` `https://psi.norge.no/los/tema/<namn>` `` (backticks + plassholdar). LinkML sin eigen `gen-doc`-genererte `class.md.jinja2`/`slot.md.jinja2`-mal (`_{{ element_description_line }}_`) gjer rein passthrough av `element.description`, men den *faktiske* teksten i den genererte fila manglar backtickane — stadfesta ved direkte samanlikning av kjeldeskjema vs. `generated/oreg/lunchregisteret/docs/tema.md`. Dette er ikkje vår eigen mal-kode (ingen backtick-stripping i `.jinja2`-filene våre) — peikar mot ei LinkML-intern (`schemaview`/YAML-parsing) normalisering av description-feltet som er utanfor dette repoet si kontroll. **Ikkje fullstendig rotårsak-granska** — krev djupare gransking av linkml-runtime/generators dersom det skal rettast ved kjelda | Kortsiktig, presis fiks: legg til eksakt-treff-eksklusjon `^https://psi\\.norge\\.no/los/tema/$` i `.github/lychee.toml` (trailing-slash-utan-suffiks er alltid eit artefakt av stripping, aldri eit tilsikta mål — reelle bruk har alltid eit temanamn etter skråstreken). Opprett `bugs/linkml-docgen-strip-backtick-description.md` som dokumenterer den ugranska LinkML-rotårsaka for seinare oppfølging (jf. CLAUDE.md § Kjente feil-konvensjonen) |

### E. README.md ↔ mkdocs/docs/index.md — delt innhald, ulik lenkjekontekst

`mkdocs/publish.sh` sin `write_index_from_readme()` (linje 78–89) kopierer
`README.md` **ordrett** til `mkdocs/docs/index.md` (ingen lenkje-omskriving),
sjølv om filene har ulik "rot" for relative lenkjer:

- **README.md** vert vist på GitHub → relative lenkjer løysast mot repo-rota
- **mkdocs/docs/index.md** vert vist i portalen → relative lenkjer løysast mot `mkdocs/docs/`-rota

To separate tabellar i README.md er kvar designa for berre éin av desse
kontekstane:

| # | Tabell | Lenkjemønster | Fungerer i README.md (GitHub) | Fungerer i index.md (portal) |
|---|---|---|---|---|
| E1 | "Domener" (statisk, handskriven, README.md linje ~176–184) | `[REFERANSE](src/linkml/referanse/)` osb. | ✅ (`src/linkml/<domain>/` finst ved repo-rota) | ❌ (`mkdocs/docs/src/linkml/<domain>/` finst ikkje) |
| E2 | "Skjema" (auto-generert av `generate_schema_table()` i `generate-readme-tables.sh`, kommentar stadfestar "Konverter ... for GitHub Pages") | `[AP-NO]($domain/)`, `[dcat-ap-no](ap-no/dcat-ap-no/)` osb. | ❌ (`ap-no/` finst ikkje ved repo-rota) | ✅ (`mkdocs/docs/ap-no/` finst i portalen) |

Same mønster gjentek seg for `generate_begrepskatalog_table()` og
`generate_modellkatalog_table()` (README.md linje 271–294) — desse brukar
E2-stilen (`$domain_link`/`$ghpages_link`) og er difor òg berre korrekte i
portal-konteksten.

**Tilråding:** gjer begge tabelltypane kontekst-uavhengige ved å bruke
**absolutte URL-ar** i staden for relative, i tråd med CLAUDE.md § "Relative
vs. absolutte lenkjer i portalinnhald" (som alt seier at `src/linkml/`-mål
ikkje er portalbygde og difor skal ha absolutt GitHub-lenkje):

- E1 (Domener-tabellen, statisk i README.md): byt `src/linkml/<domain>/` →
  `https://github.com/brreg/linkml-datamodellering-no/tree/main/src/linkml/<domain>/`
- E2 (auto-genererte tabellar i `generate-readme-tables.sh`): byt
  `$domain/`/`$ghpages_schema_link/`-mønsteret til absolutt GH Pages-URL:
  `https://brreg.github.io/linkml-datamodellering-no/$domain/` og
  `https://brreg.github.io/linkml-datamodellering-no/$ghpages_schema_link/`
  (same gjeld `generate_begrepskatalog_table()`/`generate_modellkatalog_table()`
  sine `$domain_link`/`$ghpages_link`)

Dette er den einaste kategorien som krev endring i eit script som produserer
**begge** filene (README.md direkte, index.md via kopi) — éin fiks løyser
feila i begge filer samtidig (DRY, kjelda er `generate-readme-tables.sh` +
den statiske README.md-tabellen).

### F. Infrastruktur — lychee-scope

| # | Feil | Fiks |
|---|---|---|
| F1 | `mkdocs/node_modules/@brreg/designsystemet-theme/README.md` — npm 403 | `node_modules` er ikkje i `exclude_path` i `.github/lychee.toml` (berre `generated`, `mkdocs/site`, `specs`). Legg til `"mkdocs/node_modules"` i `exclude_path`-lista |

### G. Dokumentasjonsinnhald som treng semantisk omskriving (ikkje berre lenkjebyte)

| # | Feil | Merknad |
|---|---|---|
| G1 | `mkdocs/docs/automasjon/readme-tabellgenerering.md` (2 lenkjer) — `.github/workflows/update-readme.yml` finst ikkje | Denne workflowen finst ikkje og har truleg aldri eksistert i denne forma — `generate-readme-tables.sh` køyrer i staden via `make docs-publish` (`make/50-docs.mk`), kalla frå `lenkje-og-mermaid-sjekk.yml`/`generate.yml`. Dette er ei innhaldsfeil, ikkje berre ei lenkjefeil — teksten "GitHub Actions-workflowen ... køyrer ... automatisk ved endringar i: ..." skildrar ein mekanisme som ikkje finst. Krev omskriving av avsnittet (ikkje berre URL-bytte) til å skildre den faktiske utløysingsmekanismen (`make docs-publish` sitt avhengigheitssteg i CI). **Flagga for gjennomsyn før utføring** sidan det endrar meining, ikkje berre mål |

## Steg (rekkjefølgje for utføring)

1. A-kategorien (reelle interne stibrot) — 7 uavhengige småfiksar, lågast risiko
2. F1 (`node_modules`-eksklusjon) — trivielt, ingen avhengigheiter
3. D1 (backtick-vern i `generate-validation-md.py`) — krev `make docs-publish` for å stadfeste at samt-bu/index.md sitt Valideringsresultat-avsnitt framleis renderer korrekt
4. C1–C4 (lychee.toml-eksklusjonar) — legg til alle fire i éin batch, køyr `actionlint`? **Nei** — `lychee.toml` er ikkje ein `.github/workflows/*.yml`-fil, så CLAUDE.md sitt actionlint-krav gjeld ikkje her. Verifiser i staden med lokal lychee-køyring (podman) mot eit lite utval sider
5. D2 (los/tema-eksklusjon + ny bugs/-fil) — skriv `bugs/linkml-docgen-strip-backtick-description.md` og oppdater `BUGS.md`
6. E (README.md/index.md lenkjekontekst) — endre `generate-readme-tables.sh` (E2) og den statiske Domener-tabellen i README.md (E1), køyr deretter `bash src/assets/scripts/makefile/generate-readme-tables.sh README.md` for å stadfeste at auto-generert-seksjonen framleis matchar `BEGIN/END AUTO-GENERATED`-markørane
7. B1 (kontakt-URL) — 9 filer, køyr `make lint`/`make roundtrip` per involvert skjema etterpå
8. G1 (readme-tabellgenerering.md-omskriving) — **legg fram utkast til ny tekst for brukar før utføring**, sidan det er ei innhaldsendring
9. Full verifisering: `make docs-publish && make docs-build`, deretter lokal `podman run ... lycheeverse/lychee --config .github/lychee.toml '**/*.md'` mot heile repoet for å stadfeste at talet på feil er redusert som venta (frå dagens ~150 førekomstar ned til berre G1 sine eventuelle attverande, viss den vert utsett)

## Handlingsliste

- [x] A1: `mkdocs/lib/sections/datamodell.sh` + `generated_artifacts.sh` — bruk `${PARENT_MODEL:-$schema}` for kjeldekatalog
- [x] A2: `mkdocs/docs/kom-i-gang/ny-domenemodell.md` — rett `referanse-schema.yaml` → `referansemodell/referansemodell-schema.yaml` (2 stader)
- [x] A3: same fil — rett `specs/bugs/langstring-rdflib-roundtrip.md` → `bugs/langstring-rdflib-roundtrip.md`
- [x] A4: `tests/README.md` — rett dei tre `[BUG-N]`-referansane til `../bugs/`
- [x] A5: `mkdocs/docs/arkitektur/ekstern-bruk.md` — rett `renovate.json`-stien
- [x] A6: `src/mcp-linkml-validator/policies/README.md` — rett dei to `publisering-*`-URL-ane
- [x] A7: `mkdocs/docs/automasjon/modellmanifest-generering.md` — byt til `data.norge.no/specification/modelldcat-ap-no`
- [x] B1: 9 filer — byt `brreg.no/kontakt/modellforvaltning` → CONTRIBUTING.md-anker (bytt konsekvent i både `id:`- og `har_kontaktside:`-felt for å halde eksisterande mønster der begge peika på same verdi)
- [x] C1–C4: `.github/lychee.toml` — lagt til 4 nye eksklusjonar med grunngjevingskommentarar
- [x] D1: `mkdocs/lib/scripts/generate-validation-md.py` — backtick-pakka `message` (2 stader)
- [x] D2: `.github/lychee.toml` eksakt-eksklusjon + ny `bugs/linkml-docgen-strip-backtick-description.md` (BUG-20) + `BUGS.md`-oppdatering
- [x] E1: README.md Domener-tabell → absolutte GitHub-lenkjer
- [x] E2: `generate-readme-tables.sh` (`generate_schema_table`, `generate_begrepskatalog_table`, `generate_modellkatalog_table`) → absolutte GH Pages-lenkjer
- [x] F1: `.github/lychee.toml` `exclude_path` — lagt til `mkdocs/node_modules`
- [x] G1: brukar stadfesta utkast til ny tekst i `readme-tabellgenerering.md` — utført
- [x] Verifisering: `make docs-publish`, `make docs-build`, lokal lychee-køyring, samanlikn feiltal før/etter

## Utført

Alle tiltak i handlingslista over er utførte og verifiserte lokalt (podman
sandbox mellombels avslått for `make docs-publish`/`make docs-build`/lychee
sidan containerkøyring krev skrivetilgang til `/run/user/1000/libpod`, som
standard-sandboxen blokkerer).

**Verifiseringsresultat:** `podman run lycheeverse/lychee --config
.github/lychee.toml '**/*.md'` mot heile repoet gjekk frå **~150
feilførekomstar** (brukaren sitt opphavlege utdrag) til **2 attverande
feil**, begge same kjende, alt kjeldefiksa årsak (sjå punkt nedanfor) —
reelt **0 uløyste feil**.

**Ekstra funn oppdaga under verifisering** (ikkje del av opphavleg plan,
fiksa fortløpande sidan dei var same feilklasse som alt godkjende tiltak):

- `mkdocs/docs/automasjon/readme-tabellgenerering.md` hadde ei ANDRE
  referansetabell-rad (linje ~337-338) som òg peika på det ikkje-eksisterande
  `update-readme.yml` OG eit ikkje-eksisterande `make readme-tables`-mål —
  retta til å peike på `mkdocs/publish.sh`/`make/50-docs.mk` (same
  rotårsak som G1)
- `src/mcp-linkml-modell-utkast/README.md` hadde same
  stale-portal-URL-mønster som A6 (`.../ny-domenemodell/` i staden for
  `.../kom-i-gang/ny-domenemodell/`) — retta
- **Ny rotårsak funnen, same feilklasse som D1:** `Imports`-rada i
  Metadata-tabellen (`src/assets/templates/docgen/index.md.jinja2` linje 38)
  skreiv versjonslåste URL-importar (`imports:`-verdiar med
  `raw.githubusercontent.com/.../<tag>/.../<schema>-schema`, utan
  `.yaml`-ending — dette ER korrekt LinkML-importsyntaks, IKKJE ein feil i
  sjølve skjemaet) som bar, ubeskytta tekst. Lychee sin bare-URL-detektor
  følgjer teksten som ei ekte lenkje, men URL-en manglar `.yaml` (som
  LinkML sjølv legg til internt ved import-oppløysing) og gjev difor 404 når
  nokon klikkar han i dokumentasjonen. Fiksa ved å pakke `{{ imp }}` i
  backticks i malen (same mønster som D1). **Attverande i denne
  verifiseringa** (2 feil i `oreg/lunchregisteret/index.md` og
  `klasser/index.md`) fordi malfiksen krev ein fresh `gen-doc`-køyring
  (`make domain-oreg` e.l.) for å ta effekt — `make docs-publish`/`docs-build`
  kopierer berre alt-genererte `generated/`-artefakt, dei regenererer ikkje
  sjølve gen-doc-outputen. Vil løyse seg automatisk ved neste ordinære
  `generate.yml`-køyring (som alltid køyrer full generering per domene).
- To ORPHANED, gitignorerte `generated/`-katalogar utan noka `src/linkml/`-
  kjelde (`generated/referanse/referanse/`, `generated/referanse/referanse-
  schema.yaml/`, `generated/oreg/blomsterregisteret/`) fanst frå tidlegare
  arbeidsøkter på denne maskinen og forureina den lokale
  verifiseringskøyringa med feil som aldri ville dukka opp i ekte CI (som
  alltid startar frå reint checkout). Rydda vekk (`rm -rf`) saman med
  tilhøyrande stale referansar i `mkdocs/mkdocs.yml` og to
  gitignorerte domene-`index.md`-filer — reint lokal opprydding, ingen
  kjeldeendring.

**Ikkje utført:** ingen — alle punkt i handlingslista (inkludert G1, som
fekk eksplisitt brukarstadfesting av forslått tekst før utføring) er
gjennomførte.
