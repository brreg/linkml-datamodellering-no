

# Class: AdministrasjonContainer 


_Rotcontainer for FINT Administrasjon-instansar._





URI: [https://schema.fintlabs.no/administrasjon/:AdministrasjonContainer](https://schema.fintlabs.no/administrasjon/:AdministrasjonContainer)





```mermaid
 classDiagram
    class AdministrasjonContainer
    click AdministrasjonContainer href "../AdministrasjonContainer/"
      AdministrasjonContainer : aktivitetar
        
          
    
        
        
        AdministrasjonContainer --> "*" Aktivitet : aktivitetar
        click Aktivitet href "../Aktivitet/"
    

        
      AdministrasjonContainer : anlegg
        
          
    
        
        
        AdministrasjonContainer --> "*" Anlegg : anlegg
        click Anlegg href "../Anlegg/"
    

        
      AdministrasjonContainer : ansvar
        
          
    
        
        
        AdministrasjonContainer --> "*" Ansvar : ansvar
        click Ansvar href "../Ansvar/"
    

        
      AdministrasjonContainer : arbeidsforhold
        
          
    
        
        
        AdministrasjonContainer --> "*" Arbeidsforhold : arbeidsforhold
        click Arbeidsforhold href "../Arbeidsforhold/"
    

        
      AdministrasjonContainer : arbeidsforholdstypar
        
          
    
        
        
        AdministrasjonContainer --> "*" Arbeidsforholdstype : arbeidsforholdstypar
        click Arbeidsforholdstype href "../Arbeidsforholdstype/"
    

        
      AdministrasjonContainer : arbeidslokasjoner
        
          
    
        
        
        AdministrasjonContainer --> "*" Arbeidslokasjon : arbeidslokasjoner
        click Arbeidslokasjon href "../Arbeidslokasjon/"
    

        
      AdministrasjonContainer : artar
        
          
    
        
        
        AdministrasjonContainer --> "*" Art : artar
        click Art href "../Art/"
    

        
      AdministrasjonContainer : diverse
        
          
    
        
        
        AdministrasjonContainer --> "*" Diverse : diverse
        click Diverse href "../Diverse/"
    

        
      AdministrasjonContainer : fastlonn
        
          
    
        
        
        AdministrasjonContainer --> "*" Fastlonn : fastlonn
        click Fastlonn href "../Fastlonn/"
    

        
      AdministrasjonContainer : fasttillegg
        
          
    
        
        
        AdministrasjonContainer --> "*" Fasttillegg : fasttillegg
        click Fasttillegg href "../Fasttillegg/"
    

        
      AdministrasjonContainer : formaal
        
          
    
        
        
        AdministrasjonContainer --> "*" Formaal : formaal
        click Formaal href "../Formaal/"
    

        
      AdministrasjonContainer : fravaer
        
          
    
        
        
        AdministrasjonContainer --> "*" Fravaer : fravaer
        click Fravaer href "../Fravaer/"
    

        
      AdministrasjonContainer : fravaersgrunnar
        
          
    
        
        
        AdministrasjonContainer --> "*" Fravaersgrunn : fravaersgrunnar
        click Fravaersgrunn href "../Fravaersgrunn/"
    

        
      AdministrasjonContainer : fravaerstypar
        
          
    
        
        
        AdministrasjonContainer --> "*" Fravaerstype : fravaerstypar
        click Fravaerstype href "../Fravaerstype/"
    

        
      AdministrasjonContainer : fullmakter
        
          
    
        
        
        AdministrasjonContainer --> "*" Fullmakt : fullmakter
        click Fullmakt href "../Fullmakt/"
    

        
      AdministrasjonContainer : funksjonar
        
          
    
        
        
        AdministrasjonContainer --> "*" Funksjon : funksjonar
        click Funksjon href "../Funksjon/"
    

        
      AdministrasjonContainer : fylke
        
          
    
        
        
        AdministrasjonContainer --> "*" String : fylke
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      AdministrasjonContainer : kjonn
        
          
    
        
        
        AdministrasjonContainer --> "*" String : kjonn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      AdministrasjonContainer : kommunar
        
          
    
        
        
        AdministrasjonContainer --> "*" Kommune : kommunar
        click Kommune href "../Kommune/"
    

        
      AdministrasjonContainer : kontaktpersonar
        
          
    
        
        
        AdministrasjonContainer --> "*" Kontaktperson : kontaktpersonar
        click Kontaktperson href "../Kontaktperson/"
    

        
      AdministrasjonContainer : kontrakter
        
          
    
        
        
        AdministrasjonContainer --> "*" Kontrakt : kontrakter
        click Kontrakt href "../Kontrakt/"
    

        
      AdministrasjonContainer : landkodar
        
          
    
        
        
        AdministrasjonContainer --> "*" Landkode : landkodar
        click Landkode href "../Landkode/"
    

        
      AdministrasjonContainer : lonsartar
        
          
    
        
        
        AdministrasjonContainer --> "*" Lonsart : lonsartar
        click Lonsart href "../Lonsart/"
    

        
      AdministrasjonContainer : lopenummer
        
          
    
        
        
        AdministrasjonContainer --> "*" Lopenummer : lopenummer
        click Lopenummer href "../Lopenummer/"
    

        
      AdministrasjonContainer : objekt
        
          
    
        
        
        AdministrasjonContainer --> "*" Objekt : objekt
        click Objekt href "../Objekt/"
    

        
      AdministrasjonContainer : organisasjonselement
        
          
    
        
        
        AdministrasjonContainer --> "*" Organisasjonselement : organisasjonselement
        click Organisasjonselement href "../Organisasjonselement/"
    

        
      AdministrasjonContainer : organisasjonstypar
        
          
    
        
        
        AdministrasjonContainer --> "*" Organisasjonstype : organisasjonstypar
        click Organisasjonstype href "../Organisasjonstype/"
    

        
      AdministrasjonContainer : personalressursar
        
          
    
        
        
        AdministrasjonContainer --> "*" Personalressurs : personalressursar
        click Personalressurs href "../Personalressurs/"
    

        
      AdministrasjonContainer : personalressurskategoriar
        
          
    
        
        
        AdministrasjonContainer --> "*" Personalressurskategori : personalressurskategoriar
        click Personalressurskategori href "../Personalressurskategori/"
    

        
      AdministrasjonContainer : personar
        
          
    
        
        
        AdministrasjonContainer --> "*" Person : personar
        click Person href "../Person/"
    

        
      AdministrasjonContainer : prosjekt
        
          
    
        
        
        AdministrasjonContainer --> "*" Prosjekt : prosjekt
        click Prosjekt href "../Prosjekt/"
    

        
      AdministrasjonContainer : prosjektartar
        
          
    
        
        
        AdministrasjonContainer --> "*" Prosjektart : prosjektartar
        click Prosjektart href "../Prosjektart/"
    

        
      AdministrasjonContainer : rammer
        
          
    
        
        
        AdministrasjonContainer --> "*" Ramme : rammer
        click Ramme href "../Ramme/"
    

        
      AdministrasjonContainer : rollar
        
          
    
        
        
        AdministrasjonContainer --> "*" Rolle : rollar
        click Rolle href "../Rolle/"
    

        
      AdministrasjonContainer : spraak
        
          
    
        
        
        AdministrasjonContainer --> "*" Spraak : spraak
        click Spraak href "../Spraak/"
    

        
      AdministrasjonContainer : stillingskoder
        
          
    
        
        
        AdministrasjonContainer --> "*" Stillingskode : stillingskoder
        click Stillingskode href "../Stillingskode/"
    

        
      AdministrasjonContainer : uketimetall
        
          
    
        
        
        AdministrasjonContainer --> "*" Uketimetall : uketimetall
        click Uketimetall href "../Uketimetall/"
    

        
      AdministrasjonContainer : valuta
        
          
    
        
        
        AdministrasjonContainer --> "*" Valuta : valuta
        click Valuta href "../Valuta/"
    

        
      AdministrasjonContainer : variabellonn
        
          
    
        
        
        AdministrasjonContainer --> "*" Variabellonn : variabellonn
        click Variabellonn href "../Variabellonn/"
    

        
      AdministrasjonContainer : virksomhetar
        
          
    
        
        
        AdministrasjonContainer --> "*" Virksomhet : virksomhetar
        click Virksomhet href "../Virksomhet/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Tree Root | Yes |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [personar](personar.md) | * <br/> [Person](person.md) |  |
| [kontaktpersonar](kontaktpersonar.md) | * <br/> [Kontaktperson](kontaktperson.md) |  |
| [virksomhetar](virksomhetar.md) | * <br/> [Virksomhet](virksomhet.md) |  |
| [landkodar](landkodar.md) | * <br/> [Landkode](landkode.md) |  |
| [kjonn](kjonn.md) | * <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) |  |
| [fylke](fylke.md) | * <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) |  |
| [kommunar](kommunar.md) | * <br/> [Kommune](kommune.md) |  |
| [spraak](spraak.md) | * <br/> [Spraak](spraak.md) |  |
| [valuta](valuta.md) | * <br/> [Valuta](valuta.md) |  |
| [personalressursar](personalressursar.md) | * <br/> [Personalressurs](personalressurs.md) |  |
| [arbeidsforhold](arbeidsforhold.md) | * <br/> [Arbeidsforhold](arbeidsforhold.md) |  |
| [arbeidslokasjoner](arbeidslokasjoner.md) | * <br/> [Arbeidslokasjon](arbeidslokasjon.md) |  |
| [fastlonn](fastlonn.md) | * <br/> [Fastlonn](fastlonn.md) |  |
| [fasttillegg](fasttillegg.md) | * <br/> [Fasttillegg](fasttillegg.md) |  |
| [fravaer](fravaer.md) | * <br/> [Fravaer](fravaer.md) |  |
| [fullmakter](fullmakter.md) | * <br/> [Fullmakt](fullmakt.md) |  |
| [organisasjonselement](organisasjonselement.md) | * <br/> [Organisasjonselement](organisasjonselement.md) |  |
| [rollar](rollar.md) | * <br/> [Rolle](rolle.md) |  |
| [variabellonn](variabellonn.md) | * <br/> [Variabellonn](variabellonn.md) |  |
| [aktivitetar](aktivitetar.md) | * <br/> [Aktivitet](aktivitet.md) |  |
| [anlegg](anlegg.md) | * <br/> [Anlegg](anlegg.md) |  |
| [ansvar](ansvar.md) | * <br/> [Ansvar](ansvar.md) |  |
| [artar](artar.md) | * <br/> [Art](art.md) |  |
| [arbeidsforholdstypar](arbeidsforholdstypar.md) | * <br/> [Arbeidsforholdstype](arbeidsforholdstype.md) |  |
| [diverse](diverse.md) | * <br/> [Diverse](diverse.md) |  |
| [formaal](formaal.md) | * <br/> [Formaal](formaal.md) |  |
| [fravaersgrunnar](fravaersgrunnar.md) | * <br/> [Fravaersgrunn](fravaersgrunn.md) |  |
| [fravaerstypar](fravaerstypar.md) | * <br/> [Fravaerstype](fravaerstype.md) |  |
| [funksjonar](funksjonar.md) | * <br/> [Funksjon](funksjon.md) |  |
| [kontrakter](kontrakter.md) | * <br/> [Kontrakt](kontrakt.md) |  |
| [lonsartar](lonsartar.md) | * <br/> [Lonsart](lonsart.md) |  |
| [lopenummer](lopenummer.md) | * <br/> [Lopenummer](lopenummer.md) |  |
| [objekt](objekt.md) | * <br/> [Objekt](objekt.md) |  |
| [organisasjonstypar](organisasjonstypar.md) | * <br/> [Organisasjonstype](organisasjonstype.md) |  |
| [personalressurskategoriar](personalressurskategoriar.md) | * <br/> [Personalressurskategori](personalressurskategori.md) |  |
| [prosjekt](prosjekt.md) | * <br/> [Prosjekt](prosjekt.md) |  |
| [prosjektartar](prosjektartar.md) | * <br/> [Prosjektart](prosjektart.md) |  |
| [rammer](rammer.md) | * <br/> [Ramme](ramme.md) |  |
| [stillingskoder](stillingskoder.md) | * <br/> [Stillingskode](stillingskode.md) |  |
| [uketimetall](uketimetall.md) | * <br/> [Uketimetall](uketimetall.md) |  |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:AdministrasjonContainer |
| native | https://schema.fintlabs.no/administrasjon/:AdministrasjonContainer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AdministrasjonContainer
description: Rotcontainer for FINT Administrasjon-instansar.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_usage:
  arbeidsforhold:
    name: arbeidsforhold
    multivalued: true
    inlined_as_list: true
  fastlonn:
    name: fastlonn
    multivalued: true
    inlined_as_list: true
  fasttillegg:
    name: fasttillegg
    multivalued: true
    inlined_as_list: true
  fravaer:
    name: fravaer
    multivalued: true
    inlined_as_list: true
  organisasjonselement:
    name: organisasjonselement
    multivalued: true
    inlined_as_list: true
  variabellonn:
    name: variabellonn
    multivalued: true
    inlined_as_list: true
  anlegg:
    name: anlegg
    multivalued: true
    inlined_as_list: true
  ansvar:
    name: ansvar
    multivalued: true
    inlined_as_list: true
  diverse:
    name: diverse
    multivalued: true
    inlined_as_list: true
  formaal:
    name: formaal
    multivalued: true
    inlined_as_list: true
  lopenummer:
    name: lopenummer
    multivalued: true
    inlined_as_list: true
  objekt:
    name: objekt
    multivalued: true
    inlined_as_list: true
  prosjekt:
    name: prosjekt
    multivalued: true
    inlined_as_list: true
  kjonn:
    name: kjonn
    multivalued: true
    inlined_as_list: true
  fylke:
    name: fylke
    multivalued: true
    inlined_as_list: true
attributes:
  personar:
    name: personar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Person
    multivalued: true
    inlined_as_list: true
  kontaktpersonar:
    name: kontaktpersonar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Kontaktperson
    multivalued: true
    inlined_as_list: true
  virksomhetar:
    name: virksomhetar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Virksomhet
    multivalued: true
    inlined_as_list: true
  landkodar:
    name: landkodar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Landkode
    multivalued: true
    inlined_as_list: true
  kjonn:
    name: kjonn
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - Person
    - AdministrasjonContainer
  fylke:
    name: fylke
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - Kommune
    - AdministrasjonContainer
  kommunar:
    name: kommunar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Kommune
    multivalued: true
    inlined_as_list: true
  spraak:
    name: spraak
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Spraak
    multivalued: true
    inlined_as_list: true
  valuta:
    name: valuta
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Valuta
    multivalued: true
    inlined_as_list: true
  personalressursar:
    name: personalressursar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Personalressurs
    multivalued: true
    inlined_as_list: true
  arbeidsforhold:
    name: arbeidsforhold
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Fastlonn
    - Fasttillegg
    - Variabellonn
    - Fravaer
    - Arbeidslokasjon
    - Organisasjonselement
    - Personalressurs
    range: Arbeidsforhold
  arbeidslokasjoner:
    name: arbeidslokasjoner
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Arbeidslokasjon
    multivalued: true
    inlined_as_list: true
  fastlonn:
    name: fastlonn
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Fastlonn
  fasttillegg:
    name: fasttillegg
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Fasttillegg
  fravaer:
    name: fravaer
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Fravaer
  fullmakter:
    name: fullmakter
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Fullmakt
    multivalued: true
    inlined_as_list: true
  organisasjonselement:
    name: organisasjonselement
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Ansvar
    - Fullmakt
    range: Organisasjonselement
  rollar:
    name: rollar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Rolle
    multivalued: true
    inlined_as_list: true
  variabellonn:
    name: variabellonn
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Variabellonn
  aktivitetar:
    name: aktivitetar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Aktivitet
    multivalued: true
    inlined_as_list: true
  anlegg:
    name: anlegg
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Anlegg
  ansvar:
    name: ansvar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Organisasjonselement
    - Arbeidsforhold
    range: Ansvar
  artar:
    name: artar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Art
    multivalued: true
    inlined_as_list: true
  arbeidsforholdstypar:
    name: arbeidsforholdstypar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Arbeidsforholdstype
    multivalued: true
    inlined_as_list: true
  diverse:
    name: diverse
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Diverse
  formaal:
    name: formaal
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Formaal
  fravaersgrunnar:
    name: fravaersgrunnar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Fravaersgrunn
    multivalued: true
    inlined_as_list: true
  fravaerstypar:
    name: fravaerstypar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Fravaerstype
    multivalued: true
    inlined_as_list: true
  funksjonar:
    name: funksjonar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Funksjon
    multivalued: true
    inlined_as_list: true
  kontrakter:
    name: kontrakter
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Kontrakt
    multivalued: true
    inlined_as_list: true
  lonsartar:
    name: lonsartar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Lonsart
    multivalued: true
    inlined_as_list: true
  lopenummer:
    name: lopenummer
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Lopenummer
  objekt:
    name: objekt
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Objekt
  organisasjonstypar:
    name: organisasjonstypar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Organisasjonstype
    multivalued: true
    inlined_as_list: true
  personalressurskategoriar:
    name: personalressurskategoriar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Personalressurskategori
    multivalued: true
    inlined_as_list: true
  prosjekt:
    name: prosjekt
    from_schema: https://data.norge.no/fint/fint-administrasjon
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Prosjektart
    - Fullmakt
    - Arbeidsforhold
    range: Prosjekt
  prosjektartar:
    name: prosjektartar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Prosjektart
    multivalued: true
    inlined_as_list: true
  rammer:
    name: rammer
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Ramme
    multivalued: true
    inlined_as_list: true
  stillingskoder:
    name: stillingskoder
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Stillingskode
    multivalued: true
    inlined_as_list: true
  uketimetall:
    name: uketimetall
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    domain_of:
    - AdministrasjonContainer
    range: Uketimetall
    multivalued: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: AdministrasjonContainer
description: Rotcontainer for FINT Administrasjon-instansar.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_usage:
  arbeidsforhold:
    name: arbeidsforhold
    multivalued: true
    inlined_as_list: true
  fastlonn:
    name: fastlonn
    multivalued: true
    inlined_as_list: true
  fasttillegg:
    name: fasttillegg
    multivalued: true
    inlined_as_list: true
  fravaer:
    name: fravaer
    multivalued: true
    inlined_as_list: true
  organisasjonselement:
    name: organisasjonselement
    multivalued: true
    inlined_as_list: true
  variabellonn:
    name: variabellonn
    multivalued: true
    inlined_as_list: true
  anlegg:
    name: anlegg
    multivalued: true
    inlined_as_list: true
  ansvar:
    name: ansvar
    multivalued: true
    inlined_as_list: true
  diverse:
    name: diverse
    multivalued: true
    inlined_as_list: true
  formaal:
    name: formaal
    multivalued: true
    inlined_as_list: true
  lopenummer:
    name: lopenummer
    multivalued: true
    inlined_as_list: true
  objekt:
    name: objekt
    multivalued: true
    inlined_as_list: true
  prosjekt:
    name: prosjekt
    multivalued: true
    inlined_as_list: true
  kjonn:
    name: kjonn
    multivalued: true
    inlined_as_list: true
  fylke:
    name: fylke
    multivalued: true
    inlined_as_list: true
attributes:
  personar:
    name: personar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Person
    multivalued: true
    inlined: true
    inlined_as_list: true
  kontaktpersonar:
    name: kontaktpersonar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Kontaktperson
    multivalued: true
    inlined: true
    inlined_as_list: true
  virksomhetar:
    name: virksomhetar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Virksomhet
    multivalued: true
    inlined: true
    inlined_as_list: true
  landkodar:
    name: landkodar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Landkode
    multivalued: true
    inlined: true
    inlined_as_list: true
  kjonn:
    name: kjonn
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - Person
    - AdministrasjonContainer
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  fylke:
    name: fylke
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - Kommune
    - AdministrasjonContainer
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  kommunar:
    name: kommunar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Kommune
    multivalued: true
    inlined: true
    inlined_as_list: true
  spraak:
    name: spraak
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Spraak
    multivalued: true
    inlined: true
    inlined_as_list: true
  valuta:
    name: valuta
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Valuta
    multivalued: true
    inlined: true
    inlined_as_list: true
  personalressursar:
    name: personalressursar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Personalressurs
    multivalued: true
    inlined: true
    inlined_as_list: true
  arbeidsforhold:
    name: arbeidsforhold
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Fastlonn
    - Fasttillegg
    - Variabellonn
    - Fravaer
    - Arbeidslokasjon
    - Organisasjonselement
    - Personalressurs
    range: Arbeidsforhold
    multivalued: true
    inlined: true
    inlined_as_list: true
  arbeidslokasjoner:
    name: arbeidslokasjoner
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Arbeidslokasjon
    multivalued: true
    inlined: true
    inlined_as_list: true
  fastlonn:
    name: fastlonn
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Fastlonn
    multivalued: true
    inlined: true
    inlined_as_list: true
  fasttillegg:
    name: fasttillegg
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Fasttillegg
    multivalued: true
    inlined: true
    inlined_as_list: true
  fravaer:
    name: fravaer
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Fravaer
    multivalued: true
    inlined: true
    inlined_as_list: true
  fullmakter:
    name: fullmakter
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Fullmakt
    multivalued: true
    inlined: true
    inlined_as_list: true
  organisasjonselement:
    name: organisasjonselement
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Ansvar
    - Fullmakt
    range: Organisasjonselement
    multivalued: true
    inlined: true
    inlined_as_list: true
  rollar:
    name: rollar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Rolle
    multivalued: true
    inlined: true
    inlined_as_list: true
  variabellonn:
    name: variabellonn
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Variabellonn
    multivalued: true
    inlined: true
    inlined_as_list: true
  aktivitetar:
    name: aktivitetar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Aktivitet
    multivalued: true
    inlined: true
    inlined_as_list: true
  anlegg:
    name: anlegg
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Anlegg
    multivalued: true
    inlined: true
    inlined_as_list: true
  ansvar:
    name: ansvar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Organisasjonselement
    - Arbeidsforhold
    range: Ansvar
    multivalued: true
    inlined: true
    inlined_as_list: true
  artar:
    name: artar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Art
    multivalued: true
    inlined: true
    inlined_as_list: true
  arbeidsforholdstypar:
    name: arbeidsforholdstypar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Arbeidsforholdstype
    multivalued: true
    inlined: true
    inlined_as_list: true
  diverse:
    name: diverse
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Diverse
    multivalued: true
    inlined: true
    inlined_as_list: true
  formaal:
    name: formaal
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Formaal
    multivalued: true
    inlined: true
    inlined_as_list: true
  fravaersgrunnar:
    name: fravaersgrunnar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Fravaersgrunn
    multivalued: true
    inlined: true
    inlined_as_list: true
  fravaerstypar:
    name: fravaerstypar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Fravaerstype
    multivalued: true
    inlined: true
    inlined_as_list: true
  funksjonar:
    name: funksjonar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Funksjon
    multivalued: true
    inlined: true
    inlined_as_list: true
  kontrakter:
    name: kontrakter
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Kontrakt
    multivalued: true
    inlined: true
    inlined_as_list: true
  lonsartar:
    name: lonsartar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Lonsart
    multivalued: true
    inlined: true
    inlined_as_list: true
  lopenummer:
    name: lopenummer
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Lopenummer
    multivalued: true
    inlined: true
    inlined_as_list: true
  objekt:
    name: objekt
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Objekt
    multivalued: true
    inlined: true
    inlined_as_list: true
  organisasjonstypar:
    name: organisasjonstypar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Organisasjonstype
    multivalued: true
    inlined: true
    inlined_as_list: true
  personalressurskategoriar:
    name: personalressurskategoriar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Personalressurskategori
    multivalued: true
    inlined: true
    inlined_as_list: true
  prosjekt:
    name: prosjekt
    from_schema: https://data.norge.no/fint/fint-administrasjon
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Prosjektart
    - Fullmakt
    - Arbeidsforhold
    range: Prosjekt
    multivalued: true
    inlined: true
    inlined_as_list: true
  prosjektartar:
    name: prosjektartar
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Prosjektart
    multivalued: true
    inlined: true
    inlined_as_list: true
  rammer:
    name: rammer
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Ramme
    multivalued: true
    inlined: true
    inlined_as_list: true
  stillingskoder:
    name: stillingskoder
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Stillingskode
    multivalued: true
    inlined: true
    inlined_as_list: true
  uketimetall:
    name: uketimetall
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Uketimetall
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>