# Evaluer behov for ny container med hjelpeverktøy (yq, jq, m.fl.)

## Bakgrunn

`specs/backlog/TODO.md` (linje 100) bad om ei evaluering av om repoet burde
ha ein ny, dedikert Docker/podman-container for hjelpeverktøy som `yq`,
`jq` og andre nyttige bibliotek som manglar i dei eksisterande
containerbileta.

Repoet har i dag sju containerbilete, alle med eitt klart avgrensa formål
(`src/assets/containers/images.json`):

| Image | Formål |
|---|---|
| `linkml-local` | LinkML-generering/validering |
| `python-pytest` | Python-testsuite |
| `avrotize-local` | XSD-generering |
| `asyncapi-cli-minimal` | AsyncAPI-validering |
| `plantuml` | Diagramgenerering |
| `mkdocs-local` | Dokumentasjonsportal |
| `mcp-linkml-validator` (+ modell-utkast, begrep-utkast) | MCP-serverar |

## Steg

1. Kartlegg all faktisk bruk av `yq` og `jq` i repoet (make-targets, script,
   CI-workflows, spesifikasjonar).
2. Vurder om bruken skjer lokalt (via podman, i tråd med "alt skal køyrast
   som containerar") eller i CI (GitHub-hosta runnarar).
3. Sjå etter presedens i tidlegare spesifikasjonar for korleis repoet har
   handtert same spørsmål før.
4. Konkluder og dokumenter tilrådinga.

## Funn

**`jq`** finst utelukkande i `.github/workflows/*.yml` (10 filer/steg) og
brukast av `gh`/GitHub Actions-steg til å parse JSON-output frå
`release-please`, image-manifest osv. Desse steg køyrer på GitHub-hosta
`ubuntu-latest`-runnarar, der `jq` er forhandsinstallert av GitHub — dei går
**ikkje** via podman-containerane i `make/01-containers.mk`. Ingen
`make/*.mk`-target eller lokalt script kallar `jq`.

**`yq`** vart historisk brukt til å lese/skrive verdiar i schema-YAML, men
repoet har **aktivt migrert vekk frå `yq` til Python** fleire stader,
eksplisitt grunngjeve med å unngå ekstra avhengigheit:

- `specs/done/auto-detect-validation-policy.md`: "Alternativ: bruk Python i
  staden for yq for å unngå ekstra avhengigheit" — vedtatt løysing brukar
  `python3 -c "import yaml; ..."`, som "allereie [er] tilgjengeleg i alle
  miljø der Makefile køyrer."
- `specs/done/validering-logging-publish.md`: "Les `validation_policy` frå
  `manifest.yaml` med Python (i staden for yq)".
- `src/assets/scripts/makefile/run-validation.sh`: to kommentarar som
  eksplisitt vel Python over `yq` for tilsvarande oppslag.

Den einaste attverande `yq`-bruken er i `.github/workflows/release-please.yml`,
der binæren lastast ned direkte til CI-runnaren (`sudo wget ...
/usr/local/bin/yq`) for eit enkelt release-steg — igjen på ein GitHub-hosta
runnar, ikkje via eit repo-podman-image.

**Konklusjon: ingen lokalt make-target treng verken `yq` eller `jq` i dag.**
All faktisk bruk er anten (a) CI-only på runnarar som allereie har verktøyet,
eller (b) medvite bytta ut med Python, som alt er tilgjengeleg via
`PYTHON_RUN`/`LINKML_RUN`-monteringane i `make/01-containers.mk`.

## Vurdering

Å opprette ein ny, generell "hjelpeverktøy-container" (ei samlepose med
`yq`, `jq` og "andre nyttige bibliotek") går imot fleire etablerte mønster
i repoet:

1. **Éitt formål per image.** Alle sju eksisterande bilete løyser eitt
   konkret behov (LinkML-generering, XSD, AsyncAPI, diagram, dokumentasjon,
   MCP). Ein samlepose-container for "diverse framtidig nyttige verktøy"
   har ikkje eit avgrensa formål og vil vekse ukontrollert over tid —
   nettopp det motsette av mønsteret repoet følgjer i dag.
2. **Container-storleik er ein aktiv designkriterium.** Fleire Dockerfile
   har detaljerte kommentarar om medvitne vegval for å halde
   biletstorleiken nede (`Dockerfile.asyncapi-cli-minimal`: 4,43 GB → 296 MB,
   `Dockerfile.plantuml`: 328 MB → slankare JRE-Alpine, `Dockerfile.avrotize`:
   `--no-deps` for å unngå ~450 MB ubrukte transitive pakkar). Eit nytt
   image utan konkret, verifisert behov bryt med denne linja.
3. **Repoet har alt valt Python over `yq`,** eksplisitt grunngjeve med å
   unngå ekstra avhengigheit — å no leggje til `yq` via ein ny container
   ville reversere eit tidlegare medvite vedtak utan ny grunngjeving.
4. **`jq`-bruken er avgrensa til CI-runnarar** som alt har verktøyet
   førehandsinstallert — containerisering løyser ikkje eit reelt problem
   der, berre legg til vedlikehaldskostnad (nytt image å byggje, pulle,
   patche, halde oppdatert i `images.json`).

**Tilråding: opprett ikkje ein ny container.** Dersom eit konkret,
verifisert lokalt behov for `jq`/`yq`-liknande funksjonalitet oppstår i eit
framtidig make-target:

- **Førsteval:** bruk Python (alt tilgjengeleg via `PYTHON_RUN`/`LINKML_RUN`)
  for YAML/JSON-manipulasjon — same mønster som resten av repoet.
- **Om `jq` konkret trengst** (t.d. for å halde eit shell-script lesbart),
  legg det til i det eksisterande `Dockerfile.python` (`apk add --no-cache
  jq`, ~2 MB) framfor å byggje eit nytt image. Dette held "éitt formål per
  image"-prinsippet (biletet er alt "verktøy for lokale script/testar") utan
  å auke talet på bilete som må pullast/vedlikehaldast.
- **`yq` bør ikkje leggjast til** — repoet har alt eit dokumentert, fungerande
  alternativ (Python) og ei uttrykt grunngjeving for å unngå akkurat denne
  avhengigheita.

Ingen kodeendringar er naudsynte som følgje av denne evalueringa.

## Utført

Evaluering fullført 2026-08-06. Konklusjon: ny hjelpeverktøy-container er
ikkje tilrådd. Ingen `yq`/`jq`-bruk i lokale make-targets vart funne; all
`jq`-bruk er CI-only (GitHub-hosta runnarar med `jq` førehandsinstallert),
og `yq` er alt medvite bytta ut med Python andre stader i repoet. Sjå
"Vurdering" over for full grunngjeving og fallback-anbefaling dersom eit
konkret behov oppstår seinare.
