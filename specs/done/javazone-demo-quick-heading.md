# Plan: Overskrift for `QUICK=true`-greina

## Bakgrunn

`QUICK=true`-greina (sjå
[javazone-demo-quick-flag.md](../done/javazone-demo-quick-flag.md)) gjekk
rett på `make new-modell` utan nokon overskrift, i motsetnad til alle
andre steg i scriptet som brukar `print_heading boxes "<tittel>"` (same
"boxes"-ramme som resten av demoen). Brukaren ønskjer ei overskrift i
same stil før QUICK-greina startar.

## Steg

1. Legg til `print_heading boxes "1-4. Generer skjema (QUICK)"` som
   fyrste linje i `else`-greina (`QUICK=true`), før dei to
   `${CLR_DBG}`-statuslinjene og `make new-modell`-kallet.
2. Verifiser: `bash -n` syntakssjekk, live-køyring med `QUICK=true` som
   stadfestar at "boxes"-ramma vert vist rett før `make new-modell`.

## Handlingsliste

| # | Tiltak | Fil |
|---|---|---|
| 1 | `print_heading boxes "1-4. Generer skjema (QUICK)"` i QUICK-greina | `javazone-demo-script.sh` |
| 2 | Syntakssjekk + live-verifisering | — |

---

## Utført

Gjennomført 2026-09-01: heading lagt til, `bash -n` OK, live-verifisert
med `QUICK=true DOMAIN=oreg NAME=quicktest4` (`< /dev/null`, timeout 30s)
— "boxes"-ramma med tittelen «1-4. Generer skjema (QUICK)» vert vist rett
før `make new-modell`-kallet, same stil som alle andre steg. Testartefakt
rydda opp etterpå. Ingen avvik frå planen.
