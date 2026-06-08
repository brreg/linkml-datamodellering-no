# Skisse: filer oppretta av scaffold-steget

`make new-model NAME=<namn> DOMAIN=<domene>` køyrer `src/assets/scripts/new-model.sh`
og oppretter tre filer. Nedanfor er strukturen vist for `NAME=mitt-register DOMAIN=oreg`.

---

## Filer som vert oppretta

```
src/linkml/oreg/mitt-register/
├── mitt-register-schema.yaml       ← hovudskjema
├── manifest.yaml                   ← publiserings- og generatorkonfig
└── examples/
    └── mitt-register-eksempel.yaml ← minimal instansfil
```

> **Merk:** `mkdocs/docs/ny-domenemodell.md` nemner berre dei to første filene, men scriptet oppretter også `manifest.yaml`.

---

## 1. `mitt-register-schema.yaml`

Generert av `mcp-linkml-modell-utkast` (`inputFormat: empty`, profil `default`),
deretter beriket med tre TODO-kommentarar av scriptet.

### Hovudblokker

| Blokk | Innhald |
|---|---|
| Filhode | 3 kommentarlinjer om placeholder-prefix og TODO-markeringar |
| `id` | `https://data.norge.no/oreg/mitt-register` |
| `name` | `mitt_register` (bindestrek → understrek) |
| `description` | `"Generert frå JSON Schema 'mitt_register'."` |
| `prefixes` | `linkml`, `ex` (= schema-id + `/`), `dct`, `dcat`, `foaf`, `skos`, `xsd`, `rdf`, `rdfs` |
| `default_prefix` | `"ex"` |
| `default_range` | `"string"` |
| `imports` | `["linkml:types"]` |
| `subsets` | `Obligatorisk`, `Anbefalt`, `Valgfri` |
| `classes` | Stub-klasse + `Containerklasse` (sjå nedanfor) |
| `slots` | Berre `id`-slot |

### Stub-klassen

Klassen heiter `<schema_name>` (dvs. `mitt_register`). TODO-kommentaren i skjemafila
oppmodar til å gi han eit norsk PascalCase-namn manuelt.

```yaml
classes:
  mitt_register:
    class_uri: ex:mitt_register
    annotations:
      begrepsidentifikator: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
    slots:
      - id
```

### Containerklassen

Containerklassen heiter alltid `Containerklasse`. Container-slot-namnet er
`_to_plural(stub_klassenamn, suffix="er")`, dvs. første bokstav til lowercase + `"er"`.
For `mitt_register` → `mitt_registerer`.

```yaml
  Containerklasse:
    tree_root: true
    attributes:
      mitt_registerer:
        range: mitt_register
        multivalued: true
        inlined: true
        inlined_as_list: true
```

### Global `id`-slot

```yaml
slots:
  id:
    description: Unik URI-identifikator for ressursen.
    identifier: true
    range: uriorcurie
```

### TODO-kommentarar (lagt til av scriptet)

Etter YAML-innhaldet legg scriptet til tre kommentarlinjer:

```
# TODO: Legg til domene-spesifikke imports etter 'linkml:types', t.d.:
#   - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
# TODO: Gi stub-klassen eit meiningsfult norsk namn (PascalCase).
# TODO: Legg til slots og slot_usage for eigenskapane i modellen.
```

---

## 2. `examples/mitt-register-eksempel.yaml`

Minimal instansfil. Container-slot-namnet vert henta dynamisk frå det genererte skjemaet.

```yaml
# Eksempel for mitt-register
# Tilpass instansane med reelle verdiar etter at skjemaet er ferdigstilt.
---
Containerklasse:
  mitt_registerer:
    - id: https://data.norge.no/oreg/mitt-register/eksempel-1
```

---

## 3. `manifest.yaml`

Standardkonfig — alle generatorar på, ingen ekstra flagg.

```yaml
publish_external: false
data_policy: silver

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
```

---

## Avvik mellom dokumentasjon og røyndom

| Punkt | `ny-domenemodell.md` seier | Røyndom (scriptet) |
|---|---|---|
| Filer oppretta | 2 (skjema + eksempel) | 3 (skjema + eksempel + manifest) |
| Containerklassenamn | ikkje nemnt | alltid `Containerklasse` (ikkje `<Domene>Container`) — avvik frå CLAUDE.md-konvensjonen |
| Stub-klassenamn | ikkje nemnt | `<schema_name>` i snake_case, ikkje PascalCase |
