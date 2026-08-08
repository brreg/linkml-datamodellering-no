# Erstatt «artefaktar» med «artefakter»

## Bakgrunn

Brukaren ønskte ordet «artefaktar» erstatta med «artefakter» i heile repoet.
«artefaktar» er den nynorske pluralforma og var brukt korrekt i nynorsk
dokumentasjon (CLAUDE.md, GOVERNANCE.md, specs/, mkdocs/docs/) per
skriftspråk-policyen i CLAUDE.md § Skriftspråk. Avklaring med brukaren stadfesta
at «artefakter» skal brukast **overalt utanom `specs/done/`** — dette betyr i
praksis at ordforma vert endra sjølv i nynorsk-dokumentasjon, ikkje berre i
bokmål-kontekstar (manifest.yaml-kommentarar generert av Python-skript).

`specs/done/` er arkiverte, urørte spesifikasjonar (jf. DRY-unntaket i
CLAUDE.md) og vert difor eksplisitt halde utanfor.

## Steg

1. Finn alle filer med ordgrensesøk `\bartefaktar\b` (og `\bArtefaktar\b`),
   ekskluder `.git/`, `generated/` (byggoutput) og `specs/done/` (arkivert).
2. Erstatt med `artefakter` / `Artefakter` i alle treff.
3. Inkluder kjeldeskripta som *genererer* manifest.yaml-filene
   (`src/assets/scripts/makefile/generate-informasjonsmodell.py`,
   `batch-generate.py`, `batch-generate-instances.py`) slik at neste
   regenerering ikkje reverserer endringa i dei genererte manifest-filene.
4. Verifiser at ingen utilsikta endringar sneik seg inn (t.d. reverter
   README.md-endring som kom frå eit tidlegare make-køyring, ikkje frå denne
   oppgåva).

## Handlingsliste

- [x] Identifiser alle 67 filer med `artefaktar` utanfor `.git/`, `generated/`, `specs/done/`
- [x] Erstatt ordet i alle 67 filer (CLAUDE.md, GOVERNANCE.md, PRINCIPLES.md,
      SCOPE.md, COMMANDS.md, CONTRIBUTING.md, SECURITY.md, BUGS.md,
      mkdocs/docs/**, specs/backlog/**, specs/rejected/**, .github/workflows/**,
      make/**, src/assets/scripts/makefile/**, src/linkml/**/metadata/*-manifest.yaml)
- [x] Verifiser ingen attverande treff utanfor ekskluderte katalogar
- [x] Revertert utilsikta README.md-anker-endring (ikkje del av denne oppgåva)
