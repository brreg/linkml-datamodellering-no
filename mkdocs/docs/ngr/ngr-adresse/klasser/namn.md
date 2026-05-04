

# Slot: namn 


_Namn på det geografiske området eller adressekomponenten._





URI: [ngr:namn](https://data.norge.no/vocabulary/ngr-adresse#namn)
Alias: namn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fylke](Fylke.md) | Eit norsk fylke |  no  |
| [Tettsted](Tettsted.md) | Eit tettbygd område definert av SSB |  no  |
| [Kirkesokn](Kirkesokn.md) | Eit kyrkjesokn |  no  |
| [Grunnkrets](Grunnkrets.md) | Ei grunnkrets – minste geografiske eining i statistisk inndeling |  no  |
| [Stemmekrets](Stemmekrets.md) | Ei stemmekrets brukt ved val |  no  |
| [Poststed](Poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |  no  |
| [KommunalKrets](KommunalKrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |  no  |
| [Adresseomrade](Adresseomrade.md) | Geografisk område eit adressenavn høyrer til, t |  no  |
| [GeografiskOmrade](GeografiskOmrade.md) | Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer... |  no  |
| [Svalbard](Svalbard.md) | Svalbard som særskild geografisk område |  no  |
| [Kommune](Kommune.md) | Ein norsk kommune |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Adresseomrade](Adresseomrade.md), [GeografiskOmrade](GeografiskOmrade.md) |
| Slot URI | [ngr:namn](https://data.norge.no/vocabulary/ngr-adresse#namn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:namn |
| native | https://data.norge.no/linkml/ngr-adresse/namn |




## LinkML Source

<details>
```yaml
name: namn
description: Namn på det geografiske området eller adressekomponenten.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:namn
alias: namn
domain_of:
- Adresseomrade
- GeografiskOmrade
range: string

```
</details>