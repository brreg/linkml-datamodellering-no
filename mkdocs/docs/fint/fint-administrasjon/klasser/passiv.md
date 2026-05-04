

# Slot: passiv 


_Angir at koden er passiv og ikkje kan veljast._





URI: [fint:passiv](https://schema.fintlabs.no/passiv)
Alias: passiv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Personalressurskategori](Personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |  no  |
| [Fravaersgrunn](Fravaersgrunn.md) | Grunn til fråvær |  no  |
| [Ramme](Ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |  no  |
| [Ansvar](Ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  no  |
| [Objekt](Objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |  no  |
| [Formaal](Formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |  no  |
| [Stillingskode](Stillingskode.md) | Felles kodeverk for stillingar |  no  |
| [Anlegg](Anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |  no  |
| [Art](Art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Aktivitet](Aktivitet.md) | Del av kontostrengen og detaljering av funksjon |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Prosjektart](Prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Lopenummer](Lopenummer.md) | Løpenummer i ei nummerserie |  no  |
| [Arbeidsforholdstype](Arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |  no  |
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






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Begrep](Begrep.md) |
| Slot URI | [fint:passiv](https://schema.fintlabs.no/passiv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Begrep](Begrep.md) |








## In Subsets


* [Valgfri](Valgfri.md)






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