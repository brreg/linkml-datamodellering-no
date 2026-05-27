

# Class: XEllerY 


_Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde._





URI: [modelldcatno:Xor](https://data.norge.no/vocabulary/modelldcatno#Xor)





```mermaid
 classDiagram
    class XEllerY
    click XEllerY href "../XEllerY/"
      Betingelsesregel <|-- XEllerY
        click Betingelsesregel href "../Betingelsesregel/"
      
      XEllerY : annoterer
        
          
    
        
        
        XEllerY --> "*" Modellelement : annoterer
        click Modellelement href "../Modellelement/"
    

        
      XEllerY : betingelsesuttrykk
        
          
    
        
        
        XEllerY --> "*" LangString : betingelsesuttrykk
        click LangString href "../LangString/"
    

        
      XEllerY : betinger
        
          
    
        
        
        XEllerY --> "1..*" Modellelement : betinger
        click Modellelement href "../Modellelement/"
    

        
      XEllerY : eigenskapsmerknad
        
          
    
        
        
        XEllerY --> "*" LangString : eigenskapsmerknad
        click LangString href "../LangString/"
    

        
      XEllerY : id
        
          
    
        
        
        XEllerY --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      XEllerY : identifikator_literal
        
          
    
        
        
        XEllerY --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      XEllerY : tilhorer_modul
        
          
    
        
        
        XEllerY --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      XEllerY : tittel
        
          
    
        
        
        XEllerY --> "*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```





## Inheritance
* [Merknad](merknad.md)
    * [Betingelsesregel](betingelsesregel.md)
        * **XEllerY**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:Xor](https://data.norge.no/vocabulary/modelldcatno#Xor) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [betinger](betinger.md) | 1..* <br/> [Modellelement](modellelement.md) | Modellelement betingelsesregelen avgrensar (modelldcatno:constrains) | [Betingelsesregel](betingelsesregel.md) |
| [betingelsesuttrykk](betingelsesuttrykk.md) | * <br/> [LangString](langstring.md) | Formelt uttrykk for betingelsesregelen (modelldcatno:constraintExpression) | [Betingelsesregel](betingelsesregel.md) |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Merknad](merknad.md) |
| [annoterer](annoterer.md) | * <br/> [Modellelement](modellelement.md) | Modellelement denne merknaden gjeld (modelldcatno:annotates) | [Merknad](merknad.md) |
| [eigenskapsmerknad](eigenskapsmerknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad om ein eigenskap (modelldcatno:propertyNote) | [Merknad](merknad.md) |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) | [Merknad](merknad.md) |
| [tittel](tittel.md) | * <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) | [Merknad](merknad.md) |
| [tilhorer_modul](tilhorer_modul.md) | * <br/> [Modul](modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) | [Merknad](merknad.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:Xor |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/XEllerY |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: XEllerY
description: Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
is_a: Betingelsesregel
class_uri: modelldcatno:Xor

```
</details>

### Induced

<details>
```yaml
name: XEllerY
description: Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
is_a: Betingelsesregel
attributes:
  betinger:
    name: betinger
    description: Modellelement betingelsesregelen avgrensar (modelldcatno:constrains).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:constrains
    owner: XEllerY
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
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:constraintExpression
    owner: XEllerY
    domain_of:
    - Betingelsesregel
    range: LangString
    multivalued: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: XEllerY
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
  annoterer:
    name: annoterer
    description: Modellelement denne merknaden gjeld (modelldcatno:annotates).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:annotates
    owner: XEllerY
    domain_of:
    - Merknad
    range: Modellelement
    multivalued: true
  eigenskapsmerknad:
    name: eigenskapsmerknad
    description: Fritekstmerknad om ein eigenskap (modelldcatno:propertyNote).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:propertyNote
    owner: XEllerY
    domain_of:
    - Merknad
    range: LangString
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:identifier
    owner: XEllerY
    domain_of:
    - Aktor
    - Modellkatalog
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
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
    owner: XEllerY
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
  tilhorer_modul:
    name: tilhorer_modul
    description: Modul dette elementet tilhøyrer (modelldcatno:belongsToModule).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:belongsToModule
    owner: XEllerY
    domain_of:
    - Modellelement
    - Eigenskap
    - Merknad
    range: Modul
    multivalued: true
class_uri: modelldcatno:Xor

```
</details>