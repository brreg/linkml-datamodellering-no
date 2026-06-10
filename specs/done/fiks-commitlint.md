# Plan: Fiks commitlint-feil (git ikkje funne i container)

## Utført

Utført 2026-06-10. `apk add --no-cache git` lagt til i `sh -c`-kommandoen i `.github/workflows/validate.yml`.

---

## Bakgrunn

`commitlint`-jobben i `validate.yml` feiler med:

```
Error: spawn git ENOENT
syscall: 'spawn git'
spawnargs: [ 'merge-base', 'origin/main', 'HEAD' ]
```

`@commitlint/cli` kallar internt `git merge-base` for å løyse commit-rekkevidda,
sjølv når `--from` og `--to` er eksplisitt oppgitt. `node:22-alpine` har ikkje
`git` installert, og containeren har ikkje nettverkstilgang til å hente det utan
`apk add`.

**Fix:** Legg til `apk add --no-cache git` i starten av `sh -c`-kommandoen.

---

## Steg 1 — Legg til `apk add --no-cache git` i commitlint-kommandoen ✓

**Fil:** `.github/workflows/validate.yml`

```yaml
          podman run --rm \
            -v "$PWD:/repo" -w /repo \
            --entrypoint="" \
            node:22-alpine \
            sh -c "apk add --no-cache git 2>/dev/null && \
              npm install --save-dev @commitlint/cli @commitlint/config-conventional 2>/dev/null && \
              echo 'module.exports={extends:[\"@commitlint/config-conventional\"]}' > commitlint.config.js && \
              npx commitlint --from origin/${{ github.base_ref }} --to HEAD"
```

---

## Prioritert handlingsliste

| # | Steg | Fil | Avhengigheit |
|---|---|---|---|
| 1 | Legg til `apk add --no-cache git` | `.github/workflows/validate.yml` | — |

---

## Avhengigheiter

Ingen.
