

# Class: Tettsted 


_Eit tettbygd område definert av SSB._





URI: [ngr:Tettsted](https://data.norge.no/vocabulary/ngr-adresse#Tettsted)





```mermaid
 classDiagram
    class Tettsted
    click Tettsted href "../Tettsted/"
      GeografiskOmrade <|-- Tettsted
        click GeografiskOmrade href "../GeografiskOmrade/"
      
      Tettsted : id
        
      Tettsted : namn
        
      Tettsted : tettstedsnummer
        
      
```





## Inheritance
* [GeografiskOmrade](GeografiskOmrade.md)
    * **Tettsted**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:Tettsted](https://data.norge.no/vocabulary/ngr-adresse#Tettsted) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tettstedsnummer](tettstedsnummer.md) | 0..1 <br/> [String](String.md) | SSB-tettstedsnummer |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | [GeografiskOmrade](GeografiskOmrade.md) |
| [namn](namn.md) | 0..1 <br/> [String](String.md) | Namn på det geografiske området eller adressekomponenten | [GeografiskOmrade](GeografiskOmrade.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | [tettstadar](tettstadar.md) | range | [Tettsted](Tettsted.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:Tettsted |
| native | https://data.norge.no/linkml/ngr-adresse/Tettsted |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Tettsted
description: Eit tettbygd område definert av SSB.
from_schema: https://data.norge.no/linkml/ngr-adresse
is_a: GeografiskOmrade
slots:
- tettstedsnummer
class_uri: ngr:Tettsted

```
</details>

### Induced

<details>
```yaml
name: Tettsted
description: Eit tettbygd område definert av SSB.
from_schema: https://data.norge.no/linkml/ngr-adresse
is_a: GeografiskOmrade
attributes:
  tettstedsnummer:
    name: tettstedsnummer
    description: SSB-tettstedsnummer.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    slot_uri: ngr:tettstedsnummer
    alias: tettstedsnummer
    owner: Tettsted
    domain_of:
    - Tettsted
    range: string
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    identifier: true
    alias: id
    owner: Tettsted
    domain_of:
    - GeografiskAdresse
    - Adressenavn
    - Adresseomrade
    - Adressekode
    - Husnummer
    - Bruksenhetsnummer
    - Representasjonspunkt
    - GeografiskOmrade
    - Postboks
    - Bygning
    - Bruksenhet
    range: uriorcurie
    required: true
  namn:
    name: namn
    description: Namn på det geografiske området eller adressekomponenten.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    slot_uri: ngr:namn
    alias: namn
    owner: Tettsted
    domain_of:
    - Adresseomrade
    - GeografiskOmrade
    range: string
class_uri: ngr:Tettsted

```
</details>