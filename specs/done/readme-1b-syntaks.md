# Plan: Likestill syntaks for 1b-punkta i README.md

**Kortnamn:** `readme-1b-syntaks`  
**Dato:** 2026-06-19  

---

## Bakgrunn

`### Datamodellering` og `### Begrepsmodellering` i README.md har begge eit
`1b`-punkt, men dei ser svært forskjellige ut:

**Datamodellering 1b** — kort og lesbar:
```bash
# 1b. (om ønskjeleg) Generer frå eksisterande JSON Schema
# Legg JSON Schema-filen i tmp/, t.d. tmp/modellnavn.json
make mcp-generate SCHEMA=tmp/modellnavn.json
# → genererer tmp/modellnavn-schema.yaml. Flytt ho til src/linkml/domain/modellnavn/
```

**Begrepsmodellering 1b** — lang og vanskeleg å lese:
```bash
# 1b. (om ønskjeleg) Generer utkast til begrep med mcp-linkml-begrep-utkast
echo '{"jsonrpc":"2.0","id":1,...}
{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"opprett_begrep","arguments":{
  "profil": "default",
  ...
}}}' | make mcp-begrep-run
# → lim YAML-output inn i examples/katalognavn-eksempel.yaml
```

Skilnaden er at `mcp-generate` har ein dedikert Make-target som tek éin filsti som
argument (`SCHEMA=`), medan `mcp-begrep-run` krev ein rå JSON-streng via `echo/pipe`.

I tillegg er namngjevinga inkonsistent: `mcp-generate` seier ikkje kva som vert
generert, medan `mcp-begrep-run` seier ikkje kva operasjon som vert utført.

---

## Løysing

To grep samstundes:

1. **Omdøyp** `mcp-generate` → `mcp-model-utkast` (klarare namn — kva MCP-tool og kva operasjon)
2. **Legg til** `mcp-begrep-utkast INPUT=` som ny target (speglar `mcp-model-utkast`-mønsteret)

Brukaren legg argumenta i `tmp/mitt-begrep.json`, og targeten sender fila til
`mcp-begrep-run`. Begge 1b-punkta i README vert då like korte og like namngjevne.

---

## Slik vil dei to 1b-punkta sjå ut (etter)

**Datamodellering 1b:**
```bash
# 1b. (om ønskjeleg) Generer frå eksisterande JSON Schema
# Legg JSON Schema-filen i tmp/, t.d. tmp/modellnavn.json
make mcp-model-utkast SCHEMA=tmp/modellnavn.json
# → genererer tmp/modellnavn-schema.yaml. Flytt ho til src/linkml/domain/modellnavn/
```

**Begrepsmodellering 1b:**
```bash
# 1b. (om ønskjeleg) Generer utkast til begrep
# Legg argumenta i tmp/mitt-begrep.json (sjå ny-begrepsmodell.md for format)
make mcp-begrep-utkast INPUT=tmp/mitt-begrep.json
# → lim YAML-output inn i examples/katalognavn-eksempel.yaml
```

**`tmp/mitt-begrep.json`** (innhald):
```json
{
  "profil": "default",
  "base_uri": "https://begrep.<org>.no",
  "slug": "mitt-begrep",
  "anbefalt_term_nb": "mitt begrep",
  "definisjon_nb": "definisjon av omgrepet",
  "kjelde_relasjon": "self-composed",
  "utgjevar_uri": "https://data.norge.no/organizations/<orgnr>",
  "fagomrade_uri": "https://psi.norge.no/los/tema/<slug>"
}
```

---

## Steg

### S1B1 — Omdøyp `mcp-generate` → `mcp-model-utkast` i Makefile

Omdøyp target-namnet og oppdater `.PHONY`-lista. Legg til `mcp-generate` som
deprecated alias med åtvaringsmelding, slik at eksisterande skript ikkje bryt:

```makefile
mcp-model-utkast:
	...  # same implementasjon som noverande mcp-generate

mcp-generate: mcp-model-utkast
	@echo "Åtvaring: 'make mcp-generate' er omdøypt til 'make mcp-model-utkast'" >&2
```

### S1B2 — Legg til `mcp-begrep-utkast`-target i Makefile

```makefile
# Bruk: make mcp-begrep-utkast INPUT=tmp/mitt-begrep.json
mcp-begrep-utkast:
	@test -n "$(INPUT)" || \
	  (echo "Bruk: make mcp-begrep-utkast INPUT=<sti-til-json>"; exit 1)
	@test -f "$(INPUT)" || \
	  (echo "Feil: $(INPUT) finst ikkje"; exit 1)
	@printf '%s\n%s\n' \
	  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"make","version":"1"}}}' \
	  "$$(python3 -c "import json; args=json.load(open('$(INPUT)')); print(json.dumps({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'opprett_begrep','arguments':args}}))")" \
	  | $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)
```

Legg til `mcp-begrep-utkast` i `.PHONY`-lista.

### S1B3 — Oppdater README.md

- Datamodellering 1b: `mcp-generate` → `mcp-model-utkast`
- Begrepsmodellering 1b: erstatt `echo ... | make mcp-begrep-run` med `make mcp-begrep-utkast INPUT=tmp/mitt-begrep.json`

### S1B4 — Oppdater `ny-domenemodell.md`

Alle referansar til `make mcp-generate` → `make mcp-model-utkast`.

### S1B5 — Oppdater `ny-begrepsmodell.md`

I steg 2 («Generer YAML-instansar»): legg til `make mcp-begrep-utkast INPUT=`
som primær metode, vis `tmp/mitt-begrep.json`-formatet, og behalda
`make mcp-begrep-run` som alternativ for avansert bruk (AI-assistent, skript).

### S1B6 — Oppdater COMMANDS.md (om `mcp-generate` er dokumentert der)

Sjekk om `mcp-generate` er nemnt i `COMMANDS.md` og oppdater til `mcp-model-utkast`.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avheng av |
|---|--------|-----|-----------|
| 1 | ✓ S1B1: Omdøyp `mcp-generate` → `mcp-model-utkast` | `Makefile` | — |
| 2 | ✓ S1B2: Legg til `mcp-begrep-utkast`-target | `Makefile` | — |
| 3 | ✓ S1B3: Oppdater README.md 1b | `README.md` | S1B1, S1B2 |
| 4 | ✓ S1B4: Oppdater `ny-domenemodell.md` og `index.md` | `mkdocs/docs/ny-domenemodell.md`, `index.md` | S1B1 |
| 5 | ✓ S1B5: Oppdater `ny-begrepsmodell.md` steg 2 | `mkdocs/docs/ny-begrepsmodell.md` | S1B2 |
| 6 | ✓ S1B6: Sjekk og oppdater `COMMANDS.md` | `COMMANDS.md` | S1B1 |

---

## Utført

- **S1B1** ✓ — `mcp-generate` omdøypt til `mcp-model-utkast` i Makefile; deprecated alias `mcp-generate` lagd med åtvaringsmelding; `linkml-gen-generate` oppdatert til å avhenge av `mcp-model-utkast`
- **S1B2** ✓ — `mcp-begrep-utkast INPUT=<sti>` lagt til i Makefile; les argumenta frå JSON-fil og sender til `mcp-begrep-run`; lagt til `.PHONY`
- **S1B3** ✓ — README.md: Datamodellering 1b oppdatert til `mcp-model-utkast`; Begrepsmodellering 1b erstatta lang echo/pipe med `make mcp-begrep-utkast INPUT=tmp/mitt-begrep.json` + JSON-format-eksempel
- **S1B4** ✓ — `ny-domenemodell.md` og `index.md`: alle førekomstar av `make mcp-generate` → `make mcp-model-utkast`
- **S1B5** ✓ — `ny-begrepsmodell.md` steg 2: lagt til JSON-fil-format og `make mcp-begrep-utkast INPUT=tmp/mitt-begrep.json` som primær metode; `make mcp-begrep-run` flytta til «avansert bruk»-seksjonen
- **S1B6** ✓ — `COMMANDS.md`: `mcp-generate` → `mcp-model-utkast` (2 rader); `mcp-begrep-utkast INPUT=<sti>` lagt til i begrep-seksjonen

## Avhengigheiter

- `python3` er tilgjengeleg i Makefile-konteksten (brukt av andre targets)
- `LINKML_BEGREP_RUN` og `LINKML_BEGREP_IMAGE` er allereie definerte variablar i Makefile
- `tmp/`-katalogen er i `.gitignore` (brukt av `mcp-generate`/`mcp-model-utkast` på same måte)
- `mcp-generate`-aliaset sikrar bakoverkompatibilitet for eksisterande skript og docs
