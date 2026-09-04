---
name: ci-workflows
description: Actionlint-plikta etter endring i GitHub Actions-workflows — kva som blokkerer, korleis køyre via podman. Lastast automatisk ved arbeid med filer under .github/workflows/.
paths:
  - ".github/workflows/**"
---

## Actionlint etter CI-endring

Etter *kvar* endring i `.github/workflows/*.yml` skal `actionlint` køyrast
mot den endra fila før arbeidet vert rekna som ferdig.

GitHub Actions evaluerer `${{ }}`-uttrykk overalt i eit `run:`-steg — også
inni kommentarar — så eit bokstaveleg tomt `${{ }}` eller anna ugyldig
uttrykk får heile workflowen til å feile ved parse-tid, utan at éin einaste
jobb køyrer (synest som ei 0-sekunds "workflow file issue"-feiling i
Actions-historikken).

Køyr via podman, aldri lokal installasjon:

```bash
podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/<fil>.yml
```

**Kva blokkerer:** berre feil av typen `[expression]` (og andre reelle
syntaks-/schemafeil) blokkerer arbeidet. `[shellcheck]`-funn er stilråd og
treng ikkje rettast som del av same endring.
