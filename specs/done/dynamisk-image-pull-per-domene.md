# Dynamisk image-pull per domene i generate-workflow

## Bakgrunn

**Problem:**  
`generate.yml`-workflowen pullar **alle 5 container-images** for kvart domene, uavhengig av om domenet faktisk brukar dei:

- `linkml-local` (353 MB) — **alltid påkrevd**
- `python-pytest` (79 MB) — **alltid påkrevd**
- `plantuml` (328 MB) — **alltid påkrevd**
- `asyncapi-cli-local` (4.43 GB) — **berre brukt av `samt/samt-bu`**
- `avrotize-local` (566 MB) — **for tida ikkje brukt**

**Konsekvensar:**
- 7 av 8 domene lastar ned unødvendige 5 GB (asyncapi + avrotize)
- Asyncapi-imaget aleine tar ~60 sekund å pulle
- Total pull-tid per domene: ~90 sekund
- **Sløsing:** 7 × 60s × 8 domene = ~8 minutt ekstra byggtid per push

**Årsak:**  
Hardkoda liste i workflow-steget "Last images inn i podman frå GHCR" — ingen domene-spesifikk deteksjon.

## Løysing

Legg til eit steg **før** image-pull som analyserer domenet sine `build.yaml`-filer og **detekterer kva images som faktisk trengs**:

1. **Nytt steg:** `Detekter påkrevde images for ${{ matrix.domain }}`
   - Itererer gjennom `src/linkml/${{ matrix.domain }}/*/build.yaml`
   - Sjekkar for `asyncapi: true`, `avro: true`, osv.
   - Eksporterer liste via `$GITHUB_OUTPUT`

2. **Oppdatert steg:** `Last images inn i podman frå GHCR`
   - Itererer over `${{ steps.detect-images.outputs.images }}`
   - Pullar **berre** dei detekterte images
   - Beheld parallell pull-logikk

**Forventet gevinst:**
- **7 av 8 domene:** skipper asyncapi-cli-local (sparer ~60s per domene = ~7 minutt totalt)
- **Alle domene:** skipper avrotize-local dersom ikkje brukt (ekstra ~30s)
- **Framtidig-sikker:** nye generatorar vert automatisk detekterte

## Handlingsliste

- [x] Analyser kva images kvart domene faktisk brukar
- [x] Skriv deteksjonslogikk i `.github/workflows/generate.yml`
- [x] Refaktorer pull-steg til å iterere over detektert liste
- [x] Test syntaks lokalt
- [x] Push og test i CI (sjå første generate-workflow-køyring)
- [x] Verifiser at domene som **treng** asyncapi (`samt`) framleis får det
- [x] Verifiser at andre domene **ikkje** pullar asyncapi

## Endra filer

- `.github/workflows/generate.yml` — legg til deteksjonssteg og refaktorer pull-logikk

## Tekniske detaljar

**Detekterte generator → image mapping:**

| Generator | Krev image | Aktivert av build.yaml-felt |
|---|---|---|
| gen-doc, gen-jsonld, gen-owl, osv. | `linkml-local` | (alltid) |
| gen-python | `python-pytest` | (alltid) |
| gen-plantuml | `plantuml` | (alltid) |
| gen-asyncapi | `asyncapi-cli-minimal` | `asyncapi: true` |
| gen-avro | `avrotize-local` | `avro: true` |

**Base images (alltid påkrevd):**  
`linkml-local`, `python-pytest`, `plantuml`

**Betinga images (berre dersom `build.yaml` aktiverer dei):**  
`asyncapi-cli-local`, `avrotize-local`

## Testing

**Manuell verifikasjon:**

```bash
# Sjekk kva samt treng
grep -r "asyncapi: true" src/linkml/samt/*/build.yaml
# src/linkml/samt/samt-bu/build.yaml:  asyncapi: true

# Sjekk kva ap-no treng
grep -r "asyncapi: true" src/linkml/ap-no/*/build.yaml
# (tom output — asyncapi ikkje aktivert)
```

**CI-verifikasjon:**

1. Push til `main` og følg workflow-loggar
2. Sjekk steg "Detekter påkrevde images for X"
3. Verifiser at:
   - `samt` listar `asyncapi-cli-local`
   - `ap-no`, `fint`, osv. **ikkje** listar `asyncapi-cli-local`
4. Verifiser redusert byggtid for domene utan asyncapi

## Vurdering av vidare optimalisering

**1. Caching av images på tvers av domene (avvist):**  
Pull images éin gong globalt (før matrix), eksporter til GitHub Actions artifacts, og last ned i kvar domene-jobb.

**Reknestykke:**
- **Scenario A (dagens løysing):** 10.5 GB total nedlasting frå GHCR, ~90s total tid (parallell pull)
- **Scenario B (artifact-caching):** 15.7 GB total nedlasting (5.2 GB GHCR + 10.5 GB artifacts), ~120s total tid (90s pull + 30s artifact-import)

**Konklusjon:** Dagens løysing er **raskare** (30s gevinst), brukar **mindre bandbreidde** (5 GB spart), og er **enklare**. Artifact-caching vil berre vere betre dersom GHCR-pull er ekstremt treg (>5 min per domene) eller me brukar sequential pull i staden for parallell.

**2. Lazy-loading av images:**  
Pull images **etter kvart som dei trengs** i generatorstegene — ikkje alle på førehand. Krev endring i Makefile-logikk.

**Potensial:** Berre `samt`-jobben pullar `asyncapi-cli-local`, andre jobbar hoppar over. Men sidan me allereie har dynamisk deteksjon (Fase 1), er gevinsten marginal.

**3. Alternative base images:**  
Vurder å redusere storleiken på `asyncapi-cli-local` (for tida 4.43 GB) ved å bruke `alpine`-base eller multi-stage builds.

**Potensial:** Kan redusere `asyncapi-cli-local` frå 4.43 GB til ~1-2 GB. Dette vil spare ~3 GB og ~30-40s pull-tid for `samt`-domenet.

## Utført

**Dato:** 2026-08-01

**Resultat:**  
Implementerte dynamisk image-deteksjon per domene i `generate.yml`. Kvar domene-jobb analyserer sine `build.yaml`-filer og pullar **berre** dei nødvendige container-images. Dette reduserer sløsing frå 7 × 5 GB (asyncapi + avrotize) til 0 GB for domene som ikkje brukar desse generatorane.

**Gevinst:**
- **7 av 8 domene:** skipper asyncapi-cli-local (sparer ~60s per domene)
- **Alle domene:** skipper avrotize-local dersom ikkje brukt (sparer ~30s)
- **Total estimert tidsbesparing:** ~7 minutt per workflow-køyring

**Avvist vidare optimalisering:**  
Global artifact-caching vart vurdert og avvist fordi dagens løysing (parallell pull per domene) er både raskare (30s gevinst) og brukar mindre bandbreidde (5 GB spart) enn artifact-basert caching.
