

# Class: Kvalitetssertifikat 


_Eit sertifikat som stadfester kvaliteten til eit datasett._





URI: [dqv:QualityCertificate](http://www.w3.org/ns/dqv#QualityCertificate)





```mermaid
 classDiagram
    class Kvalitetssertifikat
    click Kvalitetssertifikat href "../Kvalitetssertifikat/"
      Kvalitetsmerknad <|-- Kvalitetssertifikat
        click Kvalitetsmerknad href "../Kvalitetsmerknad/"
      
      Kvalitetssertifikat : er_i_kvalitetsdimensjon
        
          
    
        
        
        Kvalitetssertifikat --> "0..1" Kvalitetsdimensjon : er_i_kvalitetsdimensjon
        click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
    

        
      Kvalitetssertifikat : er_motivert_av
        
      Kvalitetssertifikat : har_maal
        
          
    
        
        
        Kvalitetssertifikat --> "0..1" DcatRessurs : har_maal
        click DcatRessurs href "../DcatRessurs/"
    

        
      Kvalitetssertifikat : har_merknad
        
      Kvalitetssertifikat : har_tekstdel
        
          
    
        
        
        Kvalitetssertifikat --> "0..1" Tekstdel : har_tekstdel
        click Tekstdel href "../Tekstdel/"
    

        
      Kvalitetssertifikat : id
        
      
```





## Inheritance
* [Kvalitetsmerknad](kvalitetsmerknad.md)
    * **Kvalitetssertifikat**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqv:QualityCertificate](http://www.w3.org/ns/dqv#QualityCertificate) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [er_motivert_av](er_motivert_av.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | Motivasjonen bak kvalitetsmerknaden (t | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | 0..1 <br/> [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Kvalitetsdimensjonen denne merknaden eller standarden gjeld | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_tekstdel](har_tekstdel.md) | 0..1 <br/> [Tekstdel](tekstdel.md) | Tekstleg innhald i merknaden | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_merknad](har_merknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad (rdfs:comment) | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_maal](har_maal.md) | 0..1 <br/> [DcatRessurs](dcatressurs.md) | Ressursen merknaden gjeld | [Kvalitetsmerknad](kvalitetsmerknad.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:QualityCertificate |
| native | https://data.norge.no/linkml/dqv-ap-no/Kvalitetssertifikat |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetssertifikat
description: Eit sertifikat som stadfester kvaliteten til eit datasett.
from_schema: https://data.norge.no/linkml/dqv-ap-no
is_a: Kvalitetsmerknad
class_uri: dqv:QualityCertificate

```
</details>

### Induced

<details>
```yaml
name: Kvalitetssertifikat
description: Eit sertifikat som stadfester kvaliteten til eit datasett.
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
    owner: Kvalitetssertifikat
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
    - Konsept
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
    owner: Kvalitetssertifikat
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
    owner: Kvalitetssertifikat
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
    owner: Kvalitetssertifikat
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
    owner: Kvalitetssertifikat
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
    owner: Kvalitetssertifikat
    domain_of:
    - Kvalitetsmerknad
    range: DcatRessurs
class_uri: dqv:QualityCertificate

```
</details>