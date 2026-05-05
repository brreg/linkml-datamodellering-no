

# Class: Landkode 


_Landskode i ISO 3166-1 alpha-2 format._





URI: [fint:Landkode](https://schema.fintlabs.no/Landkode)





```mermaid
 classDiagram
    class Landkode
    click Landkode href "../Landkode/"
      Begrep <|-- Landkode
        click Begrep href "../Begrep/"
      
      Landkode : gyldighetsperiode
        
          
    
        
        
        Landkode --> "0..1" Periode : gyldighetsperiode
        click Periode href "../Periode/"
    

        
      Landkode : id
        
      Landkode : kode
        
      Landkode : navn
        
      Landkode : passiv
        
      
```





## Inheritance
* [Begrep](begrep.md)
    * **Landkode**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Landkode](https://schema.fintlabs.no/Landkode) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen | [Begrep](begrep.md) |
| [kode](kode.md) | 1 <br/> [String](string.md) | Verdi som identifiserer omgrepet | [Begrep](begrep.md) |
| [navn](navn.md) | 1 <br/> [String](string.md) | Hovudnamn for omgrepet | [Begrep](begrep.md) |
| [gyldighetsperiode](gyldighetsperiode.md) | 0..1 <br/> [Periode](periode.md) | Angir gyldighetsperioden for eit omgrep/kode | [Begrep](begrep.md) |
| [passiv](passiv.md) | 0..1 <br/> [Boolean](boolean.md) | Angir at koden er passiv og ikkje kan veljast | [Begrep](begrep.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Adresse](adresse.md) | [land](land.md) | range | [Landkode](landkode.md) |
| [Person](person.md) | [statsborgerskap](statsborgerskap.md) | range | [Landkode](landkode.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Landkode |
| native | https://schema.fintlabs.no/personvern/:Landkode |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Landkode
description: Landskode i ISO 3166-1 alpha-2 format.
from_schema: https://data.norge.no/linkml/fint-personvern
is_a: Begrep
class_uri: fint:Landkode

```
</details>

### Induced

<details>
```yaml
name: Landkode
description: Landskode i ISO 3166-1 alpha-2 format.
from_schema: https://data.norge.no/linkml/fint-personvern
is_a: Begrep
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    identifier: true
    alias: id
    owner: Landkode
    domain_of:
    - Behandling
    - Samtykke
    - Tjeneste
    - Behandlingsgrunnlag
    - Personopplysning
    - Begrep
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    range: uriorcurie
    required: true
  kode:
    name: kode
    description: Verdi som identifiserer omgrepet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:kode
    alias: kode
    owner: Landkode
    domain_of:
    - Behandlingsgrunnlag
    - Personopplysning
    - Begrep
    range: string
    required: true
  navn:
    name: navn
    description: Hovudnamn for omgrepet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:navn
    alias: navn
    owner: Landkode
    domain_of:
    - Tjeneste
    - Behandlingsgrunnlag
    - Personopplysning
    - Begrep
    - Valuta
    - Person
    - Kontaktperson
    range: string
    required: true
  gyldighetsperiode:
    name: gyldighetsperiode
    description: Angir gyldighetsperioden for eit omgrep/kode.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:gyldighetsperiode
    alias: gyldighetsperiode
    owner: Landkode
    domain_of:
    - Samtykke
    - Behandlingsgrunnlag
    - Personopplysning
    - Begrep
    - Identifikator
    range: Periode
    inlined: true
  passiv:
    name: passiv
    description: Angir at koden er passiv og ikkje kan veljast.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:passiv
    alias: passiv
    owner: Landkode
    domain_of:
    - Behandlingsgrunnlag
    - Personopplysning
    - Begrep
    range: boolean
class_uri: fint:Landkode

```
</details>