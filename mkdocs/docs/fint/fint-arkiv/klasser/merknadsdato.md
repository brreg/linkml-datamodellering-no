

# Slot: merknadsdato 


_Dato og klokkeslett merknaden vart registrert._





URI: [ark:merknadsdato](https://schema.fintlabs.no/arkiv/merknadsdato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Merknad](merknad.md) | Merknad knytt til mappe, registrering eller dokumentbeskrivelse |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Merknad](merknad.md) |
| Slot URI | [ark:merknadsdato](https://schema.fintlabs.no/arkiv/merknadsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:merknadsdato |
| native | https://schema.fintlabs.no/arkiv/:merknadsdato |




## LinkML Source

<details>
```yaml
name: merknadsdato
description: Dato og klokkeslett merknaden vart registrert.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:merknadsdato
domain_of:
- Merknad
range: datetime

```
</details>