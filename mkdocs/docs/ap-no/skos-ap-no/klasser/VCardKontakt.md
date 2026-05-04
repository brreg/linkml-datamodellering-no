

# Class: VCardKontakt 


_Kontaktinformasjon (vCard) for omgrepseigaren._





URI: [vcard:Kind](http://www.w3.org/2006/vcard/ns#Kind)





```mermaid
 classDiagram
    class VCardKontakt
    click VCardKontakt href "../VCardKontakt/"
      VCardKontakt : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [vcard:Kind](http://www.w3.org/2006/vcard/ns#Kind) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Begrep](Begrep.md) | [kontaktpunkt_vcard](kontaktpunkt_vcard.md) | range | [VCardKontakt](VCardKontakt.md) |
| [Samling](Samling.md) | [kontaktpunkt_vcard](kontaktpunkt_vcard.md) | range | [VCardKontakt](VCardKontakt.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:Kind |
| native | https://data.norge.no/linkml/skos-ap-no/VCardKontakt |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VCardKontakt
description: Kontaktinformasjon (vCard) for omgrepseigaren.
from_schema: https://data.norge.no/linkml/skos-ap-no
slots:
- id
class_uri: vcard:Kind

```
</details>

### Induced

<details>
```yaml
name: VCardKontakt
description: Kontaktinformasjon (vCard) for omgrepseigaren.
from_schema: https://data.norge.no/linkml/skos-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/skos-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: VCardKontakt
    domain_of:
    - Organisasjon
    - VCardKontakt
    - Begrep
    - Definisjon
    - AssosiativRelasjon
    - GeneriskRelasjon
    - PartitivRelasjon
    - Samling
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
    range: uriorcurie
    required: true
class_uri: vcard:Kind

```
</details>