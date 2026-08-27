# Plan: løys sirkelavhengigheita i `make check-prereqs`

## Bakgrunn

Brukaren set opp repoet på ein ny PC utan `podman` og `make` installert frå
før. Det fyrste steget i README.md sin "Kom i gang"-seksjon
(`README.md:64`) er `make check-prereqs` — men det kommandoen skal gjere er
nettopp å *sjekke* om `make` (og podman m.m.) er installert. På ein maskin
utan `make` feilar `make check-prereqs` med `make: command not found` før
sjekken i det heile kan køyre — ein sirkelavhengigheit: verktøyet som skal
fortelje deg kva som manglar, krev sjølv at det manglande alt er der.

**Funn ved gjennomgang av eksisterande kode:** problemet er reint eit
dokumentasjons-/discoverability-problem, ikkje eit script-problem.
Sjølve sjekkescriptet, `src/assets/scripts/makefile/check-prereqs.bash`,
har **ingen** reell avhengigheit til `make`:

- Det er ei frittståande bash-fil, alt merkt køyrbar (`rwxrwxrwx`).
- Det einaste stadet `make` nemnast inni scriptet er sjølve *sjekken* av om
  GNU make er installert (`make --version 2>/dev/null | grep -q "GNU
  Make"`, linje 18). Denne konstruksjonen fungerer korrekt sjølv om `make`
  ikkje finst i det heile — `if`-konteksten gjer at `set -e` ikkje utløysast,
  og resultatet vert korrekt rapportert som `✗ GNU make ikkje funne`.
- Scriptet krev heller ikkje `podman` for å køyre — det berre sjekkar om
  `podman`-kommandoen finst (linje 32) og om rootless-modus fungerer
  (linje 39), og rapporterer `✗`/`⚠` dersom ikkje.

Scriptet kan altså allereie køyrast heilt fint **før** `make` og `podman`
er installerte:

```bash
bash src/assets/scripts/makefile/check-prereqs.bash
```

Problemet er at README.md og COMMANDS.md berre dokumenterer
`make check-prereqs`-forma, som skjuler denne moglegheita for brukarar som
enno ikkje har `make` installert — nettopp brukarane som treng
sjekken mest.

## Løysing

Ingen endring i sjølve `check-prereqs.bash`-logikken er naudsynt. Løysinga
er å dokumentere den direkte bash-invokeringa som det faktiske fyrste
steget, og gjere `make check-prereqs` til ein bekvem snarveg for når `make`
alt er stadfesta installert.

## Steg

1. **README.md** (`## Kom i gang`, rundt linje 60-65): legg til den direkte
   bash-invokeringa som det reelle fyrste steget, med `make check-prereqs`
   som alternativ når `make` alt er på plass. Eksempel på ny tekst:

   ```bash
   # Steg 1 — før du har installert make/podman: køyr sjekkescriptet direkte
   bash src/assets/scripts/makefile/check-prereqs.bash
   ```

   ```bash
   # Når make er stadfesta installert kan du bruke make-targetet i staden
   make check-prereqs
   ```

2. **COMMANDS.md** (raden for `check-prereqs`, linje 9): legg til ei
   fotnote/merknad om at scriptet bak targetet (`check-prereqs.bash`) kan
   køyrast direkte med `bash` utan at `make` er installert frå før, og at
   dette er den tilrådde framgangsmåten på ein heilt ny maskin.

3. **`src/assets/scripts/makefile/check-prereqs.bash`**: legg til ein kort
   kommentar øvst i fila (etter shebang) som gjer det eksplisitt at scriptet
   er designa for å køyrast standalone (utan `make`), slik at framtidige
   endringar i scriptet ikkje utilsikta introduserer ei reell
   make-avhengigheit (t.d. eit `$(MAKE)`-kall eller liknande).

4. **Verifiser:**
   - Køyr `bash src/assets/scripts/makefile/check-prereqs.bash` i eit miljø
     der `make` mellombels er fjerna frå `PATH` (t.d.
     `PATH=$(echo "$PATH" | tr ':' '\n' | grep -v /usr/bin | tr '\n' ':') bash
     src/assets/scripts/makefile/check-prereqs.bash` eller tilsvarande), og
     stadfest at output framleis viser `✗ GNU make ikkje funne` utan at
     scriptet krasjar.
   - Stadfest at `make check-prereqs` framleis fungerer uendra når `make`
     er installert (ingen regresjon i det eksisterande targetet).

## Handlingsliste

- [x] Oppdater README.md "Kom i gang"-seksjonen med direkte
      bash-invokering som primær instruks
- [x] Oppdater COMMANDS.md-raden for `check-prereqs` med merknad om
      standalone bruk
- [x] Legg til kommentar i `check-prereqs.bash` om standalone-designet
- [x] Verifiser standalone-køyring utan `make` i `PATH`
- [x] Verifiser at `make check-prereqs` framleis fungerer uendra

## Utført

- README.md: bytt `make check-prereqs`-blokka ut med to steg — direkte
  `bash src/assets/scripts/makefile/check-prereqs.bash` fyrst, deretter
  `make check-prereqs` som snarveg når make alt er installert
- COMMANDS.md: la til merknad under `check-prereqs`-rada om at scriptet
  bak targetet kan køyrast standalone utan make/podman
- `check-prereqs.bash`: la til kommentar øvst som gjer standalone-designet
  eksplisitt, for å hindre at framtidige endringar introduserer ei reell
  make-avhengigheit
- Verifisert: `bash check-prereqs.bash` med `make` fjerna frå `PATH` gjev
  korrekt `✗ GNU make ikkje funne`-output og kode 1, ingen krasj
- **Merk:** `make check-prereqs` sjølv kunne **ikkje** verifiserast uendra
  på denne maskina, sidan `make` faktisk ikkje er installert her (same
  situasjon som brukaren skildra). Sjølve make-targetet
  (`make/90-tools.mk`) er ikkje endra av desse stega, så ingen regresjon
  er venta — men dette bør stadfestast av brukaren på ei maskin med make
  installert.
