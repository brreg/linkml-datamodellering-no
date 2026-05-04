

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
        
      
```





## Inheritance
* [GeografiskAdresse](GeografiskAdresse.md)
    * **Forretningsadresse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrv:Forretningsadresse](https://data.norge.no/vocabulary/ngr-virksomhet#Forretningsadresse) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | [GeografiskAdresse](GeografiskAdresse.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VirksomhetContainer](VirksomhetContainer.md) | [forretningsadresser](forretningsadresser.md) | range | [Forretningsadresse](Forretningsadresse.md) |
| [Hovedenhet](Hovedenhet.md) | [har_forretningsadresse](har_forretningsadresse.md) | range | [Forretningsadresse](Forretningsadresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:Forretningsadresse |
| native | https://data.norge.no/linkml/ngr-virksomhet/Forretningsadresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Forretningsadresse
description: Forretningsadressa til hovudeininga – adressa der hovudkontoret held
  til.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
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
from_schema: https://data.norge.no/linkml/ngr-virksomhet
is_a: GeografiskAdresse
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-virksomhet
    rank: 1000
    identifier: true
    alias: id
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