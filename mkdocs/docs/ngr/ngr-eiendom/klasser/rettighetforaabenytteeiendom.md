

# Class: RettighetForAaBenytteEiendom 


_Rettar og avtalar som er nødvendige for å kunne benytte eigedommen. Desse er registrerte som heftingar i Grunnboka på teneleg eigedom._





URI: [ngre:RettighetForAaBenytteEiendom](https://data.norge.no/vocabulary/ngr-eiendom#RettighetForAaBenytteEiendom)





```mermaid
 classDiagram
    class RettighetForAaBenytteEiendom
    click RettighetForAaBenytteEiendom href "../RettighetForAaBenytteEiendom/"
      RettighetForAaBenytteEiendom : id
        
          
    
        
        
        RettighetForAaBenytteEiendom --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:RettighetForAaBenytteEiendom](https://data.norge.no/vocabulary/ngr-eiendom#RettighetForAaBenytteEiendom) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | [rettigheter](rettigheter.md) | range | [RettighetForAaBenytteEiendom](rettighetforaabenytteeiendom.md) |
| [FastEiendom](fasteiendom.md) | [bestar_av_rettighet](bestar_av_rettighet.md) | range | [RettighetForAaBenytteEiendom](rettighetforaabenytteeiendom.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:RettighetForAaBenytteEiendom |
| native | https://data.norge.no/ngr/ngr-eiendom/RettighetForAaBenytteEiendom |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RettighetForAaBenytteEiendom
description: Rettar og avtalar som er nødvendige for å kunne benytte eigedommen. Desse
  er registrerte som heftingar i Grunnboka på teneleg eigedom.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slots:
- id
class_uri: ngre:RettighetForAaBenytteEiendom

```
</details>

### Induced

<details>
```yaml
name: RettighetForAaBenytteEiendom
description: Rettar og avtalar som er nødvendige for å kunne benytte eigedommen. Desse
  er registrerte som heftingar i Grunnboka på teneleg eigedom.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    identifier: true
    owner: RettighetForAaBenytteEiendom
    domain_of:
    - FastEiendom
    - SamletFastEiendom
    - Borettslagsandel
    - Matrikkelenhet
    - Matrikkelnummer
    - Kommunenummer
    - Gaardsnummer
    - Bruksnummer
    - Festenummer
    - Seksjonsnummer
    - Bygning
    - Bygningsnummer
    - Representasjonspunkt
    - YtreInngang
    - Bruksenhet
    - Bruksenhetsnummer
    - Etasje
    - Teig
    - Anleggsprojeksjonsflate
    - Eierforhold
    - Hjemmel
    - Andel
    - Rettighetshaver
    - TinglystHeftelse
    - RettighetForAaBenytteEiendom
    - Borettslag
    - OffisiellAdresse
    - Person
    - Hovedenhet
    - Kommune
    range: uriorcurie
    required: true
class_uri: ngre:RettighetForAaBenytteEiendom

```
</details>