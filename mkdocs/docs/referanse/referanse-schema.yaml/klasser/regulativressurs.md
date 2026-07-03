

# Class: RegulativRessurs 


_Ein regulativ ressurs (lov, forskrift o.l.) som gjeld for ein ressurs._





URI: [eli:LegalResource](http://data.europa.eu/eli/ontology#LegalResource)





```mermaid
 classDiagram
    class RegulativRessurs
    click RegulativRessurs href "../RegulativRessurs/"
      RegulativRessurs : beskrivelse
        
          
    
        
        
        RegulativRessurs --> "0..1" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      RegulativRessurs : har_referanse
        
          
    
        
        
        RegulativRessurs --> "*" Uri : har_referanse
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      RegulativRessurs : id
        
          
    
        
        
        RegulativRessurs --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      RegulativRessurs : identifikator_literal
        
          
    
        
        
        RegulativRessurs --> "0..1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      RegulativRessurs : relatert_regulativ_ressurs
        
          
    
        
        
        RegulativRessurs --> "*" RegulativRessurs : relatert_regulativ_ressurs
        click RegulativRessurs href "../RegulativRessurs/"
    

        
      RegulativRessurs : spraak
        
          
    
        
        
        RegulativRessurs --> "*" Spraak : spraak
        click Spraak href "../Spraak/"
    

        
      RegulativRessurs : tittel
        
          
    
        
        
        RegulativRessurs --> "0..1" LangString : tittel
        click LangString href "../LangString/"
    

        
      RegulativRessurs : type_concept
        
          
    
        
        
        RegulativRessurs --> "0..1" Konsept : type_concept
        click Konsept href "../Konsept/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [eli:LegalResource](http://data.europa.eu/eli/ontology#LegalResource) |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Unik URI-identifikator for ressursen |
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [LangString](langstring.md) | Kortfatta skildring av ressursen |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) |
| [har_referanse](har_referanse.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Referanse til ekstern ressurs (rdfs:seeAlso) |
| [spraak](spraak.md) | * <br/> [Spraak](spraak.md) | Språk brukt i ressursen (dct:language) |
| [tittel](tittel.md) | 0..1 <br/> [LangString](langstring.md) | Namn eller tittel på ressursen |
| [type_concept](type_concept.md) | 0..1 <br/> [Konsept](konsept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |
| [relatert_regulativ_ressurs](relatert_regulativ_ressurs.md) | * <br/> [RegulativRessurs](regulativressurs.md) | Relatert regulativ ressurs |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RegulativRessurs](regulativressurs.md) | [relatert_regulativ_ressurs](relatert_regulativ_ressurs.md) | range | [RegulativRessurs](regulativressurs.md) |
| [Distribusjon](distribusjon.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](regulativressurs.md) |
| [Datasett](datasett.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](regulativressurs.md) |
| [Datasettserie](datasettserie.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](regulativressurs.md) |
| [Datatjeneste](datatjeneste.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](regulativressurs.md) |
| [Katalog](katalog.md) | [gjeldende_lovgivning](gjeldende_lovgivning.md) | range | [RegulativRessurs](regulativressurs.md) |








## In Subsets


* [Metadata](metadata.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | eli:LegalResource |
| native | https://data.norge.no/ap-no/dcat-ap-no/RegulativRessurs |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RegulativRessurs
description: Ein regulativ ressurs (lov, forskrift o.l.) som gjeld for ein ressurs.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slots:
- id
- beskrivelse
- identifikator_literal
- har_referanse
- spraak
- tittel
- type_concept
- relatert_regulativ_ressurs
class_uri: eli:LegalResource

```
</details>

### Induced

<details>
```yaml
name: RegulativRessurs
description: Ein regulativ ressurs (lov, forskrift o.l.) som gjeld for ein ressurs.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
attributes:
  id:
    name: id
    description: Unik URI-identifikator for ressursen.
    from_schema: https://example.org/linkml/referanse
    rank: 1000
    slot_uri: dct:identifier
    identifier: true
    owner: RegulativRessurs
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Tekstdel
    - KatalogisertRessurs
    - Aktoer
    - Kontaktopplysning
    - Tidsrom
    - Standard
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    - Ressurs
    range: uriorcurie
    required: true
  beskrivelse:
    name: beskrivelse
    description: Kortfatta skildring av ressursen.
    from_schema: https://example.org/linkml/referanse
    rank: 1000
    slot_uri: dct:description
    owner: RegulativRessurs
    domain_of:
    - RegulativRessurs
    - Gebyr
    - Distribusjon
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalogpost
    - Katalog
    - Ressurs
    range: LangString
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:identifier
    owner: RegulativRessurs
    domain_of:
    - Aktoer
    - RegulativRessurs
    - Datasett
    - Datatjeneste
    - Katalog
    range: string
  har_referanse:
    name: har_referanse
    description: Referanse til ekstern ressurs (rdfs:seeAlso).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: rdfs:seeAlso
    owner: RegulativRessurs
    domain_of:
    - Standard
    - RegulativRessurs
    range: uri
    multivalued: true
  spraak:
    name: spraak
    description: Språk brukt i ressursen (dct:language).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:language
    owner: RegulativRessurs
    domain_of:
    - Tekstdel
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Katalogpost
    - Katalog
    range: Spraak
    multivalued: true
  tittel:
    name: tittel
    description: Namn eller tittel på ressursen.
    from_schema: https://example.org/linkml/referanse
    rank: 1000
    slot_uri: dct:title
    owner: RegulativRessurs
    domain_of:
    - Standard
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalogpost
    - Katalog
    - Ressurs
    range: LangString
  type_concept:
    name: type_concept
    description: Type ressurs frå eit kontrollert vokabular (dct:type).
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:type
    owner: RegulativRessurs
    domain_of:
    - Aktoer
    - RegulativRessurs
    - Datasett
    range: Konsept
  relatert_regulativ_ressurs:
    name: relatert_regulativ_ressurs
    description: Relatert regulativ ressurs.
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dct:relation
    owner: RegulativRessurs
    domain_of:
    - RegulativRessurs
    range: RegulativRessurs
    multivalued: true
class_uri: eli:LegalResource

```
</details>