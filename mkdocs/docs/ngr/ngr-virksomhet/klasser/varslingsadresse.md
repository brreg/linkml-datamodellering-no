

# Class: Varslingsadresse 


_Offisiell varslingsadresse for verksemda – e-post eller mobilnummer som vert brukt for offisielle meldingar frå offentlege styresmakter._





URI: [ngrv:Varslingsadresse](https://data.norge.no/vocabulary/ngr-virksomhet#Varslingsadresse)





```mermaid
 classDiagram
    class Varslingsadresse
    click Varslingsadresse href "../Varslingsadresse/"
      Varslingsadresse : id
        
          
    
        
        
        Varslingsadresse --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Varslingsadresse : varslingstype
        
          
    
        
        
        Varslingsadresse --> "1" VarslingType : varslingstype
        click VarslingType href "../VarslingType/"
    

        
      Varslingsadresse : varslingsverdi
        
          
    
        
        
        Varslingsadresse --> "1" String : varslingsverdi
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrv:Varslingsadresse](https://data.norge.no/vocabulary/ngr-virksomhet#Varslingsadresse) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [varslingstype](varslingstype.md) | 1 <br/> [VarslingType](varslingtype.md) | Kanaltype for varsling (EPOST eller MOBILTELEFON) |
| [varslingsverdi](varslingsverdi.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Verdien for varslingskanalen (e-postadresse eller mobilnummer) |





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VirksomhetContainer](virksomhetcontainer.md) | [varslingsadresser](varslingsadresser.md) | range | [Varslingsadresse](varslingsadresse.md) |
| [Virksomhet](virksomhet.md) | [har_varslingsadresse](har_varslingsadresse.md) | range | [Varslingsadresse](varslingsadresse.md) |
| [Underenhet](underenhet.md) | [har_varslingsadresse](har_varslingsadresse.md) | range | [Varslingsadresse](varslingsadresse.md) |
| [Hovedenhet](hovedenhet.md) | [har_varslingsadresse](har_varslingsadresse.md) | range | [Varslingsadresse](varslingsadresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:Varslingsadresse |
| native | https://data.norge.no/ngr/ngr-virksomhet/Varslingsadresse |




## Examples
### Example: Varslingsadresse-varsling-1

```yaml
id: ngrv:eksempel/varsling-1
varslingstype: EPOST
varslingsverdi: varsling@eksempel.no

```
### Example: Varslingsadresse-varsling-2

```yaml
id: ngrv:eksempel/varsling-2
varslingstype: EPOST
varslingsverdi: bergen@eksempel.no

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Varslingsadresse
description: Offisiell varslingsadresse for verksemda – e-post eller mobilnummer som
  vert brukt for offisielle meldingar frå offentlege styresmakter.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slots:
- id
- varslingstype
- varslingsverdi
slot_usage:
  varslingstype:
    name: varslingstype
    in_subset:
    - Obligatorisk
    required: true
  varslingsverdi:
    name: varslingsverdi
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngrv:Varslingsadresse

```
</details>

### Induced

<details>
```yaml
name: Varslingsadresse
description: Offisiell varslingsadresse for verksemda – e-post eller mobilnummer som
  vert brukt for offisielle meldingar frå offentlege styresmakter.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slot_usage:
  varslingstype:
    name: varslingstype
    in_subset:
    - Obligatorisk
    required: true
  varslingsverdi:
    name: varslingsverdi
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-virksomhet
    rank: 1000
    identifier: true
    owner: Varslingsadresse
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
  varslingstype:
    name: varslingstype
    description: Kanaltype for varsling (EPOST eller MOBILTELEFON).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ngr/ngr-virksomhet
    rank: 1000
    slot_uri: ngrv:varslingstype
    owner: Varslingsadresse
    domain_of:
    - Varslingsadresse
    range: VarslingType
    required: true
  varslingsverdi:
    name: varslingsverdi
    description: Verdien for varslingskanalen (e-postadresse eller mobilnummer).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ngr/ngr-virksomhet
    rank: 1000
    slot_uri: ngrv:varslingsverdi
    owner: Varslingsadresse
    domain_of:
    - Varslingsadresse
    range: string
    required: true
class_uri: ngrv:Varslingsadresse

```
</details>