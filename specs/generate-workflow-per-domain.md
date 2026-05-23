# Generate- og validate-workflow: domene-matrise

## Bakgrunn

Den noverande matrisa i `generate.yml` har ~220 entries (20 skjema × 12 artefakttypar).
Det gjer det vanskeleg å lese CI-statusen i GitHub Actions UI. I tillegg er det 12
nær-identiske composite actions (`gen-context`, `gen-doc`, …) og `validate.yml` har 6
nær-identiske domene-jobbar — all kode som ikkje er nødvendig.

## Mål

- Maksimalt 6 parallelle `generate`-jobbar (éin per domene)
- Slett 14 composite actions som berre er tynne skall rundt `make`-kall
- Slett Python-skriptet — domenelistinga er statisk og kan hardkodast
- Konverter `validate.yml` frå 6 statiske jobbar til éin matrise-jobb
- Bevare per-domene cache-invalidering

## Ny arkitektur

### Jobb-flyt per workflow

```
generate.yml
──────────────────────────────────────────────────────────────────
                      ┌── generate/ap-no ──┐
                      ├── generate/fair    ─┤
 ensure-images ──────►├── generate/fint    ─┼──► publish
                      ├── generate/ngr     ─┤
                      ├── generate/oreg    ─┤
                      └── generate/samt   ──┘

validate.yml
──────────────────────────────────────────────────────────────────
                       ┌── validate/ap-no ─┐
                       ├── validate/fair   ─┤
 build-validator ─────►├── validate/fint   ─┤
                       ├── validate/ngr    ─┤
                       ├── validate/oreg   ─┤
                       └── validate/samt   ─┘
```

### Steg inne i kvar `generate`-jobb

```
 checkout
     │
     ▼
 cache restore  ◄── key: domain + hashFiles(src/linkml/domain/**) + infra
     │
 cache-hit? ──ja──────────────────────────────────┐
     │                                             │
    nei                                            ▼
     │                                   upload-artifact (generated/)
     ▼
 load-images (frå Actions cache)
     │
     ▼
 for artifact in linkml context shapes python
                 json-schema owl rdf erdiagram
                 doc proto plantuml examples:
   make domain-gen-$artifact DOMAIN=$domain
     │
     └──────────────────────────────────────────► upload-artifact (generated/)
```

### Steg inne i kvar `validate`-jobb

```
 checkout
     │
     ▼
 cache restore  ◄── key: domain + hashFiles(src/linkml/domain/**, examples/domain/**)
     │
 cache-hit? ──ja──► (ferdig)
     │
    nei
     │
     ▼
 load-validator (frå Actions cache)
     │
     ▼
 make domain-validate-bronze DOMAIN=$domain
     │
     ▼
 make domain-validate-examples DOMAIN=$domain
     │
     ▼
 touch .validated-$domain
```

Totalt: 6 parallelle generate-jobbar og 6 parallelle validate-jobbar.
Ingen `setup`-jobb — domenelistinga er statisk og treng ikkje skriptgenerering.

---

## Endringar

### 1. `generate.yml` — domene-matrise

Erstatt `setup`-jobben og 220-entry-matrisa med ein statisk domene-matrise direkte i jobben:

```yaml
generate:
  needs: [ensure-images]
  runs-on: ubuntu-22.04
  strategy:
    matrix:
      domain: [ap-no, fair, fint, ngr, oreg, samt]
    fail-fast: false
  steps:
    - uses: actions/checkout@v6

    - name: Cache genererte artefaktar (${{ matrix.domain }})
      id: cache-generated
      uses: actions/cache@v5
      with:
        path: generated/${{ matrix.domain }}/
        key: generated-${{ matrix.domain }}-${{ hashFiles(format('src/linkml/{0}/**', matrix.domain)) }}-infra-${{ hashFiles('src/assets/containers/Dockerfile.linkml', 'src/templates/**', 'Makefile') }}

    - uses: ./.github/actions/load-images
      if: steps.cache-generated.outputs.cache-hit != 'true'

    - name: Generer alle artefaktar for ${{ matrix.domain }}
      if: steps.cache-generated.outputs.cache-hit != 'true'
      run: |
        for artifact in linkml context shapes python json-schema owl rdf erdiagram doc proto plantuml examples; do
          make domain-gen-$artifact DOMAIN=${{ matrix.domain }}
        done

    - uses: actions/upload-artifact@v7
      with:
        name: generated-${{ matrix.domain }}
        path: generated/
        retention-days: 1
```

Merk: `hashFiles(format('src/linkml/{0}/**', matrix.domain))` er lovleg i GitHub Actions —
`format()` vert evaluert til ein streng før `hashFiles()` vert kalla.

Ingen `setup`-jobb og ingen Python-skript: domenelistinga er statisk og kjend på førehand.

### 2. `validate.yml` — domene-matrise

Erstatt 6 statiske domene-jobbar med éin matrise-jobb:

```yaml
validate:
  needs: build-validator
  runs-on: ubuntu-22.04
  strategy:
    matrix:
      domain: [ap-no, fair, fint, ngr, oreg, samt]
    fail-fast: false
  permissions:
    contents: read
    packages: read
  steps:
    - uses: actions/checkout@v6

    - name: Cache validering (${{ matrix.domain }})
      id: cache-validated
      uses: actions/cache@v5
      with:
        path: .validated-${{ matrix.domain }}
        key: validated-${{ matrix.domain }}-${{ hashFiles(format('src/linkml/{0}/**', matrix.domain), format('examples/{0}/**', matrix.domain), 'src/mcp-linkml-validator/server.py', 'src/mcp-linkml-validator/policies/**', 'src/mcp-linkml-validator/flatten-and-validate.bash', 'src/mcp-linkml-validator/Dockerfile', 'src/mcp-linkml-validator/requirements.txt', '.github/workflows/validate.yml') }}

    - uses: ./.github/actions/load-validator
      if: steps.cache-validated.outputs.cache-hit != 'true'

    - name: Valider mot bronze-policy
      if: steps.cache-validated.outputs.cache-hit != 'true'
      run: make domain-validate-bronze DOMAIN=${{ matrix.domain }}

    - name: Valider eksempelfiler mot skjema
      if: steps.cache-validated.outputs.cache-hit != 'true'
      run: make domain-validate-examples DOMAIN=${{ matrix.domain }}

    - name: Merk validering som vellykka
      if: steps.cache-validated.outputs.cache-hit != 'true'
      run: touch .validated-${{ matrix.domain }}
```

### 3. Filer som skal slettast

#### Composite actions (erstatast av direkte `make`-kall i workflowet):

```
.github/actions/gen-context/
.github/actions/gen-doc/
.github/actions/gen-erdiagram/
.github/actions/gen-examples/
.github/actions/gen-json-schema/
.github/actions/gen-linkml/
.github/actions/gen-owl/
.github/actions/gen-plantuml/
.github/actions/gen-proto/
.github/actions/gen-python/
.github/actions/gen-rdf/
.github/actions/gen-shapes/
.github/actions/validate-bronze/
.github/actions/validate-examples/
```

14 katalogar × ~20 linjer = ~280 linjer YAML som forsvinn.

#### Python-skript (ikkje lenger nødvendig):

```
.github/scripts/build-generate-matrix.py
```

#### Composite actions som vert behaldne:

```
.github/actions/load-images/      ← har reel logikk (2 cache-restore + podman load)
.github/actions/load-validator/   ← har reel logikk (cache-restore + podman load)
```

### 4. `schema-gen-*`-mål i Makefile

Dei 12 `schema-gen-*`-måla i Makefile vart lagt til for den noverande per-skjema-matrisa.
Dei er nyttige for lokal utvikling og feilsøking og kan behaldast, men trengst ikkje lenger
av CI.

---

## Cache-strategi

Med domain-matrise vert cache-nøkkelen:

```
generated-{domain}-{sha256 av alle .yaml-filer i src/linkml/{domain}/}-infra-{sha256 av Dockerfile + templates + Makefile}
```

Konsekvens samanlikna med den noverande per-skjema-tilnærminga:
- **Tidlegare**: endra ein skjemafil i `ap-no` → berre det skjemaet og dei som importerer det vart regenerert
- **No**: endra ein skjemafil i `ap-no` → alle skjema i `ap-no`-domenet vert regenerert

Dette er ein akseptabel avvegnad fordi:
1. Skjema i same domene importerer kvarandre (sjå t.d. at `dcat-ap-no` importerer `dqv-ap-no`
   og `common-ap-no`), så dei fleste endringar triggar allereie domenet sitt
2. Generering av eit heilt domene tek under eit minutt per artefakttype
3. Gevinsten i lesbarheit og kodemengde er stor

---

## Kodemengde-oversikt

| Fil/gruppe | Noverande | Etter |
|---|---|---|
| `generate.yml` | 205 linjer | ~70 linjer |
| `validate.yml` | 222 linjer | ~65 linjer |
| `gen-*` composite actions (12 stk) | 264 linjer | 0 linjer (slettar) |
| `validate-bronze` + `validate-examples` | 28 linjer | 0 linjer (slettar) |
| `build-generate-matrix.py` | 85 linjer | 0 linjer (slettar) |
| `load-images` + `load-validator` | 40 linjer | 40 linjer (uendra) |
| **Totalt** | **844 linjer** | **~175 linjer** |

Reduksjon: ~670 linjer (~79 %).

---

## Implementasjonsrekkefølgje

1. Oppdater `generate.yml` med domene-matrise og slett `setup`-jobben
2. Oppdater `validate.yml` med domene-matrise
3. Slett dei 14 composite action-katalogane
4. Slett `.github/scripts/build-generate-matrix.py`
5. Verifiser i CI at alle 6 generate-jobbar og 6 validate-jobbar vert grøne
