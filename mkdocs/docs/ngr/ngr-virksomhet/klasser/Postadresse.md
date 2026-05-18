

# Class: Postadresse 


_Postadressa verksemda mottar post på._





URI: [ngrv:Postadresse](https://data.norge.no/vocabulary/ngr-virksomhet#Postadresse)





```mermaid
 classDiagram
    class Postadresse
    click Postadresse href "../Postadresse/"
      GeografiskAdresse <|-- Postadresse
        click GeografiskAdresse href "../GeografiskAdresse/"
      
      Postadresse : id
        
          
    
        
        
        Postadresse --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* [GeografiskAdresse](geografiskadresse.md)
    * **Postadresse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrv:Postadresse](https://data.norge.no/vocabulary/ngr-virksomhet#Postadresse) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [GeografiskAdresse](geografiskadresse.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VirksomhetContainer](virksomhetcontainer.md) | [postadresser](postadresser.md) | range | [Postadresse](postadresse.md) |
| [Virksomhet](virksomhet.md) | [mottar_post_paa](mottar_post_paa.md) | range | [Postadresse](postadresse.md) |
| [Underenhet](underenhet.md) | [mottar_post_paa](mottar_post_paa.md) | range | [Postadresse](postadresse.md) |
| [Hovedenhet](hovedenhet.md) | [mottar_post_paa](mottar_post_paa.md) | range | [Postadresse](postadresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:Postadresse |
| native | https://data.norge.no/linkml/ngr-virksomhet/Postadresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Postadresse
description: Postadressa verksemda mottar post på.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
is_a: GeografiskAdresse
class_uri: ngrv:Postadresse

```
</details>

### Induced

<details>
```yaml
name: Postadresse
description: Postadressa verksemda mottar post på.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
is_a: GeografiskAdresse
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-virksomhet
    rank: 1000
    identifier: true
    alias: id
    owner: Postadresse
    domain_of:
    - Virksomhet
    - Tilstand
    - Organisasjonsform
    - Naeringskode
    - Sektorkode
    - Kontaktinformasjon
    - Varslingsadresse
    - Aktivitet
    - RolleIVirksomhet
    - Rolleinnehaver
    - Signaturrett
    - Prokura
    - GeografiskAdresse
    - Person
    range: uriorcurie
    required: true
class_uri: ngrv:Postadresse

```
</details>