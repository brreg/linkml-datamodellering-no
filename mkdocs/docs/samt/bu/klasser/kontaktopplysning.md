

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


## Eigenskapar







  
  

  
  
    
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [navn_vcard](navn_vcard.md) | 1..* <br/> [LangString](langstring.md) | Formatert namn (vCard) |





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |
| [har_epost](har_epost.md) | 0..1 <br/> [Uri](uri.md) | E-postadresse til kontaktpunktet |
| [har_kontaktside](har_kontaktside.md) | 0..1 <br/> [Uri](uri.md) | Nettside for kontakt |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](containerklasse.md) | [kontaktpunkter](kontaktpunkter.md) | range | [Kontaktopplysning](kontaktopplysning.md) |
| [Datasett](datasett.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](kontaktopplysning.md) |
| [Datasettserie](datasettserie.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](kontaktopplysning.md) |
| [Datatjeneste](datatjeneste.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](kontaktopplysning.md) |
| [Katalog](katalog.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](kontaktopplysning.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:Kind |
| native | samtbuskole:Kontaktopplysning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kontaktopplysning
description: Kontaktinformasjon for ein aktør.
from_schema: https://example.no/ontology/samt-bu-skole
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
from_schema: https://example.no/ontology/samt-bu-skole
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
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: id
    owner: Kontaktopplysning
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
  navn_vcard:
    name: navn_vcard
    description: Formatert namn (vCard).
    in_subset:
    - Obligatorisk
    from_schema: https://example.no/ontology/samt-bu-skole
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
    from_schema: https://example.no/ontology/samt-bu-skole
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
    from_schema: https://example.no/ontology/samt-bu-skole
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