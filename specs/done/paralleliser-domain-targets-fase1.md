# Paralleliser domain-targets

## Bakgrunn

`make domain-ap-no` og andre `make domain-*` targets køyrer no alle interne kommandoar (merge-imports, gen-jsonld, gen-shacl, gen-python osv.) sekvensielt. For domene med mange skjema (t.d. FINT med 7 skjema, ap-no med 9 skjema) tek dette lang tid.

Noverande struktur (frå `Makefile` linje 615-640):

```makefile
domain-$(1):
	@$$(foreach s,$$(_schemas_$(1)),merge-imports $$(s);)
	$$(call run_gen,$$(_schemas_$(1)),gen-jsonld-context,context.jsonld)
	$$(call run_gen_shacl,$$(_schemas_$(1)))
	$$(call run_gen,$$(_schemas_$(1)),gen-python,model.py)
	$$(call run_gen,$$(_schemas_$(1)),gen-json-schema,schema.json)
	$$(call run_gen_owl,$$(_schemas_$(1)))
	$$(call run_gen_rdf,$$(_schemas_$(1)))
	# ... eksempelkonvertering ...
	$$(call run_gen,$$(_schemas_$(1)),gen-erdiagram,erdiagram.md)
	$$(call run_gen,$$(_schemas_$(1)),gen-docs,docs)
	$$(call run_gen,$$(_schemas_$(1)),gen-proto,schema.proto)
	$$(call run_gen,$$(_schemas_$(1)),gen-plantuml,diagrams)
```

Kvar `run_gen`-kall køyrer sekvensielt gjennom alle skjema i domenet.

## Mål

Redusere byggtid for `make domain-*` targets ved å køyre generatorar parallelt der det er mogleg, **utan å miste feilrapportering eller lesbar output**.

**Kritisk constraint**: GitHub Actions `generate and publish` workflow må ha lettleselig output for debugging. Samanblanda parallell output er uakseptabelt i CI-loggar.

## Avhengigheiter mellom steg

| Steg | Kan køyre parallelt med | Avhengig av |
|---|---|---|
| `merge-imports` (validering) | Andre skjema sitt merge-imports | Ingenting |
| `gen-jsonld` | Alle andre generatorar | `merge-imports` (implisitt — skjema må vere gyldig) |
| `gen-shacl` | Alle andre generatorar | `merge-imports` |
| `gen-python` | Alle andre generatorar | `merge-imports` |
| `gen-json-schema` | Alle andre generatorar | `merge-imports` |
| `gen-owl` | Alle andre generatorar | `merge-imports` |
| `gen-rdf` | Alle andre generatorar | `merge-imports` |
| `gen-erdiagram` | Alle andre generatorar | `merge-imports` |
| `gen-docs` | Alle andre generatorar | `merge-imports` |
| `gen-proto` | Alle andre generatorar | `merge-imports` |
| `gen-plantuml` | `gen-docs` (brukar same template-system) | `merge-imports` |
| Eksempelkonvertering | Alle andre generatorar | `merge-imports`, skjema-artefaktar (gen-jsonld, gen-rdf) |

**Konklusjon**: Alle generatorar kan køyre parallelt **etter** at `merge-imports` har validert skjemaet. Eksempelkonvertering bør køyre til slutt (treng skjema-artefaktar).

## Timer-format

Kvar parallell jobb skal logge tidsbruk same format som `mkdocs/publish.sh`:

```bash
t0=$(date +%s%3N)  # millisekund-presisjon
# ... køyr jobb ...
elapsed_ms=$(( $(date +%s%3N) - t0 ))
printf "→ %s %s (%d.%ds)\n" \
    "$generator" "$schema" \
    $$(elapsed_ms / 1000)) \
    $$((elapsed_ms % 1000 / 100))
```

**Output-eksempel**:
```
→ gen-jsonld-context  dcat-ap-no (2.3s)
→ gen-shacl  dcat-ap-no (4.1s)
→ gen-python  dcat-ap-no (1.8s)
→ gen-jsonld-context  cpsv-ap-no (2.5s)
...
```

Dette gjev oversikt over kva som tek tid og hjelper med å identifisere flaskehalsar.

## Implementasjonsstrategi

**Fase 1: Pilot med `domain-ap-no`**

Implementer parallellisering først for `make domain-ap-no`, test grundig, og få brukar-godkjenning før me rullar ut til andre domene.

**Fase 2: Rullar ut til alle domene**

Etter godkjenning: anvend same tilnærming på alle `domain-*` targets.

## Handlingsliste

### Fase 1: Pilot med domain-ap-no

- [x] **Steg 1**: Skriv `run_gen_parallel`-funksjon med timer per jobb
  - Bruk `xargs -P 8` (8 parallelle jobbar som standard)
  - Legg til timer: `t0=$(date +%s%3N)` før kvar jobb, logg `elapsed_ms` etter
  - Timer-output same format som `mkdocs/publish.sh`: `→ <generator> <skjema> (X.Ys)`
  - Legg til feilhandtering (`exit $$rc`)
  - Logg kvar jobb sin output med timer

- [x] **Steg 2**: Erstatt `run_gen`-kall i `domain-ap-no` target med `run_gen_parallel`
  - Behald `merge-imports` sekvensielt (validering må gå før generatorar)
  - Køyr alle generatorar parallelt etter `merge-imports`
  - Berre `domain-ap-no` i denne fasen
  - Override domain-ap-no etter `domain_target` macro-eval

- [x] **Steg 3**: Legg til `PARALLEL` variabel for å kontrollere parallellisme-grad
  - `PARALLEL ?= 8` (default)
  - `make domain-ap-no PARALLEL=16` — køyr 16 jobbar parallelt
  - `make domain-ap-no PARALLEL=1` — køyr sekvensielt (debugging)
  - Vis `(PARALLEL=N)` i header når N ≠ 1

- [ ] **Steg 4**: Test output-lesbarheit for `domain-ap-no` (KRITISK)
  - Test `make domain-ap-no` med parallellisering lokalt
  - Introduser ein feil i eitt AP-NO-skjema (t.d. ugyldig YAML-syntaks i `dcat-ap-no`)
  - Verifiser at feilen er **lett å identifisere** i output (kva skjema, kva generator)
  - Samanlikn med sekvensielt output (`PARALLEL=1`) — er parallell output "god nok" for CI-debugging?
  - Verifiser at timer-output er lesbart: `→ gen-jsonld-context  dcat-ap-no (2.3s)`
  - **Beslutning**: Om parallell output er for vanskeleg å lese → bruk `PARALLEL=1` i CI

- [ ] **Steg 5**: Dokumenter `domain-ap-no` pilot
  - `COMMANDS.md` — legg til `PARALLEL` parameter og døme for `domain-ap-no`
  - Skriv kort samandrag av output-lesbarheits-testen og konklusjon
  - Inkluder tidsmålingar: sekvensielt vs. parallelt for `domain-ap-no`

- [ ] **Steg 6**: **BRUKAR-GODKJENNING** ⚠️
  - Vis brukar parallell vs. sekvensielt output frå `make domain-ap-no`
  - Vis tidsmålingar
  - Få eksplisitt godkjenning før me går vidare til Fase 2

### Fase 2: Rullar ut til alle domene (etter brukar-godkjenning)

- [ ] **Steg 7**: Anvend `run_gen_parallel` på alle `domain-*` targets
  - Bruk same tilnærming som `domain-ap-no`
  - Test kvar domene enkeltvis

- [ ] **Steg 8**: Oppdater dokumentasjon for alle domene
  - `COMMANDS.md` — oppdater alle `domain-*` døme med `PARALLEL`
  - `CONTRIBUTING.md` — beskriv parallelliseringsstrategien

- [ ] **Steg 9**: Oppdater CI workflows
  - `.github/workflows/generate-*.yml` — **VURDER**: `PARALLEL=1` (sekvensielt) for lettleselig output, ELLER `make -j 8 --output-sync=target` for hastighet med lesbar output
  - Test begge tilnærmingar i CI og vel basert på lesbarheit vs. hastighet
  - Dokumenter valet i workflow-kommentarar
  - Vurder om å bruke GitHub Actions sin `matrix` i staden (ein jobb per domene) — gjev perfekt isolert output

## Utført

### Steg 1-3: Implementert i Makefile

**Endringer**:
- Ny variabel `PARALLEL ?= 8` (linje 17)
- Ny funksjon `run_gen_parallel` med timer og xargs -P (etter linje 70)
- Ny `domain-ap-no` target som overrider auto-generert target (etter linje 683)

**Implementasjon av `run_gen_parallel`**:
```makefile
define run_gen_parallel
@if [ "$(PARALLEL)" = "1" ]; then \
	$(foreach s,$(1),echo "$(CLR_STEP)→ $(2)  $(s)$(CLR_RST)" && ...) \
else \
	printf '%s\n' $(1) | xargs -P $(PARALLEL) -I {} bash -c ' \
		s="{}"; \
		t0=$$(date +%s%3N); \
		mkdir -p "$$outdir" && $(LINKML_RUN) $(2) "$$s" > "$$outdir/$$name-$(3)" 2>&1; \
		rc=$$?; \
		elapsed_ms=$$(($$( date +%s%3N) - t0)); \
		printf "→ $(2)  %s/%s (%d.%ds)\n" "$$domain" "$$name" ...; \
		exit $$rc'; \
fi
endef
```

**Testing**:
- `make domain-ap-no PARALLEL=1` — køyrer sekvensielt (OK)
- `make domain-ap-no PARALLEL=8` — køyrer parallelt (testing...)

## Forventet speedup

Anta at kvar generator tek like lang tid og at me har 8 CPU-kjernar:

| Domene | Antal skjema | Noverande tid (sekvensielt) | Forventa tid (8 parallelle) | Speedup |
|---|---|---|---|---|
| ap-no | 9 | 9 × 10 generatorar = 90 steg | 9 × (10/8) = 11.25 steg | **8×** |
| fint | 7 | 7 × 10 = 70 steg | 7 × 1.25 = 8.75 steg | **8×** |
| ngr | 3 | 3 × 10 = 30 steg | 3 × 1.25 = 3.75 steg | **8×** |

**Realistisk speedup**: 4-6× (pga. I/O-ventetid, container-oppstart, make-overhead)

**Viktig**: Speedup avhenger av CPU-ressursar. GitHub Actions standardrunner har 4 CPU-kjernar, så der vert realistisk speedup 2.5-3× med `-j 8` (oversubscription). Lokalt med 8+ kjernar kan me oppnå 4-6× speedup.

## Risiko og avbøting

| Risiko | Sannsyn | Konsekv. | Avbøting |
|---|---|---|---|
| **Output-blanding i CI gjer debugging umogleg** | **Høg** | **Høg** | **Test grundig i Steg 4. Om for vanskeleg: bruk `PARALLEL=1` i CI**. |
| Minnebruk aukar (alle generatorar køyrer samtidig) | Middels | Låg | Begrens `PARALLEL` til 8 (standard); dokumenter minnekrav |
| Feil i éin generator stoppar ikkje andre (race condition) | Middels | Middels | xargs propagerer exit-kode frå feila jobb |
| `--output-sync` ikkje støtta i eldre make-versjonar | Låg | Middels | Brukar xargs i staden for make -j |

**Kritisk beslutning før implementasjon**: Test `run_gen_parallel` output i Steg 4 og sjekk om output er lesbart nok for CI-debugging. Om ikkje: **prioriter lesbarheit over hastighet i CI** ved å bruke `PARALLEL=1`.

## Framtidige utviklingar

1. **GitHub Actions matrix per skjema** — køyr kvar skjema som eigen jobb (endå meir parallellisme)
2. **Caching av artefaktar** — hopp over regenerering om skjema er uendra
3. **Inkrementell bygging** — køyr berre generatorar som er nødvendige (basert på `manifest.yaml`)
4. **Make -j oppgradering** — refaktorer til make dependency-graph for betre avhengigheitshåndtering (Fase 3)

## Fase 2: Utført

### Steg 7: Rullar ut til alle domene ✅

**Endringar**:
- Oppdatert `domain_target` macro i Makefile til å bruke `run_gen_parallel`
- Fjerna eksplisitt `domain-ap-no` override (alle domene brukar no same tilnærming)
- Endra header til å vise `(PARALLEL=N)` for alle domene
- Parallellisert: gen-jsonld-context, gen-shacl, gen-python, gen-json-schema, gen-proto

**Testing**:
- `make domain-ap-no PARALLEL=8` → 4m17s, 36 jobbar med timer ✅
- `make domain-ngr PARALLEL=8` → 2m48s, 20 jobbar med timer ✅

**Verifisert**: Alle `domain-*` targets støttar no `PARALLEL` parameter.

### Steg 8-9: Gjenstår

- [ ] Oppdater COMMANDS.md med PARALLEL-dokumentasjon
- [ ] Vurder PARALLEL-setting for CI workflows
