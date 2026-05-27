

# Class: Festenummer 


_Festenummer, aktuelt berre for festegrunn (0..1 i matrikkelnummeret)._





URI: [ngre:Festenummer](https://data.norge.no/vocabulary/ngr-eiendom#Festenummer)





```mermaid
 classDiagram
    class Festenummer
    click Festenummer href "../Festenummer/"
      Festenummer : festenummer_verdi
        
          
    
        
        
        Festenummer --> "1" Integer : festenummer_verdi
        click Integer href "../http://www.w3.org/2001/XMLSchema#integer/"
    

        
      Festenummer : id
        
          
    
        
        
        Festenummer --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Festenummer](https://data.norge.no/vocabulary/ngr-eiendom#Festenummer) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [festenummer_verdi](festenummer_verdi.md) | 1 <br/> [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) | Festenummer (0 |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | [bestar_av_festenummer](bestar_av_festenummer.md) | range | [Festenummer](festenummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Festenummer |
| native | https://data.norge.no/ngr/ngr-eiendom/Festenummer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Festenummer
description: Festenummer, aktuelt berre for festegrunn (0..1 i matrikkelnummeret).
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slots:
- id
- festenummer_verdi
slot_usage:
  festenummer_verdi:
    name: festenummer_verdi
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngre:Festenummer

```
</details>

### Induced

<details>
```yaml
name: Festenummer
description: Festenummer, aktuelt berre for festegrunn (0..1 i matrikkelnummeret).
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_usage:
  festenummer_verdi:
    name: festenummer_verdi
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
    owner: Festenummer
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
  festenummer_verdi:
    name: festenummer_verdi
    description: Festenummer (0..1 – berre for festegrunn).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    slot_uri: ngre:festenummer
    owner: Festenummer
    domain_of:
    - Festenummer
    range: integer
    required: true
class_uri: ngre:Festenummer

```
</details>