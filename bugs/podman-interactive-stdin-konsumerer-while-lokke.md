# Bug: `podman run -i` (PYTHON_RUN) konsumerer stdin frå omsluttande while-løkke

**ID:** BUG-10
**Status:** `løyst` (alle råka targets retta)
**Komponent:** `make/01-containers.mk`, `make/40-validation.mk`
**Oppdaga:** 2026-08-06

## Symptom

Makefile-targets som køyrer `$(PYTHON_RUN)` (definert som `podman run -i --rm ...`
i `make/01-containers.mk:41`) inne i ei `while IFS= read -r x; do ... done < <(...)`-løkke
(prosess-substitusjon) prosesserer berre **det første elementet** i løkka,
deretter avsluttar løkka stille — utan feilmelding, utan logglinje, utan
ikkje-null exit code.

Verifisert på uendra `main`:
- `make validate-examples DOMAIN=fint` validerte kun `fint-administrasjon`
  sjølv om domenet har 6 skjema med eksempelfiler.
- `make validate-bronze DOMAIN=ap-no` validerte kun **1 av 9** skjema
  (stadfesta empirisk: `git stash` av fiksen → 1 logglinje, fiks attpå →
  9 logglinjer).

## Rot-årsak

`podman run -i` koplar containeren sin stdin til prosessen sin stdin (fd 0).
Når `$(PYTHON_RUN) ... save-validation-log.py` køyrer inne i ei
`while read -r x; do ... done < <(find ...)`-løkke, arvar podman-prosessen
**same fd 0** som `read`-kommandoen les frå (prosess-substitusjonen). Podman
les/konsumerer resten av det som står igjen på den fd-en før det avsluttar,
slik at neste `read -r x`-kall i løkka får EOF og løkka avsluttar — sjølv om
`find`-lista opphavleg hadde fleire linjer.

Dette er ikkje relatert til `tree_root`-forfilteret som vart retta i
`specs/done/valider-eksempelfiler-utan-tree-root.md` — det problemet gjorde
at *ingen* ap-no-skjema nokon gong nådde løkka. Dette problemet gjer at kun
det *første* skjemaet i kvart domene vert validert, uansett domene.

**`validate-data` er ikkje råka**, sjølv om det også kallar `$(PYTHON_RUN)`
inne i ei løkke: targetet brukar `for datadir in $$(find ...); do ... done`
(ordliste frå ferdig-evaluert kommandosubstitusjon), ikkje
`while read < <(...)`. `for`-løkka har ingen avhengigheit til fd 0 mellom
iterasjonar — heile filstien-lista er alt i minnet før løkka startar, så det
finst ingen "neste `read`" som podman kan svelte. Verifisert empirisk med
`make validate-data DOMAIN=modellkatalog` (6 datakatalogar, alle 6 validerte
korrekt på uendra `main`).

## Berørte targets

| Target | Fil | Loop-mønster | Status |
|---|---|---|---|
| `validate-examples` | `make/40-validation.mk` | `while read < <(...)` | **Retta** — `$(PYTHON_RUN)`-kallet har `< /dev/null` |
| `validate-bronze` | `make/40-validation.mk` | `while read < <(...)` | **Retta** — `save-validation-log.py`-kallet har `< /dev/null` (`emit-github-validation-annotations.py`-kallet brukte alt here-string `<<<` og var ikkje råka) |
| `validate-data` | `make/40-validation.mk` | `for x in $$(...)` | **Ikkje råka** — anna loop-mønster, ingen fiks naudsynt |

## Fiks

Legg til `< /dev/null` på `$(PYTHON_RUN)`-kallet inne i `while read`-løkka,
slik at podman sin stdin peikar til `/dev/null` i staden for å arve løkka
sin fd 0. `save-validation-log.py` treng ikkje stdin-input, så dette er trygt:

```bash
$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
	--schema "$$schema" --type examples --result "$$result_json" < /dev/null 2>/dev/null || true; \
```

Eit `$(PYTHON_RUN)`-kall som alt brukar eit here-string (`<<< "$$var"`) som
stdin (som `emit-github-validation-annotations.py` i `validate-bronze`) er
**ikkje** råka — here-stringen overstyrer allereie fd 0 for det kallet.

## Generell regel

Ethvert `podman run -i`-kall (eller anna kommando som koplar til stdin) inne
i ei `while read < <(...)`-løkke i dette repoet må anten omdirigere sin
eigen stdin (`< /dev/null` eller `<<< "$$var"`), eller løkka må byggjast om
til `for x in $$(...)`-mønsteret der det er trygt (ordlista må då tåle å bli
fullt evaluert i minnet før løkka startar — uegna for veldig store lister).
