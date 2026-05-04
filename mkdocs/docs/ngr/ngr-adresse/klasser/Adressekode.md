

# Class: Adressekode 


_Firesifra kommunal kode som identifiserer eit adressenavn._





URI: [ngr:Adressekode](https://data.norge.no/vocabulary/ngr-adresse#Adressekode)





```mermaid
 classDiagram
    class Adressekode
    click Adressekode href "../Adressekode/"
      Adressekode : adresseomrade_ref
        
          
    
        
        
        Adressekode --> "0..1" Adresseomrade : adresseomrade_ref
        click Adresseomrade href "../Adresseomrade/"
    

        
      Adressekode : id
        
      Adressekode : kode
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:Adressekode](https://data.norge.no/vocabulary/ngr-adresse#Adressekode) |


## Eigenskapar







  
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kode](kode.md) | 1 <br/> [Integer](Integer.md) | Numerisk kode for adressekoden (kommunal firesifra kode) |





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |
| [adresseomrade_ref](adresseomrade_ref.md) | 0..1 <br/> [Adresseomrade](Adresseomrade.md) | Adresseområdet dette adressenamnet eller adressekoden høyrer til |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | [adressekoder](adressekoder.md) | range | [Adressekode](Adressekode.md) |
| [OffisiellAdresse](OffisiellAdresse.md) | [adressekode_ref](adressekode_ref.md) | range | [Adressekode](Adressekode.md) |
| [Adressenavn](Adressenavn.md) | [har_adressekode](har_adressekode.md) | range | [Adressekode](Adressekode.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:Adressekode |
| native | https://data.norge.no/linkml/ngr-adresse/Adressekode |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Adressekode
description: Firesifra kommunal kode som identifiserer eit adressenavn.
from_schema: https://data.norge.no/linkml/ngr-adresse
slots:
- id
- kode
- adresseomrade_ref
slot_usage:
  kode:
    name: kode
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngr:Adressekode

```
</details>

### Induced

<details>
```yaml
name: Adressekode
description: Firesifra kommunal kode som identifiserer eit adressenavn.
from_schema: https://data.norge.no/linkml/ngr-adresse
slot_usage:
  kode:
    name: kode
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    identifier: true
    alias: id
    owner: Adressekode
    domain_of:
    - GeografiskAdresse
    - Adressenavn
    - Adresseomrade
    - Adressekode
    - Husnummer
    - Bruksenhetsnummer
    - Representasjonspunkt
    - GeografiskOmrade
    - Postboks
    - Bygning
    - Bruksenhet
    range: uriorcurie
    required: true
  kode:
    name: kode
    description: Numerisk kode for adressekoden (kommunal firesifra kode).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    slot_uri: ngr:kode
    alias: kode
    owner: Adressekode
    domain_of:
    - Adressekode
    range: integer
    required: true
  adresseomrade_ref:
    name: adresseomrade_ref
    description: Adresseområdet dette adressenamnet eller adressekoden høyrer til.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    slot_uri: ngr:harAdresseomrade
    alias: adresseomrade_ref
    owner: Adressekode
    domain_of:
    - Adressenavn
    - Adressekode
    range: Adresseomrade
class_uri: ngr:Adressekode

```
</details>