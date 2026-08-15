# Vurder om make test-optimaliseringane kan vidareførast til make domain-*

## Bakgrunn

Denne økta gjorde fleire optimaliseringar av `make test` (`tests/
test_make.sh`): batcha RDF-/docs-gyldigheitssjekk (Tiltak 1 + gen-docs-
speedup), fjerna redundant skjema-kompilering i `batch-convert.py`
(Tiltak 2), splitta dei tyngste Fase A-batchane i to parallelle
delkontainarar, og heva `BATCH_GENERATE_WORKERS`-standarden. Brukaren
ønskjer ei vurdering av om nokon av desse kan vidareførast til
`make domain-*` (den faktiske produksjons-genereringspipelinen).

## Undersøking

Las `make/20-domain-targets.mk`, `src/assets/scripts/makefile/run-
domain-pipeline.sh`, `src/assets/scripts/makefile/convert-examples.sh`,
`batch-generate-instances.py` sin `run_convert()`, domenetal per
skjemakatalog, og `.github/workflows/generate.yml` sin CI-invokering.

### Kva `make domain-*` alt har (frå FØR denne økta)

- **Batcha generering** — `batch-generate.py`/`batch-generate-
  instances.py` er DEN SAME delte infrastrukturen `make domain-*` og
  `tests/test_make.sh` sine Fase A-steg BEGGE kallar. Alt batcha éin
  gong per generator, ikkje éin gong per skjema.
- **Fase-medviten parallellisering** — `run-domain-pipeline.sh` har
  ALT ei tilsvarande Fase 1/2/3-inndeling (12 samstundes steg i Fase 1
  åleine), same grunnmønster som `run_phase_a()` i `test_make.sh` (jf.
  `specs/backlog/effektiviser-generate-workflow-koyretid.md`, gjort FØR
  denne økta).
- **CI-nivå domeneparallellisme** — `generate.yml` køyrer `make
  domain-${{ matrix.domain }}` som ein GitHub Actions MATRIX-bygg — kvar
  domene får SIN EIGEN CI-runner, heilt uavhengig av dei andre. Dette er
  eit HEILT ANNA parallellitetsnivå enn `test_make.sh`, som køyrer ALLE
  35 skjema på ÉI maskin.

### Domenestorleik (tal skjema per domene, `src/linkml/*/`)

```
ap-no: 9   modellkatalog: 6   fint: 6   referanse: 4   ngr: 4
oreg: 3    samt: 1   fair: 1   begrepskatalog: 1
```

Dette er AVGJERANDE for kva som kan vidareførast — `test_make.sh`
opererer på 35 skjema SAMLA, `make domain-X` på 1-9 SKJEMA PER KALL.

## Vurdering, tiltak for tiltak

| Test-tiltak | Gjeld for domain-X? | Grunngjeving |
|---|---|---|
| **BATCH_GENERATE_WORKERS 6→8** | ✅ **Alt vidareført, ingen tiltak nødvendig** | `batch-generate.py` er DELT kode — endringa slår automatisk inn for `make domain-X` sine `gen-rdf`/`gen-docs`-kall òg, sidan miljøvariabelen berre vert lesen der (ikkje test-spesifikk plumbing). |
| **rdf-validity / docs-validity (batcha Fase B-gyldigheitssjekk)** | ❌ **Ikkje aktuelt** | Dette var ein reint TEST-intern kostnad — `test_gen_docs()`/`test_gen_rdf()` sine EKSTRA gyldigheitssjekkar (Fase B) finst ikkje i `make domain-X` sin pipeline i det heile. `make domain-X` sin jobb er å GENERERE, ikkje verifisere sitt eige output — det gjer CI sine separate `validate-*`-mål, som er UTANFOR `domain_target` og ikkje endra i denne økta. |
| **batch-convert.py-caching (Tiltak 2)** | ❌ **Ikkje aktuelt, rotårsaka finst ikkje i produksjon** | Kostnaden Tiltak 2 løyste (`PythonGenerator(schema).compile_module()` betalt 3-4× PER SKJEMA) kjem av at `roundtrip-json`/`roundtrip-ttl` sine test-eigne jobbkjeder (fleire steg PER SKJEMA: a.json→b.yaml→c.json osv.) er eit REINT TEST-omgrep — dei finst ikkje i produksjon. `gen-linkml-convert` sin eigen jobbliste (`convert-examples.sh`) har NØYAKTIG ÉIN jobb PER SKJEMA (éin eksempelfil → éin TTL-fil) — ingen repetert kompilering å eliminere, sidan kvart skjema uansett berre vert kompilert éin gong. `run_convert()` (`batch-generate-instances.py`) brukar framleis den gamle Click-CLI-mønsteret (ulikt det nye `batch-convert.py`) — kan i prinsippet omskrivast for STILISTISK konsistens, men gjev INGEN målbar tidsgevinst (kompileringskostnaden er den same uansett kallmønster, sidan han uansett berre skjer éin gong per skjema). Låg prioritet, reint kosmetisk. |
| **Splitting i 2 parallelle batchar (`run_phase_a_step_split2`/ `_run_phase_a_convert_batch_split2`)** | ❌ **Ikkje tilrådd** | To sjølvstendige grunnar: (1) Domene har 1-9 skjema — for dei fleste (6 av 9 domene har ≤4 skjema) er det for lite å dele i "to halvdelar" til at det gjev meining, og halvering av eit domene med 1-2 skjema gjev null eller negativ gevinst (dobla kontainar-oppstartskostnad). (2) Eiga undersøking denne økta (`gen-plantuml`-JVM-granskinga) fann at splitting IKKJE gav målbar gevinst NETTOPP fordi maskina alt var mette av 16-17 SAMSTUNDES steg som kjempa om same CPU/RAM — `run-domain-pipeline.sh` har ALT 12 samstundes Fase 1-steg per domene-kall, så same mettings-mekanisme ville gjort seg gjeldande der, sannsynlegvis endå sterkare sidan CI-runnarar typisk har FÆRRE kjernar enn utviklingsmaskina denne økta vart målt på. |
| **Fase A/B-oppsummering (kolonnejustert, fargar, feila-skjema-liste)** | 🟡 **Potensielt nyttig, men UX — ikkje ytingsrelatert** | `run-domain-pipeline.sh` har INGEN tilsvarande oppsummering i dag — berre `run_bg`/`wait_job` med feillogging via `log_error`. Ei tilsvarande "Fase 1: gen-docs (N skjema) ... (Xs) OK/FEIL"-oppsummering ETTER kvar fase (same idé som `print_phase_a_summary()`) ville gjeve utviklarar betre oversikt ved lokal `make domain-X`-køyring — men dette er ei UX-forbetring, IKKJE ei vidareføring av nokon av dei MÅLTE ytingsgevinstane frå denne økta. Vurderast som eit HELT NYTT, separat tiltak dersom ønska — utanfor scope for "vidarefør optimaliseringane". |

## Konklusjon

**Alle dei reelle YTINGSgevinstane frå denne økta er anten (a) allereie
delte med produksjon via felles Python-infrastruktur (worker-talet), 
eller (b) løyser eit problem (redundant per-jobbrad skjemakompilering,
kostbare per-fil Fase B-sjekkar, mange-timars fan-out over 35 skjema)
som rett og slett ikkje finst i `make domain-X` sin arkitektur** — anten
fordi problemet var eit reint test-only-omgrep (roundtrip-jobbkjeder,
Fase B-gyldigheitssjekkar), eller fordi domain-X sin CI-matrix-modell
og små per-domene skjematal gjer at den underliggjande føresetnaden
(mange samstundes einingar som kan splittast/batchast vidare) ikkje er
til stades i same grad.

Den einaste ATTVERANDE moglegheita er ei rein UX-oppsummering
(analogt `print_phase_a_summary()`) for `run-domain-pipeline.sh` — ikkje
implementert her, sidan det er ei NY funksjonalitet, ikkje ei
vidareføring av ei målt ytingsforbetring. Foreslå som eige tiltak
dersom ønska.

**Ingen kodeendringar gjort i denne spec-fila** — reint vurderande, som
bede om.

## Utført

Vurderinga er komplett (sjå «Vurdering, tiltak for tiltak» og
«Konklusjon» over) — ingen kodeendringar var venta eller gjorde, sidan
oppgåva var å VURDERE, ikkje implementere. Konklusjonen: alle fire
måletiltaka frå denne økta er anten alt delte med produksjon (workers)
eller løyser problem som ikkje finst i `make domain-X` sin arkitektur
(dei tre andre). Éin ny UX-idé (Fase-oppsummering for
`run-domain-pipeline.sh`) vart identifisert og eksplisitt lagt til
sides som eit eige, framtidig tiltak dersom ønska — ikkje del av denne
vurderinga sitt scope.

## Referanse

- `specs/done/optimaliser-make-test-basert-pa-logginnsikt.md` — Tiltak 1+2
- `specs/done/gjer-gen-docs-raskare-fase-b.md`
- `specs/done/splitt-fase-a-batchar-gen-docs-plantuml-roundtrip-json.md`
- `specs/backlog/effektiviser-generate-workflow-koyretid.md` — kjelda til
  `run-domain-pipeline.sh` sin FØR-eksisterande Fase 1/2/3-parallellisme
