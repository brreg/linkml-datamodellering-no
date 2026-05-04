

# Slot: koordinat_nord 


_Nordleg koordinat (Y) i det angitte koordinatsystemet._





URI: [ngr:koordinatNord](https://data.norge.no/vocabulary/ngr-adresse#koordinatNord)
Alias: koordinat_nord

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Representasjonspunkt](Representasjonspunkt.md) | Eit geografisk punkt (koordinatpar) som representerer posisjonen til adressa |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [Representasjonspunkt](Representasjonspunkt.md) |
| Slot URI | [ngr:koordinatNord](https://data.norge.no/vocabulary/ngr-adresse#koordinatNord) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:koordinatNord |
| native | https://data.norge.no/linkml/ngr-adresse/koordinat_nord |




## LinkML Source

<details>
```yaml
name: koordinat_nord
description: Nordleg koordinat (Y) i det angitte koordinatsystemet.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:koordinatNord
alias: koordinat_nord
domain_of:
- Representasjonspunkt
range: float

```
</details>