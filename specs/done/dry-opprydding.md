# DRY-opprydding — reduser duplikat kode og erstatt hardkoda lister med dynamiske

## Bakgrunn

`specs/done/debug-referanse-nav-meny.md` synte konkret kva som kan gå gale
når same informasjon er skriven fleire stader: `referanse`-domenet vart lagt
til `generate`-jobbens matrise i `.github/workflows/generate.yml`, men ikkje
i den hardkoda `for domain in ...`-lista same fil brukar to andre stader
(og tilsvarande i `validate.yml`) — resultatet var eit domene som forsvann
frå GitHub Pages-menyen utan feilmelding. CLAUDE.md har alt ein eksplisitt
DRY-regel ("Kvar regel, klasse, slot og kommando skal ha éi kjelde" — terskel
tre eller fleire identiske tilfelle), men regelen er berre systematisk
handheva for LinkML-skjema (via importhierarkiet). Dette er ein plan for å
gjere det same for make-laget, Python-script, CI-workflows og testar.

**Mål:** éin kjeldeplass per faktum. Der ei liste (domene, image-metadata,
domene-unntak) i dag er skriven ut fleire gonger for hand, skal han i staden
*utleiast* dynamisk frå éin autoritativ kjelde — utan å ofre lesbarheit.
Dupliserte funksjonar skal konsoliderast til delte, samanhengande modular
(ikkje éin stor "utils"-fil), slik at kvar fil framleis er lett å lese
isolert.

## Metode

Kartlegginga under er gjort med målretta `grep`/`diff` mot heile repoet
(`make/`, `src/assets/scripts/`, `mkdocs/lib/scripts/`, `.github/workflows/`,
`tests/`) — ikkje ei gjetning. Kvart funn under er verifisert ved å samanlikne
faktisk kodeinnhald, ikkje berre funksjonsnamn.

**Avgrensing:** LinkML-skjema (`src/linkml/**/*.yaml`) er halde utanfor —
dei har alt sin eigen etablerte DRY-mekanisme (importhierarkiet, jf.
`PRINCIPLES.md § 3`), og eventuelle avvik der høyrer heime i ein eigen spec.

## Funn

### A. Hardkoda lister som bør bli dynamiske

| # | Stad | Duplisert | Risiko |
|---|---|---|---|
| A1 | `.github/workflows/generate.yml` (linje 167, 456) og `validate.yml` (linje 159, 250) | Same 9-domene-liste (`ap-no, begrepskatalog, fair, ...`) skriven **4 gonger** i 2 filer, 2 ulike syntaksar (YAML-array, bash-liste) | **Stadfesta årsak** til referanse-bugen — drift mellom kopiane er umogleg å oppdage før eit domene manglar i produksjon |
| A2 | `.github/workflows/generate.yml`: `ensure-images`-jobbens matrise (linje 55-83) vs. `generate`-jobbens `pull_image`-`case`-setning (linje ~265-295) | Same image-metadata (namn, Dockerfile-hash-input, make-target) for 6 image, skriven i to heilt ulike syntaksar (YAML-matrise og bash `case`) | Same klasse feil som A1 — ny hash-input-fil lagt til éin stad, gløymt i den andre → feil cache-nøkkel/image vert henta |
| A3 | `tests/test_make.sh` (linje 289, 309, 371, 468, 525) | `if [[ "$domain" == "ap-no" \|\| "$domain" == "fair" ]]` — identisk vilkår kopiert **5 gonger** | Låg (testkode), men same "gløymt éin stad"-risiko dersom eit nytt AP-NO-liknande domene (utan `tree_root`) vert lagt til |

### B. Dupliserte Python-funksjonar (verifisert med `diff`, ikkje berre namn)

| # | Funksjon | Filer | Status |
|---|---|---|---|
| B1 | `find_released_packages()` | `update-schema-dates.py`, `makefile/run-schema-validation.py` | Identisk logikk (`run-schema-validation.py` sin docstring seier eksplisitt "Same logikk som i update-schema-dates.py") |
| B2 | `get_domain_model()` | `makefile/save-validation-log.py`, `makefile/run-schema-validation.py` | Byte-for-byte identisk |
| B3 | `load_yaml_meta()` og `rewrite_refs()` | `makefile/gen-asyncapi.py`, `makefile/gen-openapi.py` | Byte-for-byte identisk (begge funksjonar, begge filer) |
| B4 | `write_yaml()` | `makefile/collect-concepts.py`, `makefile/generate-modellkatalog.py`, `makefile/generate-informasjonsmodell.py` | **3 filer** — identisk struktur, skil seg berre i header-kommentarens filnamn-tekst (krysser CLAUDE.md sin eigen 3-terskel for abstraksjon) |
| B5 | `load_yaml()` | 5 filer: `collect-concepts.py`, `generate-modellkatalog.py`, `generate-informasjonsmodell.py` (identisk, med `Path`-typehint + docstring) og `gen-docgen-examples.py`, `gen-dqv-measurements.py` (identisk, utan typehint — sistnemnde har `or {}`-fallback) | To nesten-identiske klynger |
| B6 | `get_version()` | `makefile/save-validation-log.py`, `makefile/run-schema-validation.py` | Same regex-logikk, ulik fallback-verdi (`"0.0.0-dev"` vs `"0.0.0"`) og éin manglar eksistenssjekk — krev forsiktig samanslåing, ikkje mekanisk kopiering |

### C. Strukturell duplikasjon i Makefile

| # | Stad | Duplisert | Merknad |
|---|---|---|---|
| C1 | `make/80-images.mk` | 6 `build-docker-*`-target, identisk 3-linjers struktur (`print_header` + `podman build`), skil seg berre i target-namn, Dockerfile-variabel, image-variabel | Same `define`+`$(eval $(call ...))`-mønster som alt brukt i `make/20-domain-targets.mk` (`domain_target`) — lågrisiko, velprøvd mønster i repoet |
| C2 | `make/10-generator-macros.mk` | 10 par av `run_gen_X` (serial, brukt ved `PARALLEL=1`) / `run_gen_X_parallel` (xargs-basert) — kvart par implementerer same kommandosekvens to gonger, i to ulike syntaksar | **Ikkje eit mekanisk fiks** — sjå vurdering under |

**Vurdering av C2:** Det kan finnast eit medvite designval bak den serielle
varianten (direkte, ordna output for interaktiv feilsøking, i motsetnad til
xargs sin potensielt interleava output). Før noka endring her må det
undersøkjast om `xargs -P 1` gir identisk output-oppførsel og lesbarheit som
dagens serielle kode — dersom ikkje, bør paret *ikkje* slåast saman, sidan
lesbarheit under feilsøking veg tyngre enn linjetal. Sjå steg 8.

## Målbilete

- **CI-domenelister (A1):** éin autoritativ kjelde for "kva domene finst" —
  helst utleia frå det same `make`-baserte oppdagingsmekanismen som alt
  finst i `make/02-schema-discovery.mk`, ikkje ei ny parallell liste i CI.
  Eit nytt domene skal automatisk dukke opp overalt utan manuell
  listeoppdatering.
- **CI-image-metadata (A2):** éin JSON-/YAML-manifest-fil med image-metadata
  som både matrisa og pull-logikken les frå.
- **Python-funksjonar (B):** flytta til små, samanhengande delte modular
  (t.d. `utils/yaml_io.py`, `utils/schema_meta.py`) — ikkje éin stor
  grab-bag-fil. Kvart kallande script skal framleis vere lett å lese isolert
  (eksplisitte importar øvst, ikkje "magisk" delt tilstand).
- **Makefile (C1):** `build-docker-*`-targeta generert via macro, slik at
  kvart image sine eigenskapar står på éi linje, lett skanbart.
- **Lesbarheit:** Ingen endring skal gjere det vanskelegare å forstå éin
  fil isolert. Der dynamisk oppslag (JSON/matrise) gjer koden *vanskelegare*
  å følgje enn ei kort, stabil liste, skal det grunngjevast eksplisitt i
  koden (kommentar) kvifor dynamikken er verdt kostnaden.

## Steg

1. **A1 — Dynamisk domeneliste i CI:**
   - Legg til eit `make print-domains`-target (`make/02-schema-discovery.mk`
     eller `make/20-domain-targets.mk`) som skriv ut `$(DOMAINS)` — same
     variabel `make domain-<x>` alt bruker internt
   - Legg til eit `discover`-steg tidleg i `generate.yml` og `validate.yml`
     (i `checkout-source`-jobben, eller ein ny liten jobb) som køyrer
     `make print-domains` inne i linkml-containeren (eller reint bash — sjå
     om `find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml'`
     kan køyrast direkte i CI utan container, sidan det berre er `find`)
     og eksporterer resultatet som JSON via `$GITHUB_OUTPUT`
   - Erstatt `strategy.matrix.domain: [...]` i begge filer med
     `${{ fromJson(needs.discover.outputs.domains) }}`
   - Erstatt dei to `for domain in ...`-løkkene (merge-steget i `generate.yml`,
     nedlastingssteget i `validate.yml`) med iterasjon over same
     `needs.discover.outputs.domains`
   - **Verifiser:** ein ny `make scaffold DOMAIN=test-domene ...` (eller
     berre ein mellombels testkatalog) skal dukke opp i alle 4 stadene utan
     kodeendring

2. **A2 — Dynamisk image-manifest i CI:**
   - Opprett `src/assets/containers/images.json` (eller `.yaml`) med
     `name`, `dockerfile`, `make_target`, `hash_files` per image — same felt
     som matrisa i `ensure-images` har i dag
   - Generer `ensure-images`-matrisa frå denne fila (`fromJson`, lasta via
     eit forsteg som gjer `cat images.json`)
   - Omskriv `pull_image`-`case`-setninga i `generate`-jobben til å lese
     same JSON via `jq` i staden for hardkoda `case`-grener
   - **Merk:** høgare kompleksitet enn A1 (to jobbar, ikkje éin fil) — gjer
     dette som eit eige, godt testa delsteg, gjerne på ein testgrein før
     merge til main, sidan CI-workflows er tunge å teste lokalt

3. **A3 — `tests/test_make.sh`:** legg til ei hjelpefunksjon
   `is_geo_referert_uten_tree_root()` (eller liknande dekkjande namn) nær
   toppen av fila, erstatt dei 5 identiske `if`-vilkåra med kall til henne

4. **B1 — `find_released_packages()`:** flytt til
   `src/assets/scripts/utils/release_helpers.py`, importer frå både
   `update-schema-dates.py` og `makefile/run-schema-validation.py`

5. **B2 — `get_domain_model()` (+ B6 `get_version()`, forsiktig):** flytt
   til ny `src/assets/scripts/utils/schema_meta.py`. For `get_version()`:
   behald eksistenssjekken frå `save-validation-log.py` (den strengaste
   varianten) og gjer fallback-verdien til eit parameter
   (`get_version(schema_path, fallback="0.0.0")`) slik begge kallstader kan
   få sin opphavlege standardverdi

6. **B3 — `load_yaml_meta()` + `rewrite_refs()`:** flytt til
   `src/assets/scripts/makefile/api_spec_common.py` (smalt scope — berre
   AsyncAPI/OpenAPI-generering — held han ute av den generelle `utils/`-mappa)

7. **B4 + B5 — `write_yaml()` og `load_yaml()`:** flytt til ny
   `src/assets/scripts/utils/yaml_io.py`:
   - `load_yaml(path) -> dict` — bruk den strengaste varianten
     (`gen-dqv-measurements.py` sin `or {}`-fallback mot `None`)
   - `write_yaml(file_path, data, generated_by: str)` — `generated_by` vert
     sett til kallande script sitt filnamn (`Path(__file__).name`) i staden
     for hardkoda per fil
   - Oppdater alle 5 (`load_yaml`) / 3 (`write_yaml`) kallstadene

8. **C1 — Macro-iser `make/80-images.mk`:** følg same `define X ... endef` +
   `$(eval $(call X,...))`-mønster som `domain_target` i
   `make/20-domain-targets.mk`. Behald `##`-hjelpetekst-kommentarane slik
   `make help` (om det finst) framleis fungerer.

9. **C2 — Undersøk (ikkje nødvendigvis fiks) serial/parallel-para:** test om
   `xargs -P 1` gir identisk (rekkjefølgje, lesbarheit) output som dagens
   serielle `run_gen_X`-makroar for eitt konkret par (t.d. `run_gen_doc` /
   `run_gen_doc_parallel`). Dersom identisk: vurder å fjerne det serielle
   sporet og alltid bruke `xargs -P $(PARALLEL)` (der `PARALLEL=1` er
   spesialtilfellet). Dersom *ikkje* identisk (t.d. interleava output ved
   feil): dokumenter kvifor dei to spora må halde fram å eksistere separat,
   og la vere å endre.

10. **Test og verifiser kvart steg isolert** (ikkje samla til slutt):
    - Python: `python3 -m py_compile` på alle endra/nye filer + eit
      funksjonelt smoke-test av kvart flytta script (samanlikn output før/etter)
    - Make: `make -n` (dry-run) på minst eitt domene per endra makro, pluss
      ei reell `make domain-<x>`-køyring
    - CI: valider YAML-syntaks lokalt (`python3 -c "import yaml; ..."`),
      og vurder om `act` (lokal GitHub Actions-simulator) er tilgjengeleg
      for å teste A1/A2 før push — elles merk desse stega som "krev
      verifisering i CI etter push" i staden for å hevde dei er testa lokalt

11. **Oppdater `specs/done/`-referansar:** når alle steg er fullførte, flytt
    denne spec-en til `specs/done/dry-opprydding.md` og legg til ei kort
    kryssreferanse i `CLAUDE.md` sitt DRY-avsnitt (linje 34) om at
    make-/Python-/CI-laget no òg følgjer regelen systematisk (unngår å
    duplisere forklaringa — berre ei lenkje, jf. CLAUDE.md sin eigen
    DRY-regel for CLAUDE.md-innhald).

## Rekkjefølgje og risiko

Stega er lista i aukande kompleksitet/risiko, ikkje i påkravd rekkjefølgje —
dei er stort sett uavhengige av kvarandre. Anbefalt prioritet dersom dei
skal utførast gradvis:

1. **Høgast verdi, lågast risiko:** A1 (direkte hindrar gjentaking av
   referanse-bugen), A3, B1-B7, C1 — reint lokale, lett verifiserbare endringar
2. **Høgare risiko, krev meir testing:** A2 (fleire CI-jobbar involvert)
3. **Undersøkjande, kan ende med "ikkje fiks":** C2

## Akseptansekriterium

- [ ] Domeneliste finst berre éin stad (autoritativ kjelde), alle 4 CI-stadene
      les derifrå
- [ ] Image-metadata finst berre éin stad, både matrise og pull-logikk les derifrå
- [ ] `tests/test_make.sh` sitt `ap-no`/`fair`-vilkår finst berre éin stad
- [ ] `find_released_packages`, `get_domain_model`, `load_yaml_meta`,
      `rewrite_refs`, `write_yaml`, `load_yaml` finst berre éin stad kvar,
      importert der dei trengst
- [ ] `get_version` har parametrisert fallback, begge kallstader har
      identisk åtferd som før konsolideringa
- [ ] `make/80-images.mk` bruker macro-mønster, alle 6 image byggjer framleis
      korrekt (`make build-docker-<x>` for kvar)
- [ ] C2 er anten fiksa (dokumentert kvifor det var trygt) eller eksplisitt
      late urørt med grunngjeving i kommentar
- [ ] Ingen regresjon: alle eksisterande `make`-targets og CI-workflows
      fungerer identisk som før, verifisert per steg (ikkje berre til slutt)

## Framdrift

**Steg A1-A3 utført** (2026-08-04):

- **A1:** Nytt `make print-domains`-target (`make/02-schema-discovery.mk`)
  skriv ut `$(DOMAINS)`, eitt domene per linje — same autoritative variabel
  `make domain-<x>` alt brukar. Begge workflow-filer har no eit
  "Oppdag domene"-steg i `checkout-source`-jobben som køyrer det og
  eksporterer resultatet både som JSON (til `strategy.matrix.domain`) og
  space-separert liste (til dei to `for domain in ...`-løkkene). Alle 4
  opphavlege hardkoda 9-domene-listene er fjerna.
- **A2:** Ny `src/assets/containers/images.json` er autoritativ kjelde for
  namn/Dockerfile/make-target for alle 7 image, pluss kva `build.yaml`-flagg
  som utløyser kvart betinga image. `ensure-images`-matrisa i `generate.yml`
  hentar no biletlista derifrå (`fromJson(...)`). GHCR-tag-hashen kan ikkje
  reknast ut frå JSON-fila ved køyretid (GitHub sin `hashFiles()` er eit
  parse-tids-uttrykk, ikkje kallbart frå bash) — løyst ved å rekne alle 7
  taggane ut **éin gong** i eit nytt steg i `checkout-source`
  ("Bygg image-tag-oppslag"), eksportert som eit namn→tag-oppslag som både
  `ensure-images` og `generate`-jobben sin `pull_image`-logikk slår opp i.
  Den 30-linjers `case`-setninga med 6× duplisert `hashFiles()`-kall er
  bytt ut med ein generisk 3-linjers løkke.
  **Bonus-funn:** `detect-images`-steget sjekka `^  avro: true` i
  `build.yaml`, men det faktiske manifest-feltet er `xsd: true` (jf.
  `CONVENTIONS.md` og `samt-bu/build.yaml`) — `avrotize-local` vart difor
  **aldri** lagt til `REQUIRED_IMAGES` for noko domene i CI, uansett innhald
  i `build.yaml`. Retta samtidig som feltet vart flytta til `images.json`
  (`required_if_generator_flag: "xsd"`), sidan det var same kodeblokk som
  vart gjort datadriven. Stadfesta lokalt: `samt`-domenet (som har
  `xsd: true`) fekk før fiksen ALDRI `avrotize-local` i lista, no gjer det.
  **Ikkje utført:** `validate.yml` har ei mindre, analog duplisering
  (2 image, ingen `case`-setning) mellom sin eigen `ensure-images`-matrise
  og sine to faste "Hent X frå GHCR"-steg. Sidan `generate.yml` og
  `validate.yml` er heilt separate workflow-køyringar (ingen `needs`-deling
  mogleg på tvers av filer), krev full samanslåing ein delt *composite
  action* (`.github/actions/`) — eit større steg enn resten av A2. Ikkje
  gjort no; naturleg oppfølging.
- **A3:** Ny `lacks_tree_root()`-hjelpefunksjon i `tests/test_make.sh` (ved
  sida av den eksisterande `schema_domain()`), erstattar alle 5 identiske
  `if [[ "$domain" == "ap-no" || "$domain" == "fair" ]]`-vilkår.

**Verifisert:**
- `make print-domains` produserer identisk domenesett som den gamle
  hardkoda lista (stadfesta med `diff`)
- `detect-images`-logikken testa mot reelle `build.yaml`-filer:
  `samt`-domenet får no korrekt `avrotize-local` +
  `asyncapi-cli-minimal`, `referanse` får berre dei 4 basisimaga
- Image-tag-oppslaget (JSON-konstruksjon + `jq`-oppslag i pull-løkka) testa
  med simulerte hash-verdiar — alle 6 image slår opp korrekt `make_target`
  og `tag`
- `lacks_tree_root()` testa isolert mot fleire domenenamn
- Alle YAML-filer validert med `python3 -c "import yaml; ..."`,
  `bash -n` på `tests/test_make.sh`, jobb-avhengigheiter (`needs:`)
  kontrollert programmatisk i begge workflow-filer
- **Ikkje verifisert:** faktisk køyring i GitHub Actions (kan ikkje testast
  lokalt) — `${{ fromJson(...)[...] }}`-uttrykket for dynamisk
  objekt-oppslag i `ensure-images` er ny bruk av dette mønsteret i repoet.
  Bør overvakast nøye ved neste push til main, evt. testast fyrst med
  `workflow_dispatch` manuelt.

**Steg B1-B6 utført** (2026-08-04):

Alle 6 dupliserte Python-funksjonar flytta til delte, samanhengande modular
— kvar funksjon finst no berre éin stad (stadfesta med `grep -rl` mot heile
`src/assets/scripts/`):

| Funksjon(ar) | Ny plassering | Kallstader oppdatert |
|---|---|---|
| B1: `find_released_packages` | `utils/release_helpers.py` | `update-schema-dates.py`, `makefile/run-schema-validation.py` |
| B2/B6: `get_domain_model`, `get_version` | `utils/schema_meta.py` | `makefile/save-validation-log.py`, `makefile/run-schema-validation.py` |
| B3: `load_yaml_meta`, `rewrite_refs` | `makefile/api_spec_common.py` (smalt scope, sidan sibling-import) | `makefile/gen-asyncapi.py`, `makefile/gen-openapi.py` |
| B4/B5: `write_yaml`, `load_yaml` | `utils/yaml_io.py` | `makefile/collect-concepts.py`, `makefile/generate-modellkatalog.py`, `makefile/generate-informasjonsmodell.py`, `makefile/gen-docgen-examples.py`, `makefile/gen-dqv-measurements.py` |

**Designval undervegs:**
- `get_version(schema_path, fallback="0.0.0")`: fallback parametrisert som
  spec-en bad om — `save-validation-log.py` sender eksplisitt
  `fallback="0.0.0-dev"`, `run-schema-validation.py` brukar default. Begge
  sine opphavlege standardverdiar er bevart, stadfesta med direkte kall mot
  begge variantane.
- `load_yaml(path) -> Dict`: brukar den strengaste varianten
  (`or {}`-fallback mot tom/`None`-fil) frå `gen-dqv-measurements.py`, slik
  spec-en bad om. Verifisert at ingen av dei 5 kallstadene gjer eksplisitt
  `is None`-sjekk som ville brote med denne endringa.
- `write_yaml(file_path, data, generated_by, note="")`: `note` vart lagt
  til som eit ekstra, valfritt parameter (utover det spec-en eksplisitt
  nemnde) for å bevare den domenespesifikke andre kommentarlinja kvar av
  dei 3 originalfilene hadde — unngår å miste informasjon berre for å
  konsolidere. Stadfesta byte-identisk header-output for alle 3 kallstader.
- `gen-docgen-examples.py` sin eksisterande `try/except ImportError`-vakt
  for PyYAML er bevart urørt (importen av `utils.yaml_io` skjer *etter*
  vakta, ikkje før) — mister ikkje den vennlege feilmeldinga viss PyYAML
  skulle mangle.

**Verifisert:**
- `python3 -m py_compile` på alle 14 involverte filer (4 nye + 10 endra)
- Delt-objekt-identitet stadfesta for alle 6 funksjonar: importerte i fleire
  filer, viser identisk minneadresse — bevis på faktisk delt kode, ikkje
  berre identisk tekst
- Reell CLI-køyring av `gen-openapi.py`/`gen-asyncapi.py` mot generert
  `samt-bu`-skjema — korrekt output, byte-for-byte samanlikna manuelt
- Reell køyring av `collect-concepts.py` mot ekte repo-data: output
  **byte-identisk** med det som alt var committa (stadfesta med
  `git diff` — tomt)
- `generate-modellkatalog.py`: **viktig funn under testing** — reell
  køyring overskreiv 5 committa modellkatalog-datafiler med sterkt
  reduserte data, fordi mitt lokale arbeidstre berre har
  `metadata/*-manifest.yaml` generert for eitt domene (`referanse`) denne
  økta, ikkje alle. Dette er **ikkje** ein regresjon frå refaktoreringa —
  det er ein konsekvens av at scriptet aggregerer frå eit ufullstendig
  lokalt datagrunnlag. Endringane vart øyeblikkeleg reverterte
  (`git checkout --`), og `write_yaml`-bruken vart i staden verifisert
  trygt/isolert (mot ein midlertidig testfil, ikkje ekte repo-data).
- `gen-dqv-measurements.py` testa med `--dry-run` (scriptet skriv elles
  attende til ekte datafiler — unngjekk å røre committa data)
- `gen-docgen-examples.py` testa mot ein midlertidig output-katalog

**Steg C1-C2 utført** (2026-08-04):

- **C1 — `make/80-images.mk`:** Forsøkte fyrst full `$(eval $(call ...))`-
  macro-isering (same mønster som `domain_target`), men støytte på to
  problem som gjorde det opphavlege designet feil, begge stadfesta
  empirisk med `make -n` før dei vart retta:
  1. `$(GOURCE_DOCKERFILE)`/`$(GOURCE_IMAGE)` (definerte i
     `make/90-tools.mk`, inkludert *etter* `80-images.mk`) vart expandert
     til tomt fordi call-argument vert evaluert eagerly ved parse-tid —
     løyst ved å escape call-argumenta (`$$(...)`), som utset oppslaget
     til køyretid.
  2. Sjølv med (1) retta, viste det seg at `make help` sitt
     hjelpetekst-oppslag grep'ar KJELDEFILA på disk — `$(eval ...)`-
     generert target-tekst finst berre i Make sin minnetilstand, aldri
     på disk, og vart difor usynleg i `make help`. Sidan spec-en
     eksplisitt kravde at `make help` skal halde fram å fungere, vart
     designet lagt om: kvar target står att som literal, grep-bar tekst
     (namn + `##`-beskriving), medan sjølve den repeterte `podman build`-
     oppskrifta er delt via ein liten `docker_build`-makro brukt frå kvart
     target sin recipe. Reduserer duplikasjonen frå 6×3 linjer til 6×2 +
     éin delt makro, utan å ofre `make help`-discoverability.
  - La i tillegg til den manglande `PLANTUML_DOCKERFILE`-variabelen i
    `make/00-settings.mk` (fanst berre `PLANTUML_IMAGE` frå før) for
    konsistens med alle andre image-variablar.
  - Verifisert: alle 6 `make -n build-docker-<x>` gir identisk kommando
    som før endringa (inkl. den opphavlege, uendra "."-inkonsistensen per
    image), `make help` listar alle 6 med korrekt beskriving, og ein reell
    `make build-docker-plantuml` fullførte utan feil.

- **C2 — serial/parallel-undersøking:** Testen avdekte noko meir alvorleg
  enn spec-en la opp til: `run_parallel_with_timer` sin
  `PARALLEL=1`-fallback (som kalla serial-makroen direkte via
  `$(call $(3),$(1))`) var **reelt øydelagd** — serial-makroane sin eigen
  leiande `@` (t.d. `run_gen_linkml_serial` sin `@$(foreach ...)`) hamna
  midt i ei bash-linje når han vart substituert inn i
  `if ...; then $(call $(3),$(1)) ...`-blokka, og feila umiddelbart med
  `bash: @: command not found`. Stadfesta med `make domain-referanse
  PARALLEL=1` (feila før endringa) — ein bug som truleg aldri vart
  oppdaga sidan `PARALLEL` sin standardverdi er 16, ikkje 1.
  - **Fiks:** fjerna `if [ "$(PARALLEL)" = "1" ]; then ... else ... fi`-
    grena heilt frå `run_parallel_with_timer` — han bruker no alltid
    `xargs -P $(PARALLEL)` (der `PARALLEL=1` berre gjev éin jobb om
    gongen, funksjonelt identisk med den tiltenkte serielle åtferda).
    Fjerna det no ubrukte 3. arg (serial-makro-namn) frå alle 7 kallstader.
  - **Viktig presisering oppdaga undervegs:** dei "serielle" makroane
    (`run_gen`, `run_gen_owl`, `run_gen_rdf`, `run_gen_doc`,
    `run_gen_erdiagram`, `run_gen_plantuml`, `run_gen_openapi`,
    `run_gen_asyncapi`) er **ikkje** reindyrka PARALLEL=1-fallbacks — dei
    vert også brukt direkte av dei frittståande `make gen-doc`/`make
    gen-openapi`/osv-targeta i `make/11-generator-targets.mk` (ein annan,
    legitim bruksmåte: eitt skjema/domene om gongen, utanfor
    domain-byggjepipelinen). Desse makroane er difor **ikkje** fjerna —
    berre den øydelagde PARALLEL=1-kopling-mekanismen i
    `run_parallel_with_timer` er fjerna. Oppdaterte dei no misvisande
    "(fallback ... PARALLEL=1)"-kommentarane til å forklare dette presist.
  - **`run_gen_linkml_serial` var derimot 100 % daud kode** (ingen
    frittståande `gen-linkml`-target finst) — fjerna heilt.
  - **Ikkje utført/utanfor omfang:** `domain_target` har sin eigen,
    tredje kopi av openapi/asyncapi-logikken hand-duplisert direkte inn i
    `PARALLEL=1`-grenene (linje 73-118 i `make/20-domain-targets.mk`,
    IKKJE via `run_gen_openapi`/`run_gen_asyncapi`). Denne fungerer
    korrekt i dag (ingen bug), men er ei ekstra, urelatert duplisering
    utover det opphavlege "eitt par"-scopet spec-en peika på — flagga som
    funn, ikkje fiksa, for å halde denne økta sitt endringsomfang
    handterleg.
  - Verifisert: to fulle `make domain-<x> PARALLEL=1`-køyringar
    (referanse, samt — sistnemnde med xsd+openapi+asyncapi) fullførte
    korrekt (var *totalt* øydelagt før), pluss ei full
    `make domain-samt`-køyring med standard `PARALLEL=16` for å stadfeste
    ingen regresjon i normalsporet. Alle 7 råka makro-par eksercert.

## Framdrift — status

Alle steg A, B og C (A1-A3, B1-B6, C1-C2) er no fullførte og verifiserte.
Attståande: steg 10 (samla testverifisering — dekt løpande per steg over,
ikkje eit eige gjenstående arbeid) og steg 11 (dokumentasjon: flytt denne
spec-en til `specs/done/` og legg til kryssreferanse i `CLAUDE.md`).

## Utført

Alle 11 steg fullførte. Oppsummert per kategori (sjå "Framdrift" over for
fullstendige detaljar og verifikasjon per steg):

- **A (hardkoda lister → dynamiske):** domeneliste utleia frå
  `make print-domains` i staden for 4 hardkoda kopiar; image-metadata
  samla i `src/assets/containers/images.json`; `tests/test_make.sh` sitt
  `ap-no`/`fair`-vilkår konsolidert til éin funksjon
- **B (dupliserte Python-funksjonar):** 6 funksjonar flytta til delte,
  samanhengande modular (`utils/release_helpers.py`, `utils/schema_meta.py`,
  `makefile/api_spec_common.py`, `utils/yaml_io.py`)
- **C (Makefile-strukturell duplikasjon):** `make/80-images.mk` sine 6
  build-target deler no ein `docker_build`-makro; det viktigaste funnet var
  likevel at `run_parallel_with_timer` sin `PARALLEL=1`-fallback var reelt
  øydelagd — fiksa, med `run_gen_linkml_serial` fjerna som daud kode

**Ekstra funn undervegs** (utover den opphavlege planen):
- Ein `avro`→`xsd`-feilnamngjeving i `generate.yml` sitt `detect-images`-steg
  gjorde at `avrotize-local` aldri vart lagt til CI sin image-liste for noko
  domene — retta som del av A2
- `domain_target` sin tredje, hand-duplikerte kopi av openapi/asyncapi-logikk
  (`make/20-domain-targets.mk` linje 73-118) — identifisert, ikkje fiksa
  (utanfor økta sitt handterlege omfang, fungerer korrekt i dag)
- `validate.yml` har ei mindre, analog image-metadata-duplisering til A2 sitt
  `generate.yml`-funn — krev ein delt composite action for full løysing sidan
  workflow-filer ikkje deler `needs`-output; ikkje gjort

Alt verifisert lokalt gjennom heile arbeidet: reelle domenebyggjer
(`make domain-referanse`, `make domain-samt`) under både `PARALLEL=1` og
standard `PARALLEL=16`, `py_compile` på alle nye/endra Python-filer,
delt-objekt-identitet stadfesta for konsoliderte funksjonar, YAML-syntaks og
jobb-avhengigheiter kontrollert programmatisk for CI-workflows, og
funksjonstestar av kvar enkelt fiks mot både gyldig og korrupt/manglande input.

## Relaterte filer

- `.github/workflows/generate.yml`, `.github/workflows/validate.yml` — A1, A2
- `tests/test_make.sh` — A3
- `src/assets/scripts/update-schema-dates.py`,
  `src/assets/scripts/makefile/run-schema-validation.py` — B1, B6
- `src/assets/scripts/makefile/save-validation-log.py` — B2, B6
- `src/assets/scripts/makefile/gen-asyncapi.py`,
  `src/assets/scripts/makefile/gen-openapi.py` — B3
- `src/assets/scripts/makefile/collect-concepts.py`,
  `src/assets/scripts/makefile/generate-modellkatalog.py`,
  `src/assets/scripts/makefile/generate-informasjonsmodell.py` — B4, B5
- `src/assets/scripts/makefile/gen-docgen-examples.py`,
  `src/assets/scripts/makefile/gen-dqv-measurements.py` — B5
- `make/80-images.mk`, `make/20-domain-targets.mk` (mønster-referanse) — C1
- `make/10-generator-macros.mk` — C2
- `make/02-schema-discovery.mk` — kjelde for `print-domains`-targetet i A1
- `CLAUDE.md` — DRY-regelen (linje 34) som denne spec-en realiserer for nye lag
- `specs/done/debug-referanse-nav-meny.md` — den konkrete bugen som motiverer A1
