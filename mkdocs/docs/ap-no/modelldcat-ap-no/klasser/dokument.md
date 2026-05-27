

# Class: Dokument 


_Eit dokument (foaf:Document)._





URI: [foaf:Document](http://xmlns.com/foaf/0.1/Document)





```mermaid
 classDiagram
    class Dokument
    click Dokument href "../Dokument/"
      Dokument : format
        
          
    
        
        
        Dokument --> "0..1" String : format
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Dokument : id
        
          
    
        
        
        Dokument --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Dokument : spraak
        
          
    
        
        
        Dokument --> "*" Spraak : spraak
        click Spraak href "../Spraak/"
    

        
      Dokument : tittel
        
          
    
        
        
        Dokument --> "*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [foaf:Document](http://xmlns.com/foaf/0.1/Document) |


## Eigenskapar







  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |
| [tittel](tittel.md) | * <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |
| [spraak](spraak.md) | * <br/> [Spraak](spraak.md) | Språk brukt i ressursen (dct:language) |
| [format](format.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Filformat eller medietype (dct:format) |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Informasjonsmodell](informasjonsmodell.md) | [har_format](har_format.md) | range | [Dokument](dokument.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:Document |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/Dokument |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Dokument
description: Eit dokument (foaf:Document).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slots:
- id
- tittel
- spraak
- format
class_uri: foaf:Document

```
</details>

### Induced

<details>
```yaml
name: Dokument
description: Eit dokument (foaf:Document).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Dokument
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
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    - Kodeelement
    range: uriorcurie
    required: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
    owner: Dokument
    domain_of:
    - Standard
    - Dokument
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    range: LangString
    multivalued: true
  spraak:
    name: spraak
    description: Språk brukt i ressursen (dct:language).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:language
    owner: Dokument
    domain_of:
    - Dokument
    - Modellkatalog
    - Informasjonsmodell
    range: Spraak
    multivalued: true
  format:
    name: format
    description: Filformat eller medietype (dct:format).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:format
    owner: Dokument
    domain_of:
    - Dokument
    range: string
class_uri: foaf:Document

```
</details>