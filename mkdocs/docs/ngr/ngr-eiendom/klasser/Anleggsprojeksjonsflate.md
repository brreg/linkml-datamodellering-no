

# Class: Anleggsprojeksjonsflate 


_Fotavtrykk av 3D-eigedommar (anleggseigedommar). Manglar volumet og må supplerast på oppdrag._





URI: [ngre:Anleggsprojeksjonsflate](https://data.norge.no/vocabulary/ngr-eiendom#Anleggsprojeksjonsflate)





```mermaid
 classDiagram
    class Anleggsprojeksjonsflate
    click Anleggsprojeksjonsflate href "../Anleggsprojeksjonsflate/"
      Anleggsprojeksjonsflate : id
        
          
    
        
        
        Anleggsprojeksjonsflate --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Anleggsprojeksjonsflate](https://data.norge.no/vocabulary/ngr-eiendom#Anleggsprojeksjonsflate) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Matrikkelenhet](matrikkelenhet.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](anleggsprojeksjonsflate.md) |
| [Grunneiendom](grunneiendom.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](anleggsprojeksjonsflate.md) |
| [Festegrunn](festegrunn.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](anleggsprojeksjonsflate.md) |
| [Jordsameie](jordsameie.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](anleggsprojeksjonsflate.md) |
| [Eierseksjon](eierseksjon.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](anleggsprojeksjonsflate.md) |
| [Anleggseiendom](anleggseiendom.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](anleggsprojeksjonsflate.md) |
| [AnnenMatrikkelenhet](annenmatrikkelenhet.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](anleggsprojeksjonsflate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Anleggsprojeksjonsflate |
| native | https://data.norge.no/linkml/ngr-eiendom/Anleggsprojeksjonsflate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Anleggsprojeksjonsflate
description: Fotavtrykk av 3D-eigedommar (anleggseigedommar). Manglar volumet og må
  supplerast på oppdrag.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slots:
- id
class_uri: ngre:Anleggsprojeksjonsflate

```
</details>

### Induced

<details>
```yaml
name: Anleggsprojeksjonsflate
description: Fotavtrykk av 3D-eigedommar (anleggseigedommar). Manglar volumet og må
  supplerast på oppdrag.
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
    owner: Anleggsprojeksjonsflate
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
class_uri: ngre:Anleggsprojeksjonsflate

```
</details>