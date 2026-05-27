

# Class: Sammensetning 


_Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement._





URI: [modelldcatno:Composition](https://data.norge.no/vocabulary/modelldcatno#Composition)





```mermaid
 classDiagram
    class Sammensetning
    click Sammensetning href "../Sammensetning/"
      Eigenskap <|-- Sammensetning
        click Eigenskap href "../Eigenskap/"
      
      Sammensetning : begrep
        
          
    
        
        
        Sammensetning --> "*" Konsept : begrep
        click Konsept href "../Konsept/"
    

        
      Sammensetning : beskrivelse
        
          
    
        
        
        Sammensetning --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Sammensetning : danner_symmetri_med
        
          
    
        
        
        Sammensetning --> "0..1" Eigenskap : danner_symmetri_med
        click Eigenskap href "../Eigenskap/"
    

        
      Sammensetning : har_type
        
          
    
        
        
        Sammensetning --> "*" Modellelement : har_type
        click Modellelement href "../Modellelement/"
    

        
      Sammensetning : id
        
          
    
        
        
        Sammensetning --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Sammensetning : identifikator_literal
        
          
    
        
        
        Sammensetning --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Sammensetning : inneholder
        
          
    
        
        
        Sammensetning --> "0..1" Modellelement : inneholder
        click Modellelement href "../Modellelement/"
    

        
      Sammensetning : maks_multiplisitet
        
          
    
        
        
        Sammensetning --> "0..1" String : maks_multiplisitet
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Sammensetning : min_multiplisitet
        
          
    
        
        
        Sammensetning --> "0..1" NonNegativeInteger : min_multiplisitet
        click NonNegativeInteger href "../NonNegativeInteger/"
    

        
      Sammensetning : navigerbar
        
          
    
        
        
        Sammensetning --> "0..1" Boolean : navigerbar
        click Boolean href "../http://www.w3.org/2001/XMLSchema#boolean/"
    

        
      Sammensetning : relasjonsegenskapetikett
        
          
    
        
        
        Sammensetning --> "*" LangString : relasjonsegenskapetikett
        click LangString href "../LangString/"
    

        
      Sammensetning : sekvensnummer
        
          
    
        
        
        Sammensetning --> "0..1" NonNegativeInteger : sekvensnummer
        click NonNegativeInteger href "../NonNegativeInteger/"
    

        
      Sammensetning : tilhorer_modul
        
          
    
        
        
        Sammensetning --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      Sammensetning : tittel
        
          
    
        
        
        Sammensetning --> "*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```





## Inheritance
* [Eigenskap](eigenskap.md)
    * **Sammensetning**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:Composition](https://data.norge.no/vocabulary/modelldcatno#Composition) |


## Eigenskapar







  
  





  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [inneholder](inneholder.md) | 0..1 <br/> [Modellelement](modellelement.md) | Modellelement som er del av samansetjinga (modelldcatno:contains) |





  
  






  
  
  
    
      
    
      
    
      
    
  
  




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
| self | modelldcatno:Composition |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/Sammensetning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sammensetning
description: Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
is_a: Eigenskap
slots:
- inneholder
slot_usage:
  inneholder:
    name: inneholder
    in_subset:
    - Anbefalt
class_uri: modelldcatno:Composition

```
</details>

### Induced

<details>
```yaml
name: Sammensetning
description: Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
is_a: Eigenskap
slot_usage:
  inneholder:
    name: inneholder
    in_subset:
    - Anbefalt
attributes:
  inneholder:
    name: inneholder
    description: Modellelement som er del av samansetjinga (modelldcatno:contains).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:contains
    owner: Sammensetning
    domain_of:
    - Sammensetning
    range: Modellelement
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
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
    owner: Sammensetning
    domain_of:
    - Eigenskap
    range: Eigenskap
class_uri: modelldcatno:Composition

```
</details>