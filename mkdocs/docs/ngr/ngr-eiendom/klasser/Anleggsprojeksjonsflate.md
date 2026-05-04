

# Class: Anleggsprojeksjonsflate 


_Fotavtrykk av 3D-eigedommar (anleggseigedommar). Manglar volumet og må supplerast på oppdrag._





URI: [ngre:Anleggsprojeksjonsflate](https://data.norge.no/vocabulary/ngr-eiendom#Anleggsprojeksjonsflate)





```mermaid
 classDiagram
    class Anleggsprojeksjonsflate
    click Anleggsprojeksjonsflate href "../Anleggsprojeksjonsflate/"
      Anleggsprojeksjonsflate : id
        
      
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
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Matrikkelenhet](Matrikkelenhet.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](Anleggsprojeksjonsflate.md) |
| [Grunneiendom](Grunneiendom.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](Anleggsprojeksjonsflate.md) |
| [Festegrunn](Festegrunn.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](Anleggsprojeksjonsflate.md) |
| [Jordsameie](Jordsameie.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](Anleggsprojeksjonsflate.md) |
| [Eierseksjon](Eierseksjon.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](Anleggsprojeksjonsflate.md) |
| [Anleggseiendom](Anleggseiendom.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](Anleggsprojeksjonsflate.md) |
| [AnnenMatrikkelenhet](AnnenMatrikkelenhet.md) | [har_anleggsprojeksjonsflate](har_anleggsprojeksjonsflate.md) | range | [Anleggsprojeksjonsflate](Anleggsprojeksjonsflate.md) |












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