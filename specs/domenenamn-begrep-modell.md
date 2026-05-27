# Evaluering: Domenenamna `begrep` og `modell`

## Bakgrunn

Repoet har to domene som kan synast å overlappe semantisk:

| Domene | Skjema | Importerer | Målkatalog |
|---|---|---|---|
| `begrep` | `brreg-begrep-schema` | `skos-ap-no-schema` | Felles Begrepskatalog |
| `modell` | `brreg-modellkatalog-schema` | `modelldcat-ap-no-schema` | Felles Datakatalog |

---

## Er dei om det same?

Nei — dei implementerer ulike AP-NO-profiler og publiserer til ulike katalogar:

- **`begrep`** inneheld SKOS-definisjonar av omgrep (termar med tyding, fagområde,
  kjeldereferansar). Produksjonsdatafila er ein faktisk omgrepskatalog med begrep-objekt
  og definisjonar. Containerklassen heiter `BegrepContainer`.

- **`modell`** inneheld ein ModelDCAT-AP-NO-katalog som *beskriv informasjonsmodellar*
  (kva modellar finst, kven som eig dei, kvar dei er tilgjengelege). Containerklassen
  heiter `ModellkatalogContainer`. Innhaldet er metadata *om* modellar — ikkje sjølve
  modellane.

Dei er parallelle på same måten som `begrep` og ein hypotetisk `datakatalog` ville
vore parallelle: begge er «katalog-domene» som applicerer ein AP-NO-profil, men
dei katalogiserer ulike ting.

---

## Kva er problemet med noverande namngjeving?

### `modell` er tvetydig i denne konteksten

Heile `src/linkml/`-treet inneheld modellar (LinkML-skjema). Eit domene kalla
`modell` høyrest ut som det er rota for alle modellar — ikkje ein spesifikk
katalogtype. Samanlikn med dei andre domenenamna:

| Domene | Kva det inneheld | Namngjevingsprinsipp |
|---|---|---|
| `ap-no` | AP-NO-profiler | Standardnamn |
| `begrep` | SKOS-omgrepskatalogskjema | Innhaldstype |
| `fair` | FAIR-metadataskjema | Standardnamn |
| `fint` | FINT-integrasjonsmodellar | Organisasjon/system |
| `ngr` | NGR-grunndata-skjema | Organisasjon/system |
| `oreg` | Offentlege register-skjema | Organisasjon/system |
| `samt` | Kommunale integrasjonsmodellar | Organisasjon/system |
| `modell` | ModelDCAT-AP-NO-katalogskjema | ??? |

`modell` bryt med alle dei andre prinsippa. Det er verken eit standardnamn, ein
innhaldstype eller ein organisasjon/system-referanse — det er berre det generiske
ordet for kva heile repoet er.

### `begrep` er òg generisk — men klarare

«Begrep» som domenenamn er generisk på same vis, men er klarare fordi det peikar
på ein veletablert standard (SKOS-AP-NO-Begrep) og ein kjend katalogtype. Alle
veit at eit begrepsdomene inneheld SKOS-omgrep.

---

## Alternativ

### A: Hald noverande struktur — berre omdøyp `modell`

Einaste problemet er at `modell` er tvetydig. Eit meir presist namn:

| Alternativ | Vurdering |
|---|---|
| `modellkatalog` | Eksplisitt: det er ein katalog av modellar. Parallelt med `begrep` (katalog av omgrep). |
| `informasjonsmodell` | Langt, men presist. Ikkje ein etablert standardterm på norsk. |
| `dcat` | Kort, men kolliderer med `ap-no/dcat-ap-no`. |

**Anbefalt: `modellkatalog`** — presist, kortfatta, parallelt med `begrep`.

### B: Slå saman til eit `katalog`-domene

```
src/linkml/katalog/
  brreg-begrep/          ← skjema for omgrepskatalog
  brreg-modellkatalog/    ← skjema for modellkatalog
```

**Fordelar**: eitt domene for alle «katalog-over-noko»-typar.

**Ulemper**: kollapsar distinksjonen mellom SKOS-AP-NO og ModelDCAT-AP-NO. Vanskeleg
å eintydig referere til «begrepsdomenet» eller «modellkatalogdomenet» i CI, make-target
og dokumentasjon. Gjev ikkje meir klarleik enn alternativ A.

### C: Hald begge noverande namn uendra

Konfusjonen er primært i `modell`-namnet. Å halde det er eit val om å leve med
tvetydigheita.

---

## Konklusjon

`begrep` og `modell` er **ikkje** om det same. Dei applicerer ulike AP-NO-profiler
og publiserer til ulike katalogar.

Det reelle problemet er at **`modell` er eit dårleg domenenamn** i ein katalog der
alt er modellar. Tilrådd tiltak:

| Kva | Endring |
|---|---|
| Omdøyp `src/linkml/modell/` | → `src/linkml/modellkatalog/` |
| Oppdater alle referansar | Makefile, CI-matrise (`domain:`), `mkdocs/publish.sh`, README |
| `begrep` | Ingen endring — namnet er klart nok |

Endringa er reint organisatorisk og krev ingen endringar i skjema-`id`, URI-ar
eller genererte artefakter.

---

## Kva må endrast ved omdøyping til `modellkatalog`

| Fil | Endring |
|---|---|
| `src/linkml/modell/` | Omdøyp katalogen |
| `.github/workflows/generate.yml` | `domain: [..., modell, ...]` → `modellkatalog` |
| `.github/workflows/validate.yml` | Same |
| `mkdocs/publish.sh` | `modell)` case-label |
| `README.md` | Tekstlege referansar |
| `CLAUDE.md` | Domenetabell |

---

## Vurdering: kan `begrepskatalog` fungere som nytt domenenamn?

### Noverande tilstand

| | `begrep`-domenet | `modell`-domenet |
|---|---|---|
| Domenekatalogg | `src/linkml/begrep/` | `src/linkml/modell/` |
| Skjemanamn | `brreg-begrep` | `brreg-modellkatalog` |
| Schema-id | `https://data.norge.no/linkml/brreg-begrep` | `https://data.norge.no/linkml/brreg-modellkatalog` |
| Containerklasse | `BegrepContainer` | `ModellkatalogContainer` |

Den avgjerande skilnaden: for `modell`-domenet er skjemaet **allereie** kalla
`brreg-modellkatalog`. Omdøyping av *domenet* til `modellkatalog` er berre ei
katalogomflytting — ingen endringar i skjema, id eller containerklasse.

For `begrep`-domenet stemmer domenenamnet og skjemanamnet med kvarandre (`begrep`
↔ `brreg-begrep`). Omdøyping av domenet til `begrepskatalog` bryt denne indre
konsistensen med mindre skjemaet òg vert omdøypt.

### To alternativ for `begrep` → `begrepskatalog`

#### Alternativ 1 — berre domenekatalogg (låg kostnad)

```
src/linkml/begrepskatalog/
  brreg-begrep/           ← skjemanamn uendra
```

Domene- og skjemanamn divergerer (`begrepskatalog` vs. `brreg-begrep`).
Dette bryt mønsteret der skjemanamnet inneheld domenenamnet som prefiks
(jf. `fint/fint-*`, `ngr/ngr-*`).

#### Alternativ 2 — full omdøyping (høg kostnad)

```
src/linkml/begrepskatalog/
  brreg-begrepskatalog/   ← katalog, fil, name og id endra
```

Krev:
- Flytte og omdøyp `brreg-begrep/` → `brreg-begrepskatalog/`
- Omdøyp `brreg-begrep-schema.yaml` → `brreg-begrepskatalog-schema.yaml`
- Endre `name: brreg-begrep` → `name: brreg-begrepskatalog` i skjemaet
- **Endre `id: https://data.norge.no/linkml/brreg-begrep`** → ny URI (brot-endring)
- Omdøyp datafila `brreg-begrep.yaml` → `brreg-begrepskatalog.yaml`
- Oppdatere `published-uris.lock` og alle andre referansar

Schema-id-endringa er den kritiske kostanden: URIen
`https://data.norge.no/linkml/brreg-begrep` er den semantiske identifikatoren
for skjemaet i RDF-verda. Dersom eksterne verktøy importerer eller refererer til
denne, er ei endring ein brot-endring.

### Gevinsten ved `begrepskatalog`

| Gevinst | Vurdering |
|---|---|
| Symmetri med `modellkatalog` | Reell — begge katalog-domene får same suffix-mønster |
| Tydeleg rolle | Marginal — `begrep` er allereie eintydig |
| Førebilete for framtida | Nyttig om `datakatalog`, `tjenestekatalog` o.l. kjem |

### Konklusjon

`modellkatalog` er ein eintydig gevinst med nær null kostnad — berre ei
katalogomflytting utan skjemaendringar.

`begrepskatalog` gjev symmetri, men til uforhaldsmessig høg kostnad:

- Alternativ 1 (berre domenekatalogg) skaper ein ny inkonsistens mellom
  domenenamn og skjemanamn.
- Alternativ 2 (full omdøyping) inneber ei schema-id-endring som er ein
  semantisk brot-endring.

**Tilråding:** omdøyp `modell` → `modellkatalog`, la `begrep` vere uendra.
Symmetrien er ikkje viktig nok til å forsvare verken inkonsistensen (alt. 1)
eller brot-endringa (alt. 2).
