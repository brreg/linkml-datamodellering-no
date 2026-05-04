

# Slot: navn 



URI: [https://schema.fintlabs.no/administrasjon/:navn](https://schema.fintlabs.no/administrasjon/:navn)
Alias: navn

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
| [Organisasjonselement](Organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
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
| [Valuta](Valuta.md) | Valutakodar for offisielle valutaer |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Organisasjonselement](Organisasjonselement.md), [Begrep](Begrep.md), [Valuta](Valuta.md), [Person](Person.md), [Kontaktperson](Kontaktperson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:navn |
| native | https://schema.fintlabs.no/administrasjon/:navn |




## LinkML Source

<details>
```yaml
name: navn
alias: navn
domain_of:
- Organisasjonselement
- Begrep
- Valuta
- Person
- Kontaktperson
range: string

```
</details>