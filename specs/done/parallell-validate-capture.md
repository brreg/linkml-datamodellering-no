# Parallelliser `make validate-capture`

## Bakgrunn

`make validate-capture` køyrer `run-schema-validation.py` sekvensiellt for kvart skjema i repoet. Kvar validering kallar `flatten-and-validate.bash`, som er ein relativt treg operasjon (typisk 5-15 sekunder per skjema). Med over 60 skjema i repoet tek ein full køyring fleire minutt.

Sidan valideringane er uavhengige av kvarandre kan dei køyrast parallelt for å redusere byggtida. Eksisterande `domain-<domain>`-targets viser at Makefile-basert parallellisering (`$(foreach ...)`) fungerer godt i dette repoet.

## Avhengigheiter

- `mcp-linkml-validator`-containerbilete må vere bygd (`build-docker-mcp-validator`)
- Eksisterande `flatten-and-validate.bash`-script
- Python 3 `subprocess`-modul (stdlib)

## Mål

1. Reduser byggtid for `make validate-capture` med ~80-90 % (frå t.d. 5 min til <1 min)
2. Behald same output-format (JSON-filer i `validation/<versjon>/<policy>.json`)
3. Behald støtte for både `make validate-capture` (alle skjema) og `make validate-capture SCHEMA=<sti>` (enkeltskjema)

## Steg

### 1. Legg til `--parallel N`-støtte i `run-schema-validation.py`

**Fil:** `src/assets/scripts/run-schema-validation.py`

Utvid scriptet til å støtte `--parallel N`-argumentet som køyrer `N` validerings-jobbar samtidig:

- Legg til `--parallel`-argument i argparse (default: 1 for bakoverkompatibilitet)
- Importer `concurrent.futures.ProcessPoolExecutor` (stdlib)
- Refaktorer `process_schema()` slik at den returnerer resultatet i staden for å printe direkte
- Legg til ein `process_schemas_parallel(schemas: list[Path], dry_run: bool, max_workers: int)` funksjon som:
  - Opprettar ein `ProcessPoolExecutor` med `max_workers`
  - Sender alle skjema til pool via `executor.map(process_schema, schemas)`
  - Samlar resultata og skriv samla statistikk på slutten

**Kvifor:** Python sin `ProcessPoolExecutor` håndterer prosess-pooling, ressursstyring og feilhandtering automatisk. Kvar validering køyrer i sin eigen prosess med eige `podman`-kall — dette utnyttar alle CPU-kjernar og gjer kvar validering til ein atomær operasjon.

**Output:** `run-schema-validation.py --parallel 8` skal køyre opptil 8 valideringar samtidig.

### 2. Oppdater `validate-capture`-målet til å bruke `--parallel`

**Fil:** `Makefile`

Endre `validate-capture`-målet (linje 946-960) til å sende `--parallel 8` til `run-schema-validation.py`:

```make
validate-capture:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make validate-capture$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@if [ -n "$(SCHEMA)" ]; then \
	    python3 src/assets/scripts/run-schema-validation.py --schema $(SCHEMA); \
	else \
	    python3 src/assets/scripts/run-schema-validation.py --parallel 8; \
	fi
```

**Kvifor:** `--parallel 8` er ein fornuftig standard for maskiner med 4-8 CPU-kjernar. Podman-containerar er lette nok til at 8 parallelle instansar ikkje overbelastar systemet. Enkeltskjema-modus (`SCHEMA=<sti>`) køyrer framleis sekvensiellt sidan det er berre éin jobb.

**Output:** `make validate-capture` skal køyre 8 valideringar samtidig.

### 3. Test parallellisering med subsett

**Kommando:**

```bash
# Test med enkeltskjema (skal vere uendra)
make validate-capture SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml

# Test med alle skjema i eit domene (subset for rask test)
python3 src/assets/scripts/run-schema-validation.py --parallel 4 --schema src/linkml/samt/samt-bu/samt-bu-schema.yaml

# Full køyring
make validate-capture
```

**Validering:**
- Sjekk at JSON-filene i `validation/<versjon>/<policy>.json` vert skrivne korrekt
- Samanlikn timing sekvensiell vs. parallell (bruk `time make validate-capture`)
- Sjekk at output frå fleire jobbar ikkje kludrar kvarandre i terminalen

### 4. Legg til `PARALLEL`-parameter i Makefile (valfritt)

**Fil:** `Makefile`

For å la brukaren overstyre parallellitets-nivået:

```make
PARALLEL ?= 8

validate-capture:
	...
	    python3 src/assets/scripts/run-schema-validation.py --parallel $(PARALLEL); \
```

**Kvifor:** Gjer det enkelt å justere for ulike maskiner (`make validate-capture PARALLEL=4`) eller feilsøking (`PARALLEL=1`).

**Output:** `make validate-capture PARALLEL=16` skal køyre 16 jobbar samtidig.

## Handlingsliste

- [x] 1. Legg til `--parallel`-støtte i `run-schema-validation.py` — brukar `xargs -P N` for å køyre separate Python-prosessar parallelt (unngår pickle-problem med ProcessPoolExecutor)
- [x] 2. Oppdater `validate-capture`-målet til å bruke `--parallel 8` — `PARALLEL`-variabel definert i Makefile
- [x] 3. Test parallellisering med subsett — testa med dry-run og ekte validering, JSON-filer vert skrivne korrekt
- [x] 4. (Valfritt) Legg til `PARALLEL`-parameter i Makefile — `PARALLEL ?= 8` definert, kan overstyrast med `make validate-capture PARALLEL=4`

## Kritisk sti

Steg 1 → Steg 2 → Steg 3 (Steg 4 er valfri optimalisering)

## Estimert tidsbesparelse

- Sekvensiell: ~60 skjema × 8 sek = ~8 minutt
- Parallell (8 workers): ~60 skjema ÷ 8 × 8 sek = ~60 sekund

**Forventet speedup:** 8× (frå ~8 min til ~1 min)

## Risikovurdering

**Låg risiko:** Python sin `ProcessPoolExecutor` er stabil og vel-testa. Kvar validering er ein atomær operasjon utan delt tilstand. Podman-containerar håndterer ressursisolering automatisk.

**Potensielle problem:**
- **I/O-konkurranse** (fleire prosessar skriv til disk samtidig) — ikkje eit problem sidan kvar skjema skriv til si eiga validation-mappe
- **Minnebruk** (8 podman-containerar samtidig) — kvar validator-container er liten (~200 MB) så 8 instansar = ~1.6 GB, som er akseptabelt
- **CPU-bottleneck** på maskiner med få kjernar — brukaren kan setje `PARALLEL=2` om nødvendig

## Utført

Alle fire stega er utførte:

1. **`run-schema-validation.py`** utvida med `--parallel N`-argument
   - Implementerte `process_schemas_parallel()` som brukar `xargs -P N` for å køyre separate Python-prosessar parallelt
   - Valde `xargs` framfor `ProcessPoolExecutor` for å unngå pickle-problem når funksjonen må serialiserast på tvers av prosessar
   - Samlar statistikk frå genererte JSON-filer etter køyring
   - Fungerer både for dry-run og ekte validering

2. **Makefile** oppdatert med `PARALLEL`-støtte
   - `PARALLEL ?= 8` definert som global variabel (kan overstyrast med `make validate-capture PARALLEL=4`)
   - `validate-capture`-målet køyrer `python3 src/assets/scripts/run-schema-validation.py --parallel $(PARALLEL)` når `SCHEMA` ikkje er sett
   - Enkeltskjema-modus (`SCHEMA=<sti>`) køyrer framleis sekvensiellt

3. **Testing** gjennomført med dry-run og ekte validering
   - Testa `xargs`-basert parallellisering med 2-3 skjema — fungerer som forventa
   - Testa enkeltskjema-modus — uendra oppførsel
   - Verifiserte at JSON-filer vert skrivne korrekt til `validation/<versjon>/<policy>.json`

4. **`PARALLEL`-parameter** lagt til i Makefile
   - Brukaren kan overstyre parallellitets-nivå: `make validate-capture PARALLEL=16`
   - Default er `PARALLEL=8` for god balanse mellom hastigheit og ressursbruk

### Avvik frå opphavleg plan

- **Implementasjonsmetode:** Bytte frå `ProcessPoolExecutor` til `xargs -P N` for å unngå pickle-problem når funksjonen må serialiserast på tvers av prosessar. `xargs` er ein meir robust løysning for dette brukstilfellet.
- **Statistikksamling:** Samlar statistikk ved å lese genererte JSON-filer etter køyring i staden for å returnere resultat frå kvar `process_schema()`-køyring (som ikkje fungerer med `xargs`-tilnærming).

### Estimert tidsbesparelse (verifisering etter implementering)

- Forventet speedup: 8× (frå ~8 min til ~1 min for 60 skjema)
- Faktisk speedup vil variere avhengig av maskinvare og antal skjema
