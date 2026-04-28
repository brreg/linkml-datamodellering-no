

# Class: Kontaktopplysning 


_Kontaktinformasjon for ein aktør._





URI: [vcard:Kind](http://www.w3.org/2006/vcard/ns#Kind)





```mermaid
 classDiagram
    class Kontaktopplysning
    click Kontaktopplysning href "../Kontaktopplysning/"
      Kontaktopplysning : har_epost
        
      Kontaktopplysning : har_kontaktside
        
      Kontaktopplysning : id
        
      Kontaktopplysning : navn_vcard
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [vcard:Kind](http://www.w3.org/2006/vcard/ns#Kind) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |
| [navn_vcard](navn_vcard.md) | 1..* <br/> [LangString](LangString.md) | Formatert namn (vCard) | direct |
| [har_epost](har_epost.md) | 0..1 <br/> [Uri](Uri.md) | E-postadresse til kontaktpunktet | direct |
| [har_kontaktside](har_kontaktside.md) | 0..1 <br/> [Uri](Uri.md) | Nettside for kontakt | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [kontaktopplysningar](kontaktopplysningar.md) | range | [Kontaktopplysning](Kontaktopplysning.md) |
| [Datasett](Datasett.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](Kontaktopplysning.md) |
| [Datasettserie](Datasettserie.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](Kontaktopplysning.md) |
| [Datatjeneste](Datatjeneste.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](Kontaktopplysning.md) |
| [Katalog](Katalog.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](Kontaktopplysning.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:Kind |
| native | https://data.norge.no/linkml/dcat-ap-no/Kontaktopplysning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kontaktopplysning
description: Kontaktinformasjon for ein aktør.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
- navn_vcard
- har_epost
- har_kontaktside
slot_usage:
  navn_vcard:
    name: navn_vcard
    in_subset:
    - Obligatorisk
    required: true
class_uri: vcard:Kind

```
</details>

### Induced

<details>
```yaml
name: Kontaktopplysning
description: Kontaktinformasjon for ein aktør.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slot_usage:
  navn_vcard:
    name: navn_vcard
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Kontaktopplysning
    domain_of:
    - Frekvens
    - ProvenanceStatement
    - OdrlPolicy
    - ProvAktivitet
    - ProvAttributering
    - Tidsinstant
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - Standard
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Katalogpost
    - Spraak
    - Mediatype
    - Begrep
    - Begrepssamling
    range: uriorcurie
    required: true
  navn_vcard:
    name: navn_vcard
    description: Formatert namn (vCard).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: vcard:fn
    alias: navn_vcard
    owner: Kontaktopplysning
    domain_of:
    - Kontaktopplysning
    range: LangString
    required: true
    multivalued: true
  har_epost:
    name: har_epost
    description: E-postadresse til kontaktpunktet.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: vcard:hasEmail
    alias: har_epost
    owner: Kontaktopplysning
    domain_of:
    - Kontaktopplysning
    range: uri
  har_kontaktside:
    name: har_kontaktside
    description: Nettside for kontakt.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: vcard:hasURL
    alias: har_kontaktside
    owner: Kontaktopplysning
    domain_of:
    - Kontaktopplysning
    range: uri
class_uri: vcard:Kind

```
</details>