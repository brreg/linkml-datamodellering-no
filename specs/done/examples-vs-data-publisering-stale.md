# Stale stiar og feil begrepsbruk: `examples/` vs `data/` i publiseringsdokumentasjon

## Bakgrunn

Repoet skil tydeleg mellom to typar YAML-filer:

| Katalog | Føremål | Publiserast? |
|---|---|---|
| `src/linkml/<domene>/<modell>/examples/` | Illustrative dev-fiksturer — viser gyldig instans, nyttast i gen-doc og testing | **Nei** |
| `src/linkml/<domene>/<modell>/data/` | Stabile produksjonsdata med permanente URI-ar | **Ja** |

Denne invarianten er dokumentert i `mkdocs/docs/publisering-begrep.md` og i CLAUDE.md.

To problem er avdekka:

1. **`publisering-modell.md`** refererer til den gamlde rotnivå-stien `examples/modell/...` (fem stader) som ikkje finst etter omstruktureringen. Stien vart flytta til `src/linkml/modellkatalog/brreg-modellkatalog/examples/` — men dokumentasjonen vart ikkje oppdatert.

2. **`brreg-modellkatalog`** har aldri fått oppretta ein `data/`-underkatalog. Produksjonskatalogen (`brreg-modellkatalog-eksempel.yaml`) ligg difor feil i `examples/` og vert publisert derifrå via `convert-rdf`/`example_rdf: true`. Dette bryt med policy og gjer det vanskeleg å skilje produksjonar frå dev-fiksturer.

3. **`ny-begrepsmodell.md` steg 6** har feil generert outputsti (`generated/begrep/` → korrekt er `generated/begrepskatalog/`) og påstår at eksempel-TTL-en kan importerast til Felles Begrepskatalog — noko som er feil: berre `data/`-filer skal publiserast.

---

## Funn per fil

### 1. `mkdocs/docs/publisering-modell.md` — fem stale stiar

**Problem:** Alle referansane nedanfor brukar rotnivå-stien `examples/modell/...` som ikkje finst.

| Linje | Innhald (stale) | Rett |
|---|---|---|
| 14 | Flowchart: `examples/modell/\nbrreg-modellkatalog-eksempel.yaml` | `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/\nbrreg-modellkatalog.yaml` |
| 14 | Flowchart: `make convert-rdf` | `make convert-data` |
| 14 | Flowchart: `generated/modell/...` | `generated/modellkatalog/...` |
| 19 | `examples/modell/brreg-modellkatalog-eksempel.yaml` | `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml` |
| 37 | `examples/modell/brreg-modellkatalog-eksempel.yaml` | same som over |
| 56 | `INSTANCE=examples/modell/brreg-modellkatalog-eksempel.yaml` | `INSTANCE=src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml` |
| 80 | `examples/modell/brreg-modellkatalog-eksempel.yaml` | same som over |
| 157 | CI trigger: `examples/modell/**` | fjernast (triggeren for `src/linkml/modellkatalog/**` dekkjer alt) |
| 164 | `domain-gen-rdf` | `domain-gen-data` |

---

### 2. `brreg-modellkatalog` — manglande `data/`-underkatalog

**Problem:** `brreg-modellkatalog-eksempel.yaml` inneheld reelle produksjons-URI-ar (`https://brreg.no/modellkatalogar/brreg-modellkatalog/...`) og er kjelda for publisering til Felles Datakatalog. Men fila ligg i `examples/`, ikkje i `data/`. Schema-`manifest.yaml` har `publish_external: true` og `data_policy: felles-datakatalog`, men det er ingen `data/`-manifest som `convert-data` kan finne.

**Gjeldande flyt (feil):**

```
examples/brreg-modellkatalog-eksempel.yaml
    → convert-rdf (via example_rdf: true)
    → generated/modellkatalog/brreg-modellkatalog/brreg-modellkatalog-eksempel.ttl
    → GitHub Pages
```

**Korrekt flyt:**

```
data/brreg-modellkatalog/brreg-modellkatalog.yaml
    → convert-data (via data manifest publish_external: true)
    → generated/modellkatalog/brreg-modellkatalog/brreg-modellkatalog.ttl
    → GitHub Pages
```

**Kva må opprettast:**

```
src/linkml/modellkatalog/brreg-modellkatalog/
├── data/
│   └── brreg-modellkatalog/
│       ├── brreg-modellkatalog.yaml    ← flytt produksjonsinnhald hit
│       └── manifest.yaml              ← publish_external: true; data_policy: felles-datakatalog
```

Etter dette kan `examples/brreg-modellkatalog-eksempel.yaml` vere ein lettare dev-fikstur utan produksjons-URI-ar (t.d. berre éin modell med `https://example.org/...`-URI-ar), og `example_rdf: true` i schema-`manifest.yaml` kan setjast til `false`.

**Schema-`manifest.yaml` etter endring:**

`data_policy: felles-datakatalog` vert flytta til `data/brreg-modellkatalog/manifest.yaml`. Schema-manifesten beheld berre generator-konfigurasjon.

---

### 3. `mkdocs/docs/ny-begrepsmodell.md` steg 6 — feil sti og misvisande tekst

**Problem (linje 217):**

```
Output: `generated/begrep/<katalognavn>/<katalognavn>-eksempel.ttl`
```

Korrekt domene er `begrepskatalog`, ikkje `begrep`:

```
Output: `generated/begrepskatalog/<katalognavn>/<katalognavn>-eksempel.ttl`
```

**Problem (linje 218–220):**

```
Denne Turtle-fila er SKOS-kompatibel og kan importerast til
Felles Begrepskatalog via Begrepskatalog-API.
```

Dette er feil og misvisande: eksempel-Turtle skal *aldri* sendast til Felles Begrepskatalog. Steg 6 er utelukkande for lokal validering og forhåndsvisning under utvikling. Publisering skjer frå `data/`-fila — sjå `publisering-begrep.md`.

**Rett tekst:**

```
Output: `generated/begrepskatalog/<katalognavn>/<katalognavn>-eksempel.ttl`

Denne Turtle-fila er berre for lokal kontroll av at YAML-instansen
vert korrekt serialisert. For publisering til Felles Begrepskatalog —
sjå [Publiser til Felles Begrepskatalog](publisering-begrep.md).
```

---

## Prioritert tiltaksliste

| # | Fil | Endring | Prioritet |
|---|---|---|---|
| 1 | `src/linkml/modellkatalog/brreg-modellkatalog/data/` | Opprett `data/brreg-modellkatalog/brreg-modellkatalog.yaml` (produksjonsinnhald frå eksempelfila) og `data/brreg-modellkatalog/manifest.yaml` (`publish_external: true; data_policy: felles-datakatalog`) | Høg |
| 2 | `src/linkml/modellkatalog/brreg-modellkatalog/manifest.yaml` | Fjern `data_policy: felles-datakatalog`; sett `example_rdf: false` | Høg |
| 3 | `src/linkml/modellkatalog/brreg-modellkatalog/examples/brreg-modellkatalog-eksempel.yaml` | Erstatt med ein lett dev-fikstur (éin modell, `https://example.org/`-URI-ar) | Høg |
| 4 | `mkdocs/docs/publisering-modell.md` | Oppdater flowchart, alle fem `examples/modell/...`-stiar → `data/...`-stiar; fjern `examples/modell/**` frå CI-tabell; bytt `domain-gen-rdf` → `domain-gen-data` | Høg |
| 5 | `mkdocs/docs/ny-begrepsmodell.md` linje 217–220 | Rett outputsti (`begrep` → `begrepskatalog`); fjern påstand om publisering til Felles Begrepskatalog | Medium |
| 6 | `src/linkml/modellkatalog/brreg-modellkatalog/published-uris.lock` | Vurder om URI-ar treng oppdatering etter at datafila er flytta | Lav |

---

## Avhengigheiter

- Tiltak 1–3 må gjerast saman og testast med `make convert-data` og `make domain-validate-data DOMAIN=modellkatalog`
- Tiltak 4 kan gjerast etter at tiltak 1–3 er ferdig og CI-pipelinen er grøn
- Tiltak 5 er uavhengig

## Relaterte spesifikasjonar

- [`katalogstruktur-stale-stiar.md`](katalogstruktur-stale-stiar.md) — tidlegare kartlegging av stale stiar etter strukturendring
- [`publisering-felles-datakatalog.md`](publisering-felles-datakatalog.md) — teknisk spec for modellkatalog-publisering
- [`publisering-felles-begrepskatalog.md`](publisering-felles-begrepskatalog.md) — teknisk spec for begrepskatalog-publisering
