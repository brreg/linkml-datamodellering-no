# Bug: YAML/SchemaLoader-basert lasting støttar ikkje polymorf `inlined_as_list`

**ID:** BUG-8
**Status:** `open`
**Komponent:** `linkml-runtime` (`yamlutils.py::_normalize_inlined`)
**Oppdaga:** 2026-06-21 (proof-of-concept, MD5 steg 1, `specs/backlog/eksponer-modellelement-maskinhosting.md`)

## Symptom

Eit containerattributt med `range:` sett til ei **abstrakt** basisklasse
(t.d. `Egenskap` i `modelldcat-modell-schema.yaml`) og `inlined_as_list: true`,
der dei faktiske listeelementa er instansar av **konkrete subklassar**
(`Attributt`, `Assosiasjon` — felt som berre finst på subklassen, t.d.
`refererer_til` på `Assosiasjon`), krasjar ved lasting:

```
TypeError: Egenskap.__init__() got an unexpected keyword argument 'refererer_til'
```

Reprodusert med `linkml-convert --output-format ttl` og direkte
`yaml_loader.load(..., target_class=ModellkatalogContainer)` — begge nyttar
`linkml_runtime.utils.yamlutils.py::_normalize_inlined`, som hardkodar
instansiering til **den statiske range-klassa** (`slot_type(**as_dict(entry))`),
aldri ein faktisk subklasse, sjølv når dataen openbart tilhører subklassen.

Eit eksplisitt `@type`-felt i dataen (eit forsøk på å gje eit
typediskriminator-hint) **hjelper ikkje** — det blir berre eit ukjent
keyword-argument og feilar identisk (`unexpected keyword argument '@type'`).

## Motsetnad med JSON Schema-validering

`linkml.validator.validate()` (jsonschema-basert, brukt av
`make validate-instance` og `mcp-validate`) validerer derimot **korrekt** —
generert JSON Schema brukar `anyOf` over alle subklassar av range-klassa, og
strukturell matching (utan `@type`) lykkast så lenge subklasseformene er
strukturelt unike. Dette gjev eit **falskt positivt** signal: ein instans kan
validere feilfritt med `make validate-instance`/`mcp-validate`, men likevel
krasje hardt ved `linkml-convert`/`gen-rdf`/python-dataclass-lasting.

## Rot-årsak

To ulike kodepatar i `linkml`/`linkml-runtime`, igjen (jf. BUG-6/BUG-7):

- **JSON Schema-generatoren** (`JsonSchemaGenerator`) ekspanderer range til
  `anyOf` over range-klassa og alle kjente subklassar — polymorfi er støtta
  på **skjemanivå**.
- **YAML/SchemaLoader-basert objektlasting** (`yamlutils._normalize_inlined`,
  brukt av `yaml_loader`, `linkml-convert`, og dermed indirekte
  `gen-rdf`/RDF-dumping av datafiler) instansierer **alltid** den statiske
  deklarerte range-klassa, uavhengig av dataen sitt faktiske innhald — det
  finst ingen type-diskriminator-mekanisme (`@type` eller liknande) som blir
  respektert her.

Dette er strengt tatt ein ny variant av same root cause-familie som
BUG-6/BUG-7 (`specs/bugs/dqv-standard-class-override.md`,
`specs/bugs/duplicate-slot-merge-konflikt.md`): inkonsistens mellom
SchemaView/JSON Schema-baserte generatorar (polymorfi-medvitne) og
SchemaLoader/YAML-baserte kodepatar (ikkje polymorfi-medvitne).

## Workaround

Ingen generell workaround for å bevare éin delt, polymorf liste. Den einaste
verifiserte løysinga er å **unngå polymorf inlining heilt**: gje konkrete
subklassar (`Attributt`, `Assosiasjon`, `Objekttype`, …) **eigne, ikkje-delte
containerattributt** (t.d. `attributter: range: Attributt`,
`assosiasjoner: range: Assosiasjon`, i staden for éin delt
`egenskaper: range: Egenskap`). Dette unngår at YAML-lastaren må gjette
subklasse, sidan range då alltid er konkret og eksakt.

**Generell regel for resten av repoet:** ein `inlined`/`inlined_as_list`-
slot eller containerattributt skal alltid ha **konkret** `range:` (ikkje ei
abstrakt eller `mixin`-klasse) dersom datafila skal kunne lastes med
`linkml-convert`, `gen-rdf`, eller python-dataclass-baserte verktøy. Bruk
separate attributt per konkret subklasse i staden for ei delt, polymorf
liste.

## Konsekvens for MD5 (`specs/backlog/eksponer-modellelement-maskinhosting.md`)

Mappingtabellen og containerstrukturen i MD5-planen (delt `egenskaper:
range: Egenskap`-liste med blanding av `Attributt`/`Assosiasjon`-instansar)
må revurderes før Steg 2 held fram — sjå «Opne spørsmål» i den specen.

## Løysing

Ingen upstream-fiks venta (same designval-kategori som BUG-6/BUG-7). Permanent
løysing for dette repoet er å designe containerstrukturar med konkret range
per subklasse, aldri delte polymorfe lister.
