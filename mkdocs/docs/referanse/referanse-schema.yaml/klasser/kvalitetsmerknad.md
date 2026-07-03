

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
        
          
    
        
        
        Kvalitetsmerknad --> "*" Kvalitetsdimensjon : er_i_kvalitetsdimensjon
        click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
    

        
      Kvalitetsmerknad : er_motivert_av
        
          
    
        
        
        Kvalitetsmerknad --> "1" DqvMotivasjon : er_motivert_av
        click DqvMotivasjon href "../DqvMotivasjon/"
    

        
      Kvalitetsmerknad : har_maal
        
          
    
        
        
        Kvalitetsmerknad --> "0..1" Uriorcurie : har_maal
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Kvalitetsmerknad : har_merknad
        
          
    
        
        
        Kvalitetsmerknad --> "*" LangString : har_merknad
        click LangString href "../LangString/"
    

        
      Kvalitetsmerknad : har_tekstdel
        
          
    
        
        
        Kvalitetsmerknad --> "*" Tekstdel : har_tekstdel
        click Tekstdel href "../Tekstdel/"
    

        
      Kvalitetsmerknad : id
        
          
    
        
        
        Kvalitetsmerknad --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* **Kvalitetsmerknad**
    * [Brukartilbakemelding](brukartilbakemelding.md)
    * [Kvalitetssertifikat](kvalitetssertifikat.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqv:QualityAnnotation](http://www.w3.org/ns/dqv#QualityAnnotation) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [er_motivert_av](er_motivert_av.md) | 1 <br/> [DqvMotivasjon](dqvmotivasjon.md) | Motivasjonen bak kvalitetsmerknaden |





  
  

  
  

  
  
    
  

  
  
    
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | * <br/> [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld |
| [har_tekstdel](har_tekstdel.md) | * <br/> [Tekstdel](tekstdel.md) | Tekstleg innhald i merknaden (0 |





  
  

  
  

  
  

  
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_merknad](har_merknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad (rdfs:comment) |
| [har_maal](har_maal.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Datasett, distribusjon eller datatjeneste merknaden gjeld |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Unik URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](datasett.md) | [har_kvalitetsmerknad](har_kvalitetsmerknad.md) | range | [Kvalitetsmerknad](kvalitetsmerknad.md) |








## In Subsets


* [Metadata](metadata.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:QualityAnnotation |
| native | https://data.norge.no/ap-no/dqv-core/Kvalitetsmerknad |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetsmerknad
description: Ein merknad om kvaliteten til eit datasett.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
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
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
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
    description: Unik URI-identifikator for ressursen.
    from_schema: https://example.org/linkml/referanse
    rank: 1000
    slot_uri: dct:identifier
    identifier: true
    owner: Kvalitetsmerknad
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
  er_motivert_av:
    name: er_motivert_av
    description: Motivasjonen bak kvalitetsmerknaden.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: oa:motivatedBy
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    range: DqvMotivasjon
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    description: Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: dqv:inDimension
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    range: Kvalitetsdimensjon
    required: false
    multivalued: true
  har_tekstdel:
    name: har_tekstdel
    description: Tekstleg innhald i merknaden (0..n).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: oa:hasBody
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    range: Tekstdel
    multivalued: true
  har_merknad:
    name: har_merknad
    description: Fritekstmerknad (rdfs:comment).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: rdfs:comment
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    range: LangString
    multivalued: true
  har_maal:
    name: har_maal
    description: Datasett, distribusjon eller datatjeneste merknaden gjeld.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: oa:hasTarget
    owner: Kvalitetsmerknad
    domain_of:
    - Kvalitetsmerknad
    range: uriorcurie
class_uri: dqv:QualityAnnotation

```
</details>