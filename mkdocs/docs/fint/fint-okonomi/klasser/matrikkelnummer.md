

# Class: Matrikkelnummer 


_Eintydleg identifisering av matrikkeleining innanfor kommune._





URI: [fint:Matrikkelnummer](https://schema.fintlabs.no/Matrikkelnummer)





```mermaid
 classDiagram
    class Matrikkelnummer
    click Matrikkelnummer href "../Matrikkelnummer/"
      Matrikkelnummer : adresse
        
          
    
        
        
        Matrikkelnummer --> "0..1" Adresse : adresse
        click Adresse href "../Adresse/"
    

        
      Matrikkelnummer : bruksnummer
        
          
    
        
        
        Matrikkelnummer --> "0..1" String : bruksnummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Matrikkelnummer : festenummer
        
          
    
        
        
        Matrikkelnummer --> "0..1" String : festenummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Matrikkelnummer : gaardsnummer
        
          
    
        
        
        Matrikkelnummer --> "0..1" String : gaardsnummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Matrikkelnummer : kommunenummer
        
          
    
        
        
        Matrikkelnummer --> "0..1" Kommune : kommunenummer
        click Kommune href "../Kommune/"
    

        
      Matrikkelnummer : seksjonsnummer
        
          
    
        
        
        Matrikkelnummer --> "0..1" String : seksjonsnummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Matrikkelnummer](https://schema.fintlabs.no/Matrikkelnummer) |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [adresse](adresse.md) | 0..1 <br/> [Adresse](adresse.md) | Adresse til matrikkeleining |
| [bruksnummer](bruksnummer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Fortløpande nummerering av bruk under gårdsnummer |
| [festenummer](festenummer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [gaardsnummer](gaardsnummer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [seksjonsnummer](seksjonsnummer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [kommunenummer](kommunenummer.md) | 0..1 <br/> [Kommune](kommune.md) | Nummerering av kommunen i høve til SSB si offisielle liste |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Matrikkelnummer |
| native | https://schema.fintlabs.no/:Matrikkelnummer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Matrikkelnummer
description: Eintydleg identifisering av matrikkeleining innanfor kommune.
from_schema: https://data.norge.no/fint/fint-common
slots:
- adresse
- bruksnummer
- festenummer
- gaardsnummer
- seksjonsnummer
- kommunenummer
class_uri: fint:Matrikkelnummer

```
</details>

### Induced

<details>
```yaml
name: Matrikkelnummer
description: Eintydleg identifisering av matrikkeleining innanfor kommune.
from_schema: https://data.norge.no/fint/fint-common
attributes:
  adresse:
    name: adresse
    description: Adresse til matrikkeleining.
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:adresse
    owner: Matrikkelnummer
    domain_of:
    - Matrikkelnummer
    - Faktura
    range: Adresse
    inlined: true
  bruksnummer:
    name: bruksnummer
    description: Fortløpande nummerering av bruk under gårdsnummer.
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:bruksnummer
    owner: Matrikkelnummer
    domain_of:
    - Matrikkelnummer
    range: string
  festenummer:
    name: festenummer
    description: Fortløpande nummerering av festar under gårdsnummer/bruksnummer.
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:festenummer
    owner: Matrikkelnummer
    domain_of:
    - Matrikkelnummer
    range: string
  gaardsnummer:
    name: gaardsnummer
    description: Nummerering av gårdseiging i matrikkelen, unik innanfor kommune.
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:gaardsnummer
    owner: Matrikkelnummer
    domain_of:
    - Matrikkelnummer
    range: string
  seksjonsnummer:
    name: seksjonsnummer
    description: Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer.
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:seksjonsnummer
    owner: Matrikkelnummer
    domain_of:
    - Matrikkelnummer
    range: string
  kommunenummer:
    name: kommunenummer
    description: Nummerering av kommunen i høve til SSB si offisielle liste.
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:kommunenummer
    owner: Matrikkelnummer
    domain_of:
    - Matrikkelnummer
    range: Kommune
class_uri: fint:Matrikkelnummer

```
</details>