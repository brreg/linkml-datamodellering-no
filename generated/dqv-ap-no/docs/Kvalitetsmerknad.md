

# Class: Kvalitetsmerknad 


_Ein merknad om kvaliteten til eit datasett._





URI: [dqv:QualityAnnotation](http://www.w3.org/ns/dqv#QualityAnnotation)





```mermaid
 classDiagram
    class Kvalitetsmerknad
    click Kvalitetsmerknad href "../Kvalitetsmerknad/"
      Kvalitetsmerknad <|-- Brukartilbakemelding
        click Brukartilbakemelding href "../Brukartilbakemelding/"
      Kvalitetsmerknad <|-- Kvalitetssertifikat
        click Kvalitetssertifikat href "../Kvalitetssertifikat/"
      
      Kvalitetsmerknad : er_i_kvalitetsdimensjon
        
          
    
        
        
        Kvalitetsmerknad --> "0..1" Kvalitetsdimensjon : er_i_kvalitetsdimensjon
        click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
    

        
      Kvalitetsmerknad : er_motivert_av
        
      Kvalitetsmerknad : har_maal
        
          
    
        
        
        Kvalitetsmerknad --> "0..1" DcatRessurs : har_maal
        click DcatRessurs href "../DcatRessurs/"
    

        
      Kvalitetsmerknad : har_merknad
        
      Kvalitetsmerknad : har_tekstdel
        
          
    
        
        
        Kvalitetsmerknad --> "0..1" Tekstdel : har_tekstdel
        click Tekstdel href "../Tekstdel/"
    

        
      Kvalitetsmerknad : id
        
      
```





## Inheritance
* **Kvalitetsmerknad**
    * [Brukartilbakemelding](Brukartilbakemelding.md)
    * [Kvalitetssertifikat](Kvalitetssertifikat.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqv:QualityAnnotation](http://www.w3.org/ns/dqv#QualityAnnotation) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [er_motivert_av](er_motivert_av.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Motivasjonen bak kvalitetsmerknaden (t |





  
  

  
  

  
  
    
  

  
  
    
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | 0..1 <br/> [Kvalitetsdimensjon](Kvalitetsdimensjon.md) | Kvalitetsdimensjonen denne merknaden eller standarden gjeld |
| [har_tekstdel](har_tekstdel.md) | 0..1 <br/> [Tekstdel](Tekstdel.md) | Tekstleg innhald i merknaden |





  
  

  
  

  
  

  
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_merknad](har_merknad.md) | * <br/> [LangString](LangString.md) | Fritekstmerknad (rdfs:comment) |
| [har_maal](har_maal.md) | 0..1 <br/> [DcatRessurs](DcatRessurs.md) | Ressursen merknaden gjeld |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [kvalitetsmerknader](kvalitetsmerknader.md) | range | [Kvalitetsmerknad](Kvalitetsmerknad.md) |
| [Datasett](Datasett.md) | [har_kvalitetsmerknad](har_kvalitetsmerknad.md) | range | [Kvalitetsmerknad](Kvalitetsmerknad.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:QualityAnnotation |
| native | https://data.norge.no/linkml/dqv-ap-no/Kvalitetsmerknad |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetsmerknad
description: Ein merknad om kvaliteten til eit datasett.
from_schema: https://data.norge.no/linkml/dqv-ap-no
slots:
- id
- er_motivert_av
- er_i_kvalitetsdimensjon
- har_tekstdel
- har_merknad
- har_maal
slot_usage:
  er_motivert_av:
    name: er_motivert_av
    in_subset:
    - Obligatorisk
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    in_subset:
    - Anbefalt
  har_tekstdel:
    name: har_tekstdel
    in_subset:
    - Anbefalt
  har_merknad:
    name: har_merknad
    in_subset:
    - Valgfri
  har_maal:
    name: har_maal
    in_subset:
    - Valgfri
class_uri: dqv:QualityAnnotation

```
</details>

### Induced

<details>
```yaml
name: Kvalitetsmerknad
description: Ein merknad om kvaliteten til eit datasett.
from_schema: https://data.norge.no/linkml/dqv-ap-no
slot_usage:
  er_motivert_av:
    name: er_motivert_av
    in_subset:
    - Obligatorisk
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    in_subset:
    - Anbefalt
  har_tekstdel:
    name: har_tekstdel
    in_subset:
    - Anbefalt
  har_merknad:
    name: har_merknad
    in_subset:
    - Valgfri
  har_maal:
    name: har_maal
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Kvalitetsmerknad
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
  er_motivert_av:
    name: er_motivert_av
    description: Motivasjonen bak kvalitetsmerknaden (t.d. oa:assessing).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: oa:motivatedBy
    alias: er_motivert_av
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    range: uriorcurie
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    description: Kvalitetsdimensjonen denne merknaden eller standarden gjeld.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: dqv:inDimension
    alias: er_i_kvalitetsdimensjon
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    - Standard
    range: Kvalitetsdimensjon
  har_tekstdel:
    name: har_tekstdel
    description: Tekstleg innhald i merknaden.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: oa:hasBody
    alias: har_tekstdel
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    range: Tekstdel
  har_merknad:
    name: har_merknad
    description: Fritekstmerknad (rdfs:comment).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: rdfs:comment
    alias: har_merknad
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    range: LangString
    multivalued: true
  har_maal:
    name: har_maal
    description: Ressursen merknaden gjeld.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: oa:hasTarget
    alias: har_maal
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    range: DcatRessurs
class_uri: dqv:QualityAnnotation

```
</details>