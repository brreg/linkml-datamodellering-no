

# Slot: trinn 


_Årstrinnet._





URI: [utd:trinn](https://schema.fintlabs.no/utdanning/trinn)
Alias: trinn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  yes  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  yes  |






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


* from schema: https://data.norge.no/linkml/fint-utdanning




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
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:trinn
alias: trinn
domain_of:
- Klasse
- Programomrade
range: Arstrinn
multivalued: true

```
</details>