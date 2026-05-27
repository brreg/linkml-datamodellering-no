

# Slot: personnavn 


_Namn på person (Personnavn-objekt)._





URI: [ark:personnavn](https://schema.fintlabs.no/arkiv/personnavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personnavn](personnavn.md) |
| Domain Of | [Personalmappe](personalmappe.md) |
| Slot URI | [ark:personnavn](https://schema.fintlabs.no/arkiv/personnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:personnavn |
| native | https://schema.fintlabs.no/arkiv/:personnavn |




## LinkML Source

<details>
```yaml
name: personnavn
description: Namn på person (Personnavn-objekt).
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:personnavn
domain_of:
- Personalmappe
range: Personnavn
inlined: true

```
</details>