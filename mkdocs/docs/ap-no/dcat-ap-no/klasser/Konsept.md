

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
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Aktor](Aktor.md) | [type_concept](type_concept.md) | range | [Konsept](Konsept.md) |
| [RegulativRessurs](RegulativRessurs.md) | [type_concept](type_concept.md) | range | [Konsept](Konsept.md) |
| [Gebyr](Gebyr.md) | [valuta](valuta.md) | range | [Konsept](Konsept.md) |
| [Relasjon](Relasjon.md) | [har_rolle](har_rolle.md) | range | [Konsept](Konsept.md) |
| [Distribusjon](Distribusjon.md) | [lisens](lisens.md) | range | [Konsept](Konsept.md) |
| [Distribusjon](Distribusjon.md) | [status](status.md) | range | [Konsept](Konsept.md) |
| [Distribusjon](Distribusjon.md) | [tilgjengelighet](tilgjengelighet.md) | range | [Konsept](Konsept.md) |
| [Datasett](Datasett.md) | [tema](tema.md) | range | [Konsept](Konsept.md) |
| [Datasett](Datasett.md) | [begrep](begrep.md) | range | [Konsept](Konsept.md) |
| [Datasett](Datasett.md) | [dekningsomrade](dekningsomrade.md) | range | [Konsept](Konsept.md) |
| [Datasett](Datasett.md) | [type_concept](type_concept.md) | range | [Konsept](Konsept.md) |
| [Datasettserie](Datasettserie.md) | [tema](tema.md) | range | [Konsept](Konsept.md) |
| [Datasettserie](Datasettserie.md) | [dekningsomrade](dekningsomrade.md) | range | [Konsept](Konsept.md) |
| [Datatjeneste](Datatjeneste.md) | [tema](tema.md) | range | [Konsept](Konsept.md) |
| [Datatjeneste](Datatjeneste.md) | [tilgjengelighet](tilgjengelighet.md) | range | [Konsept](Konsept.md) |
| [Datatjeneste](Datatjeneste.md) | [lisens](lisens.md) | range | [Konsept](Konsept.md) |
| [Datatjeneste](Datatjeneste.md) | [status](status.md) | range | [Konsept](Konsept.md) |
| [Katalogpost](Katalogpost.md) | [status](status.md) | range | [Konsept](Konsept.md) |
| [Katalog](Katalog.md) | [dekningsomrade](dekningsomrade.md) | range | [Konsept](Konsept.md) |
| [Katalog](Katalog.md) | [lisens](lisens.md) | range | [Konsept](Konsept.md) |












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