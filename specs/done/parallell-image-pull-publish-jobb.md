# Parallell image-pulling i publish-jobben (generate.yml)

## Bakgrunn

`publish`-jobben i `.github/workflows/generate.yml` pulla dei to imaga han
treng (`mkdocs-local`, `python-pytest`) frå GHCR i to separate, sekvensielle
steg (tidlegare linje 451-466), kvart med eiga manuell
`hashFiles(...)`-utrekning av GHCR-taggen og eige `podman pull` + `podman
tag`. Resten av workflowen (`generate`-jobben, linje 238-243) pullar images
parallelt via den delte composite-actionen
`.github/actions/pull-images` (`pull_image()`-funksjon i bakgrunnen, `wait`
på alle PID-ar), med fallback til lokalt `make <target>`-bygg dersom ein
pull feilar, og hentar GHCR-taggane frå `checkout-source` sin autoritative
`image_tags`-output i staden for å rekne dei ut på nytt.

Sekvensiell pulling i `publish`-jobben var både treigare enn nødvendig og eit
avvik frå det etablerte mønsteret elles i workflowen (og eit brot på
DRY-prinsippet i CLAUDE.md — same `hashFiles()`-formel var duplisert to
stader).

## Steg

1. Erstatt dei to sekvensielle "Last `<image>` frå GHCR"-stega i
   `publish`-jobben med eitt kall til `./.github/actions/pull-images`,
   med `images` sett til ein hardkoda JSON-literal for dei to imaga
   (`mkdocs-local` → `build-docker-mkdocs`, `python-pytest` →
   `build-docker-python`) og `image_tags` sett til
   `needs.checkout-source.outputs.image_tags` (same autoritative kjelde
   som `generate`-jobben alt brukar).
2. Behald eksisterande "Logg inn på GHCR"-steg uendra (krevst før
   `pull-images`-actionen køyrer).
3. Verifiser at `build-docker-mkdocs` (`make/50-docs.mk:19`) og
   `build-docker-python` (`make/80-images.mk:34`) finst som fallback-mål
   dersom GHCR-pull skulle feile.
4. Køyr `actionlint` mot `generate.yml` (CLAUDE.md-krav etter kvar
   CI-workflow-endring).

## Handlingsliste

- [x] `.github/workflows/generate.yml`: `publish`-jobben brukar no
      `./.github/actions/pull-images` parallelt i staden for to sekvensielle
      `podman pull`-steg
- [x] `actionlint` køyrt mot endra fil — ingen `[expression]`-/schemafeil,
      berre `[shellcheck]`-funn i uendra skript andre stader i fila (linje
      201, 363), ikkje relatert til denne endringa

## Utført

- `.github/workflows/generate.yml`: dei to sekvensielle "Last `<image>` frå
  GHCR"-stega i `publish`-jobben (tidlegare linje 451-466) er erstatta med
  eitt kall til `./.github/actions/pull-images`, same composite-action
  `generate`-jobben alt brukar for parallell pulling. Fjerna dupliserte
  `hashFiles()`-utrekningar til fordel for den autoritative
  `needs.checkout-source.outputs.image_tags`-kjelda.
- Verifisert: `build-docker-mkdocs` (`make/50-docs.mk:19`) og
  `build-docker-python` (`make/80-images.mk:34`) finst som fallback-mål.
  `actionlint` køyrt mot fila — ingen blokkerande funn.
