

# Class: Gaardsnummer 


_Gårdsnummer innanfor kommunen._





URI: [ngre:Gaardsnummer](https://data.norge.no/vocabulary/ngr-eiendom#Gaardsnummer)





```mermaid
 classDiagram
    class Gaardsnummer
    click Gaardsnummer href "../Gaardsnummer/"
      Gaardsnummer : gaardsnummer_verdi
        
          
    
        
        
        Gaardsnummer --> "1" Integer : gaardsnummer_verdi
        click Integer href "../http://www.w3.org/2001/XMLSchema#integer/"
    

        
      Gaardsnummer : id
        
          
    
        
        
        Gaardsnummer --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Gaardsnummer](https://data.norge.no/vocabulary/ngr-eiendom#Gaardsnummer) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [gaardsnummer_verdi](gaardsnummer_verdi.md) | 1 <br/> [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) | Gårdsnummer innanfor kommunen |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | [bestar_av_gaardsnummer](bestar_av_gaardsnummer.md) | range | [Gaardsnummer](gaardsnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Gaardsnummer |
| native | https://data.norge.no/linkml/ngr-eiendom/Gaardsnummer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gaardsnummer
description: Gårdsnummer innanfor kommunen.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slots:
- id
- gaardsnummer_verdi
slot_usage:
  gaardsnummer_verdi:
    name: gaardsnummer_verdi
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngre:Gaardsnummer

```
</details>

### Induced

<details>
```yaml
name: Gaardsnummer
description: Gårdsnummer innanfor kommunen.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_usage:
  gaardsnummer_verdi:
    name: gaardsnummer_verdi
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
    owner: Gaardsnummer
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
  gaardsnummer_verdi:
    name: gaardsnummer_verdi
    description: Gårdsnummer innanfor kommunen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:gaardsnummer
    alias: gaardsnummer_verdi
    owner: Gaardsnummer
    domain_of:
    - Gaardsnummer
    range: integer
    required: true
class_uri: ngre:Gaardsnummer

```
</details>