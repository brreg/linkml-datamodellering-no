# Plan: `glow` for pen markdown-rendering av analyse-tabellane i demoen

## Bakgrunn

Brukaren spurde om det er mogleg å parse/rendre markdown pent i
terminalen — motivert av at `analyse-similar-classes-domain`/
`analyse-similar-slots-domain` (steg 5-6 i demoen) i dag dumpar rå
markdown-pipe-tabellar rett til terminalen, som er tunge å lese live for
eit publikum.

## Undersøking

Testa `glow` (Charm) live mot den faktiske tabell-outputen frå
`analyse-similar-slots-domain DOMAIN=ap-no`: rendrar korrekt kolonne-
justerte, tekstbrotne tabellar med feit overskrift — vesentleg meir
lesbart enn rå `|`-syntaks.

**`glow` finst ikkje i Ubuntu sine apt-repo** (stadfesta —
`apt-get install glow` feilar, "Unable to locate package"). Charm
distribuerer via eige apt-repo eller statiske binærfiler. Løysing: last
ned den statiske Linux-binærfila direkte frå GitHub Releases i
Dockerfile (`glow_3.0.0_Linux_x86_64.tar.gz`, verifisert korrekt
tarball-struktur — binærfila ligg i ein undermappe, ikkje i rota av
arkivet). Same eingongs-nettverksbehov som resten av
`demo-fun-tools`-biletet (apt-installasjon av figlet/toilet/cowsay/lolcat/boxes) —
ingen endring i offline-eigenskapane etter bygging.

## Plan

### 1 — Utvid `Dockerfile.fun-tools` med `glow`

```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL -o /tmp/glow.tar.gz https://github.com/charmbracelet/glow/releases/download/v3.0.0/glow_3.0.0_Linux_x86_64.tar.gz \
    && tar -xzf /tmp/glow.tar.gz -C /tmp \
    && mv /tmp/glow_3.0.0_Linux_x86_64/glow /usr/local/bin/glow \
    && chmod +x /usr/local/bin/glow \
    && rm -rf /tmp/glow.tar.gz /tmp/glow_3.0.0_Linux_x86_64
```

### 2 — Kople inn i steg 5/6 i `javazone-demo-script.sh`

Berre desse to stega produserer markdown (steg 3 er JSON, steg 8 er
YAML-fil + kort statuslinje — `glow` gjev ingen verdi der). Sidan
`step()` sin eksekveringsmodell er `"$@"` (direkte argv, ingen shell-pipe),
vert kvart steg sin `make | fun glow`-kombinasjon pakka i ein liten
wrapper-funksjon og sendt til `step()` som kommandoen:

```bash
run_analyse_classes() { make analyse-similar-classes-domain DOMAIN="$DOMAIN" | fun glow -w "$(tput cols 2>/dev/null || echo 100)" -; }
run_analyse_slots()   { make analyse-similar-slots-domain DOMAIN="$DOMAIN" | fun glow -w "$(tput cols 2>/dev/null || echo 100)" -; }
```

`tput cols` gjev faktisk terminalbreidd der scriptet køyrer (fell tilbake
til 100 dersom `tput` manglar/feilar, t.d. ved ikkje-interaktiv piping).

## Filer som vert påverka

- `src/assets/scripts/demo/Dockerfile.fun-tools`
- `src/assets/scripts/demo/javazone-demo-script.sh`

## Handlingsliste

1. [x] Utvid `Dockerfile.fun-tools` med `glow`
2. [x] Legg til `run_analyse_classes`/`run_analyse_slots`-wrapparar og
   kople dei inn i steg 5/6
3. [x] Verifiser: bygg biletet på nytt, køyr steg 5/6 og stadfest at
   tabellane renderer pent

## Utført

`Dockerfile.fun-tools` utvida med `curl`/`ca-certificates` (byggetids-
avhengigheiter) og `glow` (statisk binærfil frå GitHub Releases, sidan
han ikkje finst i Ubuntu sine apt-repo). `javazone-demo-script.sh` fekk
`run_analyse_classes`/`run_analyse_slots`-wrapparar som pipar
`make analyse-similar-*-domain` sin output gjennom
`fun glow -w "$(tput cols)"`, kopla inn i steg 5/6 i staden for dei
tidlegare direkte `make`-kalla. **Fallback lagt til:** dersom
`demo-fun-tools`-biletet ikkje finst, køyrer wrapparane rå `make`
direkte — analyseresultatet skal aldri gå tapt berre fordi pynt-biletet
manglar.

**Verifisert:** biletet bygd på nytt (glow-steget lukkast), og
`run_analyse_classes` testa isolert — tabellen renderer korrekt med
kolonnejustering og tekstbryting via `glow`.
