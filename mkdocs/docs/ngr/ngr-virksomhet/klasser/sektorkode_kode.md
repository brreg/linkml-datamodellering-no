

# Slot: sektorkode_kode 


_Institusjonell sektorkode (t.d. 1120 for statsforvaltinga)._





URI: [ngrv:sektorkodeKode](https://data.norge.no/vocabulary/ngr-virksomhet#sektorkodeKode)
Alias: sektorkode_kode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sektorkode](sektorkode.md) | Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer (t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Sektorkode](sektorkode.md) |
| Slot URI | [ngrv:sektorkodeKode](https://data.norge.no/vocabulary/ngr-virksomhet#sektorkodeKode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:sektorkodeKode |
| native | https://data.norge.no/linkml/ngr-virksomhet/sektorkode_kode |




## LinkML Source

<details>
```yaml
name: sektorkode_kode
description: Institusjonell sektorkode (t.d. 1120 for statsforvaltinga).
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:sektorkodeKode
alias: sektorkode_kode
domain_of:
- Sektorkode
range: string

```
</details>