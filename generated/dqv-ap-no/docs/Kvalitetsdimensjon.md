

# Class: Kvalitetsdimensjon 


_Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål._





URI: [dqv:Dimension](http://www.w3.org/ns/dqv#Dimension)





```mermaid
 classDiagram
    class Kvalitetsdimensjon
    click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
      Kvalitetsdimensjon <|-- Kvalitetsdeldimensjon
        click Kvalitetsdeldimensjon href "../Kvalitetsdeldimensjon/"
      
      Kvalitetsdimensjon : har_anbefalt_term
        
      Kvalitetsdimensjon : har_definisjon
        
      Kvalitetsdimensjon : id
        
      
```





## Inheritance
* **Kvalitetsdimensjon**
    * [Kvalitetsdeldimensjon](Kvalitetsdeldimensjon.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqv:Dimension](http://www.w3.org/ns/dqv#Dimension) |


## Eigenskapar







  
  

  
  

  
  





  
  

  
  
    
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_anbefalt_term](har_anbefalt_term.md) | * <br/> [LangString](LangString.md) | Føretrekt term/namn for dimensjonen eller målet |
| [har_definisjon](har_definisjon.md) | * <br/> [LangString](LangString.md) | Definisjon av dimensjonen eller målet |





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [kvalitetsdimensjonar](kvalitetsdimensjonar.md) | range | [Kvalitetsdimensjon](Kvalitetsdimensjon.md) |
| [Kvalitetsdeldimensjon](Kvalitetsdeldimensjon.md) | [er_deldimensjon_av](er_deldimensjon_av.md) | range | [Kvalitetsdimensjon](Kvalitetsdimensjon.md) |
| [Kvalitetsmerknad](Kvalitetsmerknad.md) | [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | range | [Kvalitetsdimensjon](Kvalitetsdimensjon.md) |
| [Brukartilbakemelding](Brukartilbakemelding.md) | [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | range | [Kvalitetsdimensjon](Kvalitetsdimensjon.md) |
| [Kvalitetssertifikat](Kvalitetssertifikat.md) | [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | range | [Kvalitetsdimensjon](Kvalitetsdimensjon.md) |
| [Standard](Standard.md) | [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | range | [Kvalitetsdimensjon](Kvalitetsdimensjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:Dimension |
| native | https://data.norge.no/linkml/dqv-ap-no/Kvalitetsdimensjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetsdimensjon
description: Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål.
from_schema: https://data.norge.no/linkml/dqv-ap-no
slots:
- id
- har_anbefalt_term
- har_definisjon
slot_usage:
  har_anbefalt_term:
    name: har_anbefalt_term
    in_subset:
    - Anbefalt
  har_definisjon:
    name: har_definisjon
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
from_schema: https://data.norge.no/linkml/dqv-ap-no
slot_usage:
  har_anbefalt_term:
    name: har_anbefalt_term
    in_subset:
    - Anbefalt
  har_definisjon:
    name: har_definisjon
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Kvalitetsdimensjon
    domain_of:
    - DcatRessurs
    - Datasett
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    - Motivasjon
    - Spraak
    - Mediatype
    - Begrep
    - Begrepssamling
    range: uriorcurie
    required: true
  har_anbefalt_term:
    name: har_anbefalt_term
    description: Føretrekt term/namn for dimensjonen eller målet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: skos:prefLabel
    alias: har_anbefalt_term
    owner: Kvalitetsdimensjon
    domain_of:
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    range: LangString
    multivalued: true
  har_definisjon:
    name: har_definisjon
    description: Definisjon av dimensjonen eller målet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: skos:definition
    alias: har_definisjon
    owner: Kvalitetsdimensjon
    domain_of:
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    range: LangString
    multivalued: true
class_uri: dqv:Dimension

```
</details>