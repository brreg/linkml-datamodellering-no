# Fiks nøkkelnamn-mismatch i gen-dqv-measurements.py

## Bakgrunn

Avdekt under gjennomgangen i `specs/done/verifiser-vurderinger-standardetterleving.md`
(gap 7): `src/assets/scripts/makefile/gen-dqv-measurements.py` les nøkkelen
`data_policy` frå datamanifest (`build.yaml`), men repoet gjennomførte ei
namneendring frå `data_policy` → `validation_policy` for alle manifest (sjå
`specs/done/validering-logging-publish.md`, steg 2). Scriptet vart aldri
oppdatert i den migreringa.

Konsekvens: `manifest.get("data_policy")` returnerer alltid `None`,
`PROFILES.get(None)` returnerer `None`, og `main()` hoppar stille over **alle**
datafiler — ingen feilmelding, ingen synleg indikasjon på at noko er gale
(`0 datafil(er) oppdatert.` ser ut som ein triviell "ingenting å gjere"-status).
`brreg-begrepskatalog.yaml` har difor null `kvalitetsmaalingar`, og
`brreg-modellkatalog.yaml` har berre gamle, ikkje oppdaterte målingar.

## Steg

1. Rett nøkkelnamnet `data_policy` → `validation_policy` alle stader i
   `gen-dqv-measurements.py` (docstring, kommentar, `main()`-oppslag).
2. Legg til ei synleg åtvaring (stderr) når eit datamanifest har ein
   `validation_policy`-verdi som ikkje finst i `PROFILES` — i tråd med
   "Ingen stille feil"-prinsippet i CLAUDE.md, slik at ein framtidig
   nøkkel-/verdi-mismatch ikkje igjen forsvinn stille.
3. Oppdater `COMMANDS.md` sin omtale av scriptet (nemner `data_policy`).
4. Køyr `make gen-dqv-measurements` og verifiser at
   `brreg-begrepskatalog.yaml` og alle 6 modellkatalog-datafilene får
   `kvalitetsmaalingar` skrivne/oppdaterte.
5. Køyr `make lint`/`make roundtrip` på dei påverka skjema for å
   stadfeste at dei genererte datafilene framleis er gyldige.
6. Oppdater `mkdocs/docs/arkitektur/standardetterleving.md`: rad
   "Beskrivelse av kvalitet på datasett" tilbake til ✅, og fjern/marker
   gap 7 i "Attverande gap"-tabellen som løyst.

## Utført

1. **Nøkkelnamn retta** i `gen-dqv-measurements.py` (docstring, kommentar,
   `main()`-oppslag): `data_policy` → `validation_policy`.
2. **Ny stille-feil-vern** lagt til: `main()` skriv no ei stderr-åtvaring
   («ukjend/manglande validation_policy») for datamanifest som ikkje matchar
   nokon `PROFILES`-nøkkel, i staden for å hoppe stille over.
3. **`COMMANDS.md`** oppdatert til å nemne `validation_policy` i staden for
   `data_policy` for `gen-dqv-measurements`-rada.
4. **Verifisert med `make gen-dqv-measurements`:** scriptet finn no alle 6
   datamanifest (var 0 før fiksen). `brreg-modellkatalog.yaml` fekk oppdaterte
   (friske) tal — verifisert gyldig med `make validate-instance`.

**To nye, separate gap avdekt under verifisering (ikkje del av denne fiksen):**

- **`brreg-begrepskatalog.yaml` manglar framleis kvalitetsmålingar** — ikkje
  nøkkelnamn-mismatchen, men fordi datafila ikkje har nokon `samlingar:`-blokk
  i det heile (`collect-concepts.py` genererer berre `begrep:`). Scriptet krev
  akkurat éin `samlingar`-oppføring for å kunne ankre målinga med tekstinnsetting,
  og hoppar difor korrekt (med synleg melding) over fila.
- **5 av 6 modellkatalog-skjema manglar `kvalitetsmaalingar`-attributtet** på
  `ModellkatalogContainer`-klassen (`digdir-`, `kartverket-`, `ksdigital-`,
  `novari-`, `skatteetaten-modellkatalog-schema.yaml`) — berre
  `brreg-modellkatalog-schema.yaml` har attributtet. Første køyring av det
  fiksa scriptet skreiv difor schema-ugyldige `kvalitetsmaalingar:`-blokker inn
  i desse 5 datafilene (`Additional properties are not allowed`); dette vart
  oppdaga av `make validate-instance` og endringane i dei 5 filene er reverterte
  (`git checkout --`) att til opphavleg tilstand. Berre `brreg-modellkatalog.yaml`
  sin oppdatering står att, sidan dette er det einaste skjemaet som faktisk
  støttar attributtet i dag.

Desse to gapa er **ikkje** løyste som del av denne specen — dei krev anten (a)
at `collect-concepts.py` også skriv ein `samlingar:`-container, eller (b) at
`kvalitetsmaalingar` vert lagt til dei 5 andre `ModellkatalogContainer`-klassane
(og på sikt bør denne nær-identiske klassa vurderast faktorisert til eit delt
importert basisskjema, jf. DRY-prinsippet i CLAUDE.md). Sjå
`mkdocs/docs/arkitektur/standardetterleving.md` for oppdatert gap-status.
