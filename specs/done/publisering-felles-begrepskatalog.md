# Plan: Publisering til Felles Begrepskatalog

## Mål

Automatisk publisering av SKOS/Turtle-filer genererte frå LinkML-instansar
til [Felles Begrepskatalog](https://data.norge.no/concepts) via høstingsendepunkt,
med ein eigen valideringspolicy (`felles-begrepskatalog`) som sikrar at skjemaet
oppfyller SKOS-AP-NO-Begrep-krava før publisering.

## Bakgrunn

Repoet har to typar YAML-filer med klart skilde føremål:

| Katalog | Føremål | Publiserast til Felles Begrepskatalog? |
|---|---|---|
| `examples/<domene>/` | Illustrative døme — viser gyldig datafil, nyttast i gen-doc | **Nei** |
| `data/<domene>/` | Reelle produksjonsdata — dei faktiske begrepsdefinisjonane | **Ja** |

Eksempelfiler skal **aldri** publiserast til eksterne mottakarar. Dei er berre
til internt bruk: som gyldige dataeksempel og for gen-doc-dokumentasjon.

Pipelinen genererer allereie Turtle frå YAML via `convert-rdf`. Det som manglar er:

1. Ein `data/`-katalog med reelle begrepsfiler (skilt frå `examples/`)
2. Ein `felles-begrepskatalog`-policy i `mcp-linkml-validator`
3. Ei konverteringspipeline for `data/`-filer til Turtle
4. Registrering av GitHub Pages-URL som høstingsendepunkt

---

## Del 1 — Policy: `felles-begrepskatalog`

### Føremål

Validerer at eit begrepskatalogskjema (t.d. `brreg-begrep-schema.yaml`) er
strukturelt klart for publisering til Felles Begrepskatalog:

- Importerer SKOS-AP-NO-Begrep (direkte eller transitivt)
- Containerklassen eksponerer `Begrep` og `Samling`
- `Begrep`-klassen har alle obligatoriske SKOS-AP-NO-slots
- `Samling`-klassen har alle obligatoriske SKOS-AP-NO-slots

Policyen arvar `bronze` (schema `id`/`name`, HTTP-URI-sjekk).

### Bruk

```bash
make mcp-validate \
  SCHEMA=src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml \
  POLICY=felles-begrepskatalog
```

### Plassering

```
src/mcp-linkml-validator/policies/felles-begrepskatalog.yaml
```

### YAML-struktur

```yaml
version: 1
extends: bronze

description: >
  Policy for begrepskatalogskjema som skal publiserast til Felles Begrepskatalog.
  Validerer at skjemaet importerer SKOS-AP-NO-Begrep og eksponerer dei nødvendige
  klassane og slotsa via containerklassen (tree_root).
  Arvar bronselaget: grunnleggande metadata- og modelleringskrav.

required:
  schema: [id, name]
  class: []
  slot: []

recommended:
  schema: [description, title, version]
  class: []
  slot: []

checks:

  # ── Import-krav ─────────────────────────────────────────────────────────────

  schema_importerer_skos_ap_no:
    severity: error
    description: >
      Skjemaet må importere skos-ap-no-schema (direkte eller transitivt).
      SKOS-AP-NO-Begrep er grunnlaget for alle begrepskatalogskjema.
    check: schema_imports
    must_import: skos-ap-no-schema

  # ── Prefiks-krav ─────────────────────────────────────────────────────────────

  schema_brukar_skos_prefix:
    severity: error
    description: >
      Skjemaet må deklarere skos:-prefikset. Alle begrep er skos:Concept.
    check: schema_declares_standard_prefix
    standard_prefixes: [skos]

  schema_brukar_dct_prefix:
    severity: error
    description: >
      Skjemaet må deklarere dct:-prefikset (Dublin Core Terms).
      Nødvendig for dct:identifier, dct:publisher, dct:title o.a.
    check: schema_declares_standard_prefix
    standard_prefixes: [dct]

  # ── Containerklasse-krav ─────────────────────────────────────────────────────

  container_har_begrep:
    severity: error
    description: >
      Containerklassen (tree_root) må ha eit attributt med range Begrep.
      Felles Begrepskatalog krev minst eitt begrep per katalog.
    check: container_has_class
    class: Begrep

  container_har_samling:
    severity: warning
    description: >
      Containerklassen bør ha eit attributt med range Samling.
      Anbefalt for å organisere begrep i namngjeve samlingar (skos:Collection).
    check: container_has_class
    class: Samling

  # ── Begrep-krav (skos:Concept) — SKOS-AP-NO-Begrep obligatoriske ─────────────

  begrep_har_anbefalt_term:
    severity: error
    description: >
      Begrep må ha skos:prefLabel (anbefalt term). Obligatorisk i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: skos:prefLabel

  begrep_har_definisjon:
    severity: error
    description: >
      Begrep må ha skos:definition eller euvoc:xlDefinition.
      SKOS-AP-NO-Begrep krev minst éin av desse formene.
    check: merged_class_has_any_slot_with_uri
    class: Begrep
    slot_uris:
      - skos:definition
      - euvoc:xlDefinition

  begrep_har_identifikator:
    severity: error
    description: >
      Begrep må ha dct:identifier. Obligatorisk i SKOS-AP-NO-Begrep —
      gir kvart begrep ein persistent URI.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: dct:identifier

  begrep_har_utgjevar:
    severity: error
    description: >
      Begrep må ha dct:publisher. Obligatorisk i SKOS-AP-NO-Begrep —
      peikar til ansvarleg organisasjon.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: dct:publisher

  begrep_har_kontaktpunkt:
    severity: error
    description: >
      Begrep må ha dcat:contactPoint. Obligatorisk i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: dcat:contactPoint

  # ── Begrep-krav — SKOS-AP-NO-Begrep anbefalte ────────────────────────────────

  begrep_har_fagomrade:
    severity: warning
    description: >
      Begrep bør ha dct:subject (fagområde / LOS-tema). Anbefalt i SKOS-AP-NO-Begrep
      — gir kontekst og moglegheit for temafiltrering i katalogen.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: dct:subject

  begrep_har_ansvarleg_verksemd:
    severity: warning
    description: >
      Begrep bør ha dct:creator (ansvarleg verksemd). Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: dct:creator

  begrep_har_gyldig_fra:
    severity: warning
    description: >
      Begrep bør ha euvoc:startDate (gyldig frå). Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: euvoc:startDate

  begrep_har_gyldig_til:
    severity: warning
    description: >
      Begrep bør ha euvoc:endDate (gyldig til). Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: euvoc:endDate

  begrep_har_opprettingsdato:
    severity: warning
    description: >
      Begrep bør ha dct:created (opprettingsdato). Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: dct:created

  begrep_har_endringsdato:
    severity: warning
    description: >
      Begrep bør ha dct:modified (dato sist oppdatert). Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: dct:modified

  begrep_har_merknad:
    severity: warning
    description: >
      Begrep bør ha skos:scopeNote (merknad). Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: skos:scopeNote

  begrep_har_tillate_term:
    severity: warning
    description: >
      Begrep bør ha skos:altLabel (tillaten term). Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Begrep
    slot_uri: skos:altLabel

  # ── Definisjon-krav (euvoc:XlNote) ───────────────────────────────────────────

  definisjon_har_tekst:
    severity: error
    description: >
      Definisjon må ha rdf:value (definisjonsteikst). Obligatorisk i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Definisjon
    slot_uri: rdf:value

  definisjon_har_kjelde_relasjon:
    severity: warning
    description: >
      Definisjon bør ha skosno:relationshipWithSource (kjelde-relasjon).
      Anbefalt i SKOS-AP-NO-Begrep — beskriv forholdet mellom definisjonen og kjelda.
    check: merged_class_has_slot_with_uri
    class: Definisjon
    slot_uri: skosno:relationshipWithSource

  # ── AssosiativRelasjon-krav (skosno:AssociativeConceptRelation) ───────────────

  assosiativ_relasjon_har_til_omgrep:
    severity: error
    description: >
      AssosiativRelasjon må ha skosno:hasToConcept (til-omgrep).
      Obligatorisk i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: AssosiativRelasjon
    slot_uri: skosno:hasToConcept

  assosiativ_relasjon_har_relasjontype:
    severity: error
    description: >
      AssosiativRelasjon må ha skosno:relationRole (relasjonstype).
      Obligatorisk i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: AssosiativRelasjon
    slot_uri: skosno:relationRole

  # ── GeneriskRelasjon-krav (skosno:GenericConceptRelation) ────────────────────

  generisk_relasjon_har_overomgrep:
    severity: error
    description: >
      GeneriskRelasjon må ha skosno:hasGenericConcept (overomgrep).
      Obligatorisk i SKOS-AP-NO-Begrep — skjemaet må støtte begge retningar.
    check: merged_class_has_slot_with_uri
    class: GeneriskRelasjon
    slot_uri: skosno:hasGenericConcept

  generisk_relasjon_har_underomgrep:
    severity: error
    description: >
      GeneriskRelasjon må ha skosno:hasSpecificConcept (underomgrep).
      Obligatorisk i SKOS-AP-NO-Begrep — skjemaet må støtte begge retningar.
    check: merged_class_has_slot_with_uri
    class: GeneriskRelasjon
    slot_uri: skosno:hasSpecificConcept

  generisk_relasjon_har_inndelingskriterium:
    severity: warning
    description: >
      GeneriskRelasjon bør ha dct:description (inndelingskriterium).
      Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: GeneriskRelasjon
    slot_uri: dct:description

  # ── PartitivRelasjon-krav (skosno:PartitiveConceptRelation) ──────────────────

  partitiv_relasjon_har_delomgrep:
    severity: error
    description: >
      PartitivRelasjon må ha skosno:hasPartitiveConcept (delomgrep).
      Obligatorisk i SKOS-AP-NO-Begrep — skjemaet må støtte begge retningar.
    check: merged_class_has_slot_with_uri
    class: PartitivRelasjon
    slot_uri: skosno:hasPartitiveConcept

  partitiv_relasjon_har_heilskapleg_omgrep:
    severity: error
    description: >
      PartitivRelasjon må ha skosno:hasComprehensiveConcept (heilskapleg omgrep).
      Obligatorisk i SKOS-AP-NO-Begrep — skjemaet må støtte begge retningar.
    check: merged_class_has_slot_with_uri
    class: PartitivRelasjon
    slot_uri: skosno:hasComprehensiveConcept

  partitiv_relasjon_har_inndelingskriterium:
    severity: warning
    description: >
      PartitivRelasjon bør ha dct:description (inndelingskriterium).
      Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: PartitivRelasjon
    slot_uri: dct:description

  # ── Samling-krav (skos:Collection) — SKOS-AP-NO-Begrep obligatoriske ─────────

  samling_har_identifikator:
    severity: error
    description: >
      Samling må ha dct:identifier. Obligatorisk i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Samling
    slot_uri: dct:identifier

  samling_har_tittel:
    severity: error
    description: >
      Samling må ha dct:title (namn på samlinga). Obligatorisk i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Samling
    slot_uri: dct:title

  samling_har_utgjevar:
    severity: error
    description: >
      Samling må ha dct:publisher. Obligatorisk i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Samling
    slot_uri: dct:publisher

  samling_har_kontaktpunkt:
    severity: error
    description: >
      Samling må ha dcat:contactPoint. Obligatorisk i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Samling
    slot_uri: dcat:contactPoint

  samling_har_medlem:
    severity: error
    description: >
      Samling må ha skos:member. Obligatorisk i SKOS-AP-NO-Begrep —
      samlinga må innehalde minst eitt begrep.
    check: merged_class_has_slot_with_uri
    class: Samling
    slot_uri: skos:member

  # ── Samling-krav — SKOS-AP-NO-Begrep anbefalte ───────────────────────────────

  samling_har_beskrivelse:
    severity: warning
    description: >
      Samling bør ha dct:description (beskriving av samlinga).
      Anbefalt i SKOS-AP-NO-Begrep.
    check: merged_class_has_slot_with_uri
    class: Samling
    slot_uri: dct:description

instance_checks:

  # ── Instans-validering av utgjevar-URI ────────────────────────────────────────

  utgjevar_er_kjend_org:
    severity: error
    description: >
      dct:publisher-verdien i instansen må vere ein URI på formatet
      https://data.norge.no/organizations/<9-sifra orgnr> og liggje
      i lista over kjente utgivarar. Sikrar at berre gyldige Brønnøysund-
      registrerte organisasjonar kan setjast som utgjevar i katalogen.
    check: instance_slot_uri_pattern
    slot_uri: dct:publisher
    pattern: "^https://data\\.norge\\.no/organizations/\\d{9}$"
    known_values:
      - https://data.norge.no/organizations/974760673
```

### Nye check-handlers i `server.py`

Tre nye check-typar må implementerast (dei eksisterande dekkar ikkje importerte klasser):

#### `schema_imports`

Sjekkar at skjemaet sin importliste inneheld eit gjeve skjemanamn (substring-match
på importstiar, t.d. `skos-ap-no-schema` treff `../../ap-no/skos-ap-no/skos-ap-no-schema`).

```python
def _check_schema_imports(sv, schema, config, issues):
    must_import = config["must_import"]
    found = any(must_import in imp for imp in (schema.imports or []))
    if not found:
        issues.append(issue(
            config["severity"], "missing_required_import", "schema",
            f"Skjemaet importerer ikkje '{must_import}'",
        ))
```

#### `merged_class_has_slot_with_uri`

Som eksisterande `class_has_slot_with_uri`, men brukar `sv.get_class()` (SchemaView
sin samanslåtte visning) slik at importerte klasser som `Begrep` og `Samling`
òg vert sjekka — ikkje berre lokalt definerte klasser.

```python
def _check_merged_class_has_slot_with_uri(sv, schema, config, issues):
    cname = config["class"]
    required_uri = config["slot_uri"]
    if sv.get_class(cname) is None:
        return  # klassen finst ikkje ein gong i imports — ikkje relevant
    if required_uri not in _collect_class_slot_uris(sv, cname):
        severity = config["severity"]
        code = "class_missing_required_slot" if severity == "error" \
               else "class_missing_recommended_slot"
        issues.append(issue(
            severity, code, f"class:{cname}",
            f"Klasse '{cname}' manglar slot med {required_uri}",
        ))
```

#### `merged_class_has_any_slot_with_uri`

Som over, men godtek kva som helst av ei liste med URI-ar (brukt for
`skos:definition` **eller** `euvoc:xlDefinition`).

```python
def _check_merged_class_has_any_slot_with_uri(sv, schema, config, issues):
    cname = config["class"]
    slot_uris = config["slot_uris"]
    if sv.get_class(cname) is None:
        return
    found = _collect_class_slot_uris(sv, cname)
    if not any(uri in found for uri in slot_uris):
        severity = config["severity"]
        code = "class_missing_required_slot" if severity == "error" \
               else "class_missing_recommended_slot"
        issues.append(issue(
            severity, code, f"class:{cname}",
            f"Klasse '{cname}' manglar minst éin slot med URI frå: "
            f"{', '.join(slot_uris)}",
        ))
```

Legg til i `_CHECK_HANDLERS`-dicten:
```python
"schema_imports":                    _check_schema_imports,
"merged_class_has_slot_with_uri":    _check_merged_class_has_slot_with_uri,
"merged_class_has_any_slot_with_uri": _check_merged_class_has_any_slot_with_uri,
```

#### Instans-spesifikke check-handlers

`instance_checks:` opererer på den parsade YAML-instansen — ikkje på skjemastrukturen.
Handlerane får ein eigen signatyr og vert ikkje registrerte i `_CHECK_HANDLERS`.

##### `instance_slot_uri_pattern`

Går rekursivt gjennom instansobjektet, finn alle slot-verdiar der slot sin `slot_uri`
samsvarar med konfigurert `slot_uri`, og validerer kvar verdi mot eit regex-mønster.
Dersom `known_values` er sett, vert verdien i tillegg sjekka mot lista.

```python
import re

def _check_instance_slot_uri_pattern(sv, schema, instance, config, issues):
    slot_uri_target = config["slot_uri"]
    pattern = re.compile(config["pattern"])
    known_values = config.get("known_values", [])

    # Finn alle slot-namn (i schema + imports) med matchande slot_uri
    target_slots = {
        name
        for name, s in sv.all_slots().items()
        if (s.slot_uri or "") == slot_uri_target
        or sv.expand_curie(s.slot_uri or "") == sv.expand_curie(slot_uri_target)
    }

    def walk(obj, path=""):
        if not isinstance(obj, dict):
            return
        for key, val in obj.items():
            if key in target_slots:
                values = val if isinstance(val, list) else [val]
                for v in values:
                    if not isinstance(v, str):
                        continue
                    loc = f"instance:{path}.{key}" if path else f"instance:{key}"
                    if not pattern.match(v):
                        issues.append(issue(
                            config["severity"],
                            "instance_slot_invalid_uri_pattern",
                            loc,
                            f"'{v}' passar ikkje mønsteret {config['pattern']} "
                            f"for {slot_uri_target}",
                        ))
                    elif known_values and v not in known_values:
                        issues.append(issue(
                            config["severity"],
                            "instance_slot_unknown_value",
                            loc,
                            f"'{v}' er ikkje i lista over kjente utgivarar: "
                            f"{', '.join(known_values)}",
                        ))
            walk(val, f"{path}.{key}" if path else key)

    walk(instance)
```

##### Dispatch-funksjon og integrering i `validate_schema`

```python
_INSTANCE_CHECK_HANDLERS = {
    "instance_slot_uri_pattern": _check_instance_slot_uri_pattern,
}

def _run_instance_checks(sv, schema, instance, policy, issues):
    for check_name, config in (policy.get("instance_checks") or {}).items():
        handler = _INSTANCE_CHECK_HANDLERS.get(config.get("check"))
        if handler is None:
            continue
        handler(sv, schema, instance, config, issues)
```

I `validate_schema`, etter at instansen er parsa (dvs. etter den eksisterande
`validate_instance`-kallet), legg til:

```python
# Etter eksisterande instansvalidering (if instance_text is not None: ...)
if instance_text is not None:
    parsed_instance = yaml.safe_load(instance_text)
    _run_instance_checks(sv, schema, parsed_instance, policy, issues)
```

`yaml.safe_load` er allereie tilgjengeleg i `server.py` (brukt for policy-lasting).
`parsed_instance` er ein vanleg Python-dict — ingen ekstra avhengigheiter.

### Sjekkoversikt

#### Import og prefiks

| Check | URI / Krav | Alvor | Kjelde |
|---|---|---|---|
| `schema_imports` | `skos-ap-no-schema` | error | Ny |
| `schema_declares_standard_prefix` | `skos` | error | Eksisterande |
| `schema_declares_standard_prefix` | `dct` | error | Eksisterande |

#### Containerklasse

| Check | Klasse | Alvor | Kjelde |
|---|---|---|---|
| `container_has_class` | `Begrep` | error | Eksisterande |
| `container_has_class` | `Samling` | warning | Eksisterande |

#### Begrep (skos:Concept)

| URI | Krav per SKOS-AP-NO | Alvor |
|---|---|---|
| `skos:prefLabel` | Obligatorisk | error |
| `skos:definition` / `euvoc:xlDefinition` | Obligatorisk (éin av) | error |
| `dct:identifier` | Obligatorisk | error |
| `dct:publisher` | Obligatorisk | error |
| `dcat:contactPoint` | Obligatorisk | error |
| `dct:subject` | Anbefalt | warning |
| `dct:creator` | Anbefalt | warning |
| `euvoc:startDate` | Anbefalt | warning |
| `euvoc:endDate` | Anbefalt | warning |
| `dct:created` | Anbefalt | warning |
| `dct:modified` | Anbefalt | warning |
| `skos:scopeNote` | Anbefalt | warning |
| `skos:altLabel` | Anbefalt | warning |

#### Definisjon (euvoc:XlNote)

| URI | Krav per SKOS-AP-NO | Alvor |
|---|---|---|
| `rdf:value` | Obligatorisk | error |
| `skosno:relationshipWithSource` | Anbefalt | warning |

#### AssosiativRelasjon (skosno:AssociativeConceptRelation)

| URI | Krav per SKOS-AP-NO | Alvor |
|---|---|---|
| `skosno:hasToConcept` | Obligatorisk | error |
| `skosno:relationRole` | Obligatorisk | error |

#### GeneriskRelasjon (skosno:GenericConceptRelation)

| URI | Krav per SKOS-AP-NO | Alvor |
|---|---|---|
| `skosno:hasGenericConcept` | Obligatorisk | error |
| `skosno:hasSpecificConcept` | Obligatorisk | error |
| `dct:description` | Anbefalt | warning |

#### PartitivRelasjon (skosno:PartitiveConceptRelation)

| URI | Krav per SKOS-AP-NO | Alvor |
|---|---|---|
| `skosno:hasPartitiveConcept` | Obligatorisk | error |
| `skosno:hasComprehensiveConcept` | Obligatorisk | error |
| `dct:description` | Anbefalt | warning |

#### Samling (skos:Collection)

| URI | Krav per SKOS-AP-NO | Alvor |
|---|---|---|
| `dct:identifier` | Obligatorisk | error |
| `dct:title` | Obligatorisk | error |
| `dct:publisher` | Obligatorisk | error |
| `dcat:contactPoint` | Obligatorisk | error |
| `skos:member` | Obligatorisk | error |
| `dct:description` | Anbefalt | warning |

#### Instans-sjekkar

Desse køyrer mot den parsade YAML-instansen (ikkje skjemaet) og krev at
`instance_text` er tilgjengeleg (automatisk via `flatten-and-validate.bash`).

| Check | Slot-URI | Krav | Alvor |
|---|---|---|---|
| `instance_slot_uri_pattern` | `dct:publisher` | Mønster `https://data.norge.no/organizations/\d{9}` og i `known_values` | error |

Pluss arva frå `bronze`: `schema_id_is_http_uri`, `all_classes_have_class_uri` (warning),
`all_slots_have_slot_uri` (warning), `all_classes_have_identifier` (warning).

---

## Del 2 — Datafiler og konverteringspipeline

### Katalogstruktur for reelle data

Reelle begrepsdefinisjonar ligg i `data/`-katalogen, spegla etter same
domene/skjema-mønster som `src/linkml/` og `examples/`:

```
data/
  begrep/
    brreg-begrep.yaml        # reelle begrepsdefinisjonar — det som vert publisert
```

Éi YAML-fil per begrepskatalog. Fila følgjer same skjemastruktur som
`examples/begrep/brreg-begrep-eksempel.yaml`, men inneheld faktiske
produksjonsdata med stabile URI-ar.

### Konverteringspipeline

Ein ny Makefile-regel `convert-data` konverterer alle `data/`-filer til Turtle,
parallelt med `convert-rdf` (som handterer `examples/`):

```makefile
convert-data:
	@for domain in $$(ls data/ 2>/dev/null); do \
		for datafile in data/$$domain/*-eksempel.yaml data/$$domain/*.yaml; do \
			[ -f "$$datafile" ] || continue; \
			name=$$(basename "$$datafile" .yaml); \
			# resolv schema: same mønster som convert-rdf \
			schema=src/linkml/$$domain/$$name/$$name-schema.yaml; \
			mkdir -p $(GEN_DIR)/$$domain/$$name; \
			$(LINKML_RUN) linkml-convert \
				--schema $$schema --output-format ttl \
				--no-validate \
				--output $(GEN_DIR)/$$domain/$$name/$$name.ttl \
				$$datafile; \
		done; \
	done
```

`generate.yml` utvidar med `convert-data` etter `convert-rdf` slik at
`data/`-filer vert publiserte til GitHub Pages ved kvar push til `main`.

### Publisert URL

```
https://brreg.github.io/linkml-datamodellering-no/begrep/brreg-begrep/brreg-begrep.ttl
```

Kvar gong `data/begrep/brreg-begrep.yaml` vert endra og pushat til `main`,
kjøyrer `generate.yml` og publiserer ny versjon av `.ttl`-fila automatisk.

---

## Del 3 — Publisering via høstingsendepunkt

### Tilnærming: høstingsendepunkt

Data.norge.no tilbyr to publiseringsmetodar:

| Metode | Passar for |
|---|---|
| **Høstingsendepunkt** (valt her) | Automatisert generering, hyppige oppdateringar, stor katalog |
| Registreringsløsinga | Manuell oppføring av enkeltbegrep via nettskjema |

### Steg-for-steg

#### Steg 1 — Opprett datafil og validér

Lag `data/begrep/brreg-begrep.yaml` med reelle begrepsdefinisjonar.
Valider skjema og datafil i eitt steg:

```bash
make mcp-validate \
  SCHEMA=src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=data/begrep/brreg-begrep.yaml
```

`flatten-and-validate.bash` tek `INSTANCE` som eksplisitt tredje argument
(sjå Del 4 § Instansvalidering). Alle feil (severity: error) må rettast
før registrering. Åtvaringar (warning) bør rettast, men blokkerer ikkje publisering.

Sjekk i tillegg at den genererte `.ttl`-fila har eksplisitte språktag (`@nb`/`@nn`/`@en`)
på alle `skos:prefLabel`- og `skos:definition`-verdiar — dette er eit RDF-nivå-krav
utanfor LinkML sin validator.

#### Steg 2 — Tilgang til administrasjonsgrensesnittet

Krev **ID-porten-innlogging** og **Altinn-rolle** for organisasjonen (Brønnøysund, orgnr. 974760673).

1. Logg inn på [registrering.fellesdatakatalog.digdir.no](https://registrering.fellesdatakatalog.digdir.no) med ID-porten (sikkerheitsnivå 3)
2. Aksepter vilkår for bruk ved første innlogging (krev administratorrolle i Altinn)
3. Verifiser at du ser Brønnøysund-organisasjonen i oversikta

> Nødvendig Altinn-rolle: sjå [data.norge.no/nb/docs/sharing-data/login-and-access](https://data.norge.no/nb/docs/sharing-data/login-and-access)

#### Steg 3 — Registrer høstingsendepunkt

Navigér til [admin.fellesdatakatalog.digdir.no/data-sources](https://admin.fellesdatakatalog.digdir.no/data-sources) og legg til ny datakjelde:

| Felt | Verdi |
|---|---|
| **Utgjevar** | Registerenheten i Brønnøysund (974760673) |
| **Katalogtype** | Begreper |
| **Datakildentype** | SKOS-AP-NO |
| **Format** | Turtle |
| **Datakjelde-URL** | `https://brreg.github.io/linkml-datamodellering-no/begrep/brreg-begrep/brreg-begrep.ttl` |
| **Autentisering** | (tomt — endepunktet er offentleg) |

Lagre. Felles datakatalog vil frå no av høste endepunktet automatisk med jamleg intervall.

#### Steg 4 — Utløys manuell høsting

Etter registrering: klikk **«Høst»** for å utløyse umiddelbar høsting utan å
vente på neste automatiske syklus. Behandlingstida er typisk nokre minutt.

#### Steg 5 — Verifiser publisering

Søk på nokre av begrepene frå `data/begrep/brreg-begrep.yaml` på
[data.norge.no/concepts](https://data.norge.no/concepts) og verifiser at:

- Begrepet visast med rett definisjon
- Utgjevar er «Registerenheten i Brønnøysund»
- Kontaktpunkt er korrekt
- LOS-tema er sett

### Automatisk oppdatering etter publisering

Når høstingsendepunktet er registrert éin gong, er arbeidsflyten fullt automatisk:

```
rediger data/begrep/brreg-begrep.yaml
    → make convert-data  (eller CI-pipeline ved push til main)
    → generated/begrep/brreg-begrep/brreg-begrep.ttl
    → GitHub Pages publiserer ny .ttl
    → Felles Begrepskatalog høstar automatisk ved neste syklus
```

Merk: `examples/begrep/brreg-begrep-eksempel.yaml` vert ikkje endra som
del av denne arbeidsflyten. Eksempelfila kan oppdaterast uavhengig
(t.d. for å illustrere skjemaendringar), men vert aldri publisert.

---

## Kjende avgrensingar og risiko

### Del 4 — Instansvalidering av datafiler

#### Eksplisitt instansbane i `flatten-and-validate.bash`

`flatten-and-validate.bash` tek eit valfritt tredje argument — ein eksplisitt
instansfil — i tillegg til schema og policy. Når dette argumentet er gjeve,
nyttast datafila i staden for å oppdage `examples/`-fila automatisk:

```bash
# Automatisk (eksempel-fil): brukast for bronze/silver/gold
bash src/mcp-linkml-validator/flatten-and-validate.bash \
  src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml \
  bronze

# Eksplisitt datafil (publiseringspolicyen): brukast for felles-begrepskatalog
bash src/mcp-linkml-validator/flatten-and-validate.bash \
  src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml \
  felles-begrepskatalog \
  data/begrep/brreg-begrep.yaml
```

Makefile-regelen `mcp-validate` les ein valfri `INSTANCE`-variabel og sender
han vidare til skriptet:

```makefile
mcp-validate:
	bash src/mcp-linkml-validator/flatten-and-validate.bash \
	  $(SCHEMA) $(POLICY) $(INSTANCE)
```

#### Kva instansvalideringa fangar opp

`make mcp-validate SCHEMA=... POLICY=felles-begrepskatalog INSTANCE=data/begrep/brreg-begrep.yaml`
validerer datafila mot det flatta skjemaet og rapporterer:

| Feil-type | Eksempel |
|---|---|
| Manglande obligatorisk felt | `Begrep` utan `anbefalt_term` (`skos:prefLabel`) |
| Manglande obligatorisk felt | `Definisjon` utan `tekst` (`rdf:value`) |
| Ugyldig type | tekst-verdi der URI er forventa |
| Feil kardinalitet | `multivalued: false`-slot med liste |
| Ukjend klasse/slot | Typo i instansnøkkel |
| Ugyldig utgjevar-URI | `dct:publisher` ikkje i `known_values`-lista |

Instansvalideringa fangar **ikkje** opp:
- Manglande språktag (`@nb`/`@nn`) — RDF-nivå-krav; bør validerast mot
  SKOS-AP-NO SHACL-shapes frå [informasjonsforvaltning/skos-ap-no-begrep](https://github.com/Informasjonsforvaltning/skos-ap-no-begrep)

#### Anbefalt arbeidsflyt

```
1. rediger data/begrep/brreg-begrep.yaml
2. make mcp-validate \
     SCHEMA=src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml \
     POLICY=felles-begrepskatalog \
     INSTANCE=data/begrep/brreg-begrep.yaml
   → validerer skjema + datafil + instance_checks (utgjevar-URI) i eitt steg
3. (ved nye URI-ar) oppdater published-uris.lock
4. push til main → CI køyrer same validering automatisk
5. GitHub Pages publiserer ny .ttl → Felles Begrepskatalog høstar
```

#### CI-integrering

`validate.yml` utvidast med eit eige steg for datafiler:

```yaml
- name: Valider datafiler mot publiseringspolicyer
  run: |
    if [ -f data/begrep/brreg-begrep.yaml ]; then
      make mcp-validate \
        SCHEMA=src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml \
        POLICY=felles-begrepskatalog \
        INSTANCE=data/begrep/brreg-begrep.yaml
    fi
```

Eksisterande `make mcp-validate` per skjema (utan `INSTANCE`) held fram
uendra — det validerer skjemastrukturen mot bronze/silver/gold og nyttar
eksempelfila for instansvalidering av skjemakvalitet.

### Fleire begrepskatalogfiler

Dersom det kjem fleire begrepskatalogskjema (t.d. `digdir-begrep`, `ssb-begrep`),
må kvart skjema registrerast som eige høstingsendepunkt. Vurder om alle katalogar
skal registrerast frå same repo, eller om eigarar registrerer eigne endepunkt.

### URI-stabilitet

#### Problemet

Kvart begrep har ein permanent URI som identifikator, t.d.
`https://begrep.brreg.no/aksjeklasser`. Denne URI-en vert generert frå `id:`-feltet
i YAML-instansfila og lagt inn i den publiserte `.ttl`-fila som `dct:identifier`.

Når Felles Begrepskatalog høstar `.ttl`-fila, knyt han metadataa til URI-en.
Viss ein URI seinare **endrast** (t.d. ved å endre ein slug), vil høstaren:
- Opprette eit nytt begrep med ny URI
- Behalde det gamle begrepet med gamal URI som ein separat oppføring

Resultatet er duplikat i katalogen og øydelagde lenkjer i system som refererer til
den opphavlege URI-en.

#### Prinsipp: URI-ar er uforanderlege etter første publisering

`id:`-feltet i `data/begrep/<katalog>.yaml` er **permanent** frå det
augeblikket katalogen er registrert som høstingsendepunkt. Denne regelen gjeld:

- `id:` på `Begrep`-objekt (`https://begrep.brreg.no/<slug>`)
- `id:` på `Definisjon`-objekt (`https://begrep.brreg.no/def/<slug>-<lang>`)
- `id:` på `Samling`-objekt (`https://begrep.brreg.no/samlingar/<slug>`)

Konsekvens: val av slug ved oppretting er eit permanent val. Vel ein stabil,
omgreps-dekkande slug — ikkje ein som refererer til spesifikk versjon, kontekst
eller organisasjonsstruktur som kan endre seg.

#### Mekanisme: URI-register (slugs.lock)

Legg til ei låsefil som sporar alle URI-ar som er publisert til Felles Begrepskatalog.
Fila vert sjekka inn i git og fungerer som ein kontrakt mellom repoet og katalogen.

**Plassering:** `src/linkml/begrep/<katalog>/published-uris.lock`

**Format:**
```
# Publiserte URI-ar for brreg-begrep — IKKJE endre eller slett eksisterande linjer.
# Nye URI-ar leggast til nedst etter publisering.
# Sist oppdatert: 2025-xx-xx
https://begrep.brreg.no/aksjeklasser
https://begrep.brreg.no/foretaksnavn
https://begrep.brreg.no/nestleder
https://begrep.brreg.no/samlingar/registerbegrep-2025
```

**Arbeidsflyt:**
1. Nye begrep: legg til `id:` i `data/begrep/brreg-begrep.yaml`, legg til same URI nedst i `.lock`-fila, commit
2. CI-sjekk: alle URI-ar i `.lock`-fila må framleis finst i datafila — manglar betyr at eit publisert begrep er fjerna (error)
3. Etter høsting bekrefta i Felles Begrepskatalog: oppdater kommentaren «Sist oppdatert» i `.lock`-fila

#### CI-sjekk: validate-published-uris

Legg til ein enkel CI-sjekk (bash-skript eller Make-regel) som køyrer ved kvar PR:

```bash
#!/usr/bin/env bash
# Sjekk at alle URI-ar i .lock-fila framleis finst i datafila
set -euo pipefail
LOCK="src/linkml/begrep/brreg-begrep/published-uris.lock"
DATA="data/begrep/brreg-begrep.yaml"
failed=0
while IFS= read -r uri; do
    [[ "$uri" =~ ^#|^$ ]] && continue
    if ! grep -qF "$uri" "$DATA"; then
        echo "FEIL: Publisert URI manglar frå datafila: $uri" >&2
        failed=1
    fi
done < "$LOCK"
exit $failed
```

Skriptet feilar PRen dersom nokon har fjerna eller endra eit `id:`-felt for eit
allereie publisert begrep. Eksempelfiler (`examples/`) er ikkje med i denne sjekken —
dei kan endrast fritt utan å bryte URI-kontrakten.

#### Handtering av endringar: deprecering

Dersom eit begrep faktisk må erstattast (t.d. feil namn, omdefiniering):

1. **Behald** det opphavlege begrepet i `data/begrep/brreg-begrep.yaml` — slett det ikkje
2. Legg til `er_erstatta_av: <ny-uri>` (`dct:isReplacedBy`) på det gamle begrepet
3. Legg til `erstattar: <gamal-uri>` (`dct:replaces`) på det nye begrepet
4. Vurder å merkje det gamle begrepet med `euvoc:status` → `deprecated`

Dette gir ein fullstendig sporbar historikk i katalogen og bevarer integriteten til
eksisterande lenkjer.

### Manglar `skos:ConceptScheme`

Den genererte `.ttl`-fila har `skos:Collection` men ikkje `skos:ConceptScheme`.
SKOS-AP-NO-Begrep krev ikkje `ConceptScheme` eksplisitt, men nokre validatorar
åtvarar. Vurder å legge til `skos:ConceptScheme`-støtte i `mcp-linkml-begrep-generator`.

### Høstingsfrekvens

Felles datakatalog styrer høstingsintervallet sjølv. For umiddelbar oppdatering
etter kvart push kan ein automatisere manuell høstingsutløysing via
[Catalog View API](https://data.norge.no/nb/technical/api) med Maskinporten-autentisering.
Dette er eit framtidig forbetringstiltak.

---

## Referansar

- [Felles Begrepskatalog](https://data.norge.no/concepts)
- [SKOS-AP-NO-Begrep-spesifikasjonen](https://informasjonsforvaltning.github.io/skos-ap-no-begrep/)
- [Dele data — data.norge.no](https://data.norge.no/nb/docs/sharing-data)
- [Publisere beskrivelsar](https://data.norge.no/nb/docs/sharing-data/publishing-data-descriptions)
- [Administrasjonsgrensesnitt](https://admin.fellesdatakatalog.digdir.no/data-sources)
- [Innlogging og tilgang](https://data.norge.no/nb/docs/sharing-data/login-and-access)
