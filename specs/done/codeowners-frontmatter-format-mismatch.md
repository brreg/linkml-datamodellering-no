# CODEOWNERS.md-mismatch: `load_org_registry()` fann alltid 0 organisasjonar

## Bakgrunn

Etter fiksen i `specs/done/mcp-validator-feilvising-og-relativ-import-bug.md`
vart `make gen-modelldcat-elements DRYRUN=1` køyrd som del av ei fire-
target-verifisering. Han feila med:

```
FEIL: Ingen organisasjonar funne i CODEOWNERS.md-frontmatter.
```

Stadfesta at feilen er **uavhengig** av `SchemaView`-patchen frå forrige
spec — `git diff HEAD -- CODEOWNERS.md` var tom, og feilen oppstår før
skriptet nokon gong når `SchemaView(...)`.

## Rotårsak

`CODEOWNERS.md` sitt organisasjonsregister er ein Markdown-kodeblokk
(```` ```yaml ... ``` ````), ikkje ekte `---`-frontmatter.
`update-modellkatalog.py::load_org_registry()` sjekka
`content.startswith("---")`, som aldri stemmer for denne fila — funksjonen
returnerte difor alltid ein tom dict, deterministisk, uavhengig av miljø.

To andre, korrekte parsarar av same fil finst alt i repoet:
`src/assets/scripts/utils/codeowners.py::load_codeowners()` (delt/kanonisk,
brukt av `collect-concepts.py` og `new-modell.sh`) og
`generate-modellkatalog.py::load_codeowners()` (eigen duplikat, men
korrekt). Berre `update-modellkatalog.py` sin variant hadde drifta frå det
faktiske filformatet — eit DRY-brot (tre parallelle implementasjonar) som
i praksis vart ein funksjonell bug.

Full analyse: `bugs/codeowners-frontmatter-format-mismatch.md` (BUG-16).

## Steg

1. Fiks `update-modellkatalog.py::load_org_registry()` til å delegere til
   `utils/codeowners.py::load_codeowners()` i staden for å implementere
   `---`-frontmatter-parsing sjølv.
2. Verifiser begge konsumentar (`gen-modelldcat-elements.py` via
   exec_module-import, og `update-modellkatalog.py` sjølv) med `--dry-run`
   — ingen filer skal skrivast under verifisering.
3. Dokumenter som BUG-16 i `bugs/` + `BUGS.md`.

**Medvite ikkje gjort:** konsolidering av `generate-modellkatalog.py` sin
eigen (korrekte) duplikat-parsar inn i `utils/codeowners.py`. Han er ikkje
broten, så å endre han ville vore eit reint DRY-tiltak på fungerande kode —
krev eksplisitt brukargodkjenning per CLAUDE.md, ikkje gjort som del av
denne bugfiksen.

## Handlingsliste

- [x] `update-modellkatalog.py::load_org_registry()`: delegér til `utils/codeowners.py::load_codeowners()`
- [x] `bugs/codeowners-frontmatter-format-mismatch.md` (BUG-16) + oppføring i `BUGS.md`
- [x] Verifisert `gen-modelldcat-elements DRYRUN=1` — finn no alle 6 org, 0 filer endra
- [x] Verifisert `update-modellkatalog.py --dry-run` — finn no alle 6 org, oppdaterer/lagar stubs korrekt, 0 filer endra

## Utført

- `src/assets/scripts/makefile/update-modellkatalog.py`: `load_org_registry()` delegerer no til `utils/codeowners.py::load_codeowners()` (fjerna den broken `---`-frontmatter-parsinga)
- `bugs/codeowners-frontmatter-format-mismatch.md` (BUG-16, ny fil)
- `BUGS.md`: lagt til BUG-16-oppføring
- Verifisert end-to-end med `--dry-run` for begge konsumentar — ingen repo-mutasjonar under verifisering
