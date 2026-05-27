

# Class: Modul 


_Ein modul som grupperer modellelement i informasjonsmodellen._





URI: [modelldcatno:Module](https://data.norge.no/vocabulary/modelldcatno#Module)





```mermaid
 classDiagram
    class Modul
    click Modul href "../Modul/"
      Modellelement <|-- Modul
        click Modellelement href "../Modellelement/"
      
      Modul : begrep
        
          
    
        
        
        Modul --> "*" Konsept : begrep
        click Konsept href "../Konsept/"
    

        
      Modul : beskrivelse
        
          
    
        
        
        Modul --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Modul : har_eigenskap
        
          
    
        
        
        Modul --> "*" Eigenskap : har_eigenskap
        click Eigenskap href "../Eigenskap/"
    

        
      Modul : id
        
          
    
        
        
        Modul --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Modul : identifikator_literal
        
          
    
        
        
        Modul --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Modul : tilhorer_modul
        
          
    
        
        
        Modul --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      Modul : tittel
        
          
    
        
        
        Modul --> "1..*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```





## Inheritance
* [Modellelement](modellelement.md)
    * **Modul**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:Module](https://data.norge.no/vocabulary/modelldcatno#Module) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Modellelement](modellelement.md) |
| [tittel](tittel.md) | 1..* <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) | [Modellelement](modellelement.md) |
| [begrep](begrep.md) | * <br/> [Konsept](konsept.md) | Fagomgrep ressursen handlar om (dct:subject) | [Modellelement](modellelement.md) |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) | [Modellelement](modellelement.md) |
| [har_eigenskap](har_eigenskap.md) | * <br/> [Eigenskap](eigenskap.md) | Eigenskapar modellelementet har (modelldcatno:hasProperty) | [Modellelement](modellelement.md) |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) | [Modellelement](modellelement.md) |
| [tilhorer_modul](tilhorer_modul.md) | * <br/> [Modul](modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) | [Modellelement](modellelement.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Modellelement](modellelement.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Objekttype](objekttype.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [RootObjekttype](rootobjekttype.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Datatype](datatype.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [EnkelType](enkeltype.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Kodeliste](kodeliste.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Modul](modul.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Eigenskap](eigenskap.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Attributt](attributt.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Assosiasjon](assosiasjon.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Rolle](rolle.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Spesialisering](spesialisering.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Sammensetning](sammensetning.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Realisering](realisering.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Abstraksjon](abstraksjon.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Avhengighet](avhengighet.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Samling](samling.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Valg](valg.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [AlleAv](alleav.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [NoenAv](noenav.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Merknad](merknad.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Betingelsesregel](betingelsesregel.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Og](og.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Eller](eller.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [XEllerY](xellery.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |
| [Ikke](ikke.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](modul.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:Module |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/Modul |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Modul
description: Ein modul som grupperer modellelement i informasjonsmodellen.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
is_a: Modellelement
class_uri: modelldcatno:Module

```
</details>

### Induced

<details>
```yaml
name: Modul
description: Ein modul som grupperer modellelement i informasjonsmodellen.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
is_a: Modellelement
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Modul
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
    owner: Modul
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
    owner: Modul
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
    owner: Modul
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
    owner: Modul
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
    owner: Modul
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
    owner: Modul
    domain_of:
    - Modellelement
    - Eigenskap
    - Merknad
    range: Modul
    multivalued: true
class_uri: modelldcatno:Module

```
</details>