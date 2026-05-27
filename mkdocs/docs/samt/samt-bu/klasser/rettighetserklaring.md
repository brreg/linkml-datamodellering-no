

# Class: Rettighetserklaring 


_Ei erklæring om rettar til ein ressurs (ODRS)._





URI: [dct:RightsStatement](http://purl.org/dc/terms/RightsStatement)





```mermaid
 classDiagram
    class Rettighetserklaring
    click Rettighetserklaring href "../Rettighetserklaring/"
      Rettighetserklaring : anvendelsesretningslinjer
        
          
    
        
        
        Rettighetserklaring --> "0..1" String : anvendelsesretningslinjer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Rettighetserklaring : id
        
          
    
        
        
        Rettighetserklaring --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Rettighetserklaring : jurisdiksjon
        
          
    
        
        
        Rettighetserklaring --> "0..1" String : jurisdiksjon
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Rettighetserklaring : krediteringstekst
        
          
    
        
        
        Rettighetserklaring --> "0..1" String : krediteringstekst
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Rettighetserklaring : krediteringsurl
        
          
    
        
        
        Rettighetserklaring --> "0..1" Uri : krediteringsurl
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Rettighetserklaring : opphavsrettsaar
        
          
    
        
        
        Rettighetserklaring --> "0..1" GYear : opphavsrettsaar
        click GYear href "../GYear/"
    

        
      Rettighetserklaring : opphavsrettserklaring
        
          
    
        
        
        Rettighetserklaring --> "0..1" String : opphavsrettserklaring
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Rettighetserklaring : opphavsrettsinnehaver
        
          
    
        
        
        Rettighetserklaring --> "0..1" String : opphavsrettsinnehaver
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Rettighetserklaring : opphavsrettsnotis
        
          
    
        
        
        Rettighetserklaring --> "0..1" String : opphavsrettsnotis
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dct:RightsStatement](http://purl.org/dc/terms/RightsStatement) |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |
| [anvendelsesretningslinjer](anvendelsesretningslinjer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Retningslinjer for gjenbruk av data |
| [jurisdiksjon](jurisdiksjon.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Jurisdiksjon for rettigheitserklæringa |
| [krediteringstekst](krediteringstekst.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekst som skal brukast ved kreditering |
| [krediteringsurl](krediteringsurl.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URL for kreditering av rettshavar |
| [opphavsrettserklaring](opphavsrettserklaring.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Opphavsrettserklæring |
| [opphavsrettsinnehaver](opphavsrettsinnehaver.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på opphavsrettsinnehavar |
| [opphavsrettsnotis](opphavsrettsnotis.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Opphavsrettsnotis |
| [opphavsrettsaar](opphavsrettsaar.md) | 0..1 <br/> [GYear](gyear.md) | Årstal for opphavsrett |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Distribusjon](distribusjon.md) | [rettigheter](rettigheter.md) | range | [Rettighetserklaring](rettighetserklaring.md) |
| [Datatjeneste](datatjeneste.md) | [rettigheter](rettigheter.md) | range | [Rettighetserklaring](rettighetserklaring.md) |
| [Katalog](katalog.md) | [rettigheter](rettigheter.md) | range | [Rettighetserklaring](rettighetserklaring.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:RightsStatement |
| native | https://data.norge.no/ap-no/dcat-ap-no/Rettighetserklaring |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Rettighetserklaring
description: Ei erklæring om rettar til ein ressurs (ODRS).
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slots:
- id
- anvendelsesretningslinjer
- jurisdiksjon
- krediteringstekst
- krediteringsurl
- opphavsrettserklaring
- opphavsrettsinnehaver
- opphavsrettsnotis
- opphavsrettsaar
class_uri: dct:RightsStatement

```
</details>

### Induced

<details>
```yaml
name: Rettighetserklaring
description: Ei erklæring om rettar til ein ressurs (ODRS).
from_schema: https://data.norge.no/ap-no/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Rettighetserklaring
    domain_of:
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
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    - SamtBuContainer
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: uriorcurie
    required: true
  anvendelsesretningslinjer:
    name: anvendelsesretningslinjer
    description: Retningslinjer for gjenbruk av data.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: odrs:reuserGuidelines
    owner: Rettighetserklaring
    domain_of:
    - Rettighetserklaring
    range: string
  jurisdiksjon:
    name: jurisdiksjon
    description: Jurisdiksjon for rettigheitserklæringa.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: odrs:jurisdiction
    owner: Rettighetserklaring
    domain_of:
    - Rettighetserklaring
    range: string
  krediteringstekst:
    name: krediteringstekst
    description: Tekst som skal brukast ved kreditering.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: odrs:attributionText
    owner: Rettighetserklaring
    domain_of:
    - Rettighetserklaring
    range: string
  krediteringsurl:
    name: krediteringsurl
    description: URL for kreditering av rettshavar.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: odrs:attributionURL
    owner: Rettighetserklaring
    domain_of:
    - Rettighetserklaring
    range: uri
  opphavsrettserklaring:
    name: opphavsrettserklaring
    description: Opphavsrettserklæring.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: odrs:copyrightStatement
    owner: Rettighetserklaring
    domain_of:
    - Rettighetserklaring
    range: string
  opphavsrettsinnehaver:
    name: opphavsrettsinnehaver
    description: Namn på opphavsrettsinnehavar.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: odrs:copyrightHolder
    owner: Rettighetserklaring
    domain_of:
    - Rettighetserklaring
    range: string
  opphavsrettsnotis:
    name: opphavsrettsnotis
    description: Opphavsrettsnotis.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: odrs:copyrightNotice
    owner: Rettighetserklaring
    domain_of:
    - Rettighetserklaring
    range: string
  opphavsrettsaar:
    name: opphavsrettsaar
    description: Årstal for opphavsrett.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: odrs:copyrightYear
    owner: Rettighetserklaring
    domain_of:
    - Rettighetserklaring
    range: GYear
class_uri: dct:RightsStatement

```
</details>