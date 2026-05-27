

# Class: Konsept 


_Referanse til eit SKOS-omgrep frå eit kontrollert vokabular._





URI: [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept)





```mermaid
 classDiagram
    class Konsept
    click Konsept href "../Konsept/"
      Konsept : id
        
          
    
        
        
        Konsept --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
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
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Aktor](aktor.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [RegulativRessurs](regulativressurs.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Gebyr](gebyr.md) | [valuta](valuta.md) | range | [Konsept](konsept.md) |
| [Distribusjon](distribusjon.md) | [status](status.md) | range | [Konsept](konsept.md) |
| [Datasett](datasett.md) | [dekningsomraade](dekningsomraade.md) | range | [Konsept](konsept.md) |
| [Datasett](datasett.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Datasettserie](datasettserie.md) | [dekningsomraade](dekningsomraade.md) | range | [Konsept](konsept.md) |
| [Datatjeneste](datatjeneste.md) | [status](status.md) | range | [Konsept](konsept.md) |
| [Katalogpost](katalogpost.md) | [status](status.md) | range | [Konsept](konsept.md) |
| [Katalog](katalog.md) | [dekningsomraade](dekningsomraade.md) | range | [Konsept](konsept.md) |










## See Also

* [https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be](https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be)



## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:Concept |
| native | https://data.norge.no/ap-no/common-ap-no/Konsept |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Konsept
description: Referanse til eit SKOS-omgrep frå eit kontrollert vokabular.
from_schema: https://data.norge.no/ap-no/common-ap-no
see_also:
- https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be
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
from_schema: https://data.norge.no/ap-no/common-ap-no
see_also:
- https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Konsept
    domain_of:
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    - SamtBuContainer
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: uriorcurie
    required: true
class_uri: skos:Concept

```
</details>