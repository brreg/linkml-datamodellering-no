

# Class: Hovedenhet 


_Ei hovudeining i Einingsregisteret. Juridisk person som kan ha undereiningar. Tilhøyrer Domene virksomhet._





URI: [ngre:Hovedenhet](https://data.norge.no/vocabulary/ngr-eiendom#Hovedenhet)





```mermaid
 classDiagram
    class Hovedenhet
    click Hovedenhet href "../Hovedenhet/"
      Hovedenhet : id
        
          
    
        
        
        Hovedenhet --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Hovedenhet](https://data.norge.no/vocabulary/ngr-eiendom#Hovedenhet) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Rettighetshaver](rettighetshaver.md) | [er_av_type_hovedenhet](er_av_type_hovedenhet.md) | range | [Hovedenhet](hovedenhet.md) |
| [Borettslag](borettslag.md) | [er_av_type_hovedenhet](er_av_type_hovedenhet.md) | range | [Hovedenhet](hovedenhet.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Hovedenhet |
| native | https://data.norge.no/ngr/ngr-eiendom/Hovedenhet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Hovedenhet
description: Ei hovudeining i Einingsregisteret. Juridisk person som kan ha undereiningar.
  Tilhøyrer Domene virksomhet.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slots:
- id
class_uri: ngre:Hovedenhet

```
</details>

### Induced

<details>
```yaml
name: Hovedenhet
description: Ei hovudeining i Einingsregisteret. Juridisk person som kan ha undereiningar.
  Tilhøyrer Domene virksomhet.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    identifier: true
    owner: Hovedenhet
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
class_uri: ngre:Hovedenhet

```
</details>