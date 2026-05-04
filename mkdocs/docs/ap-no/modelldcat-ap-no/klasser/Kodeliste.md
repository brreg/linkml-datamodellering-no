

# Class: Kodeliste 


_Ei kodeliste — eit kontrollert vokabular av tillate verdiar._





URI: [modelldcatno:CodeList](https://data.norge.no/vocabulary/modelldcatno#CodeList)





```mermaid
 classDiagram
    class Kodeliste
    click Kodeliste href "../Kodeliste/"
      Modellelement <|-- Kodeliste
        click Modellelement href "../Modellelement/"
      
      Kodeliste : begrep
        
          
    
        
        
        Kodeliste --> "*" Konsept : begrep
        click Konsept href "../Konsept/"
    

        
      Kodeliste : beskrivelse
        
      Kodeliste : har_eigenskap
        
          
    
        
        
        Kodeliste --> "*" Eigenskap : har_eigenskap
        click Eigenskap href "../Eigenskap/"
    

        
      Kodeliste : har_referanse
        
      Kodeliste : id
        
      Kodeliste : identifikator_literal
        
      Kodeliste : tilhorer_modul
        
          
    
        
        
        Kodeliste --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      Kodeliste : tittel
        
      
```





## Inheritance
* [Modellelement](Modellelement.md)
    * **Kodeliste**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:CodeList](https://data.norge.no/vocabulary/modelldcatno#CodeList) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_referanse](har_referanse.md) | * <br/> [Uri](Uri.md) | Referanse til ekstern ressurs (rdfs:seeAlso) |




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
| [Attributt](Attributt.md) | [har_verdi_fra](har_verdi_fra.md) | range | [Kodeliste](Kodeliste.md) |
| [Kodeelement](Kodeelement.md) | [i_skjema](i_skjema.md) | range | [Kodeliste](Kodeliste.md) |
| [Kodeelement](Kodeelement.md) | [topp_begrep_av](topp_begrep_av.md) | range | [Kodeliste](Kodeliste.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:CodeList |
| native | https://data.norge.no/linkml/modelldcat-ap-no/Kodeliste |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kodeliste
description: Ei kodeliste — eit kontrollert vokabular av tillate verdiar.
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
is_a: Modellelement
slots:
- har_referanse
class_uri: modelldcatno:CodeList

```
</details>

### Induced

<details>
```yaml
name: Kodeliste
description: Ei kodeliste — eit kontrollert vokabular av tillate verdiar.
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
is_a: Modellelement
attributes:
  har_referanse:
    name: har_referanse
    description: Referanse til ekstern ressurs (rdfs:seeAlso).
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    slot_uri: rdfs:seeAlso
    alias: har_referanse
    owner: Kodeliste
    domain_of:
    - Standard
    - Kodeliste
    range: uri
    multivalued: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Kodeliste
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
    owner: Kodeliste
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
    owner: Kodeliste
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
    owner: Kodeliste
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
    owner: Kodeliste
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
    owner: Kodeliste
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
    owner: Kodeliste
    domain_of:
    - Modellelement
    - Eigenskap
    - Merknad
    range: Modul
    multivalued: true
class_uri: modelldcatno:CodeList

```
</details>