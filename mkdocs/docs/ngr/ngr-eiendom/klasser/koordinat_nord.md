

# Slot: koordinat_nord 


_Nordleg koordinat (Y) i det angitte koordinatsystemet._





URI: [ngre:koordinatNord](https://data.norge.no/vocabulary/ngr-eiendom#koordinatNord)
Alias: koordinat_nord

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Representasjonspunkt](representasjonspunkt.md) | Geografisk punkt (koordinatpar) som representerer posisjonen til bygningen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](float.md) |
| Domain Of | [Representasjonspunkt](representasjonspunkt.md) |
| Slot URI | [ngre:koordinatNord](https://data.norge.no/vocabulary/ngr-eiendom#koordinatNord) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:koordinatNord |
| native | https://data.norge.no/linkml/ngr-eiendom/koordinat_nord |




## LinkML Source

<details>
```yaml
name: koordinat_nord
description: Nordleg koordinat (Y) i det angitte koordinatsystemet.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:koordinatNord
alias: koordinat_nord
domain_of:
- Representasjonspunkt
range: float

```
</details>