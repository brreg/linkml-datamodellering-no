

# Class: Livshendelse 


_Ei livshending som kan utløyse behov for tenester (t.d. fødsel, ekteskap)._





URI: [cv:LifeEvent](http://data.europa.eu/m8g/LifeEvent)





```mermaid
 classDiagram
    class Livshendelse
    click Livshendelse href "../Livshendelse/"
      Hendelse <|-- Livshendelse
        click Hendelse href "../Hendelse/"
      
      Livshendelse : beskrivelse
        
      Livshendelse : er_beskrive_av
        
      Livshendelse : har_kontaktpunkt
        
          
    
        
        
        Livshendelse --> "1..*" Kontaktpunkt : har_kontaktpunkt
        click Kontaktpunkt href "../Kontaktpunkt/"
    

        
      Livshendelse : id
        
      Livshendelse : identifikator_literal
        
      Livshendelse : kan_utlose
        
          
    
        
        
        Livshendelse --> "*" OffentligTjeneste : kan_utlose
        click OffentligTjeneste href "../OffentligTjeneste/"
    

        
      Livshendelse : kan_utlose_behov_for
        
      Livshendelse : tema
        
          
    
        
        
        Livshendelse --> "*" Konsept : tema
        click Konsept href "../Konsept/"
    

        
      Livshendelse : tittel
        
      Livshendelse : type_concept
        
          
    
        
        
        Livshendelse --> "0..1" Konsept : type_concept
        click Konsept href "../Konsept/"
    

        
      
```





## Inheritance
* [Hendelse](Hendelse.md)
    * **Livshendelse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [cv:LifeEvent](http://data.europa.eu/m8g/LifeEvent) |


## Eigenskapar







  
  





  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kan_utlose_behov_for](kan_utlose_behov_for.md) | * <br/> [Uriorcurie](Uriorcurie.md) | Tenester det kan oppstå behov for som følgje av hendinga |





  
  






  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | [Hendelse](Hendelse.md) |
| [tittel](tittel.md) | 1..* <br/> [LangString](LangString.md) | Namn/tittel på ressursen (dct:title) | [Hendelse](Hendelse.md) |
| [identifikator_literal](identifikator_literal.md) | 1 <br/> [String](String.md) | Tekstleg identifikator for ressursen (dct:identifier) | [Hendelse](Hendelse.md) |
| [har_kontaktpunkt](har_kontaktpunkt.md) | 1..* <br/> [Kontaktpunkt](Kontaktpunkt.md) | Kontaktpunkt for tenesta eller organisasjonen | [Hendelse](Hendelse.md) |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](LangString.md) | Fritekstbeskrivelse av ressursen (dct:description) | [Hendelse](Hendelse.md) |
| [kan_utlose](kan_utlose.md) | * <br/> [OffentligTjeneste](OffentligTjeneste.md) | Offentlege tenester hendinga kan utløyse | [Hendelse](Hendelse.md) |
| [tema](tema.md) | * <br/> [Konsept](Konsept.md) | Emne/tema tenesta handlar om | [Hendelse](Hendelse.md) |
| [er_beskrive_av](er_beskrive_av.md) | * <br/> [Uri](Uri.md) | Datasett som beskriv ressursen | [Hendelse](Hendelse.md) |
| [type_concept](type_concept.md) | 0..1 <br/> [Konsept](Konsept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) | [Hendelse](Hendelse.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:LifeEvent |
| native | https://data.norge.no/linkml/cpsv-ap-no/Livshendelse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Livshendelse
description: Ei livshending som kan utløyse behov for tenester (t.d. fødsel, ekteskap).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
is_a: Hendelse
slots:
- kan_utlose_behov_for
slot_usage:
  kan_utlose_behov_for:
    name: kan_utlose_behov_for
    in_subset:
    - Anbefalt
class_uri: cv:LifeEvent

```
</details>

### Induced

<details>
```yaml
name: Livshendelse
description: Ei livshending som kan utløyse behov for tenester (t.d. fødsel, ekteskap).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
is_a: Hendelse
slot_usage:
  kan_utlose_behov_for:
    name: kan_utlose_behov_for
    in_subset:
    - Anbefalt
attributes:
  kan_utlose_behov_for:
    name: kan_utlose_behov_for
    description: Tenester det kan oppstå behov for som følgje av hendinga.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: cpsvno:mayTriggerNeedFor
    alias: kan_utlose_behov_for
    owner: Livshendelse
    domain_of:
    - Livshendelse
    - Virksomhetshendelse
    range: uriorcurie
    multivalued: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Livshendelse
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Aktor
    - Kontaktpunkt
    - Tjenestekanal
    - Dokumentasjonstype
    - Tjenesteresultattype
    - Tjenesteresultattypeliste
    - Gebyr
    - Regel
    - RegulativRessurs
    - Deltagelse
    - Adresse
    - Katalog
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
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: dct:title
    alias: tittel
    owner: Livshendelse
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Aktor
    - Dokumentasjonstype
    - Tjenesteresultattype
    - Tjenesteresultattypeliste
    - Regel
    - RegulativRessurs
    - Katalog
    range: LangString
    required: true
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: dct:identifier
    alias: identifikator_literal
    owner: Livshendelse
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Aktor
    - Tjenestekanal
    - Dokumentasjonstype
    - Tjenesteresultattype
    - Gebyr
    - Regel
    - RegulativRessurs
    - Katalog
    range: string
    required: true
  har_kontaktpunkt:
    name: har_kontaktpunkt
    description: Kontaktpunkt for tenesta eller organisasjonen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: cv:contactPoint
    alias: har_kontaktpunkt
    owner: Livshendelse
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Katalog
    range: Kontaktpunkt
    required: true
    multivalued: true
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: dct:description
    alias: beskrivelse
    owner: Livshendelse
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Tjenestekanal
    - Dokumentasjonstype
    - Tjenesteresultattype
    - Tjenesteresultattypeliste
    - Gebyr
    - Regel
    - Katalog
    range: LangString
    multivalued: true
  kan_utlose:
    name: kan_utlose
    description: Offentlege tenester hendinga kan utløyse.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: cpsvno:mayTrigger
    alias: kan_utlose
    owner: Livshendelse
    domain_of:
    - Hendelse
    range: OffentligTjeneste
    multivalued: true
  tema:
    name: tema
    description: Emne/tema tenesta handlar om.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: dct:subject
    alias: tema
    owner: Livshendelse
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    range: Konsept
    multivalued: true
  er_beskrive_av:
    name: er_beskrive_av
    description: Datasett som beskriv ressursen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: cccevno:isDescribedBy
    alias: er_beskrive_av
    owner: Livshendelse
    domain_of:
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Dokumentasjonstype
    - Tjenesteresultattype
    range: uri
    multivalued: true
  type_concept:
    name: type_concept
    description: Type ressurs frå eit kontrollert vokabular (dct:type).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: dct:type
    alias: type_concept
    owner: Livshendelse
    domain_of:
    - LovpalagtTjeneste
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - OffentligOrganisasjon
    - Tjenestekanal
    - Tjenesteresultattype
    - Regel
    - RegulativRessurs
    range: Konsept
class_uri: cv:LifeEvent

```
</details>