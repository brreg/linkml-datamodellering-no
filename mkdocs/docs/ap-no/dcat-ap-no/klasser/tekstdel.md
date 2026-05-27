

# Class: Tekstdel 


_Ein tekstleg del av ein kvalitetsmerknad (Web Annotation)._





URI: [oa:TextualBody](http://www.w3.org/ns/oa#TextualBody)





```mermaid
 classDiagram
    class Tekstdel
    click Tekstdel href "../Tekstdel/"
      Tekstdel : format
        
          
    
        
        
        Tekstdel --> "0..1" String : format
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Tekstdel : har_verdi_tekstdel
        
          
    
        
        
        Tekstdel --> "1" String : har_verdi_tekstdel
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Tekstdel : id
        
          
    
        
        
        Tekstdel --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Tekstdel : spraak
        
          
    
        
        
        Tekstdel --> "*" Spraak : spraak
        click Spraak href "../Spraak/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [oa:TextualBody](http://www.w3.org/ns/oa#TextualBody) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_verdi_tekstdel](har_verdi_tekstdel.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstinnhaldet i tekstdelen |





  
  

  
  

  
  
    
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [format](format.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Filformat eller medietype (dct:format) |
| [spraak](spraak.md) | * <br/> [Spraak](spraak.md) | Språk brukt i ressursen (dct:language) |





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | [har_tekstdel](har_tekstdel.md) | range | [Tekstdel](tekstdel.md) |
| [Brukartilbakemelding](brukartilbakemelding.md) | [har_tekstdel](har_tekstdel.md) | range | [Tekstdel](tekstdel.md) |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | [har_tekstdel](har_tekstdel.md) | range | [Tekstdel](tekstdel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oa:TextualBody |
| native | https://data.norge.no/ap-no/dqv-ap-no/Tekstdel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Tekstdel
description: Ein tekstleg del av ein kvalitetsmerknad (Web Annotation).
from_schema: https://data.norge.no/ap-no/dqv-ap-no
slots:
- id
- har_verdi_tekstdel
- format
- spraak
slot_usage:
  har_verdi_tekstdel:
    name: har_verdi_tekstdel
    in_subset:
    - Obligatorisk
    required: true
  format:
    name: format
    in_subset:
    - Anbefalt
  spraak:
    name: spraak
    in_subset:
    - Anbefalt
class_uri: oa:TextualBody

```
</details>

### Induced

<details>
```yaml
name: Tekstdel
description: Ein tekstleg del av ein kvalitetsmerknad (Web Annotation).
from_schema: https://data.norge.no/ap-no/dqv-ap-no
slot_usage:
  har_verdi_tekstdel:
    name: har_verdi_tekstdel
    in_subset:
    - Obligatorisk
    required: true
  format:
    name: format
    in_subset:
    - Anbefalt
  spraak:
    name: spraak
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Tekstdel
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    range: uriorcurie
    required: true
  har_verdi_tekstdel:
    name: har_verdi_tekstdel
    description: Tekstinnhaldet i tekstdelen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dqv-ap-no
    slot_uri: rdfs:value
    owner: Tekstdel
    domain_of:
    - Tekstdel
    range: string
    required: true
  format:
    name: format
    description: Filformat eller medietype (dct:format).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:format
    owner: Tekstdel
    domain_of:
    - Tekstdel
    - Distribusjon
    - Datatjeneste
    range: string
  spraak:
    name: spraak
    description: Språk brukt i ressursen (dct:language).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:language
    owner: Tekstdel
    domain_of:
    - Tekstdel
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Katalogpost
    - Katalog
    range: Spraak
    multivalued: true
class_uri: oa:TextualBody

```
</details>