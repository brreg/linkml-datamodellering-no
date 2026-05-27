

# Class: Brukartilbakemelding 


_Tilbakemelding frå ein brukar om kvaliteten til eit datasett._





URI: [dqv:UserQualityFeedback](http://www.w3.org/ns/dqv#UserQualityFeedback)





```mermaid
 classDiagram
    class Brukartilbakemelding
    click Brukartilbakemelding href "../Brukartilbakemelding/"
      Kvalitetsmerknad <|-- Brukartilbakemelding
        click Kvalitetsmerknad href "../Kvalitetsmerknad/"
      
      Brukartilbakemelding : er_i_kvalitetsdimensjon
        
          
    
        
        
        Brukartilbakemelding --> "*" Kvalitetsdimensjon : er_i_kvalitetsdimensjon
        click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
    

        
      Brukartilbakemelding : er_motivert_av
        
          
    
        
        
        Brukartilbakemelding --> "1" Uriorcurie : er_motivert_av
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Brukartilbakemelding : har_maal
        
          
    
        
        
        Brukartilbakemelding --> "0..1" Uri : har_maal
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Brukartilbakemelding : har_merknad
        
          
    
        
        
        Brukartilbakemelding --> "*" LangString : har_merknad
        click LangString href "../LangString/"
    

        
      Brukartilbakemelding : har_tekstdel
        
          
    
        
        
        Brukartilbakemelding --> "0..1" Tekstdel : har_tekstdel
        click Tekstdel href "../Tekstdel/"
    

        
      Brukartilbakemelding : id
        
          
    
        
        
        Brukartilbakemelding --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* [Kvalitetsmerknad](kvalitetsmerknad.md)
    * **Brukartilbakemelding**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqv:UserQualityFeedback](http://www.w3.org/ns/dqv#UserQualityFeedback) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [er_motivert_av](er_motivert_av.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Motivasjonen bak kvalitetsmerknaden (t | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | * <br/> [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_tekstdel](har_tekstdel.md) | 0..1 <br/> [Tekstdel](tekstdel.md) | Tekstleg innhald i merknaden | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_merknad](har_merknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad (rdfs:comment) | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_maal](har_maal.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Ressursen merknaden gjeld | [Kvalitetsmerknad](kvalitetsmerknad.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:UserQualityFeedback |
| native | https://data.norge.no/ap-no/dqv-ap-no/Brukartilbakemelding |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Brukartilbakemelding
description: Tilbakemelding frå ein brukar om kvaliteten til eit datasett.
from_schema: https://data.norge.no/ap-no/dqv-ap-no
rank: 1000
is_a: Kvalitetsmerknad
class_uri: dqv:UserQualityFeedback

```
</details>

### Induced

<details>
```yaml
name: Brukartilbakemelding
description: Tilbakemelding frå ein brukar om kvaliteten til eit datasett.
from_schema: https://data.norge.no/ap-no/dqv-ap-no
rank: 1000
is_a: Kvalitetsmerknad
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Brukartilbakemelding
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    range: uriorcurie
    required: true
  er_motivert_av:
    name: er_motivert_av
    description: Motivasjonen bak kvalitetsmerknaden (t.d. oa:assessing).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dqv-ap-no
    rank: 1000
    slot_uri: oa:motivatedBy
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: uriorcurie
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    description: 'Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld.

      '
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-ap-no
    rank: 1000
    slot_uri: dqv:inDimension
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    - Standard
    range: Kvalitetsdimensjon
    required: false
    multivalued: true
  har_tekstdel:
    name: har_tekstdel
    description: Tekstleg innhald i merknaden.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-ap-no
    rank: 1000
    slot_uri: oa:hasBody
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: Tekstdel
  har_merknad:
    name: har_merknad
    description: Fritekstmerknad (rdfs:comment).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: rdfs:comment
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    range: LangString
    multivalued: true
  har_maal:
    name: har_maal
    annotations:
      gyldige_verdier:
        tag: gyldige_verdier
        value: dcat:Resource
    description: Ressursen merknaden gjeld.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dqv-ap-no
    rank: 1000
    slot_uri: oa:hasTarget
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: uri
class_uri: dqv:UserQualityFeedback

```
</details>