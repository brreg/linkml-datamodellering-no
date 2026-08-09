# Prerequisite-sjekk og oppdaterte eksempel i ekstern-bruk.md

## Bakgrunn

Brukaren bad om to endringar i `mkdocs/docs/arkitektur/ekstern-bruk.md`:

1. Dokumenter ein **prerequisite-sjekk** for eksterne repo (i dag manglar
   sida heilt ei sjekk av at Podman/rootless/user namespace er korrekt
   konfigurert før dei podman-baserte eksempla i "Lokal utvikling" faktisk
   kan køyrast).
2. "Lokal utvikling"-overskrifta bør innehalde eksempel som **samsvarar
   med** mønsteret i `mkdocs/docs/kom-i-gang/ny-domenemodell.md`.

Under kartlegginga vart det oppdaga to konkrete, urelaterte bugar som
direkte påverkar korleis punkt 1 og 2 bør løysast — begge dokumenterte i
"Funn" under, sidan dei avgjer kva som er "korrekt mønster å matche".

## Funn

### A. `ny-domenemodell.md` steg 0 refererer til make-target som ikkje finst

`mkdocs/docs/kom-i-gang/ny-domenemodell.md` linje 9-14:

```bash
make check-prereqs
make linkml-build-docker && make python-build-docker && make mcp-val-build
```

`grep -rn "^linkml-build-docker:\|^python-build-docker:\|^mcp-val-build:"
make/*.mk Makefile` gjev **null treff** — desse tre måla finst ikkje. Dei
faktiske måla (stadfesta i `make/80-images.mk` og `COMMANDS.md` §
"Container-image-bygging") er `build-docker-linkml`, `build-docker-python`
og `build-docker-mcp-validator`. `check-prereqs` sjølv er korrekt (finst i
`make/90-tools.mk`).

Dette er ein pre-eksisterande, urelatert dokumentasjonsbug i
`ny-domenemodell.md` — ikkje noko denne økta introduserer. Han bør rettast
**før** ekstern-bruk.md sitt "Lokal utvikling"-avsnitt vert justert til å
"samsvare" med denne fila, elles kopierer vi feilen vidare.

### B. `ekstern-bruk.md` sitt eksisterande "Lokal utvikling"-eksempel bruker eit ugyldig CLI-flagg

`mkdocs/docs/arkitektur/ekstern-bruk.md` linje 202-207:

```bash
# Valider skjema lokalt
podman run --rm \
  -v "$(pwd):/work" -w /work \
  ghcr.io/brreg/linkml-local:latest \
  gen-linkml --validate src/linkml/mitt-domene/min-modell/min-modell-schema.yaml
```

`--validate` var eit flagg for `linkml lint` (`linkml lint --validate`),
**ikkje** for `gen-linkml` — stadfesta avvikla/fjerna i LinkML 1.13.0, sjå
`bugs/lint-validate-flag-deprecated.md`. `gen-linkml` sjølv tek berre
skjemastien, og gjer fail-fast strukturvalidering ved berre å køyre
(output diskardast) — nøyaktig mønsteret internt kode alt bruker
(`src/assets/scripts/migreringsscript/migrate-all-containers.sh` linje
145: `${LINKML_RUN} gen-linkml "${schema}"`, og
`make/10-generator-macros.mk` sin kommentar: "gen-linkml — reint
fail-fast valideringssteg"). Korrekt eksempel er `gen-linkml <schema>`
utan flagg.

### C. `check-prereqs.bash` er allereie ein fullstendig frittståande, curl-bar script

`src/assets/scripts/makefile/check-prereqs.bash` har **ingen** avhengigheit
til dette repoet sin Makefile-tilstand eller katalogstruktur — han sjekkar
berre systemføresetnader (GNU make, Git, Podman, Podman rootless,
`/etc/subuid`/`/etc/subgid`, WSL2, diskplass) og er reint `bash`. Han kan
difor curl-ast og køyrast standalone i eit eksternt repo, akkurat som
`bootstrap.sh` alt vert dokumentert brukt i `ekstern-bruk.md`:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/assets/scripts/makefile/check-prereqs.bash | bash
```

Dette er den naturlege løysinga på punkt 1 — ingen ny funksjonalitet
trengst, berre dokumentasjon av eit alt eksisterande, gjenbrukbart script.

## Steg

1. **Rett `ny-domenemodell.md` steg 0** (`make/80-images.mk`/`COMMANDS.md`
   som fasit): byt `make linkml-build-docker && make python-build-docker
   && make mcp-val-build` med `make build-docker-linkml && make
   build-docker-python && make build-docker-mcp-validator`.
2. **Rett det eksisterande, ugyldige `--validate`-flagget** i
   `ekstern-bruk.md` sitt "Lokal utvikling"-avsnitt: `gen-linkml --validate
   <schema>` → `gen-linkml <schema>`.
3. **Legg til ein prerequisite-sjekk** i "Lokal utvikling"-avsnittet i
   `ekstern-bruk.md`, plassert **før** dei eksisterande `podman run`-
   eksempla (sidan dei krev at Podman rootless/subuid-subgid er korrekt
   konfigurert for å fungere i det heile). Bruk
   `curl -sSL .../check-prereqs.bash | bash`-mønsteret frå funn C, i same
   stil som "Bootstrap"-avsnittet lenger oppe på sida (kort forklarande
   setning + kodeblokk).
4. **Juster resten av "Lokal utvikling"-eksempla til å samsvare stilistisk
   med `ny-domenemodell.md`** (funn A, no retta): behald dei to
   eksisterande `podman run`-eksempla (valider, generer JSON Schema — med
   retta `gen-linkml`-kall frå steg 2), og legg til eit tredje eksempel for
   `linkml lint <schema>` (utan `--validate`-flagg, sjå funn B) slik at
   "Lokal utvikling" dekkjer **både** strukturvalidering (`gen-linkml`) og
   stilsjekk (`linkml lint`) — same to steg som `ny-domenemodell.md` sitt
   steg 3 dekkjer internt via `make lint`/`make mcp-linkml-valider-modell`,
   berre uttrykt som rå `podman run`-kall sidan eksterne repo ikkje har
   tilgang til dette repoet sin Makefile eller MCP-validator-serveren.
   Policy-validering (`mcp-linkml-valider-modell`) kan **ikkje** tilbydast
   identisk eksternt (krev MCP-serveren, som ikkje er publisert som eige
   standalone-image i dag) — nemn dette eksplisitt som ei kjend avgrensing
   i staden for å late som om det er dekt.
5. Verifiser at alle kodeblokker i begge filene refererer til **verkelege**
   make-target/CLI-flagg (kryssjekk mot `COMMANDS.md` og `make/*.mk`,
   same metode som brukt i denne evalueringa) — ikkje berre dei to alt
   kjende bugane over, men resten av sida òg, sidan same type feil kan
   finnast fleire stader.
6. Oppdater specen med `## Utført` og flytt til `specs/done/`.

## Akseptansekriterium

- `ny-domenemodell.md` steg 0 refererer berre til make-target som faktisk
  finst i `make/*.mk`.
- `ekstern-bruk.md` sitt "Lokal utvikling"-avsnitt har ein tydeleg,
  curl-bar prerequisite-sjekk før dei podman-baserte eksempla.
- Ingen `--validate`-flagg attgåande på `gen-linkml` nokon stad i
  dokumentasjonen.
- "Lokal utvikling" dekkjer strukturvalidering + lint, med eksplisitt
  merknad om at policy-validering (MCP) ikkje er tilgjengeleg for eksterne
  repo i dag.
- Alle kommandoar i begge filene er kryssjekka mot faktisk kode
  (`make/*.mk`, `COMMANDS.md`) — ingen påstandar basert på gjetting.

## Handlingsliste

- [x] Steg 1: `ny-domenemodell.md` steg 0 retta til verkelege make-target
- [x] Steg 2: `--validate`-flagget fjerna frå `ekstern-bruk.md`
- [x] Steg 3: prerequisite-sjekk (curl `check-prereqs.bash`) lagt til i
      "Lokal utvikling"
- [x] Steg 4: `linkml lint`-eksempel lagt til, policy-validering-avgrensing
      dokumentert eksplisitt
- [ ] Steg 5: resten av begge sidene kryssjekka mot faktisk kode

## Utført (Steg 1-4 — 2026-08-09)

- **Steg 1:** `ny-domenemodell.md` linje 9-14 retta til
  `make build-docker-linkml && make build-docker-python && make
  build-docker-mcp-validator` (verifisert mot `make/80-images.mk`).
- **Steg 2+3+4:** `ekstern-bruk.md` sitt "Lokal utvikling"-avsnitt
  omstrukturert til nummererte steg (`0 — Sjekk føresetnader`,
  `1 — Valider og generer artefakter`), same stil som
  `ny-domenemodell.md`:
  - Ny `### 0`: curl-bar `check-prereqs.bash`, forklart som fri for
    Makefile-/katalogavhengigheit.
  - `gen-linkml --validate` → `gen-linkml` (utan det ugyldige flagget).
  - Nytt `linkml lint`-eksempel lagt til, med note om at repoet sin eigen
    `.linkmllint.yaml` (`standard_naming` avslått) må hentast eksplisitt
    for identisk åtferd med CI.
  - Ny åtvaringsboks: policy-validering (bronze/silver/gold) krev meir
    enn éin `podman run` — retta undervegs frå ei først feilaktig påstand
    om at `mcp-linkml-validator`-biletet ikkje er offentleg (det **er**
    offentleg, stadfesta via `.github/workflows/reusable-validate.yml`;
    det som manglar er støttefilene `flatten-and-validate.bash`/
    `policies/`, ikkje sjølve biletet).
  - Kryssreferanse til `ny-domenemodell.md#3-valider-undervegs` — slug
    verifisert direkte med `markdown.extensions.toc.slugify()` (Python),
    ikkje gjetta (fyrste forsøk hadde ein feilaktig dobbel bindestrek).

**Ikkje gjort (utanfor denne økta sitt scope, ikkje bede om):** Steg 5
(fullstendig kryssjekk av resten av begge sider mot faktisk kode) og
flytting til `specs/done/` — brukaren bad eksplisitt berre om steg 1-4.

## Relaterte filer

- `mkdocs/docs/arkitektur/ekstern-bruk.md` — hovudmål
- `mkdocs/docs/kom-i-gang/ny-domenemodell.md` — referansemønster, treng eiga retting (funn A)
- `src/assets/scripts/makefile/check-prereqs.bash` — prerequisite-scriptet som skal dokumenterast curl-bart
- `bootstrap.sh` — eksisterande curl-mønster å følgje for prerequisite-sjekken
- `bugs/lint-validate-flag-deprecated.md` — kjelde for funn B
- `make/80-images.mk`, `COMMANDS.md` § "Container-image-bygging" — fasit for korrekte make-target-namn
