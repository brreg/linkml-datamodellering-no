

# Slot: passiv 


_Angir at koden er passiv og ikkje kan veljast._





URI: [fint:passiv](https://schema.fintlabs.no/passiv)
Alias: passiv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Uketimetall](uketimetall.md) | Timer per veke i 100 % stilling |  no  |
| [Kontrakt](kontrakt.md) | Kontrakt transaksjonen er knytt til |  no  |
| [Personalressurskategori](personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Anlegg](anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |  no  |
| [Fravaersgrunn](fravaersgrunn.md) | Grunn til fråvær |  no  |
| [Organisasjonstype](organisasjonstype.md) | Typen til eit organisasjonselement |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Funksjon](funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Formaal](formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |  no  |
| [Stillingskode](stillingskode.md) | Felles kodeverk for stillingar |  no  |
| [Lonsart](lonsart.md) | Type ytelse |  no  |
| [Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  no  |
| [Objekt](objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |  no  |
| [Ramme](ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |  no  |
| [Prosjekt](prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |  no  |
| [Arbeidsforholdstype](arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Lopenummer](lopenummer.md) | Løpenummer i ei nummerserie |  no  |
| [Fravaerstype](fravaerstype.md) | Type fråvær |  no  |
| [Diverse](diverse.md) | Del av kontostrengen; supplement til øvrige dimensjonar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Art](art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |  no  |
| [Aktivitet](aktivitet.md) | Del av kontostrengen og detaljering av funksjon |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [Begrep](begrep.md) |
| Slot URI | [fint:passiv](https://schema.fintlabs.no/passiv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:passiv |
| native | https://schema.fintlabs.no/:passiv |




## LinkML Source

<details>
```yaml
name: passiv
description: Angir at koden er passiv og ikkje kan veljast.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:passiv
alias: passiv
domain_of:
- Begrep
range: boolean

```
</details>