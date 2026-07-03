# Reorganiser make targets med konsekvent namngjevingsmønster

## Bakgrunn

`make <TAB><TAB>` viser i dag 100+ targets i alfabetisk rekkjefølgje, noko som gjer det vanskeleg å finne relaterte kommandoar. Ulike kategoriar nyttar ulike prefix-konvensjonar (`mcp-`, `docs-`, `gen-`, `domain-`, `schema-`), noko som spreier relaterte targets utover i lista.

Målet er å innføre eit konsekvent namngjevingsmønster som grupperer relaterte targets saman når dei sorteres alfabetisk.

## Foreslått namngjevingsmønster

### Struktur: `<kategori>-<subkategori>-<namn>`

| Kategori | Subkategori | Døme |
|---|---|---|
| `build-docker` | `<containernavn>` | `build-docker-linkml`, `build-docker-mkdocs`, `build-docker-mcp-validator` |
| `mcp` | `<server>-<handling>` | `mcp-validator-build`, `mcp-validator-run`, `mcp-validator-smoke` |
| `gen` | `<format>` | `gen-jsonld`, `gen-shacl`, `gen-python` |
| `validate` | `<type>` | `validate-instance`, `validate-capture`, `validate-bronze` |
| `new` | `<ressurstype>` | `new-model`, `new-org-catalog`, `new-begrepskatalog` |
| `docs` | `<handling>` | `docs-build`, `docs-serve`, `docs-publish` |

### Konkrete endringar

#### 1. Container-bygging: `*-build-docker` → `build-docker-*`

| Gammalt namn | Nytt namn |
|---|---|
| `linkml-build-docker` | `build-docker-linkml` |
| `docs-build-docker` | `build-docker-mkdocs` |
| `python-build-docker` | `build-docker-python` |
| `avrotize-build-docker` | `build-docker-avrotize` |
| `asyncapi-build-docker` | `build-docker-asyncapi` |
| `gource-build` | `build-docker-gource` |
| `mcp-mod-build` | `build-docker-mcp-modell-utkast` |
| `mcp-begrep-build` | `build-docker-mcp-begrep-utkast` |
| `mcp-val-build` | `build-docker-mcp-validator` |

#### 2. MCP-servere: `mcp-<kortnamn>-*` → `mcp-<fullnamn>-*`

| Gammalt namn | Nytt namn |
|---|---|
| `mcp-mod-run` | `mcp-modell-utkast-run` |
| `mcp-mod-smoke` | `mcp-modell-utkast-smoke` |
| `mcp-mod-test` | `mcp-modell-utkast-test` |
| `mcp-begrep-run` | `mcp-begrep-utkast-run` |
| `mcp-begrep-smoke` | `mcp-begrep-utkast-smoke` |
| `mcp-begrep-list-profiles` | `mcp-begrep-utkast-list-profiles` |
| `mcp-val-run` | `mcp-validator-run` |
| `mcp-val-smoke` | `mcp-validator-smoke` |
| `mcp-val-test` | `mcp-validator-test` |

#### 3. Validering: samle under `validate-*`

| Gammalt namn | Nytt namn |
|---|---|
| `mcp-validate` | `validate-policy` |
| `validate-instance` | `validate-instance` (uendra) |
| `validate-capture` | `validate-capture` (uendra) |
| `domain-validate-bronze` | `validate-domain-bronze` |
| `domain-validate-data` | `validate-domain-data` |
| `domain-validate-examples` | `validate-domain-examples` |

#### 4. Dokumentasjon: `docs-` forblir uendra (allereie konsekvent)

Ingen endringar — `docs-build`, `docs-serve`, `docs-build-fast` er allereie konsekvent namngjevne.

#### 5. Ny ressurs: `new-` forblir uendra (allereie konsekvent)

Ingen endringar — `new-model`, `new-org-catalog`, `new-begrepskatalog`.

#### 6. Generering: `gen-*` forblir stort sett uendra

Fjern duplikatar og konsolider:
- `gen-docs` → `gen-html-docs` (for å skilje frå `docs-*`)
- `gen-jsonld` → `gen-jsonld-context` (for konsistens)
- `gen-shacl` → `gen-shacl-shapes` (for konsistens)

#### 7. Andre targets

| Gammalt namn | Nytt namn | Kommentar |
|---|---|---|
| `publish` | `docs-publish` | Flytt til docs-kategorien |
| `check-prereqs` | `check-prereqs` | Uendra |
| `check-published-uris` | `check-published-uris` | Uendra |
| `update-modellkatalog` | `update-modellkatalog` | Uendra |
| `clean` | `clean` | Uendra |
| `all` | `all` | Uendra |

## Steg

1. **Opprett alias for alle endra targets**
   - Legg til `.PHONY`-targets med gamalt namn som peikar til nytt namn
   - Skrive deprecation-warning som skriv "ÅTVARING: `<gammalt>` er forelda, bruk `<nytt>`"

2. **Oppdater alle indre avhengigheiter i Makefile**
   - Søk gjennom Makefile etter referansar til gamle namn i prerekvisisjoner
   - Erstatt med nye namn

3. **Oppdater COMMANDS.md**
   - Erstatt alle referansar til gamle namn med nye namn
   - Omorganiser tabellane etter ny gruppering

4. **Oppdater CLAUDE.md**
   - Oppdater døme i "Valider arbeidet ditt"-seksjonen

5. **Oppdater CONTRIBUTING.md**
   - Oppdater døme i pull request-seksjon

6. **Test alle aliasa**
   - Køyr `make <gammalt-namn>` for kvar alias og verifiser at det fungerer

7. **Oppdater CI-workflows (.github/workflows/)**
   - Søk gjennom alle workflow-filer og erstatt gamle namn med nye

## Prioritert handlingsliste

- [x] Opprett alias for alle endra targets med deprecation-warnings — 19 alias lagt til i eigen seksjon
- [x] Oppdater indre avhengigheiter i Makefile — 4 referansar oppdaterte (new-model, mcp-validate, validate-capture, .PHONY)
- [ ] Oppdater COMMANDS.md
- [ ] Oppdater CLAUDE.md
- [ ] Oppdater CONTRIBUTING.md
- [ ] Test alle aliasa
- [ ] Oppdater CI-workflows

## Avhengigheiter

- Eksisterande Makefile
- COMMANDS.md
- CLAUDE.md
- CONTRIBUTING.md
- `.github/workflows/*.yml`

## Merknader

- **Bakoverkompatibilitet:** Alle gamle namn skal fungere med deprecation-warning i minst to release-syklusar før dei vert fjerna
- **Deprecation-format:**
  ```makefile
  linkml-build-docker:
  	@echo "ÅTVARING: 'linkml-build-docker' er forelda, bruk 'build-docker-linkml'" >&2
  	@$(MAKE) --no-print-directory build-docker-linkml
  ```
- **Prioritet:** Start med dei mest brukte targets (`*-build-docker`, `mcp-validate`, `publish`)
- **Fase ut gamle namn:** Etter to releases (eller 3 månader), fjern aliasa og oppdater dokumentasjonen
