

# Class: Organisasjonsform 


_Klassifikasjon av juridisk organisasjonsform (t.d. AS, ENK, BA, NUF). Kodeverk forvalta av Enhetsregisteret._





URI: [ngrv:Organisasjonsform](https://data.norge.no/vocabulary/ngr-virksomhet#Organisasjonsform)





```mermaid
 classDiagram
    class Organisasjonsform
    click Organisasjonsform href "../Organisasjonsform/"
      Organisasjonsform : id
        
      Organisasjonsform : organisasjonsform_beskrivelse
        
      Organisasjonsform : organisasjonsform_kode
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrv:Organisasjonsform](https://data.norge.no/vocabulary/ngr-virksomhet#Organisasjonsform) |


## Eigenskapar







  
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [organisasjonsform_kode](organisasjonsform_kode.md) | 1 <br/> [String](String.md) | Kode for organisasjonsform (t |





  
  

  
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [organisasjonsform_beskrivelse](organisasjonsform_beskrivelse.md) | 0..1 <br/> [String](String.md) | Tekstleg skildring av organisasjonsforma |





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VirksomhetContainer](VirksomhetContainer.md) | [organisasjonsformer](organisasjonsformer.md) | range | [Organisasjonsform](Organisasjonsform.md) |
| [Virksomhet](Virksomhet.md) | [er_klassifisert_som_organisasjonsform](er_klassifisert_som_organisasjonsform.md) | range | [Organisasjonsform](Organisasjonsform.md) |
| [Underenhet](Underenhet.md) | [er_klassifisert_som_organisasjonsform](er_klassifisert_som_organisasjonsform.md) | range | [Organisasjonsform](Organisasjonsform.md) |
| [Hovedenhet](Hovedenhet.md) | [er_klassifisert_som_organisasjonsform](er_klassifisert_som_organisasjonsform.md) | range | [Organisasjonsform](Organisasjonsform.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:Organisasjonsform |
| native | https://data.norge.no/linkml/ngr-virksomhet/Organisasjonsform |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organisasjonsform
description: Klassifikasjon av juridisk organisasjonsform (t.d. AS, ENK, BA, NUF).
  Kodeverk forvalta av Enhetsregisteret.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
slots:
- id
- organisasjonsform_kode
- organisasjonsform_beskrivelse
slot_usage:
  organisasjonsform_kode:
    name: organisasjonsform_kode
    in_subset:
    - Obligatorisk
    required: true
  organisasjonsform_beskrivelse:
    name: organisasjonsform_beskrivelse
    in_subset:
    - Anbefalt
class_uri: ngrv:Organisasjonsform

```
</details>

### Induced

<details>
```yaml
name: Organisasjonsform
description: Klassifikasjon av juridisk organisasjonsform (t.d. AS, ENK, BA, NUF).
  Kodeverk forvalta av Enhetsregisteret.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
slot_usage:
  organisasjonsform_kode:
    name: organisasjonsform_kode
    in_subset:
    - Obligatorisk
    required: true
  organisasjonsform_beskrivelse:
    name: organisasjonsform_beskrivelse
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-virksomhet
    rank: 1000
    identifier: true
    alias: id
    owner: Organisasjonsform
    domain_of:
    - Virksomhet
    - Tilstand
    - Organisasjonsform
    - Naeringskode
    - Sektorkode
    - Kontaktinformasjon
    - Varslingsadresse
    - Aktivitet
    - RolleIVirksomhet
    - Rolleinnehaver
    - Signaturrett
    - Prokura
    - GeografiskAdresse
    - Person
    range: uriorcurie
    required: true
  organisasjonsform_kode:
    name: organisasjonsform_kode
    description: Kode for organisasjonsform (t.d. AS, ENK, BA, NUF).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-virksomhet
    rank: 1000
    slot_uri: ngrv:organisasjonsformKode
    alias: organisasjonsform_kode
    owner: Organisasjonsform
    domain_of:
    - Organisasjonsform
    range: string
    required: true
  organisasjonsform_beskrivelse:
    name: organisasjonsform_beskrivelse
    description: Tekstleg skildring av organisasjonsforma.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/ngr-virksomhet
    rank: 1000
    slot_uri: ngrv:organisasjonsformBeskrivelse
    alias: organisasjonsform_beskrivelse
    owner: Organisasjonsform
    domain_of:
    - Organisasjonsform
    range: string
class_uri: ngrv:Organisasjonsform

```
</details>