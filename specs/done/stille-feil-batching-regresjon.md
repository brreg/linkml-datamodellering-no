# Stille feil-regresjon i batching-arbeidet (validate-bronze/validate-data)

## Bakgrunn

`specs/done/ingen-stille-feil.md` (lukka 2026-08-04) gjennomgjekk og fiksa
stille-feil-mønster i make-laget, Python-scripta og CI-workflows. Etter at den
spec-en vart lukka, vart valideringsmåla i `make/40-validation.mk` skrivne om
til å bruke batch-flatning (`batch-flatten-and-validate.py`) i staden for
per-skjema-kall (arbeid utført 2026-07-31 til 2026-08-07, jf.
`specs/backlog/evaluer-batching-resterande-kommandoar.md`). Omskrivinga
introduserte fleire nye `2>/dev/null`/`|| true`-mønster som ikkje er audita
mot «ingen stille feil»-regelen, og eitt reelt korrektheitsbrot: `make
validate-data` kan ikkje lenger feile, uansett valideringsresultat.

Denne spec-en dokumenterer funna frå ein full re-gjennomgang av repoet
(2026-08-09) etter CLAUDE.md sin regel om at ingen kommando, funksjon eller
script skal kunne feile utan synleg logging ved `LOGLVL=ERROR` (default-nivå).
Python-scripta under `src/assets/scripts/` og `mkdocs/lib/scripts/` som vart
fiksa i den opphavlege spec-en er stadfesta framleis korrekte — ingen nye funn
der. Alle nye funn er i `make/40-validation.mk`, med nokre tilleggsfunn i
`mkdocs/lib/`-bash-skript og to MCP-servarar utanfor det opphavlege
filfokuset.

## Funn

### 1. Korrektheitsbrot: `validate-data` kan aldri feile (høgast prioritet)

`make/40-validation.mk:78-121` (recipe for `validate-data`) manglar heilt den
`FAILED`-sporinga og `exit $$FAILED` som søskena `validate-bronze` (linje 72)
og `validate-examples` (linje 192) har. Løkka (linje 114-121) skriv
valideringsresultat til logg via `save-validation-log.py`, men sjekkar aldri
om resultatet faktisk var `"valid":false`, og recipe-en avsluttar difor alltid
med exit 0.

**Konsekvens:** `.github/workflows/validate.yml:258` køyrer
`make validate-data DOMAIN=${{ matrix.domain }}` som eige CI-steg. Sidan målet
alltid returnerer 0, kan ein PR med faktisk ugyldige datafiler aldri raudt-
merkjast av dette steget — i strid med COMMANDS.md sin dokumenterte kontrakt
("pass/fail per datafil").

I tillegg manglar `validate-data` det tilsvarande kallet til
`emit-github-validation-annotations.py` som `validate-bronze` har (linje 67),
så sjølv om `FAILED`-sporing vert lagt til, må annotasjons-steget leggjast til
parallelt for at feil skal verte synlege som GitHub Actions-annotasjonar
(ikkje berre exit code).

### 2. Stderr frå batch-valideringsscriptet vert kasta bort

`make/40-validation.mk:57` og `:109` (`validate-bronze` og `validate-data`)
kallar `batch-flatten-and-validate.py` med `2>/dev/null`, utan `run_logged`.
Dersom scriptet krasjar heilt (t.d. import-feil, korrupt input) i staden for
å produsere eit gyldig per-skjema JSON-resultat, forsvinn den faktiske
feilteksten sporlaust. Einaste spor vert den generiske
`"message":"Batch-resultat manglar"`-fallbacken (linje 63/116), som i
`validate-data` sitt tilfelle (jf. funn 1) ikkje eingong vert overvaka.

### 3. `save-validation-log.py`-kall undertrykkjer feil ubetinga

Tre stader kallar `save-validation-log.py` med `2>/dev/null || true` (eller
`< /dev/null 2>/dev/null || true`), utan `run_logged`:

- `make/40-validation.mk:66` (`validate-bronze`)
- `make/40-validation.mk:119` (`validate-data`)
- `make/40-validation.mk:178` (`validate-examples`)

Feil i loggeskrivinga sjølv (t.d. disk full, sti-problem) er ikkje ein
forventa/uskuldig feilkjelde slik unntaket for `podman image exists`-mønsteret
er — dette bør bruke `run_logged` eller minst behalde stderr synleg ved feil.

### 4. `detect-validation-policy.py`-kallet kastar vekk scriptet si eiga åtvaring

`make/40-validation.mk:204`:

```make
@DETECTED_POLICY=$$($(PYTHON_RUN) python3 /work/.../detect-validation-policy.py "$(SCHEMA)" 2>/dev/null || echo "bronze"); \
```

`detect-validation-policy.py` vart fiksa i `ingen-stille-feil.md` (steg 5-6)
til å skrive ei eksplisitt `ÅTVARING`-linje til stderr før fallback til
bronze. Make-wrapperen her kastar likevel vekk heile stderr med
`2>/dev/null`, så åtvaringa når aldri brukaren — fiksen frå den opphavlege
spec-en er reelt sett nullstilt på make-nivå.

### 5. Same mønster i `mkdocs/lib/`-bash-skript (utanfor opphavleg filfokus)

Desse følgjer identisk "python -c ... 2>/dev/null || echo default"-mønster
utan synleg åtvaring, og vart ikkje dekt av `ingen-stille-feil.md` sitt
avgrensa filfokus (`src/assets/scripts/` og `mkdocs/lib/scripts/` — ikkje
`mkdocs/lib/sections/` eller `mkdocs/lib/utils/`):

- **`mkdocs/lib/sections/badges.sh:57`** — høgast alvorsgrad av desse: viss
  `validation_json` er korrupt/uleseleg, fell scriptet stille tilbake på
  `errors="0"`, som fører til at badgen viser **"✓ godkjent"** for eit skjema
  der valideringsresultatet faktisk ikkje kunne lesast. Dette er ein reell
  korrektheitsfeil i publisert dokumentasjon (feilaktig positiv badge), ikkje
  berre manglande logging.
- **`mkdocs/lib/utils/metadata_parsers.sh:54`** — same "bruk default"-mønster
  som `detect-validation-policy.py` hadde før fiksen, men bash-ekvivalenten
  fekk aldri tilsvarande ÅTVARING-linje.
- **`mkdocs/publish.sh:254`** — stille fallback til tom delmodell-liste ved
  korrupt `build.yaml`, kan skjule manglande delmodell-relasjonar i publisert
  dokumentasjon utan spor.
- **`mkdocs/lib/sections/delmodellar.sh:36,67,68`** — same mønster for
  tittel/skildring-felt, lågare alvorsgrad (kosmetisk docs-innhald).

Reine oppryddings-/kopieringsoperasjonar (`mkdocs/publish.sh:214-215`,
`mkdocs/lib/copy_artifacts.sh:40`) er vurderte som **OK-benigne** — tomt
kjeldemateriale er forventa og ufarleg der, analogt med `rm -rf`-idiomet.

### 6. To MCP-servarar med stille `except Exception` (utanfor opphavleg filfokus)

`src/mcp-linkml-validator/` vart eksplisitt halde utanfor filfokuset i
`ingen-stille-feil.md`. To andre MCP-servarar har tilsvarande stille mønster,
lågare prioritet sidan dei ikkje er CI-kritiske:

- **`src/mcp-linkml-modell-utkast/server.py:25`** og
  **`src/mcp-linkml-begrep-utkast/server.py:26`** (`_list_profiles()`) —
  `except Exception: profiles.append({"name": path.stem, "description": ""})`.
  Ei korrupt profil-YAML gjev berre ei tom skildring i lista, ingen
  indikasjon på at parsing feila.
- **`src/mcp-linkml-modell-utkast/validator.py:48`** — `except Exception: pass`
  i dummy-instans-bygging for roundtrip-test. Lågast prioritet av desse to,
  sidan det er eit test-/valideringshjelpemiddel, ikkje ein produksjonssti.

### Vurdert og stadfesta OK (ingen endring naudsynt)

- `make/40-validation.mk:81` (`find ... -path '*/data/*' 2>/dev/null`) —
  tom-treff er alt handtert eksplisitt (`log_info "Ingen datafiler funne..."`).
  Grensetilfelle: ein reell `find`-feil på ein delkatalog (t.d. permission
  denied) ville framleis vore stille, men dette vert ikkje prioritert i denne
  runden.
- `make/40-validation.mk:155` (`podman run ... linkml validate ... 2>&1`) —
  fangar output i variabel og parsar/loggar `[ERROR]`-linjer eksplisitt,
  funksjonelt tilsvarande `run_logged`.
- `make/40-validation.mk:210,226`, `make/60-mcp.mk:110`,
  `make/70-scaffolding.mk:21` (`podman image exists ... 2>/dev/null || make
  build-...`) — eksplisitt uttrykt unntak i CLAUDE.md-regelen: forventa,
  uskuldig eksistenssjekk.
- Alle `except`-blokker i `src/assets/scripts/` og `mkdocs/lib/scripts/` frå
  det opphavlege grep-søket (inkl. `new-modell.sh:66`, som er filnamnet
  `ingen-stille-feil.md` refererer til med skrivefeilen `new-model.sh`) —
  stadfesta framleis korrekt logga, jf. `ingen-stille-feil.md` § Utført.
- `src/assets/scripts/makefile/run-validation.sh:67,108` — feilar høgt med
  eksplisitt stderr-melding + `exit 1` uansett årsak, ikkje ei stille
  svelging. Merknad: `2>/dev/null` her kastar likevel vekk Python sin faktiske
  traceback, så feilmeldinga kan vere unøyaktig (seier "manglar felt" sjølv
  om årsaka er korrupt YAML) — ikkje eit brot etter regelens ordlyd, men verdt
  å forbetre presisjonen ved anledning.
- `.github/workflows/*.yml` — dei to stadene identifiserte i
  `ingen-stille-feil.md` er stadfesta framleis fiksa, ingen nye funn.

## Målbilete

- `make validate-data` feilar (non-zero exit) og produserer GitHub Actions-
  annotasjonar når ei datafil faktisk feilar valideringa, symmetrisk med
  `validate-bronze` og `validate-examples`.
- Alle `2>/dev/null`/`|| true`-kall til `batch-flatten-and-validate.py` og
  `save-validation-log.py` i `make/40-validation.mk` bruker `run_logged` (eller
  tilsvarande synleg feilhandtering) i staden for ubetinga stderr-discard.
- `detect-validation-policy.py` si ÅTVARING-linje når faktisk brukaren, ikkje
  berre stdout-verdien.
- `badges.sh` viser ikkje "✓ godkjent" for eit skjema der valideringsresultatet
  faktisk ikkje kunne lesast.

## Steg

1. **Fiks `validate-data`-korrektheitsbrotet** (`make/40-validation.mk:78-121`):
   legg til `FAILED`-sporing (etter mønster frå `validate-bronze`) og
   `exit $$FAILED`. Vurder om `emit-github-validation-annotations.py` skal
   kallast per datafil (som i `validate-bronze`) for synlege PR-annotasjonar,
   eller om ei enklare `log_error`-melding er tilstrekkeleg for dette målet —
   avklar med brukar kva som er ønskt granularitet før implementering.
2. **Erstatt `2>/dev/null` med `run_logged`** for dei to
   `batch-flatten-and-validate.py`-kalla (linje 57, 109).
3. **Erstatt `2>/dev/null || true` med `run_logged`** (eller ekvivalent synleg
   feilhandtering) for dei tre `save-validation-log.py`-kalla (linje 66, 119,
   178). Merk: desse kalla har bevisst soft-fail-semantikk (ei loggeskrive-
   feil skal ikkje stoppe heile valideringsmålet) — behald non-fatal åtferd,
   berre gjer feilen synleg, jf. mønsteret frå `run_gen_informasjonsmodell_instance`
   i `ingen-stille-feil.md` steg 3.
4. **Fjern `2>/dev/null` frå `detect-validation-policy.py`-kallet** (linje 204)
   slik at scriptet si eiga ÅTVARING-linje når brukaren.
5. **Fiks `badges.sh:57`** slik at eit uleseleg/korrupt `validation_json` ikkje
   fell tilbake på `errors="0"` (som gjev feilaktig "✓ godkjent") — bruk ein
   eigen statusverdi (t.d. "ukjent"/"⚠") og skriv ei åtvaring til stderr.
6. **Vurder (lågare prioritet) om steg 5-6 sitt scope frå
   `ingen-stille-feil.md` skal utvidast** til `mkdocs/lib/utils/metadata_parsers.sh`
   og `mkdocs/publish.sh:254` (delmodell-fallback) — avklar med brukar om desse
   skal fiksast no eller dokumenterast som kjend, lågrisiko avvik.
7. **Vurder (lågaste prioritet) dei to MCP-servarane** (`server.py` i
   `mcp-linkml-modell-utkast`/`mcp-linkml-begrep-utkast`, og
   `mcp-linkml-modell-utkast/validator.py:48`) — avklar med brukar om desse er
   i scope, sidan `src/mcp-linkml-validator/` eksplisitt vart halde utanfor i
   den opphavlege spec-en.
8. **Test lokalt:**
   - Induser ei ugyldig datafil kunstig og køyr `make validate-data
     DOMAIN=<domain>`, verifiser non-zero exit og synleg feilmelding.
   - Induser eit korrupt/manglande `validation_json` og verifiser at
     `badges.sh` ikkje lenger viser "✓ godkjent".
   - Verifiser at normal (suksess-) køyring av `validate-bronze`/`validate-data`
     framleis er stille som før, med `LOGLVL=DEBUG` som viser fanga output.
9. **Oppdater `bugs/`** dersom noko av dette viser seg å vere eit kjent,
   ikkje-triviell avvik som treng ein dokumentert workaround i staden for full
   fiks (t.d. dersom `emit-github-validation-annotations.py`-integrasjonen i
   `validate-data` viser seg å krevje større omskriving).

## Akseptansekriterier

- [x] `make validate-data` returnerer non-zero exit code når minst éi datafil
      feilar valideringa, og 0 elles
- [x] Ein kunstig induserte feil i `batch-flatten-and-validate.py`- eller
      `save-validation-log.py`-kalla i `validate-bronze`/`validate-data`/
      `validate-examples` produserer ei synleg `[ERROR]`-melding ved
      `LOGLVL=INFO` (default)
- [x] `detect-validation-policy.py` si ÅTVARING-linje er synleg for brukaren
      når policy-deteksjon feilar
- [x] `badges.sh` viser ikkje "✓ godkjent" for eit skjema med uleseleg/korrupt
      valideringsresultat
- [x] Normal (suksess-) køyring av alle tre valideringsmåla er upåverka
      (framleis stille output, identisk artefaktproduksjon)

## Relaterte filer

- `make/40-validation.mk` — `validate-bronze`, `validate-data`,
  `validate-examples`, `mcp-linkml-valider-modell`
- `make/00-settings.mk` — `run_logged`-definisjon (gjenbrukast, ikkje endrast)
- `src/mcp-linkml-validator/batch-flatten-and-validate.py`
- `src/assets/scripts/makefile/save-validation-log.py`
- `src/assets/scripts/makefile/emit-github-validation-annotations.py`
- `src/assets/scripts/makefile/detect-validation-policy.py`
- `mkdocs/lib/sections/badges.sh`
- `mkdocs/lib/utils/metadata_parsers.sh`
- `mkdocs/publish.sh`
- `src/mcp-linkml-modell-utkast/server.py`, `validator.py`
- `src/mcp-linkml-begrep-utkast/server.py`
- `.github/workflows/validate.yml` — kallar `make validate-data` som CI-steg
- `specs/done/ingen-stille-feil.md` — opphavleg audit og fiks
- `specs/backlog/evaluer-batching-resterande-kommandoar.md` — batching-arbeidet
  som introduserte regresjonen

## Utført

Avklaringar med brukar før implementering:
- **Steg 1 (annotasjonsnivå):** berre exit-kode + `log_error`-melding for
  `validate-data` (ikkje full `emit-github-validation-annotations.py`-
  integrasjon som `validate-bronze`).
- **Steg 6 (mkdocs/lib-scope):** fiksa no, sjølv om utanfor opphavleg
  filfokus.
- **Steg 7 (MCP-servar-scope):** fiksa no, sjølv om `src/mcp-linkml-validator/`
  sjølv framleis er halde utanfor (uendra frå den opphavlege spec-en).

Endringar:

- **`make/40-validation.mk`:**
  - `validate-data` (linje 78-132): lagt til `FAILED`-teljar, sjekk av
    `"valid": false` i resultat-JSON per datafil (`grep -Eq`), `log_error`
    med `::error file=...`-annotasjon, og `exit $$FAILED`. I same slag lagt
    til `< /dev/null` på `save-validation-log.py`-kallet i
    `while read ... done < "$$JOBS_TSV"`-løkka — eit nytt, udokumentert
    tilfelle av BUG-10 (stdin-konsumering), sidan denne løkka vart
    introdusert av batching-omskrivinga etter at BUG-10 vart løyst og
    dokumentert som "ikkje råka" (den gongen brukte `validate-data` ei
    `for`-løkke, ikkje `while read < fil`).
  - Alle fem attverande `2>/dev/null`/`2>/dev/null || true`-kall til
    `batch-flatten-and-validate.py`/`save-validation-log.py`
    (`validate-bronze` linje 56 og 65, `validate-data` linje 110 og 124,
    `validate-examples` linje 184) erstatta med `run_logged`.
  - `detect-validation-policy.py`-kallet (linje ~208) mista sin
    `2>/dev/null`, slik at scriptet si eiga ÅTVARING-linje når brukaren.
- **`mkdocs/lib/sections/badges.sh`:** valideringsstatus-parsing (linje ~55-65)
  skil no mellom "0 feil" og "kunne ikkje lese resultatfila" — sistnemnde
  behelt `val_status="ukjent"` (default) i staden for å falle tilbake på
  `errors="0"` → falsk "✓ godkjent"-badge, og skriv ei ÅTVARING til stderr.
- **`mkdocs/lib/utils/metadata_parsers.sh`:** `load_manifest_cache()` og
  `get_validation_policy()` skriv no ei ÅTVARING til stderr før fallback til
  tomme verdiar/`bronze` ved korrupt/uleseleg `build.yaml`.
- **`mkdocs/publish.sh`:** delmodell-oppslaget (linje ~254) skriv no ei
  ÅTVARING til stderr før fallback til tom submodels-liste ved korrupt
  `build.yaml`.
- **`mkdocs/lib/sections/delmodellar.sh`:** dei tre `python3 -c ... || echo
  default`-kalla (parent_title, sub_title, sub_desc) skriv no ei ÅTVARING til
  stderr ved parse-feil, i staden for å falle stille tilbake på
  skjemanamnet/tom streng.
- **`src/mcp-linkml-modell-utkast/server.py`,
  `src/mcp-linkml-begrep-utkast/server.py`:** `_list_profiles()` skriv no ei
  ÅTVARING til stderr med filsti og feiltekst når ein profil-YAML ikkje kan
  parsast, i staden for å stille falle tilbake på tom skildring.
- **`src/mcp-linkml-modell-utkast/validator.py`:** lagt til `import sys`;
  `_build_dummy_instance()` skriv no ei ÅTVARING til stderr med klassenamn og
  feiltekst i staden for `except Exception: pass`.

**Verifisert:**
- `bash -n` på alle fire endra shell-skript, `python3 -m py_compile` på alle
  tre endra Python-filer.
- `make validate-data DOMAIN=modellkatalog` (6 datakatalogar): suksess-sti
  identisk med før (stille output, exit 0, alle 6 loggfiler lagra korrekt).
  Kunstig indusert feil (lagt til eit ugyldig felt i éi datafil): synleg
  `[ERROR]`-melding med `::error file=...`, `make` avslutta med non-zero exit
  (`Error 1` frå recipe, `Error 2` frå make sjølv — konsistent med
  `validate-bronze`/`validate-examples` sitt eksisterande mønster).
- `make validate-bronze DOMAIN=fair`: suksess-sti identisk med før (stille
  output utanom forventa `::warning`-linjer, exit 0).
- `make validate-examples DOMAIN=fair`: suksess-sti identisk med før (stille
  output, exit 0).
- Isolert test av `detect-validation-policy.py`-kallet mot ein kunstig
  korrupt `build.yaml`: ÅTVARING-linja frå scriptet er no synleg (var
  usynleg før fiksen), fallback til `bronze` framleis korrekt.
- Isolert test av `badges.sh` sin valideringsstatus-logikk mot ei korrupt
  JSON-fil: `val_status` held seg på `ukjent`/`lightgrey` (ikkje lenger falsk
  `✓_godkjent`/`green`), ÅTVARING skriven til stderr.
- Alle test-induserte endringar i genererte `validation/*.json`-artefakt
  reverserte etter verifisering (`git checkout --`), slik at denne commit-en
  berre inneheld kjeldekodeendringane.

Alle 9 steg i spec-en er fullførte. Ingen `bugs/`-oppføring var naudsynt —
alle funn vart fiksa direkte, ikkje dokumenterte som workaround.
