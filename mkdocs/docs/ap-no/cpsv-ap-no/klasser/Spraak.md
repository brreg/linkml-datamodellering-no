

# Class: Spraak 


_Ein språkreferanse (dct:LinguisticSystem)._





URI: [dct:LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)





```mermaid
 classDiagram
    class Spraak
    click Spraak href "../Spraak/"
      Spraak : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dct:LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OffentligTjeneste](offentligtjeneste.md) | [sprak](sprak.md) | range | [Spraak](spraak.md) |
| [Tjeneste](tjeneste.md) | [sprak](sprak.md) | range | [Spraak](spraak.md) |
| [Kontaktpunkt](kontaktpunkt.md) | [sprak](sprak.md) | range | [Spraak](spraak.md) |
| [Dokumentasjonstype](dokumentasjonstype.md) | [godtek_sprak](godtek_sprak.md) | range | [Spraak](spraak.md) |
| [Tjenesteresultattype](tjenesteresultattype.md) | [mogleg_sprak](mogleg_sprak.md) | range | [Spraak](spraak.md) |
| [Regel](regel.md) | [sprak](sprak.md) | range | [Spraak](spraak.md) |
| [Katalog](katalog.md) | [sprak](sprak.md) | range | [Spraak](spraak.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:LinguisticSystem |
| native | https://data.norge.no/linkml/cpsv-ap-no/Spraak |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Spraak
description: Ein språkreferanse (dct:LinguisticSystem).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
slots:
- id
class_uri: dct:LinguisticSystem

```
</details>

### Induced

<details>
```yaml
name: Spraak
description: Ein språkreferanse (dct:LinguisticSystem).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Spraak
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
class_uri: dct:LinguisticSystem

```
</details>