

# Class: Teig 


_Eit samanhengande areal med same type grenser. Mangler ofte vannareal som høyrer til eigedommen. Grensene kan ha manglande eller dårleg nøyaktigheit._





URI: [ngre:Teig](https://data.norge.no/vocabulary/ngr-eiendom#Teig)





```mermaid
 classDiagram
    class Teig
    click Teig href "../Teig/"
      Teig : id
        
          
    
        
        
        Teig --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Teig](https://data.norge.no/vocabulary/ngr-eiendom#Teig) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | [teiger](teiger.md) | range | [Teig](teig.md) |
| [Matrikkelenhet](matrikkelenhet.md) | [er_del_av_teig](er_del_av_teig.md) | range | [Teig](teig.md) |
| [Matrikkelenhet](matrikkelenhet.md) | [har_teig](har_teig.md) | range | [Teig](teig.md) |
| [Grunneiendom](grunneiendom.md) | [er_del_av_teig](er_del_av_teig.md) | range | [Teig](teig.md) |
| [Grunneiendom](grunneiendom.md) | [har_teig](har_teig.md) | range | [Teig](teig.md) |
| [Festegrunn](festegrunn.md) | [er_del_av_teig](er_del_av_teig.md) | range | [Teig](teig.md) |
| [Festegrunn](festegrunn.md) | [har_teig](har_teig.md) | range | [Teig](teig.md) |
| [Jordsameie](jordsameie.md) | [er_del_av_teig](er_del_av_teig.md) | range | [Teig](teig.md) |
| [Jordsameie](jordsameie.md) | [har_teig](har_teig.md) | range | [Teig](teig.md) |
| [Eierseksjon](eierseksjon.md) | [er_del_av_teig](er_del_av_teig.md) | range | [Teig](teig.md) |
| [Eierseksjon](eierseksjon.md) | [har_teig](har_teig.md) | range | [Teig](teig.md) |
| [Anleggseiendom](anleggseiendom.md) | [er_del_av_teig](er_del_av_teig.md) | range | [Teig](teig.md) |
| [Anleggseiendom](anleggseiendom.md) | [har_teig](har_teig.md) | range | [Teig](teig.md) |
| [AnnenMatrikkelenhet](annenmatrikkelenhet.md) | [er_del_av_teig](er_del_av_teig.md) | range | [Teig](teig.md) |
| [AnnenMatrikkelenhet](annenmatrikkelenhet.md) | [har_teig](har_teig.md) | range | [Teig](teig.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Teig |
| native | https://data.norge.no/ngr/ngr-eiendom/Teig |




## Examples
### Example: Teig-teig-1

```yaml
id: ngre:eksempel/teig-1

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Teig
description: Eit samanhengande areal med same type grenser. Mangler ofte vannareal
  som høyrer til eigedommen. Grensene kan ha manglande eller dårleg nøyaktigheit.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slots:
- id
class_uri: ngre:Teig

```
</details>

### Induced

<details>
```yaml
name: Teig
description: Eit samanhengande areal med same type grenser. Mangler ofte vannareal
  som høyrer til eigedommen. Grensene kan ha manglande eller dårleg nøyaktigheit.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    identifier: true
    owner: Teig
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
class_uri: ngre:Teig

```
</details>