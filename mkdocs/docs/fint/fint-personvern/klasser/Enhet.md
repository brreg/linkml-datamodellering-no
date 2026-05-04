

# Class: Enhet 


_Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd identifisert med organisasjonsnummer._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [fint:Enhet](https://schema.fintlabs.no/Enhet)





```mermaid
 classDiagram
    class Enhet
    click Enhet href "../Enhet/"
      Aktoer <|-- Enhet
        click Aktoer href "../Aktoer/"
      

      Enhet <|-- Virksomhet
        click Virksomhet href "../Virksomhet/"
      

      Enhet : forretningsadresse
        
          
    
        
        
        Enhet --> "0..1" Adresse : forretningsadresse
        click Adresse href "../Adresse/"
    

        
      Enhet : kontaktinformasjon
        
          
    
        
        
        Enhet --> "0..1" Kontaktinformasjon : kontaktinformasjon
        click Kontaktinformasjon href "../Kontaktinformasjon/"
    

        
      Enhet : organisasjonsnavn
        
      Enhet : organisasjonsnummer
        
          
    
        
        
        Enhet --> "0..1" Identifikator : organisasjonsnummer
        click Identifikator href "../Identifikator/"
    

        
      Enhet : postadresse
        
          
    
        
        
        Enhet --> "0..1" Adresse : postadresse
        click Adresse href "../Adresse/"
    

        
      
```





## Inheritance
* [Aktoer](Aktoer.md)
    * **Enhet**
        * [Virksomhet](Virksomhet.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Enhet](https://schema.fintlabs.no/Enhet) |


## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [forretningsadresse](forretningsadresse.md) | 0..1 <br/> [Adresse](Adresse.md) | Besøksadresse til ein organisasjonseining i einingsregisteret |
| [organisasjonsnavn](organisasjonsnavn.md) | 0..1 <br/> [String](String.md) | Namn på eining registrert i Einingsregisteret |
| [organisasjonsnummer](organisasjonsnummer.md) | 0..1 <br/> [Identifikator](Identifikator.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [kontaktinformasjon](kontaktinformasjon.md) | 0..1 <br/> [Kontaktinformasjon](Kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør | [Aktoer](Aktoer.md) |
| [postadresse](postadresse.md) | 0..1 <br/> [Adresse](Adresse.md) | Informasjon om postadresse til ein aktør | [Aktoer](Aktoer.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Enhet |
| native | https://schema.fintlabs.no/personvern/:Enhet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Enhet
description: Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd
  identifisert med organisasjonsnummer.
from_schema: https://data.norge.no/linkml/fint-personvern
is_a: Aktoer
abstract: true
attributes:
  forretningsadresse:
    name: forretningsadresse
    description: Besøksadresse til ein organisasjonseining i einingsregisteret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:forretningsadresse
    domain_of:
    - Enhet
    range: Adresse
    inlined: true
  organisasjonsnavn:
    name: organisasjonsnavn
    description: Namn på eining registrert i Einingsregisteret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:organisasjonsnavn
    domain_of:
    - Enhet
    range: string
  organisasjonsnummer:
    name: organisasjonsnummer
    description: Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:organisasjonsnummer
    domain_of:
    - Enhet
    range: Identifikator
    inlined: true
class_uri: fint:Enhet

```
</details>

### Induced

<details>
```yaml
name: Enhet
description: Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd
  identifisert med organisasjonsnummer.
from_schema: https://data.norge.no/linkml/fint-personvern
is_a: Aktoer
abstract: true
attributes:
  forretningsadresse:
    name: forretningsadresse
    description: Besøksadresse til ein organisasjonseining i einingsregisteret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:forretningsadresse
    alias: forretningsadresse
    owner: Enhet
    domain_of:
    - Enhet
    range: Adresse
    inlined: true
  organisasjonsnavn:
    name: organisasjonsnavn
    description: Namn på eining registrert i Einingsregisteret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:organisasjonsnavn
    alias: organisasjonsnavn
    owner: Enhet
    domain_of:
    - Enhet
    range: string
  organisasjonsnummer:
    name: organisasjonsnummer
    description: Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:organisasjonsnummer
    alias: organisasjonsnummer
    owner: Enhet
    domain_of:
    - Enhet
    range: Identifikator
    inlined: true
  kontaktinformasjon:
    name: kontaktinformasjon
    description: Den føretrekte måten å kome i kontakt med ein aktør.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:kontaktinformasjon
    alias: kontaktinformasjon
    owner: Enhet
    domain_of:
    - Aktoer
    - Kontaktperson
    range: Kontaktinformasjon
    inlined: true
  postadresse:
    name: postadresse
    description: Informasjon om postadresse til ein aktør.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:postadresse
    alias: postadresse
    owner: Enhet
    domain_of:
    - Aktoer
    range: Adresse
    inlined: true
class_uri: fint:Enhet

```
</details>