# Handter plantuml på same måte som andre build-image-jobbar

## Bakgrunn

`plantuml` er implementert med ein hardkoda `hash_files: "2026-07-06"` i `.github/workflows/generate.yml`. Dette gjer at imaget ikkje vert oppdatert automatisk når upstream `docker.io/plantuml/plantuml:latest` endrar seg, og skil seg frå dei andre build-image-jobbane som brukar `hashFiles()` på Dockerfile-innhaldet.

For at `plantuml` skal handterast på same måte som dei andre imagea, må den:
- Bruke ein stabil hash basert på **faktisk innhald** (ikkje ein manuelt vedlikehalden datostempel)
- Oppdaterast automatisk når upstream-imaget endrar seg

Sidan `plantuml` er eit upstream-image utan lokal Dockerfile, må vi bruke **image digest** frå `docker.io/plantuml/plantuml:latest` som hash-kjelde.

## Løysing

**Strategi 1: Bruk Dockerfile som wrapper rundt upstream-image**

1. Legg til Dockerfile som pullar og aliasarar upstream-imaget:
   ```dockerfile
   # src/assets/containers/Dockerfile.plantuml
   FROM docker.io/plantuml/plantuml:latest
   ```
2. Endre `matrix.image` for `plantuml`:
   - `dockerfile: src/assets/containers/Dockerfile.plantuml`
   - `hash_files: src/assets/containers/Dockerfile.plantuml`
   - `make_target: build-docker-plantuml` (ny target)
3. Legg til `build-docker-plantuml` i Makefile som byggjer frå Dockerfile
4. Fjern `pull-plantuml`-target
5. Reverser workaround med `set-tag`-steg

**Problem:** Dockerfilen endrar seg aldri, så `hashFiles()` vil alltid returnere same hash — imaget vert aldri oppdatert sjølv om upstream endrar seg.

**Strategi 2: Pin upstream image med digest i Dockerfile**

1. Hent digest for `docker.io/plantuml/plantuml:latest` manuelt eller via script
2. Legg til Dockerfile med pinned digest:
   ```dockerfile
   # src/assets/containers/Dockerfile.plantuml
   FROM docker.io/plantuml/plantuml@sha256:<digest>
   ```
3. Oppdater digest-en manuelt/automatisk når upstream endrar seg
4. Bruk `hashFiles()` på Dockerfilen

**Problem:** Dette krev manuell eller automatisert vedlikehald av digest-en.

**Strategi 3: Hent digest dynamisk i workflow (føreslått)**

1. Legg til steg i `ensure-images` som hentar digest frå `docker.io/plantuml/plantuml:latest`:
   ```yaml
   - name: Hent upstream digest for plantuml
     if: matrix.image.name == 'plantuml'
     id: upstream-digest
     run: |
       DIGEST=$(skopeo inspect docker://docker.io/plantuml/plantuml:latest | jq -r '.Digest' | cut -d: -f2 | cut -c1-12)
       echo "digest=$DIGEST" >> $GITHUB_OUTPUT
   ```
2. Endre `hash_files` for `plantuml` til å bruke digest-outputen
3. Behald `pull-plantuml`-target, men endre Makefile til å tagge med digest

**Fordel:** Automatisk oppdatering når upstream endrar seg, ingen manuelt vedlikehald.

## Val: Strategi 1 (Dockerfile wrapper)

Brukar ein lokal Dockerfile som wrapper rundt upstream-imaget. Dette gjer at `plantuml` handterast på nøyaktig same måte som dei andre build-image-jobbane.

**Trade-off:** Imaget vert berre oppdatert når Dockerfilen endrar seg (t.d. ved å legge til ein kommentar med dato). Dette er akseptabelt sidan upstream `plantuml/plantuml:latest` endrast sjeldan, og manuell oppdatering gir kontroll over når nye versjonar vert tatt i bruk.

## Tiltak

- [x] Opprett `src/assets/containers/Dockerfile.plantuml`
- [x] Endre `matrix.image.plantuml` i `.github/workflows/generate.yml`
- [x] Legg til `build-docker-plantuml` i Makefile
- [x] Fjern `pull-plantuml`-target frå Makefile
- [x] Reverser `set-tag`-workaround i workflow
- [x] Oppdater alle referansar til å bruke `hashFiles()` konsistent
- [x] Endre `PLANTUML_IMAGE` i Makefile til `localhost/plantuml:latest`
- [x] Fjern `-upstream`-suffiks frå alle namn (image, target, variabel)
- [x] Oppdater `COMMANDS.md` med `build-docker-plantuml`-target

## Utført

`plantuml` byggjer no frå `Dockerfile.plantuml` og brukar `hashFiles()` på same måte som dei andre imagea. Alle referansar i `ensure-images` og `generate`-jobbane er oppdaterte til å bruke `hashFiles('src/assets/containers/Dockerfile.plantuml')`. Image-namnet er endra frå `plantuml-upstream` til `plantuml` for å matche dei andre lokale imagea.
