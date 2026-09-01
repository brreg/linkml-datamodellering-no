# Plan: Kommandolinje-visning i `QUICK=true`-overskrifta

## Bakgrunn

Overskrifta lagt til i
[javazone-demo-quick-heading.md](../done/javazone-demo-quick-heading.md)
("1-4. Generer skjema (QUICK)") mangla den farga
`$ make <target> ARG=...`-kommandolinja som alle andre steg viser rett
etter overskrifta (t.d. steg 5: heading -> blank linje -> farga
kommandolinje -> `make` sin eigen `***`-banner). Brukaren ønskjer same
mønster for QUICK-greina, utan å reintrodusere `prompt_enter`-pausen
(QUICK sitt heile føremål er å hoppe over pausar for steg 1-4).

## Steg

1. Legg til, rett etter `print_heading boxes "1-4. Generer skjema
   (QUICK)"`: ei tom linje + `$ ${CLR_STEP}make new-modell${CLR_RST}
   ${CLR_OK}DOMAIN=${DOMAIN}${CLR_RST} ${CLR_OK}NAME=${NAME}${CLR_RST}` —
   ordrett same tekst/fargekonvensjon som den interaktive steg 3-visinga.
2. Verifiser: `bash -n`, live-køyring med `QUICK=true` som stadfestar at
   kommandolinja vert vist mellom overskrifta og `make` sin eigen
   `***`-banner.

## Handlingsliste

| # | Tiltak | Fil |
|---|---|---|
| 1 | Farga `$ make new-modell DOMAIN=... NAME=...`-linje i QUICK-greina | `javazone-demo-script.sh` |
| 2 | Syntakssjekk + live-verifisering | — |

---

## Utført

Gjennomført 2026-09-01: kommandolinja lagt til rett etter overskrifta
(ingen `prompt_enter` lagt til — QUICK er framleis pauselaus for steg
1-4). `bash -n` OK. Live-verifisert med
`QUICK=true DOMAIN=oreg NAME=quicktest5` (`< /dev/null`, timeout 30s) —
output viser heading -> blank linje -> farga kommandolinje ->
`make` sin eigen `***`-banner, i den rekkjefølgja brukaren etterspurde.
Testartefakt rydda opp etterpå. Ingen avvik frå planen.
