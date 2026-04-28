

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
        
          
    
        
        
        Brukartilbakemelding --> "0..1" Kvalitetsdimensjon : er_i_kvalitetsdimensjon
        click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
    

        
      Brukartilbakemelding : er_motivert_av
        
      Brukartilbakemelding : har_maal
        
          
    
        
        
        Brukartilbakemelding --> "0..1" DcatRessurs : har_maal
        click DcatRessurs href "../DcatRessurs/"
    

        
      Brukartilbakemelding : har_merknad
        
      Brukartilbakemelding : har_tekstdel
        
          
    
        
        
        Brukartilbakemelding --> "0..1" Tekstdel : har_tekstdel
        click Tekstdel href "../Tekstdel/"
    

        
      Brukartilbakemelding : id
        
      
```





## Inheritance
* [Kvalitetsmerknad](Kvalitetsmerknad.md)
    * **Brukartilbakemelding**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqv:UserQualityFeedback](http://www.w3.org/ns/dqv#UserQualityFeedback) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | [Kvalitetsmerknad](Kvalitetsmerknad.md) |
| [er_motivert_av](er_motivert_av.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Motivasjonen bak kvalitetsmerknaden (t | [Kvalitetsmerknad](Kvalitetsmerknad.md) |
| [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | 0..1 <br/> [Kvalitetsdimensjon](Kvalitetsdimensjon.md) | Kvalitetsdimensjonen denne merknaden eller standarden gjeld | [Kvalitetsmerknad](Kvalitetsmerknad.md) |
| [har_tekstdel](har_tekstdel.md) | 0..1 <br/> [Tekstdel](Tekstdel.md) | Tekstleg innhald i merknaden | [Kvalitetsmerknad](Kvalitetsmerknad.md) |
| [har_merknad](har_merknad.md) | * <br/> [LangString](LangString.md) | Fritekstmerknad (rdfs:comment) | [Kvalitetsmerknad](Kvalitetsmerknad.md) |
| [har_maal](har_maal.md) | 0..1 <br/> [DcatRessurs](DcatRessurs.md) | Ressursen merknaden gjeld | [Kvalitetsmerknad](Kvalitetsmerknad.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [brukartilbakemeldingar](brukartilbakemeldingar.md) | range | [Brukartilbakemelding](Brukartilbakemelding.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:UserQualityFeedback |
| native | https://data.norge.no/linkml/dqv-ap-no/Brukartilbakemelding |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Brukartilbakemelding
description: Tilbakemelding frå ein brukar om kvaliteten til eit datasett.
from_schema: https://data.norge.no/linkml/dqv-ap-no
is_a: Kvalitetsmerknad
class_uri: dqv:UserQualityFeedback

```
</details>

### Induced

<details>
```yaml
name: Brukartilbakemelding
description: Tilbakemelding frå ein brukar om kvaliteten til eit datasett.
from_schema: https://data.norge.no/linkml/dqv-ap-no
is_a: Kvalitetsmerknad
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Brukartilbakemelding
    domain_of:
    - DcatRessurs
    - Datasett
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    - Motivasjon
    - Spraak
    - Mediatype
    - Begrep
    - Begrepssamling
    range: uriorcurie
    required: true
  er_motivert_av:
    name: er_motivert_av
    description: Motivasjonen bak kvalitetsmerknaden (t.d. oa:assessing).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: oa:motivatedBy
    alias: er_motivert_av
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: uriorcurie
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    description: Kvalitetsdimensjonen denne merknaden eller standarden gjeld.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: dqv:inDimension
    alias: er_i_kvalitetsdimensjon
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    - Standard
    range: Kvalitetsdimensjon
  har_tekstdel:
    name: har_tekstdel
    description: Tekstleg innhald i merknaden.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: oa:hasBody
    alias: har_tekstdel
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: Tekstdel
  har_merknad:
    name: har_merknad
    description: Fritekstmerknad (rdfs:comment).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: rdfs:comment
    alias: har_merknad
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    range: LangString
    multivalued: true
  har_maal:
    name: har_maal
    description: Ressursen merknaden gjeld.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: oa:hasTarget
    alias: har_maal
    owner: Brukartilbakemelding
    domain_of:
    - Kvalitetsmerknad
    range: DcatRessurs
class_uri: dqv:UserQualityFeedback

```
</details>