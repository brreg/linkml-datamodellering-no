

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://schema.fintlabs.no/administrasjon/:id](https://schema.fintlabs.no/administrasjon/:id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Arbeidslokasjon](Arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |
| [Personalressurskategori](Personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |  no  |
| [Fravaersgrunn](Fravaersgrunn.md) | Grunn til fråvær |  no  |
| [Ramme](Ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |  no  |
| [Ansvar](Ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  no  |
| [Lonn](Lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Objekt](Objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |  no  |
| [Variabellonn](Variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Formaal](Formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |  no  |
| [Fravaer](Fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |
| [Stillingskode](Stillingskode.md) | Felles kodeverk for stillingar |  no  |
| [Fasttillegg](Fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Fullmakt](Fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Rolle](Rolle.md) | Rettighet eller type fullmakt |  no  |
| [Anlegg](Anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |  no  |
| [Organisasjonselement](Organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Personalressurs](Personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Art](Art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Aktivitet](Aktivitet.md) | Del av kontostrengen og detaljering av funksjon |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Prosjektart](Prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [Fastlonn](Fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Arbeidsforholdstype](Arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |  no  |
| [Lopenummer](Lopenummer.md) | Løpenummer i ei nummerserie |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Uketimetall](Uketimetall.md) | Timer per veke i 100 % stilling |  no  |
| [Fravaerstype](Fravaerstype.md) | Type fråvær |  no  |
| [Funksjon](Funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |  no  |
| [Organisasjonstype](Organisasjonstype.md) | Typen til eit organisasjonselement |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Lonsart](Lonsart.md) | Type ytelse |  no  |
| [Prosjekt](Prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |  no  |
| [Diverse](Diverse.md) | Del av kontostrengen; supplement til øvrige dimensjonar |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Kontrakt](Kontrakt.md) | Kontrakt transaksjonen er knytt til |  no  |
| [Valuta](Valuta.md) | Valutakodar for offisielle valutaer |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Lonn](Lonn.md), [Fravaer](Fravaer.md), [Fullmakt](Fullmakt.md), [Rolle](Rolle.md), [Arbeidslokasjon](Arbeidslokasjon.md), [Organisasjonselement](Organisasjonselement.md), [Personalressurs](Personalressurs.md), [Arbeidsforhold](Arbeidsforhold.md), [Begrep](Begrep.md), [Valuta](Valuta.md), [Person](Person.md), [Kontaktperson](Kontaktperson.md), [Virksomhet](Virksomhet.md) |

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