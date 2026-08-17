# Erstatt "namn" med "navn"

## Bakgrunn

TODO.md hadde eit ope punkt: «erstatte namn med navn». Brukaren stadfesta at dette
gjeld all dokumentasjon, og bad om at LinkML-skjema også vert undersøkt for om
"namn" (nynorsk) har snike seg inn der det skal vere "navn" (bokmål-konvensjonen
for modellering, jf. CLAUDE.md § Skriftspråk).

Eit fullstendig repo-søk viste at "namn" finst i to heilt ulike kategoriar:

1. **Dokumentasjon** (root-`*.md`, `mkdocs/docs/`, `bugs/`, `specs/backlog/`,
   README-filer under `src/`) — nynorsk-domene der brukaren no ønskjer "navn" i
   staden for "namn", inkludert i samansetjingar (`namngjeving` → `navngjeving`,
   `slotnamn` → `slotnavn` osv.). Repoet er alt inkonsekvent her — nokre filer
   brukar "navn" (`mcp-target-navnekonvensjon.md`), andre "namn"
   (`mcp-server-namngjeving.md`).
2. **LinkML-skjema** — bokmål-domene der "namn" er ei reell avviking frå
   konvensjonen. Dette dukkar opp både som **skildringstekst** ("Namn på
   aktøren." → skal vere "Navn på aktøren.") og som **faktiske identifikatorar**:
   globale slot-namn (`namn:` → `navn:`) og lokaldelen i `slot_uri`
   (`ngr:namn` → `ngr:navn`, `ngrp:namn` → `ngrp:navn`). Identifikator-endringar
   er brotande API/URI-endringar, ikkje kosmetikk.

Brukaren har stadfesta følgjande avgrensingar for arbeidet:

- `specs/done/` (og tilsvarande `specs/rejected/`) er arkiv og skal **ikkje** endrast.
- Samansette ord skal også rettast konsekvent (`namngjeving` → `navngjeving` osv.).
- Faktiske slot-namn/`slot_uri` i skjema skal også rettast, ikkje berre skildringstekst.

## Eksplisitt utanfor scope (grunngjeving)

- **`CHANGELOG.md`-filer** — auto-genererte av `release-please` frå historiske
  commit-meldingar. Handrediger vert overskrivne ved neste release og ville
  forfalske historikken. La stå urørt.
- **`specs/done/` og `specs/rejected/`** — arkiv, urørt per konvensjon.
- **Nynorsk-språkverdiar med vilje** — begrepskatalog-data har eksplisitt
  `_nb`/`_nn`-splitting (LangString/definisjonsobjekt). Der ordforma med
  "namn" står i eit `_nn`-felt eller i eit `anbefalt_term`-listeelement som
  representerer den nynorske termen, er det **korrekt** og skal **ikkje**
  endrast:
  - `src/linkml/oreg/begrepssamling-foretaksregisteret/begrep/foretaksnavn.yaml`
  - `src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`
  - `src/linkml/begrepskatalog/brreg-begrepskatalog/examples/brreg-begrepskatalog-eksempel.yaml`
    (linje 76 er nb — alt korrekt "navnet"; linje 80 er nn — korrekt med "namnet")
- **Genererte modellkatalog-datafiler** (`src/linkml/modellkatalog/*/data/*/*.yaml`,
  t.d. `brreg-modellkatalog.yaml`, `kartverket-modellkatalog.yaml`,
  `novari-modellkatalog.yaml`, `skatteetaten-modellkatalog.yaml`) — genererte av
  `make gen-informasjonsmodell-instance` + `make gen-modellkatalog-instance` frå
  kjeldeskjemaa sine eigne `description`-felt. Retting skjer i kjeldeskjemaa;
  desse filene vert oppdaterte ved regenerering, ikkje handretta.
- **Kode og CI** (`*.py`, `*.sh`, `*.jinja2`, `.github/**/*.yml`, `tests/**`) —
  brukaren sitt oppdrag gjaldt dokumentasjon og LinkML-skjema, ikkje
  programidentifikatorar. `src/mcp-linkml-begrep-utkast/los_tema.py` har t.d.
  eit `"namn"`-nøkkelnamn i ein Python-datastruktur (LOS-tema-liste) som ikkje
  vert dekt her — kan takast som eiga oppfølging om ønskt.

## Handlingsliste

### A — Dokumentasjon (nynorsk `*.md`, mekanisk "namn" → "navn", inkl. samansetjingar)

Køyrt som skripta substring-erstatning (case-bevarande: Namn→Navn, NAMN→NAVN,
namn→navn) på heile filer, sidan ingen av desse inneheld nn-språk-unntak:

- Rot: `BUGS.md`, `CLAUDE.md`, `CODEOWNERS.md`, `COMMANDS.md`, `CONTRIBUTING.md`,
  `CONVENTIONS.md`, `GOVERNANCE.md`, `PRINCIPLES.md`, `README.md`, `SCOPE.md`,
  `SECURITY.md`
- `make/README.md`
- Alle `bugs/*.md` som inneheld "namn" (14 filer, inkl. tabellrettinga i
  `bugs/langstring-rdflib-roundtrip.md`, sjå eiga linje under)
- Alle `mkdocs/docs/**/*.md` som inneheld "namn" (13 filer)
- Alle `specs/backlog/*.md` som inneheld "namn", utanom denne fila sjølv (10 filer,
  inkl. `TODO.md` — fjern det fullførte punktet «erstatte namn med navn»)
- `src/linkml/fint/description.md`, `src/linkml/ngr/ngr-person/description.md`
- `src/mcp-linkml-modell-utkast/README.md`, `src/mcp-linkml-validator/policies/README.md`

**Denne fila** (`specs/backlog/erstatt-namn-med-navn.md`) er halden utanfor det
skripta søket sidan ho diskuterer det gamle ordet "namn" som tekst — ho vart
skriven/retta for hand.

### B — `src/mcp-linkml-begrep-utkast/README.md` (handrediger, ikkje skripta)

Inneheld både legitime `_nn`-verdiar (skal stå) og eit par feilmerkte `_nb`-felt
som ved eit uhell inneheld nynorsk tekst. Rett kun:
- Linje 34 (`definisjon_nb` i JSON-eksempelet): nynorsk tekst → bokmål,
  tilsvarande den korrekte nb-teksten i `brreg-begrepskatalog-eksempel.yaml:76`.
- Linje 198 (YAML-eksempel, id `...foretaksnavn-nb`): same retting.
- La linje 33, 185, 201, 219 (nn-verdiar, "føretaksnamn") stå urørte.
- Elles: mekanisk "namn"→"navn" i resten av fila (prosa som "namn og skildring").

### C — Skildringstekst i LinkML-skjema (bokmål-domene, ingen identifikator-endring)

Mekanisk "namn" → "navn" i `description`/kommentarfelt, ingen nøkkel-/URI-endring:

- `src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml` (2 stader)
- `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` (4 stader, inkl. LOS-plassholdaren `<namn>` → `<navn>`)
- `src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml` (1 stad)
- `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml` (1 stad)
- `src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml` (6 stader)
- `src/linkml/fint/fint-arkiv/fint-arkiv-schema.yaml` (14 stader)
- `src/linkml/fint/fint-common/fint-common-schema.yaml` (11 stader)
- `src/linkml/fint/fint-okonomi/fint-okonomi-schema.yaml` (4 stader)
- `src/linkml/fint/fint-personvern/fint-personvern-schema.yaml` (1 stad, kommentar)
- `src/linkml/fint/fint-ressurs/fint-ressurs-schema.yaml` (2 stader)
- `src/linkml/fint/fint-utdanning/fint-utdanning-schema.yaml` (3 stader)
- `src/linkml/ngr/ngr-eiendom/ngr-eiendom-schema.yaml` (2 stader)
- `src/linkml/ngr/ngr-virksomhet/ngr-virksomhet-schema.yaml` (2 stader)
- `src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml` (1 kommentar)
- `src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml` (1 stad)
- `src/linkml/referanse/referansemodell-bronze/referansemodell-bronze-schema.yaml` (1 stad)
- `src/linkml/samt/samt-bu/samt-bu-schema.yaml` (kommentar + 1 skildring)
- `src/mcp-linkml-modell-utkast/profiles/bronze.yaml`, `profiles/silver.yaml` (kommentarar/skildringar)
- `src/mcp-linkml-validator/policies/bronze.yaml`, `gold.yaml`, `felles-begrepskatalog.yaml` (skildringar)

Ingen versjonsheving naudsynt (`docs`-type per `specs/done/conventional-commits-modellversjonering.md`).

### D — Faktiske identifikatorar i skjema (brotande — treng `!`-commit)

1. **`src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml`**
   - Global slot `namn:` → `navn:`, `slot_uri: ngr:namn` → `ngr:navn`, skildring "Namn på..." → "Navn på..."
   - Oppdater `slots:`-referansar i `Adresseomrade` og `GeografiskOmrade` (linje ~264, ~345) frå `- namn` til `- navn`
   - Synk `examples/ngr-adresse-eksempel.yaml`: 5 nøkkelbruk `namn:` → `navn:`

2. **`src/linkml/ngr/ngr-person/ngr-person-schema.yaml`**
   - Slot `navn:` har alt korrekt nøkkelnamn, men `slot_uri: ngrp:namn` → `ngrp:navn` (URI-en heng etter), skildring "Namn på person eller institusjon." → "Navn på..."

3. **`src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`**
   - Global slot `foretrekt_namn:` → `foretrekt_navn:` (slot_uri `skos:prefLabel` uendra), skildring → "Føretrekt navn/term..."
   - Oppdater `slots:`- og `slot_usage:`-referansar i klassen som brukar han (linje ~444, ~453)
   - Synk `examples/cpsv-ap-no-eksempel.yaml`: `foretrekt_namn:` → `foretrekt_navn:`

4. **`src/linkml/referanse/referansemodell-gold/referansemodell-gold-schema.yaml`**
   - Global slot `namn:` (klasse `Aktor`, `slot_uri: foaf:name`) → `navn:`, skildring "Namn på aktøren." → "Navn på aktøren."
   - Oppdater `slots:`- og `slot_usage:`-referansane i `Aktor`-klassen

5. **`src/linkml/referanse/referansemodell-silver/referansemodell-silver-schema.yaml`**
   - Same retting som gold (linje ~220, ~222, ~330-331)
   - Oppdater kommentarane `# silver: aktor_namn → error` og `# Aktør: silver aktor_namn (foaf:name)` til `aktor_navn` (sjå punkt F)

### E — Feilkopla eksempel (ikkje ei "namn"→"navn"-endring, men oppdaga i same gjennomgang)

`src/linkml/ap-no/modelldcat-ap-no/examples/modelldcat-ap-no-eksempel.yaml` linje 177
brukar nøkkelen `namn_aktor:` under `aktorar:`, men det gjeldande skjemaet
(`dcat-ap-no-schema.yaml`, klasse `Aktoer`) definerer slotet `navn_aktoer`
(stadfesta korrekt bruk i `dcat-ap-no-eksempel.yaml:52`). Eksempelet har vorte
liggjande att med eit gamalt/feil feltnamn. Rett til `navn_aktoer:`.

Følgjeretting: `bugs/langstring-rdflib-roundtrip.md` linje 80, tabellrada
`| modelldcat-ap-no | Aktor | namn_aktor |` → `| modelldcat-ap-no | Aktoer | navn_aktoer |`
(inngår i del A sitt filutval, men treng manuell kontroll av heile rada, ikkje
berre ordet "namn").

### F — Validator-regel-ID i `mcp-linkml-validator`

`src/mcp-linkml-validator/policies/silver.yaml` har regel-nøkkelen `aktor_namn:`
(sjekkar at `Aktør`-klassen har `foaf:name`). Berre referert frå denne fila og
kommentarane i `referansemodell-silver-schema.yaml` (punkt D5) — trygt å endre.
Rett nøkkelen til `aktor_navn:` og skildringsteksten "(namn)" → "(navn)".

### G — Avleidde artefakt (avvik frå opphavleg plan)

Forsøkte først `make gen-informasjonsmodell-instance DOMAIN=<domene>` +
`make gen-modellkatalog-instance` slik planlagt. Dette viste seg å dra inn
mykje ekstra, urelatert drift i dei fire modellkatalog-datafilene (endra
URI-skjema frå `brreg.no/...` til `data.norge.no/organizations/.../...`,
fjerna `tema`/`har_kvalitetsmaaling`-felt, endra lisensfelt, endra
`status`-verdiar m.m.) — altså akkumulert avstand mellom generatoren/metadata
og sist committa katalogfiler, heilt urelatert til namn→navn-oppdraget.

**Avvik:** Regenereringa vart forkasta (`git checkout --`), og i staden vart
same mekaniske "namn"→"navn"-erstatning brukt direkte på dei fire filene
(`brreg-modellkatalog.yaml`, `kartverket-modellkatalog.yaml`,
`novari-modellkatalog.yaml`, `skatteetaten-modellkatalog.yaml`), inkludert
URI-stiane som inneheldt det gamle slotnamnet (t.d.
`.../ngr-adresse/Adresseomrade/namn` → `.../navn`). Dette gjev eit surgisk
diff (kun ordbyte) utan å blande inn den urelaterte katalog-drifta.

`make gen-informasjonsmodell-instance` (per-domene-steget før aggregeringa)
skreiv òg over kvart skjema sin `metadata/<skjema>-manifest.yaml` med same
type urelatert drift (kortare skildringar, oppdaterte versjonsnummer/datoar).
Desse vart òg reverterte med `git checkout --` av same grunn. Full
regenerering av manifest og modellkatalogar bør takast som eiga, seinare
oppgåve — ikkje del av dette namn→navn-oppdraget.

### H — Validering

Etter kvar brotande skjema-endring (del D):
```bash
make lint SCHEMA=src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml
make validate-instance SCHEMA=src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml INSTANCE=src/linkml/ngr/ngr-adresse/examples/ngr-adresse-eksempel.yaml
make lint SCHEMA=src/linkml/ngr/ngr-person/ngr-person-schema.yaml
make lint SCHEMA=src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml
make validate-instance SCHEMA=src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml INSTANCE=src/linkml/ap-no/cpsv-ap-no/examples/cpsv-ap-no-eksempel.yaml
make lint SCHEMA=src/linkml/referanse/referansemodell-gold/referansemodell-gold-schema.yaml
make lint SCHEMA=src/linkml/referanse/referansemodell-silver/referansemodell-silver-schema.yaml
make lint SCHEMA=src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml
make validate-instance SCHEMA=src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml INSTANCE=src/linkml/ap-no/modelldcat-ap-no/examples/modelldcat-ap-no-eksempel.yaml
```

## Utført

Alle punkt A–F gjennomførte. 86 filer endra (utanom denne specen):

- **Del A/B** — mekanisk "namn"→"navn" (inkl. samansetjingar) i 53
  dokumentasjonsfiler (rot-`*.md`, `bugs/`, `mkdocs/docs/`, `specs/backlog/`,
  README-filer). `TODO.md` sitt fullførte punkt fjerna.
  `mcp-linkml-begrep-utkast/README.md` handretta: to feilmerkte
  `_nb`-eksempeltekstar retta til bokmål, `_nn`-verdiane ("føretaksnamn")
  ståande urørte.
- **Del C** — mekanisk "namn"→"navn" i skildrings-/kommentarfelt i 22
  skjema-/policy-/profil-YAML-filer (AP-NO, FINT, NGR, oreg, referansemodell,
  mcp-linkml-validator, mcp-linkml-modell-utkast). Ingen identifikator-endring.
- **Del D** — brotande identifikator-rettingar:
  - `ngr-adresse-schema.yaml`: global slot `namn`→`navn`, `slot_uri`
    `ngr:namn`→`ngr:navn`, 2 `slots:`-referansar, synka eksempelfil (5 nøklar)
  - `ngr-person-schema.yaml`: `slot_uri` `ngrp:namn`→`ngrp:navn` (nøkkelen var
    alt `navn`)
  - `cpsv-ap-no-schema.yaml`: global slot `foretrekt_namn`→`foretrekt_navn`,
    synka `slots:`/`slot_usage:` og eksempelfil
  - `referansemodell-gold-schema.yaml` og `referansemodell-silver-schema.yaml`:
    global slot `namn`→`navn` i klassen `Aktor`, kommentarar oppdaterte
  - Alle seks skjema lint-sjekka (`make lint`) — berre pre-eksisterande,
    urelaterte åtvaringar (prefiks-konvensjonar, manglande skildring på
    containerattributtar). `ngr-adresse` sin eksempelfil validert reint mot
    det nye slotnamnet med `make validate-instance`.
- **Del E** — `modelldcat-ap-no-eksempel.yaml` sin forelda `namn_aktor:`-nøkkel
  retta til `navn_aktoer:` (matchar det faktiske slotet i `dcat-ap-no`, klasse
  `Aktoer`). Følgjeretting i `bugs/langstring-rdflib-roundtrip.md` sin tabell
  (klasse- og slotnamn).
- **Del F** — `aktor_namn`→`aktor_navn` i `mcp-linkml-validator/policies/silver.yaml`,
  kommentarane i `referansemodell-silver-schema.yaml` synka.
- **Del G (avvik)** — sjå eiga forklaring i seksjonen ovanfor: regenerering av
  modellkatalog- og manifestfiler vart forkasta pga. urelatert drift; same
  mekaniske erstatning vart i staden brukt direkte på dei fire
  modellkatalog-datafilene som inneheldt "namn".

**Ikkje gjort (utanfor scope, sjå § Eksplisitt utanfor scope):** CHANGELOG.md,
kode/CI (`*.py`, `*.sh`, `.github/**`, `tests/**`), regenerering av
`metadata/*-manifest.yaml`.
