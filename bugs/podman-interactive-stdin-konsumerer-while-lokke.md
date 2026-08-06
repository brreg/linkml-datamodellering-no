# Bug: `podman run -i` (PYTHON_RUN) konsumerer stdin frå omsluttande while-løkke

**ID:** BUG-10
**Status:** `delvis retta` (validate-examples retta, validate-data framleis råka)
**Komponent:** `make/01-containers.mk`, `make/40-validation.mk`
**Oppdaga:** 2026-08-06

## Symptom

Makefile-targets som køyrer `$(PYTHON_RUN)` (definert som `podman run -i --rm ...`
i `make/01-containers.mk:41`) inne i ei `while IFS= read -r x; do ... done < <(...)`-løkke
prosesserer berre **det første elementet** i løkka, deretter avsluttar løkka stille
— utan feilmelding, utan logglinje, utan ikkje-null exit code.

Verifisert på uendra `main`: `make validate-examples DOMAIN=fint` validerer kun
`fint-administrasjon` sjølv om domenet har 6 skjema med eksempelfiler
(`fint-arkiv`, `fint-okonomi`, `fint-personvern`, `fint-ressurs`, `fint-utdanning`
vert aldri validerte).

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

## Berørte targets

| Target | Fil | Status |
|---|---|---|
| `validate-examples` | `make/40-validation.mk` | **Retta** — `$(PYTHON_RUN)`-kallet har no `< /dev/null` |
| `validate-data` | `make/40-validation.mk` | **Ikkje retta** — same mønster, same feil, framleis open |

## Workaround / fiks

Legg til `< /dev/null` på `$(PYTHON_RUN)`-kallet inne i løkka, slik at podman
sin stdin peikar til `/dev/null` i staden for å arve løkka sin fd 0.
`save-validation-log.py` treng ikkje stdin-input, så dette er trygt:

```bash
$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
	--schema "$$schema" --type examples --result "$$result_json" < /dev/null 2>/dev/null || true; \
```

## Løysing

Anten:
1. Fjern `-i`-flagget frå `PYTHON_RUN` (verifiser at ingen andre bruksstader
   av `$(PYTHON_RUN)` faktisk treng interaktiv stdin), eller
2. Legg til `< /dev/null` på kvart `$(PYTHON_RUN)`-kall som køyrer inne i ei
   `while read`-løkke — inkludert `validate-data` (`make/40-validation.mk`,
   `save-validation-log.py --type data-$$catalog`-kallet).

Når `validate-data` er retta, oppdater denne fila til `Status: løyst` og
fjern raden frå "Berørte targets"-tabellen.
