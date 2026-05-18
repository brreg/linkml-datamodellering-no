

# Class: Lisensdokument 


_Eit lisensdokument (dct:LicenseDocument)._





URI: [dct:LicenseDocument](http://purl.org/dc/terms/LicenseDocument)





```mermaid
 classDiagram
    class Lisensdokument
    click Lisensdokument href "../Lisensdokument/"
      Lisensdokument : id
        
          
    
        
        
        Lisensdokument --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Lisensdokument : type_concept
        
          
    
        
        
        Lisensdokument --> "0..1" Konsept : type_concept
        click Konsept href "../Konsept/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dct:LicenseDocument](http://purl.org/dc/terms/LicenseDocument) |


## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |
| [type_concept](type_concept.md) | 0..1 <br/> [Konsept](konsept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Modelkatalog](modelkatalog.md) | [lisens](lisens.md) | range | [Lisensdokument](lisensdokument.md) |
| [Informasjonsmodell](informasjonsmodell.md) | [lisens](lisens.md) | range | [Lisensdokument](lisensdokument.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:LicenseDocument |
| native | https://data.norge.no/linkml/modelldcat-ap-no/Lisensdokument |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Lisensdokument
description: Eit lisensdokument (dct:LicenseDocument).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slots:
- id
- type_concept
class_uri: dct:LicenseDocument

```
</details>

### Induced

<details>
```yaml
name: Lisensdokument
description: Eit lisensdokument (dct:LicenseDocument).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    alias: id
    owner: Lisensdokument
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Standard
    - Lisensdokument
    - Lokasjon
    - Tidsperiode
    - Dokument
    - Modelkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    - Kodeelement
    range: uriorcurie
    required: true
  type_concept:
    name: type_concept
    description: Type ressurs frå eit kontrollert vokabular (dct:type).
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:type
    alias: type_concept
    owner: Lisensdokument
    domain_of:
    - Aktor
    - Lisensdokument
    - Informasjonsmodell
    range: Konsept
class_uri: dct:LicenseDocument

```
</details>