

# Slot: varslingstype 


_Kanaltype for varsling (EPOST eller MOBILTELEFON)._





URI: [ngrv:varslingstype](https://data.norge.no/vocabulary/ngr-virksomhet#varslingstype)
Alias: varslingstype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varslingsadresse](varslingsadresse.md) | Offisiell varslingsadresse for verksemda – e-post eller mobilnummer som vert ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VarslingType](varslingtype.md) |
| Domain Of | [Varslingsadresse](varslingsadresse.md) |
| Slot URI | [ngrv:varslingstype](https://data.norge.no/vocabulary/ngr-virksomhet#varslingstype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:varslingstype |
| native | https://data.norge.no/linkml/ngr-virksomhet/varslingstype |




## LinkML Source

<details>
```yaml
name: varslingstype
description: Kanaltype for varsling (EPOST eller MOBILTELEFON).
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:varslingstype
alias: varslingstype
domain_of:
- Varslingsadresse
range: VarslingType

```
</details>