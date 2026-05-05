

# Slot: namn 


_Namn på det geografiske området eller adressekomponenten._





URI: [ngr:namn](https://data.norge.no/vocabulary/ngr-adresse#namn)
Alias: namn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](kommune.md) | Ein norsk kommune |  no  |
| [GeografiskOmrade](geografiskomrade.md) | Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer... |  no  |
| [Fylke](fylke.md) | Eit norsk fylke |  no  |
| [Tettsted](tettsted.md) | Eit tettbygd område definert av SSB |  no  |
| [Svalbard](svalbard.md) | Svalbard som særskild geografisk område |  no  |
| [Grunnkrets](grunnkrets.md) | Ei grunnkrets – minste geografiske eining i statistisk inndeling |  no  |
| [Adresseomrade](adresseomrade.md) | Geografisk område eit adressenavn høyrer til, t |  no  |
| [KommunalKrets](kommunalkrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |  no  |
| [Poststed](poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |  no  |
| [Stemmekrets](stemmekrets.md) | Ei stemmekrets brukt ved val |  no  |
| [Kirkesokn](kirkesokn.md) | Eit kyrkjesokn |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Adresseomrade](adresseomrade.md), [GeografiskOmrade](geografiskomrade.md) |
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