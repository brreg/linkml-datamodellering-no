

# Slot: trinn 


_Årstrinnet._





URI: [utd:trinn](https://schema.fintlabs.no/utdanning/trinn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  yes  |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arstrinn](arstrinn.md) |
| Domain Of | [Klasse](klasse.md), [Programomrade](programomrade.md) |
| Slot URI | [utd:trinn](https://schema.fintlabs.no/utdanning/trinn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:trinn |
| native | https://schema.fintlabs.no/utdanning/:trinn |




## LinkML Source

<details>
```yaml
name: trinn
description: Årstrinnet.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:trinn
domain_of:
- Klasse
- Programomrade
range: Arstrinn
multivalued: true

```
</details>