

# Class: Svalbard 


_Svalbard som særskild geografisk område._





URI: [ngr:Svalbard](https://data.norge.no/vocabulary/ngr-adresse#Svalbard)





```mermaid
 classDiagram
    class Svalbard
    click Svalbard href "../Svalbard/"
      GeografiskOmrade <|-- Svalbard
        click GeografiskOmrade href "../GeografiskOmrade/"
      
      Svalbard : id
        
      Svalbard : namn
        
      
```





## Inheritance
* [GeografiskOmrade](GeografiskOmrade.md)
    * **Svalbard**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:Svalbard](https://data.norge.no/vocabulary/ngr-adresse#Svalbard) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | [GeografiskOmrade](GeografiskOmrade.md) |
| [namn](namn.md) | 0..1 <br/> [String](String.md) | Namn på det geografiske området eller adressekomponenten | [GeografiskOmrade](GeografiskOmrade.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | [svalbardOmrader](svalbardOmrader.md) | range | [Svalbard](Svalbard.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:Svalbard |
| native | https://data.norge.no/linkml/ngr-adresse/Svalbard |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Svalbard
description: Svalbard som særskild geografisk område.
from_schema: https://data.norge.no/linkml/ngr-adresse
is_a: GeografiskOmrade
class_uri: ngr:Svalbard

```
</details>

### Induced

<details>
```yaml
name: Svalbard
description: Svalbard som særskild geografisk område.
from_schema: https://data.norge.no/linkml/ngr-adresse
is_a: GeografiskOmrade
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    identifier: true
    alias: id
    owner: Svalbard
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
    owner: Svalbard
    domain_of:
    - Adresseomrade
    - GeografiskOmrade
    range: string
class_uri: ngr:Svalbard

```
</details>