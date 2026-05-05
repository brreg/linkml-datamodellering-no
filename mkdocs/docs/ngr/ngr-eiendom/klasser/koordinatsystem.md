

# Slot: koordinatsystem 


_Koordinatsystem/projeksjon (t.d. EPSG:25833 for UTM sone 33N)._





URI: [ngre:koordinatsystem](https://data.norge.no/vocabulary/ngr-eiendom#koordinatsystem)
Alias: koordinatsystem

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Representasjonspunkt](representasjonspunkt.md) | Geografisk punkt (koordinatpar) som representerer posisjonen til bygningen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Representasjonspunkt](representasjonspunkt.md) |
| Slot URI | [ngre:koordinatsystem](https://data.norge.no/vocabulary/ngr-eiendom#koordinatsystem) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:koordinatsystem |
| native | https://data.norge.no/linkml/ngr-eiendom/koordinatsystem |




## LinkML Source

<details>
```yaml
name: koordinatsystem
description: Koordinatsystem/projeksjon (t.d. EPSG:25833 for UTM sone 33N).
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:koordinatsystem
alias: koordinatsystem
domain_of:
- Representasjonspunkt
range: string

```
</details>