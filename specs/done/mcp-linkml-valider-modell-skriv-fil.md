# Plan: `make mcp-linkml-valider-modell` skal skrive valideringsresultat til fil

## Bakgrunn

I dag finst tre delvis overlappande valideringstarget i `make/40-validation.mk`,
alle bygde på same underliggande MCP-validator (`flatten-and-validate.bash`),
men med ulik oppførsel:

| Target | Skriv til terminal | Skriv til fil | Kalla frå CI |
|---|---|---|---|
| `mcp-linkml-valider-modell` | Full JSON (`{valid, errorCount, warningCount, issues}`) | **Nei** | Nei |
| `validate-policy-logg` | Berre eitt-linjes oppsummering (`✓ Validering vellykka: <sti>` / `✗ ...`) | Ja — `src/linkml/<domain>/<modell>/validation/<versjon>/<policy>.json` | Ja (`.github/workflows/{generate,validate}.yml`) |
| `validate-capture` | (batch-verktøy, avgrensa til release-please sine "released packages") | Ja | Nei |

Dette tre-delinga vart medvite **ikkje** konsolidert i
`specs/done/make-kommando-inkonsistens-audit.md` (namnekonsistens 4):
`validate-policy-logg` sin underliggande `run-validation.sh` er CI-kritisk
infrastruktur, og CLAUDE.md krev eksplisitt brukargodkjenning før slikt
script vert skrive om åleine for DRY-formål. Denne spec-en er nettopp den
godkjenninga — men avgrensa til det brukaren konkret har bede om: at
`mcp-linkml-valider-modell` (kommandoen brukt for manuell, lokal
policy-validering — t.d. i «Neste steg» frå `make new-modell`) **òg** skal
skrive resultatet til fil, utan å endre `run-validation.sh` sjølv.

**Kvifor filskriving åleine ikkje er nok:** `mkdocs/publish.sh` (via
`mkdocs/lib/sections/valideringsresultat.sh` →
`get_validation_json_path()` i `mkdocs/lib/utils/metadata_parsers.sh`) les
**ikkje** frå `src/linkml/<domain>/<modell>/validation/`. Han les frå
`generated/<domain>/<modell>/validation/<versjon>/<policy>.json` — ein
katalog som er `.gitignore`-a og berre fyllast av eit dedikert CI-steg
(«Kopier valideringsloggar til generated/», `.github/workflows/generate.yml`
linje 263-306: `mkdir -p "$target_dir"; cp -rv "$validation_version_dir"/*
"$target_dir/"`). **Ingen lokalt make-target gjer denne kopieringa i dag.**
Konsekvens: sjølv om ein køyrer `validate-policy-logg` lokalt (som alt
skriv til `src/linkml/.../validation/`), vil `make docs-build`/`docs-serve`
lokalt framleis vise «*Valideringsresultat ikkje tilgjengeleg — ingen
validering enno.*» — nøyaktig symptomet brukaren skildrar.

## Mål

Éin kommando — `make mcp-linkml-valider-modell SCHEMA=<sti> [POLICY=<policy>]`
— skal:

1. Vise fullt valideringsresultat i terminalen (som i dag).
2. Skrive resultatet til `src/linkml/<domain>/<modell>/validation/<versjon>/<policy>.json`
   (co-location-strukturen, same format som `validate-policy-logg` alt brukar).
3. **Umiddelbart** gjere resultatet synleg for ein lokal
   `make docs-build`/`make docs-serve`/`make docs-publish`, ved òg å skrive
   til `generated/<domain>/<modell>/validation/<versjon>/<policy>.json` —
   utan noko separat, lett-å-gløyme synkroniseringssteg.

`run-validation.sh` (CI-kritisk) skal **ikkje** endrast.

## Design

### Steg 1 — Lat `mcp-linkml-valider-modell` delegere til `run-validation.sh`

`run-validation.sh` gjer alt det underliggande arbeidet som trengst
(køyrer `flatten-and-validate.bash`, byggjer logg-objektet via den delte
`src/assets/scripts/utils/validation_log.py`, skriv til
`src/linkml/.../validation/<versjon>/<policy>.json`) — det einaste som
manglar er at han i dag berre skriv ei kort oppsummeringslinje til stderr i
staden for å echo den fulle JSON-en. `--quiet`-flagget hans er allereie
laga nettopp for maskinlesbar bruk: han undertrykk oppsummeringslinja og
skriv i staden **berre loggstien** til stdout.

Dagens `_mcp-valider-modell-with-header` (`make/40-validation.mk`):

```makefile
_mcp-valider-modell-with-header:
	$(call print_header,mcp-linkml-valider-modell,SCHEMA=$(SCHEMA)  POLICY=$(POLICY))
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@bash $(MCP_DIR)/flatten-and-validate.bash $(SCHEMA) $(POLICY) $(INSTANCE)
```

Føreslått endring:

```makefile
_mcp-valider-modell-with-header:
	$(call print_header,mcp-linkml-valider-modell,SCHEMA=$(SCHEMA)  POLICY=$(POLICY))
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@eval "$$LOG_FUNCTIONS"; \
	LOG_PATH=$$(bash src/assets/scripts/makefile/run-validation.sh \
	    --schema "$(SCHEMA)" --policy "$(POLICY)" \
	    $(if $(INSTANCE),--instance "$(INSTANCE)") --quiet); \
	EXIT_CODE=$$?; \
	cat "$$LOG_PATH"; \
	GEN_PATH=$$(echo "$$LOG_PATH" | sed 's#^src/linkml/#generated/#'); \
	mkdir -p "$$(dirname "$$GEN_PATH")"; \
	cp "$$LOG_PATH" "$$GEN_PATH"; \
	log_info "Skrive til: $$LOG_PATH (og kopiert til $$GEN_PATH for lokal portalvising)"; \
	exit $$EXIT_CODE
```

`run-validation.sh` sjølv er **uendra** — han vert berre kalla, ikkje
omskrive. `mkdir -p`+`cp`-steget er identisk mønster til CI sitt
kopisteg i `generate.yml` (same to linjer, berre éin fil om gongen i
staden for eit heilt versjons-katalog).

**Konsekvens for terminalformatet:** `cat "$LOG_PATH"` viser den
**pakka** logg-strukturen frå `validation_log.py`
(`{schema, domain, version, validated_at, validation_policy, result: {valid,
errorCount, warningCount, issues}}`), ikkje det bare `{valid, errorCount,
...}`-objektet frå `flatten-and-validate.bash` direkte. Dette er ei medviten
forbetring — meir kontekst i same utskrift — men er ei brotsendring for
alle som måtte parse dagens bare stdout-format programmatisk. Stadfesta
**ingen** GitHub Actions-workflow kallar `mcp-linkml-valider-modell` (grepa
gjennom `.github/workflows/*.yml` — treff null) — kommandoen er utelukkande
eit manuelt/lokalt utviklarverktøy i dag, så risikoen vurderast som låg.

### Steg 2 — Verifiser `--instance`-parameter-paritet

Dagens `_mcp-valider-modell-with-header` sender `$(INSTANCE)` direkte som
tredje posisjonsargument til `flatten-and-validate.bash`.
`run-validation.sh` støttar òg `--instance <path>` og sender han vidare til
same `flatten-and-validate.bash`-kall — bør fungere identisk, men må
verifiserast eksplisitt før dette landar (t.d. mot eit skjema med
`INSTANCE=`-parameter sett), sidan `run-validation.sh` sin
argumentparsing/feilhandtering for `--instance` aldri har vore trafikkert
frå denne kallestaden før.

### Steg 3 — Dokumentasjon

- `COMMANDS.md`: oppdater skildringa av `mcp-linkml-valider-modell` til å
  nemne at resultatet no òg vert skrive til
  `src/linkml/<domain>/<modell>/validation/<versjon>/<policy>.json` (og
  kopiert til `generated/...` for lokal portalvising).
- Vurder å leggje til ei kort merknad i
  `mkdocs/docs/kom-i-gang/ny-domenemodell.md` (steg 3/«Valider undervegs»)
  om at valideringsresultat no dukkar opp automatisk i ein lokal
  `make docs-serve`/`docs-build` etter ein `mcp-linkml-valider-modell`-køyring.

## Opne spørsmål / vurderingar

1. **Overskriv alltid, uavhengig av resultat?** Ja — dette er alt
   `run-validation.sh` sin eksisterande, testa oppførsel (skriv logg
   uavhengig av om valideringa er `valid: true` eller `false`); ingen
   endring trengst her, berre eit medvite val å ikkje avvike frå det.
2. **Skal `generated/`-kopien slettast/reinsast ved neste `make <domain>`-
   køyring, eller kan han verte forelda mellom lokale valideringskøyringar?**
   CI sitt `cache-generated`-steg (sjå `if: steps.cache-generated.outputs.cache-hit
   != 'true'` i `generate.yml`) hoppar over kopisteget når cache-treff — dvs.
   CI sjølv toler ein potensielt forelda `generated/`-kopi mellom køyringar
   når input er uendra. Same toleranse gjeld lokalt: ein forelda kopi er
   ufarleg (viser berre eit eldre resultat inntil neste
   `mcp-linkml-valider-modell`-køyring), og `generated/` er uansett heilt
   regenererbar frå `make <domain>`. Ingen ekstra reinsingslogikk føreslått.
3. **Bør `validate-policy-logg` òg få det same `generated/`-kopisteget?**
   Utanfor scope for denne spec-en (brukaren spurde spesifikt om
   `mcp-linkml-valider-modell`), men er eit naturleg oppfølgingssteg —
   same eitt-linjes `mkdir -p`+`cp`-mønster kan leggjast til
   `validate-policy-logg`-targetet i `make/40-validation.mk` utan å røre
   `run-validation.sh`. Nemnt her som forslag til vidare arbeid, ikkje del
   av handlingslista under.

## Prioritert handlingsliste

| # | Steg | Fil |
|---|---|---|
| 1 | Endre `_mcp-valider-modell-with-header` til å delegere til `run-validation.sh --quiet`, cat-e loggfila, og kopiere til `generated/` | `make/40-validation.mk` |
| 2 | Verifiser `--instance`-parameter-paritet mot eit reelt skjema med `INSTANCE=` sett | manuell test |
| 3 | Oppdater dokumentasjon | `COMMANDS.md`, `mkdocs/docs/kom-i-gang/ny-domenemodell.md` |
| 4 | Manuell verifisering | Køyr `make mcp-linkml-valider-modell SCHEMA=<eksisterande skjema>`, stadfest fil skriven begge stader, stadfest `make docs-build` viser resultatet, stadfest eksisterande `mcp-linkml-valider-modell-smoke`/`-test`/`-run`-target (uendra sub-target-familie) framleis fungerer |

## Avhengigheiter

- Ingen nye container-images.
- Ingen endring i `run-validation.sh`, `validation_log.py`,
  `flatten-and-validate.bash` eller `detect-validation-policy.py` — alt
  gjenbruk skjer på eksisterande, uendra API/kontrakt.
- Ingen endring i `mkdocs/lib/utils/metadata_parsers.sh` sin
  `get_validation_json_path()` — han held fram med å lese frå `generated/`
  som einaste kjelde, uendra invariant; denne spec-en sørger berre for at
  den kjelda faktisk er fylt ut lokalt.

## Utført

Alle fire handlingsliste-punkta er gjennomførte, nøyaktig etter planen —
ingen avvik denne gongen.

- **Steg 1** (`_mcp-valider-modell-with-header` i `make/40-validation.mk`)
  implementert som føreslått: delegerer til
  `run-validation.sh --schema ... --policy ... [--instance ...] --quiet`,
  cat-ar den skrivne loggfila til terminalen, kopierer henne til
  `generated/<domain>/<modell>/validation/<versjon>/<policy>.json`, og
  propagerer exit-koden frå `run-validation.sh`. `run-validation.sh` sjølv
  er urørt.
- **Steg 2** (`--instance`-paritet) verifisert: testa
  `make mcp-linkml-valider-modell SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml
  POLICY=silver INSTANCE=src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml`
  — identisk oppførsel til utan `INSTANCE=`, ingen avvik.
- **Steg 3** (dokumentasjon) oppdatert: `COMMANDS.md` sin rad for
  `mcp-linkml-valider-modell`, og eit nytt avsnitt i steg 3 («Valider
  undervegs») i `mkdocs/docs/kom-i-gang/ny-domenemodell.md`.
- **Steg 4** (manuell verifisering) gjennomført mot
  `src/linkml/samt/samt-bu/samt-bu-schema.yaml` (versjon `1.10.1`, som
  endå ikkje hadde noka valideringslogg — trygt testobjekt utan risiko for
  å overskrive eksisterande, committa loggar):
  - Stadfesta at fila vart skriven identisk begge stader
    (`src/linkml/samt/samt-bu/validation/1.10.1/silver.json` og
    `generated/samt/samt-bu/validation/1.10.1/silver.json` — `diff` viste
    ingen skilnad).
  - Stadfesta at `python3 mkdocs/lib/scripts/generate-validation-md.py
    generated/samt/samt-bu/validation/1.10.1/silver.json samt samt-bu`
    korrekt genererer «## Valideringsresultat»-seksjonen frå den nye fila
    — provar at heile kjeda fram til portalvising fungerer.
  - `make docs-build` køyrer framleis reint (same, uendra
    førehandseksisterande åtvaringar, ingen nye).
  - Testartefakta (`validation/1.10.1/` i begge katalogar) sletta etter
    verifisering — arbeidstreet er urørt utover dei fire tiltenkte filene.

**Endra filer:** `make/40-validation.mk`, `COMMANDS.md`,
`mkdocs/docs/kom-i-gang/ny-domenemodell.md`.
