

# Class: Tidsinstant 


_Eit tidspunkt (OWL Time)._





URI: [time:Instant](http://www.w3.org/6006/time#Instant)





```mermaid
 classDiagram
    class Tidsinstant
    click Tidsinstant href "../Tidsinstant/"
      Tidsinstant : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [time:Instant](http://www.w3.org/6006/time#Instant) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Tidsrom](tidsrom.md) | [begynnelse](begynnelse.md) | range | [Tidsinstant](tidsinstant.md) |
| [Tidsrom](tidsrom.md) | [slutt](slutt.md) | range | [Tidsinstant](tidsinstant.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | time:Instant |
| native | https://data.norge.no/linkml/dcat-ap-no/Tidsinstant |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Tidsinstant
description: Eit tidspunkt (OWL Time).
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
class_uri: time:Instant

```
</details>

### Induced

<details>
```yaml
name: Tidsinstant
description: Eit tidspunkt (OWL Time).
from_schema: https://data.norge.no/linkml/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Tidsinstant
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
    - Konsept
    - Begrepssamling
    range: uriorcurie
    required: true
class_uri: time:Instant

```
</details>