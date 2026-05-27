

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/ngr/ngr-adresse/id](https://data.norge.no/ngr/ngr-adresse/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeografiskAdresse](geografiskadresse.md) | Abstrakt basisklasse for norske adressar |  no  |
| [Adressenavn](adressenavn.md) | Offisielt namn på ei veglenke eller eit adresseobjekt i ein kommune, tildelt ... |  no  |
| [Adresseomrade](adresseomrade.md) | Geografisk område eit adressenavn høyrer til, t |  no  |
| [Adressekode](adressekode.md) | Firesifra kommunal kode som identifiserer eit adressenavn |  no  |
| [Husnummer](husnummer.md) | Husnummer beståande av eit obligatorisk nummer og ein valfri bokstav (t |  no  |
| [Bruksenhetsnummer](bruksenhetsnummer.md) | Identifikator for ei brukseining (leilegheit o |  no  |
| [Representasjonspunkt](representasjonspunkt.md) | Eit geografisk punkt (koordinatpar) som representerer posisjonen til adressa |  no  |
| [GeografiskOmrade](geografiskomrade.md) | Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer... |  no  |
| [Postboks](postboks.md) | Ei postboks registrert i Postboksregisteret |  no  |
| [Bygning](bygning.md) | Referanse til ein bygning i Matrikkelen |  no  |
| [Bruksenhet](bruksenhet.md) | Referanse til ei brukseining (leilegheit/lokale) i Matrikkelen |  no  |
| [OffisiellAdresse](offisielladresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  no  |
| [Postboksadresse](postboksadresse.md) | Ei postboksadresse registrert i Postboksregisteret (Posten Norge) |  no  |
| [Fylke](fylke.md) | Eit norsk fylke |  no  |
| [Kommune](kommune.md) | Ein norsk kommune |  no  |
| [Poststed](poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |  no  |
| [Grunnkrets](grunnkrets.md) | Ei grunnkrets – minste geografiske eining i statistisk inndeling |  no  |
| [Tettsted](tettsted.md) | Eit tettbygd område definert av SSB |  no  |
| [Kirkesokn](kirkesokn.md) | Eit kyrkjesokn |  no  |
| [Stemmekrets](stemmekrets.md) | Ei stemmekrets brukt ved val |  no  |
| [KommunalKrets](kommunalkrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |  no  |
| [Svalbard](svalbard.md) | Svalbard som særskild geografisk område |  no  |






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


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/ngr/ngr-adresse/id |
| native | https://data.norge.no/ngr/ngr-adresse/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
identifier: true
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