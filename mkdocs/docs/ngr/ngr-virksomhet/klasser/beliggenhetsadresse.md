

# Class: Beliggenhetsadresse 


_Beliggenheitsadressa til underleininga – den fysiske adressa der aktiviteten vert utøvd._





URI: [ngrv:Beliggenhetsadresse](https://data.norge.no/vocabulary/ngr-virksomhet#Beliggenhetsadresse)





```mermaid
 classDiagram
    class Beliggenhetsadresse
    click Beliggenhetsadresse href "../Beliggenhetsadresse/"
      GeografiskAdresse <|-- Beliggenhetsadresse
        click GeografiskAdresse href "../GeografiskAdresse/"
      
      Beliggenhetsadresse : id
        
          
    
        
        
        Beliggenhetsadresse --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* [GeografiskAdresse](geografiskadresse.md)
    * **Beliggenhetsadresse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrv:Beliggenhetsadresse](https://data.norge.no/vocabulary/ngr-virksomhet#Beliggenhetsadresse) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [GeografiskAdresse](geografiskadresse.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VirksomhetContainer](virksomhetcontainer.md) | [beliggenhetsadresser](beliggenhetsadresser.md) | range | [Beliggenhetsadresse](beliggenhetsadresse.md) |
| [Underenhet](underenhet.md) | [har_beliggenhetsadresse](har_beliggenhetsadresse.md) | range | [Beliggenhetsadresse](beliggenhetsadresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:Beliggenhetsadresse |
| native | https://data.norge.no/ngr/ngr-virksomhet/Beliggenhetsadresse |




## Examples
### Example: Beliggenhetsadresse-beliggenhetsadresse-1

```yaml
id: ngrv:eksempel/beliggenhetsadresse-1

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Beliggenhetsadresse
description: Beliggenheitsadressa til underleininga – den fysiske adressa der aktiviteten
  vert utøvd.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
is_a: GeografiskAdresse
class_uri: ngrv:Beliggenhetsadresse

```
</details>

### Induced

<details>
```yaml
name: Beliggenhetsadresse
description: Beliggenheitsadressa til underleininga – den fysiske adressa der aktiviteten
  vert utøvd.
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
    owner: Beliggenhetsadresse
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
class_uri: ngrv:Beliggenhetsadresse

```
</details>