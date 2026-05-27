

# Class: TinglystHeftelse 


_Heftelse tinglyst i Grunnboka mot ein eigedom eller burettslagsandel. Nokre heftingar har avgrensa geografisk utbreiing og manglar stadfestring._





URI: [ngre:TinglystHeftelse](https://data.norge.no/vocabulary/ngr-eiendom#TinglystHeftelse)





```mermaid
 classDiagram
    class TinglystHeftelse
    click TinglystHeftelse href "../TinglystHeftelse/"
      TinglystHeftelse : id
        
          
    
        
        
        TinglystHeftelse --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:TinglystHeftelse](https://data.norge.no/vocabulary/ngr-eiendom#TinglystHeftelse) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | [tinglystHeftelser](tinglystheftelser.md) | range | [TinglystHeftelse](tinglystheftelse.md) |
| [FastEiendom](fasteiendom.md) | [har_tinglyst_heftelse](har_tinglyst_heftelse.md) | range | [TinglystHeftelse](tinglystheftelse.md) |
| [Borettslagsandel](borettslagsandel.md) | [har_tinglyst_heftelse](har_tinglyst_heftelse.md) | range | [TinglystHeftelse](tinglystheftelse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:TinglystHeftelse |
| native | https://data.norge.no/ngr/ngr-eiendom/TinglystHeftelse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TinglystHeftelse
description: Heftelse tinglyst i Grunnboka mot ein eigedom eller burettslagsandel.
  Nokre heftingar har avgrensa geografisk utbreiing og manglar stadfestring.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slots:
- id
class_uri: ngre:TinglystHeftelse

```
</details>

### Induced

<details>
```yaml
name: TinglystHeftelse
description: Heftelse tinglyst i Grunnboka mot ein eigedom eller burettslagsandel.
  Nokre heftingar har avgrensa geografisk utbreiing og manglar stadfestring.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    identifier: true
    owner: TinglystHeftelse
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
class_uri: ngre:TinglystHeftelse

```
</details>