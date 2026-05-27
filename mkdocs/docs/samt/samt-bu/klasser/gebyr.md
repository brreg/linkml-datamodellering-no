

# Class: Gebyr 


_Eit gebyr knytt til bruk av ein datatjeneste._





URI: [cv:Cost](http://data.europa.eu/m8g/Cost)





```mermaid
 classDiagram
    class Gebyr
    click Gebyr href "../Gebyr/"
      Gebyr : belop
        
          
    
        
        
        Gebyr --> "0..1" String : belop
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Gebyr : beskrivelse
        
          
    
        
        
        Gebyr --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Gebyr : dokumentasjon
        
          
    
        
        
        Gebyr --> "*" Uri : dokumentasjon
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Gebyr : id
        
          
    
        
        
        Gebyr --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Gebyr : valuta
        
          
    
        
        
        Gebyr --> "0..1" Konsept : valuta
        click Konsept href "../Konsept/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [cv:Cost](http://data.europa.eu/m8g/Cost) |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |
| [belop](belop.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Beløp for gebyret |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [dokumentasjon](dokumentasjon.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Lenke til dokumentasjon om ressursen |
| [valuta](valuta.md) | 0..1 <br/> [Konsept](konsept.md) | Valuta (cv:currency) |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | [har_gebyr](har_gebyr.md) | range | [Gebyr](gebyr.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:Cost |
| native | https://data.norge.no/ap-no/dcat-ap-no/Gebyr |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gebyr
description: Eit gebyr knytt til bruk av ein datatjeneste.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slots:
- id
- belop
- beskrivelse
- dokumentasjon
- valuta
class_uri: cv:Cost

```
</details>

### Induced

<details>
```yaml
name: Gebyr
description: Eit gebyr knytt til bruk av ein datatjeneste.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Gebyr
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
  belop:
    name: belop
    description: Beløp for gebyret.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: cv:hasValue
    owner: Gebyr
    domain_of:
    - Gebyr
    range: string
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:description
    owner: Gebyr
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
  dokumentasjon:
    name: dokumentasjon
    description: Lenke til dokumentasjon om ressursen.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: foaf:page
    owner: Gebyr
    domain_of:
    - Gebyr
    - Distribusjon
    - Datasett
    - Datatjeneste
    range: uri
    multivalued: true
  valuta:
    name: valuta
    description: Valuta (cv:currency).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: cv:currency
    owner: Gebyr
    domain_of:
    - Gebyr
    range: Konsept
class_uri: cv:Cost

```
</details>