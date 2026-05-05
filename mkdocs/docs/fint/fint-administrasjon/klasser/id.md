

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://schema.fintlabs.no/administrasjon/:id](https://schema.fintlabs.no/administrasjon/:id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Stillingskode](stillingskode.md) | Felles kodeverk for stillingar |  no  |
| [Lonsart](lonsart.md) | Type ytelse |  no  |
| [Personalressurskategori](personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |  no  |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |
| [Fravaerstype](fravaerstype.md) | Type fråvær |  no  |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |
| [Funksjon](funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |  no  |
| [Fravaersgrunn](fravaersgrunn.md) | Grunn til fråvær |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Lopenummer](lopenummer.md) | Løpenummer i ei nummerserie |  no  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  no  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [Objekt](objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |  no  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Rolle](rolle.md) | Rettighet eller type fullmakt |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Diverse](diverse.md) | Del av kontostrengen; supplement til øvrige dimensjonar |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Arbeidsforholdstype](arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Aktivitet](aktivitet.md) | Del av kontostrengen og detaljering av funksjon |  no  |
| [Kontrakt](kontrakt.md) | Kontrakt transaksjonen er knytt til |  no  |
| [Anlegg](anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |  no  |
| [Formaal](formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |  no  |
| [Prosjekt](prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |  no  |
| [Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Organisasjonstype](organisasjonstype.md) | Typen til eit organisasjonselement |  no  |
| [Ramme](ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Uketimetall](uketimetall.md) | Timer per veke i 100 % stilling |  no  |
| [Art](art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Lonn](lonn.md), [Fravaer](fravaer.md), [Fullmakt](fullmakt.md), [Rolle](rolle.md), [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md), [Personalressurs](personalressurs.md), [Arbeidsforhold](arbeidsforhold.md), [Begrep](begrep.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md), [Virksomhet](virksomhet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:id |
| native | https://schema.fintlabs.no/administrasjon/:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
identifier: true
alias: id
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

```
</details>