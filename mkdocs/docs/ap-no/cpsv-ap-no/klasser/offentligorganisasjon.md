

# Class: OffentligOrganisasjon 


_Ein offentleg organisasjon som er ansvarleg for ei teneste._





URI: [cv:PublicOrganisation](http://data.europa.eu/m8g/PublicOrganisation)





```mermaid
 classDiagram
    class OffentligOrganisasjon
    click OffentligOrganisasjon href "../OffentligOrganisasjon/"
      Aktor <|-- OffentligOrganisasjon
        click Aktor href "../Aktor/"
      
      OffentligOrganisasjon : adresse_ref
        
          
    
        
        
        OffentligOrganisasjon --> "0..1" Adresse : adresse_ref
        click Adresse href "../Adresse/"
    

        
      OffentligOrganisasjon : dekningsomraade
        
          
    
        
        
        OffentligOrganisasjon --> "1..*" Konsept : dekningsomraade
        click Konsept href "../Konsept/"
    

        
      OffentligOrganisasjon : deltek_i
        
          
    
        
        
        OffentligOrganisasjon --> "*" Deltagelse : deltek_i
        click Deltagelse href "../Deltagelse/"
    

        
      OffentligOrganisasjon : foretrekt_namn
        
          
    
        
        
        OffentligOrganisasjon --> "1..*" LangString : foretrekt_namn
        click LangString href "../LangString/"
    

        
      OffentligOrganisasjon : heimeside
        
          
    
        
        
        OffentligOrganisasjon --> "*" Uri : heimeside
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      OffentligOrganisasjon : id
        
          
    
        
        
        OffentligOrganisasjon --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      OffentligOrganisasjon : identifikator_literal
        
          
    
        
        
        OffentligOrganisasjon --> "1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      OffentligOrganisasjon : tittel
        
          
    
        
        
        OffentligOrganisasjon --> "1..*" LangString : tittel
        click LangString href "../LangString/"
    

        
      OffentligOrganisasjon : type_concept
        
          
    
        
        
        OffentligOrganisasjon --> "0..1" Konsept : type_concept
        click Konsept href "../Konsept/"
    

        
      
```





## Inheritance
* [Aktor](aktor.md)
    * **OffentligOrganisasjon**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [cv:PublicOrganisation](http://data.europa.eu/m8g/PublicOrganisation) |


## Eigenskapar







  
  
    
  

  
  
    
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [foretrekt_namn](foretrekt_namn.md) | 1..* <br/> [LangString](langstring.md) | Føretrekt namn/term for organisasjonen |
| [dekningsomraade](dekningsomraade.md) | 1..* <br/> [Konsept](konsept.md) | Geografisk dekningsområde (dct:spatial) |





  
  

  
  

  
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [type_concept](type_concept.md) | 0..1 <br/> [Konsept](konsept.md) | Type ressurs frå eit kontrollert vokabular (dct:type) |





  
  

  
  

  
  
    
  

  
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [heimeside](heimeside.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Heimeside for ressursen eller organisasjonen (foaf:homepage) |






  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Aktor](aktor.md) |
| [tittel](tittel.md) | 1..* <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) | [Aktor](aktor.md) |
| [identifikator_literal](identifikator_literal.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) | [Aktor](aktor.md) |
| [adresse_ref](adresse_ref.md) | 0..1 <br/> [Adresse](adresse.md) | Postadresse knytt til aktøren | [Aktor](aktor.md) |
| [deltek_i](deltek_i.md) | * <br/> [Deltagelse](deltagelse.md) | Deltakingar aktøren er del av | [Aktor](aktor.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OffentligTjeneste](offentligtjeneste.md) | [har_ansvarleg_styremakt](har_ansvarleg_styremakt.md) | range | [OffentligOrganisasjon](offentligorganisasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:PublicOrganisation |
| native | https://data.norge.no/linkml/cpsv-ap-no/OffentligOrganisasjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OffentligOrganisasjon
description: Ein offentleg organisasjon som er ansvarleg for ei teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
is_a: Aktor
slots:
- foretrekt_namn
- dekningsomraade
- heimeside
- type_concept
slot_usage:
  dekningsomraade:
    name: dekningsomraade
    in_subset:
    - Obligatorisk
    required: true
  foretrekt_namn:
    name: foretrekt_namn
    in_subset:
    - Obligatorisk
    required: true
  type_concept:
    name: type_concept
    in_subset:
    - Anbefalt
  heimeside:
    name: heimeside
    in_subset:
    - Valgfri
  adresse_ref:
    name: adresse_ref
    in_subset:
    - Valgfri
class_uri: cv:PublicOrganisation

```
</details>

### Induced

<details>
```yaml
name: OffentligOrganisasjon
description: Ein offentleg organisasjon som er ansvarleg for ei teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
is_a: Aktor
slot_usage:
  dekningsomraade:
    name: dekningsomraade
    in_subset:
    - Obligatorisk
    required: true
  foretrekt_namn:
    name: foretrekt_namn
    in_subset:
    - Obligatorisk
    required: true
  type_concept:
    name: type_concept
    in_subset:
    - Anbefalt
  heimeside:
    name: heimeside
    in_subset:
    - Valgfri
  adresse_ref:
    name: adresse_ref
    in_subset:
    - Valgfri
attributes:
  foretrekt_namn:
    name: foretrekt_namn
    description: Føretrekt namn/term for organisasjonen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/cpsv-ap-no
    rank: 1000
    slot_uri: skos:prefLabel
    owner: OffentligOrganisasjon
    domain_of:
    - OffentligOrganisasjon
    range: LangString
    required: true
    multivalued: true
  dekningsomraade:
    name: dekningsomraade
    description: Geografisk dekningsområde (dct:spatial).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:spatial
    owner: OffentligOrganisasjon
    domain_of:
    - OffentligTjeneste
    - Tjeneste
    - OffentligOrganisasjon
    - Katalog
    range: Konsept
    required: true
    multivalued: true
  heimeside:
    name: heimeside
    description: Heimeside for ressursen eller organisasjonen (foaf:homepage).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: foaf:homepage
    owner: OffentligOrganisasjon
    domain_of:
    - OffentligTjeneste
    - Tjeneste
    - OffentligOrganisasjon
    - Katalog
    range: uri
    multivalued: true
  type_concept:
    name: type_concept
    description: Type ressurs frå eit kontrollert vokabular (dct:type).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: dct:type
    owner: OffentligOrganisasjon
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
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    owner: OffentligOrganisasjon
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
    owner: OffentligOrganisasjon
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
    owner: OffentligOrganisasjon
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
    owner: OffentligOrganisasjon
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
    owner: OffentligOrganisasjon
    domain_of:
    - Aktor
    range: Deltagelse
    multivalued: true
class_uri: cv:PublicOrganisation

```
</details>