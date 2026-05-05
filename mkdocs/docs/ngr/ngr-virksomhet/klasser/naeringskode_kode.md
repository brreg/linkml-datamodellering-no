

# Slot: naeringskode_kode 


_NACE-kode for næringsgruppering (t.d. 62.010)._





URI: [ngrv:naeringskodeKode](https://data.norge.no/vocabulary/ngr-virksomhet#naeringskodeKode)
Alias: naeringskode_kode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Naeringskode](naeringskode.md) | Næringskode basert på SSBs Standard for næringsgruppering (SN2007/NACE) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Naeringskode](naeringskode.md) |
| Slot URI | [ngrv:naeringskodeKode](https://data.norge.no/vocabulary/ngr-virksomhet#naeringskodeKode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:naeringskodeKode |
| native | https://data.norge.no/linkml/ngr-virksomhet/naeringskode_kode |




## LinkML Source

<details>
```yaml
name: naeringskode_kode
description: NACE-kode for næringsgruppering (t.d. 62.010).
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:naeringskodeKode
alias: naeringskode_kode
domain_of:
- Naeringskode
range: string

```
</details>