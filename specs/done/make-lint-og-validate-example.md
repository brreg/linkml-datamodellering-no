# Nye make-mål: `lint` og `validate-instance`

## Bakgrunn

`./tests/lint_schema.bash` og `./tests/validate_schema.bash` er nyttige enkeltsjekkar
under utvikling, men krev at brukaren kallar bash-skriptet direkte med full stiargument.
Alle andre enkeltsjekkar i repoet (`make test SCHEMA=...`, `make mcp-validate SCHEMA=...`)
vert kalla via `make`.

I tillegg brukar bash-skriptane `docker.io/linkml/linkml:latest` (public image), medan
resten av Makefile brukar `localhost/linkml-local:latest` via `LINKML_RUN`. Skriptane er
dermed inkonsistente med det etablerte mønsteret.

## Mål

Erstatt bash-skriptane med to nye make-mål som inline kommandoane direkte og brukar
`LINKML_RUN`:

| Nytt mål | Erstattar | Parametrar |
|---|---|---|
| `make lint [SCHEMA=<sti>]` | `./tests/lint_schema.bash` | `SCHEMA` — sti til skjemafil (valfri; utan argument lintes alle skjema) |
| `make validate-instance SCHEMA=<sti> INSTANCE=<sti>` | `./tests/validate_schema.bash` | `SCHEMA` — sti til skjemafil, `INSTANCE` — sti til datafil |

`SCHEMA` er same parameternamn som i `make test` og `make mcp-validate`. `INSTANCE` er
konsistent med `INSTANCE=`-parameteren som allereie er i bruk i `make mcp-validate`.

## Implementasjon

### Plassering i Makefile

Legg begge mål inn rett etter `validate:`-målet (linje ~171), i same blokk som
`test` og `validate`. Dei høyrer saman som enkeltskjema-operasjonar.

### `make lint`

Utan `SCHEMA` vert alle skjema i `$(SCHEMAS)` linta. Med `SCHEMA` vert berre det eine skjemaet linta.

```makefile
# Bruk: make lint [SCHEMA=<sti-til-skjema>]
lint:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make lint$(if $(SCHEMA),  SCHEMA=$(SCHEMA),  (alle skjema))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@if [ -n "$(SCHEMA)" ]; then \
		$(LINKML_RUN) linkml lint --validate "$(SCHEMA)"; \
	else \
		$(foreach s,$(SCHEMAS),$(LINKML_RUN) linkml lint --validate "$(s)" &&) true; \
	fi
```

### `make validate-instance`

```makefile
# Bruk: make validate-instance SCHEMA=<sti-til-skjema> INSTANCE=<sti-til-datafil>
validate-instance:
	@test -n "$(SCHEMA)" || (echo "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@test -n "$(INSTANCE)" || (echo "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make validate-instance  SCHEMA=$(SCHEMA)  INSTANCE=$(INSTANCE)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_RUN) linkml validate --schema "$(SCHEMA)" "$(INSTANCE)"
```

### Legg til i `.PHONY`

Begge mål skal leggast til i `.PHONY`-lista (rundt linje 147).

### Slett bash-skriptane

Etter at make-måla er på plass og verifiserte, skal desse filene slettast:

- `tests/lint_schema.bash`
- `tests/validate_schema.bash`

## Oppdatering av COMMANDS.md

Erstatt radene med direktekall til bash-skriptane med dei nye make-måla i valideringstabellen:

| Kommando | Beskriving | Output |
|---|---|---|
| `make lint` | Linter alle skjema i repoet. | OK/FEIL per skjema til stdout; avsluttar med kode 1 ved feil |
| `make lint SCHEMA=<sti>` | Linter eit enkelt skjema raskt utan å køyre generatorar. Nyttig for hurtigsjekk under utvikling. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
| `make validate-instance SCHEMA=<sti> INSTANCE=<sti>` | Validerer ei datafil mot eit skjema utan lint og generatorar. Raskaste enkeltsjekk av datainnhald. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
