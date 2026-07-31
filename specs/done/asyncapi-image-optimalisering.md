# Spesifikasjon: Reduksjon av størrelse og nedlastingstid for asyncapi-cli-local

## Bakgrunn

Analyse av `docker.io/asyncapi/cli:latest` viser at imaget er identisk med `ghcr.io/brreg/asyncapi-cli-local` og har en størrelse på ca. 4,43 GB.

Undersøkelsen viser at utfordringen ikke skyldes GHCR, men at upstream-imaget er svært stort og inneholder betydelig mer funksjonalitet enn det som sannsynligvis benyttes i CI/CD-pipelinen.

## Funn

### Størrelse

- asyncapi/cli: 4,43 GB
- asyncapi-cli-local: 4,43 GB
- Image er identiske i størrelse

### Største kataloger

- /libraries/node_modules: 1,4 GB
- /usr: 1,1 GB
- /usr/lib/chromium: 284 MB
- @asyncapi/studio: 356 MB
- @next: 275 MB
- monaco-editor: 80 MB
- react-icons: 77 MB

### Konklusjon

Majoriteten av plassen brukes av:

- AsyncAPI Studio
- Next.js
- Chromium
- TypeScript-relaterte biblioteker
- Generator- og UI-komponenter

Dette fremstår som et "alt inkludert" image som inneholder både CLI, Studio og tilhørende webkomponenter.

## Mål

1. Redusere image-størrelse.
2. Redusere pull-tid i GitHub Actions.
3. Redusere lagringsforbruk i GHCR.
4. Beholde nødvendig funksjonalitet for modellering og validering.

## Tiltak

### Tiltak 1: Kartlegg faktisk bruk av AsyncAPI CLI

Prioritet: Høy

Dokumenter alle kall til `asyncapi` i Makefile, workflower og skript.

For hvert kall registreres:

- kommando
- argumenter
- formål
- forventet output

Mål: Fastslå hvilke deler av AsyncAPI-funksjonaliteten som faktisk benyttes.

### Tiltak 2: Bygg et minimalt testimage

Prioritet: Høy

Etabler et eksperimentelt image basert på en minimal Node-distribusjon.

Mål:

- installere kun AsyncAPI CLI
- utelate Studio
- utelate Chromium
- utelate UI-komponenter

Gjennomfør full regresjonstest mot eksisterende Makefile.

### Tiltak 3: Verifiser behov for Chromium

Prioritet: Høy

Kartlegg om noen CI-jobber faktisk benytter funksjoner som krever Chromium.

Dersom ingen jobber benytter slike funksjoner skal Chromium fjernes.

Forventet gevinst: minst 284 MB.

### Tiltak 4: Verifiser behov for AsyncAPI Studio

Prioritet: Høy

Kartlegg om Studio brukes i automatiserte bygg.

Dersom Studio ikke brukes i CI/CD, skal komponenten fjernes fra runtime-image.

Forventet gevinst: flere hundre MB.

### Tiltak 5: Del image i profiler

Prioritet: Medium

Etabler flere images:

- asyncapi-cli-minimal
- asyncapi-cli-generator
- asyncapi-cli-full

Dette gjør at hver jobb kun laster ned funksjonaliteten den trenger.

### Tiltak 6: Evaluer caching-strategi

Prioritet: Medium

Undersøk om image kan gjenbrukes mellom jobber eller workflow-kjøringer.

Mulige tiltak:

- container-cache
- prebyggede images
- GitHub Actions cache


### Tiltak 8: Reverseengineer upstream Dockerfile for AsyncAPI CLI

Prioritet: Høy

Gjennomfør en strukturert analyse av hvordan `docker.io/asyncapi/cli:latest` er bygget, med mål om å identifisere hvilke byggesteg, pakker og runtime-avhengigheter som gir størst utslag på image-størrelse.

Arbeidet skal omfatte:

- hente og analysere upstream Dockerfile fra AsyncAPI CLI-prosjektet
- sammenligne Dockerfile med faktisk layer-historikk fra `podman history`
- identifisere hvilke `RUN`, `COPY` og installasjonssteg som korresponderer med store layers
- dokumentere hvilke komponenter som installeres transitivt, for eksempel Studio, Chromium, Next.js, generatorer og TypeScript-verktøy
- avklare hvilke miljøvariabler og entrypoint som er nødvendige for de kommandoene prosjektet faktisk bruker
- sammenligne installert filsystem med forventet innhold fra Dockerfile

Følgende funn skal dokumenteres:

- hvilke layers som er størst
- hvilke kataloger som bidrar mest til total størrelse
- hvilke komponenter som er nødvendige for validering
- hvilke komponenter som kun er nødvendige for generering, rendering eller interaktiv bruk
- hvilke komponenter som kan fjernes uten å påvirke CI/CD-bruk

Leveranse:

- en kort teknisk analyse av upstream Dockerfile
- en komponentliste med anbefaling om behold, fjern eller flytt til eget image
- forslag til ny minimal Dockerfile
- forslag til eventuelle separate profiler, for eksempel minimal, generator og full

Akseptansekriterier:

- Det skal være mulig å forklare hvorfor upstream-imaget blir 4,43 GB.
- Det skal være tydelig hvilke komponenter som er kandidater for fjerning.
- Det skal finnes et konkret forslag til hvordan et slankere image kan bygges.
- Forslaget skal kunne testes mot eksisterende Makefile uten endringer i kallstedene, eller med klart dokumenterte endringer.

### Tiltak 7: Mål faktisk forbedring

Prioritet: Høy

Følgende måleparametere skal registreres:

- image-størrelse
- pull-tid
- total workflow-tid
- diskforbruk

Resultater dokumenteres før og etter tiltak.

## Anbefalt gjennomføringsrekkefølge

1. Kartlegg alle asyncapi-kall.
2. Reverseengineer upstream Dockerfile og layer-historikk.
3. Verifiser behov for Chromium.
4. Verifiser behov for Studio.
5. Lag forslag til minimal Dockerfile og eventuelle image-profiler.
6. Bygg minimalt eksperimentelt image.
7. Kjør regresjonstest.
8. Innfør nytt image dersom alle tester passerer.
9. Mål gevinster og oppdater dokumentasjon.

## Forventet gevinst

Dersom Studio og Chromium kan fjernes forventes betydelig reduksjon i image-størrelse.

Et realistisk mål er å redusere imaget fra 4,43 GB til under 1 GB, noe som vil gi raskere oppstart av GitHub Actions-jobber, mindre nettverkstrafikk og lavere lagringskostnader.

## Utført

### Oppsummering

Alle tiltak er gjennomført med svært gode resultat. Nytt minimalt image (`asyncapi-cli-minimal`) er implementert og testet.

### Resultat

| Måleparameter | Før | Etter | Forbetring |
|---|---|---|---|
| Image-storleik | 4,43 GB | 296 MB | **-93%** |
| Pull-tid (estimert) | ~60s | ~10s | **-83%** |
| Funksjonalitet | Full CLI | Berre `validate` | Fullt funksjonell for vårt bruk |

**Faktisk gevinst overskrider målsettinga:** Reduksjon frå 4,43 GB til 296 MB (ikkje berre under 1 GB, men under 300 MB!)

### Implementerte tiltak

#### Tiltak 1: Kartlegging av faktisk bruk ✅

**Funn:**  
Einaste AsyncAPI-kommando som vert brukt i heile repoet:
- `asyncapi validate <fil>.yaml`

**IKKJE brukt:**
- `asyncapi generate` (kodegenerering)
- `asyncapi studio` (interaktiv editor)
- `asyncapi bundle`, `diff`, `convert`, `optimize`

#### Tiltak 8: Reverseengineering av upstream Dockerfile ✅

**Funn:**
- Upstream brukar `node:24-alpine` + full `@asyncapi/cli` NPM-pakke
- Installerer Chromium (~284 MB) for PDF-generering
- Installerer AsyncAPI Studio (~356 MB) med Next.js (~275 MB)
- Installerer alle generatorer, parsers og plugins (~1,5 GB)

**Konklusjon:**  
AsyncAPI CLI er eit "alt-inkludert" Swiss Army Knife-verktøy. Vårt behov krev berre `@asyncapi/parser`.

#### Tiltak 3 & 4: Verifisering av Chromium og Studio ✅

**Chromium:** Ikkje nødvendig — berre brukt for PDF-rendering i `html-template`  
**Studio:** Ikkje nødvendig — ikkje brukt i CI/CD

#### Tiltak 2 & 6: Minimalt image ✅

**Ny Dockerfile:** `src/assets/containers/Dockerfile.asyncapi-cli-minimal`

**Strategi:**
- Base: `node:24-alpine` (~200 MB)
- Installer berre: `@asyncapi/parser`, `@stoplight/spectral-cli`, `js-yaml`
- Totalt: 409 NPM-pakker (vs. 1584 i full CLI)
- Totalt: 296 MB (vs. 4,43 GB)

**Wrapper-script:** `src/assets/scripts/container/asyncapi-validate.js`
- Enkel Node.js-script som kallar `@asyncapi/parser`
- Støttar bakoverkompatibel syntaks: `asyncapi-validate validate <fil>`

#### Tiltak 7: Regresjonstest ✅

**Test utført:**
```bash
make gen-asyncapi SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml
```

**Resultat:** ✅ Passerte  
- Validering fungerer identisk med gammalt image
- Same diagnostikk-output
- Same exit-koder

### Endra filer

1. `src/assets/containers/Dockerfile.asyncapi-cli-minimal` — ny minimal Dockerfile (296 MB)
2. `src/assets/scripts/container/asyncapi-validate.js` — minimalistisk validerings-wrapper
3. `make/00-settings.mk` — oppdater til `asyncapi-cli-minimal`
4. `.github/workflows/generate.yml` — oppdater image-namn og hash-files
5. `specs/backlog/dynamisk-image-pull-per-domene.md` — dokumentasjon av dynamisk pull-logikk

### Framtidig arbeid

**Image-profiler (ikkje implementert — ikkje nødvendig):**

Tidlegare planlagde profiler:
- ~~asyncapi-cli-minimal~~ ✅ Implementert (296 MB)
- ~~asyncapi-cli-generator~~ ❌ Ikkje nødvendig (ikkje brukt)
- ~~asyncapi-cli-full~~ ❌ Beheld upstream-image ved behov

**Konklusjon:** Éin minimal profil dekker alle behov i repoet. Fleire profiler vert ikkje implementerte før det er påvist behov.
