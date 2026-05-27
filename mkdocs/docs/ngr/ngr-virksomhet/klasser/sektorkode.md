

# Class: Sektorkode 


_Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer (t.d. offentleg, privat)._





URI: [ngrv:Sektorkode](https://data.norge.no/vocabulary/ngr-virksomhet#Sektorkode)





```mermaid
 classDiagram
    class Sektorkode
    click Sektorkode href "../Sektorkode/"
      Sektorkode : id
        
          
    
        
        
        Sektorkode --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Sektorkode : sektorkode_beskrivelse
        
          
    
        
        
        Sektorkode --> "0..1" String : sektorkode_beskrivelse
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Sektorkode : sektorkode_kode
        
          
    
        
        
        Sektorkode --> "1" String : sektorkode_kode
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrv:Sektorkode](https://data.norge.no/vocabulary/ngr-virksomhet#Sektorkode) |


## Eigenskapar







  
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [sektorkode_kode](sektorkode_kode.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Institusjonell sektorkode (t |





  
  

  
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [sektorkode_beskrivelse](sektorkode_beskrivelse.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg skildring av sektorkoden |





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VirksomhetContainer](virksomhetcontainer.md) | [sektorkoder](sektorkoder.md) | range | [Sektorkode](sektorkode.md) |
| [Hovedenhet](hovedenhet.md) | [er_klassifisert_i_sektorkode](er_klassifisert_i_sektorkode.md) | range | [Sektorkode](sektorkode.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:Sektorkode |
| native | https://data.norge.no/ngr/ngr-virksomhet/Sektorkode |




## Examples
### Example: Sektorkode-sektorkode-2100

```yaml
id: ngrv:eksempel/sektorkode-2100
sektorkode_kode: '2100'
sektorkode_beskrivelse: Private aksjeselskaper mv.

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sektorkode
description: Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer
  (t.d. offentleg, privat).
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slots:
- id
- sektorkode_kode
- sektorkode_beskrivelse
slot_usage:
  sektorkode_kode:
    name: sektorkode_kode
    in_subset:
    - Obligatorisk
    required: true
  sektorkode_beskrivelse:
    name: sektorkode_beskrivelse
    in_subset:
    - Anbefalt
class_uri: ngrv:Sektorkode

```
</details>

### Induced

<details>
```yaml
name: Sektorkode
description: Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer
  (t.d. offentleg, privat).
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slot_usage:
  sektorkode_kode:
    name: sektorkode_kode
    in_subset:
    - Obligatorisk
    required: true
  sektorkode_beskrivelse:
    name: sektorkode_beskrivelse
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-virksomhet
    rank: 1000
    identifier: true
    owner: Sektorkode
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
  sektorkode_kode:
    name: sektorkode_kode
    description: Institusjonell sektorkode (t.d. 1120 for statsforvaltinga).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ngr/ngr-virksomhet
    rank: 1000
    slot_uri: ngrv:sektorkodeKode
    owner: Sektorkode
    domain_of:
    - Sektorkode
    range: string
    required: true
  sektorkode_beskrivelse:
    name: sektorkode_beskrivelse
    description: Tekstleg skildring av sektorkoden.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ngr/ngr-virksomhet
    rank: 1000
    slot_uri: ngrv:sektorkodeBeskrivelse
    owner: Sektorkode
    domain_of:
    - Sektorkode
    range: string
class_uri: ngrv:Sektorkode

```
</details>