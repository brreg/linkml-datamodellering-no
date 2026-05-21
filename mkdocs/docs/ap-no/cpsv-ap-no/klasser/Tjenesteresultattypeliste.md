

# Class: Tjenesteresultattypeliste 


_Ei liste over moglege tjenesteresultattypar._





URI: [cpsvno:OutputTypeList](https://data.norge.no/vocabulary/cpsvno#OutputTypeList)





```mermaid
 classDiagram
    class Tjenesteresultattypeliste
    click Tjenesteresultattypeliste href "../Tjenesteresultattypeliste/"
      Tjenesteresultattypeliste : beskrivelse
        
          
    
        
        
        Tjenesteresultattypeliste --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Tjenesteresultattypeliste : id
        
          
    
        
        
        Tjenesteresultattypeliste --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Tjenesteresultattypeliste : tittel
        
          
    
        
        
        Tjenesteresultattypeliste --> "*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [cpsvno:OutputTypeList](https://data.norge.no/vocabulary/cpsvno#OutputTypeList) |


## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |
| [tittel](tittel.md) | * <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cpsvno:OutputTypeList |
| native | https://data.norge.no/linkml/cpsv-ap-no/Tjenesteresultattypeliste |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Tjenesteresultattypeliste
description: Ei liste over moglege tjenesteresultattypar.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slots:
- id
- tittel
- beskrivelse
class_uri: cpsvno:OutputTypeList

```
</details>

### Induced

<details>
```yaml
name: Tjenesteresultattypeliste
description: Ei liste over moglege tjenesteresultattypar.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    owner: Tjenesteresultattypeliste
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
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
    range: uriorcurie
    required: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:title
    owner: Tjenesteresultattypeliste
    domain_of:
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Aktor
    - Dokumentasjonstype
    - Tjenesteresultattype
    - Tjenesteresultattypeliste
    - Regel
    - RegulativRessurs
    - Katalog
    range: LangString
    multivalued: true
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:description
    owner: Tjenesteresultattypeliste
    domain_of:
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
class_uri: cpsvno:OutputTypeList

```
</details>