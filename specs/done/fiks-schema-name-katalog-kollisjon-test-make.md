# Fiks schema_name()-kollisjon for samlokaliserte AP-NO-profilskjema i test_make.sh

## Bakgrunn

Brukaren la merke til at `make test` sin terminalutskrift viste
tilsynelatande dupliserte loggliner — same testnamn ("validate
(modelldcat-ap-no)", "validate (dqv-ap-no)") dukka opp fleire gonger på
rad. Undersøking synte at dette **ikkje** er dupliserte testkøyringar, men
eit rotårsaks-namnekollisjonsproblem: tre ulike skjemafiler vert alle
viste med det same, feilaktige namnet.

## Rotårsak — stadfesta empirisk

`schema_name()` (`tests/test_make.sh:50`) hentar «namnet» til eit skjema
frå **katalogen** det ligg i, ikkje frå filnamnet:

```bash
schema_name()   { echo "$1" | cut -d/ -f4; }
```

Dette held for det vanlege mønsteret (éin `<modell>-schema.yaml` per
katalog, katalognamn == filnamn), men **to AP-NO-katalogar** bryt denne
føresetnaden ved å samlokalisere fleire, sjølvstendige skjemafiler:

```
src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml
src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml
src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml
src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml
src/linkml/ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml
```

`schema_name()` returnerer `"dqv-ap-no"` for **begge** filene i den fyrste
katalogen, og `"modelldcat-ap-no"` for **alle tre** i den andre — difor dei
tilsynelatande dupliserte logglinjene.

Til samanlikning brukar `batch-generate.py` (Python-sida, `gen-*`-generering)
allereie den **korrekte** metoden — filnamn-basert, ikkje katalog-basert:

```python
def schema_domain_name(schema: str) -> tuple[str, str]:
    domain = schema.split("/")[2]
    name = re.sub(r"-schema$", "", Path(schema).stem)
    return domain, name
```

`metadata/`-katalogen i begge dei råka AP-NO-katalogane har òg **allereie**
per-skjema-korrekte filnamn (`dqv-ap-no-manifest.yaml` **og**
`dqv-core-manifest.yaml`, `modelldcat-ap-no-manifest.yaml` **og**
`modelldcat-katalog-manifest.yaml` **og** `modelldcat-modell-manifest.yaml`)
— stadfestar at samlokalisering er eit medvite, etablert mønster i
kjeldetreet, berre `schema_name()` i test_make.sh har ikkje halde tritt.

## Konsekvens — dette er meir enn ein visningsfeil

`schema_outdir()` og eksempelfil-stien vert bygde frå same kolliderande
`$name`, så for `dqv-core-schema.yaml` reknar test-suiten ut
`generated/ap-no/dqv-ap-no/dqv-ap-no-model.py` som forventa output-fil —
**søskenet** sin fil, ikkje sin eigen. Sidan den fila finst (korrekt
generert for `dqv-ap-no-schema.yaml`), rapporterer sjekken **OK** utan
nokon gong å ha sett på `dqv-core` sin eigen output — ein falsk positiv.

Kartlegging av alle 17 Fase B-sjekkane, etter kategori:

| Kategori | Sjekkar | Konsekvens |
|---|---|---|
| **Trygt** (nøkla på full skjemasti via `phase_a_check`, ikkje `$name`) | `validate`, `linkml-lint` | Ingen — desse identifiserer alltid rett skjema |
| **Hoppar over uansett** (`ap-no`/`fair` manglar `tree_root`) | `roundtrip-json`, `roundtrip-ttl`, `convert-rdf`, `mcp-validate-instance` | Ingen praktisk konsekvens for dei 5 råka skjemaa i dag, men koden er framleis feil i prinsippet |
| **Falsk positiv-risiko** (`$outdir/$name-<suffiks>` kolliderer) | `gen-jsonld`, `gen-python`, `gen-jsonschema`, `gen-rdf`, `gen-erdiagram`, `gen-docs`, `gen-shacl`, `gen-owl`, `gen-proto`, `gen-plantuml` | Sjekkar **søskenet** sin fil — stadfestar aldri at `dqv-core`/`modelldcat-katalog`/`modelldcat-modell` sin eigen genererte output faktisk finst/er gyldig |
| **Feil valideringsmål** | `linkml-validate` | Validerer mot `tests/fixtures/dqv-ap-no-fixture.yaml` (søskenet sin fixture) i staden for eit `dqv-core`-spesifikt fixture, som ikkje finst |

Kort sagt: **11 av 17 sjekkar** har aldri faktisk stadfesta noko om
`dqv-core`, `modelldcat-katalog` eller `modelldcat-modell` sin eigen
genererte output — dei har stille re-sjekka eit tilfeldig eksisterande
søskenskjema sin fil i staden.

## Løysingsdesign

Splitt det semantisk overlessa `$name`/`schema_name()`-omgrepet i to:

```bash
# Fila sin eigen, unike basisnamn (filnamn utan -schema.yaml) — identifiserer
# DETTE skjemaet eintydig, sjølv når fleire skjema er samlokaliserte i same
# katalog. Brukt for genererte artefaktnamn/utdatakatalog og visingsnamn i
# testutskrifta. Matchar batch-generate.py sin schema_domain_name().
schema_name() {
    local base
    base=$(basename "$1" .yaml)
    echo "${base%-schema}"
}

# Kjeldekatalognamnet (4. sti-komponent) — brukt KUN til å finne DELTE
# per-katalog-ressursar (examples/<katalog>-eksempel.yaml,
# tests/fixtures/<katalog>-fixture.yaml) når fleire skjema er
# samlokaliserte (AP-NO-profilfamiliar).
schema_dir_name() { echo "$1" | cut -d/ -f4; }
```

For **32 av 35** skjema (normalmønsteret, éin fil per katalog) er
`schema_name()` og `schema_dir_name()` identiske — **null åtferdsendring**
for desse. Berre dei 5 samlokaliserte skjemaa (2+3) får korrekt,
distinkt identitet.

**Viktig presisering:** sidan `schema_name()` sjølv vert retta, treng
**ingen** kallstader som brukar han for artefaktnamn/utdatakatalog/
visingsnamn/BUG-lister endrast i det heile — dei vert automatisk korrekte.
Berre kallstader som **finn delte ressursar** (eksempelfil, fixture-fil)
må eksplisitt byte til den nye `schema_dir_name()`.

## Tiltak

| # | Tiltak | Fil |
|---|---|---|
| 1 | Endre `schema_name()` til filnamn-basert (sjå design over) | `tests/test_make.sh:50` |
| 2 | Legg til ny `schema_dir_name()` (gamal `schema_name()`-logikk) | `tests/test_make.sh` |
| 3 | Byt alle **eksempelfil-sti-konstruksjonar** (`"src/linkml/$domain/$name/examples/$name-eksempel.yaml"`) til å bruke `schema_dir_name()` for **begge** `$name`-førekomstane (katalog OG filnamn-prefiks — filene heiter t.d. `dqv-ap-no-eksempel.yaml`, ikkje `dqv-core-eksempel.yaml`): `mcp_instance_job()` (linje 67), `run_schema_tests()` (linje 215), `run_phase_a_convert_rdf()` (linje 468), `run_phase_a_roundtrip_json()` (linje 495), `run_phase_a_roundtrip_ttl()` (linje 524), `run_phase_a_linkml_validate()` (linje 554), `test_linkml_validate()` (linje 801) | `tests/test_make.sh` |
| 4 | Byt alle **fixture-sti-konstruksjonar** (`tests/fixtures/$name-fixture.yaml`) til `schema_dir_name()`: `mcp_instance_job()` (linje 70), `linkml_validate_job()` (linje 136), feilmelding i `test_linkml_validate()` (linje 807) | `tests/test_make.sh` |
| 5 | **Trådingsdetalj:** dei `*_job()`-hjelpefunksjonane (`mcp_instance_job`, `linkml_validate_job`, `convert_rdf_job`, `roundtrip_json_job`, `roundtrip_ttl_job`) tek `$name` som **parameter** frå kallaren — kallarane (`run_schema_tests()`, `run_phase_a_*()`) må sende `$(schema_dir_name "$schema")` til desse funksjonskalla spesifikt (sidan jobbfunksjonane sin einaste bruk av `$name` er å finne delte ressursar), samstundes som kallaren sin EIGEN `$name`-variabel (brukt til `$outdir`/visingsnamn) held fram som den no filnamn-baserte verdien. Krev ei eiga, forsiktig gjennomgang av kvar kallstad — ikkje ei mekanisk søk-og-byt, sidan same variabelnamn (`$name`) no må bety to ulike ting avhengig av kontekst | `tests/test_make.sh` |
| 6 | Verifiser at `schema_outdir()` for `dqv-core-schema.yaml`/`modelldcat-katalog-schema.yaml`/`modelldcat-modell-schema.yaml` no gjev **same** katalog som `batch-generate.py` sin `schema_domain_name()` faktisk skriv til (`generated/ap-no/dqv-core/` osv., ikkje `generated/ap-no/dqv-ap-no/`) | — |
| 7 | Verifiser at terminalutskrifta no viser **distinkte** namn for alle 5 tidlegare-kolliderande skjema (ikkje lenger duplikat-utsjåande linjer) | — |
| 8 | Verifiser at `linkml-validate` for dei 3 nye-namngjevne AP-NO-underskjemaa no **hoppar over** (manglande `dqv-core-fixture.yaml` osv.) i staden for å validere mot søskenet sitt fixture — dette er ei **forbetring** (tydeleg hopp-over-grunngjeving beat stille feil-validering), sjølv om det reduserer talet på faktisk utførte valideringar inntil eigne fixture-filer eventuelt vert skrivne (eige, separat, domenekunnskap-tiltak — ikkje del av dette) | — |
| 9 | Full `make test` — stadfest at dei 5 tidlegare-kolliderande skjemaa sine `gen-*`-sjekkar no faktisk validerer sin EIGEN output (ikkje søskenet sin), og at det totale resultatsettet elles er uendra for dei resterande 30 skjemaa | — |
| 10 | `bash -n tests/test_make.sh` (syntakssjekk) | — |

## Ute av scope

- **Å skrive dedikerte `tests/fixtures/dqv-core-fixture.yaml`/
  `modelldcat-katalog-fixture.yaml`/`modelldcat-modell-fixture.yaml`** for å
  gjenvinne full `linkml-validate`-dekning for desse tre skjemaa krev
  domenekunnskap om kva gyldige instansar av kvart delskjema ser ut som —
  ein eigen oppfølgingsspec, ikkje ein mekanisk kodefiks.
- Same vurdering for eventuelle framtidige dedikerte eksempelfiler
  (`dqv-core-eksempel.yaml` osv.) dersom ein seinare ønskjer å aktivere
  roundtrip/convert-rdf/mcp-validate-instance for desse (som uansett
  hoppar over på grunn av manglande `tree_root` i AP-NO-profilar, uavhengig
  av namnefiksen).

## Utført

Alle 10 tiltak gjennomførte og verifiserte:

1-2. `schema_name()` retta til filnamn-basert (`basename ... .yaml`, strip
   `-schema`-suffiks); ny `schema_dir_name()` med den gamle,
   katalog-baserte logikken lagt til.
3. Alle eksempelfil-sti-konstruksjonar (`mcp_instance_job()`,
   `run_schema_tests()`, `run_phase_a_convert_rdf()`,
   `run_phase_a_roundtrip_json()`, `run_phase_a_roundtrip_ttl()`,
   `run_phase_a_linkml_validate()`, `test_linkml_validate()`) bytte til
   `schema_dir_name()` for begge `$name`-førekomstane i stien.
4. Alle fixture-sti-konstruksjonar (`linkml_validate_job()`,
   `test_linkml_validate()` sin feilmelding) bytte til `schema_dir_name()`.
5. `mcp_instance_job()` og `linkml_validate_job()` omskrivne til å
   utleie kjeldekatalognamnet **internt** frå `$schema` (i staden for å
   stole på at kallaren sender rett variant av `$name`) — gjer dei
   sjølvstendig korrekte uavhengig av kva kallaren sin eigen `$name`
   tyder. `mcp_instance_job()` sitt no ubrukte `$name`-parameter vart
   fjerna, og dei to kallstadene oppdaterte til 2-argument-kall.
6. Verifisert: `schema_outdir()` for `dqv-core`/`modelldcat-katalog`/
   `modelldcat-modell` gjev no `generated/ap-no/<eige-namn>/` — stadfesta
   identisk med kva `batch-generate.py` faktisk skriv til (`ls generated/ap-no/`
   viser separate katalogar for alle fem tidlegare-kolliderande skjema).
7. Verifisert: full `make test` viser no distinkte visingsnamn for alle
   fem (`dqv-ap-no`, `dqv-core`, `modelldcat-ap-no`, `modelldcat-katalog`,
   `modelldcat-modell`) — ikkje lenger duplikat-utsjåande linjer.
8. **Presisering av opphavleg overslag:** spec-teksten antok at
   `linkml-validate` for dei tre nye-namngjevne skjemaa ville hoppe over
   (manglande dedikert fixture). Verifisert **feil** — sidan
   `linkml_validate_job()` sin fixture-oppslag alt vart eksplisitt sett
   til å bruke `schema_dir_name()` (delt per katalog, jf. tiltak 4),
   finn han framleis **same delte fixture**
   (`tests/fixtures/dqv-ap-no-fixture.yaml` osv.) som før fiksen — og
   sidan den gamle, buggy `schema_name()` **alt var** katalog-basert,
   var denne konkrete åtferda **uendra** av heile fiksen (verken før
   eller etter brukte `linkml-validate` noko anna enn det delte
   fixture-et for desse skjemaa). `linkml-validate` høyrer difor **ikkje**
   heime i «Feil valideringsmål»-kategorien i denne specen sin analyse —
   det var alltid korrekt (om enn ved eit samantreff av to kompenserande
   bugs) å bruke det delte fixture-et. Dei 10 genuint retta sjekkane er
   `gen-jsonld`, `gen-python`, `gen-jsonschema`, `gen-rdf`, `gen-erdiagram`,
   `gen-docs`, `gen-shacl`, `gen-owl`, `gen-proto`, `gen-plantuml`.
9. Full `make test`: **591 OK, 5 feil** — identisk resultatsett som
   referansen, ingen regresjon. Stikkprøve stadfesta at
   `gen-python (dqv-core)`/`gen-python (modelldcat-katalog)`/
   `gen-python (modelldcat-modell)` no faktisk sjekkar sine EIGNE filer
   (`generated/ap-no/dqv-core/dqv-core-model.py` osv., stadfesta
   eksisterande på disk) — ikkje lenger søskenet sin fil.
10. `bash -n tests/test_make.sh` — syntaks OK.

## Referanse

- `tests/test_make.sh:49-51` — `schema_domain()`/`schema_name()`/`schema_outdir()`
- `src/assets/scripts/makefile/batch-generate.py` sin `schema_domain_name()` — den allereie korrekte, filnamn-baserte referanseimplementasjonen
- `src/linkml/ap-no/dqv-ap-no/`, `src/linkml/ap-no/modelldcat-ap-no/` — dei to råka, samlokaliserte katalogane
- `src/linkml/ap-no/dqv-ap-no/metadata/`, `src/linkml/ap-no/modelldcat-ap-no/metadata/` — stadfestar at per-skjema-korrekt namngjeving allereie er etablert konvensjon andre stader i same katalogar
