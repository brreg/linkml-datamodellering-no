

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/ngr-adresse/id](https://data.norge.no/linkml/ngr-adresse/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adressenavn](adressenavn.md) | Offisielt namn på ei veglenke eller eit adresseobjekt i ein kommune, tildelt ... |  no  |
| [Bruksenhet](bruksenhet.md) | Referanse til ei brukseining (leilegheit/lokale) i Matrikkelen |  no  |
| [Adresseomrade](adresseomrade.md) | Geografisk område eit adressenavn høyrer til, t |  no  |
| [Bygning](bygning.md) | Referanse til ein bygning i Matrikkelen |  no  |
| [Adressekode](adressekode.md) | Firesifra kommunal kode som identifiserer eit adressenavn |  no  |
| [Poststed](poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |  no  |
| [Svalbard](svalbard.md) | Svalbard som særskild geografisk område |  no  |
| [Kirkesokn](kirkesokn.md) | Eit kyrkjesokn |  no  |
| [Representasjonspunkt](representasjonspunkt.md) | Eit geografisk punkt (koordinatpar) som representerer posisjonen til adressa |  no  |
| [GeografiskAdresse](geografiskadresse.md) | Abstrakt basisklasse for norske adressar |  no  |
| [Fylke](fylke.md) | Eit norsk fylke |  no  |
| [Stemmekrets](stemmekrets.md) | Ei stemmekrets brukt ved val |  no  |
| [Kommune](kommune.md) | Ein norsk kommune |  no  |
| [Bruksenhetsnummer](bruksenhetsnummer.md) | Identifikator for ei brukseining (leilegheit o |  no  |
| [Husnummer](husnummer.md) | Husnummer beståande av eit obligatorisk nummer og ein valfri bokstav (t |  no  |
| [Grunnkrets](grunnkrets.md) | Ei grunnkrets – minste geografiske eining i statistisk inndeling |  no  |
| [KommunalKrets](kommunalkrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |  no  |
| [Postboksadresse](postboksadresse.md) | Ei postboksadresse registrert i Postboksregisteret (Posten Norge) |  no  |
| [GeografiskOmrade](geografiskomrade.md) | Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer... |  no  |
| [OffisiellAdresse](offisielladresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  no  |
| [Postboks](postboks.md) | Ei postboks registrert i Postboksregisteret |  no  |
| [Tettsted](tettsted.md) | Eit tettbygd område definert av SSB |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [GeografiskAdresse](geografiskadresse.md), [Adressenavn](adressenavn.md), [Adresseomrade](adresseomrade.md), [Adressekode](adressekode.md), [Husnummer](husnummer.md), [Bruksenhetsnummer](bruksenhetsnummer.md), [Representasjonspunkt](representasjonspunkt.md), [GeografiskOmrade](geografiskomrade.md), [Postboks](postboks.md), [Bygning](bygning.md), [Bruksenhet](bruksenhet.md) |

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