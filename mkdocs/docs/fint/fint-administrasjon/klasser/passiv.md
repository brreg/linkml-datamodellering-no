

# Slot: passiv 


_Angir at koden er passiv og ikkje kan veljast._





URI: [fint:passiv](https://schema.fintlabs.no/passiv)
Alias: passiv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Stillingskode](stillingskode.md) | Felles kodeverk for stillingar |  no  |
| [Lonsart](lonsart.md) | Type ytelse |  no  |
| [Personalressurskategori](personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |  no  |
| [Fravaerstype](fravaerstype.md) | Type fråvær |  no  |
| [Funksjon](funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |  no  |
| [Fravaersgrunn](fravaersgrunn.md) | Grunn til fråvær |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Lopenummer](lopenummer.md) | Løpenummer i ei nummerserie |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  no  |
| [Objekt](objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Diverse](diverse.md) | Del av kontostrengen; supplement til øvrige dimensjonar |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Arbeidsforholdstype](arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |  no  |
| [Kontrakt](kontrakt.md) | Kontrakt transaksjonen er knytt til |  no  |
| [Aktivitet](aktivitet.md) | Del av kontostrengen og detaljering av funksjon |  no  |
| [Anlegg](anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |  no  |
| [Formaal](formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |  no  |
| [Prosjekt](prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |  no  |
| [Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Organisasjonstype](organisasjonstype.md) | Typen til eit organisasjonselement |  no  |
| [Ramme](ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |  no  |
| [Uketimetall](uketimetall.md) | Timer per veke i 100 % stilling |  no  |
| [Art](art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](boolean.md) |
| Domain Of | [Begrep](begrep.md) |
| Slot URI | [fint:passiv](https://schema.fintlabs.no/passiv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Begrep](begrep.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:passiv |
| native | https://schema.fintlabs.no/administrasjon/:passiv |




## LinkML Source

<details>
```yaml
name: passiv
description: Angir at koden er passiv og ikkje kan veljast.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:passiv
alias: passiv
owner: Begrep
domain_of:
- Begrep
range: boolean

```
</details>