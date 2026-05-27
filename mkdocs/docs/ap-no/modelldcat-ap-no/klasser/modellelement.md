

# Class: Modellelement 


_Abstrakt basisklasse for alle modellelement i ein informasjonsmodell._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [modelldcatno:ModelElement](https://data.norge.no/vocabulary/modelldcatno#ModelElement)





```mermaid
 classDiagram
    class Modellelement
    click Modellelement href "../Modellelement/"
      Modellelement <|-- Objekttype
        click Objekttype href "../Objekttype/"
      Modellelement <|-- RootObjekttype
        click RootObjekttype href "../RootObjekttype/"
      Modellelement <|-- Datatype
        click Datatype href "../Datatype/"
      Modellelement <|-- EnkelType
        click EnkelType href "../EnkelType/"
      Modellelement <|-- Kodeliste
        click Kodeliste href "../Kodeliste/"
      Modellelement <|-- Modul
        click Modul href "../Modul/"
      
      Modellelement : begrep
        
          
    
        
        
        Modellelement --> "*" Konsept : begrep
        click Konsept href "../Konsept/"
    

        
      Modellelement : beskrivelse
        
          
    
        
        
        Modellelement --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Modellelement : har_eigenskap
        
          
    
        
        
        Modellelement --> "*" Eigenskap : har_eigenskap
        click Eigenskap href "../Eigenskap/"
    

        
      Modellelement : id
        
          
    
        
        
        Modellelement --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Modellelement : identifikator_literal
        
          
    
        
        
        Modellelement --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Modellelement : tilhorer_modul
        
          
    
        
        
        Modellelement --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      Modellelement : tittel
        
          
    
        
        
        Modellelement --> "1..*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```





## Inheritance
* **Modellelement**
    * [Objekttype](objekttype.md)
    * [RootObjekttype](rootobjekttype.md)
    * [Datatype](datatype.md)
    * [EnkelType](enkeltype.md)
    * [Kodeliste](kodeliste.md)
    * [Modul](modul.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:ModelElement](https://data.norge.no/vocabulary/modelldcatno#ModelElement) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tittel](tittel.md) | 1..* <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |





  
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [begrep](begrep.md) | * <br/> [Konsept](konsept.md) | Fagomgrep ressursen handlar om (dct:subject) |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) |
| [har_eigenskap](har_eigenskap.md) | * <br/> [Eigenskap](eigenskap.md) | Eigenskapar modellelementet har (modelldcatno:hasProperty) |





  
  

  
  

  
  

  
  

  
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [tilhorer_modul](tilhorer_modul.md) | * <br/> [Modul](modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Informasjonsmodell](informasjonsmodell.md) | [inneholder_modellelement](inneholder_modellelement.md) | range | [Modellelement](modellelement.md) |
| [Eigenskap](eigenskap.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Attributt](attributt.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Assosiasjon](assosiasjon.md) | [refererer_til](refererer_til.md) | range | [Modellelement](modellelement.md) |
| [Assosiasjon](assosiasjon.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Rolle](rolle.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Spesialisering](spesialisering.md) | [har_generelt_begrep](har_generelt_begrep.md) | range | [Modellelement](modellelement.md) |
| [Spesialisering](spesialisering.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Sammensetning](sammensetning.md) | [inneholder](inneholder.md) | range | [Modellelement](modellelement.md) |
| [Sammensetning](sammensetning.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Realisering](realisering.md) | [har_leverandor](har_leverandor.md) | range | [Modellelement](modellelement.md) |
| [Realisering](realisering.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Abstraksjon](abstraksjon.md) | [er_abstraksjon_av](er_abstraksjon_av.md) | range | [Modellelement](modellelement.md) |
| [Abstraksjon](abstraksjon.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Avhengighet](avhengighet.md) | [avhengig_av](avhengig_av.md) | range | [Modellelement](modellelement.md) |
| [Avhengighet](avhengighet.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Samling](samling.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Valg](valg.md) | [har_noe](har_noe.md) | range | [Modellelement](modellelement.md) |
| [Valg](valg.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [AlleAv](alleav.md) | [har_noe](har_noe.md) | range | [Modellelement](modellelement.md) |
| [AlleAv](alleav.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [NoenAv](noenav.md) | [har_noe](har_noe.md) | range | [Modellelement](modellelement.md) |
| [NoenAv](noenav.md) | [har_type](har_type.md) | range | [Modellelement](modellelement.md) |
| [Merknad](merknad.md) | [annoterer](annoterer.md) | range | [Modellelement](modellelement.md) |
| [Betingelsesregel](betingelsesregel.md) | [betinger](betinger.md) | range | [Modellelement](modellelement.md) |
| [Betingelsesregel](betingelsesregel.md) | [annoterer](annoterer.md) | range | [Modellelement](modellelement.md) |
| [Og](og.md) | [betinger](betinger.md) | range | [Modellelement](modellelement.md) |
| [Og](og.md) | [annoterer](annoterer.md) | range | [Modellelement](modellelement.md) |
| [Eller](eller.md) | [betinger](betinger.md) | range | [Modellelement](modellelement.md) |
| [Eller](eller.md) | [annoterer](annoterer.md) | range | [Modellelement](modellelement.md) |
| [XEllerY](xellery.md) | [betinger](betinger.md) | range | [Modellelement](modellelement.md) |
| [XEllerY](xellery.md) | [annoterer](annoterer.md) | range | [Modellelement](modellelement.md) |
| [Ikke](ikke.md) | [betinger](betinger.md) | range | [Modellelement](modellelement.md) |
| [Ikke](ikke.md) | [annoterer](annoterer.md) | range | [Modellelement](modellelement.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:ModelElement |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/Modellelement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Modellelement
description: Abstrakt basisklasse for alle modellelement i ein informasjonsmodell.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
abstract: true
slots:
- id
- tittel
- begrep
- identifikator_literal
- har_eigenskap
- beskrivelse
- tilhorer_modul
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  begrep:
    name: begrep
    in_subset:
    - Anbefalt
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Anbefalt
  har_eigenskap:
    name: har_eigenskap
    in_subset:
    - Anbefalt
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
  tilhorer_modul:
    name: tilhorer_modul
    in_subset:
    - Valgfri
class_uri: modelldcatno:ModelElement

```
</details>

### Induced

<details>
```yaml
name: Modellelement
description: Abstrakt basisklasse for alle modellelement i ein informasjonsmodell.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
abstract: true
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  begrep:
    name: begrep
    in_subset:
    - Anbefalt
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Anbefalt
  har_eigenskap:
    name: har_eigenskap
    in_subset:
    - Anbefalt
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
  tilhorer_modul:
    name: tilhorer_modul
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Modellelement
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
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
    owner: Modellelement
    domain_of:
    - Standard
    - Dokument
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    range: LangString
    required: true
    multivalued: true
  begrep:
    name: begrep
    description: Fagomgrep ressursen handlar om (dct:subject).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:subject
    owner: Modellelement
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
    owner: Modellelement
    domain_of:
    - Aktor
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    - Kodeelement
    range: string
  har_eigenskap:
    name: har_eigenskap
    description: Eigenskapar modellelementet har (modelldcatno:hasProperty).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:hasProperty
    owner: Modellelement
    domain_of:
    - Modellelement
    range: Eigenskap
    multivalued: true
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:description
    owner: Modellelement
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
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
    owner: Modellelement
    domain_of:
    - Modellelement
    - Eigenskap
    - Merknad
    range: Modul
    multivalued: true
class_uri: modelldcatno:ModelElement

```
</details>