# Plan: dx-prof som LinkML-modell

## Bakgrunn

[Profiles Vocabulary (dx-prof)](https://www.w3.org/TR/dx-prof/) er ein W3C-standard
for å skildre relasjonar mellom spesifikasjonar, profiler av desse og støtteartefakter
(valideringsressursar, rettleiingar o.l.). Kjelde-ontologien ligg på:
`http://www.w3.org/ns/dx/prof/` (autorativt TTL: https://www.w3.org/TR/dx-prof/rdf/prof.ttl)

Ein LinkML-modell av dx-prof gjer det mogleg å:
- bruke dx-prof semantikk i LinkML-baserte skjema og domenemodeller
- formelt skildre at t.d. `dcat-ap-no` er ein `prof:Profile` av DCAT
- generere SHACL/OWL/JSON-Schema frå profil-registreringar

---

## Ontologi-analyse

Kjelde-TTL-en definerer:

### Klasser

| URI | rdfs:label | Merknad |
|---|---|---|
| `prof:Profile` | Profile | `rdfs:subClassOf dct:Standard` |
| `prof:ResourceDescriptor` | Resource Descriptor | Skildrar eit artefakt knytt til ein profil |
| `prof:ResourceRole` | Resource Role | `rdfs:subClassOf skos:Concept` |

### Objekteigedommar

| URI | rdfs:label | domain | range | Merknad |
|---|---|---|---|---|
| `prof:hasArtifact` | has artifact | ResourceDescriptor | rdfs:Resource | URL til nedlastbar fil |
| `prof:hasResource` | has resource | (ingen) | ResourceDescriptor | Knyter profil til RessursBeskrivelse |
| `prof:hasRole` | has role | ResourceDescriptor | skos:Concept | Funksjonen til eit artefakt |
| `prof:isProfileOf` | is profile of | Profile | dct:Standard | `subPropertyOf isTransitiveProfileOf` |
| `prof:isTransitiveProfileOf` | is transitive profile of | Profile | dct:Standard | Transitiv lukking av isProfileOf |
| `prof:isInheritedFrom` | is inherited from | ResourceDescriptor | Profile | Arva profil-deskriptor |

### Dataeigedommar

| URI | rdfs:label | domain | range |
|---|---|---|---|
| `prof:hasToken` | has token | Profile | xsd:token |

### Annotasjonseigedommar (frå dct:)

`dct:conformsTo` og `dct:format` er annoterte som relevante for dx-prof (men definerte i dct:).

---

## Plassering og importhierarki

```
src/linkml/ap-no/dx-prof/
├── dx-prof-schema.yaml
├── manifest.yaml
└── examples/
    └── dx-prof-eksempel.yaml
```

**Import:** `linkml:types` berre. dx-prof importerer ikkje common-ap-no — det er eit
W3C-vokabular som ligg *under* AP-NO-profilene i hierarkiet. Andre AP-NO-skjema som
treng `prof:`-klasser vil importere dette skjemaet direkte.

**Domain:** `ap-no` — saman med dei andre W3C-vokabularprofilane.

**Schema-ID:** `https://data.norge.no/ap-no/dx-prof`

---

## Steg 1 — Skriv `dx-prof-schema.yaml`

### Namngjeving (bokmål, jf. CLAUDE.md)

| prof: | LinkML-klassenamn | LinkML-slotsnamn |
|---|---|---|
| Profile | Profil | — |
| ResourceDescriptor | RessursBeskrivelse | — |
| ResourceRole | RessursRolle | — |
| hasArtifact | — | har_artefakt |
| hasResource | — | har_ressurs |
| hasRole | — | har_rolle |
| isProfileOf | — | er_profil_av |
| isTransitiveProfileOf | — | er_transitiv_profil_av |
| isInheritedFrom | — | er_arvet_fra |
| hasToken | — | har_token |

### Skjemastruktur

```yaml
id: https://data.norge.no/ap-no/dx-prof
name: dx-prof
title: Profiles Vocabulary (dx-prof)
description: >-
  W3C Profiles Vocabulary — skildrar relasjonar mellom spesifikasjonar,
  profiler og støtteartefakter. Basert på https://www.w3.org/TR/dx-prof/

version: "1.0.0"

prefixes:
  linkml:  https://w3id.org/linkml/
  prof:    http://www.w3.org/ns/dx/prof/
  dct:     http://purl.org/dc/terms/
  skos:    http://www.w3.org/2004/02/skos/core#
  rdfs:    http://www.w3.org/2000/01/rdf-schema#
  xsd:     http://www.w3.org/2001/XMLSchema#

default_prefix: https://data.norge.no/ap-no/dx-prof/
default_range: string

imports:
  - linkml:types

classes:
  Standard:              # dct:Standard — nødvendig for range på isProfileOf
    class_uri: dct:Standard
    mixin: true
    description: Ein etablert standard.

  Konsept:               # skos:Concept — nødvendig for range på hasRole
    class_uri: skos:Concept
    mixin: true
    description: Eit SKOS-omgrep.

  Profil:
    class_uri: prof:Profile
    is_a: Standard
    description: >-
      Ein spesifikasjon som avgrenser, utvidar, kombinerer eller rettleier bruk av
      andre spesifikasjonar. Inkluderer det som ofte kallast "applikasjonsprofil".
    slots:
      - id
      - har_ressurs
      - er_profil_av
      - er_transitiv_profil_av
      - har_token

  RessursBeskrivelse:
    class_uri: prof:ResourceDescriptor
    description: >-
      Ei skildring av ein ressurs som definerer eit aspekt av ein profil — ein
      del, eit trekk eller ei rolle — saman med formatet og rolla til ressursen.
    slots:
      - id
      - har_artefakt
      - har_rolle
      - er_arvet_fra

  RessursRolle:
    class_uri: prof:ResourceRole
    is_a: Konsept
    description: >-
      Ei rolle som ein profilressurs, skildra av RessursBeskrivelse, spelar.

slots:
  har_artefakt:
    slot_uri: prof:hasArtifact
    domain: RessursBeskrivelse
    range: uri
    description: URL til ei nedlastbar fil med opplysningar om format og rolle.

  har_ressurs:
    slot_uri: prof:hasResource
    range: RessursBeskrivelse
    multivalued: true
    description: Ein ressurs som skildrar naturen til eit artefakt og rolla det spelar for profilen.

  har_rolle:
    slot_uri: prof:hasRole
    domain: RessursBeskrivelse
    range: Konsept
    multivalued: true
    description: Funksjonen til eit artefakt skildra av RessursBeskrivelse.

  er_profil_av:
    slot_uri: prof:isProfileOf
    domain: Profil
    range: Standard
    multivalued: true
    description: Ein spesifikasjon som denne profilen avgrensar, utvidar eller kombinerer.

  er_transitiv_profil_av:
    slot_uri: prof:isTransitiveProfileOf
    domain: Profil
    range: Standard
    multivalued: true
    description: Transitiv lukking av er_profil_av — alle spesifikasjonar profilen er avleidd av.

  er_arvet_fra:
    slot_uri: prof:isInheritedFrom
    domain: RessursBeskrivelse
    range: Profil
    description: >-
      Ein basispesifikasjon som sin RessursBeskrivelse òg skal reknast
      som RessursBeskrivelse for denne profilen.

  har_token:
    slot_uri: prof:hasToken
    domain: Profil
    range: string
    description: Føretrekt kortnamn for profilen, til bruk der URI ikkje kan nyttast.
```

---

## Steg 2 — Skriv `manifest.yaml`

```yaml
publish_external: false

generators:
  jsonld_context: true
  shacl: true
  python: false
  json_schema: true
  owl: true          # ← hovudformålet: OWL for innhaldssamanlikning
  rdf: false
  protobuf: false
  erdiagram: true
  docs: true
  plantuml: false
  example_rdf: false
```

---

## Steg 3 — Skriv eksempelfil

`examples/dx-prof-eksempel.yaml` — ein minimal instans som demonstrerer
at `Profil` kan ha `RessursBeskrivelse` med `RessursRolle`:

```yaml
profiler:
  - id: https://example.org/profil/eksempel-ap
    er_profil_av:
      - https://www.w3.org/TR/vocab-dcat-2/
    har_token: eksempel-ap
    har_ressurs:
      - https://example.org/profil/eksempel-ap/shacl

ressursbeskrivingar:
  - id: https://example.org/profil/eksempel-ap/shacl
    har_artefakt: https://example.org/profil/eksempel-ap/shacl.ttl
    har_rolle:
      - http://www.w3.org/ns/dx/prof/role/validation

ressursroller:
  - id: http://www.w3.org/ns/dx/prof/role/validation
```

(Containerklassen `DxProfContainer` med `tree_root: true` og attributtane
`profiler`, `ressursbeskrivingar`, `ressursroller`.)

---

## Steg 4 — Generer OWL og valider innhald

### 4a — Generer OWL

```bash
make mcp-validate SCHEMA=src/linkml/ap-no/dx-prof/dx-prof-schema.yaml POLICY=bronze
make domain-gen-owl DOMAIN=ap-no   # eller enkeltskjema via make gen-owl
```

Outputfila: `generated/ap-no/dx-prof/dx-prof.owl.ttl`

### 4b — Innhaldssamanlikning mot kjelde-TTL

LinkML sin `gen-owl` produserer gyldig OWL, men er ikkje strukturelt identisk med
kjeldontologien. Ein innhaldssamanlikning må sjekke *semantikk*, ikkje syntaks:

**Kva som skal kontrollerast:**

| Sjekk | Kjelde (prof.ttl) | Forventa i generert OWL |
|---|---|---|
| Alle klasser finst | Profile, ResourceDescriptor, ResourceRole | ✓ som `owl:Class` |
| Alle objekteigedommar finst | hasArtifact, hasResource, hasRole, isProfileOf, isTransitiveProfileOf, isInheritedFrom | ✓ som `owl:ObjectProperty` |
| Dataeigedommar finst | hasToken | ✓ som `owl:DatatypeProperty` |
| `rdfs:subClassOf` | Profile → dct:Standard, ResourceRole → skos:Concept | ✓ |
| `rdfs:subPropertyOf` | isProfileOf → isTransitiveProfileOf | ✓ |
| `rdfs:domain` per eigendom | ResourceDescriptor for hasArtifact, hasRole, isInheritedFrom; Profile for isProfileOf o.fl. | ✓ |
| `rdfs:range` per eigendom | prof:ResourceDescriptor, skos:Concept, dct:Standard, prof:Profile, xsd:token | ✓ |
| `skos:definition` | Alle 10 omgrep har definisjon | Bør kartleggast til `rdfs:comment` eller `skos:definition` |

**Valideringsskript:** `src/assets/scripts/validate-owl-vs-source.py`

```python
# Køyrast manuelt: python3 validate-owl-vs-source.py \
#   generated/ap-no/dx-prof/dx-prof.owl.ttl \
#   https://www.w3.org/TR/dx-prof/rdf/prof.ttl

# Nyttar rdflib (tilgjengeleg i python-pytest-image).
# Lastar begge grafar, sjekkar:
# 1. Alle URIar frå prof: som er owl:Class/owl:ObjectProperty/owl:DatatypeProperty
#    finst i generert graf
# 2. rdfs:subClassOf, rdfs:subPropertyOf, rdfs:domain, rdfs:range er identiske
# 3. Rapporterer prosentvis dekning og manglar
```

Alternativt kan ein bruke `make`-kommandoen med `podman run` og det eksisterande
`python-pytest`-imaget — same mønster som andre Python-skript i `src/assets/scripts/`.

### 4c — Kjende avvik (aksepterte)

LinkML `gen-owl` vil avvike frå prof.ttl på desse punktane, som er *forventa og aksepterte*:

| Avvik | Grunn |
|---|---|
| Ekstra LinkML-metadata (linkml:, owl:imports) | LinkML-generert boilerplate |
| `skos:definition` → `rdfs:comment` | LinkML mappar `description:` til `rdfs:comment` |
| Klassar utan `owl:Class`-eksplisitt-deklarasjon (mixin) | LinkML brukar eigne OWL-mønster |
| Domene/range uttrykt som `owl:Restriction` | LinkML-konvensjon for slot constraints |
| `dc:contributor`, `dct:creator` metadata manglar | Bibliografisk metadata — ikkje modellert |

---

## Steg 5 — Integrasjon i importhierarki

Etter ferdigstilling kan andre skjema importere dx-prof:

```yaml
# t.d. i common-ap-no-schema.yaml:
imports:
  - linkml:types
  - ../dx-prof/dx-prof-schema
```

Dette gjer `Profil`, `RessursBeskrivelse` og tilhøyrande slots tilgjengeleg i alle
AP-NO-profil-skjema utan duplisering.

---

## Prioritert handlingsliste

| # | Steg | Fil | Merknad |
|---|---|---|---|
| 1 | Skjema | `src/linkml/ap-no/dx-prof/dx-prof-schema.yaml` | Implementer etter specen over |
| 2 | Manifest | `src/linkml/ap-no/dx-prof/manifest.yaml` | `owl: true` er obligatorisk |
| 3 | Eksempel | `src/linkml/ap-no/dx-prof/examples/dx-prof-eksempel.yaml` | Containerklasse + minimal instans |
| 4 | Bronze-validering | — | `make mcp-validate ... POLICY=bronze` |
| 5 | OWL-generering | `generated/ap-no/dx-prof/dx-prof.owl.ttl` | Verifiser at `gen-owl` lukkast |
| 6 | Valideringsskript | `src/assets/scripts/validate-owl-vs-source.py` | rdflib-basert innhaldssjekk |
| 7 | Importintegrasjon | `common-ap-no-schema.yaml` (valfritt) | Berre om andre skjema treng prof:-klasser |

---

## Avhengigheiter

- Ingen nye container-images nødvendig — `gen-owl` køyrer i eksisterande `linkml-local`-image
- `rdflib` finst i `python-pytest`-imaget for valideringsskriptet
- Ingen endringar i CI-workflows nødvendig (ap-no-domenet er allereie med i matrix)
