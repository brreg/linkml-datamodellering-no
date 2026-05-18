

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
        
          
    
        
        
        AdministrasjonContainer --> "*" Fylke : fylke
        click Fylke href "../Fylke/"
    

        
      AdministrasjonContainer : kjonn
        
          
    
        
        
        AdministrasjonContainer --> "*" Kjonn : kjonn
        click Kjonn href "../Kjonn/"
    

        
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
| [personar](personar.md) | * <br/> [Person](person.md) | Alle personar i containeren |
| [kontaktpersonar](kontaktpersonar.md) | * <br/> [Kontaktperson](kontaktperson.md) | Alle kontaktpersonar i containeren |
| [virksomhetar](virksomhetar.md) | * <br/> [Virksomhet](virksomhet.md) | Alle verksemder i containeren |
| [landkodar](landkodar.md) | * <br/> [Landkode](landkode.md) | Alle landkodar i containeren |
| [kjonn](kjonn.md) | * <br/> [Kjonn](kjonn.md) | Kjønn |
| [fylke](fylke.md) | * <br/> [Fylke](fylke.md) | Fylke |
| [kommunar](kommunar.md) | * <br/> [Kommune](kommune.md) | Alle kommuneverdiar i containeren |
| [spraak](spraak.md) | * <br/> [Spraak](spraak.md) | Alle språkverdiar i containeren |
| [valuta](valuta.md) | * <br/> [Valuta](valuta.md) | Alle valutaverdiar i containeren |
| [personalressursar](personalressursar.md) | * <br/> [Personalressurs](personalressurs.md) | Alle personalressursar i containeren |
| [arbeidsforhold](arbeidsforhold.md) | * <br/> [Arbeidsforhold](arbeidsforhold.md) | Arbeidsforhold ressursen er knytt til |
| [arbeidslokasjoner](arbeidslokasjoner.md) | * <br/> [Arbeidslokasjon](arbeidslokasjon.md) | Alle arbeidslokasjoner i containeren |
| [fastlonn](fastlonn.md) | * <br/> [Fastlonn](fastlonn.md) | Fastlønn for arbeidsforholdet |
| [fasttillegg](fasttillegg.md) | * <br/> [Fasttillegg](fasttillegg.md) | Faste tillegg for arbeidsforholdet |
| [fravaer](fravaer.md) | * <br/> [Fravaer](fravaer.md) | Fråvær knytt til ressursen |
| [fullmakter](fullmakter.md) | * <br/> [Fullmakt](fullmakt.md) | Alle fullmakter i containeren |
| [organisasjonselement](organisasjonselement.md) | * <br/> [Organisasjonselement](organisasjonselement.md) | Organisasjonselement ressursen er knytt til |
| [rollar](rollar.md) | * <br/> [Rolle](rolle.md) | Alle rollar i containeren |
| [variabellonn](variabellonn.md) | * <br/> [Variabellonn](variabellonn.md) | Variabel lønn for arbeidsforholdet |
| [aktivitetar](aktivitetar.md) | * <br/> [Aktivitet](aktivitet.md) | Alle aktivitetar i containeren |
| [anlegg](anlegg.md) | * <br/> [Anlegg](anlegg.md) | Objekt som skal aktiverast eller avskrivast |
| [ansvar](ansvar.md) | * <br/> [Ansvar](ansvar.md) | Ansvarleg for ei utgift eller inntekt |
| [artar](artar.md) | * <br/> [Art](art.md) | Alle artar i containeren |
| [arbeidsforholdstypar](arbeidsforholdstypar.md) | * <br/> [Arbeidsforholdstype](arbeidsforholdstype.md) | Alle arbeidsforholdstypar i containeren |
| [diverse](diverse.md) | * <br/> [Diverse](diverse.md) | Spesifikasjon som ikkje kjem fram i øvrige dimensjonar |
| [formaal](formaal.md) | * <br/> [Formaal](formaal.md) | Formål viser aktivitet og tenesteproduksjon |
| [fravaersgrunnar](fravaersgrunnar.md) | * <br/> [Fravaersgrunn](fravaersgrunn.md) | Alle fråværsgrunnar i containeren |
| [fravaerstypar](fravaerstypar.md) | * <br/> [Fravaerstype](fravaerstype.md) | Alle fråværstypar i containeren |
| [funksjonar](funksjonar.md) | * <br/> [Funksjon](funksjon.md) | Alle funksjonar i containeren |
| [kontrakter](kontrakter.md) | * <br/> [Kontrakt](kontrakt.md) | Alle kontrakter i containeren |
| [lonsartar](lonsartar.md) | * <br/> [Lonsart](lonsart.md) | Alle lønnsartar i containeren |
| [lopenummer](lopenummer.md) | * <br/> [Lopenummer](lopenummer.md) | Løpenummer i ei nummerserie |
| [objekt](objekt.md) | * <br/> [Objekt](objekt.md) | Objekt ressursen er knytt til |
| [organisasjonstypar](organisasjonstypar.md) | * <br/> [Organisasjonstype](organisasjonstype.md) | Alle organisasjonstypar i containeren |
| [personalressurskategoriar](personalressurskategoriar.md) | * <br/> [Personalressurskategori](personalressurskategori.md) | Alle personalressurskategoriar i containeren |
| [prosjekt](prosjekt.md) | * <br/> [Prosjekt](prosjekt.md) | Prosjekt ressursen er knytt til |
| [prosjektartar](prosjektartar.md) | * <br/> [Prosjektart](prosjektart.md) | Alle prosjektartar i containeren |
| [rammer](rammer.md) | * <br/> [Ramme](ramme.md) | Alle rammer i containeren |
| [stillingskoder](stillingskoder.md) | * <br/> [Stillingskode](stillingskode.md) | Alle stillingskoder i containeren |
| [uketimetall](uketimetall.md) | * <br/> [Uketimetall](uketimetall.md) | Alle uketimetallverdiar i containeren |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




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
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slots:
- personar
- kontaktpersonar
- virksomhetar
- landkodar
- kjonn
- fylke
- kommunar
- spraak
- valuta
- personalressursar
- arbeidsforhold
- arbeidslokasjoner
- fastlonn
- fasttillegg
- fravaer
- fullmakter
- organisasjonselement
- rollar
- variabellonn
- aktivitetar
- anlegg
- ansvar
- artar
- arbeidsforholdstypar
- diverse
- formaal
- fravaersgrunnar
- fravaerstypar
- funksjonar
- kontrakter
- lonsartar
- lopenummer
- objekt
- organisasjonstypar
- personalressurskategoriar
- prosjekt
- prosjektartar
- rammer
- stillingskoder
- uketimetall
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
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: AdministrasjonContainer
description: Rotcontainer for FINT Administrasjon-instansar.
from_schema: https://data.norge.no/linkml/fint-administrasjon
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
    description: Alle personar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:personar
    alias: personar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Person
    multivalued: true
    inlined: true
    inlined_as_list: true
  kontaktpersonar:
    name: kontaktpersonar
    description: Alle kontaktpersonar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:kontaktpersonar
    alias: kontaktpersonar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Kontaktperson
    multivalued: true
    inlined: true
    inlined_as_list: true
  virksomhetar:
    name: virksomhetar
    description: Alle verksemder i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:virksomhetar
    alias: virksomhetar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Virksomhet
    multivalued: true
    inlined: true
    inlined_as_list: true
  landkodar:
    name: landkodar
    description: Alle landkodar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:landkodar
    alias: landkodar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Landkode
    multivalued: true
    inlined: true
    inlined_as_list: true
  kjonn:
    name: kjonn
    description: Kjønn.
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:kjonn
    alias: kjonn
    owner: AdministrasjonContainer
    domain_of:
    - Person
    - AdministrasjonContainer
    range: Kjonn
    multivalued: true
    inlined_as_list: true
  fylke:
    name: fylke
    description: Fylke.
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:fylke
    alias: fylke
    owner: AdministrasjonContainer
    domain_of:
    - Kommune
    - AdministrasjonContainer
    range: Fylke
    multivalued: true
    inlined_as_list: true
  kommunar:
    name: kommunar
    description: Alle kommuneverdiar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:kommunar
    alias: kommunar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Kommune
    multivalued: true
    inlined: true
    inlined_as_list: true
  spraak:
    name: spraak
    description: Alle språkverdiar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:spraak
    alias: spraak
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Spraak
    multivalued: true
    inlined: true
    inlined_as_list: true
  valuta:
    name: valuta
    description: Alle valutaverdiar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:valuta
    alias: valuta
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Valuta
    multivalued: true
    inlined: true
    inlined_as_list: true
  personalressursar:
    name: personalressursar
    description: Alle personalressursar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:personalressursar
    alias: personalressursar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Personalressurs
    multivalued: true
    inlined: true
    inlined_as_list: true
  arbeidsforhold:
    name: arbeidsforhold
    description: Arbeidsforhold ressursen er knytt til.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:arbeidsforhold
    alias: arbeidsforhold
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
    inlined_as_list: true
  arbeidslokasjoner:
    name: arbeidslokasjoner
    description: Alle arbeidslokasjoner i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:arbeidslokasjoner
    alias: arbeidslokasjoner
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Arbeidslokasjon
    multivalued: true
    inlined: true
    inlined_as_list: true
  fastlonn:
    name: fastlonn
    description: Fastlønn for arbeidsforholdet.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:fastlonn
    alias: fastlonn
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Fastlonn
    multivalued: true
    inlined_as_list: true
  fasttillegg:
    name: fasttillegg
    description: Faste tillegg for arbeidsforholdet.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:fasttillegg
    alias: fasttillegg
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Fasttillegg
    multivalued: true
    inlined_as_list: true
  fravaer:
    name: fravaer
    description: Fråvær knytt til ressursen.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:fravaer
    alias: fravaer
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Fravaer
    multivalued: true
    inlined_as_list: true
  fullmakter:
    name: fullmakter
    description: Alle fullmakter i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:fullmakter
    alias: fullmakter
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Fullmakt
    multivalued: true
    inlined: true
    inlined_as_list: true
  organisasjonselement:
    name: organisasjonselement
    description: Organisasjonselement ressursen er knytt til.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:organisasjonselement
    alias: organisasjonselement
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Ansvar
    - Fullmakt
    range: Organisasjonselement
    multivalued: true
    inlined_as_list: true
  rollar:
    name: rollar
    description: Alle rollar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:rollar
    alias: rollar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Rolle
    multivalued: true
    inlined: true
    inlined_as_list: true
  variabellonn:
    name: variabellonn
    description: Variabel lønn for arbeidsforholdet.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:variabellonn
    alias: variabellonn
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Arbeidsforhold
    range: Variabellonn
    multivalued: true
    inlined_as_list: true
  aktivitetar:
    name: aktivitetar
    description: Alle aktivitetar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:aktivitetar
    alias: aktivitetar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Aktivitet
    multivalued: true
    inlined: true
    inlined_as_list: true
  anlegg:
    name: anlegg
    description: Objekt som skal aktiverast eller avskrivast.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:anlegg
    alias: anlegg
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Anlegg
    multivalued: true
    inlined_as_list: true
  ansvar:
    name: ansvar
    description: Ansvarleg for ei utgift eller inntekt.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:ansvar
    alias: ansvar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Organisasjonselement
    - Arbeidsforhold
    range: Ansvar
    multivalued: true
    inlined_as_list: true
  artar:
    name: artar
    description: Alle artar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:artar
    alias: artar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Art
    multivalued: true
    inlined: true
    inlined_as_list: true
  arbeidsforholdstypar:
    name: arbeidsforholdstypar
    description: Alle arbeidsforholdstypar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:arbeidsforholdstypar
    alias: arbeidsforholdstypar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Arbeidsforholdstype
    multivalued: true
    inlined: true
    inlined_as_list: true
  diverse:
    name: diverse
    description: Spesifikasjon som ikkje kjem fram i øvrige dimensjonar.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:diverse
    alias: diverse
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Diverse
    multivalued: true
    inlined_as_list: true
  formaal:
    name: formaal
    description: Formål viser aktivitet og tenesteproduksjon.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:formaal
    alias: formaal
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Formaal
    multivalued: true
    inlined_as_list: true
  fravaersgrunnar:
    name: fravaersgrunnar
    description: Alle fråværsgrunnar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:fravaersgrunnar
    alias: fravaersgrunnar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Fravaersgrunn
    multivalued: true
    inlined: true
    inlined_as_list: true
  fravaerstypar:
    name: fravaerstypar
    description: Alle fråværstypar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:fravaerstypar
    alias: fravaerstypar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Fravaerstype
    multivalued: true
    inlined: true
    inlined_as_list: true
  funksjonar:
    name: funksjonar
    description: Alle funksjonar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:funksjonar
    alias: funksjonar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Funksjon
    multivalued: true
    inlined: true
    inlined_as_list: true
  kontrakter:
    name: kontrakter
    description: Alle kontrakter i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:kontrakter
    alias: kontrakter
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Kontrakt
    multivalued: true
    inlined: true
    inlined_as_list: true
  lonsartar:
    name: lonsartar
    description: Alle lønnsartar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:lonsartar
    alias: lonsartar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Lonsart
    multivalued: true
    inlined: true
    inlined_as_list: true
  lopenummer:
    name: lopenummer
    description: Løpenummer i ei nummerserie.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:lopenummer
    alias: lopenummer
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Lopenummer
    multivalued: true
    inlined_as_list: true
  objekt:
    name: objekt
    description: Objekt ressursen er knytt til.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:objekt
    alias: objekt
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Fullmakt
    - Arbeidsforhold
    range: Objekt
    multivalued: true
    inlined_as_list: true
  organisasjonstypar:
    name: organisasjonstypar
    description: Alle organisasjonstypar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:organisasjonstypar
    alias: organisasjonstypar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Organisasjonstype
    multivalued: true
    inlined: true
    inlined_as_list: true
  personalressurskategoriar:
    name: personalressurskategoriar
    description: Alle personalressurskategoriar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:personalressurskategoriar
    alias: personalressurskategoriar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Personalressurskategori
    multivalued: true
    inlined: true
    inlined_as_list: true
  prosjekt:
    name: prosjekt
    description: Prosjekt ressursen er knytt til.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:prosjekt
    alias: prosjekt
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    - Kontostreng
    - Prosjektart
    - Fullmakt
    - Arbeidsforhold
    range: Prosjekt
    multivalued: true
    inlined_as_list: true
  prosjektartar:
    name: prosjektartar
    description: Alle prosjektartar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:prosjektartar
    alias: prosjektartar
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Prosjektart
    multivalued: true
    inlined: true
    inlined_as_list: true
  rammer:
    name: rammer
    description: Alle rammer i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:rammer
    alias: rammer
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Ramme
    multivalued: true
    inlined: true
    inlined_as_list: true
  stillingskoder:
    name: stillingskoder
    description: Alle stillingskoder i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:stillingskoder
    alias: stillingskoder
    owner: AdministrasjonContainer
    domain_of:
    - AdministrasjonContainer
    range: Stillingskode
    multivalued: true
    inlined: true
    inlined_as_list: true
  uketimetall:
    name: uketimetall
    description: Alle uketimetallverdiar i containeren.
    from_schema: https://data.norge.no/linkml/fint-administrasjon
    rank: 1000
    slot_uri: adm:uketimetall
    alias: uketimetall
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