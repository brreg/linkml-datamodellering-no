# Bug: `update-modellkatalog.py::load_org_registry()` forventa `---`-frontmatter, men CODEOWNERS.md brukar ```yaml`-fence

**ID:** BUG-16
**Status:** `løyst`
**Komponent:** `src/assets/scripts/makefile/update-modellkatalog.py`
**Oppdaga:** 2026-08-13

## Symptom

`make gen-modelldcat-elements` og `make update-modellkatalog` feila alltid med:

```
FEIL: Ingen organisasjonar funne i CODEOWNERS.md-frontmatter.
```

## Rot-årsak

`CODEOWNERS.md` sitt organisasjonsregister er skrive som ein Markdown-kodeblokk:

```markdown
​```yaml
organizations:
  - alias: brreg
    ...
​```
```

— ikkje som ekte YAML-frontmatter (`---\n...\n---`). Filas eiga dokumentasjon
(linje 82-84) kallar det likevel "YAML-frontmatter", og
`update-modellkatalog.py::load_org_registry()` tok det bokstaveleg:

```python
if not content.startswith("---"):
    return {}
```

Sidan fila startar med ```` ```yaml ````, ikkje `---`, returnerte funksjonen
alltid ein tom dict — feilen var difor **deterministisk**, ikkje
miljøavhengig.

To andre, korrekte parsarar av same fil finst alt i repoet:

- `src/assets/scripts/utils/codeowners.py::load_codeowners()` — den delte,
  kanoniske parsaren (brukt av `collect-concepts.py`, `new-modell.sh`)
- `src/assets/scripts/makefile/generate-modellkatalog.py::load_codeowners()`
  — eigen (duplikat, men korrekt) parsar

Berre `update-modellkatalog.py` sin variant var feil — eit klassisk
DRY-brot der tre parallelle implementasjonar av same parsing hadde drifta
frå kvarandre.

## Løysing

`update-modellkatalog.py::load_org_registry()` delegerer no til den delte
parsaren i `utils/codeowners.py::load_codeowners()` i staden for å
implementere `---`-frontmatter-parsing sjølv. `generate-modellkatalog.py`
sin eigen (korrekte) duplikat er **ikkje** rørt — konsolidering av han er
eit reint DRY-tiltak på fungerande kode og krev eksplisitt brukargodkjenning
(jf. CLAUDE.md), ikkje gjort som del av denne bugfiksen.

Verifisert med `--dry-run` for begge påverka konsumentar
(`gen-modelldcat-elements.py`, `update-modellkatalog.py`) — begge finn no
alle 6 organisasjonane og prosesserer skjema korrekt utan å skrive filer.
