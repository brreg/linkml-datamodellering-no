# Stale referansar i src/assets/scripts/

## Resultat

Sju filer og ein katalog er gjennomgåtte. To funn i scripts:

---

## Funn

### 1. `migreringsscript/migrate-all-containers.sh` linje 66–72 — gamalt eksempel-stimønster

`find_example()`-funksjonen søkjer etter eksempelfiler med gamalt rot-nivå-mønster:

```bash
example="examples/${domain}/${name}-eksempel.yaml"
```

Korrekt sti er:

```bash
example="src/linkml/${domain}/${name}/examples/${name}-eksempel.yaml"
```

Sidan migrerings-scriptet truleg allereie er brukt og ikkje lenger er i aktiv bruk
(alle skjema er migrerte), er dette låg prioritet. Men om scriptet vert køyrt på nytt
vil instansvalidering (steg 3) alltid hoppe over pga. manglande eksempelfil.

---

### 2. `pr-linkml-interactive.bash` linje 2 — feil container-image

```bash
IMAGE="docker.io/linkml/linkml:latest"
```

Brukar det offentlege Docker Hub-imaget i staden for det lokale
`localhost/linkml-local:latest` som alle andre skript brukar. Inkonsistent med
repoet sitt prinsipp om berre å bruke lokale container-images.

Scriptet er eit uferdig interaktivt debug-verktøy (norsk/engelsk miks,
utkommentert kode) og er ikkje i aktiv bruk i Makefile eller CI.

---

## Prioritert tiltaksliste (scripts)

| # | Fil | Endring | Prioritet |
|---|---|---|---|
| 1 | `migreringsscript/migrate-all-containers.sh` linje 66–72 | Oppdater `find_example()` til `src/linkml/${domain}/${name}/examples/` | Lav |
| 2 | `pr-linkml-interactive.bash` linje 2 | Byt `docker.io/linkml/linkml:latest` → `localhost/linkml-local:latest`, eller slett scriptet | Lav |

---

# Stale schema-id — alle skjema brukar gamalt `/linkml/`-mønster

## Konvensjon

Rett konvensjon per `new-model.sh` og namngjevings-spesifikasjon:

```
https://data.norge.no/<domain>/<name>
```

Eksempel: `https://data.norge.no/ngr/ngr-adresse`

Alle eksisterande skjema er oppretta med det gamle mønsteret:

```
https://data.norge.no/linkml/<name>
```

Desse må oppdaterast. `default_prefix` er alltid `<id>/` — rettast automatisk saman med `id`.

---

## Vurdering av dei to mønstra

### `https://data.norge.no/linkml/<model>`

**For:**
- Enkelt og flatt — berre eitt segment etter vertsnamnet.
- Signaliserer eksplisitt at dette er ein LinkML-artefakt, noko som kan vere nyttig for å skilje frå andre ressursar på same domene.

**Mot:**
- Kodar implementasjonsteknologi inn i ein persistent identifikator. Dersom verktøykjeda seinare byttar frå LinkML til t.d. SHACL eller OWL som primærformat, vert URI-en misvisande — men kan ikkje endrast utan å bryte alle referansar.
- Flatt namnerom: `https://data.norge.no/linkml/common` er tvetydig — `common` i kva domene? Dette tvingar unike namn på tvers av alle domene.
- Bryt med W3C Cool URIs-prinsippet om teknologinøytrale, stabile identifikatorar. Eit godt URI fortel kva ressursen *er*, ikkje kva teknologi han er *laga med*.
- Samsvarer ikkje med korleis `data.norge.no` strukturerer andre ressursar (t.d. `data.norge.no/concepts/`, `data.norge.no/datasets/`).

### `https://data.norge.no/<domain>/<model>`

**For:**
- Teknologinøytralt — URI-en forblir gyldig uavhengig av verktøykjeda.
- Hierarkisk og sjølvforklarande: lesaren ser domenetilhøyrsla direkte i URI-en.
- Samsvarer med den faktiske katalogstrukturen (`src/linkml/<domain>/<model>/`) og med data.norge.no sin øvrige URI-strategi.
- Eliminerer kollisjonsproblem: `ap-no/common-ap-no` og `ngr/common` kan sameksistere utan namnekonflikt.
- Samsvar med internasjonale fellesstandardar for LOD (Linked Open Data) — URI-ar bør vere opaque og semantisk stabile.

**Mot:**
- Domene må fastsetjast ved oppretting og er vanskeleg å endre seinare — same persistens-problem, men no på domene-nivå i staden for teknologi-nivå.
- Noko lengre URI-ar.

### Konklusjon

**`https://data.norge.no/<domain>/<model>` er det riktige mønsteret.** Den avgjerande grunnen er at persistente identifikatorar ikkje bør kode implementasjonsdetaljar. `linkml` i ein URI er ein teknologietikett, ikkje ein semantisk etikett — han fortel kva verktøy som vart brukt, ikkje kva ressursen representerer. Domene-segmentet er derimot semantisk stabilt: eit skjema tilhøyrer ap-no-domenet uavhengig av om det i framtida vert eksportert som SHACL, OWL eller noko anna.

Den einaste reelle kostnaden er at ID-endringa er ein bryt­ande endring (*breaking change*) for eventuelle eksterne importørar av ap-no-skjema. Sjå merknad under ap-no-seksjonen nedanfor.

---

## Filer som må oppdaterast

### ap-no (7 skjema)

Merk: desse skjema kan vere importerte av eksterne repo via `bootstrap.sh` og
`reusable-validate.yml`. ID-endring er ein semver-brot og krev koordinering.

| Fil | Gamalt id | Nytt id |
|---|---|---|
| `src/linkml/ap-no/common/common-ap-no-schema.yaml` | `https://data.norge.no/linkml/common-ap-no` | `https://data.norge.no/ap-no/common-ap-no` |
| `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml` | `https://data.norge.no/linkml/cpsv-ap-no` | `https://data.norge.no/ap-no/cpsv-ap-no` |
| `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` | `https://data.norge.no/linkml/dcat-ap-no` | `https://data.norge.no/ap-no/dcat-ap-no` |
| `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml` | `https://data.norge.no/linkml/dqv-ap-no` | `https://data.norge.no/ap-no/dqv-ap-no` |
| `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml` | `https://data.norge.no/linkml/modelldcat-ap-no` | `https://data.norge.no/ap-no/modelldcat-ap-no` |
| `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml` | `https://data.norge.no/linkml/skos-ap-no` | `https://data.norge.no/ap-no/skos-ap-no` |
| `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml` | `https://data.norge.no/linkml/xkos-ap-no` | `https://data.norge.no/ap-no/xkos-ap-no` |

`common-ap-no-schema.yaml` har i tillegg ein eksplisitt `capno:`-prefix som også
nyttar det gamle mønsteret og må oppdaterast:

```yaml
# Gamalt
capno: https://data.norge.no/linkml/common-ap-no/
# Nytt
capno: https://data.norge.no/ap-no/common-ap-no/
```

### begrepskatalog (1 skjema)

| Fil | Gamalt id | Nytt id |
|---|---|---|
| `src/linkml/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog-schema.yaml` | `https://data.norge.no/linkml/brreg-begrepskatalog` | `https://data.norge.no/begrepskatalog/brreg-begrepskatalog` |

### fair (1 skjema)

| Fil | Gamalt id | Nytt id |
|---|---|---|
| `src/linkml/fair/fair-metadata/fair-metadata-schema.yaml` | `https://data.norge.no/linkml/fair-metadata` | `https://data.norge.no/fair/fair-metadata` |

(`default_prefix` brukar `https://data.norge.no/fair#` — separat konvensjon, rør ikkje.)

### fint (7 skjema)

| Fil | Gamalt id | Nytt id |
|---|---|---|
| `src/linkml/fint/fint-common/fint-common-schema.yaml` | `https://data.norge.no/linkml/fint-common` | `https://data.norge.no/fint/fint-common` |
| `src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml` | `https://data.norge.no/linkml/fint-administrasjon` | `https://data.norge.no/fint/fint-administrasjon` |
| `src/linkml/fint/fint-arkiv/fint-arkiv-schema.yaml` | `https://data.norge.no/linkml/fint-arkiv` | `https://data.norge.no/fint/fint-arkiv` |
| `src/linkml/fint/fint-okonomi/fint-okonomi-schema.yaml` | `https://data.norge.no/linkml/fint-okonomi` | `https://data.norge.no/fint/fint-okonomi` |
| `src/linkml/fint/fint-personvern/fint-personvern-schema.yaml` | `https://data.norge.no/linkml/fint-personvern` | `https://data.norge.no/fint/fint-personvern` |
| `src/linkml/fint/fint-ressurs/fint-ressurs-schema.yaml` | `https://data.norge.no/linkml/fint-ressurs` | `https://data.norge.no/fint/fint-ressurs` |
| `src/linkml/fint/fint-utdanning/fint-utdanning-schema.yaml` | `https://data.norge.no/linkml/fint-utdanning` | `https://data.norge.no/fint/fint-utdanning` |

### modellkatalog (1 skjema)

| Fil | Gamalt id | Nytt id |
|---|---|---|
| `src/linkml/modellkatalog/brreg-modellkatalog/brreg-modellkatalog-schema.yaml` | `https://data.norge.no/linkml/brreg-modellkatalog` | `https://data.norge.no/modellkatalog/brreg-modellkatalog` |

### ngr (4 skjema)

| Fil | Gamalt id | Nytt id |
|---|---|---|
| `src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml` | `https://data.norge.no/linkml/ngr-adresse` | `https://data.norge.no/ngr/ngr-adresse` |
| `src/linkml/ngr/ngr-eiendom/ngr-eiendom-schema.yaml` | `https://data.norge.no/linkml/ngr-eiendom` | `https://data.norge.no/ngr/ngr-eiendom` |
| `src/linkml/ngr/ngr-person/ngr-person-schema.yaml` | `https://data.norge.no/linkml/ngr-person` | `https://data.norge.no/ngr/ngr-person` |
| `src/linkml/ngr/ngr-virksomhet/ngr-virksomhet-schema.yaml` | `https://data.norge.no/linkml/ngr-virksomhet` | `https://data.norge.no/ngr/ngr-virksomhet` |

### oreg (1 skjema — default_prefix berre)

`register-over-aksjeeiere-schema.yaml` har `id: https://example.no/...` (placeholder —
ikkje berørt), men `default_prefix` refererer det gamle mønsteret:

| Fil | Gamalt default_prefix | Nytt default_prefix |
|---|---|---|
| `src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml` | `https://data.norge.no/linkml/register-over-aksjeeiere/` | `https://data.norge.no/oreg/register-over-aksjeeiere/` |

---

## Dokumentasjonsfiler som må oppdaterast

| Fil | Linje(r) | Gamalt | Nytt |
|---|---|---|---|
| `CLAUDE.md` | 231, 233 | `https://data.norge.no/linkml/ngr-adresse` | `https://data.norge.no/ngr/ngr-adresse` |
| `mkdocs/docs/ny-begrepsmodell.md` | 47, 55 | `https://data.norge.no/linkml/<katalognavn>` | `https://data.norge.no/begrepskatalog/<katalognavn>` |

---

## Prioritert tiltaksliste (schema-id)

| # | Skjema/fil | Prioritet | Merknad |
|---|---|---|---|
| 1 | ngr (4 skjema) | Medium | Interne referansar, ikkje ekstern bruk |
| 2 | begrepskatalog, modellkatalog (2 skjema) | Medium | Interne referansar |
| 3 | fair (1 skjema) | Medium | Interne referansar |
| 4 | fint (7 skjema) | Medium | Interne referansar |
| 5 | ap-no (7 skjema) | **Høg — koordiner først** | Kan vere importerte eksternt; ID-endring er semver-brot |
| 6 | `CLAUDE.md` og `ny-begrepsmodell.md` | Lav | Dokumentasjon |
