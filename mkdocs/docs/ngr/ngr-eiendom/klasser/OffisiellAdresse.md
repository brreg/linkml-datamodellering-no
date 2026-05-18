

# Class: OffisiellAdresse 


_Offisiell adresse tildelt av kommunen. Tilhøyrer Domene adresse og forvaltast av Matrikkelen via NGR-adresse._





URI: [ngre:OffisiellAdresse](https://data.norge.no/vocabulary/ngr-eiendom#OffisiellAdresse)





```mermaid
 classDiagram
    class OffisiellAdresse
    click OffisiellAdresse href "../OffisiellAdresse/"
      OffisiellAdresse : id
        
          
    
        
        
        OffisiellAdresse --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:OffisiellAdresse](https://data.norge.no/vocabulary/ngr-eiendom#OffisiellAdresse) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [YtreInngang](ytreinngang.md) | [har_offisiell_adresse](har_offisiell_adresse.md) | range | [OffisiellAdresse](offisielladresse.md) |
| [Bruksenhet](bruksenhet.md) | [har_offisiell_adresse](har_offisiell_adresse.md) | range | [OffisiellAdresse](offisielladresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:OffisiellAdresse |
| native | https://data.norge.no/linkml/ngr-eiendom/OffisiellAdresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OffisiellAdresse
description: Offisiell adresse tildelt av kommunen. Tilhøyrer Domene adresse og forvaltast
  av Matrikkelen via NGR-adresse.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slots:
- id
class_uri: ngre:OffisiellAdresse

```
</details>

### Induced

<details>
```yaml
name: OffisiellAdresse
description: Offisiell adresse tildelt av kommunen. Tilhøyrer Domene adresse og forvaltast
  av Matrikkelen via NGR-adresse.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    identifier: true
    alias: id
    owner: OffisiellAdresse
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
class_uri: ngre:OffisiellAdresse

```
</details>