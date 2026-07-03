# mcp-target-navnekonvensjon

## Bakgrunn

Alle make-targets som begynner på `mcp*` skal følgje same namnekonvensjon og vere meir unike ved å begynne på `mcp-linkml*` i staden. Dette gjer namna meir presise og følgjer mønsteret som allereie er etablert for nokre av targeta (t.d. `mcp-linkml-modell-utkast`, `mcp-linkml-begrep-utkast`).

Følgjande targets må endrast:

| Gammalt namn | Nytt namn |
|---|---|
| `mcp-validator-run` | `mcp-linkml-validate-run` |
| `mcp-validator-smoke` | `mcp-linkml-validate-smoke` |
| `mcp-validator-test` | `mcp-linkml-validate-test` |
| `mcp-modell-utkast-run` | `mcp-linkml-modell-utkast-run` |
| `mcp-modell-utkast-smoke` | `mcp-linkml-modell-utkast-smoke` |
| `mcp-modell-utkast-test` | `mcp-linkml-modell-utkast-test` |
| `mcp-begrep-utkast-run` | `mcp-linkml-begrep-utkast-run` |
| `mcp-begrep-utkast-smoke` | `mcp-linkml-begrep-utkast-smoke` |
| `mcp-begrep-utkast-list-profiles` | `mcp-linkml-begrep-utkast-list-profiles` |
| `mcp-validate` | `mcp-linkml-validate` |

Desse targeta er allereie riktig namngjeve og treng inga endring:
- `mcp-linkml-modell-utkast` (linje 836)
- `mcp-linkml-begrep-utkast` (linje 887)

## Avhengigheiter

Ingen eksterne avhengigheiter — berre interne Makefile-endringar.

## Prioritert handlingsliste

1. [✓] **Endre target-definisjonar i Makefile**
   
   Endra alle 10 target-namn i Makefile samt echo-meldingar og bruksrettleiingar i kommentarar.
   - Endre `mcp-validator-run` → `mcp-linkml-validate-run` (linje 780)
   - Endre `mcp-validator-smoke` → `mcp-linkml-validate-smoke` (linje 786)
   - Endre `mcp-validator-test` → `mcp-linkml-validate-test` (linje 792)
   - Endre `mcp-modell-utkast-run` → `mcp-linkml-modell-utkast-run` (linje 811)
   - Endre `mcp-modell-utkast-smoke` → `mcp-linkml-modell-utkast-smoke` (linje 817)
   - Endre `mcp-modell-utkast-test` → `mcp-linkml-modell-utkast-test` (linje 823)
   - Endre `mcp-begrep-utkast-run` → `mcp-linkml-begrep-utkast-run` (linje 873)
   - Endre `mcp-begrep-utkast-smoke` → `mcp-linkml-begrep-utkast-smoke` (linje 879)
   - Endre `mcp-begrep-utkast-list-profiles` → `mcp-linkml-begrep-utkast-list-profiles` (linje 899)
   - Endre `mcp-validate` → `mcp-linkml-validate` (linje 930)

2. [✓] **Oppdater echo-meldingar i Makefile**
   
   Gjorde saman med steg 1 — alle echo-meldingar og bruksrettleiingar i kommentarar vart oppdaterte.

3. [✓] **Oppdater andre filer som refererer til desse targeta**
   
   - Oppdaterte alle `make mcp-validate` til `make mcp-linkml-validate` i mkdocs/docs/, README.md og CONTRIBUTING.md med sed
   - Oppdaterte eksempeloutput i mkdocs/docs/monitorering.md manuelt
   - `.github/workflows/*.yml` — berre `build-docker-mcp-validator` er referert (treng ikkje endring)
   - `tests/*` — ingen referansar til gamle target-namn funne

4. [✓] **Valider at alt framleis fungerer**
   
   - `make mcp-linkml-validate-smoke` — køyrt, fungerer
   - `make mcp-linkml-modell-utkast-smoke` — køyrt, fungerer
   - `make mcp-linkml-begrep-utkast-smoke` — køyrt, fungerer
   - `make mcp-linkml-validate SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` — køyrt, fungerer

## Utført

Alle mcp-*-targets følgjer no same namnekonvensjon med `mcp-linkml-*`-prefiks:

**Nye namn:**
- `mcp-linkml-validate` (tidlegare `mcp-validate`)
- `mcp-linkml-validate-run` (tidlegare `mcp-validator-run`)
- `mcp-linkml-validate-smoke` (tidlegare `mcp-validator-smoke`)
- `mcp-linkml-validate-test` (tidlegare `mcp-validator-test`)
- `mcp-linkml-modell-utkast-run` (tidlegare `mcp-modell-utkast-run`)
- `mcp-linkml-modell-utkast-smoke` (tidlegare `mcp-modell-utkast-smoke`)
- `mcp-linkml-modell-utkast-test` (tidlegare `mcp-modell-utkast-test`)
- `mcp-linkml-begrep-utkast-run` (tidlegare `mcp-begrep-utkast-run`)
- `mcp-linkml-begrep-utkast-smoke` (tidlegare `mcp-begrep-utkast-smoke`)
- `mcp-linkml-begrep-utkast-list-profiles` (tidlegare `mcp-begrep-utkast-list-profiles`)

**Endringar:**
- Makefile: 10 target-definisjonar, echo-meldingar og bruksrettleiingar oppdaterte
- mkdocs/docs/*.md, README.md, CONTRIBUTING.md: Alle `make mcp-validate` erstatta med `make mcp-linkml-validate` (sed + manuell oppdatering av eksempeloutput)
- .github/workflows/*.yml: Ingen endringar nødvendige (berre build-docker-targets er refererte)

**Namnekonvensjonsmønster:**
- Hovudtarget: `mcp-linkml-<funksjon>` (t.d. `mcp-linkml-validate`)
- Hjelpetargets: `mcp-linkml-<funksjon>-<operasjon>` (t.d. `mcp-linkml-validate-smoke`)

Alle smoke-testar og validering fungerer som forventa.

## Why

Dette sikrar konsistent namngjeving på tvers av alle MCP-relaterte make-targets og gjer dei meir grep-venlige og lette å skilje frå andre `mcp*`-kommandoar i systemet.

## How to apply

Gjennomfør stega i rekkjefølgje. Etter kvart steg skal spesifikasjonen oppdaterast med ✓ og ei kort skildring av kva som vart implementert.
