

# Slot: juridiskNavn 


_Juridisk namn på skulen._





URI: [utd:juridiskNavn](https://schema.fintlabs.no/utdanning/juridiskNavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Skole](skole.md) |
| Slot URI | [utd:juridiskNavn](https://schema.fintlabs.no/utdanning/juridiskNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:juridiskNavn |
| native | https://schema.fintlabs.no/utdanning/:juridiskNavn |




## LinkML Source

<details>
```yaml
name: juridiskNavn
description: Juridisk namn på skulen.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:juridiskNavn
domain_of:
- Skole
range: string

```
</details>