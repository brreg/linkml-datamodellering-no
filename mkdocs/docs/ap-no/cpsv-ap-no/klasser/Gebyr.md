

# Class: Gebyr 


_Eit gebyr knytt til ei teneste._





URI: [cv:Cost](http://data.europa.eu/m8g/Cost)





```mermaid
 classDiagram
    class Gebyr
    click Gebyr href "../Gebyr/"
      Gebyr : beskrivelse
        
      Gebyr : id
        
      Gebyr : identifikator_literal
        
      Gebyr : valuta
        
          
    
        
        
        Gebyr --> "0..1" Konsept : valuta
        click Konsept href "../Konsept/"
    

        
      Gebyr : verdi
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [cv:Cost](http://data.europa.eu/m8g/Cost) |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  





  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](LangString.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [String](String.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [verdi](verdi.md) | 0..1 <br/> [Float](Float.md) | Verdien av gebyret |
| [valuta](valuta.md) | 0..1 <br/> [Konsept](Konsept.md) | Valuta (cv:currency) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | [har_gebyr](har_gebyr.md) | range | [Gebyr](Gebyr.md) |
| [OffentligTjeneste](OffentligTjeneste.md) | [har_gebyr](har_gebyr.md) | range | [Gebyr](Gebyr.md) |
| [Tjeneste](Tjeneste.md) | [har_gebyr](har_gebyr.md) | range | [Gebyr](Gebyr.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:Cost |
| native | https://data.norge.no/linkml/cpsv-ap-no/Gebyr |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gebyr
description: Eit gebyr knytt til ei teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
slots:
- id
- beskrivelse
- identifikator_literal
- verdi
- valuta
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Valgfri
  verdi:
    name: verdi
    in_subset:
    - Valgfri
  valuta:
    name: valuta
    in_subset:
    - Valgfri
class_uri: cv:Cost

```
</details>

### Induced

<details>
```yaml
name: Gebyr
description: Eit gebyr knytt til ei teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Valgfri
  verdi:
    name: verdi
    in_subset:
    - Valgfri
  valuta:
    name: valuta
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Gebyr
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Aktor
    - Kontaktpunkt
    - Tjenestekanal
    - Dokumentasjonstype
    - Tjenesteresultattype
    - Tjenesteresultattypeliste
    - Gebyr
    - Regel
    - RegulativRessurs
    - Deltagelse
    - Adresse
    - Katalog
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
    range: uriorcurie
    required: true
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: dct:description
    alias: beskrivelse
    owner: Gebyr
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Tjenestekanal
    - Dokumentasjonstype
    - Tjenesteresultattype
    - Tjenesteresultattypeliste
    - Gebyr
    - Regel
    - Katalog
    range: LangString
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: dct:identifier
    alias: identifikator_literal
    owner: Gebyr
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Aktor
    - Tjenestekanal
    - Dokumentasjonstype
    - Tjenesteresultattype
    - Gebyr
    - Regel
    - RegulativRessurs
    - Katalog
    range: string
  verdi:
    name: verdi
    description: Verdien av gebyret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: cv:value
    alias: verdi
    owner: Gebyr
    domain_of:
    - Gebyr
    range: float
  valuta:
    name: valuta
    description: Valuta (cv:currency).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: cv:currency
    alias: valuta
    owner: Gebyr
    domain_of:
    - Gebyr
    range: Konsept
class_uri: cv:Cost

```
</details>