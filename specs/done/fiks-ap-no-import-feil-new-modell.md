# Fiks CURIE-feil og handter gen-rdf-avgrensing for versjonslåst AP-NO-import

## Bakgrunn

Den scaffolda modellen `src/linkml/oreg/lunchregisteret/` (ikkje committa,
laga med `make new-modell`) reproduserer **to separate feil**, begge med rot
i det same versjonslåste `raw.githubusercontent.com`-importet av
`dcat-ap-no-schema` som `new-modell.sh` set inn som standard:

**Feil 1 — `gen-rdf` (CI, `make domain-oreg`):**

```
[ERROR] ::error file=src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml
::rdf feila for oreg/lunchregisteret (3.42s) — HTTP Error 404: Not Found
make[1]: *** [make/11-generator-targets.mk:36: gen-rdf] Error 1
```

**Feil 2 — `roundtrip-json`/`roundtrip-ttl` (`make roundtrip`):**

```
[ERROR] ::error file=.../lunchregisteret-schema.yaml::convert feila
(.../lunchregisteret-eksempel.yaml → tmp/roundtrip-json/lunchregisteret/a.json)
— Unknown CURIE prefix: https
```

Dei to andre `oreg`-modellane (`enhetsregisteret-bvrinn`,
`register-over-aksjeeiere`) råkast ikkje av nokon av feila — begge
importerer berre `linkml:types`, ingen AP-NO-profil.

**Retningsval:** versjonslåste URL-importar (git-tag-pinna
`raw.githubusercontent.com`-importar) skal **framleis vere eit fullt
støtta mønster** — dei skal ikkje bytast bort til fordel for relativ sti.
Scope er avgrensa til **vår eigen lokale/CI-generering** (`make`-måla i
dette repoet), ikkje til å gjere ting fungere for eksterne forbrukarar som
sjølv køyrer generatorar mot våre publiserte skjema via den pinna URL-en.

## Reprodusert og isolert

**Feil 1** — direkte traceback (utanom `batch-generate.py` sin
eittlinje-feilhandtering) stadfestar rotårsaka:

```python
>>> from linkml.generators.rdfgen import RDFGenerator
>>> RDFGenerator('src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml').serialize()
...
File ".../rdfgen.py", line 64, in end_schema
    graph.parse(data=jsonld_str, format="json-ld", ...)
...
File ".../rdflib/plugins/shared/jsonld/context.py", line 481, in _fetch_context
    source_json, _ = source_to_json(source_url)
...
urllib.error.HTTPError: HTTP Error 404: Not Found
```

`RDFGenerator.end_schema()` byggjer JSON-LD internt via `JSONLDGenerator`,
som i `end_schema()` (linkml, `jsonldgen.py`) **ubetinga** legg til éin
`@context`-URL per import i importgrafen:

```python
for imp in list(self.loaded.values())[1:]:
    context.append(imp[0] + ".context.jsonld")
```

`imp[0]` er den oppløyste importstrengen (her: den pinna
`raw.githubusercontent.com`-URL-en). `rdflib` sin JSON-LD-parser **fetchar
denne URL-en over nettverk** når grafen vert parsa — stadfesta 404 med
`curl -I` mot den konstruerte URL-en.

**Feil 2** — allereie reprodusert og analysert som **BUG-15**
(`bugs/relativ-import-via-versjonslast-url.md`): `SchemaView.imports_closure()`
i `linkml_runtime` brukar filsystem-semantikk (`pathlib.Path`/
`os.path.normpath`) til å løyse relative importar i eit allereie importert
skjema. Når skjemanamnet er ein full URL, kollapsar `pathlib.Path` `https://`
til `https:/`, og det etterfølgjande CURIE-oppslaget feilar med
`Unknown CURIE prefix: https`.

Stadfesta **pre-eksisterande** (ikkje innført av
`specs/done/fjern-lokale-subsets-new-modell.md`): same feiltekst dukka opp i
`make lint` på det same skjemaet før subsets-fiksen vart gjord.

## Rotårsak

### Feil 1 er isolert til nett `rdfgen` — ikkje eit generelt importoppløysingsproblem

Undersøkt direkte i `linkml.converter.cli:cli` (koden bak `linkml-convert`,
som `batch-convert.py` brukar for `roundtrip-ttl`/`convert-rdf`): når
output-format er `rdf`/`ttl`, byggjer han ein `SchemaView` og kallar
`get_dumper("ttl").dump(obj, output, schemaview=sv)` — ein **heilt annan**
kodeveg (`linkml_runtime`-dumparane) enn `RDFGenerator.end_schema()`, og
**ikkje** ramma av `.context.jsonld`-konstruksjonen over.

Stadfesta empirisk mot den same `lunchregisteret`-scaffolden: `gen-python`,
`gen-jsonschema`, `gen-owl`, `gen-proto`, `gen-graphql`,
`gen-jsonld-context`, `gen-shacl` og `gen-plantuml` genererer **alle**
problemfritt for eit skjema med versjonslåst URL-import. **Berre** `gen-rdf`
(via `RDFGenerator`/`JSONLDGenerator`) feilar.

Årsaka: `.context.jsonld`-filer er byggoutput (`make gen-jsonld-context`),
skrivne til `generated/`, som er heilt `.gitignore`-a — dei finst aldri i
git-historia. `JSONLDGenerator` føreset derimot at ei
`<import>.context.jsonld`-fil ligg **rett ved sida av** kvart importert
skjema sin kjeldeplassering — ei føresetnad som held for LinkML-prosjekt
som publiserer genererte artefakt saman med kjeldekoden, men ikkje for
dette repoet sitt skilje mellom kjeldekode og byggoutput. Sjølv om ei slik
fil fanst der, ville filnamnet uansett ikkje matche: LinkML konstruerer
alltid `<importnamn> + ".context.jsonld"` (**punktum**), medan
`batch-generate.py` sin `REGISTRY` (out_suffix `"context.jsonld"`) alltid
produserer `<schema>-context.jsonld` (**bindestrek**) — to uavhengige
mismatchar, ikkje éin.

Å byggje eit lokalt sti-omskrivings- og namngjevingsoppsett spesifikt for å
lure `RDFGenerator` til å finne ei korrekt plassert/namngjeven fil vart
vurdert (sjå tidlegare versjon av denne specen), men er uforholdsmessig
komplekst for éin einaste generator når problemet enkelt kan **avgrensast
eksplisitt** i staden — sjå Tiltak.

### Feil 2: BUG-15 manglar patch i ein 6. kallstad

BUG-15 er allereie kjend og har ein monkeypatch-workaround
(`src/assets/scripts/utils/linkml_relative_import_patch.py`, funksjonen
`apply()`), kalla frå **fem** stader der `SchemaView` vert bygd direkte eller
transitivt: `src/mcp-linkml-validator/server.py`,
`batch-linkml-validate.py`, `gen-modelldcat-elements.py`,
`validate-modelldcat.py`, `batch-generate.py`.

`src/assets/scripts/makefile/batch-convert.py` — som driv **Kategori D**:
`convert-rdf`, `roundtrip-json` og `roundtrip-ttl` (kalla frå
`tests/test_make.sh:383`, brukt av `make roundtrip`) — kallar
`linkml.converter.cli:cli` direkte, som internt byggjer sin eigen
`SchemaView` via same buggy `imports_closure()`. Denne fila var **ikkje** med
i lista over patcha kallstader då BUG-15 vart dokumentert og fiksa. Dette er
ein **enkel, velprøvd** fiks — same 3-linjers mønster som alt fungerer på
dei fem andre kallstadene — og løyser roundtrip/convert-rdf fullstendig,
utan behov for nokon skip/guard-logikk.

## Tiltak

### Del 1 — handter gen-rdf-avgrensinga eksplisitt (Feil 1)

| # | Tiltak | Fil |
|---|---|---|
| 1 | Legg til hjelpefunksjonen `schema_has_versioned_import(schema_path)` i `batch-generate.py` — les schemaet sin `imports:`-liste (yaml.safe_load) og returnerer `True` dersom nokon oppføring inneheld `"://"` | `src/assets/scripts/makefile/batch-generate.py` |
| 2 | Utvid `GeneratorSpec`-dataklassen med feltet `skip_if_versioned_import: bool = False`, sett til `True` berre for `REGISTRY["rdf"]` | `src/assets/scripts/makefile/batch-generate.py` |
| 3 | I `main()`: for generatorar med `skip_if_versioned_import=True`, filtrer `enabled`-lista i to før hovudløkka — skjema med versjonslåst import vert **hoppa over** (ikkje forsøkt), med ei tydeleg, ikkje-stille loggline (t.d. `HOPPAR OVER rdf for oreg/lunchregisteret — versjonslåst URL-import, sjå bugs/gen-rdf-manglar-stotte-for-versjonslaste-importar.md (BUG-17)`). Dette skal **ikkje** telje som `failed` — returkode skal vere 0 for eit domene der einaste "feil" er slike hopp-over | `src/assets/scripts/makefile/batch-generate.py` |
| 4 | Opprett `bugs/gen-rdf-manglar-stotte-for-versjonslaste-importar.md` som **BUG-17** — dokumenter symptom, rotårsak (frå analysen over: hardkoda `.context.jsonld`-URL-konstruksjon i `JSONLDGenerator.end_schema()`, kombinert med at `generated/` er `.gitignore`-a og at namnekonvensjonane uansett ikkje matchar), status `workaround` (denne skip-logikken), komponent `linkml` (`RDFGenerator`/`JSONLDGenerator`), affected: alle skjema med `rdf: true` og minst eitt versjonslåst URL-import | `bugs/gen-rdf-manglar-stotte-for-versjonslaste-importar.md` |
| 5 | Legg BUG-17 til i `BUGS.md` sin indekstabell og under «Generatorar»-seksjonen | `BUGS.md` |
| 6 | Stadfest empirisk (`make docs-build`) at mkdocs sin «Generated artifacts»-tabell hoppar over `schema.ttl`-rada gracefully når fila manglar — koden i `publish.sh` linje 436-441 sjekkar alt `[ -f ... ]` før han listar kvar artefakttype, så inga kodeendring er venta naudsynt her, berre stadfesting | — |

### Del 2 — legg til manglande BUG-15-patch i batch-convert.py (Feil 2)

| # | Tiltak | Fil |
|---|---|---|
| 7 | Legg til `sys.path.insert(...)` + `import linkml_relative_import_patch` + `linkml_relative_import_patch.apply()` i `batch-convert.py`, identisk mønster som `batch-generate.py` (linje 66-70) | `src/assets/scripts/makefile/batch-convert.py` |
| 8 | Legg `batch-convert.py` til i lista over patcha kallstader i `bugs/relativ-import-via-versjonslast-url.md` (BUG-15) sin «Workaround»-seksjon | `bugs/relativ-import-via-versjonslast-url.md` |

### Del 3 — verifisering (samla)

| # | Tiltak |
|---|---|
| 9 | `make gen-rdf SCHEMA=src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml` — skal no vise ei `HOPPAR OVER`-melding og returnere 0, ikkje feile |
| 10 | `make domain-oreg` — full pipeline grøn (rdf-steget hoppar over `lunchregisteret`, feilar ikkje lenger domenet som heilskap) |
| 11 | `make roundtrip SCHEMA=src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml` — grøn (frå Del 2, ingen skip naudsynt her) |
| 12 | `make gen-rdf DOMAIN=ap-no` (og eit anna domene utan versjonslåste importar, t.d. `referanse`) — stadfest ingen regresjon, genererer framleis normalt |
| 13 | Køyr full `make test` for å stadfeste ingen regresjon andre stader |

## Referanse

- `bugs/relativ-import-via-versjonslast-url.md` (BUG-15) — full rotårsaksanalyse og patch-mekanisme for Feil 2
- `src/assets/scripts/utils/linkml_relative_import_patch.py` — den eksisterande patchen (`apply()`, idempotent)
- `src/assets/scripts/makefile/batch-generate.py:66-70` — referansemønster for korleis BUG-15-patchen skal kallast
- `mkdocs/publish.sh:436-441` — eksisterande `[ -f ... ]`-vakt som gjer manglande `schema.ttl`-artefakt trygt for dokumentasjonsgenereringa
- `specs/done/new-modell-genererer-gyldig-eksempel.md` — der det versjonslåste importmønsteret i `new-modell.sh` opphaveleg vart innført
- `specs/done/fjern-lokale-subsets-new-modell.md` — der Feil 1 og Feil 2 først vart observert (utanfor scope der)

## Utført

Alle 13 opphavlege tiltak gjennomførte, pluss to tilleggsfunn oppdaga under
full `make test`-verifisering (tiltak 13) som kravde tilsvarande små,
same-mønster-fiksar:

**Del 1 (Feil 1 — gen-rdf):**
1-3. `schema_has_versioned_import()` + `skip_if_versioned_import`-felt +
   filtrering/logging lagt til i `batch-generate.py`. Verifisert: `make
   gen-rdf SCHEMA=.../lunchregisteret-schema.yaml` skriv no
   `HOPPAR OVER rdf for oreg/lunchregisteret — ...` og returnerer 0.
4-5. `bugs/gen-rdf-manglar-stotte-for-versjonslaste-importar.md` oppretta
   som **BUG-17**, lagt til i `BUGS.md` (indeks + «Generatorar»-seksjon).
6. Stadfesta via kodelesing (`publish.sh:436-441`) at manglande
   `schema.ttl` handterast gracefully — ingen full `make docs-build` køyrt
   (heile-repoet-operasjon, uforholdsmessig tungt for denne stadfestinga).

**Tillegg oppdaga under verifisering:** `tests/test_make.sh` sin
`test_gen_rdf()`-funksjon kjente ikkje til det nye, tilsikta hoppet, og
rapporterte difor `gen-rdf (lunchregisteret)` som **FEILA** (ikkje hoppa
over) i `make test`. Retta ved å leggje til ei skip-betingelse i
`test_gen_rdf()` (namnebasert `case`, same mønster som BUG-1/BUG-2 sine
skip-betingelsar), referert til BUG-17. Verifisert isolert:
`gen-rdf (lunchregisteret)` → OK.

**Del 2 (Feil 2 — BUG-15/CURIE):**
7-8. Patch-kall lagt til i `batch-convert.py`, `bugs/relativ-import-via-versjonslast-url.md`
   oppdatert med den nye kallstaden. Verifisert isolert:
   `roundtrip-json (lunchregisteret)` → OK (CURIE-krasjen er borte).

**Tillegg oppdaga under verifisering:** Full `make test` synte at
`linkml-lint (lunchregisteret)` **òg** feila med `Unknown CURIE prefix:
https` — ein **sjuande, tidlegare ukjend kallstad** for BUG-15:
`src/assets/scripts/makefile/batch-lint.py` (brukt av `linkml-lint`-testen,
byggjer `Linter` direkte) hadde ikkje patchen. Retta med identisk
patch-kall, og lagt til i `bugs/relativ-import-via-versjonslast-url.md` sitt
workaround-avsnitt. Verifisert isolert: `linkml-lint (lunchregisteret)` → OK.

**Del 3 (verifisering):**
9-10. `make gen-rdf`/`make domain-oreg` for `lunchregisteret` — grøn, ingen
   regresjon i resten av `oreg`-domenet.
11. `make roundtrip SCHEMA=.../lunchregisteret-schema.yaml` isolert:
   `roundtrip-json` → **OK**. `roundtrip-ttl` → **framleis FEIL**, men no ei
   **anna, ny og distinkt** feilmelding enn BUG-15 sitt krasj: eit
   innhaldsavvik der `id`-verdien kjem attende som CURIE
   (`lunchregisteret:eksempel-1`) i staden for full URI
   (`https://data.norge.no/oreg/lunchregisteret/eksempel-1`) etter
   TTL-roundtrip. Dette var maskert av CURIE-krasjen tidlegare og er **ute
   av scope** for denne specen (som galdt å fjerne krasjen, ikkje full
   byte-for-byte roundtrip-truskap) — kandidat for eiga spec/bug-oppføring
   om ønskt.
12. `make gen-rdf SCHEMA=referansemodell` (skjema utan versjonslåst import)
   — stadfesta ingen regresjon, genererer normalt (ikkje hoppa over).
13. Full `make test` køyrt (562 OK, 34 feil). Dei to feila som direkte
   gjaldt denne specen (`gen-rdf`/`linkml-lint` for `lunchregisteret`) er no
   retta (sjå tilleggsfunna over). Dei resterande ~30 feila
   (`roundtrip-json`/`roundtrip-ttl` for ei rekkje **urelaterte** skjema —
   `fint-*`, `ngr-*`, `*-modellkatalog`, `samt-bu`, `brreg-begrepskatalog`,
   ingen av dei brukar versjonslåste importar) synte eit mønster
   (`FileNotFoundError` for filer som synleg vart oppretta tidlegare i
   same logg) som tyder på ein **pre-eksisterande race condition** mellom
   Fase A (sekvensiell batch-konvertering) og Fase B (parallelle
   per-skjema-testar) i `tests/test_make.sh` sin roundtrip-orkestrering —
   stadfesta IKKJE knytt til endringane i denne specen (skjemaa er
   urelaterte, og koden som vart endra her rører ikkje `tmp/`-handtering
   eller fase-synkronisering). Ikkje undersøkt vidare eller retta — utanfor
   scope, kandidat for eiga spec om ønskt.
