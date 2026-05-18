

# Slot: namn 


_Namn på det geografiske området eller adressekomponenten._





URI: [ngr:namn](https://data.norge.no/vocabulary/ngr-adresse#namn)
Alias: namn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KommunalKrets](kommunalkrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |  no  |
| [Stemmekrets](stemmekrets.md) | Ei stemmekrets brukt ved val |  no  |
| [Poststed](poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |  no  |
| [GeografiskOmrade](geografiskomrade.md) | Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer... |  no  |
| [Svalbard](svalbard.md) | Svalbard som særskild geografisk område |  no  |
| [Kirkesokn](kirkesokn.md) | Eit kyrkjesokn |  no  |
| [Adresseomrade](adresseomrade.md) | Geografisk område eit adressenavn høyrer til, t |  no  |
| [Fylke](fylke.md) | Eit norsk fylke |  no  |
| [Grunnkrets](grunnkrets.md) | Ei grunnkrets – minste geografiske eining i statistisk inndeling |  no  |
| [Tettsted](tettsted.md) | Eit tettbygd område definert av SSB |  no  |
| [Kommune](kommune.md) | Ein norsk kommune |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
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