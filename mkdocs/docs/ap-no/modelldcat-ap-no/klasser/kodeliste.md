

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
        
          
    
        
        
        Kodeliste --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Kodeliste : har_eigenskap
        
          
    
        
        
        Kodeliste --> "*" Eigenskap : har_eigenskap
        click Eigenskap href "../Eigenskap/"
    

        
      Kodeliste : har_referanse
        
          
    
        
        
        Kodeliste --> "*" Uri : har_referanse
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Kodeliste : id
        
          
    
        
        
        Kodeliste --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Kodeliste : identifikator_literal
        
          
    
        
        
        Kodeliste --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Kodeliste : tilhorer_modul
        
          
    
        
        
        Kodeliste --> "*" Modul : tilhorer_modul
        click Modul href "../Modul/"
    

        
      Kodeliste : tittel
        
          
    
        
        
        Kodeliste --> "1..*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```





## Inheritance
* [Modellelement](modellelement.md)
    * **Kodeliste**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [modelldcatno:CodeList](https://data.norge.no/vocabulary/modelldcatno#CodeList) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_referanse](har_referanse.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Referanse til ekstern ressurs (rdfs:seeAlso) |




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
| [Attributt](attributt.md) | [har_verdi_fra](har_verdi_fra.md) | range | [Kodeliste](kodeliste.md) |
| [Kodeelement](kodeelement.md) | [i_skjema](i_skjema.md) | range | [Kodeliste](kodeliste.md) |
| [Kodeelement](kodeelement.md) | [topp_begrep_av](topp_begrep_av.md) | range | [Kodeliste](kodeliste.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:CodeList |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/Kodeliste |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kodeliste
description: Ei kodeliste — eit kontrollert vokabular av tillate verdiar.
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
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
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
is_a: Modellelement
attributes:
  har_referanse:
    name: har_referanse
    description: Referanse til ekstern ressurs (rdfs:seeAlso).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: rdfs:seeAlso
    owner: Kodeliste
    domain_of:
    - Standard
    - Kodeliste
    range: uri
    multivalued: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Kodeliste
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
    owner: Kodeliste
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
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:identifier
    owner: Kodeliste
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
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:description
    owner: Kodeliste
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