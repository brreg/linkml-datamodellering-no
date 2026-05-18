

# Class: Eigenskap 


_Abstrakt basisklasse for eigenskapar knytt til eit modellelement._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [modelldcatno:Property](https://data.norge.no/vocabulary/modelldcatno#Property)





```mermaid
 classDiagram
    class Eigenskap
    click Eigenskap href "../Eigenskap/"
      Eigenskap <|-- Attributt
        click Attributt href "../Attributt/"
      Eigenskap <|-- Assosiasjon
        click Assosiasjon href "../Assosiasjon/"
      Eigenskap <|-- Rolle
        click Rolle href "../Rolle/"
      Eigenskap <|-- Spesialisering
        click Spesialisering href "../Spesialisering/"
      Eigenskap <|-- Sammensetning
        click Sammensetning href "../Sammensetning/"
      Eigenskap <|-- Realisering
        click Realisering href "../Realisering/"
      Eigenskap <|-- Abstraksjon
        click Abstraksjon href "../Abstraksjon/"
      Eigenskap <|-- Avhengighet
        click Avhengighet href "../Avhengighet/"
      Eigenskap <|-- Samling
        click Samling href "../Samling/"
      Eigenskap <|-- Valg
        click Valg href "../Valg/"
      
      Eigenskap : begrep
        
          
    
        
        
        Eigenskap --> "*" Konsept : begrep
        click Konsept href "../Konsept/"
    

        
      Eigenskap : beskrivelse
        
          
    
        
        
        Eigenskap --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Eigenskap : danner_symmetri_med
        
          
    
        
        
        Eigenskap --> "0..1" Eigenskap : danner_symmetri_med
        click Eigenskap href "../Eigenskap/"
    

        
      Eigenskap : har_type
        
          
    
        
        
        Eigenskap --> "*" Modellelement : har_type
        click Modellelement href "../Modellelement/"
    

        
      Eigenskap : id
        
          
    
        
        
        Eigenskap --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Eigenskap : identifikator_literal
        
          
    
        
        
        Eigenskap --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Eigenskap : maks_multiplisitet
        
          
    
        
        
        Eigenskap --> "0..1" String : maks_multiplisitet
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Eigenskap : min_multiplisitet
        
          
    
        
        
        Eigenskap --> "0..1" NonNegativeInteger : min_multiplisitet
        click NonNegativeInteger href "../NonNegativeInteger/"
    

        
      Eigenskap : navigerbar
        
          
    
        
        
        Eigenskap --> "0..1" Boolean : navigerbar
        click Boolean href "../http://www.w3.org/2001/XMLSchema#boolean/"
    

        
      Eigenskap : relasjonsegenskapetikett
        
          
    
        
        
        Eigenskap --> "*" LangString : relasjonsegenskapetikett
        click LangString href "../LangString/"
    

        
      Eigenskap : sekvensnummer
        
          
    
        
        
        Eigenskap --> "0..1" NonNegativeInteger : sekvensnummer
        click NonNegativeInteger href "../NonNegativeInteger/"
    

        
      Eigenskap : tilhorer_modul
        
          
    
        
        
        Eigenskap --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      Eigenskap : tittel
        
          
    
        
        
        Eigenskap --> "*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```





## Inheritance
* **Eigenskap**
    * [Attributt](attributt.md)
    * [Assosiasjon](assosiasjon.md)
    * [Rolle](rolle.md)
    * [Spesialisering](spesialisering.md)
    * [Sammensetning](sammensetning.md)
    * [Realisering](realisering.md)
    * [Abstraksjon](abstraksjon.md)
    * [Avhengighet](avhengighet.md)
    * [Samling](samling.md)
    * [Valg](valg.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:Property](https://data.norge.no/vocabulary/modelldcatno#Property) |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  

  
  

  
  

  
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [begrep](begrep.md) | * <br/> [Konsept](konsept.md) | Fagomgrep ressursen handlar om (dct:subject) |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) |
| [navigerbar](navigerbar.md) | 0..1 <br/> [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) | Om eigenskapen er navigerbar i begge retningar (modelldcatno:navigable) |
| [min_multiplisitet](min_multiplisitet.md) | 0..1 <br/> [NonNegativeInteger](nonnegativeinteger.md) | Minste multiplisitet for eigenskapen (modelldcatno:minOccurs) |
| [tittel](tittel.md) | * <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |
| [maks_multiplisitet](maks_multiplisitet.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Høgste multiplisitet — heltalstal, "n" eller "*" (modelldcatno:maxOccurs) |





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [har_type](har_type.md) | * <br/> [Modellelement](modellelement.md) | Type modellelement for eigenskapen (modelldcatno:hasType) |
| [relasjonsegenskapetikett](relasjonsegenskapetikett.md) | * <br/> [LangString](langstring.md) | Lesetekst for eigenskapen i ein relasjon (modelldcatno:relationPropertyLabel) |
| [sekvensnummer](sekvensnummer.md) | 0..1 <br/> [NonNegativeInteger](nonnegativeinteger.md) | Sekvensnummer for eigenskapen i modellelementet (modelldcatno:sequenceNumber) |
| [tilhorer_modul](tilhorer_modul.md) | * <br/> [Modul](modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) |
| [danner_symmetri_med](danner_symmetri_med.md) | 0..1 <br/> [Eigenskap](eigenskap.md) | Eigenskap som denne eigenskapen dannar symmetri med (modelldcatno:formsSymmet... |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Modellelement](modellelement.md) | [har_eigenskap](har_eigenskap.md) | range | [Eigenskap](eigenskap.md) |
| [Objekttype](objekttype.md) | [har_eigenskap](har_eigenskap.md) | range | [Eigenskap](eigenskap.md) |
| [RootObjekttype](rootobjekttype.md) | [har_eigenskap](har_eigenskap.md) | range | [Eigenskap](eigenskap.md) |
| [Datatype](datatype.md) | [har_eigenskap](har_eigenskap.md) | range | [Eigenskap](eigenskap.md) |
| [EnkelType](enkeltype.md) | [har_eigenskap](har_eigenskap.md) | range | [Eigenskap](eigenskap.md) |
| [Kodeliste](kodeliste.md) | [har_eigenskap](har_eigenskap.md) | range | [Eigenskap](eigenskap.md) |
| [Modul](modul.md) | [har_eigenskap](har_eigenskap.md) | range | [Eigenskap](eigenskap.md) |
| [Eigenskap](eigenskap.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Attributt](attributt.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Assosiasjon](assosiasjon.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Rolle](rolle.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Spesialisering](spesialisering.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Sammensetning](sammensetning.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Realisering](realisering.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Abstraksjon](abstraksjon.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Avhengighet](avhengighet.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Samling](samling.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [Valg](valg.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [AlleAv](alleav.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |
| [NoenAv](noenav.md) | [danner_symmetri_med](danner_symmetri_med.md) | range | [Eigenskap](eigenskap.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:Property |
| native | https://data.norge.no/linkml/modelldcat-ap-no/Eigenskap |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Eigenskap
description: Abstrakt basisklasse for eigenskapar knytt til eit modellelement.
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
abstract: true
slots:
- id
- begrep
- identifikator_literal
- navigerbar
- min_multiplisitet
- tittel
- maks_multiplisitet
- beskrivelse
- har_type
- relasjonsegenskapetikett
- sekvensnummer
- tilhorer_modul
- danner_symmetri_med
slot_usage:
  begrep:
    name: begrep
    in_subset:
    - Anbefalt
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Anbefalt
  navigerbar:
    name: navigerbar
    in_subset:
    - Anbefalt
  min_multiplisitet:
    name: min_multiplisitet
    in_subset:
    - Anbefalt
  tittel:
    name: tittel
    in_subset:
    - Anbefalt
  maks_multiplisitet:
    name: maks_multiplisitet
    in_subset:
    - Anbefalt
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
  har_type:
    name: har_type
    in_subset:
    - Valgfri
  relasjonsegenskapetikett:
    name: relasjonsegenskapetikett
    in_subset:
    - Valgfri
  sekvensnummer:
    name: sekvensnummer
    in_subset:
    - Valgfri
  tilhorer_modul:
    name: tilhorer_modul
    in_subset:
    - Valgfri
  danner_symmetri_med:
    name: danner_symmetri_med
    in_subset:
    - Valgfri
class_uri: modelldcatno:Property

```
</details>

### Induced

<details>
```yaml
name: Eigenskap
description: Abstrakt basisklasse for eigenskapar knytt til eit modellelement.
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
abstract: true
slot_usage:
  begrep:
    name: begrep
    in_subset:
    - Anbefalt
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Anbefalt
  navigerbar:
    name: navigerbar
    in_subset:
    - Anbefalt
  min_multiplisitet:
    name: min_multiplisitet
    in_subset:
    - Anbefalt
  tittel:
    name: tittel
    in_subset:
    - Anbefalt
  maks_multiplisitet:
    name: maks_multiplisitet
    in_subset:
    - Anbefalt
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
  har_type:
    name: har_type
    in_subset:
    - Valgfri
  relasjonsegenskapetikett:
    name: relasjonsegenskapetikett
    in_subset:
    - Valgfri
  sekvensnummer:
    name: sekvensnummer
    in_subset:
    - Valgfri
  tilhorer_modul:
    name: tilhorer_modul
    in_subset:
    - Valgfri
  danner_symmetri_med:
    name: danner_symmetri_med
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    alias: id
    owner: Eigenskap
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
  begrep:
    name: begrep
    description: Fagomgrep ressursen handlar om (dct:subject).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:subject
    alias: begrep
    owner: Eigenskap
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
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:identifier
    alias: identifikator_literal
    owner: Eigenskap
    domain_of:
    - Aktor
    - Modelkatalog
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
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:navigable
    alias: navigerbar
    owner: Eigenskap
    domain_of:
    - Eigenskap
    range: boolean
  min_multiplisitet:
    name: min_multiplisitet
    description: Minste multiplisitet for eigenskapen (modelldcatno:minOccurs).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:minOccurs
    alias: min_multiplisitet
    owner: Eigenskap
    domain_of:
    - Eigenskap
    range: NonNegativeInteger
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:title
    alias: tittel
    owner: Eigenskap
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
  maks_multiplisitet:
    name: maks_multiplisitet
    description: Høgste multiplisitet — heltalstal, "n" eller "*" (modelldcatno:maxOccurs).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:maxOccurs
    alias: maks_multiplisitet
    owner: Eigenskap
    domain_of:
    - Eigenskap
    range: string
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:description
    alias: beskrivelse
    owner: Eigenskap
    domain_of:
    - Modelkatalog
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
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:hasType
    alias: har_type
    owner: Eigenskap
    domain_of:
    - Eigenskap
    range: Modellelement
    multivalued: true
  relasjonsegenskapetikett:
    name: relasjonsegenskapetikett
    description: Lesetekst for eigenskapen i ein relasjon (modelldcatno:relationPropertyLabel).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:relationPropertyLabel
    alias: relasjonsegenskapetikett
    owner: Eigenskap
    domain_of:
    - Eigenskap
    range: LangString
    multivalued: true
  sekvensnummer:
    name: sekvensnummer
    description: Sekvensnummer for eigenskapen i modellelementet (modelldcatno:sequenceNumber).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:sequenceNumber
    alias: sekvensnummer
    owner: Eigenskap
    domain_of:
    - Eigenskap
    range: NonNegativeInteger
  tilhorer_modul:
    name: tilhorer_modul
    description: Modul dette elementet tilhøyrer (modelldcatno:belongsToModule).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:belongsToModule
    alias: tilhorer_modul
    owner: Eigenskap
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
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:formsSymmetryWith
    alias: danner_symmetri_med
    owner: Eigenskap
    domain_of:
    - Eigenskap
    range: Eigenskap
class_uri: modelldcatno:Property

```
</details>