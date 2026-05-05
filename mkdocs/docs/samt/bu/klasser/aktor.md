

# Class: Aktor 


_Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs._





URI: [foaf:Agent](http://xmlns.com/foaf/0.1/Agent)





```mermaid
 classDiagram
    class Aktor
    click Aktor href "../Aktor/"
      Aktor : id
        
      Aktor : identifikator_literal
        
      Aktor : navn_aktor
        
      Aktor : type_concept
        
          
    
        
        
        Aktor --> "0..1" Konsept : type_concept
        click Konsept href "../Konsept/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [foaf:Agent](http://xmlns.com/foaf/0.1/Agent) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [navn_aktor](navn_aktor.md) | 1..* <br/> [LangString](langstring.md) | Namn på aktøren |





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [String](string.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [type_concept](type_concept.md) | 0..1 <br/> [Konsept](konsept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](containerklasse.md) | [utgivere](utgivere.md) | range | [Aktor](aktor.md) |
| [Containerklasse](containerklasse.md) | [organisasjoner](organisasjoner.md) | range | [Aktor](aktor.md) |
| [Datasett](datasett.md) | [utgiver](utgiver.md) | range | [Aktor](aktor.md) |
| [Datasett](datasett.md) | [produsent](produsent.md) | range | [Aktor](aktor.md) |
| [Datasettserie](datasettserie.md) | [utgiver](utgiver.md) | range | [Aktor](aktor.md) |
| [Datatjeneste](datatjeneste.md) | [utgiver](utgiver.md) | range | [Aktor](aktor.md) |
| [Katalog](katalog.md) | [utgiver](utgiver.md) | range | [Aktor](aktor.md) |
| [Katalog](katalog.md) | [produsent](produsent.md) | range | [Aktor](aktor.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:Agent |
| native | samtbuskole:Aktor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aktor
description: Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs.
from_schema: https://example.no/ontology/samt-bu-skole
slots:
- id
- navn_aktor
- identifikator_literal
- type_concept
slot_usage:
  navn_aktor:
    name: navn_aktor
    in_subset:
    - Obligatorisk
    required: true
class_uri: foaf:Agent

```
</details>

### Induced

<details>
```yaml
name: Aktor
description: Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs.
from_schema: https://example.no/ontology/samt-bu-skole
slot_usage:
  navn_aktor:
    name: navn_aktor
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: id
    owner: Aktor
    domain_of:
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
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
    range: uriorcurie
    required: true
  navn_aktor:
    name: navn_aktor
    description: Namn på aktøren.
    in_subset:
    - Obligatorisk
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: foaf:name
    alias: navn_aktor
    owner: Aktor
    domain_of:
    - Aktor
    range: LangString
    required: true
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:identifier
    alias: identifikator_literal
    owner: Aktor
    domain_of:
    - Aktor
    - RegulativRessurs
    - Datasett
    - Datatjeneste
    - Katalog
    range: string
  type_concept:
    name: type_concept
    description: Type ressurs frå eit kontrollert vokabular (dct:type).
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:type
    alias: type_concept
    owner: Aktor
    domain_of:
    - Aktor
    - RegulativRessurs
    - Datasett
    range: Konsept
class_uri: foaf:Agent

```
</details>