

# Class: Attributt 


_Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi._





URI: [modelldcatno:Attribute](https://data.norge.no/vocabulary/modelldcatno#Attribute)





```mermaid
 classDiagram
    class Attributt
    click Attributt href "../Attributt/"
      Eigenskap <|-- Attributt
        click Eigenskap href "../Eigenskap/"
      
      Attributt : begrep
        
          
    
        
        
        Attributt --> "*" Konsept : begrep
        click Konsept href "../Konsept/"
    

        
      Attributt : beskrivelse
        
          
    
        
        
        Attributt --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Attributt : danner_symmetri_med
        
          
    
        
        
        Attributt --> "0..1" Eigenskap : danner_symmetri_med
        click Eigenskap href "../Eigenskap/"
    

        
      Attributt : har_datatype
        
          
    
        
        
        Attributt --> "*" Datatype : har_datatype
        click Datatype href "../Datatype/"
    

        
      Attributt : har_enkel_type
        
          
    
        
        
        Attributt --> "*" EnkelType : har_enkel_type
        click EnkelType href "../EnkelType/"
    

        
      Attributt : har_type
        
          
    
        
        
        Attributt --> "*" Modellelement : har_type
        click Modellelement href "../Modellelement/"
    

        
      Attributt : har_verdi_fra
        
          
    
        
        
        Attributt --> "*" Kodeliste : har_verdi_fra
        click Kodeliste href "../Kodeliste/"
    

        
      Attributt : id
        
          
    
        
        
        Attributt --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Attributt : identifikator_literal
        
          
    
        
        
        Attributt --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Attributt : inneholder_objekttype
        
          
    
        
        
        Attributt --> "*" Objekttype : inneholder_objekttype
        click Objekttype href "../Objekttype/"
    

        
      Attributt : maks_multiplisitet
        
          
    
        
        
        Attributt --> "0..1" String : maks_multiplisitet
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Attributt : min_multiplisitet
        
          
    
        
        
        Attributt --> "0..1" NonNegativeInteger : min_multiplisitet
        click NonNegativeInteger href "../NonNegativeInteger/"
    

        
      Attributt : navigerbar
        
          
    
        
        
        Attributt --> "0..1" Boolean : navigerbar
        click Boolean href "../http://www.w3.org/2001/XMLSchema#boolean/"
    

        
      Attributt : relasjonsegenskapetikett
        
          
    
        
        
        Attributt --> "*" LangString : relasjonsegenskapetikett
        click LangString href "../LangString/"
    

        
      Attributt : sekvensnummer
        
          
    
        
        
        Attributt --> "0..1" NonNegativeInteger : sekvensnummer
        click NonNegativeInteger href "../NonNegativeInteger/"
    

        
      Attributt : tilhorer_modul
        
          
    
        
        
        Attributt --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      Attributt : tittel
        
          
    
        
        
        Attributt --> "*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```





## Inheritance
* [Eigenskap](eigenskap.md)
    * **Attributt**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:Attribute](https://data.norge.no/vocabulary/modelldcatno#Attribute) |


## Eigenskapar







  
  

  
  

  
  

  
  





  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_datatype](har_datatype.md) | * <br/> [Datatype](datatype.md) | Datatype for attributten (modelldcatno:hasDataType) |
| [har_enkel_type](har_enkel_type.md) | * <br/> [EnkelType](enkeltype.md) | Enkel type for attributten (modelldcatno:hasSimpleType) |
| [har_verdi_fra](har_verdi_fra.md) | * <br/> [Kodeliste](kodeliste.md) | Kodeliste for tillate verdiar til attributten (modelldcatno:hasValueFrom) |
| [inneholder_objekttype](inneholder_objekttype.md) | * <br/> [Objekttype](objekttype.md) | Objekttype som attributten inneheld (modelldcatno:containsObjectType) |





  
  

  
  

  
  

  
  






  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Eigenskap](eigenskap.md) |
| [begrep](begrep.md) | * <br/> [Konsept](konsept.md) | Fagomgrep ressursen handlar om (dct:subject) | [Eigenskap](eigenskap.md) |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) | [Eigenskap](eigenskap.md) |
| [navigerbar](navigerbar.md) | 0..1 <br/> [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) | Om eigenskapen er navigerbar i begge retningar (modelldcatno:navigable) | [Eigenskap](eigenskap.md) |
| [min_multiplisitet](min_multiplisitet.md) | 0..1 <br/> [NonNegativeInteger](nonnegativeinteger.md) | Minste multiplisitet for eigenskapen (modelldcatno:minOccurs) | [Eigenskap](eigenskap.md) |
| [tittel](tittel.md) | * <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) | [Eigenskap](eigenskap.md) |
| [maks_multiplisitet](maks_multiplisitet.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Høgste multiplisitet — heltalstal, "n" eller "*" (modelldcatno:maxOccurs) | [Eigenskap](eigenskap.md) |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) | [Eigenskap](eigenskap.md) |
| [har_type](har_type.md) | * <br/> [Modellelement](modellelement.md) | Type modellelement for eigenskapen (modelldcatno:hasType) | [Eigenskap](eigenskap.md) |
| [relasjonsegenskapetikett](relasjonsegenskapetikett.md) | * <br/> [LangString](langstring.md) | Lesetekst for eigenskapen i ein relasjon (modelldcatno:relationPropertyLabel) | [Eigenskap](eigenskap.md) |
| [sekvensnummer](sekvensnummer.md) | 0..1 <br/> [NonNegativeInteger](nonnegativeinteger.md) | Sekvensnummer for eigenskapen i modellelementet (modelldcatno:sequenceNumber) | [Eigenskap](eigenskap.md) |
| [tilhorer_modul](tilhorer_modul.md) | * <br/> [Modul](modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) | [Eigenskap](eigenskap.md) |
| [danner_symmetri_med](danner_symmetri_med.md) | 0..1 <br/> [Eigenskap](eigenskap.md) | Eigenskap som denne eigenskapen dannar symmetri med (modelldcatno:formsSymmet... | [Eigenskap](eigenskap.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:Attribute |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/Attributt |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Attributt
description: Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
is_a: Eigenskap
slots:
- har_datatype
- har_enkel_type
- har_verdi_fra
- inneholder_objekttype
slot_usage:
  har_datatype:
    name: har_datatype
    in_subset:
    - Anbefalt
  har_enkel_type:
    name: har_enkel_type
    in_subset:
    - Anbefalt
  har_verdi_fra:
    name: har_verdi_fra
    in_subset:
    - Anbefalt
  inneholder_objekttype:
    name: inneholder_objekttype
    in_subset:
    - Anbefalt
class_uri: modelldcatno:Attribute

```
</details>

### Induced

<details>
```yaml
name: Attributt
description: Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
is_a: Eigenskap
slot_usage:
  har_datatype:
    name: har_datatype
    in_subset:
    - Anbefalt
  har_enkel_type:
    name: har_enkel_type
    in_subset:
    - Anbefalt
  har_verdi_fra:
    name: har_verdi_fra
    in_subset:
    - Anbefalt
  inneholder_objekttype:
    name: inneholder_objekttype
    in_subset:
    - Anbefalt
attributes:
  har_datatype:
    name: har_datatype
    description: Datatype for attributten (modelldcatno:hasDataType).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:hasDataType
    owner: Attributt
    domain_of:
    - Attributt
    range: Datatype
    multivalued: true
  har_enkel_type:
    name: har_enkel_type
    description: Enkel type for attributten (modelldcatno:hasSimpleType).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:hasSimpleType
    owner: Attributt
    domain_of:
    - Attributt
    range: EnkelType
    multivalued: true
  har_verdi_fra:
    name: har_verdi_fra
    description: Kodeliste for tillate verdiar til attributten (modelldcatno:hasValueFrom).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:hasValueFrom
    owner: Attributt
    domain_of:
    - Attributt
    range: Kodeliste
    multivalued: true
  inneholder_objekttype:
    name: inneholder_objekttype
    description: Objekttype som attributten inneheld (modelldcatno:containsObjectType).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:containsObjectType
    owner: Attributt
    domain_of:
    - Attributt
    range: Objekttype
    multivalued: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Attributt
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
  begrep:
    name: begrep
    description: Fagomgrep ressursen handlar om (dct:subject).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:subject
    owner: Attributt
    domain_of:
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Kodeelement
    range: Konsept
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:identifier
    owner: Attributt
    domain_of:
    - Aktor
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    - Kodeelement
    range: string
  navigerbar:
    name: navigerbar
    description: Om eigenskapen er navigerbar i begge retningar (modelldcatno:navigable).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:navigable
    owner: Attributt
    domain_of:
    - Eigenskap
    range: boolean
  min_multiplisitet:
    name: min_multiplisitet
    description: Minste multiplisitet for eigenskapen (modelldcatno:minOccurs).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:minOccurs
    owner: Attributt
    domain_of:
    - Eigenskap
    range: NonNegativeInteger
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
    owner: Attributt
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
  maks_multiplisitet:
    name: maks_multiplisitet
    description: Høgste multiplisitet — heltalstal, "n" eller "*" (modelldcatno:maxOccurs).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:maxOccurs
    owner: Attributt
    domain_of:
    - Eigenskap
    range: string
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:description
    owner: Attributt
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    range: LangString
    multivalued: true
  har_type:
    name: har_type
    description: Type modellelement for eigenskapen (modelldcatno:hasType).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:hasType
    owner: Attributt
    domain_of:
    - Eigenskap
    range: Modellelement
    multivalued: true
  relasjonsegenskapetikett:
    name: relasjonsegenskapetikett
    description: Lesetekst for eigenskapen i ein relasjon (modelldcatno:relationPropertyLabel).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:relationPropertyLabel
    owner: Attributt
    domain_of:
    - Eigenskap
    range: LangString
    multivalued: true
  sekvensnummer:
    name: sekvensnummer
    description: Sekvensnummer for eigenskapen i modellelementet (modelldcatno:sequenceNumber).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:sequenceNumber
    owner: Attributt
    domain_of:
    - Eigenskap
    range: NonNegativeInteger
  tilhorer_modul:
    name: tilhorer_modul
    description: Modul dette elementet tilhøyrer (modelldcatno:belongsToModule).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:belongsToModule
    owner: Attributt
    domain_of:
    - Modellelement
    - Eigenskap
    - Merknad
    range: Modul
    multivalued: true
  danner_symmetri_med:
    name: danner_symmetri_med
    description: Eigenskap som denne eigenskapen dannar symmetri med (modelldcatno:formsSymmetryWith).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:formsSymmetryWith
    owner: Attributt
    domain_of:
    - Eigenskap
    range: Eigenskap
class_uri: modelldcatno:Attribute

```
</details>