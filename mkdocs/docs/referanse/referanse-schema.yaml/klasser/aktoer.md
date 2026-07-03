

# Class: Aktoer 


_Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs._





URI: [foaf:Agent](http://xmlns.com/foaf/0.1/Agent)





```mermaid
 classDiagram
    class Aktoer
    click Aktoer href "../Aktoer/"
      Aktoer : id
        
          
    
        
        
        Aktoer --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Aktoer : identifikator_literal
        
          
    
        
        
        Aktoer --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Aktoer : navn_aktoer
        
          
    
        
        
        Aktoer --> "1..*" LangString : navn_aktoer
        click LangString href "../LangString/"
    

        
      Aktoer : type_concept
        
          
    
        
        
        Aktoer --> "0..1" Konsept : type_concept
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
| [navn_aktoer](navn_aktoer.md) | 1..* <br/> [LangString](langstring.md) | Namn på aktøren |





  
  

  
  

  
  
    
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) |





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Unik URI-identifikator for ressursen |
| [type_concept](type_concept.md) | 0..1 <br/> [Konsept](konsept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](datasett.md) | [utgiver](utgiver.md) | range | [Aktoer](aktoer.md) |
| [Datasett](datasett.md) | [produsent](produsent.md) | range | [Aktoer](aktoer.md) |
| [Datasettserie](datasettserie.md) | [utgiver](utgiver.md) | range | [Aktoer](aktoer.md) |
| [Datatjeneste](datatjeneste.md) | [utgiver](utgiver.md) | range | [Aktoer](aktoer.md) |
| [Katalog](katalog.md) | [utgiver](utgiver.md) | range | [Aktoer](aktoer.md) |
| [Katalog](katalog.md) | [produsent](produsent.md) | range | [Aktoer](aktoer.md) |








## In Subsets


* [Metadata](metadata.md)




## See Also

* [https://data.norge.no/concepts/d85379a6-837b-3102-b202-999a99240d69](https://data.norge.no/concepts/d85379a6-837b-3102-b202-999a99240d69)



## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:Agent |
| native | https://data.norge.no/ap-no/dcat-ap-no/Aktoer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aktoer
description: Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
see_also:
- https://data.norge.no/concepts/d85379a6-837b-3102-b202-999a99240d69
slots:
- id
- navn_aktoer
- identifikator_literal
- type_concept
slot_usage:
  navn_aktoer:
    name: navn_aktoer
    in_subset:
    - Obligatorisk
    required: true
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Anbefalt
class_uri: foaf:Agent

```
</details>

### Induced

<details>
```yaml
name: Aktoer
description: Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
see_also:
- https://data.norge.no/concepts/d85379a6-837b-3102-b202-999a99240d69
slot_usage:
  navn_aktoer:
    name: navn_aktoer
    in_subset:
    - Obligatorisk
    required: true
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: Unik URI-identifikator for ressursen.
    from_schema: https://example.org/linkml/referanse
    rank: 1000
    slot_uri: dct:identifier
    identifier: true
    owner: Aktoer
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Tekstdel
    - KatalogisertRessurs
    - Aktoer
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
    - Datasett
    - Katalogpost
    - Ressurs
    range: uriorcurie
    required: true
  navn_aktoer:
    name: navn_aktoer
    description: Namn på aktøren.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: foaf:name
    owner: Aktoer
    domain_of:
    - Aktoer
    range: LangString
    required: true
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:identifier
    owner: Aktoer
    domain_of:
    - Aktoer
    - RegulativRessurs
    - Datasett
    - Datatjeneste
    - Katalog
    range: string
  type_concept:
    name: type_concept
    description: Type ressurs frå eit kontrollert vokabular (dct:type).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:type
    owner: Aktoer
    domain_of:
    - Aktoer
    - RegulativRessurs
    - Datasett
    range: Konsept
class_uri: foaf:Agent

```
</details>