

# Slot: merknadstekst 


_Merknad frå saksbehandlar, leiar eller arkivpersonale._





URI: [ark:merknadstekst](https://schema.fintlabs.no/arkiv/merknadstekst)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Merknad](merknad.md) | Merknad knytt til mappe, registrering eller dokumentbeskrivelse |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Merknad](merknad.md) |
| Slot URI | [ark:merknadstekst](https://schema.fintlabs.no/arkiv/merknadstekst) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:merknadstekst |
| native | https://schema.fintlabs.no/arkiv/:merknadstekst |




## LinkML Source

<details>
```yaml
name: merknadstekst
description: Merknad frå saksbehandlar, leiar eller arkivpersonale.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:merknadstekst
domain_of:
- Merknad
range: string

```
</details>