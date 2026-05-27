

# Class: Kommunenummer 


_Firesifra kommunenummer (t.d. 0301 for Oslo)._





URI: [ngre:Kommunenummer](https://data.norge.no/vocabulary/ngr-eiendom#Kommunenummer)





```mermaid
 classDiagram
    class Kommunenummer
    click Kommunenummer href "../Kommunenummer/"
      Kommunenummer : id
        
          
    
        
        
        Kommunenummer --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Kommunenummer : kommunenummer_verdi
        
          
    
        
        
        Kommunenummer --> "1" String : kommunenummer_verdi
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Kommunenummer](https://data.norge.no/vocabulary/ngr-eiendom#Kommunenummer) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kommunenummer_verdi](kommunenummer_verdi.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Firesifra kommunenummer (t |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | [bestar_av_kommunenummer](bestar_av_kommunenummer.md) | range | [Kommunenummer](kommunenummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Kommunenummer |
| native | https://data.norge.no/ngr/ngr-eiendom/Kommunenummer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kommunenummer
description: Firesifra kommunenummer (t.d. 0301 for Oslo).
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slots:
- id
- kommunenummer_verdi
slot_usage:
  kommunenummer_verdi:
    name: kommunenummer_verdi
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngre:Kommunenummer

```
</details>

### Induced

<details>
```yaml
name: Kommunenummer
description: Firesifra kommunenummer (t.d. 0301 for Oslo).
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_usage:
  kommunenummer_verdi:
    name: kommunenummer_verdi
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    identifier: true
    owner: Kommunenummer
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
  kommunenummer_verdi:
    name: kommunenummer_verdi
    description: Firesifra kommunenummer (t.d. 0301 for Oslo).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    slot_uri: ngre:kommunenummer
    owner: Kommunenummer
    domain_of:
    - Kommunenummer
    - Kommune
    range: string
    required: true
class_uri: ngre:Kommunenummer

```
</details>