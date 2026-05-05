

# Class: Konsept 


_Referanse til eit SKOS-omgrep frå eit kontrollert vokabular._





URI: [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept)





```mermaid
 classDiagram
    class Konsept
    click Konsept href "../Konsept/"
      Konsept : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Aktor](aktor.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [RegulativRessurs](regulativressurs.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Gebyr](gebyr.md) | [valuta](valuta.md) | range | [Konsept](konsept.md) |
| [Relasjon](relasjon.md) | [har_rolle](har_rolle.md) | range | [Konsept](konsept.md) |
| [Distribusjon](distribusjon.md) | [lisens](lisens.md) | range | [Konsept](konsept.md) |
| [Distribusjon](distribusjon.md) | [status](status.md) | range | [Konsept](konsept.md) |
| [Distribusjon](distribusjon.md) | [tilgjengelighet](tilgjengelighet.md) | range | [Konsept](konsept.md) |
| [Datasett](datasett.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [Datasett](datasett.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Datasett](datasett.md) | [dekningsomrade](dekningsomrade.md) | range | [Konsept](konsept.md) |
| [Datasett](datasett.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Datasettserie](datasettserie.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [Datasettserie](datasettserie.md) | [dekningsomrade](dekningsomrade.md) | range | [Konsept](konsept.md) |
| [Datatjeneste](datatjeneste.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [Datatjeneste](datatjeneste.md) | [tilgjengelighet](tilgjengelighet.md) | range | [Konsept](konsept.md) |
| [Datatjeneste](datatjeneste.md) | [lisens](lisens.md) | range | [Konsept](konsept.md) |
| [Datatjeneste](datatjeneste.md) | [status](status.md) | range | [Konsept](konsept.md) |
| [Katalogpost](katalogpost.md) | [status](status.md) | range | [Konsept](konsept.md) |
| [Katalog](katalog.md) | [dekningsomrade](dekningsomrade.md) | range | [Konsept](konsept.md) |
| [Katalog](katalog.md) | [lisens](lisens.md) | range | [Konsept](konsept.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:Concept |
| native | https://data.norge.no/linkml/dcat-ap-no/Konsept |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Konsept
description: Referanse til eit SKOS-omgrep frå eit kontrollert vokabular.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
class_uri: skos:Concept

```
</details>

### Induced

<details>
```yaml
name: Konsept
description: Referanse til eit SKOS-omgrep frå eit kontrollert vokabular.
from_schema: https://data.norge.no/linkml/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Konsept
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
class_uri: skos:Concept

```
</details>