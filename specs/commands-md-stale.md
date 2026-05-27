# Stale referansar i COMMANDS.md

## Funn

### 1. `make new-model` — feil output-sti for eksempelfil

**Linje 27**, Output-kolonna:

```
`src/linkml/<domene>/<namn>/<namn>-schema.yaml`<br>`examples/<domene>/<namn>-eksempel.yaml`
```

`examples/<domene>/<namn>-eksempel.yaml` er den gamle rotkatalogtilvisande stien.
`new-model.sh` legg fila på:

```
src/linkml/<domene>/<namn>/examples/<namn>-eksempel.yaml
```

---

### 2. Domenegenerering — manglar `begrepskatalog` og `modellkatalog`

**Linje 60–65**, tabellen «Per domene (anbefalt)» listar berre:
`ap-no`, `fair`, `fint`, `ngr`, `oreg`, `samt`.

`begrepskatalog` og `modellkatalog` er aktive domene og støttar `make <domene>` på
lik linje med dei andre.

---

### 3. Container-image-tabell — manglar `mcp-begrep-build`

**Linje 15–21**, image-tabellen listar `mcp-mod-build` og `mcp-val-build`, men ikkje:

| Kommando | Image | Bruk |
|---|---|---|
| `make mcp-begrep-build` | `mcp-linkml-begrep-utkast` | Begrepsinstans-generator MCP-server |

Kommandoen finst i Makefile (linje 752) og er med i `make check-prereqs`-kjeden i README.

---

### 4. Manglande seksjon for `mcp-linkml-begrep-utkast`

Det finst ein full seksjon for `mcp-linkml-modell-utkast` (linje 95–104), men ingen
tilsvarende for `mcp-linkml-begrep-utkast`. Tilgjengelege kommandoar:

| Kommando | Beskriving |
|---|---|
| `make mcp-begrep-build` | Bygg container-image |
| `make mcp-begrep-run` | Start server interaktivt (stdin/stdout) |
| `make mcp-begrep-smoke` | Røyktest med eksempel-meldingar |
| `make mcp-begrep-list-profiles` | List tilgjengelege organisasjonsprofiler |

---

## Prioritert tiltaksliste

| # | Linje | Endring | Prioritet |
|---|---|---|---|
| 1 | 27 | Rett `examples/<domene>/...` → `src/linkml/<domene>/<namn>/examples/...` | Høg |
| 2 | 60–65 | Legg til `begrepskatalog` og `modellkatalog` i domenetabellen | Høg |
| 3 | 15–21 | Legg til `mcp-begrep-build` i container-image-tabellen | Medium |
| 4 | etter linje 114 | Legg til seksjon for `mcp-linkml-begrep-utkast` | Medium |
