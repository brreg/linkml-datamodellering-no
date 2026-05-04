

# Class: Virksomhet 


_Ein juridisk organisasjon som produserer varer eller tenester._





URI: [fint:Virksomhet](https://schema.fintlabs.no/Virksomhet)





```mermaid
 classDiagram
    class Virksomhet
    click Virksomhet href "../Virksomhet/"
      Enhet <|-- Virksomhet
        click Enhet href "../Enhet/"
      
      Virksomhet : forretningsadresse
        
          
    
        
        
        Virksomhet --> "0..1" Adresse : forretningsadresse
        click Adresse href "../Adresse/"
    

        
      Virksomhet : id
        
      Virksomhet : kontaktinformasjon
        
          
    
        
        
        Virksomhet --> "0..1" Kontaktinformasjon : kontaktinformasjon
        click Kontaktinformasjon href "../Kontaktinformasjon/"
    

        
      Virksomhet : laerling
        
      Virksomhet : organisasjonsnavn
        
      Virksomhet : organisasjonsnummer
        
          
    
        
        
        Virksomhet --> "0..1" Identifikator : organisasjonsnummer
        click Identifikator href "../Identifikator/"
    

        
      Virksomhet : postadresse
        
          
    
        
        
        Virksomhet --> "0..1" Adresse : postadresse
        click Adresse href "../Adresse/"
    

        
      Virksomhet : virksomhetsId
        
          
    
        
        
        Virksomhet --> "1" Identifikator : virksomhetsId
        click Identifikator href "../Identifikator/"
    

        
      
```





## Inheritance
* [Aktoer](Aktoer.md)
    * [Enhet](Enhet.md)
        * **Virksomhet**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Virksomhet](https://schema.fintlabs.no/Virksomhet) |


## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator (tilsvarar systemId i FINT) |
| [virksomhetsId](virksomhetsId.md) | 1 <br/> [Identifikator](Identifikator.md) | Intern unik identifikator i økonomisystemet |
| [laerling](laerling.md) | * <br/> [Uriorcurie](Uriorcurie.md) | Referanse til Laerling (Utdanning) i verksemda |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [forretningsadresse](forretningsadresse.md) | 0..1 <br/> [Adresse](Adresse.md) | Besøksadresse til ein organisasjonseining i einingsregisteret | [Enhet](Enhet.md) |
| [organisasjonsnavn](organisasjonsnavn.md) | 0..1 <br/> [String](String.md) | Namn på eining registrert i Einingsregisteret | [Enhet](Enhet.md) |
| [organisasjonsnummer](organisasjonsnummer.md) | 0..1 <br/> [Identifikator](Identifikator.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret | [Enhet](Enhet.md) |
| [kontaktinformasjon](kontaktinformasjon.md) | 0..1 <br/> [Kontaktinformasjon](Kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør | [Aktoer](Aktoer.md) |
| [postadresse](postadresse.md) | 0..1 <br/> [Adresse](Adresse.md) | Informasjon om postadresse til ein aktør | [Aktoer](Aktoer.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Virksomhet |
| native | https://schema.fintlabs.no/ressurs/:Virksomhet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Virksomhet
description: Ein juridisk organisasjon som produserer varer eller tenester.
from_schema: https://data.norge.no/linkml/fint-ressurs
is_a: Enhet
slots:
- id
attributes:
  virksomhetsId:
    name: virksomhetsId
    description: Intern unik identifikator i økonomisystemet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:virksomhetsId
    domain_of:
    - Virksomhet
    range: Identifikator
    required: true
    inlined: true
  laerling:
    name: laerling
    description: Referanse til Laerling (Utdanning) i verksemda.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:laerling
    domain_of:
    - Person
    - Virksomhet
    range: uriorcurie
    multivalued: true
class_uri: fint:Virksomhet

```
</details>

### Induced

<details>
```yaml
name: Virksomhet
description: Ein juridisk organisasjon som produserer varer eller tenester.
from_schema: https://data.norge.no/linkml/fint-ressurs
is_a: Enhet
attributes:
  virksomhetsId:
    name: virksomhetsId
    description: Intern unik identifikator i økonomisystemet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:virksomhetsId
    alias: virksomhetsId
    owner: Virksomhet
    domain_of:
    - Virksomhet
    range: Identifikator
    required: true
    inlined: true
  laerling:
    name: laerling
    description: Referanse til Laerling (Utdanning) i verksemda.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:laerling
    alias: laerling
    owner: Virksomhet
    domain_of:
    - Person
    - Virksomhet
    range: uriorcurie
    multivalued: true
  id:
    name: id
    description: URI-identifikator (tilsvarar systemId i FINT).
    from_schema: https://data.norge.no/linkml/fint-ressurs
    rank: 1000
    identifier: true
    alias: id
    owner: Virksomhet
    domain_of:
    - Applikasjon
    - Applikasjonsressurs
    - Applikasjonsressurstilgjengelighet
    - DigitalEnhet
    - Enhetsgruppe
    - Enhetsgruppemedlemskap
    - Identitet
    - Rettighet
    - Applikasjonskategori
    - Brukertype
    - Enhetstype
    - Handhevingstype
    - Lisensmodell
    - Plattform
    - Produsent
    - Status
    - Begrep
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    range: uriorcurie
    required: true
  forretningsadresse:
    name: forretningsadresse
    description: Besøksadresse til ein organisasjonseining i einingsregisteret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:forretningsadresse
    alias: forretningsadresse
    owner: Virksomhet
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
    owner: Virksomhet
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
    owner: Virksomhet
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
    owner: Virksomhet
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
    owner: Virksomhet
    domain_of:
    - Aktoer
    range: Adresse
    inlined: true
class_uri: fint:Virksomhet

```
</details>