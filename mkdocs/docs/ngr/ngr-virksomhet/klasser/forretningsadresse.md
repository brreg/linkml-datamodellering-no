

# Class: Forretningsadresse 


_Forretningsadressa til hovudeininga – adressa der hovudkontoret held til._





URI: [ngrv:Forretningsadresse](https://data.norge.no/vocabulary/ngr-virksomhet#Forretningsadresse)





```mermaid
 classDiagram
    class Forretningsadresse
    click Forretningsadresse href "../Forretningsadresse/"
      GeografiskAdresse <|-- Forretningsadresse
        click GeografiskAdresse href "../GeografiskAdresse/"
      
      Forretningsadresse : id
        
          
    
        
        
        Forretningsadresse --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* [GeografiskAdresse](geografiskadresse.md)
    * **Forretningsadresse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrv:Forretningsadresse](https://data.norge.no/vocabulary/ngr-virksomhet#Forretningsadresse) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [GeografiskAdresse](geografiskadresse.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VirksomhetContainer](virksomhetcontainer.md) | [forretningsadresser](forretningsadresser.md) | range | [Forretningsadresse](forretningsadresse.md) |
| [Hovedenhet](hovedenhet.md) | [har_forretningsadresse](har_forretningsadresse.md) | range | [Forretningsadresse](forretningsadresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:Forretningsadresse |
| native | https://data.norge.no/ngr/ngr-virksomhet/Forretningsadresse |




## Examples
### Example: Forretningsadresse-forretningsadresse-1

```yaml
id: ngrv:eksempel/forretningsadresse-1

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Forretningsadresse
description: Forretningsadressa til hovudeininga – adressa der hovudkontoret held
  til.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
is_a: GeografiskAdresse
class_uri: ngrv:Forretningsadresse

```
</details>

### Induced

<details>
```yaml
name: Forretningsadresse
description: Forretningsadressa til hovudeininga – adressa der hovudkontoret held
  til.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
is_a: GeografiskAdresse
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-virksomhet
    rank: 1000
    identifier: true
    owner: Forretningsadresse
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
class_uri: ngrv:Forretningsadresse

```
</details>