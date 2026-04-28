

# Class: RegulativRessurs 


_Ein regulativ ressurs (lov, forskrift o.l.) som gjeld for ein ressurs._





URI: [eli:LegalResource](http://data.europa.eu/eli/ontology#LegalResource)





```mermaid
 classDiagram
    class RegulativRessurs
    click RegulativRessurs href "../RegulativRessurs/"
      RegulativRessurs : beskrivelse
        
      RegulativRessurs : har_referanse
        
      RegulativRessurs : id
        
      RegulativRessurs : identifikator_literal
        
      RegulativRessurs : relatert_regulativ_ressurs
        
          
    
        
        
        RegulativRessurs --> "*" RegulativRessurs : relatert_regulativ_ressurs
        click RegulativRessurs href "../RegulativRessurs/"
    

        
      RegulativRessurs : sprak
        
          
    
        
        
        RegulativRessurs --> "*" Spraak : sprak
        click Spraak href "../Spraak/"
    

        
      RegulativRessurs : tittel
        
      RegulativRessurs : type_concept
        
          
    
        
        
        RegulativRessurs --> "0..1" Begrep : type_concept
        click Begrep href "../Begrep/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [eli:LegalResource](http://data.europa.eu/eli/ontology#LegalResource) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](LangString.md) | Fritekstbeskrivelse av ressursen (dct:description) | direct |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [String](String.md) | Tekstleg identifikator for ressursen (dct:identifier) | direct |
| [har_referanse](har_referanse.md) | * <br/> [Uri](Uri.md) | Referanse til ekstern ressurs (rdfs:seeAlso) | direct |
| [sprak](sprak.md) | * <br/> [Spraak](Spraak.md) | Språk brukt i ressursen (dct:language) | direct |
| [tittel](tittel.md) | * <br/> [LangString](LangString.md) | Namn/tittel på ressursen (dct:title) | direct |
| [type_concept](type_concept.md) | 0..1 <br/> [Begrep](Begrep.md) | Type ressurs frå eit kontrollert vokabular (dct:type) | direct |
| [relatert_regulativ_ressurs](relatert_regulativ_ressurs.md) | * <br/> [RegulativRessurs](RegulativRessurs.md) | Relatert regulativ ressurs | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [regulativeRessursar](regulativeRessursar.md) | range | [RegulativRessurs](RegulativRessurs.md) |
| [RegulativRessurs](RegulativRessurs.md) | [relatert_regulativ_ressurs](relatert_regulativ_ressurs.md) | range | [RegulativRessurs](RegulativRessurs.md) |
| [Distribusjon](Distribusjon.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](RegulativRessurs.md) |
| [Datasett](Datasett.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](RegulativRessurs.md) |
| [Datasettserie](Datasettserie.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](RegulativRessurs.md) |
| [Datatjeneste](Datatjeneste.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](RegulativRessurs.md) |
| [Katalog](Katalog.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](RegulativRessurs.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | eli:LegalResource |
| native | https://data.norge.no/linkml/dcat-ap-no/RegulativRessurs |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RegulativRessurs
description: Ein regulativ ressurs (lov, forskrift o.l.) som gjeld for ein ressurs.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
- beskrivelse
- identifikator_literal
- har_referanse
- sprak
- tittel
- type_concept
- relatert_regulativ_ressurs
class_uri: eli:LegalResource

```
</details>

### Induced

<details>
```yaml
name: RegulativRessurs
description: Ein regulativ ressurs (lov, forskrift o.l.) som gjeld for ein ressurs.
from_schema: https://data.norge.no/linkml/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: RegulativRessurs
    domain_of:
    - Frekvens
    - ProvenanceStatement
    - OdrlPolicy
    - ProvAktivitet
    - ProvAttributering
    - Tidsinstant
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - Standard
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Katalogpost
    - Spraak
    - Mediatype
    - Begrep
    - Begrepssamling
    range: uriorcurie
    required: true
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dct:description
    alias: beskrivelse
    owner: RegulativRessurs
    domain_of:
    - RegulativRessurs
    - Gebyr
    - Distribusjon
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalogpost
    - Katalog
    range: LangString
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dct:identifier
    alias: identifikator_literal
    owner: RegulativRessurs
    domain_of:
    - Aktor
    - RegulativRessurs
    - Datasett
    - Datatjeneste
    - Katalog
    range: string
  har_referanse:
    name: har_referanse
    description: Referanse til ekstern ressurs (rdfs:seeAlso).
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: rdfs:seeAlso
    alias: har_referanse
    owner: RegulativRessurs
    domain_of:
    - Standard
    - RegulativRessurs
    range: uri
    multivalued: true
  sprak:
    name: sprak
    description: Språk brukt i ressursen (dct:language).
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dct:language
    alias: sprak
    owner: RegulativRessurs
    domain_of:
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Katalogpost
    - Katalog
    range: Spraak
    multivalued: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dct:title
    alias: tittel
    owner: RegulativRessurs
    domain_of:
    - Standard
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalogpost
    - Katalog
    range: LangString
    multivalued: true
  type_concept:
    name: type_concept
    description: Type ressurs frå eit kontrollert vokabular (dct:type).
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dct:type
    alias: type_concept
    owner: RegulativRessurs
    domain_of:
    - Aktor
    - RegulativRessurs
    - Datasett
    range: Begrep
  relatert_regulativ_ressurs:
    name: relatert_regulativ_ressurs
    description: Relatert regulativ ressurs.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dct:relation
    alias: relatert_regulativ_ressurs
    owner: RegulativRessurs
    domain_of:
    - RegulativRessurs
    range: RegulativRessurs
    multivalued: true
class_uri: eli:LegalResource

```
</details>