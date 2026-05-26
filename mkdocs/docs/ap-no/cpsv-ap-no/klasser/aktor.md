

# Class: Aktor 


_Ein aktør (person eller organisasjon) relatert til ei teneste._





URI: [foaf:Agent](http://xmlns.com/foaf/0.1/Agent)





```mermaid
 classDiagram
    class Aktor
    click Aktor href "../Aktor/"
      Aktor <|-- OffentligOrganisasjon
        click OffentligOrganisasjon href "../OffentligOrganisasjon/"
      
      Aktor : adresse_ref
        
          
    
        
        
        Aktor --> "0..1" Adresse : adresse_ref
        click Adresse href "../Adresse/"
    

        
      Aktor : deltek_i
        
          
    
        
        
        Aktor --> "*" Deltagelse : deltek_i
        click Deltagelse href "../Deltagelse/"
    

        
      Aktor : id
        
          
    
        
        
        Aktor --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Aktor : identifikator_literal
        
          
    
        
        
        Aktor --> "1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Aktor : tittel
        
          
    
        
        
        Aktor --> "1..*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```





## Inheritance
* **Aktor**
    * [OffentligOrganisasjon](offentligorganisasjon.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [foaf:Agent](http://xmlns.com/foaf/0.1/Agent) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tittel](tittel.md) | 1..* <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |
| [identifikator_literal](identifikator_literal.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) |





  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [adresse_ref](adresse_ref.md) | 0..1 <br/> [Adresse](adresse.md) | Postadresse knytt til aktøren |
| [deltek_i](deltek_i.md) | * <br/> [Deltagelse](deltagelse.md) | Deltakingar aktøren er del av |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Tjeneste](tjeneste.md) | [eigd_av](eigd_av.md) | range | [Aktor](aktor.md) |
| [Deltagelse](deltagelse.md) | [deltakar](deltakar.md) | range | [Aktor](aktor.md) |
| [Katalog](katalog.md) | [utgjevar](utgjevar.md) | range | [Aktor](aktor.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:Agent |
| native | https://data.norge.no/linkml/cpsv-ap-no/Aktor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aktor
description: Ein aktør (person eller organisasjon) relatert til ei teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slots:
- id
- tittel
- identifikator_literal
- adresse_ref
- deltek_i
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
  adresse_ref:
    name: adresse_ref
    in_subset:
    - Valgfri
  deltek_i:
    name: deltek_i
    in_subset:
    - Valgfri
class_uri: foaf:Agent

```
</details>

### Induced

<details>
```yaml
name: Aktor
description: Ein aktør (person eller organisasjon) relatert til ei teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
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
  adresse_ref:
    name: adresse_ref
    in_subset:
    - Valgfri
  deltek_i:
    name: deltek_i
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    owner: Aktor
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
    owner: Aktor
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
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:identifier
    owner: Aktor
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
    required: true
  adresse_ref:
    name: adresse_ref
    description: Postadresse knytt til aktøren.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: locn:address
    owner: Aktor
    domain_of:
    - Aktor
    range: Adresse
  deltek_i:
    name: deltek_i
    description: Deltakingar aktøren er del av.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: cv:participates
    owner: Aktor
    domain_of:
    - Aktor
    range: Deltagelse
    multivalued: true
class_uri: foaf:Agent

```
</details>