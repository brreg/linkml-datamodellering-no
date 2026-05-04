

# Class: Hendelse 


_Ei hending som kan utløyse behov for ei offentleg teneste._





URI: [cv:Event](http://data.europa.eu/m8g/Event)





```mermaid
 classDiagram
    class Hendelse
    click Hendelse href "../Hendelse/"
      Hendelse <|-- Livshendelse
        click Livshendelse href "../Livshendelse/"
      Hendelse <|-- Virksomhetshendelse
        click Virksomhetshendelse href "../Virksomhetshendelse/"
      
      Hendelse : beskrivelse
        
      Hendelse : er_beskrive_av
        
      Hendelse : har_kontaktpunkt
        
          
    
        
        
        Hendelse --> "1..*" Kontaktpunkt : har_kontaktpunkt
        click Kontaktpunkt href "../Kontaktpunkt/"
    

        
      Hendelse : id
        
      Hendelse : identifikator_literal
        
      Hendelse : kan_utlose
        
          
    
        
        
        Hendelse --> "*" OffentligTjeneste : kan_utlose
        click OffentligTjeneste href "../OffentligTjeneste/"
    

        
      Hendelse : tema
        
          
    
        
        
        Hendelse --> "*" Konsept : tema
        click Konsept href "../Konsept/"
    

        
      Hendelse : tittel
        
      Hendelse : type_concept
        
          
    
        
        
        Hendelse --> "0..1" Konsept : type_concept
        click Konsept href "../Konsept/"
    

        
      
```





## Inheritance
* **Hendelse**
    * [Livshendelse](Livshendelse.md)
    * [Virksomhetshendelse](Virksomhetshendelse.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [cv:Event](http://data.europa.eu/m8g/Event) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tittel](tittel.md) | 1..* <br/> [LangString](LangString.md) | Namn/tittel på ressursen (dct:title) |
| [identifikator_literal](identifikator_literal.md) | 1 <br/> [String](String.md) | Tekstleg identifikator for ressursen (dct:identifier) |
| [har_kontaktpunkt](har_kontaktpunkt.md) | 1..* <br/> [Kontaktpunkt](Kontaktpunkt.md) | Kontaktpunkt for tenesta eller organisasjonen |





  
  

  
  

  
  

  
  

  
  
    
  

  
  
    
  

  
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](LangString.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [kan_utlose](kan_utlose.md) | * <br/> [OffentligTjeneste](OffentligTjeneste.md) | Offentlege tenester hendinga kan utløyse |





  
  

  
  

  
  

  
  

  
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tema](tema.md) | * <br/> [Konsept](Konsept.md) | Emne/tema tenesta handlar om |
| [er_beskrive_av](er_beskrive_av.md) | * <br/> [Uri](Uri.md) | Datasett som beskriv ressursen |
| [type_concept](type_concept.md) | 0..1 <br/> [Konsept](Konsept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | [er_gruppert_av](er_gruppert_av.md) | range | [Hendelse](Hendelse.md) |
| [OffentligTjeneste](OffentligTjeneste.md) | [er_gruppert_av](er_gruppert_av.md) | range | [Hendelse](Hendelse.md) |
| [Tjeneste](Tjeneste.md) | [er_gruppert_av](er_gruppert_av.md) | range | [Hendelse](Hendelse.md) |
| [Tjenesteresultattype](Tjenesteresultattype.md) | [kan_skape_hending](kan_skape_hending.md) | range | [Hendelse](Hendelse.md) |
| [Katalog](Katalog.md) | [inneheld_hending](inneheld_hending.md) | range | [Hendelse](Hendelse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:Event |
| native | https://data.norge.no/linkml/cpsv-ap-no/Hendelse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Hendelse
description: Ei hending som kan utløyse behov for ei offentleg teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
slots:
- id
- tittel
- identifikator_literal
- har_kontaktpunkt
- beskrivelse
- kan_utlose
- tema
- er_beskrive_av
- type_concept
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Obligatorisk
    required: true
  har_kontaktpunkt:
    name: har_kontaktpunkt
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Anbefalt
  kan_utlose:
    name: kan_utlose
    in_subset:
    - Anbefalt
  tema:
    name: tema
    in_subset:
    - Valgfri
  er_beskrive_av:
    name: er_beskrive_av
    in_subset:
    - Valgfri
  type_concept:
    name: type_concept
    in_subset:
    - Valgfri
class_uri: cv:Event

```
</details>

### Induced

<details>
```yaml
name: Hendelse
description: Ei hending som kan utløyse behov for ei offentleg teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Obligatorisk
    required: true
  har_kontaktpunkt:
    name: har_kontaktpunkt
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Anbefalt
  kan_utlose:
    name: kan_utlose
    in_subset:
    - Anbefalt
  tema:
    name: tema
    in_subset:
    - Valgfri
  er_beskrive_av:
    name: er_beskrive_av
    in_subset:
    - Valgfri
  type_concept:
    name: type_concept
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Hendelse
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
    owner: Hendelse
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
    owner: Hendelse
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
    owner: Hendelse
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
    owner: Hendelse
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
    owner: Hendelse
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
    owner: Hendelse
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
    owner: Hendelse
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
    owner: Hendelse
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
class_uri: cv:Event

```
</details>