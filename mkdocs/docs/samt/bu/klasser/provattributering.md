

# Class: ProvAttributering 


_Ein kvalifisert PROV-attributering._





URI: [prov:Attribution](http://www.w3.org/ns/prov#Attribution)





```mermaid
 classDiagram
    class ProvAttributering
    click ProvAttributering href "../ProvAttributering/"
      ProvAttributering : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [prov:Attribution](http://www.w3.org/ns/prov#Attribution) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](datasett.md) | [annen_ansvarlig_aktor](annen_ansvarlig_aktor.md) | range | [ProvAttributering](provattributering.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Attribution |
| native | samtbuskole:ProvAttributering |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvAttributering
description: Ein kvalifisert PROV-attributering.
from_schema: https://example.no/ontology/samt-bu-skole
slots:
- id
class_uri: prov:Attribution

```
</details>

### Induced

<details>
```yaml
name: ProvAttributering
description: Ein kvalifisert PROV-attributering.
from_schema: https://example.no/ontology/samt-bu-skole
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: id
    owner: ProvAttributering
    domain_of:
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
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
    range: uriorcurie
    required: true
class_uri: prov:Attribution

```
</details>