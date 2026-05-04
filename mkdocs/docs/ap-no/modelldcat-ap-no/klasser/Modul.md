

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
        
      Modul : har_eigenskap
        
          
    
        
        
        Modul --> "*" Eigenskap : har_eigenskap
        click Eigenskap href "../Eigenskap/"
    

        
      Modul : id
        
      Modul : identifikator_literal
        
      Modul : tilhorer_modul
        
          
    
        
        
        Modul --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      Modul : tittel
        
      
```





## Inheritance
* [Modellelement](Modellelement.md)
    * **Modul**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:Module](https://data.norge.no/vocabulary/modelldcatno#Module) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | [Modellelement](Modellelement.md) |
| [tittel](tittel.md) | 1..* <br/> [LangString](LangString.md) | Namn/tittel på ressursen (dct:title) | [Modellelement](Modellelement.md) |
| [begrep](begrep.md) | * <br/> [Konsept](Konsept.md) | Fagomgrep ressursen handlar om (dct:subject) | [Modellelement](Modellelement.md) |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [String](String.md) | Tekstleg identifikator for ressursen (dct:identifier) | [Modellelement](Modellelement.md) |
| [har_eigenskap](har_eigenskap.md) | * <br/> [Eigenskap](Eigenskap.md) | Eigenskapar modellelementet har (modelldcatno:hasProperty) | [Modellelement](Modellelement.md) |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](LangString.md) | Fritekstbeskrivelse av ressursen (dct:description) | [Modellelement](Modellelement.md) |
| [tilhorer_modul](tilhorer_modul.md) | * <br/> [Modul](Modul.md) | Modul dette elementet tilhøyrer (modelldcatno:belongsToModule) | [Modellelement](Modellelement.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Modellelement](Modellelement.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Objekttype](Objekttype.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [RootObjekttype](RootObjekttype.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Datatype](Datatype.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [EnkelType](EnkelType.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Kodeliste](Kodeliste.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Modul](Modul.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Eigenskap](Eigenskap.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Attributt](Attributt.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Assosiasjon](Assosiasjon.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Rolle](Rolle.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Spesialisering](Spesialisering.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Sammensetning](Sammensetning.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Realisering](Realisering.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Abstraksjon](Abstraksjon.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Avhengighet](Avhengighet.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Samling](Samling.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Valg](Valg.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [AlleAv](AlleAv.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [NoenAv](NoenAv.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Merknad](Merknad.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Betingelsesregel](Betingelsesregel.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Og](Og.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Eller](Eller.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [XEllerY](XEllerY.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |
| [Ikke](Ikke.md) | [tilhorer_modul](tilhorer_modul.md) | range | [Modul](Modul.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:Module |
| native | https://data.norge.no/linkml/modelldcat-ap-no/Modul |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Modul
description: Ein modul som grupperer modellelement i informasjonsmodellen.
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
is_a: Modellelement
class_uri: modelldcatno:Module

```
</details>

### Induced

<details>
```yaml
name: Modul
description: Ein modul som grupperer modellelement i informasjonsmodellen.
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
is_a: Modellelement
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Modul
    domain_of:
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
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
    range: uriorcurie
    required: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:title
    alias: tittel
    owner: Modul
    domain_of:
    - Standard
    - Dokument
    - Modelkatalog
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
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:subject
    alias: begrep
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
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:identifier
    alias: identifikator_literal
    owner: Modul
    domain_of:
    - Aktor
    - Modelkatalog
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
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:hasProperty
    alias: har_eigenskap
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
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:description
    alias: beskrivelse
    owner: Modul
    domain_of:
    - Modelkatalog
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
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:belongsToModule
    alias: tilhorer_modul
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