# Effektiviser køyretida til policy-validering (mcp-linkml-validator)

## Bakgrunn

Brukaren opplever at validering mot policy (`make validate-bronze`,
`make validate-data`, `make mcp-linkml-valider-modell` m.fl.) tek lang tid.
Denne specen er resultatet av ein full gjennomgang av all kode knytt til
`mcp-linkml-validator` — `server.py`, `flatten-and-validate.bash`,
`validate-and-log.py`, `annotate-validate.py`, policy-YAML, alle
`make/40-validation.mk`- og `make/60-mcp.mk`-target, og støtteskripta i
`src/assets/scripts/makefile/` — for å finne konkrete, målbare tiltak.

**Allereie gjort (ikkje duplisert her):**

- `specs/done/parallelliser-domene-validering.md` — parallelliserte
  «Valider alle skjema for domene»-steget i `generate.yml`/`validate.yml`
  (CI-nivå, per-manifest bakgrunnsjobbar).
- `specs/done/timing-valideringskall.md` — la til per-kall-timing i CI-logg.
- `specs/done/videre-containeroptimering-mcp-plantuml-alpine.md` (B2+B4) —
  konsoliderte dei tre `mcp-linkml-*`-imaga til éin Dockerfile med delte lag,
  og migrerte til Alpine-basis (`mcp-linkml-validator` og `linkml-local` er
  no ~216–222 MB, ned frå ~292–352 MB).
- `specs/done/containerisering-python-kall.md` — fjerna alle direkte
  host-Python-kall frå Makefile; all Python køyrer no via `$(PYTHON_RUN)`/
  `$(LINKML_RUN)`/`$(MCP_RUN)`.

Desse tiltaka løyste image-storleik og CI-nivå overlapping, men rørte **ikkje**
sjølve arkitekturen for korleis eit einskild valideringskall er bygd opp.
Denne specen fokuserer på nettopp det — kor tida faktisk går **innanfor**
eitt `flatten-and-validate.bash`-kall, og kvifor det gjentek seg identisk for
kvart skjema.

## Funn — kvantifiserte målingar

Målt lokalt (WSL2/podman, varme image-lag, ingen nettverkspulling) med
`src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml`, eit middels stort skjema:

| Steg | Tid | Kommentar |
|---|---|---|
| `bash flatten-and-validate.bash <schema> bronze` (heile kallet) | **19,8 s** | 2 podman-kontainarar i sekvens |
| — Steg 1: `podman run … gen-linkml --mergeimports` (flat ut) | 8,6 s | `LINKML_IMAGE` |
| — Steg 2: `podman run … mcp-linkml-validator` (valider) | 11,4 s | `MCP_IMAGE` |
| Reint `podman run --rm mcp-linkml-validator python3 -c "print()"` (tom kontainar-oppstart) | 2,6 s | Baseline podman/WSL2-overhead |
| `import linkml_runtime` (inne i kontainaren) | 3,5 s | |
| + `from linkml.validator import validate` | 1,4 s | |
| + `from linkml.linter.linter import Linter` | 0,02 s | Ubetydeleg |

**Kjernefunn: Python-importtida til `linkml`/`linkml_runtime` (~5 s) dominerer
totalt over både podman-oppstart (~2,6 s) og sjølve valideringslogikken
(sub-sekund — `user`/`sys`-tid i alle målingane over er 0,1–0,3 s).** Dette
er ikkje eit spørsmål om image-storleik (Alpine-migreringa i
`videre-containeroptimering`-specen løyste eit anna problem), men om at
`linkml` sitt avhengigheitstre (pydantic, antlr4, sqlalchemy-liknande
maskineri m.fl.) må lastast på nytt for **kvar einaste** kontainar-prosess,
og repoet startar éin ny kontainar-prosess **per skjema**, **to gonger**
(flat ut + valider).

### Verifisert: importtida er nesten heilt amortiserbar

Sende 5 valideringskall (same skjema) som 5 separate JSON-RPC-meldingar til
**éin** `mcp-linkml-validator`-kontainar over stdin (serveren les alt
meldingar i ei løkke frå stdin i `main()` — dette krev ingen kodeendring i
`server.py`):

- 1 kall i éin kontainar: **11,2 s**
- 5 kall i éin kontainar: **14,7 s** — marginalkostnad **~0,9 s per ekstra
  skjema**, mot ~11 s for eit nytt, kaldt kontainarkall.

Det vil seie: importtida til `linkml_runtime`/`linkml.validator` vert betalt
**éin gong per kontainar-prosess**, ikkje éin gong per skjema. Repoet nyttar
i dag arkitekturen «éin kontainar per skjema» i alle løkker
(`validate-bronze`, `validate-data`, `validate-examples` i
`make/40-validation.mk`), og betaler dermed importskatten på nytt for kvart
einaste skjema, heilt unødvendig.

### Verifisert: sjølve utflatingssteget (Steg 1) er unødvendig

`flatten-and-validate.bash` sitt Steg 1 køyrer `gen-linkml --mergeimports`
i ein **eigen** kontainar (`LINKML_IMAGE`) for å slå saman importerte skjema
til éi flat fil, før den flate fila vert sendt til
`mcp-linkml-validator`-kontainaren som rå tekst (`schemaText`).

Testa direkte: `linkml_runtime.utils.schemaview.SchemaView` løyser
imports **transitivt og automatisk** ved konstruksjon, utan noka ekstern
utflating:

```
construct SchemaView (uflata, løyser imports naturleg): 0,13 s
imports deklarert: ['linkml:types']
tree_root til stades: True
all_classes (inkl. importerte): 23
```

0,13 s mot 8,6 s for utflatingssteget via eigen kontainar. `server.py` sin
eigen `validate_schema()`-funksjon konstruerer allereie ein `SchemaView`
(linje 767–770) — utflatinga i Steg 1 er reint dobbeltarbeid som gjer
**akkurat det SchemaView allereie gjer internt**, berre tregare og via ein
ekstra kontainar.

**Utflatinga er dessutan årsak til to dokumenterte, eksisterande
workarounds** som forsvinn heilt om ho fjernast:

1. `flatten-and-validate.bash` Steg 1b (linje 49–69): `gen-linkml
   --mergeimports` strippar `tree_root`-flagget frå containerklassen når det
   dumpar til YAML att — koden må lese det tilbake frå originalskjemaet og
   patche det inn manuelt.
2. `server.py` sin `_check_schema_imports`-handterar (linje 368–381):
   kommentaren seier eksplisitt «Merged schemas lose the imports list — use
   a characteristic class as proxy» — sjekken må gjette seg til om eit
   skjema importerer noko basert på om ein kjenneteikn-klasse finst, sidan
   den flate YAML-fila ikkje lenger har `imports:`-lista.

Begge er symptom på informasjonstap ved å rundtrippe skjemaet gjennom
serialisering-til-YAML-og-attende i staden for å la `SchemaView` løyse
imports naturleg mot filsystemet.

## Tiltak (prioritert etter forventa gevinst / risiko)

### Tiltak 1 — Batch fleire skjema inn i éin MCP-kontainar-prosess

**Forventa gevinst:** størst enkelttiltak. For eit domene med N skjema:
frå ~N × 11 s til ~11 s + (N−1) × 0,9 s for valideringssteget åleine.
For `fint` (7 skjema) svarar det til ~77 s → ~17 s for valideringssteget.

**Steg:**

1. Lag eit nytt orkestreringsskript (t.d.
   `src/assets/scripts/makefile/batch-flatten-and-validate.py`) som for eit
   gjeve domene/liste av skjema:
   - Byggjer éin lang JSON-RPC-meldingsstraum (`initialize` + eitt
     `tools/call` per skjema) og sender ho til **éin**
     `podman run -i --rm … mcp-linkml-validator`-kontainar.
   - Demultipleksar dei N JSON-RPC-svara tilbake til éin-resultat-per-skjema,
     same JSON-form som dagens `flatten-and-validate.bash` produserer, slik
     at `save-validation-log.py`/`emit-github-validation-annotations.py`
     kan gjenbrukast uendra.
2. Oppdater `validate-bronze`, `validate-data`, `validate-examples`
   (`make/40-validation.mk`) til å kalle det nye batch-skriptet i staden for
   å løkke `flatten-and-validate.bash` per skjema.
3. Handter feil per skjema individuelt (eitt skjema sin parse/valideringsfeil
   skal ikkje stoppe resten av batchen) — spegl dagens
   feilhandtering/exit-kode-oppførsel i `validate-bronze`.
4. Test: køyr mot eit domene med mange skjema (`fint` eller `ap-no`) og
   samanlikn resultat-JSON mot noverande sekvensielle køyring for kvart
   skjema (bør vere identisk innhald, berre raskare).

**Risiko:** Låg-til-moderat. Endrar orkestreringslaget, ikkje sjølve
valideringslogikken i `server.py`. Følgjer det etablerte mønsteret frå
`containerisering-python-kall.md` (flytt Makefile-logikk til eigne
Python-script).

### Tiltak 2 — Fjern det separate utflatingssteget (Steg 1)

**Forventa gevinst:** halverer talet på kontainar-oppstartar per skjema,
og fjernar ~8,6 s (kald kontainar) eller det tilsvarande importtillegget
(varm/batch) per skjema. Kombinert med Tiltak 1 køyrer heile
flat-ut-og-valider-flyten i **éin** kontainar-prosess i staden for to.

**Steg:**

1. Endre MCP-verktøyet (`validate_linkml_schema`) til å ta imot skjemaets
   **repo-relative sti** i staden for (eller i tillegg til) `schemaText`,
   og mount heile repoet (ikkje berre `server.py` + `policies/`) inn i
   kontainaren — slik `SchemaView` kan løyse relative imports naturleg mot
   filsystemet, akkurat som i spiketesten over.
2. Fjern Steg 1 (`gen-linkml --mergeimports`) og Steg 1b
   (tree_root-tilbakelesing) frå `flatten-and-validate.bash`.
3. Forenkle `_check_schema_imports` i `server.py` — fjern
   `characteristic_class`-proxy-fallbacket, sidan `schema.imports` no alltid
   er korrekt.
4. Verifiser at instansvalidering (`validate_instance()` → `linkml.validator
   .validate(instance, schema_dict, target_class=...)`) framleis løyser
   imports korrekt når han får eit `schema_dict` som ikkje lenger er
   pre-flata — LinkML sin `validate()`-funksjon aksepterer normalt ein
   skjemasti direkte, som truleg er meir robust enn dagens
   `yaml.safe_load(schema_text)`-omveg. Krev eiga verifisering, sidan dette
   er den delen av koden med høgast risiko for regresjon.
5. Oppdater `reusable-validate.yml` (brukt av **eksterne** repo via
   `workflow_call`) tilsvarande — han kallar same
   `flatten-and-validate.bash`, så endringa slår gjennom automatisk, men
   test eksplisitt at eit kallande repo med berre delvis sparse-checkout
   framleis har dei filene `SchemaView` treng for å løyse sine imports.
6. Kjør `tests/test_mcp_policies.py` og
   `mcp-linkml-valider-modell-smoke`/`-test` og stadfest uendra resultat.

**Risiko:** Moderat — dette er den einaste endringa som rører sjølve
MCP-verktøyets input-kontrakt (`schemaText` → sti-basert) og
instansvalideringsvegen. Følg repoet sitt etablerte mønster for slike
endringar (jf. Alpine-spiken i `videre-containeroptimering-mcp-plantuml-
alpine.md`): gjer eit lite, isolert spike-forsøk først (som er gjort her,
sjå «Funn») og verifiser breitt (fleire skjema, inkl. eitt med fleire
importnivå og eitt med instansdata) før permanent endring.

### Tiltak 3 — Parallelliser Makefile sine eigne validate-target

**Forventa gevinst:** moderat, men svært lav risiko og rask å gjennomføre —
overlappar eksisterande arbeid i staden for å fjerne det, så gevinsten er
mindre enn Tiltak 1/2, men tiltaket er trygt å gjere uavhengig og først.

**Funn:** `specs/done/parallelliser-domene-validering.md` parallelliserte
CI-workflowen (`generate.yml`/`validate.yml`), men **Makefile sine eigne**
`validate-bronze`, `validate-data`, `validate-examples`
(`make/40-validation.mk`) er framleis strengt sekvensielle
`while IFS= read -r schema; do … done`-løkker. Dette er banen ein
utviklar faktisk trigger lokalt via `make validate-bronze DOMAIN=fint`, og
han får ingen nytte av CI-parallelliseringa.

**Steg:**

1. Bruk same mønster som `parallelliser-domene-validering.md` etablerte
   (`&` + `PIDS`-array + `wait`-løkke for feilsamling) i dei tre
   løkkene i `make/40-validation.mk`.
2. Behald `save-validation-log.py`/`emit-github-validation-annotations.py`-
   kalla per skjema uendra (dei er allereie containeriserte via
   `$(PYTHON_RUN)`, jf. `containerisering-python-kall.md`).
3. Vurder om ei `-P<N>`-avgrensing (jf. `validate-capture` sin
   `PARALLEL`-parameter) er naudsynt for å unngå å overbelaste lokal
   podman-maskin ved store domene (t.d. `ap-no` med 10 skjema) — spesielt
   viktig her sidan denne endringa **ikkje** reduserer talet på kontainarar,
   berre overlappar dei (i motsetnad til Tiltak 1/2, som reduserer det
   faktiske arbeidet).

**Risiko:** Låg — same mønster er alt verifisert og i produksjon i
`generate.yml`/`validate.yml`.

**Merk om rekkjefølgje:** Tiltak 3 åleine gjev mindre gevinst enn Tiltak 1,
og kan i verste fall **auke** ressurspresset dersom det vert gjort **utan**
Tiltak 1/2 — fleire samtidige kontainarar som kvar for seg betaler full
importskatt (~11 s), på ein lokal podman-maskin med avgrensa CPU/IO, kan gje
dårlegare totalgjennomstrøyming enn sekvensiell køyring med redusert
per-kontainar-kostnad. `parallelliser-domene-validering.md` flagga
akkurat dette som eit ope spørsmål for CI («opp mot 16 containarar
samstundes … dersom CI-runnerane viser seg overbelasta, bør ei
`xargs -P<N>`-avgrensing vurderast»). **Tilråding: gjer Tiltak 1 (batching)
først** — det gjev størst gevinst med lågast ressursrisiko, og gjer Tiltak 3
mindre naudsynt (ein batch treng ikkje parallellisering, sidan han allereie
unngår per-skjema-kontainarkostnaden).

### Ikkje eit tiltak: image-storleik / Alpine

Presiserer for ordens skuld: ytterlegare containerslanking er **ikkje**
identifisert som eit gjenverande problem her. `videre-containeroptimering-
mcp-plantuml-alpine.md` har alt teke `mcp-linkml-validator`/`linkml-local`
ned til ~216–222 MB på Alpine, og målingane over syner tydeleg at
flaskehalsen er Python sitt eige importoppsett (talet på moduler `linkml`
lastar), ikkje image-laget eller nettverk. Ei ny runde med image-slanking
ville ikkje målbart påverke tala i denne specen.

## Handlingsliste

- [x] Tiltak 1: design og implementer batch-orkestreringsskript for
      MCP-validering (eitt podman-kall, N skjema over stdin)
- [x] Tiltak 1: oppdater `make/40-validation.mk` sine target til å bruke
      batch-skriptet
- [x] Tiltak 1: verifiser identisk resultat-JSON mot dagens sekvensielle
      køyring for eit fleirskjema-domene
- [x] Tiltak 2: spike verifisert (sjå «Funn») — implementer sti-basert
      `validate_linkml_schema`-kontrakt, fjern Steg 1/1b frå
      `flatten-and-validate.bash`
- [x] Tiltak 2: verifiser instansvalideringsvegen (`validate_instance()`)
      framleis løyser imports korrekt utan pre-flating (avdekte og retta ein
      separat bug undervegs, sjå «Utført (Tiltak 2)»)
- [x] Tiltak 2: kjør `tests/test_mcp_policies.py` og
      `mcp-linkml-valider-modell-smoke`/`-test`, stadfest uendra resultat
- [x] Tiltak 2: verifiser `reusable-validate.yml` (ekstern repo-bruk)
      framleis fungerer med sti-basert kontrakt
- [x] Tiltak 3: parallelliser `validate-examples` i `make/40-validation.mk`
      (einaste attverande sekvensielle løkke — brukar ikkje
      `flatten-and-validate.bash`/MCP-validatoren og fell difor utanfor
      Tiltak 1/2 sitt virkefelt, sjå eige punkt under)
- [x] **Nytt, avdekt av Tiltak 2:** regenerer og gjennomgå alle committa
      `validation/*/bronze.json`-loggar for skjema med imports (`ap-no`,
      `fint`, `modellkatalog` m.fl.) — talet på åtvaringar går ned for desse
      (sjå «Utført (Tiltak 2)», bugfix-funnet). Dei committa loggane er
      framleis dei gamle, inflaterte tala til nokon køyrer valideringa på
      nytt.

## Utført (Tiltak 1 — 2026-08-07)

Implementert som planlagt, med éi tilleggsendring utover opphavleg design
(sjå «Nødvendig herding» under).

**Nye/endra filer:**

- `src/mcp-linkml-validator/batch-flatten-and-validate.py` (ny) — batchar
  Steg 2 (MCP-validering) for N skjema inn i éin `podman run`. Steg 1
  (utflating via `gen-linkml --mergeimports`) køyrer framleis éin
  kontainar per skjema — uendra frå før, ventar på Tiltak 2. Støttar to
  kallformer: `--policy <p> schema1 schema2 …` (homogen policy, instans
  auto-oppdaga — brukt av `validate-bronze`) og `--jobs-tsv <fil>`
  (heterogen schema/policy/instans-liste — brukt av `validate-data`).
- `make/40-validation.mk`: `validate-bronze` og `validate-data` bygger no
  éin jobbliste og kallar batch-skriptet éin gong for heile domenet, i
  staden for å løkke `flatten-and-validate.bash` per skjema/datafil.
  Nedstraums logging (`save-validation-log.py`,
  `emit-github-validation-annotations.py`) er uendra — les berre resultatet
  frå batch-outputen i staden for frå eit ferskt `flatten-and-validate.bash`-kall.
- `src/mcp-linkml-validator/server.py`: `main()`-løkka fangar no
  exceptions per JSON-RPC-melding i staden for å la dei ta ned heile
  prosessen. **Nødvendig herding, ikkje valfri polish:** før batching delte
  kvart skjema sin eigen kontainar — éin uventa feil i éitt skjema kunne
  berre ramme det eine skjemaet. Med batching deler N skjema éin
  serverprosess, så utan denne endringa ville éin ubehandla exception i
  skjema K drepe heile batchen og miste resultat for skjema K+1…N.

**Verifisert (målt lokalt, WSL2/podman, varme image-lag):**

| Domene | Skjema | Før (sekvensiell) | Etter (batcha) | Gevinst |
|---|---|---|---|---|
| `oreg` | 2 | 39,7 s | 31,7 s | −20 % |
| `fint` | 6 | 139,5 s | 91,2 s | −35 % |

Gevinsten er mindre enn dei ~10× som vart målt for MCP-steget isolert
(sjå «Funn»), sidan utflatingssteget (framleis éin kontainar per skjema)
utgjer ein stadig større del av totaltida etter kvart som denne
optimeringa fjernar tida MCP-steget brukte. Dette er venta, og er nettopp
grunngjevinga for Tiltak 2 (fjern utflatingssteget) som neste steg — det
vil gje eit mykje større samla gevinst.

Resultatinnhald verifisert byte-for-byte identisk (sortert på
`(code, target)`) mot gamal sekvensiell køyring for `oreg` (begge skjema)
og `fint` (`fint-arkiv`). `validate-data` verifisert mot `modellkatalog`
(6 katalogar) — `valid`/`errorCount`/`warningCount`/`issues` identiske;
den einaste feltdiff-en som dukka opp (`validation_type` →
`validation_policy` i éin loggfil) er ei alt dokumentert, ikkje-relatert
feltnamnavdrift (BUG-12), ikkje ei følgje av denne endringa.

**Testa:**
- `make mcp-linkml-valider-modell-test` (28 testar) — alle grøne etter
  `server.py`-herdinga.
- `make mcp-linkml-valider-modell-smoke` — uendra respons.
- `make validate-bronze DOMAIN=oreg`, `make validate-data
  DOMAIN=modellkatalog` — køyrde til slutt, skreiv korrekte
  valideringsloggar (verifisert innhald, deretter reverterte
  test-genererte artefaktar før commit).

**Funne, ikkje-relatert bug undervegs:** `emit-github-validation-
annotations.py` les skjemastien frå miljøvariabelen `SCHEMA`, men
`$(PYTHON_RUN)` (i `make/01-containers.mk`) forwardar ikkje `-e SCHEMA`
inn i kontainaren — annotasjonane vert difor emitta med tomt `file=`
(`::warning file=::slot:x: …`). Dette er ein feil som fanst identisk før
denne endringa (kallmønsteret `SCHEMA="$$schema" $(PYTHON_RUN) …` er
uendra), berre ikkje verifisert i praksis før no. Påverkar ikkje
`FAILED`-teljinga (som brukar scriptet sin exit-kode, ikkje `file=`-
feltet), så ingen funksjonell konsekvens for denne specen — men bør
dokumenterast i `bugs/` som eiga sak.

**Attverande arbeid:** Tiltak 2 og Tiltak 3 (delvis, sjå over) er ikkje
implementerte i denne runden.

## Utført (Tiltak 2 — 2026-08-07)

Implementert som planlagt: `validate_linkml_schema` tek no imot **anten**
`schemaText` (uendra, for kallarar utan montert repo) **eller** `schemaPath`
(nytt — sti til ei fil som alt finst i kontainaren). `schemaText` er
**ikkje** fjerna eller endra i åtferd — reint additivt, null risiko for
eksisterande kallarar som framleis sender rå tekst (t.d. denne MCP-serveren
brukt direkte som verktøy av eit AI-klientprogram, jf.
`mcp__linkml-validator__validate_linkml_schema` i denne økta).

**Endra filer:**

- `src/mcp-linkml-validator/server.py`: `validate_schema()`/
  `validate_instance()` tek no imot `schema_path`/`schema_obj` som
  alternativ til `schema_text`. TOOL_DEF for `validate_linkml_schema` har
  fått eit nytt `schemaPath`-felt (ikkje lenger `required: [schemaText]` —
  validering av at minst éitt av felta er gjeve skjer no i
  `validate_schema()` sjølv).
- `src/mcp-linkml-validator/flatten-and-validate.bash`: Steg 1
  (`gen-linkml --mergeimports` i eigen kontainar) og Steg 1b
  (tree_root-tilbakelesing) er fjerna heilt. Skriptet monterer no
  `$REPO_ROOT:/repo:ro` og sender `schemaPath` i staden for `schemaText`.
  Namnet er historisk (skriptet flatar ikkje lenger ut noko sjølv) —
  ikkje endra, for å unngå å bryte eksterne referansar (`reusable-
  validate.yml` sitt sparse-checkout listar filnamnet eksplisitt).
- `src/mcp-linkml-validator/batch-flatten-and-validate.py`: fjerna
  `flatten_schema()` og all podman-bruk av `LINKML_IMAGE` heilt —
  batch-skriptet gjer no **berre** eitt podman-kall totalt, uansett kor
  mange skjema som valideres.
- `.github/workflows/reusable-validate.yml`: fjerna pull/tag av
  `ghcr.io/brreg/linkml-local` (ikkje lenger brukt av
  `flatten-and-validate.bash`) og `LINKML_IMAGE`-env frå «Valider
  skjema»-steget. `actionlint` køyrd — ingen `[expression]`-feil.

**Avvik frå opphavleg plan:** `_check_schema_imports` i `server.py` er
**ikkje** forenkla/fjerna `characteristic_class`-fallbacket, i motsetnad til
det opphavlege forslaget. Grunngjeving: fallbacket er framleis reelt nyttig
for `schemaText`-kallarar (som framleis kan sende inn skjema utan fullt
løyste imports), og å fjerne det gjev inga målbar gevinst — det er død kode
berre for `schemaPath`-vegen, der `schema.imports` alt er korrekt. Behalde
uendra som eit trygt fallback.

### Kritisk bug avdekt og retta undervegs: `linkml.validator.validate()` reknar feil sti for relative importar når schema er ein rå sti-streng

Spiken i «Funn» synte at `SchemaView(schema_path)` løyser imports korrekt og
raskt (0,13 s) — men instansvalideringssteget (`validate_instance()`, kalla
frå `validate_schema()` når `instanceText` er gjeven) sender skjemaet vidare
til **linkml sin eigen** `linkml.validator.validate(instance, schema, …)`.
Verifisert empirisk at denne funksjonen, når `schema` er ein rå sti-streng,
reknar ut relative importar **feil** — for
`/repo/src/linkml/modellkatalog/brreg-modellkatalog/brreg-modellkatalog-schema.yaml`
sin import `../../ap-no/modelldcat-ap-no/modelldcat-ap-no-schema` gav han
`[Errno 2] No such file or directory: '/ap-no/modelldcat-ap-no/modelldcat-
ap-no-schema.yaml'` — biblioteket brukar tilsynelatande CWD/eit anna
grunnlag enn skjemafila sin eigen katalog for å løyse relative importar når
det får ein sti-streng, i staden for filas eigen plassering.

**Retting:** send eit alt bygd `SchemaDefinition`-objekt (`sv.schema`, som
`validate_schema()` uansett alt har bygd i Steg 1) til `lm_validate()` i
staden for ein sti-streng. Verifisert direkte at dette gjev korrekt
importoppløysing (0 feil, mot feilen over med sti-streng). `validate_
instance()` sin signatur er endra frå `schema_path: str | None` til
`schema_obj: SchemaDefinition | None` som følgje av dette — reint internt,
ingen kontraktendring for MCP-verktøya utetter.

### Uventa, men korrekt sideeffekt: fjerning av utflating fiksar ein reell falsk-positiv-bug i policy-sjekkane

Samanlikna resultat for `brreg-modellkatalog-schema.yaml` (importerer
`modelldcat-ap-no`, som igjen importerer `dcat-ap-no`) med
`felles-datakatalog`-policy, før og etter Tiltak 2:

| | Errors | Warnings |
|---|---|---|
| Før (utflata schemaText) | 0 | 67 |
| Etter (schemaPath, native imports) | 0 | 6 |

61 av dei 61 forskjellige åtvaringane var kodane `all_classes_have_
concept_ref` m.fl. retta mot klasser som **ikkje er definerte i
`brreg-modellkatalog-schema.yaml`** i det heile — dei er importerte frå
`modelldcat-ap-no`/`dcat-ap-no` (`Datasett`, `Distribusjon`, `Katalog`,
`Aktoer` m.fl.). **Dette er stikk i strid med CLAUDE.md sin eigen
dokumenterte regel:** «AP-NO-profil-skjema skal ikkje ha
`begrepsidentifikator` på klassane sine … Klassane der (t.d. `Datasett`,
`Katalog`, `Distribusjon`) er definerte av W3C/EU-standardar … ikkje av
norske omgrep i Felles begrepskatalog.»

**Rotårsak:** `gen-linkml --mergeimports` slår saman alle importerte
klasser inn i `classes:`-blokka til det utflata skjemaet, slik at dei ser
ut som lokalt definerte klasser. Policy-sjekkane i `server.py` itererer
medvite over `schema.classes` (ikkje `sv.all_classes()`) nettopp for å
avgrense seg til lokalt definerte element — men denne avgrensinga vart
verdilaus når «lokalt» og «importert» vart identiske etter utflating.
Native `SchemaView`-oppløysing (utan utflating) held skiljet korrekt: kun
genuint lokale klasser/slots hamnar i `schema.classes`/`schema.slots`.

**Verifisert breiare** (ikkje berre spesialtilfellet over) — same mønster
stadfesta for fleire skjema med imports via `make validate-bronze`:

| Skjema | Åtvaringar før | Åtvaringar etter |
|---|---|---|
| `ap-no/dcat-ap-no` | 35 | 22 |
| `fint/fint-administrasjon` | 63 | 34 |

Alle testa skjema heldt `errorCount: 0`/`valid: true` uendra — berre
talet på (reelt feilaktige) åtvaringar gjekk ned. Dette er **ikkje** ein
regresjon frå Tiltak 2, men ein bugfix som var ein direkte konsekvens av å
fjerne utflatinga. **Konsekvens:** alle committa
`src/linkml/*/*/validation/*/bronze.json` (og tilsvarande `silver`/`gold`/
`felles-*`-loggar) for skjema med imports viser no inflaterte,
historisk feilaktige åtvaringstal inntil dei vert regenererte (sjå
handlingslista).

**Verifisert (målt lokalt, WSL2/podman, varme image-lag) — totalgevinst
Tiltak 1 + Tiltak 2 kombinert:**

| Domene | Skjema | Original baseline | Tiltak 1 åleine | Tiltak 1+2 |
|---|---|---|---|---|
| `oreg` | 2 | 39,7 s | 31,7 s | — (ikkje re-målt separat) |
| `fint` | 6 | 139,5 s | 91,2 s | **63,3 s** (−55 % frå baseline) |
| `ap-no` | 10 | — (ikkje målt før) | — | 81,4 s |

**Testa:**
- `make mcp-linkml-valider-modell-test` (28 testar) — grøne, inkludert
  etter `validate_instance()`-signaturendringa.
- `make mcp-linkml-valider-modell-smoke` — uendra respons.
- `make validate-bronze DOMAIN={oreg,fint,ap-no}` — alle fullførte med
  exit-kode 0, ingen krasj, korrekte valideringsloggar (verifiserte,
  deretter reverterte testgenererte artefaktar før commit).
- Direkte samanlikning `flatten-and-validate.bash` før/etter (via
  `git stash`) for `ngr-adresse` (enkel importstruktur, kun `linkml:
  types`) og `brreg-modellkatalog` (fleirnivå relativ import via
  `modelldcat-ap-no` → `dcat-ap-no`).
- `actionlint` mot `reusable-validate.yml`.

**Ikkje testa/gjenstår:** faktisk køyring av `reusable-validate.yml` frå eit
ekte eksternt repo (krev eit reelt `workflow_call`-oppsett, ikkje testbart
lokalt) — logikken er verifisert å vere korrekt (same `REPO_ROOT`-mekanisme
som før, berre eitt mindre podman-kall), men ikkje stadfesta i praksis i CI.

## Utført (Tiltak 3 + loggregenerering — 2026-08-07)

### Tiltak 3 — parallelliser `validate-examples`

`validate-examples` (`make/40-validation.mk`) var den einaste attverande
strengt sekvensielle løkka — han brukar `linkml validate` direkte, ikkje
`flatten-and-validate.bash`/batch-skriptet, og fall difor utanfor Tiltak
1/2 sitt verkefelt. Parallellisert med same mønster som `mkdocs/publish.sh`
og `specs/done/parallelliser-domene-validering.md` alt etablerte:
kvart skjema sin valideringskropp er pakka inn i ein `( … ) &`-subshell
(eigen variabel-scope per parallell jobb — unngår race conditions på
`result`/`has_error`/`exit_code`), PID-ar og skjemanamn sporast i
`PIDS`/`KEYS`-array, og ei etterfølgande `wait`-løkke tel opp `FAILED`
basert på kvar subshell sin exit-kode. `SHELL := /bin/bash` er alt sett i
`Makefile` (linje 8), så bash-array-syntaksen fungerer utan endring.

**Verifisert:**
- Isolert test av sjølve PIDS/KEYS/wait-mekanikken (4 simulerte jobbar, 2
  suksess + 2 feil) — stadfesta at `FAILED`-teljinga og exit-koden er
  korrekte under parallell køyring.
- `make validate-examples DOMAIN=ngr` (4 skjema): fullførte med exit-kode
  0, alle fire valideringsloggane skrivne korrekt. Kvart skjema sitt
  einskildkall tok ~10,7 s, men **total veggklokketid var 17,1 s** (mot
  ~42,8 s sekvensielt — dei fire containerane køyrde overlappande).
- Testartefaktar reverterte før commit.

### Loggregenerering — fiks stale valideringsloggar frå Tiltak 2-bugfixen

Køyrde `make validate-bronze DOMAIN=<domene>` for alle 9 domene (`ap-no`,
`begrepskatalog`, `fair`, `fint`, `modellkatalog`, `ngr`, `oreg`,
`referanse`, `samt`) for å oppdatere dei committa `bronze.json`-loggane med
korrekt (ikkje-inflatert) åtvaringstal etter bugfixen i Tiltak 2.

**Resultat:** 21 eksisterande `bronze.json`-filer oppdaterte (pluss 2 nye
for `oreg`, som ikkje hadde committa bronze-loggar frå før). Verifisert
programmatisk (samanlikna kvar fil mot `git show HEAD:<sti>`) at **alle**
endringane er reine reduksjonar i `warningCount` — `valid` og `errorCount`
er identiske før/etter for kvar einaste fil, ingen skjema gjekk frå gyldig
til ugyldig eller omvendt. Størst utslag: `modelldcat-ap-no` (66→8 og
66→5 åtvaringar for to versjonar), `dqv-ap-no 1.15.0` (35→5),
`digdir-/kartverket-/ksdigital-/novari-/skatteetaten-modellkatalog`
(68→7 kvar).

Silver/gold/`felles-*`-loggar (skrivne via `log-mcp-validate`/
`run-validation.sh`, ikkje `validate-bronze`) er **ikkje** regenererte i
denne runden — dei brukar den same, no fiksa `flatten-and-validate.bash`,
og vil difor sjølvrette seg ved neste ordinære `generate.yml`/
`validate.yml`-køyring i CI. Ikkje prioritert her for å avgrense omfanget
av denne enkeltendringa.

**Alle tiltak i denne specen er no gjennomførte** (Tiltak 1, 2, 3 og
loggregenereringa). Specen er klar til å flyttast til `specs/done/`.

## Tillegg: estimert minnegevinst og evaluering av byggetidstiltak (2026-08-07)

Oppfølgingsspørsmål frå brukar: (1) kvantifiser estimert spart minnebruk frå
tiltaka over, (2) vurder om noko kan gjerast ved **bygging** av
`linkml`/`linkml_runtime`-kontaineren for å redusere oppstart-/importtid
ytterlegare, utover det Tiltak 1/2 alt oppnår.

### 1) Estimert spart minnebruk

Målt direkte (`resource.getrusage().ru_maxrss` inne i kontaineren):

| Prosess | Peak RSS |
|---|---|
| Bar Python-tolk, ingen import | 9,4 MB |
| Etter `import linkml_runtime` + `linkml.validator` + `linkml.linter` | 89–110 MB |
| `gen-linkml` sitt eige importkjede (`linkml.generators.linkmlgen`) | 86,3 MB |

Minneveksten **innanfor** éin batcha prosess er svak — importkostnaden
dominerer, ikkje talet på valideringar i same prosess:

| Skjema validerte i same prosess (batch) | Peak RSS |
|---|---|
| 1 | 107,6 MB |
| 10 | 124,4 MB (+1,9 MB/skjema) |
| 36 | 172,5 MB (+1,9 MB/skjema) |

**Kvar minnegevinsten faktisk gjeld — og kvar han ikkje gjer:**

- **`make validate-bronze`/`validate-data` (Tiltak 1):** den gamle
  arkitekturen var *sekvensiell* — peak-minne var alltid ~110 MB på eitt
  tidspunkt, uansett kor mange skjema (containerar køyrde etter kvarandre,
  ikkje samstundes). Tiltak 1 endrar difor **ikkje** peak-minnebruk her i
  praksis — gevinsten var tid (importskatten betalt éin gong, ikkje N
  gonger), ikkje minne. Verdt å presisere sidan det er lett å anta
  «færre containerar = mindre minne generelt», noko som berre stemmer for
  *samtidige* scenario.
- **Tiltak 2 (fjerna utflatingssteget) i CI sin parallelle domenevalidering**
  (`generate.yml`/`validate.yml`, alt parallellisert i ein tidlegare spec —
  N skjema validerte **samstundes** i bakgrunnen): før Tiltak 2 brukte
  kvart samtidig skjema to sekvensielle containerar (flatten ~86 MB +
  valider ~110 MB). Estimert aggregert peak-minne for eit domene med N
  samtidige skjema: **frå ~N × 196 MB til ~N × 110 MB, ei odel omtrent
  44 % reduksjon** i denne konkrete, samtidige køyringsbanen. (Estimat basert
  på målte einskild-prosess-tal — ikkje stadfesta med faktisk
  `podman stats`-måling under ein reell parallell CI-køyring.)
- **Tiltak 3 (parallellisert `validate-examples`) går motsett veg,
  medvite:** N containerar køyrer no samstundes i staden for sekvensielt —
  byter **meir** aggregert minnebruk mot **mindre** veggklokketid. For eit
  domene med N skjema er estimert samtidig peak no i storleiksorden N ×
  (minnebruk for éin `linkml validate`-container), mot éin einskild
  container om gongen før. Nemnt eksplisitt her sidan spørsmålet gjeld
  minne spesifikt — dette er ein avveging, ikkje ei eintydig forbetring på
  minnesida.

### 2) Evaluering: byggetidstiltak for å redusere importtid

Testa empirisk mot `src/assets/containers/Dockerfile.mcp-linkml`:

**a) Precompilert bytekode.** Biletet set i dag `PYTHONDONTWRITEBYTECODE=1`
i `base-runtime`-steget, som hindrar **all** `.pyc`-cache (stadfesta: nesten
ingen `__pycache__`-katalogar finst i det committa biletet). Bygde eit
spike-bilete med `RUN python3 -m compileall -q -j 0 /install` lagt til i
`base-builder`-steget (stadfesta at `.pyc`-filer faktisk vart skrivne og
kopierte over til sluttbiletet). Målt importtid (3 køyringar kvar):
produksjonsbilete 3,9–5,0 s, spike-bilete 4,2–5,4 s — **ingen måleleg
forbetring**, innanfor normal støy.

**b) `PYTHONOPTIMIZE=1`.** Testa som ei rimeleg gissing (strip
docstrings/assert). Resultat: **gjorde det verre** — importtid dobla seg
til ~10,2–10,6 s. Sannsynleg årsak: ein separat, ukacha bytekode-variant
(`.opt-1.pyc`) tvingar full rekompilering uavhengig av om
`PYTHONDONTWRITEBYTECODE` er sett. **Ikkje å tilrå.**

**c) `-X importtime`-profilering** (`python3 -X importtime -c "import
linkml_runtime; from linkml.validator import validate; from
linkml.linter.linter import Linter"`): kostnaden fordeler seg over **~984
moduler**, ingen enkelt modul dominerer (største enkeltmodul etter eigen
tid: `linkml_runtime.linkml_model.meta` på 160 ms, deretter `typing`
124 ms, `ShExJSG.ShExJ` 116 ms, `argparse` 91 ms, `tarfile` 88 ms — ei lang
hale av moderate kostnader, ikkje éin flaskehals). Summen av eigen-tid
(~5,1 s) matchar observert veggklokketid tett, som stadfestar at kostnaden
er reell **CPU-utføringstid ved modulinitialisering** (bygging av
pydantic-liknande modellar, klassehierarki, registreringar i
`linkml_runtime.linkml_model`, `rdflib`, `linkml.generators` m.fl.) — ikkje
disk-I/O og ikkje parse-/kompileringstid (jf. punkt a).

**Konklusjon:** ingen testa byggetidstiltak reduserer sjølve importkostnaden
meiningsfullt. Kostnaden er **strukturell** — bredda av `linkml` sitt
avhengigheitstre (~984 moduler for ein minimal valideringsbruk) — ikkje
konsentrert i éin komponent som kan fjernast eller bytast ut utan å endre
`linkml`/`linkml_runtime` sjølve (utanfor dette repoet sin kontroll, og eit
langt større og meir risikofylt inngrep enn nokon av tiltaka i denne
specen). Den tidlegare Alpine-migreringa
(`videre-containeroptimering-mcp-plantuml-alpine.md`) endrar heller ikkje
dette biletet — importkostnaden er CPU-bunden Python-utføring, ikkje noko
musl/glibc-skilnaden mellom Alpine og Debian/slim påverkar.

**Praktisk følgje:** batching (Tiltak 1) er difor ikkje berre den beste,
men i praksis den **einaste** tilgjengelege avbøtinga innanfor dette repoet
sin kontroll — han reduserer *kor ofte* kostnaden vert betalt, ikkje sjølve
kostnaden. Er endå meir aggressiv batching (t.d. éin langlevd
validator-prosess/daemon på tvers av heile `make`-økta, i staden for éin
kontainar per `validate-bronze DOMAIN=...`-kall) ønskt, er det den einaste
attverande retninga med reelt potensial — men det er eit større
arkitektonisk steg (krev eit persistent daemon-oppsett, gjev mest nytte
lokalt i utviklingsløkker, lite for CI der kvar jobb uansett startar i eit
reint miljø) og er **ikkje** vurdert eller implementert her.
