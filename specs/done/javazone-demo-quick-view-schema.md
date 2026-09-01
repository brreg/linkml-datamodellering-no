# Plan: Vis generert skjema med `less` i `QUICK=true`-greina

## Bakgrunn

`QUICK=true` (sjå [javazone-demo-quick-flag.md](../done/javazone-demo-quick-flag.md))
genererer `$SCHEMA` stille — ingen diff, ingen visning av sluttresultatet
— før scriptet held fram til steg 5 (validering). Brukaren ønskjer at
scriptet, i `QUICK=true`-greina, viser det ferdig-genererte skjemaet med
`less` (same mønster som `run_help`/`run_validate`) rett før steg 5, slik
at presentatøren/brukaren faktisk ser innhaldet før valideringssteget
startar — utan å måtte opne fila i ein separat editor.

`QUICK=false` treng ikkje dette — der ser du innhaldet undervegs via dei
tre diff-visingane i steg 4a-4c.

## Steg

1. **Ny funksjon `run_view_schema`** rett etter `run_validate` (same fil,
   same "(trykk 'q' …)"-mønster): `less -R -F -X "$SCHEMA"`.
2. **I `QUICK=true`-greina**: etter dei tre `insert_before_line`-kalla og
   før avslutningslinja, legg til éin `prompt_enter` (eigen tekst: "Trykk
   Enter for å sjå det genererte skjemaet …") følgt av `run_view_schema`.
   Behald den eksisterande `${CLR_OK}Ferdig — held fram frå steg
   5.${CLR_RST}`-linja rett etter, slik at overgangen til steg 5 framleis
   er tydeleg markert.
3. **Verifiser**: `bash -n` syntakssjekk, deretter ein live-køyring med
   `QUICK=true` (som i `javazone-demo-quick-flag.md` sitt verifiseringssteg)
   som stadfestar at `less` opnar med det ferdig-genererte skjemaet rett
   før "5. Valider skjemaet"-overskrifta.

## Handlingsliste

| # | Tiltak | Fil |
|---|---|---|
| 1 | Ny `run_view_schema`-funksjon | `javazone-demo-script.sh` |
| 2 | `prompt_enter` + `run_view_schema`-kall i `QUICK=true`-greina | `javazone-demo-script.sh` |
| 3 | Syntakssjekk + live-verifisering | — |

---

## Utført

Alle tre steg gjennomførte 2026-09-01:

- **Steg 1**: `run_view_schema()` lagt til rett etter `run_validate()`,
  same `(trykk 'q' …)`-hint + `less -R -F -X`-mønster, denne gongen mot
  `"$SCHEMA"` direkte (ikkje ein pipe frå `make`).
- **Steg 2**: `QUICK=true`-greina utvida med
  `prompt_enter "Trykk Enter for å sjå det genererte skjemaet … "` +
  `run_view_schema` rett etter dei tre `insert_before_line`-kalla, før
  den eksisterande `${CLR_OK}Ferdig — held fram frå steg 5.${CLR_RST}`-linja.
- **Steg 3**: `bash -n` OK. Live-køyring med
  `QUICK=true DOMAIN=oreg NAME=quicktest3` (`< /dev/null`, timeout 60s)
  stadfesta at `less`-hintet og det fullstendige, genererte skjemaet
  (`id:`, `classes:`, alle seks klassane osv.) vert vist rett etter
  generering og rett før "5. Valider skjemaet"-overskrifta. Testartefakt
  (`src/linkml/oreg/quicktest3`, `generated/oreg/quicktest3`) rydda opp
  etterpå.

Ingen avvik frå planen.
