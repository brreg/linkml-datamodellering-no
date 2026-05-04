

# Class: GeografiskOmrade 


_Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer til._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [ngr:GeografiskOmrade](https://data.norge.no/vocabulary/ngr-adresse#GeografiskOmrade)





```mermaid
 classDiagram
    class GeografiskOmrade
    click GeografiskOmrade href "../GeografiskOmrade/"
      GeografiskOmrade <|-- Fylke
        click Fylke href "../Fylke/"
      GeografiskOmrade <|-- Kommune
        click Kommune href "../Kommune/"
      GeografiskOmrade <|-- Poststed
        click Poststed href "../Poststed/"
      GeografiskOmrade <|-- Grunnkrets
        click Grunnkrets href "../Grunnkrets/"
      GeografiskOmrade <|-- Tettsted
        click Tettsted href "../Tettsted/"
      GeografiskOmrade <|-- Kirkesokn
        click Kirkesokn href "../Kirkesokn/"
      GeografiskOmrade <|-- Stemmekrets
        click Stemmekrets href "../Stemmekrets/"
      GeografiskOmrade <|-- KommunalKrets
        click KommunalKrets href "../KommunalKrets/"
      GeografiskOmrade <|-- Svalbard
        click Svalbard href "../Svalbard/"
      
      GeografiskOmrade : id
        
      GeografiskOmrade : namn
        
      
```





## Inheritance
* **GeografiskOmrade**
    * [Fylke](Fylke.md)
    * [Kommune](Kommune.md)
    * [Poststed](Poststed.md)
    * [Grunnkrets](Grunnkrets.md)
    * [Tettsted](Tettsted.md)
    * [Kirkesokn](Kirkesokn.md)
    * [Stemmekrets](Stemmekrets.md)
    * [KommunalKrets](KommunalKrets.md)
    * [Svalbard](Svalbard.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:GeografiskOmrade](https://data.norge.no/vocabulary/ngr-adresse#GeografiskOmrade) |


## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |
| [namn](namn.md) | 0..1 <br/> [String](String.md) | Namn på det geografiske området eller adressekomponenten |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OffisiellAdresse](OffisiellAdresse.md) | [geografisk_omrade](geografisk_omrade.md) | range | [GeografiskOmrade](GeografiskOmrade.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:GeografiskOmrade |
| native | https://data.norge.no/linkml/ngr-adresse/GeografiskOmrade |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeografiskOmrade
description: Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer
  til.
from_schema: https://data.norge.no/linkml/ngr-adresse
abstract: true
slots:
- id
- namn
class_uri: ngr:GeografiskOmrade

```
</details>

### Induced

<details>
```yaml
name: GeografiskOmrade
description: Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer
  til.
from_schema: https://data.norge.no/linkml/ngr-adresse
abstract: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    identifier: true
    alias: id
    owner: GeografiskOmrade
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
    owner: GeografiskOmrade
    domain_of:
    - Adresseomrade
    - GeografiskOmrade
    range: string
class_uri: ngr:GeografiskOmrade

```
</details>