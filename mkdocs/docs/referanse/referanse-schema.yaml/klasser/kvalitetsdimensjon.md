

# Class: Kvalitetsdimensjon 


_Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål._





URI: [dqv:Dimension](http://www.w3.org/ns/dqv#Dimension)





```mermaid
 classDiagram
    class Kvalitetsdimensjon
    click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
      Kvalitetsdimensjon <|-- Kvalitetsdeldimensjon
        click Kvalitetsdeldimensjon href "../Kvalitetsdeldimensjon/"
      
      Kvalitetsdimensjon : gjelder_standard
        
          
    
        
        
        Kvalitetsdimensjon --> "*" Uriorcurie : gjelder_standard
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Kvalitetsdimensjon : har_anbefalt_term
        
          
    
        
        
        Kvalitetsdimensjon --> "*" LangString : har_anbefalt_term
        click LangString href "../LangString/"
    

        
      Kvalitetsdimensjon : har_kvalitetsdefinisjon
        
          
    
        
        
        Kvalitetsdimensjon --> "*" LangString : har_kvalitetsdefinisjon
        click LangString href "../LangString/"
    

        
      Kvalitetsdimensjon : id
        
          
    
        
        
        Kvalitetsdimensjon --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* **Kvalitetsdimensjon**
    * [Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqv:Dimension](http://www.w3.org/ns/dqv#Dimension) |


## Eigenskapar







  
  

  
  

  
  

  
  





  
  

  
  
    
  

  
  
    
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_anbefalt_term](har_anbefalt_term.md) | * <br/> [LangString](langstring.md) | Føretrekt term/namn for dimensjonen eller målet |
| [har_kvalitetsdefinisjon](har_kvalitetsdefinisjon.md) | * <br/> [LangString](langstring.md) | Definisjon av dimensjonen eller målet |
| [gjelder_standard](gjelder_standard.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Standard(ar) denne kvalitetsdimensjonen gjeld for |





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Unik URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md) | [er_deldimensjon_av](er_deldimensjon_av.md) | range | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | range | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |
| [Brukartilbakemelding](brukartilbakemelding.md) | [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | range | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | range | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |








## In Subsets


* [Metadata](metadata.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:Dimension |
| native | https://data.norge.no/ap-no/dqv-core/Kvalitetsdimensjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetsdimensjon
description: Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
slots:
- id
- har_anbefalt_term
- har_kvalitetsdefinisjon
- gjelder_standard
slot_usage:
  har_anbefalt_term:
    name: har_anbefalt_term
    in_subset:
    - Anbefalt
  har_kvalitetsdefinisjon:
    name: har_kvalitetsdefinisjon
    in_subset:
    - Anbefalt
  gjelder_standard:
    name: gjelder_standard
    in_subset:
    - Anbefalt
class_uri: dqv:Dimension

```
</details>

### Induced

<details>
```yaml
name: Kvalitetsdimensjon
description: Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
slot_usage:
  har_anbefalt_term:
    name: har_anbefalt_term
    in_subset:
    - Anbefalt
  har_kvalitetsdefinisjon:
    name: har_kvalitetsdefinisjon
    in_subset:
    - Anbefalt
  gjelder_standard:
    name: gjelder_standard
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
    owner: Kvalitetsdimensjon
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
  har_anbefalt_term:
    name: har_anbefalt_term
    description: Føretrekt term/namn for dimensjonen eller målet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: skos:prefLabel
    owner: Kvalitetsdimensjon
    domain_of:
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    range: LangString
    multivalued: true
  har_kvalitetsdefinisjon:
    name: har_kvalitetsdefinisjon
    description: Definisjon av dimensjonen eller målet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: skos:definition
    owner: Kvalitetsdimensjon
    domain_of:
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    range: LangString
    multivalued: true
  gjelder_standard:
    name: gjelder_standard
    description: Standard(ar) denne kvalitetsdimensjonen gjeld for.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: dqvno:appliesToStandard
    owner: Kvalitetsdimensjon
    domain_of:
    - Kvalitetsdimensjon
    range: uriorcurie
    multivalued: true
class_uri: dqv:Dimension

```
</details>