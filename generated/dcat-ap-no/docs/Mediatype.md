

# Class: Mediatype 


_Ein medietype eller filformat (dct:MediaTypeOrExtent)._





URI: [dct:MediaTypeOrExtent](http://purl.org/dc/terms/MediaTypeOrExtent)





```mermaid
 classDiagram
    class Mediatype
    click Mediatype href "../Mediatype/"
      Mediatype : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dct:MediaTypeOrExtent](http://purl.org/dc/terms/MediaTypeOrExtent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Distribusjon](Distribusjon.md) | [format](format.md) | range | [Mediatype](Mediatype.md) |
| [Distribusjon](Distribusjon.md) | [komprimeringsformat](komprimeringsformat.md) | range | [Mediatype](Mediatype.md) |
| [Distribusjon](Distribusjon.md) | [medietype](medietype.md) | range | [Mediatype](Mediatype.md) |
| [Distribusjon](Distribusjon.md) | [pakkeformat](pakkeformat.md) | range | [Mediatype](Mediatype.md) |
| [Datatjeneste](Datatjeneste.md) | [format](format.md) | range | [Mediatype](Mediatype.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:MediaTypeOrExtent |
| native | https://data.norge.no/linkml/dcat-ap-no/Mediatype |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Mediatype
description: Ein medietype eller filformat (dct:MediaTypeOrExtent).
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
class_uri: dct:MediaTypeOrExtent

```
</details>

### Induced

<details>
```yaml
name: Mediatype
description: Ein medietype eller filformat (dct:MediaTypeOrExtent).
from_schema: https://data.norge.no/linkml/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Mediatype
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
class_uri: dct:MediaTypeOrExtent

```
</details>