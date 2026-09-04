---
name: codeowners-format
description: CODEOWNERS.md sitt organisasjonsregister er ein ```yaml-fence, ikkje ekte YAML-frontmatter — BUG-16-fella og kva parsar nytt script skal bruke. Lastast automatisk ved arbeid med CODEOWNERS.md.
paths:
  - "CODEOWNERS.md"
---

## Ikkje ekte frontmatter

`CODEOWNERS.md` sitt organisasjonsregister (`organizations:`-lista, brukt av
`new-modellkatalog`, `gen-modelldcat-elements`,
`validate-modellkatalog-instance` m.fl.) er skrive som ein Markdown-kodeblokk:

````markdown
```yaml
organizations:
  - alias: brreg
    ...
```
````

— **ikkje** som ekte YAML-frontmatter (`---\n...\n---`), sjølv om fila sin
eigen dokumentasjon kallar det "YAML-frontmatter". Eit script som testar
`content.startswith("---")` for å oppdage registeret vil **alltid** feile
stille (tom dict, ingen feilmelding) — dette skjedde reelt i
`update-modellkatalog.py::load_org_registry()`, sjå
`bugs/codeowners-frontmatter-format-mismatch.md` (BUG-16).

## Bruk den delte parsaren

Nye script som treng å lese organisasjonsregisteret skal **ikkje**
implementere eiga parsing av fila. Bruk den kanoniske, delte parsaren:

```python
from utils.codeowners import load_codeowners
```

(`src/assets/scripts/utils/codeowners.py`, alt brukt av
`collect-concepts.py` og `new-modell.sh`). `generate-modellkatalog.py` har
ein eigen, korrekt duplikat-parsar — dette er eit kjent, men **ikkje**
konsolidert DRY-avvik (konsolidering krev eksplisitt brukargodkjenning, jf.
CLAUDE.md), ikkje eit mønster å kopiere i nytt kode.
