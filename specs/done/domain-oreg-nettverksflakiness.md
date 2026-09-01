# Plan: Fiks `make domain-oreg`-feil (transient DNS/nettverksflakiness)

## Bakgrunn

Brukaren melde at `make domain-oreg` feilar. Køyrt live (2026-09-01,
`timeout 300 make domain-oreg`, full logg i denne økta): **6 av 16
batcha grupper feila** (`merge`, `shacl`, `python`, `rdf`, `docs`,
`plantuml`), medan **10 gjekk OK** (`jsonld-context`, `json-schema`,
`owl`, `proto`, `graphql`, `java`, `convert-instance-rdf`, `xsd`,
`openapi`, `asyncapi`).

Alle feila med **nøyaktig same underliggjande feil**:

```
<urlopen error [Errno -3] Try again>
```

Norsk feiltekst frå `check-import-duplicates`:
```
[ERROR] ::error file=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml::check-import-duplicates kunne ikkje analysere ... — <urlopen error [Errno -3] Try again>
```

`Errno -3` er `EAI_AGAIN` — ein **DNS-oppløysingsfeil** (ikkje "host
finst ikkje", men "prøv igjen seinare"), utløyst av `getaddrinfo()` inne
i podman-containarane når dei prøver å løyse
`raw.githubusercontent.com` for å laste det versjonslåste
`dcat-ap-no-schema`-importet som praktisk talt alle `oreg`-skjema
brukar (jf. `mkdocs/docs/arkitektur/importhierarki.md`).

## Rotårsak-undersøking

**Ikkje ein kodefeil i repoet — transient nettverksflakiness, mest
truleg forsterka av parallellisering.** Grunngjeving:

1. **Same import, ulikt utfall.** `gen-python`/`gen-rdf`/`gen-shacl`/
   `gen-schema-docs`/`gen-plantuml`/`validate` feila, medan
   `gen-jsonschema`/`gen-owl`/`gen-jsonld-context`/`gen-proto`/
   `gen-graphql`/`gen-java` — som løyser **den same** eksterne importen
   for **dei same skjemaa** — gjekk OK i same køyring. Ein deterministisk
   kodefeil ville ramma alle likt; eit sporadisk mønster peikar mot
   transient infrastruktur.
2. **Manuell verifisering rett etter feila køyring:** `curl` mot den
   nøyaktige `raw.githubusercontent.com`-URL-en frå vertsskalet svara
   `HTTP 200` umiddelbart. Ein isolert `podman run alpine getent hosts
   raw.githubusercontent.com` løyste også korrekt (returnerte ei
   IPv6-adresse). Nettverket er altså **stort sett** oppe — feilen er
   sporadisk, ikkje totalt fråvær av tilkopling.
3. **`domain-oreg` sin Fase 1 køyrer svært mange podman-containarar
   samstundes** (sjå COMMANDS.md § "Generering av artefakter" —
   fase-parallellisering, ingen brukarstyrt jobb-tal). Kvar av desse
   containerane løyser **uavhengig** det same eksterne vertsnamnet
   omtrent samstundes — akkurat det mønsteret (mange samstundes
   DNS-oppslag via éin delt resolver) som er kjend for å trigge
   periodevise `EAI_AGAIN`-feil under last.
4. **Miljøfaktor (ikkje noko repoet kan fikse i kode):** vertsmaskina
   sin `/etc/resolv.conf` (WSL2-generert) peikar til
   `nameserver 10.255.255.254` — WSL2 sin interne DNS-proxy, som er
   kjend for å vere ustabil under samstundes last (mange samtidige
   NXDOMAIN/timeout-relaterte GitHub-issue-rapportar om nett dette). Alle
   podman-containarane arvar/rutar truleg DNS gjennom denne same
   flaskehalsen. Dette er **ikkje** noko `Makefile`/Python-skripta i
   repoet kan løyse direkte — det er ein eigenskap ved brukaren sitt
   WSL2-oppsett — men det forklarer **kvifor** akkurat denne typen feil
   dukkar opp akkurat no, og stør konklusjonen om at retry er rett
   mottiltak (transiente feil, ikkje permanente).

**Konklusjon:** Ikkje ein bug å rette i sjølve import-logikken (BUG-15,
`bugs/relativ-import-via-versjonslast-url.md`, er ein *annan*, allereie
retta feil — feil URL-parsing, ikkje nettverksflakiness). Dette er ein
**robustheitsmangel**: repoet sine batch-generatorar gjer i dag **null
forsøk på gjenoppretting** ved ein forbigåande DNS-glipp, sjølv om éin
enkelt gjenkøyring typisk løyser problemet momentant (stadfesta empirisk
tidlegare i denne økta: eit `make lint`-kall som feila med akkurat denne
feilen lukkast umiddelbart ved eit blott gjenforsøk, utan andre endringar).

## Teknisk sporing — éin delt nettverks-flaskehals

Spora heile kallkjeda for **begge** generator-familiane som er ramma:

| Familie | Generatorar | Lastar via |
|---|---|---|
| `SchemaView`-baserte | owlgen, shaclgen, jsonschemagen, docgen, linkmlgen, mcp-linkml-validator | `SchemaView.load_import()` → `load_schema_wrap()` (`linkml_runtime.utils.schemaview`) → `YAMLLoader().load()` |
| `SchemaLoader`-baserte | pythongen, protogen, rdfgen, graphqlgen, plantumlgen, jsonldcontextgen | `linkml.utils.rawloader.load_raw_schema()` → `yaml_loader.load()` |

**Begge familiane konvergerer på nøyaktig same lågnivå-funksjon:**
`yaml_loader.load()` → `linkml_runtime.loaders.loader_root._read_source()`
→ `hbreader.hbread()` → `hbreader.hbopen()` → `urllib.request.urlopen()`.
Stadfesta ved direkte kjeldekode-inspeksjon av den installerte
`linkml`/`linkml_runtime`-versjonen (pinna i
`src/assets/containers/Dockerfile.linkml`/`Dockerfile.mcp-linkml`).

`hbreader.hbopen` er difor **éin einaste, delt flaskehals** for **all**
nettverksavhengig skjemalasting i heile repoet sitt LinkML-verktøysett —
uavhengig av kva generator eller høgnivå-lastar som utløyser han.

## Foreslått fiks

**Legg til eit tredje monkeypatch-steg i
`src/assets/scripts/utils/linkml_relative_import_patch.py`** — same,
allereie etablerte fellesmodul som `.apply()`-kallet i alle 8 relevante
skript (`server.py`, `batch-generate.py`, `batch-linkml-validate.py`,
`batch-convert.py`, `batch-lint.py`, `check-import-duplicates.py`,
`gen-modelldcat-elements.py`, `validate-modelldcat.py`,
`mcp-linkml-modell-utkast/validator.py`) allereie går gjennom for
BUG-15-fiksen. Ein tredje `_apply_retry_patch()`-funksjon der, kalla frå
`apply()`, ville automatisk dekkje **alle** desse køyrevegane i eitt
steg.

Patchen ville **pakke inn `hbreader.hbopen`** med eit gjenforsøksforsøk:

- Fangar `URLError`/`socket.gaierror`/`ConnectionError`/`TimeoutError`
  (transportlagsfeil) — **ikkje** `HTTPError` (som er ein `URLError`-
  subklasse, men representerer eit ekte HTTP-svar, t.d. 404; å prøve
  den på nytt er meiningslaust).
- 2-3 forsøk med kort backoff (t.d. 2 sekund) — nok til å overleve dei
  fleire-sekunds-lange DNS-glippane stadfesta i denne økta, utan å
  gøyme ein reelt fråverande nettverkstilkopling for lenge.
- Skriv éi tydeleg `ÅTVARING`-linje til stderr per gjenforsøk (jf.
  "Ingen stille feil"-prinsippet i CLAUDE.md) — brukaren skal sjå at eit
  gjenforsøk skjedde, ikkje berre at det til slutt lukkast stille.

**Robustheitsfordel samanlikna med dei to eksisterande patchane:** Dei
to eksisterande patchane (`_apply_schemaview_patch`,
`_apply_mergeutils_patch`) kopierer og modifiserer intern
`linkml`/`linkml_runtime`-kjeldekode, og har difor ein eksplisitt
`_EXPECTED_SOURCE_MARKER_*`-sjekk som hoppar over patchinga (med
åtvaring) dersom upstream-koden har endra seg. Retry-patchen derimot
**pakkar berre inn** ein offentleg, stabil funksjon
(`hbreader.hbopen`) utan å kjenne til implementasjonsdetaljar — ho
treng ingen tilsvarande kjeldekode-marker-sjekk, og er dermed robust
mot framtidige `linkml`/`linkml_runtime`-oppgraderingar.

## Steg

1. Legg til `_apply_retry_patch(retries=3, backoff_seconds=2.0)` i
   `linkml_relative_import_patch.py` — pakkar inn `hbreader.hbopen`,
   som skildra over.
2. Kall `_apply_retry_patch()` frå `apply()` (i tillegg til dei to
   eksisterande kalla).
3. Oppdater modulen sin toppkommentar (kort skildring av det nye,
   tredje patch-føremålet — same struktur som dei to eksisterande
   punkta 1/2 i lista der).
4. **Verifiser**:
   - `bash -n`/`python3 -m py_compile` på fila.
   - Simuler ein transient feil (t.d. eit lite testskript som
     monkeypatchar `hbreader.hbopen` til å kaste `URLError` dei to
     fyrste gongene og lukkast tredje gong, stadfest at
     `_apply_retry_patch()` sin innpakking faktisk prøver på nytt og
     til slutt returnerer resultatet).
   - Køyr `make domain-oreg` på nytt (fleire gonger om naudsynt for å
     fange eit nytt tilfelle av den transiente feilen) og stadfest at
     han no anten lukkast heilt, eller i det minste viser synlege
     `ÅTVARING: nettverksfeil ... prøver på nytt`-linjer i staden for å
     feile hardt på fyrste glipp.
   - Køyr `make mcp-linkml-valider-modell-test` og relevante
     `tests/test_make.sh`-kategoriar som rører import-lastinga, for å
     stadfeste ingen regresjon i den normale (ikkje-feilande) stien.
5. **Valfritt, ikkje ein kodeendring:** vurder ei kort notis i
   `CONTRIBUTING.md` eller ein ny fil i `bugs/` om WSL2 sin
   DNS-proxy-flakiness (`10.255.255.254`) som ei **kjend, miljøavhengig**
   årsak til periodevise nettverksfeil under batch-generering på WSL2 —
   reint informativt, med tilvising til denne specen. Ikkje ein
   føresetnad for steg 1-4.

## Handlingsliste

| # | Tiltak | Fil | Type |
|---|---|---|---|
| 1 | `_apply_retry_patch()` — pakk inn `hbreader.hbopen` med gjenforsøk | `src/assets/scripts/utils/linkml_relative_import_patch.py` | Ny funksjonalitet |
| 2 | Kall frå `apply()` | same fil | Ny funksjonalitet |
| 3 | Oppdater toppkommentar | same fil | Dokumentasjon |
| 4 | Verifiser (unit-liknande simulering + reell `make domain-oreg`-gjenkøyring + regresjonstestar) | — | Verifisering |
| 5 (valfri) | Notis om WSL2 DNS-flakiness | `CONTRIBUTING.md` eller ny `bugs/`-fil | Dokumentasjon |

## Utført

Steg 1-4 gjennomførte 2026-09-01 (steg 5, den valfrie WSL2-notisen, er
ikkje gjort — reint informativt tillegg, ikkje ein føresetnad for fiksen):

- **Steg 1-2**: `_apply_retry_patch(retries=3, backoff_seconds=2.0)` lagt
  til i `linkml_relative_import_patch.py`, kalla frå `apply()`. Pakkar
  inn `hbreader.hbopen`; retryar `URLError`/`socket.gaierror`/
  `ConnectionError`/`TimeoutError`, let `HTTPError` passere umiddelbart.
- **Steg 3**: Toppkommentaren oppdatert til å skildre alle tre patchane
  (var to), med grunngjeving for kvifor punkt 3 ikkje treng
  `_EXPECTED_SOURCE_MARKER`-sjekk.
- **Steg 4 — verifisert**:
  - `python3 -m py_compile` OK.
  - Simulert transient feil i eit isolert testmiljø (podman
    `python:3.14-slim` + `hbreader`, sjå testskript i denne økta sin
    scratchpad): fake `hbopen` som feilar med `URLError(gaierror)` dei
    to fyrste kalla og lukkast tredje gong — stadfesta retry skjer,
    korrekt tal kall (3), korrekt total ventetid (>=2× backoff), og at
    `HTTPError` **ikkje** vert retrya (propagerer umiddelbart, éin
    kalltelling).
  - **Reell `make domain-oreg`, to gongar på rad**: begge gav
    `17 OK, 0 feil` (mot `10 OK, 6 feil` før fiksen). Fyrste køyringa
    synte **4 faktiske transiente DNS-glipp** (`ÅTVARING: nettverksfeil
    ... forsøk 1/3 ... Try again`), alle løyste seg sjølv på fyrste
    gjenforsøk — direkte, reell stadfesting av at fiksen løyser akkurat
    det observerte problemet, ikkje berre den simulerte testen. Andre
    køyringa synte 4 nye transiente glipp, same utfall.
  - `make mcp-linkml-valider-modell-test`: 45/45 testar OK — ingen
    regresjon i den normale (ikkje-feilande) stien.
  - `make domain-oreg` sine biverknader (oppdaterte
    `metadata/*-manifest.yaml`-filer for
    `enhetsregisteret-bvrinnfelles`/`register-over-aksjeeiere`, samt
    `javazonetalk` sine genererte artefakt) er venta, normale
    resultat av å faktisk køyre målet — urørt av meg utover det.

Ingen avvik frå planen.

## Kjelder

- Full logg frå den feila `make domain-oreg`-køyringa (2026-09-01,
  6 av 16 grupper feila, alle med `<urlopen error [Errno -3] Try
  again>`) — sjå denne samtaleøkta.
- `hbreader`-kjeldekode (installert versjon i `linkml`/`linkml_runtime`-
  containarbiletet): `hbopen()`/`hbread()` i `hbreader/__init__.py`.
- `linkml_runtime.utils.schemaview.load_schema_wrap()` og
  `linkml.utils.rawloader.load_raw_schema()` — begge sporne til
  `yaml_loader.load()` → `hbread()` → `hbopen()`.
- `bugs/relativ-import-via-versjonslast-url.md` (BUG-15) — den
  **eksisterande**, URL-parsing-relaterte feilen som
  `linkml_relative_import_patch.py` allereie rettar; stadfesta som
  **ikkje** same feil som denne specen adresserer (ulik feilmelding,
  ulik årsak — parsing vs. transient nettverk).
