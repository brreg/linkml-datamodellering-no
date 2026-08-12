

# Class: Brukartilbakemelding 


_Tilbakemelding frå ein brukar om kvaliteten til eit datasett._





URI: [dqv:UserQualityFeedback](http://www.w3.org/ns/dqv#UserQualityFeedback)





```mermaid
 classDiagram
    class Brukartilbakemelding
    click Brukartilbakemelding href "../brukartilbakemelding/"
      Kvalitetsmerknad <|-- Brukartilbakemelding
        click Kvalitetsmerknad href "../kvalitetsmerknad/"
      
      Brukartilbakemelding : er_i_kvalitetsdimensjon
        
          
    
        
        
        Brukartilbakemelding --> "*" Kvalitetsdimensjon : er_i_kvalitetsdimensjon
        click Kvalitetsdimensjon href "../kvalitetsdimensjon/"
    

        
      Brukartilbakemelding : er_motivert_av
        
          
    
        
        
        Brukartilbakemelding --> "1" DqvMotivasjon : er_motivert_av
        click DqvMotivasjon href "../dqvmotivasjon/"
    

        
      Brukartilbakemelding : har_maal
        
          
    
        
        
        Brukartilbakemelding --> "0..1" Uriorcurie : har_maal
        click Uriorcurie href "../uriorcurie/"
    

        
      Brukartilbakemelding : har_merknad
        
          
    
        
        
        Brukartilbakemelding --> "*" LangString : har_merknad
        click LangString href "../langstring/"
    

        
      Brukartilbakemelding : har_tekstdel
        
          
    
        
        
        Brukartilbakemelding --> "*" Tekstdel : har_tekstdel
        click Tekstdel href "../tekstdel/"
    

        
      Brukartilbakemelding : id
        
          
    
        
        
        Brukartilbakemelding --> "1" Uriorcurie : id
        click Uriorcurie href "../uriorcurie/"
    

        
      
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
| --- | --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen. | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [er_motivert_av](er_motivert_av.md) | 1 <br/> [DqvMotivasjon](dqvmotivasjon.md) | Motivasjonen bak kvalitetsmerknaden. | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | * <br/> [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld. | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_tekstdel](har_tekstdel.md) | * <br/> [Tekstdel](tekstdel.md) | Tekstleg innhald i merknaden (0..n). | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_merknad](har_merknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad (rdfs:comment). | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_maal](har_maal.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Datasett, distribusjon eller datatjeneste merknaden gjeld. | [Kvalitetsmerknad](kvalitetsmerknad.md) |











## In Subsets


* [Metadata](metadata.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:UserQualityFeedback |
| native | https://data.norge.no/ap-no/dqv-core/Brukartilbakemelding |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Brukartilbakemelding
description: Tilbakemelding frå ein brukar om kvaliteten til eit datasett.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
is_a: Kvalitetsmerknad
class_uri: dqv:UserQualityFeedback

```
</details>

### Induced

<details>
```yaml
name: Brukartilbakemelding
description: Tilbakemelding frå ein brukar om kvaliteten til eit datasett.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
is_a: Kvalitetsmerknad
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Brukartilbakemelding
    domain_of:
    - Lisensdokument
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
  er_motivert_av:
    name: er_motivert_av
    description: Motivasjonen bak kvalitetsmerknaden.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: oa:motivatedBy
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: DqvMotivasjon
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    description: Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: dqv:inDimension
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: Kvalitetsdimensjon
    required: false
    multivalued: true
  har_tekstdel:
    name: har_tekstdel
    description: Tekstleg innhald i merknaden (0..n).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: oa:hasBody
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: Tekstdel
    multivalued: true
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
    description: Datasett, distribusjon eller datatjeneste merknaden gjeld.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: oa:hasTarget
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: uriorcurie
class_uri: dqv:UserQualityFeedback

```
</details>