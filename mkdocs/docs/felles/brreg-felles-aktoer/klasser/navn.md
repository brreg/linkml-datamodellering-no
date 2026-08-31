

# Slot: navn 


_Namnet på ressursen._





URI: [brreg_felles_adresse:navn](https://data.norge.no/felles/brreg-felles-adresse/navn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Poststed](poststed.md) | Eit poststed knytt til eit postnummer. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Poststed](poststed.md) |
| Slot URI | [brreg_felles_adresse:navn](https://data.norge.no/felles/brreg-felles-adresse/navn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_adresse:navn |
| native | https://data.norge.no/felles/brreg-felles-adresse/navn |




## LinkML Source

<details>
```yaml
name: navn
description: Namnet på ressursen.
from_schema: https://data.norge.no/felles/brreg-felles-adresse
slot_uri: brreg_felles_adresse:navn
domain_of:
- Poststed
range: string

```
</details>