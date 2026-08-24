# Erstatt "namn" med "navn" i heile repoet (fase 2 — kode/CI/tests)

## Bakgrunn

Brukaren bad om ein spec for å byte ut **namn** (konservativ nynorskform,
sjeldan i bruk) med **navn** (bokmål) i heile repoet. `namn`→`navn` er alt
eit dokumentert unntak frå den generelle nynorsk-for-dokumentasjon-regelen
(CLAUDE.md § Skriftspråk, «Unntak — enkeltord i bokmålsform»).

**Dette er IKKJE eit blankt ark.** Eit tidlegare, fullført tiltak
(`specs/done/erstatt-namn-med-navn.md`) gjorde alt ein full
"namn"→"navn"-runde, men avgrensa seg eksplisitt til
**dokumentasjon og LinkML-skjema** — «Kode og CI (`*.py`, `*.sh`,
`.github/**/*.yml`, `tests/**`) — brukaren sitt oppdrag gjaldt
dokumentasjon og LinkML-skjema, ikkje programidentifikatorar» (sitat frå
den specen sin § «Eksplisitt utanfor scope»). Eit ferskt repo-søk
(`grep -rlIE '\bnamn\b'`, ekskl. `specs/`, `CHANGELOG.md`) stadfestar at
det attverande biletet i dag er nett dette: **kode/CI/tests** (som vart
medvite utelate då) pluss ei handfull nye/attverande dokumentasjons-
tilfelle som har dukka opp sidan (nytt innhald, eller mekaniske treff som
vart forbigått).

Denne specen er difor **fase 2**: lukk att det som vart medvite utsett i
fase 1, pluss dei få attverande dokumentasjonstilfella. Same metodikk og
avgrensingar (spesielt `specs/done/`-arkivet urørt) held fram uendra.

## Kartlegging (verifisert med `grep`, éin og éin fil lese for kontekst)

### A — Lågrisiko: rein prosa i kommentarar/docstrings/hjelpetekst

Ingen identifikatorendring — berre nynorsk ord i kode- og
CI-kommentarar/`description:`-felt/log- og hjelpetekst. Mekanisk
"namn"→"navn" (case-bevarande, inkl. samansetjingar som
`namnerom`→`navnerom`, `filnamn`→`filnavn`, `slotnamnkonvensjonar`→
`slotnavnkonvensjonar`, `klassnamn`→`klassnavn`), same metode som fase 1
sin del A:

| Fil | Førekomstar | Merknad |
|---|---|---|
| `CLAUDE.md` | 1 (linje 156) | `fil-/mappenamn`, `slotnamnkonvensjonar` — samansetjingar forbigått av fase 1. **Linje 135 (`\| namn \| navn \|`) og linje 138 (spec-filnamn-referanse) skal IKKJE endrast** — sjå § Eksplisitt utanfor scope |
| `COMMANDS.md` | 3 | `id/namn/tittel`, `kolliderer med namn`, `same namn som`, plassholdaren `<namn>` i eit eksempel på feilmelding |
| `mkdocs/docs/kom-i-gang/build-config.md` | 1 | Plasshaldar `<delmodell-namn>` → `<delmodell-navn>` |
| `mkdocs/docs/kom-i-gang/ny-domenemodell.md` | 3 | `$defs`/`definitions`-namn, `id/namn/tittel`, `eit namn som alt finst` |
| `.github/lychee.toml` | 11 | Alle i kommentarar: `namnerommet` (×~6), `<namn>`-plasshaldar, `temanamn` (×2) |
| `.github/workflows/release-please.yml` | 1 | Kommentar: `tag-namn` |
| `.github/workflows/validate.yml` | 3 | Kommentarar: `instance-<namn>.json`, `Event-namnet`, `filnamn` |
| `.github/actions/compute-image-tags/action.yml` | 2 | `description:`-felt: `namn/Dockerfile/make-target`, `{namn: hash-tag}` — stadfesta reint prosa-skildring av JSON-forma, **ikkje** ein reell JSON-nøkkel (verifisert mot faktisk output — nøklane er bilettnamn som `linkml-local`) |
| `.github/actions/ensure-image/action.yml` | 1 | `description:`: `Image-namn` |
| `.github/actions/pull-images/action.yml` | 2 | `description:`: `<namn>`-plasshaldar, `{namn: hash-tag}` (same grunngjeving som over) |
| `make/00-settings.mk`, `make/03-output.mk`, `make/10-generator-macros.mk`, `make/11-generator-targets.mk`, `make/20-domain-targets.mk`, `make/40-validation.mk` | ukjent presist tal, verifiser ved utføring | `##`-kommentarar/hjelpetekst |
| `make/70-scaffolding.mk` | verifiser | Fase 1 (`namn-navn-konsistens-make-help.md`) fiksa `NAME=<namn>`→`NAME=<modell>`/`<begrepssamling-navn>` for `new-modell`/`remove-modell`/`new-begrepssamling` spesifikt — verifiser at ingen andre `namn`-tilfelle attstår i same fil (t.d. interne kodekommentarar som `namnekolonna`) |
| `mkdocs/lib/scripts/check-mermaid-click-hrefs.py` | verifiser | Docstring/kommentar |
| `mkdocs/lib/sections/avhengigheiter.sh`, `badges.sh`, `classes.sh` | verifiser | Kommentarar — **ikkje** shell-variabelnamn (stadfesta med `grep -nE '\$\{?namn'` — null treff) |
| `mkdocs/lib/utils/imported_schemas.sh` | verifiser | Kommentar |
| `mkdocs/publish.sh` | verifiser | Kommentarar — same stadfesting som over, ingen `namn`-variablar |
| `src/assets/containers/Dockerfile.mcp-linkml` | verifiser | Kommentar |
| `src/assets/scripts/makefile/check-import-duplicates.py`, `collect-concepts.py`, `find-similar-names.py`, `find-unused-local-definitions.py`, `save-validation-log.py`, `update-modellkatalog.py` | verifiser | Docstrings/kommentarar/loggtekst — **ikkje** dict-/variabelnøklar (stadfesta) |
| `src/assets/scripts/makefile/help.sh` | verifiser | Interne kodekommentarar (jf. fase 1 sitt funn om at desse er utviklarvendte, ikkje CLI-output — framleis korrekt å rette som prosa) |
| `src/assets/scripts/migreringsscript/migrate-schema-metadata.sh` | verifiser | Kommentar |
| `src/assets/scripts/scaffolding/new-begrepssamling.sh`, `new-modell.sh`, `new-modellkatalog.sh`, `remove-modell.sh` | verifiser | Kommentarar — verifiser samstundes at ingen `log_error`/brukarvendt hjelpetekst framleis viser `<namn>` (bør alt vere retta via fase 1 sin `make/70-scaffolding.mk`-fiks, men scripta sjølve har eigne `Bruk: ...`-meldingar som ikkje vart dekte då) |
| `src/mcp-linkml-modell-utkast/converter.py` | 2 | Kommentarar: `container-slot-namn`, `{ klassnamn: {...} }` (skildrar ein dict-form i ein kommentar, **ikkje** ein reell nøkkel — stadfesta) |
| `src/mcp-linkml-modell-utkast/validator.py` | verifiser | Kommentar |
| `src/mcp-linkml-validator/server.py` | verifiser | Kommentar/docstring |
| `src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml` | 1 | `# TODO: Gi stub-klassen eit meir meiningsfullt namn.` — **NB: dette skjemaet ser ut til å vere under aktiv utvikling i ei anna, samstundes køyrande økt** (stadfesta gjennom fleire tidlegare turar denne sesjonen) — verifiser at skjemaet framleis eksisterer i denne forma før endring, ikkje overskriv pågåande arbeid |
| `specs/backlog/javazone-demo-plan.md` | 8 | Aktiv backlog-spec (ikkje arkivert), fleire reelle enkeltord-tilfelle (`kva namn`, `NAME=<namn>`, `Eit vilkårleg namn») — **same åtvaring som over**: kan vere under aktiv redigering samstundes, sjekk på nytt før endring |
| `tests/test_check_import_duplicates.py`, `tests/test_mcp_linkml_generator.py` (docstring/kommentar-delen, ikkje fixture-delen — sjå del B), `tests/test-mcp-linkml-generator.json`, `tests/test_make.sh` | verifiser | Kommentarar/docstrings — stadfesta ingen `namn`-shell-variablar i `test_make.sh` |

### B — Moderat risiko: sjølvstendige testfixture-identifikatorar

Faktiske YAML/JSON-nøklar i testfixturar (ikkje berre prosa), men
konsekvensen er avgrensa til testfila sjølv (ingen ekstern kontrakt) —
krev at nøkkel + alle tilhøyrande assertions vert endra saman, elles
feilar testen:

- **`tests/test_mcp_server.py`** — `namn:` som LinkML-slotnøkkel i
  innebygd YAML-testfixtur (linje 39, 40 [`description: Personens
  namn`], 70, 97). Same mønster som dei reelle skjema-rettingane i fase 1
  sin del D (`ngr-adresse`, `cpsv-ap-no` osv.) — testar sannsynlegvis
  nett den slot-namngjevingskonvensjonen. Rett nøkkel + skildringstekst
  saman, køyr testen etterpå.
- **`tests/test_mcp_linkml_generator.py`** — `"namn"` som JSON
  Schema-eigenskapsnøkkel i testfixtur (linje 88, 91, 96, 97, 113 m.fl.),
  brukt i `assertEqual`/`assertTrue`-assertions mot resultatet frå
  `mcp-linkml-modell-utkast` sin JSON→LinkML-konverterar. Rett nøkkel i
  BÅDE input-fixture og assertions saman — ein delvis retting vil få
  testen til å feile stille (feil nøkkel i assertion mot korrekt output,
  eller omvendt).

### C — Høg risiko: ekstern MCP-verktøykontrakt (krev eksplisitt avklaring)

**`src/mcp-linkml-begrep-utkast/los_tema.py`** — den statiske
`LOS_TEMA`-lista brukar `"namn"` som ordbok-nøkkel for **kvart einaste**
LOS-tema-oppslag (~90 førekomstar, t.d. `{"uri": "...", "namn":
"Næringsliv"}`). Dette er **ikkje** eit reint dokumentasjonstilfelle:
`src/mcp-linkml-begrep-utkast/server.py` sin `_handle_list_los_tema()`
serialiserer `LOS_TEMA` **direkte og uendra** (`json.dumps(LOS_TEMA,
...)`) som svaret på MCP-verktøyet `list_los_tema` — `"namn"` er difor
del av den **faktiske, eksterne JSON-kontrakten** eit MCP-klientkall ser i
svaret sitt, ikkje berre eit internt Python-datastrukturval.

Fase 1 sin spec identifiserte nett dette tilfellet og sette det
eksplisitt utanfor eige scope: «kan takast som eiga oppfølging om
ønskt» — denne specen er den oppfølginga.

**Konsekvens av å endre:** ein MCP-klient (t.d. eit LLM-kall via
`opprett_begrep`-arbeidsflyten, sjå `mcp__linkml-begrep-utkast__list_los_tema`)
som alt forventar `"namn"`-nøkkelen i svaret, vil få eit anna feltnamn
(`"navn"`) etter denne endringa. Sidan dette er eit lokalt/internt
MCP-verktøy (ikkje ein publisert, versjonert ekstern API), er den
praktiske risikoen truleg låg — men det er framleis ei åtferdsendring i
verktøyet sitt grensesnitt, ikkje ei rein tekstretting.

**Tilråding:** avklar eksplisitt med brukaren FØR utføring om denne
nøkkelen skal endrast. Dersom ja: rett alle ~90 førekomstar i
`los_tema.py` (mekanisk, sidan dei er identisk formaterte), verifiser at
`server.py` ikkje har anna kode som les `"namn"` eksplisitt (stadfesta i
kartlegginga at han berre passthrough-serialiserer), og køyr
`tests/test_mcp_server.py`/relevante MCP-testar etterpå.

## Eksplisitt utanfor scope (vidareført frå fase 1, uendra grunngjeving)

- **`specs/done/` og `specs/rejected/`** — arkiv, urørt. Gjeld òg
  filnamna sjølve: `specs/done/make-target-namn-vs-funksjon.md`,
  `specs/done/namn-navn-konsistens-make-help.md`,
  `specs/done/erstatt-namn-med-navn.md` skal **ikkje** endrast/omdøypast.
- **Lenkjer FRÅ levande dokumentasjon TIL desse arkiverte filnamna** —
  stadfesta to stader: `mkdocs/docs/kom-i-gang/ny-begrepsmodell.md:7` og
  `ny-org.md:93` lenkar begge til
  `specs/done/make-target-namn-vs-funksjon.md`. Dette er **korrekte
  lenkjer** til eit faktisk filnamn — å endre lenkjeteksten utan å
  omdøype fila ville brote lenkja. La stå urørt.
- **`CHANGELOG.md`-filer** — auto-genererte av `release-please`, vert
  overskrivne ved neste release.
- **`CLAUDE.md` linje 135** (`| namn | navn |`) — dette ER
  unntakstabellen sjølv, som eksplisitt namngjev ordet «namn» som forma
  ein skal *unngå*. Å endre denne rada ville sletta regelen sitt eige
  innhald.
- **Nynorsk-språkverdiar med vilje** (`_nn`-felt, jf. fase 1 sitt punkt
  om `foretaksnamn.yaml`/`brreg-begrepskatalog.yaml`) — uendra, ikkje
  re-verifisert i detalj her sidan fase 1 alt gjekk gjennom desse
  spesifikt; stikkprøve ved utføring anbefalt sidan begrepskatalog-data
  kan ha vakse sidan.
- **Genererte modellkatalog-/manifest-datafiler** — regenererast, vert
  ikkje handretta (same grunngjeving som fase 1 sitt punkt G).

## Tiltak / handlingsliste

1. **Avklar del C (los_tema.py) med brukaren FØR utføring** — dette er
   einaste punktet som treng eit reelt val, ikkje berre mekanisk
   utføring (sjå § Høg risiko over).
2. **Del A — mekanisk prosa-erstatning**, fil for fil, case-bevarande
   (Namn→Navn, NAMN→NAVN, namn→navn), inkludert samansetjingar. Hopp
   over linjene eksplisitt nemnde i § Eksplisitt utanfor scope. Verifiser
   `javazonetalk-schema.yaml` og `specs/backlog/javazone-demo-plan.md`
   sin gjeldande tilstand på nytt før endring (moglegvis endra av
   samstundes arbeid, jf. åtvaringane i kartlegginga).
3. **Del B — testfixture-identifikatorar**: rett nøkkel + assertions
   saman i `tests/test_mcp_server.py` og `tests/test_mcp_linkml_generator.py`,
   køyr testane, stadfest grøn status.
4. **Del C — utfør berre dersom brukaren stadfestar (steg 1)**: rett
   `los_tema.py`, verifiser `server.py` uendra treng ingen kodeendring,
   køyr `tests/test_mcp_server.py`.
5. **Actionlint** på alle endra `.github/workflows/*.yml`-filer (jf.
   CLAUDE.md "Actionlint etter CI-endring") — sjølv om endringane her
   berre er kommentartekst, ikkje `${{ }}`-uttrykk, køyr likevel for å
   stadfeste ingen utilsikta syntaksbrot.
6. **Verifiser sluttilstand**: `grep -rlIE '\bnamn\b' . --exclude-dir=.git
   --exclude-dir=specs --exclude=CHANGELOG.md` bør etter dette berre
   treffe filer som er eksplisitt lista i § Eksplisitt utanfor scope
   (dvs. ingen, sidan alle attverande unntak ligg i `specs/`/`CLAUDE.md`
   linje 135, som ekskluderast av søket sjølv eller er eksplisitt
   grunngjevne unntak).

## Akseptansekriterium

- [x] Brukaren har eksplisitt teke stilling til del C (los_tema.py) før
      den delen vert utført — stadfesta ja
- [x] Alle del A-filer mekanisk retta, ingen nye avvik introduserte
      (stikkprøve: `grep -c namn <fil>` før/etter matchar forventa diff)
- [x] `tests/test_mcp_server.py` og `tests/test_mcp_linkml_generator.py`
      grøne etter del B (`test_mcp_server.py`: 10 feilar/19 grøne, identisk
      feilsett før/etter stadfesta via `git stash` — ikkje forårsaka av
      denne endringa; `test_mcp_linkml_generator.py`: 47/47 grøne)
- [x] `los_tema.py`/`server.py`-relaterte testar grøne etter del C —
      verifisert end-to-end med eit ekte `list_los_tema`-JSON-RPC-kall,
      returnerer no `navn`-felt korrekt
- [x] `actionlint` køyrt mot alle endra `.github/workflows/*.yml` — berre
      pre-eksisterande `[shellcheck]`-stilråd, ingen `[expression]`-feil
- [x] Sluttverifiseringssøket viser ingen uventa treff — alle attverande
      treff er dei eksplisitt grunngjevne unntaka (sjå "Utført")
- [x] `specs/done/`, `specs/rejected/`, `CHANGELOG.md`-filer, og alle
      fire spec-filnamn-lenkjene urørte

## Relaterte filer

- `specs/done/erstatt-namn-med-navn.md` — fase 1, same mønster/metodikk,
  eksplisitt scope-avgrensing denne specen byggjer vidare på
- `specs/done/namn-navn-konsistens-make-help.md` — tidlegare,
  smalare `make help`-spesifikk retting (alt fullført, uendra)
- `CLAUDE.md` § Skriftspråk — unntakstabellen (`namn`→`navn`) denne
  specen realiserer fullt ut
- `src/mcp-linkml-begrep-utkast/los_tema.py`, `server.py` — del C,
  høgrisiko-tilfellet
- `tests/test_mcp_server.py`, `tests/test_mcp_linkml_generator.py` —
  del B, testfixture-identifikatorar

## Utført

**Metodekorrigering oppdaga undervegs:** kartlegginga i denne specen vart
opphavleg gjort med `grep -rlIE '\bnamn\b'` (ordgrense-avgrensa), same
mønster som fase 1 sin rapport brukte for fil-nivå-lista. Under
utføringa vart det stadfesta at `\bnamn\b` **ikkje** fangar reine
samansetjingar utan bindestrek (`klassenamn`, `slotnamn`, `Kortnamn`
osv.) — `\b` krev eit ord-grense-teikn på begge sider, og "e" i
"klass**e**namn" er eit vanleg ordteikn, ikkje ei grense. Dette vart
oppdaga då `mkdocs/publish.sh` (alt retta) synte å skrive filnamna
`liknande-klassenavn-alle-domene.md` m.fl., medan
`mkdocs/lib/scripts/generate-modellanalyse-md.py` (som IKKJE var i den
opphavlege fil-lista, sidan ingen av «namn»-førekomstane der er
ordgrense-avgrensa) framleis refererte dei gamle filnamna
(`liknande-klassenamn-alle-domene.md`) — ei brotande lenkje som ville
synt seg som 404 i den publiserte portalen. Utføringa vart difor bygd om
til å bruke eit **breiare substring-søk** (`grep -rliE "namn"`, ingen
ordgrense), som er det fase 1 (`erstatt-namn-med-navn.md`) faktisk
brukte i praksis (jf. "Samansette ord skal også rettast konsekvent").
Dette avdekte om lag dobbelt så mange filer som den opphavlege
kartlegginga i denne specen lista.

**Del A (mekanisk prosa-erstatning):** ~55 filer retta
(case-bevarande: `NAMN`→`NAVN`, `Namn`→`Navn`, `namn`→`navn`), på tvers
av `.github/**` (workflows/actions/lychee.toml), `make/*.mk`,
`mkdocs/lib/**`+`mkdocs/publish.sh`, `mkdocs/docs/kom-i-gang/*.md`,
`COMMANDS.md`, `src/assets/scripts/**` (makefile/, scaffolding/,
migreringsscript/, utils/, containers/, templates/docgen/),
`src/mcp-linkml-modell-utkast/*.py`, `src/mcp-linkml-validator/*.py`,
LinkML-skjema-kommentarar i alle 7 `enhetsregisteret-*`/`javazonetalk`-
skjemaa. Inkludert eitt reelt portal-synleg tilfelle:
`src/assets/templates/docgen/class.md.jinja2` sin "Namn"-tabelloverskrift
(brukt i **alle** genererte klasse-sider på tvers av heile portalen) er
no "Navn". `mkdocs/lib/scripts/generate-modellanalyse-md.py` sine tre
cross-domain-relativstiar vart oppdaterte til å matche `publish.sh` sine
nye filnamn (sjå metodekorrigeringa over).

**Del B (testfixture-identifikatorar):** `tests/test_mcp_server.py`
(4 `namn:`-nøklar i innebygde YAML-fixturar, reint interne, ingen
assertions refererer strengen direkte) og
`tests/test_mcp_linkml_generator.py` (`"namn"`-nøkkel + tilhøyrande
assertions retta saman, inkl. testmetodenamnet
`test_slot_namns_kollisjon_...`→`test_slot_navns_kollisjon_...`) retta.
Køyrt via podman (`make mcp-linkml-modell-utkast-test`: 47/47 grøne;
`test_mcp_server.py` via `mcp-linkml-validator`-imaget + pytest: 19/29
grøne — **10 feilar var alt til stades FØR denne endringa**, stadfesta
med `git stash`/re-køyring på uendra kode (feila på ureletarte tema:
manglande `required`-nøkkel i tool-skjema, manglande `title`-metadata i
testfixturen, «fair»-policy-sjekkar som ikkje finn forventa kodar —
ingen av dei namn/navn-relaterte).

**Del C (los_tema.py, godkjent av brukar):** alle 81
`"namn":`→`"navn":`-ordboknøklar i `LOS_TEMA` retta (pluss éin
docstring-førekomst), `src/mcp-linkml-begrep-utkast/server.py` sine 6
prosa-/`description:`-førekomstar retta (ingen kodeendring naudsynt der,
stadfesta at han berre passthrough-serialiserer lista). Verifisert
end-to-end: bygde `mcp-linkml-begrep-utkast`-imaget på nytt, sende eit
ekte `list_los_tema`-JSON-RPC-kall gjennom `podman run`, stadfesta at
svaret no inneheld `"navn"` (ikkje `"namn"`) for kvart LOS-tema-oppslag.

**Ikkje endra (stadfesta, grunngjeve unntak):**

- `CLAUDE.md` linje 135 (unntakstabellen sjølv) og linje 138, `make/01-containers.mk`
  linje 18, `mkdocs/lib/scripts/generate-modellanalyse-md.py` linje 13,
  `mkdocs/docs/kom-i-gang/ny-begrepsmodell.md`/`ny-org.md` — alle
  refererer eksakte filnamn i `specs/done/` (fire ulike spec-filer),
  urørte for å ikkje brekke lenkjer/regelinnhald.
- `src/linkml/begrepskatalog/brreg-begrepskatalog/{data,examples}/*.yaml`,
  `src/linkml/oreg/begrepssamling-foretaksregisteret/begrep/foretaksnavn.yaml`,
  `src/mcp-linkml-begrep-utkast/README.md` — stadfesta legitime
  `_nn`-språkverdiar (nynorsk-termen "føretaksnamn"/"namnet" er korrekt
  i sin `-nn`-kontekst), same vurdering som fase 1.
- `src/linkml/fair/fair-metadata/validation/{1.0.0,1.1.0}/gold.json`,
  `src/linkml/oreg/enhetsregisteret-bvrinn/validation/1.0.0/silver.json`
  — genererte valideringsrapportar med stale "Slotnamn"-meldingstekst
  frå FØR `server.py` sitt meldingstekst-felt vart retta (til "Slotnavn")
  i denne same økta. Ikkje handretta (genererte artefakt, same prinsipp
  som fase 1 sitt punkt G) — vert korrekte automatisk neste gong
  `make mcp-linkml-valider-modell` køyrer for desse skjemaa.
- `src/tmp/*` — ikkje-gitignora, men openbert mellombelse/scratch-filer
  frå ei anna, samstundes køyrande økt (stadfesta via filnamnmønster og
  `git ls-files`) — urørt, jf. instruksen om å ikkje overskrive pågåande
  arbeid frå andre kjelder.

**Verifisering:**

- Full repo-sveip (`grep -rliE "namn" . --exclude-dir=.git
  --exclude-dir=specs --exclude-dir=src/tmp --exclude=CHANGELOG.md`)
  etter alle tre delar: berre dei eksplisitt grunngjevne unntaka over
  attstår.
- `python3 -c "import ast; ast.parse(...)"` på alle endra `.py`-filer:
  ingen syntaksfeil.
- `yaml.safe_load()` på alle endra `.yml`/`.yaml`-filer: ingen parsefeil.
- `actionlint` på alle fire endra `.github/workflows/*.yml`: berre
  pre-eksisterande `[shellcheck]`-stilråd.
- `make lint` på eit utval endra LinkML-skjema (`enhetsregisteret-bvrfriv`,
  `javazonetalk`): "✓ No problems found".
