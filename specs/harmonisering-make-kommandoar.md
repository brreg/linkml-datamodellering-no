# Harmonisering av make-kommandoar for MCP-servarar

## Problem

To ulike prefiks-skjema for to servarar som er strukturelt identiske:

| Server | Prefiks | Eksempel |
|---|---|---|
| mcp-linkml-validator | `mcp-` | `mcp-build`, `mcp-smoke`, `mcp-test-policies` |
| mcp-linkml-generator | `linkml-gen-` | `linkml-gen-build`, `linkml-gen-smoke`, `linkml-gen-test-converter` |

`mcp-` aleine er tvetydig no som det finst to MCP-servarar. Test-target har heller ikkje konsistent namn (`mcp-test-policies` vs `linkml-gen-test-converter`).

## Forslag: `mcp-val-*` og `mcp-gen-*`

Begge servarar bruker `mcp-`-prefikset (begge er MCP-servarar), med ein kortform for å identifisere kva server (`val`/`gen`). Brukarvendte kommandoar — dei som tar `SCHEMA=`-argument — beheld enkelt verb utan servar-infiks.

### Server-administrasjon

| Handling | Validator (no) | Validator (forslag) | Generator (no) | Generator (forslag) |
|---|---|---|---|---|
| Bygg image | `mcp-build` | `mcp-val-build` | `linkml-gen-build` | `mcp-gen-build` |
| Start interaktivt | `mcp-run` | `mcp-val-run` | `linkml-gen-run` | `mcp-gen-run` |
| Røyktest | `mcp-smoke` | `mcp-val-smoke` | `linkml-gen-smoke` | `mcp-gen-smoke` |
| Einingstestar | `mcp-test-policies` | `mcp-val-test` | `linkml-gen-test-converter` | `mcp-gen-test` |

`mcp-test` (validator) er dead code (heile kroppen er kommentert ut) og kan slettast.

### Brukarvendte kommandoar

| No | Forslag | Endring |
|---|---|---|
| `mcp-validate SCHEMA=… POLICY=…` | `mcp-validate` | Ingen — beheld kortnamnet |
| `linkml-gen-generate SCHEMA=…` | `mcp-generate SCHEMA=…` | Kortare, paralell til `mcp-validate` |

`mcp-validate` er allereie dokumentert i README og COMMANDS.md — ingen endring der.
`mcp-generate` er kortare og signaliserer at dette er eit brukargrensesnitt, ikkje server-administrasjon.

### Samanfatning

```
mcp-val-build    mcp-gen-build    ← bygg image
mcp-val-run      mcp-gen-run      ← start interaktivt
mcp-val-smoke    mcp-gen-smoke    ← røyktest
mcp-val-test     mcp-gen-test     ← einingstestar

mcp-validate     mcp-generate     ← brukargrensesnitt (SCHEMA=, POLICY=)
```

## Omfang av endringar

Berre Makefile og COMMANDS.md. Ingen endringar i skript, Dockerfilar, testar eller server-kode.

Alle gamle target-namn bør behaldast som alias (`old-name: new-name`) i minst éin syklusar for å unngå å bryta skript som bruker dei.
