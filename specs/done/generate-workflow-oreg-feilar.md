# Spec: fiks `make domain-oreg`-feil for blomsterregisteret

## Bakgrunn

CI-jobben `generate domain-oreg` feilar for
`src/linkml/oreg/blomsterregisteret/blomsterregisteret-schema.yaml` med to
uavhengige feil, begge isolerte til dette eine skjemaet (dei to andre
oreg-skjemaa — enhetsregisteret-bvrinn, register-over-aksjeeiere — går
gjennom uendra):

### Feil 1: `Unknown CURIE prefix: https`
Rammar `merge`, `shacl`, `json-schema`, `owl`, `doc` — alle generatorane som
gjer full transitiv import-oppløysing (`mergeimports=True`).

Dette er BUG-15 (`bugs/relativ-import-via-versjonslast-url.md`) — kjend frå
førre økt, med monkeypatch-workaround i
`src/assets/scripts/utils/linkml_relative_import_patch.py`. Patchen vart
berre kalla frå 4 stader (`server.py`, `batch-linkml-validate.py`,
`gen-modelldcat-elements.py`, `validate-modelldcat.py`) — **ikkje** frå
`src/assets/scripts/makefile/batch-generate.py`, som er skriptet
`gen-linkml-merge`/`gen-shacl`/`gen-jsonschema`/`gen-owl`/`gen-docs` faktisk
køyrer via (`make/10-generator-macros.mk`). Same rotårsak, ny kallestad som
vart gløymd i førre fiks.

### Feil 2: `Conflicting URIs (..., ...) for item: kontaktpunkt` / `Obligatorisk`
Rammar `jsonld-context`, `python`, `proto`, `rdf`, `graphql`, `plantuml` —
generatorane som ikkje treff CURIE-bugen direkte, men som slår saman
importkjeda på namn (via `linkml.utils.mergeutils.merge_schemas`, sjølve
DRY-mekanismen for import).

`blomsterregisteret-schema.yaml` deklarerte sine eigne topplevel-element som
kolliderer med element alt definerte i importkjeda, med ulik definisjon frå
to ulike skjema (`from_schema`-URI) — noko LinkML sin import-merge ikkje kan
forsone:
- `kontaktpunkt`-slot (linje 58-61, `range: uriorcurie`) vs. den alt
  definerte i `dcat-ap-no-schema.yaml` (`range: Kontaktopplysning`)
- `subsets: Obligatorisk/Anbefalt/Valgfri` (linje 31-37) vs. dei alt
  definerte i `common-ap-no-schema.yaml` (importert transitivt via
  dcat-ap-no-schema)

Ingen av desse var brukt av nokon klasse i fila — reine restar frå
mcp-linkml-generator-utkastet, i strid med DRY-importhierarkiet
(CLAUDE.md § LinkML Importhierarki).

### Feil 3 (dukka opp etter Feil 1+2 var fiksa): `rdf` — `HTTP Error 404: Not Found`
Éin attverande feil etter Feil 1+2 var retta: `gen-rdf` for blomsterregisteret
feila med ein ekte HTTP 404 (ikkje ein linkml-bug). Rotårsak: `RDFGenerator`
(via `JSONLDGenerator.end_schema()` i `linkml/generators/jsonldgen.py`)
appenderer automatisk `<importert-skjemanamn> + ".context.jsonld"` til
JSON-LD-`@context`-lista for kvart importert skjema, og `rdflib` sin
JSON-LD-parser **hentar** denne URL-en over nett for å ekspandere dokumentet.
Når det importerte skjemanamnet er ein full URL (versjonslåst import), vert
dette ein ekte, fetchbar HTTPS-URL — men `dcat-ap-no-schema.context.jsonld`
er aldri publisert i `src/linkml/ap-no/dcat-ap-no/` (kontekstfiler er
byggoutput i `generated/`, med anna namnemønster: `-context.jsonld`, ikkje
`.context.jsonld`) → 404. Ved **relative** importar er det appenderte
strengen ikkje ein absolutt URI, så `rdflib` sin JSON-LD-prosessor prøver
aldri å hente han — difor råka berre blomsterregisteret dette.

Djupare årsak: `mkdocs/docs/arkitektur/importhierarki.md` seier eksplisitt at
AP-NO-profilar **ikkje** skal versjonslåsast (dei "følgjer standardar og
endrar seg sjeldan") — versjonslåsing er meint for import **mellom
domenemodellar**. `blomsterregisteret-schema.yaml` sin import av
`dcat-ap-no-schema` via pinna URL var difor sjølve avviket, ikkje berre eit
utløysande symptom. Andre domenemodellar (t.d.
`src/linkml/referanse/referansemodell/referansemodell-schema.yaml`)
importerer `dcat-ap-no-schema` via relativ sti
(`../../ap-no/dcat-ap-no/dcat-ap-no-schema`).

## Steg

1. **`batch-generate.py`**: legg til same
   `sys.path.insert(...) / import linkml_relative_import_patch / .apply()`-
   mønster som dei fire eksisterande kallestadene, før
   `importlib.import_module(spec.module)` køyrer.
2. **`blomsterregisteret-schema.yaml`**: fjern den overflødige,
   ubrukte `kontaktpunkt`-sloten (linje 58-61) og det overflødige,
   ubrukte `subsets:`-blokka (Obligatorisk/Anbefalt/Valgfri, linje 31-37).
   Begge er alt tilgjengelege via importkjeda (dcat-ap-no-schema →
   common-ap-no-schema).
3. **`linkml_relative_import_patch.py`**: utvid patchen til òg å dekke
   `linkml.utils.mergeutils.resolve_merged_imports()` — ein SEPARAT kopi av
   same buggy `Path(...).parent`-mønster, brukt av den eldre
   `SchemaLoader`-baserte generator-familien
   (pythongen/protogen/rdfgen/graphqlgen/plantumlgen/jsonldcontextgen, jf.
   `uses_schemaloader = True`), ikkje dekt av (1) sin `SchemaView`-patch.
4. **`bugs/relativ-import-via-versjonslast-url.md`**: oppdater til å
   dokumentere begge dei patcha kodestadene (SchemaView + mergeutils) og
   den femte kallestaden (`batch-generate.py`).
5. **`blomsterregisteret-schema.yaml`**: endre importen av
   `dcat-ap-no-schema` frå versjonslåst URL til relativ sti
   (`../../ap-no/dcat-ap-no/dcat-ap-no-schema`) — retter Feil 3 ved rota og
   bringer skjemaet i tråd med importhierarki-konvensjonen for AP-NO-profilar.
6. Verifiser med `make domain-oreg` — alle 12 generator-gruppene (inkl.
   `gen-informasjonsmodell-instance`) skal fullføre utan feil.

## Handlingsliste

- [x] Steg 1: patch `batch-generate.py` (SchemaView-patchen)
- [x] Steg 2: fjern duplikat `kontaktpunkt`-slot og duplikat `subsets`-blokk
- [x] Steg 3: utvid patchen til `mergeutils.resolve_merged_imports()`
- [x] Steg 4: oppdater BUG-15-dokumentasjon
- [x] Steg 5: rett blomsterregisteret sin dcat-ap-no-import til relativ sti
- [x] Steg 6: `make domain-oreg` grønt (alle 12 grupper, inkl.
      gen-informasjonsmodell-instance)

## Utført

Alle steg fullførte og verifiserte. `make domain-oreg` køyrer no reint for
alle tre oreg-skjema. Feilsøkinga avdekte at CI-feilen hadde tre uavhengige
rotårsaker som kvarandre delvis skjulte (CURIE-bugen i to ulike
linkml-modular skjulte den ekte 404-feilen inntil begge var patcha).
