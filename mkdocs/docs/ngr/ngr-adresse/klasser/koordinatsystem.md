

# Slot: koordinatsystem 


_Koordinatsystem/projeksjon (t.d. EPSG:25833 for UTM sone 33N)._





URI: [ngr:koordinatsystem](https://data.norge.no/vocabulary/ngr-adresse#koordinatsystem)
Alias: koordinatsystem

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Representasjonspunkt](representasjonspunkt.md) | Eit geografisk punkt (koordinatpar) som representerer posisjonen til adressa |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Representasjonspunkt](representasjonspunkt.md) |
| Slot URI | [ngr:koordinatsystem](https://data.norge.no/vocabulary/ngr-adresse#koordinatsystem) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:koordinatsystem |
| native | https://data.norge.no/linkml/ngr-adresse/koordinatsystem |




## LinkML Source

<details>
```yaml
name: koordinatsystem
description: Koordinatsystem/projeksjon (t.d. EPSG:25833 for UTM sone 33N).
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:koordinatsystem
alias: koordinatsystem
domain_of:
- Representasjonspunkt
range: string

```
</details>