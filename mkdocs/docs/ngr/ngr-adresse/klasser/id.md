

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/ngr-adresse/id](https://data.norge.no/linkml/ngr-adresse/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bygning](Bygning.md) | Referanse til ein bygning i Matrikkelen |  no  |
| [Fylke](Fylke.md) | Eit norsk fylke |  no  |
| [Adressekode](Adressekode.md) | Firesifra kommunal kode som identifiserer eit adressenavn |  no  |
| [Poststed](Poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |  no  |
| [Bruksenhet](Bruksenhet.md) | Referanse til ei brukseining (leilegheit/lokale) i Matrikkelen |  no  |
| [Adresseomrade](Adresseomrade.md) | Geografisk område eit adressenavn høyrer til, t |  no  |
| [Adressenavn](Adressenavn.md) | Offisielt namn på ei veglenke eller eit adresseobjekt i ein kommune, tildelt ... |  no  |
| [Tettsted](Tettsted.md) | Eit tettbygd område definert av SSB |  no  |
| [Representasjonspunkt](Representasjonspunkt.md) | Eit geografisk punkt (koordinatpar) som representerer posisjonen til adressa |  no  |
| [Husnummer](Husnummer.md) | Husnummer beståande av eit obligatorisk nummer og ein valfri bokstav (t |  no  |
| [GeografiskAdresse](GeografiskAdresse.md) | Abstrakt basisklasse for norske adressar |  no  |
| [Bruksenhetsnummer](Bruksenhetsnummer.md) | Identifikator for ei brukseining (leilegheit o |  no  |
| [Svalbard](Svalbard.md) | Svalbard som særskild geografisk område |  no  |
| [Postboks](Postboks.md) | Ei postboks registrert i Postboksregisteret |  no  |
| [Postboksadresse](Postboksadresse.md) | Ei postboksadresse registrert i Postboksregisteret (Posten Norge) |  no  |
| [Kirkesokn](Kirkesokn.md) | Eit kyrkjesokn |  no  |
| [Grunnkrets](Grunnkrets.md) | Ei grunnkrets – minste geografiske eining i statistisk inndeling |  no  |
| [Stemmekrets](Stemmekrets.md) | Ei stemmekrets brukt ved val |  no  |
| [KommunalKrets](KommunalKrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |  no  |
| [GeografiskOmrade](GeografiskOmrade.md) | Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer... |  no  |
| [Kommune](Kommune.md) | Ein norsk kommune |  no  |
| [OffisiellAdresse](OffisiellAdresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [GeografiskAdresse](GeografiskAdresse.md), [Adressenavn](Adressenavn.md), [Adresseomrade](Adresseomrade.md), [Adressekode](Adressekode.md), [Husnummer](Husnummer.md), [Bruksenhetsnummer](Bruksenhetsnummer.md), [Representasjonspunkt](Representasjonspunkt.md), [GeografiskOmrade](GeografiskOmrade.md), [Postboks](Postboks.md), [Bygning](Bygning.md), [Bruksenhet](Bruksenhet.md) |

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


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-adresse/id |
| native | https://data.norge.no/linkml/ngr-adresse/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
identifier: true
alias: id
domain_of:
- GeografiskAdresse
- Adressenavn
- Adresseomrade
- Adressekode
- Husnummer
- Bruksenhetsnummer
- Representasjonspunkt
- GeografiskOmrade
- Postboks
- Bygning
- Bruksenhet
range: uriorcurie
required: true

```
</details>