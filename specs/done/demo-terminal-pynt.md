# Plan: figlet/toilet/cowsay/lolcat/boxes for demo-scriptet, utan lokal installasjon

## Bakgrunn

Brukaren vil bruke `figlet`, `toilet`, `cowsay`, `lolcat` og `boxes` for å
friske opp terminaloutput i JavaZone-demoen, men vil ikkje installere dei
lokalt — matchar repoet sitt generelle prinsipp om at verktøy skal køyrast
containerisert med podman, ikkje installerast på verten.

## Undersøking

Testa live med ein eigen `podman build` (ikkje del av repoet sitt
eksisterande `images.json`-registrerte byggsystem, sidan dette er
demo-spesifikt pynt, ikkje kjerne-genereringsverktøy — same prinsipp som
`migreringsscript/` (ingen eigne make-target)):

- Alle fem pakkane finst reint i Ubuntu 22.04 sine standard apt-repo
  (`figlet toilet cowsay lolcat boxes` — éin `apt-get install`, ingen
  ekstra repo/PPA naudsynt)
- **Snublestein funne og retta:** `cowsay` og `lolcat` installerer til
  `/usr/games/` (Debian/Ubuntu sin «games»-FHS-konvensjon), som **ikkje**
  er i default `$PATH` i ein container — dei feila med
  «executable file not found» til `ENV PATH="/usr/games:${PATH}"` vart
  lagt til i imaget

## Plan

### 1 — Nytt Dockerfile

`src/assets/scripts/demo/Dockerfile.fun-tools`:

```dockerfile
FROM docker.io/library/ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends \
    figlet toilet cowsay lolcat boxes \
    && rm -rf /var/lib/apt/lists/*
ENV PATH="/usr/games:${PATH}"
```

### 2 — Lat biletbygging + wrapper-funksjon i demo-scriptet

`javazone-demo-script.sh` sjekkar om `localhost/demo-fun-tools` finst,
byggjer han automatisk fyrste gong (same «bygg berre viss det manglar»-
mønster som resten av repoet sine make-target), og definerer ein enkel
`fun()`-wrapper-funksjon:

```bash
fun() { podman run --rm -i "$FUN_IMAGE" "$@"; }
```

Bruk: `fun figlet "tekst"`, `... | fun lolcat -f`, `... | fun cowsay`,
`... | fun boxes`, `fun toilet "tekst"`.

### 3 — To tasteful pynt-punkt i scriptet (ikkje meir)

Med 10 minutt totalt bør pynten vere kort og ikkje stele tid frå sjølve
den tekniske demoen:

- **Opning:** figlet-banner pipa gjennom lolcat, før steg 1
- **Avslutning:** ei kort cowsay-helsing etter «Demo ferdig»

Ingen pynt inni sjølve steg 1-8 — dei skal halde fram reint fokuserte på
kommandoane og output.

### Offline-konsekvens

Fyrste `podman build` av `demo-fun-tools` treng nettverk (pullar
`ubuntu:22.04` + apt-pakkar). Legg til i offline-sjekklista i
[[javazone-demo-plan]]: bygg biletet på førehand, medan nettverk er
tilgjengeleg.

## Filer som vert påverka

- `src/assets/scripts/demo/Dockerfile.fun-tools` (ny)
- `src/assets/scripts/demo/javazone-demo-script.sh` (lat biletbygging +
  `fun()`-wrapper + to pynt-punkt)
- `specs/backlog/javazone-demo-plan.md` (offline-sjekklista utvida)

## Handlingsliste

1. [x] Opprett `Dockerfile.fun-tools`
2. [x] Legg til lat biletbygging + `fun()`-wrapper i demo-scriptet
3. [x] Legg til figlet+lolcat-opning og cowsay-avslutning
4. [x] Oppdater offline-sjekklista i `javazone-demo-plan.md`
5. [x] Verifiser: køyr scriptet frå botnen, stadfest at biletet
   auto-byggjer fyrste gong og at alle fem verktøya renderer korrekt

## Utført

`src/assets/scripts/demo/Dockerfile.fun-tools` bygd og verifisert —
`ubuntu:22.04` med `figlet toilet cowsay lolcat boxes` via apt, pluss
`ENV PATH="/usr/games:${PATH}"` for å fikse at `cowsay`/`lolcat` elles
ikkje vart funne (Debian/Ubuntu sin «games»-FHS-konvensjon, oppdaga under
verifiseringa).

`javazone-demo-script.sh`: lat biletbygging (byggjer `localhost/demo-fun-tools`
berre viss han manglar, feilar ikkje heile scriptet om biletbygginga
skulle feile — held berre fram utan pynt), `fun()`-wrapper-funksjon, eit
figlet+lolcat-banner heilt i opninga, og ei kort cowsay-helsing etter
«Demo ferdig».

**Verifisert med reelle køyringar:**
- `podman build` av `Dockerfile.fun-tools` lukkast
- Alle fem verktøy testa individuelt (`figlet`, `toilet`, `cowsay`,
  `boxes`, `lolcat` — pipa gjennom kvarandre der aktuelt) — alle
  fungerer korrekt, inkludert UTF-8 (æøå) i `cowsay`-teksten
- Heile scriptet køyrt frå botnen med `printf '\n' | bash ...` —
  banneret vises korrekt før steg 1, resten av flyten uendra
