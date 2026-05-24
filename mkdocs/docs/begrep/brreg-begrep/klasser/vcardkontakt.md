

# Class: VCardKontakt 


_Kontaktinformasjon (vCard) for omgrepseigaren._





URI: [vcard:Kind](http://www.w3.org/2006/vcard/ns#Kind)





```mermaid
 classDiagram
    class VCardKontakt
    click VCardKontakt href "../VCardKontakt/"
      VCardKontakt : id
        
          
    
        
        
        VCardKontakt --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
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
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Begrep](begrep.md) | [kontaktpunkt_vcard](kontaktpunkt_vcard.md) | range | [VCardKontakt](vcardkontakt.md) |
| [Samling](samling.md) | [kontaktpunkt_vcard](kontaktpunkt_vcard.md) | range | [VCardKontakt](vcardkontakt.md) |
| [BegrepContainer](begrepcontainer.md) | [kontaktpunkt](kontaktpunkt.md) | range | [VCardKontakt](vcardkontakt.md) |












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
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    owner: VCardKontakt
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - Organisasjon
    - VCardKontakt
    - Begrep
    - Definisjon
    - AssosiativRelasjon
    - GeneriskRelasjon
    - PartitivRelasjon
    - Samling
    range: uriorcurie
    required: true
class_uri: vcard:Kind

```
</details>