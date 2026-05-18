

# Class: Betingelsesregel 


_Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskapar._





URI: [modelldcatno:ConstraintRule](https://data.norge.no/vocabulary/modelldcatno#ConstraintRule)





```mermaid
 classDiagram
    class Betingelsesregel
    click Betingelsesregel href "../Betingelsesregel/"
      Merknad <|-- Betingelsesregel
        click Merknad href "../Merknad/"
      

      Betingelsesregel <|-- Og
        click Og href "../Og/"
      Betingelsesregel <|-- Eller
        click Eller href "../Eller/"
      Betingelsesregel <|-- XEllerY
        click XEllerY href "../XEllerY/"
      Betingelsesregel <|-- Ikke
        click Ikke href "../Ikke/"
      

      Betingelsesregel : annoterer
        
          
    
        
        
        Betingelsesregel --> "*" Modellelement : annoterer
        click Modellelement href "../Modellelement/"
    

        
      Betingelsesregel : betingelsesuttrykk
        
          
    
        
        
        Betingelsesregel --> "*" LangString : betingelsesuttrykk
        click LangString href "../LangString/"
    

        
      Betingelsesregel : betinger
        
          
    
        
        
        Betingelsesregel --> "1..*" Modellelement : betinger
        click Modellelement href "../Modellelement/"
    

        
      Betingelsesregel : eigenskapsmerknad
        
          
    
        
        
        Betingelsesregel --> "*" LangString : eigenskapsmerknad
        click LangString href "../LangString/"
    

        
      Betingelsesregel : id
        
          
    
        
        
        Betingelsesregel --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Betingelsesregel : identifikator_literal
        
          
    
        
        
        Betingelsesregel --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Betingelsesregel : tilhorer_modul
        
          
    
        
        
        Betingelsesregel --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      Betingelsesregel : tittel
        
          
    
        
        
        Betingelsesregel --> "*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```





## Inheritance
* [Merknad](merknad.md)
    * **Betingelsesregel**
        * [Og](og.md)
        * [Eller](eller.md)
        * [XEllerY](xellery.md)
        * [Ikke](ikke.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:ConstraintRule](https://data.norge.no/vocabulary/modelldcatno#ConstraintRule) |


## Eigenskapar







  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [betinger](betinger.md) | 1..* <br/> [Modellelement](modellelement.md) | Modellelement betingelsesregelen avgrensar (modelldcatno:constrains) |





  
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [betingelsesuttrykk](betingelsesuttrykk.md) | * <br/> [LangString](langstring.md) | Formelt uttrykk for betingelsesregelen (modelldcatno:constraintExpression) |





  
  

  
  






  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Merknad](merknad.md) |
| [annoterer](annoterer.md) | * <br/> [Modellelement](modellelement.md) | Modellelement denne merknaden gjeld (modelldcatno:annotates) | [Merknad](merknad.md) |
| [eigenskapsmerknad](eigenskapsmerknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad om ein eigenskap (modelldcatno:propertyNote) | [Merknad](merknad.md) |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) | [Merknad](merknad.md) |
| [tittel](tittel.md) | * <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) | [Merknad](merknad.md) |
| [tilhorer_modul](tilhorer_modul.md) | * <br/> [Modul](modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) | [Merknad](merknad.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:ConstraintRule |
| native | https://data.norge.no/linkml/modelldcat-ap-no/Betingelsesregel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Betingelsesregel
description: Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskapar.
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
is_a: Merknad
slots:
- betinger
- betingelsesuttrykk
slot_usage:
  betinger:
    name: betinger
    in_subset:
    - Obligatorisk
    required: true
  betingelsesuttrykk:
    name: betingelsesuttrykk
    in_subset:
    - Anbefalt
class_uri: modelldcatno:ConstraintRule

```
</details>

### Induced

<details>
```yaml
name: Betingelsesregel
description: Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskapar.
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
is_a: Merknad
slot_usage:
  betinger:
    name: betinger
    in_subset:
    - Obligatorisk
    required: true
  betingelsesuttrykk:
    name: betingelsesuttrykk
    in_subset:
    - Anbefalt
attributes:
  betinger:
    name: betinger
    description: Modellelement betingelsesregelen avgrensar (modelldcatno:constrains).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:constrains
    alias: betinger
    owner: Betingelsesregel
    domain_of:
    - Betingelsesregel
    range: Modellelement
    required: true
    multivalued: true
  betingelsesuttrykk:
    name: betingelsesuttrykk
    description: Formelt uttrykk for betingelsesregelen (modelldcatno:constraintExpression).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:constraintExpression
    alias: betingelsesuttrykk
    owner: Betingelsesregel
    domain_of:
    - Betingelsesregel
    range: LangString
    multivalued: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    alias: id
    owner: Betingelsesregel
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
  annoterer:
    name: annoterer
    description: Modellelement denne merknaden gjeld (modelldcatno:annotates).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:annotates
    alias: annoterer
    owner: Betingelsesregel
    domain_of:
    - Merknad
    range: Modellelement
    multivalued: true
  eigenskapsmerknad:
    name: eigenskapsmerknad
    description: Fritekstmerknad om ein eigenskap (modelldcatno:propertyNote).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:propertyNote
    alias: eigenskapsmerknad
    owner: Betingelsesregel
    domain_of:
    - Merknad
    range: LangString
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:identifier
    alias: identifikator_literal
    owner: Betingelsesregel
    domain_of:
    - Aktor
    - Modelkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    - Kodeelement
    range: string
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:title
    alias: tittel
    owner: Betingelsesregel
    domain_of:
    - Standard
    - Dokument
    - Modelkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    range: LangString
    multivalued: true
  tilhorer_modul:
    name: tilhorer_modul
    description: Modul dette elementet tilhøyrer (modelldcatno:belongsToModule).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:belongsToModule
    alias: tilhorer_modul
    owner: Betingelsesregel
    domain_of:
    - Modellelement
    - Eigenskap
    - Merknad
    range: Modul
    multivalued: true
class_uri: modelldcatno:ConstraintRule

```
</details>