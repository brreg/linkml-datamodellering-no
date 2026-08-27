# Plan: legg til jq som kjend føresetnad

## Bakgrunn

`make new-modell DOMAIN=oreg NAME=javazonetalk` feila med
`jq: command not found` (`src/assets/scripts/scaffolding/new-modell.sh:42`,
som les `DCAT_AP_NO_VERSION` frå `.github/release-please-manifest.json` via
`jq`). `jq` er dermed ei reell føresetnad for scaffolding-flyten, men er
ikkje sjekka av `src/assets/scripts/makefile/check-prereqs.bash` eller nemnt
i README.md/COMMANDS.md — feilen dukkar difor fyrst opp midt i eit
scaffolding-steg, ikkje ved oppsett.

## Steg

1. **`check-prereqs.bash`**: legg til ein `jq`-sjekk (same mønster som
   Git-sjekken: `command -v jq`), med installasjonshint for apt.
2. **COMMANDS.md** (raden for `check-prereqs`, linje 9): legg `jq` til lista
   over sjekka føresetnadar.
3. **README.md** (`## Kom i gang`, "Føresetnader"-linja): legg `jq` til
   verktøylista.
4. **Verifiser:** køyr `bash src/assets/scripts/makefile/check-prereqs.bash`
   og stadfest at jq-linja viser korrekt OK/FEIL avhengig av om jq er
   installert.

## Handlingsliste

- [x] Legg til jq-sjekk i check-prereqs.bash
- [x] Oppdater COMMANDS.md-raden for check-prereqs
- [x] Oppdater README.md føresetnadar-lista
- [x] Verifiser standalone-køyring av check-prereqs.bash

## Utført

- `check-prereqs.bash`: la til jq-sjekk (same mønster som Git), plassert før
  Podman-sjekken
- COMMANDS.md: la til jq i lista over sjekka føresetnadar i
  `check-prereqs`-rada
- README.md: la til jq i "Føresetnader"-lista under "Kom i gang"
- Verifisert: `bash check-prereqs.bash` viser korrekt
  `✗ jq ikkje funne`-melding med installasjonshint på denne maskina (jq er
  faktisk ikkje installert her — same rotårsak som feilen i
  `make new-modell`)
