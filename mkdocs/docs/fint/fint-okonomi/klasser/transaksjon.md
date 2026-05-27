

# Slot: transaksjon 


_Transaksjonen posteringa tilhøyrer._





URI: [okn:transaksjon](https://schema.fintlabs.no/okonomi/transaksjon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Transaksjon](transaksjon.md) |
| Domain Of | [Postering](postering.md) |
| Slot URI | [okn:transaksjon](https://schema.fintlabs.no/okonomi/transaksjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:transaksjon |
| native | https://schema.fintlabs.no/okonomi/:transaksjon |




## LinkML Source

<details>
```yaml
name: transaksjon
description: Transaksjonen posteringa tilhøyrer.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:transaksjon
domain_of:
- Postering
range: Transaksjon

```
</details>