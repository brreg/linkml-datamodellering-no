# Nynorsk-omsetjing — plan for README og mkdocs-filer

## Bakgrunn og mål

### Språkdeling

Repoet nyttar to skriftspråk med klart skilde domene:

| Domene | Språk | Gjeld |
|---|---|---|
| **Modellering** | **Norsk bokmål** | Klassenamn, slotnamn, skildringar og kommentarar i `.yaml`-skjema |
| **Dokumentasjon** | **Nynorsk** | README-filer, mkdocs-sider, spesifikasjonar i `specs/` |

Bakgrunnen for bokmål i modellering er at skjemaa følgjer terminologien i norske offentlege
standardar (DCAT-AP-NO, SKOS-AP-NO m.fl.) som er skrivne på bokmål. Dokumentasjonen rundt
skjemaa (README, rettleiingar) er derimot på nynorsk.

**Konsekvens:** Omsetjingsarbeidet nedanfor gjeld utelukkande dokumentasjonsfiler — ikkje
innhaldet i `.yaml`-skjema.

### Omfang

Tekstfilene (README og mkdocs) er skrivne på bokmål, nynorsk eller blanding.
Målet er at alle README-filer og det eine mkdocs-dokumentet er konsekvent på nynorsk.

---

## Filstatus

### Gruppe A — Ferdig nynorsk (ingen endring nødvendig)

| Fil | Merknad |
|---|---|
| `examples/README.md` | Nynorsk |
| `mkdocs/README.md` | Nynorsk |
| `src/linkml/README.md` | Nynorsk |
| `src/mcp-linkml-generator/README.md` | Fullstendig nynorsk |
| `src/mcp-linkml-validator/README.md` | Fullstendig nynorsk |

### Gruppe B — Korte filer, enkle å omsetje (5–10 min kvar)

| Fil | Omfang | Bokmålsinnslag |
|---|---|---|
| `specs/README.md` | 2 liner | «dokumenterer» (ok), «endringer» → «endringar» |
| `src/README.md` | 3 liner | «kildekoden» → «kjeldekoden», «ligg» er alt nynorsk |
| `src/assets/README.md` | 2 liner | «kildekode» → «kjeldekode», «brukt» ok, «kommandoer» → «kommandoar» |
| `src/templates/docgen/README.md` | 3 liner | «benyttes» → «brukast», «templates» ok (teknisk) |
| `tests/README.md` | 2 liner | «testkode» ok, «hjelpemidler» → «hjelpemiddel» |
| `tmp/README.md` | 4 liner | «artefakter» → «artefaktar», «flyttes» → «flytjast» |

### Gruppe C — Store filer, hovudarbeid (30–60 min kvar)

| Fil | Omfang | Status |
|---|---|---|
| `README.md` | ~133 liner | Bokmål gjennomgåande |
| `mkdocs/docs/ny-domenemodell.md` | ~184 liner | Mest nynorsk, nokre restar |

> **`mkdocs/docs/index.md` oppdaterast ikkje direkte** — han vert generert automatisk frå
> `README.md` ved bygg. Det er tilstrekkeleg å omsetje `README.md`.

---

## Ordbok — gjeldande omsetjingar

Desse bokmålsformene finst i filene og skal omsetjast konsekvent:

| Bokmål | Nynorsk |
|---|---|
| ikke | ikkje |
| inneholder | inneheld |
| inneholde | innehalde |
| tilgjengelig(e) | tilgjengeleg(e) |
| kommandoene | kommandoane |
| kommandoer | kommandoar |
| verdier | verdiar |
| artefakter | artefaktar |
| generatorer | generatorar |
| skjemaer | skjema (uendra fleirtal) |
| forutsetninger | føresetnader |
| åpen-kildekode / åpen kildekode | open kjeldekode |
| kildekode | kjeldekode |
| hjelpemidler | hjelpemiddel |
| nedenfor | nedanfor |
| modelleringsprinsipper | modelleringsprinsipp |
| Beskrivelse (kolonneoverskrift) | Skildring |
| selvstendige | sjølvstendige |
| relasjoner | relasjonar |
| dine egne | dine eigne |
| ønskelig | ønskeleg |
| midlertidige | mellombelse |
| benyttes | brukast |
| skrives | skrivast |
| flyttes | flytjast |
| menneskelig | menneskeleg |
| egenskaper / egenskapar | eigenskapar |
| veiledning | rettleiing |
| kode-arkivet / kode-repositoryet | kodelageret |
| én gang | éin gong |

**Bevar uendra:** tekniske termar, produktnamn, kommandoar, URL-ar, kodeblokkinnhald.

---

## Spesifikke endringar per fil

### `README.md` (rot)

Alle avsnitt er på bokmål. Omsetje heile fila. Hovudendringar:

- Ingress: «åpen-kildekode modelleringsspråk» → «open kjeldekode-modelleringsspråk»;
  «inneholder» → «inneheld»
- «Kom i gang»: «Forutsetninger» → «Føresetnader»; «nedenfor» → «nedanfor»;
  «dine egne verdier» → «dine eigne verdiar»; «ønskelig» → «ønskeleg»;
  «tilgjengelige kommandoer» → «tilgjengelege kommandoar»
- «Domener»-tabell: «Beskrivelse» → «Skildring» (kolonneoverskrift)
- «Skjemaer»-tabell: «selvstendige» → «sjølvstendige»; overskrift → «Skjema»
- «Genererte artefakter»-seksjonen: «artefakter» → «artefaktar» gjennomgåande;
  «relasjoner» → «relasjonar»; «menneskelig» → «menneskeleg»
- «Katalogstruktur»: «kildekode» → «kjeldekode»; «Midlertidige filer» → «Mellombelse filer»

### `mkdocs/docs/ny-domenemodell.md`

Allereie mest nynorsk. Gjenverande restar:

- Linje 160: «**Norsk bokmål** — alle klassenamn, slotnamn og skildringer skrives på bokmål.»
  → «…og skildringar skrivast på bokmål.»
- Kontroller: alle «egenskapar» → «eigenskapar»; «relasjoner» → «relasjonar» (om dei finst)

### `specs/README.md`

```
# ./specs
Her dokumenterer vi større endringar i repoet ved hjelp av endringsplanar genererte av KI.
```
(«endringer» → «endringar»; «vha» → «ved hjelp av»)

### `src/README.md`

```
# ./src
Her har vi all kjeldekoden i repoet (utenom tester som ligg i /tests og Makefile som ligg på rot)
```
(«kildekoden» → «kjeldekoden»; «root» → «rot»)

### `src/assets/README.md`

```
# ./src/assets
Her har vi diverse kjeldekode brukt i samband med LinkML-kommandoar.
```
(«kildekode» → «kjeldekode»; «ifbm» → «i samband med»; «kommandoer» → «kommandoar»)

### `src/templates/docgen/README.md`

```
# ./src/templates/docgen
Her har vi jinja2-malar som brukast i samband med `make gen-docs`-kommandoen som genererer
markdown-dokumentasjon av ein (eller alle) LinkML-modellar.
Vi har nytta jinja2-malar for å gruppere klasser etter obligatorisk, anbefalt og valgfri
i markdown-dokumentasjonen.
```
(«templates» → «malar»; «benyttes» → «brukast»; «benytta» → «nytta»)

### `tests/README.md`

```
# ./tests
Her har vi all testkode og hjelpemiddel for å kunne køyre testar.
```
(«hjelpemidler» → «hjelpemiddel»; «kjøre» → «køyre»; «tester» → «testar»)

### `tmp/README.md`

```
# ./tmp
Her har vi artefaktar som ikkje er kjeldekode i prosjektet, men som kan nyttast i make-kommandoar.
T.d. `make json2linkml-generate SCHEMA=/tmp/person.json`.

Dersom ein generert LinkML-modell i ./tmp-katalogen skal arbeidast vidare med og bli ein offisiell
modell, må han flytjast til ./src/linkml/..
```
(«artefakter» → «artefaktar»; «kildekode» → «kjeldekode»; «benyttes» → «nyttast»;
«flyttes» → «flytjast»; «offieisll» (stavefeil) → «offisiell»)

---

## Rekkjefølgje

1. **Gruppe B** — korte filer, alle seks på éin gong (lavast risiko, rask gevinst)
2. **`mkdocs/docs/ny-domenemodell.md`** — allereie nynorsk, minimal innsats
3. **`README.md`** (rot) — stort, men strukturert; omset avsnitt for avsnitt
   (`mkdocs/docs/index.md` følgjer automatisk ved neste bygg)
