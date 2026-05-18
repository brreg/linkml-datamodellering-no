

# Class: Tjenesteresultattype 


_Typen resultat som ei teneste produserer._





URI: [cpsvno:OutputType](https://data.norge.no/vocabulary/cpsvno#OutputType)





```mermaid
 classDiagram
    class Tjenesteresultattype
    click Tjenesteresultattype href "../Tjenesteresultattype/"
      Tjenesteresultattype : beskrivelse
        
          
    
        
        
        Tjenesteresultattype --> "1..*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Tjenesteresultattype : er_beskrive_av
        
          
    
        
        
        Tjenesteresultattype --> "*" Uri : er_beskrive_av
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Tjenesteresultattype : er_spesifisert_i
        
          
    
        
        
        Tjenesteresultattype --> "0..1" Uriorcurie : er_spesifisert_i
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Tjenesteresultattype : id
        
          
    
        
        
        Tjenesteresultattype --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Tjenesteresultattype : identifikator_literal
        
          
    
        
        
        Tjenesteresultattype --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Tjenesteresultattype : kan_skape_hending
        
          
    
        
        
        Tjenesteresultattype --> "*" Hendelse : kan_skape_hending
        click Hendelse href "../Hendelse/"
    

        
      Tjenesteresultattype : mogleg_spraak
        
          
    
        
        
        Tjenesteresultattype --> "*" Spraak : mogleg_spraak
        click Spraak href "../Spraak/"
    

        
      Tjenesteresultattype : tittel
        
          
    
        
        
        Tjenesteresultattype --> "1..*" LangString : tittel
        click LangString href "../LangString/"
    

        
      Tjenesteresultattype : type_concept
        
          
    
        
        
        Tjenesteresultattype --> "0..1" Konsept : type_concept
        click Konsept href "../Konsept/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [cpsvno:OutputType](https://data.norge.no/vocabulary/cpsvno#OutputType) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  

  
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tittel](tittel.md) | 1..* <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |
| [beskrivelse](beskrivelse.md) | 1..* <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) |





  
  

  
  

  
  

  
  

  
  
    
  

  
  

  
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [mogleg_spraak](mogleg_spraak.md) | * <br/> [Spraak](spraak.md) | Mogleg språk for tenesteresultatet |





  
  

  
  

  
  

  
  
    
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) |
| [er_beskrive_av](er_beskrive_av.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Datasett som beskriv ressursen |
| [er_spesifisert_i](er_spesifisert_i.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Liste eller spesifikasjon ressursen er del av |
| [kan_skape_hending](kan_skape_hending.md) | * <br/> [Hendelse](hendelse.md) | Hending tenesteresultatet kan skape |
| [type_concept](type_concept.md) | 0..1 <br/> [Konsept](konsept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OffentligTjeneste](offentligtjeneste.md) | [har_tenesteresultattype](har_tenesteresultattype.md) | range | [Tjenesteresultattype](tjenesteresultattype.md) |
| [Tjeneste](tjeneste.md) | [har_tenesteresultattype](har_tenesteresultattype.md) | range | [Tjenesteresultattype](tjenesteresultattype.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cpsvno:OutputType |
| native | https://data.norge.no/linkml/cpsv-ap-no/Tjenesteresultattype |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Tjenesteresultattype
description: Typen resultat som ei teneste produserer.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slots:
- id
- tittel
- beskrivelse
- identifikator_literal
- mogleg_spraak
- er_beskrive_av
- er_spesifisert_i
- kan_skape_hending
- type_concept
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Obligatorisk
    required: true
  mogleg_spraak:
    name: mogleg_spraak
    in_subset:
    - Anbefalt
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Valgfri
  er_beskrive_av:
    name: er_beskrive_av
    in_subset:
    - Valgfri
  er_spesifisert_i:
    name: er_spesifisert_i
    in_subset:
    - Valgfri
  kan_skape_hending:
    name: kan_skape_hending
    in_subset:
    - Valgfri
  type_concept:
    name: type_concept
    in_subset:
    - Valgfri
class_uri: cpsvno:OutputType

```
</details>

### Induced

<details>
```yaml
name: Tjenesteresultattype
description: Typen resultat som ei teneste produserer.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Obligatorisk
    required: true
  mogleg_spraak:
    name: mogleg_spraak
    in_subset:
    - Anbefalt
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Valgfri
  er_beskrive_av:
    name: er_beskrive_av
    in_subset:
    - Valgfri
  er_spesifisert_i:
    name: er_spesifisert_i
    in_subset:
    - Valgfri
  kan_skape_hending:
    name: kan_skape_hending
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
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    alias: id
    owner: Tjenesteresultattype
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
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
    range: uriorcurie
    required: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:title
    alias: tittel
    owner: Tjenesteresultattype
    domain_of:
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
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:description
    alias: beskrivelse
    owner: Tjenesteresultattype
    domain_of:
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
    required: true
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:identifier
    alias: identifikator_literal
    owner: Tjenesteresultattype
    domain_of:
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
  mogleg_spraak:
    name: mogleg_spraak
    description: Mogleg språk for tenesteresultatet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: cpsvno:possibleLanguage
    alias: mogleg_spraak
    owner: Tjenesteresultattype
    domain_of:
    - Tjenesteresultattype
    range: Spraak
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
    owner: Tjenesteresultattype
    domain_of:
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Dokumentasjonstype
    - Tjenesteresultattype
    range: uri
    multivalued: true
  er_spesifisert_i:
    name: er_spesifisert_i
    description: Liste eller spesifikasjon ressursen er del av.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: cv:isSpecifiedIn
    alias: er_spesifisert_i
    owner: Tjenesteresultattype
    domain_of:
    - Dokumentasjonstype
    - Tjenesteresultattype
    range: uriorcurie
  kan_skape_hending:
    name: kan_skape_hending
    description: Hending tenesteresultatet kan skape.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: xkos:causes
    alias: kan_skape_hending
    owner: Tjenesteresultattype
    domain_of:
    - Tjenesteresultattype
    range: Hendelse
    multivalued: true
  type_concept:
    name: type_concept
    description: Type ressurs frå eit kontrollert vokabular (dct:type).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:type
    alias: type_concept
    owner: Tjenesteresultattype
    domain_of:
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - OffentligOrganisasjon
    - Tjenestekanal
    - Tjenesteresultattype
    - Regel
    - RegulativRessurs
    range: Konsept
class_uri: cpsvno:OutputType

```
</details>