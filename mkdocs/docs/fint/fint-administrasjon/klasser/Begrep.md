

# Class: Begrep 


_Abstrakt fellesbase for alle FINT-kodeverk._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [fint:Begrep](https://schema.fintlabs.no/Begrep)





```mermaid
 classDiagram
    class Begrep
    click Begrep href "../Begrep/"
      Begrep <|-- Aktivitet
        click Aktivitet href "../Aktivitet/"
      Begrep <|-- Anlegg
        click Anlegg href "../Anlegg/"
      Begrep <|-- Ansvar
        click Ansvar href "../Ansvar/"
      Begrep <|-- Art
        click Art href "../Art/"
      Begrep <|-- Arbeidsforholdstype
        click Arbeidsforholdstype href "../Arbeidsforholdstype/"
      Begrep <|-- Diverse
        click Diverse href "../Diverse/"
      Begrep <|-- Formaal
        click Formaal href "../Formaal/"
      Begrep <|-- Fravaersgrunn
        click Fravaersgrunn href "../Fravaersgrunn/"
      Begrep <|-- Fravaerstype
        click Fravaerstype href "../Fravaerstype/"
      Begrep <|-- Funksjon
        click Funksjon href "../Funksjon/"
      Begrep <|-- Kontrakt
        click Kontrakt href "../Kontrakt/"
      Begrep <|-- Lonsart
        click Lonsart href "../Lonsart/"
      Begrep <|-- Lopenummer
        click Lopenummer href "../Lopenummer/"
      Begrep <|-- Objekt
        click Objekt href "../Objekt/"
      Begrep <|-- Organisasjonstype
        click Organisasjonstype href "../Organisasjonstype/"
      Begrep <|-- Personalressurskategori
        click Personalressurskategori href "../Personalressurskategori/"
      Begrep <|-- Prosjekt
        click Prosjekt href "../Prosjekt/"
      Begrep <|-- Prosjektart
        click Prosjektart href "../Prosjektart/"
      Begrep <|-- Ramme
        click Ramme href "../Ramme/"
      Begrep <|-- Stillingskode
        click Stillingskode href "../Stillingskode/"
      Begrep <|-- Uketimetall
        click Uketimetall href "../Uketimetall/"
      Begrep <|-- Landkode
        click Landkode href "../Landkode/"
      Begrep <|-- Kjonn
        click Kjonn href "../Kjonn/"
      Begrep <|-- Fylke
        click Fylke href "../Fylke/"
      Begrep <|-- Kommune
        click Kommune href "../Kommune/"
      Begrep <|-- Spraak
        click Spraak href "../Spraak/"
      
      Begrep : gyldighetsperiode
        
          
    
        
        
        Begrep --> "0..1" Periode : gyldighetsperiode
        click Periode href "../Periode/"
    

        
      Begrep : id
        
      Begrep : kode
        
      Begrep : navn
        
      Begrep : passiv
        
      
```





## Inheritance
* **Begrep**
    * [Aktivitet](Aktivitet.md)
    * [Anlegg](Anlegg.md)
    * [Ansvar](Ansvar.md)
    * [Art](Art.md)
    * [Arbeidsforholdstype](Arbeidsforholdstype.md)
    * [Diverse](Diverse.md)
    * [Formaal](Formaal.md)
    * [Fravaersgrunn](Fravaersgrunn.md)
    * [Fravaerstype](Fravaerstype.md)
    * [Funksjon](Funksjon.md)
    * [Kontrakt](Kontrakt.md)
    * [Lonsart](Lonsart.md)
    * [Lopenummer](Lopenummer.md)
    * [Objekt](Objekt.md)
    * [Organisasjonstype](Organisasjonstype.md)
    * [Personalressurskategori](Personalressurskategori.md)
    * [Prosjekt](Prosjekt.md)
    * [Prosjektart](Prosjektart.md)
    * [Ramme](Ramme.md)
    * [Stillingskode](Stillingskode.md)
    * [Uketimetall](Uketimetall.md)
    * [Landkode](Landkode.md)
    * [Kjonn](Kjonn.md)
    * [Fylke](Fylke.md)
    * [Kommune](Kommune.md)
    * [Spraak](Spraak.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Begrep](https://schema.fintlabs.no/Begrep) |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |
| [kode](kode.md) | 1 <br/> [String](String.md) | Verdi som identifiserer omgrepet |
| [navn](navn.md) | 1 <br/> [String](String.md) | Hovudnamn for omgrepet |
| [gyldighetsperiode](gyldighetsperiode.md) | 0..1 <br/> [Periode](Periode.md) | Angir gyldighetsperioden for eit omgrep/kode |
| [passiv](passiv.md) | 0..1 <br/> [Boolean](Boolean.md) | Angir at koden er passiv og ikkje kan veljast |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Begrep |
| native | https://schema.fintlabs.no/administrasjon/:Begrep |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Begrep
description: Abstrakt fellesbase for alle FINT-kodeverk.
from_schema: https://data.norge.no/linkml/fint-administrasjon
abstract: true
slots:
- id
attributes:
  kode:
    name: kode
    description: Verdi som identifiserer omgrepet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:kode
    domain_of:
    - Begrep
    range: string
    required: true
  navn:
    name: navn
    description: Hovudnamn for omgrepet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:navn
    domain_of:
    - Organisasjonselement
    - Begrep
    - Valuta
    - Person
    - Kontaktperson
    range: string
    required: true
  gyldighetsperiode:
    name: gyldighetsperiode
    description: Angir gyldighetsperioden for eit omgrep/kode.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:gyldighetsperiode
    domain_of:
    - Fullmakt
    - Organisasjonselement
    - Arbeidsforhold
    - Begrep
    - Identifikator
    range: Periode
    inlined: true
  passiv:
    name: passiv
    description: Angir at koden er passiv og ikkje kan veljast.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:passiv
    domain_of:
    - Begrep
    range: boolean
class_uri: fint:Begrep

```
</details>

### Induced

<details>
```yaml
name: Begrep
description: Abstrakt fellesbase for alle FINT-kodeverk.
from_schema: https://data.norge.no/linkml/fint-administrasjon
abstract: true
attributes:
  kode:
    name: kode
    description: Verdi som identifiserer omgrepet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:kode
    alias: kode
    owner: Begrep
    domain_of:
    - Begrep
    range: string
    required: true
  navn:
    name: navn
    description: Hovudnamn for omgrepet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:navn
    alias: navn
    owner: Begrep
    domain_of:
    - Organisasjonselement
    - Begrep
    - Valuta
    - Person
    - Kontaktperson
    range: string
    required: true
  gyldighetsperiode:
    name: gyldighetsperiode
    description: Angir gyldighetsperioden for eit omgrep/kode.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:gyldighetsperiode
    alias: gyldighetsperiode
    owner: Begrep
    domain_of:
    - Fullmakt
    - Organisasjonselement
    - Arbeidsforhold
    - Begrep
    - Identifikator
    range: Periode
    inlined: true
  passiv:
    name: passiv
    description: Angir at koden er passiv og ikkje kan veljast.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:passiv
    alias: passiv
    owner: Begrep
    domain_of:
    - Begrep
    range: boolean
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    identifier: true
    alias: id
    owner: Begrep
    domain_of:
    - Lonn
    - Fravaer
    - Fullmakt
    - Rolle
    - Arbeidslokasjon
    - Organisasjonselement
    - Personalressurs
    - Arbeidsforhold
    - Begrep
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    range: uriorcurie
    required: true
class_uri: fint:Begrep

```
</details>