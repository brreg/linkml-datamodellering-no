

# Class: Bruksenhetsnummer 


_Identifikator for ei brukseining innanfor ein bygning, t.d. H0201 = 2. etasje, eining 1 (etasjeplan + etasjenummer + nummerering)._





URI: [ngre:Bruksenhetsnummer](https://data.norge.no/vocabulary/ngr-eiendom#Bruksenhetsnummer)





```mermaid
 classDiagram
    class Bruksenhetsnummer
    click Bruksenhetsnummer href "../Bruksenhetsnummer/"
      Bruksenhetsnummer : etasjenummer
        
      Bruksenhetsnummer : etasjeplan
        
          
    
        
        
        Bruksenhetsnummer --> "1" Etasjeplan : etasjeplan
        click Etasjeplan href "../Etasjeplan/"
    

        
      Bruksenhetsnummer : id
        
      Bruksenhetsnummer : nummerering_i_etasjen
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Bruksenhetsnummer](https://data.norge.no/vocabulary/ngr-eiendom#Bruksenhetsnummer) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [etasjeplan](etasjeplan.md) | 1 <br/> [Etasjeplan](Etasjeplan.md) | Kode for kva del av bygningen brukseininga ligg i (H/U/K/L/M) |
| [etasjenummer](etasjenummer.md) | 1 <br/> [Integer](Integer.md) | Etasjenummer (t |
| [nummerering_i_etasjen](nummerering_i_etasjen.md) | 1 <br/> [Integer](Integer.md) | Løpenummer for brukseininga innanfor etasjen |





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Bruksenhet](Bruksenhet.md) | [har_bruksenhetsnummer](har_bruksenhetsnummer.md) | range | [Bruksenhetsnummer](Bruksenhetsnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Bruksenhetsnummer |
| native | https://data.norge.no/linkml/ngr-eiendom/Bruksenhetsnummer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Bruksenhetsnummer
description: Identifikator for ei brukseining innanfor ein bygning, t.d. H0201 = 2.
  etasje, eining 1 (etasjeplan + etasjenummer + nummerering).
from_schema: https://data.norge.no/linkml/ngr-eiendom
slots:
- id
- etasjeplan
- etasjenummer
- nummerering_i_etasjen
slot_usage:
  etasjeplan:
    name: etasjeplan
    in_subset:
    - Obligatorisk
    required: true
  etasjenummer:
    name: etasjenummer
    in_subset:
    - Obligatorisk
    required: true
  nummerering_i_etasjen:
    name: nummerering_i_etasjen
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngre:Bruksenhetsnummer

```
</details>

### Induced

<details>
```yaml
name: Bruksenhetsnummer
description: Identifikator for ei brukseining innanfor ein bygning, t.d. H0201 = 2.
  etasje, eining 1 (etasjeplan + etasjenummer + nummerering).
from_schema: https://data.norge.no/linkml/ngr-eiendom
slot_usage:
  etasjeplan:
    name: etasjeplan
    in_subset:
    - Obligatorisk
    required: true
  etasjenummer:
    name: etasjenummer
    in_subset:
    - Obligatorisk
    required: true
  nummerering_i_etasjen:
    name: nummerering_i_etasjen
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    identifier: true
    alias: id
    owner: Bruksenhetsnummer
    domain_of:
    - FastEiendom
    - SamletFastEiendom
    - Borettslagsandel
    - Matrikkelenhet
    - Matrikkelnummer
    - Kommunenummer
    - Gaardsnummer
    - Bruksnummer
    - Festenummer
    - Seksjonsnummer
    - Bygning
    - Bygningsnummer
    - Representasjonspunkt
    - YtreInngang
    - Bruksenhet
    - Bruksenhetsnummer
    - Etasje
    - Teig
    - Anleggsprojeksjonsflate
    - Eierforhold
    - Hjemmel
    - Andel
    - Rettighetshaver
    - TinglystHeftelse
    - RettighetForAaBenytteEiendom
    - Borettslag
    - OffisiellAdresse
    - Person
    - Hovedenhet
    - Kommune
    range: uriorcurie
    required: true
  etasjeplan:
    name: etasjeplan
    description: Kode for kva del av bygningen brukseininga ligg i (H/U/K/L/M).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:etasjeplan
    alias: etasjeplan
    owner: Bruksenhetsnummer
    domain_of:
    - Bruksenhetsnummer
    range: Etasjeplan
    required: true
  etasjenummer:
    name: etasjenummer
    description: Etasjenummer (t.d. 2 for 2. etasje).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:etasjenummer
    alias: etasjenummer
    owner: Bruksenhetsnummer
    domain_of:
    - Bruksenhetsnummer
    - Etasje
    range: integer
    required: true
  nummerering_i_etasjen:
    name: nummerering_i_etasjen
    description: Løpenummer for brukseininga innanfor etasjen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:nummereringIEtasjen
    alias: nummerering_i_etasjen
    owner: Bruksenhetsnummer
    domain_of:
    - Bruksenhetsnummer
    range: integer
    required: true
class_uri: ngre:Bruksenhetsnummer

```
</details>