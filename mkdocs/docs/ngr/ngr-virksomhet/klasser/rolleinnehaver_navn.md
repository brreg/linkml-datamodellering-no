

# Slot: rolleinnehaver_navn 


_Namn på rolleinnehavar (nyttes for institusjonelle rollehavarar)._





URI: [ngrv:rolleinnehaverNavn](https://data.norge.no/vocabulary/ngr-virksomhet#rolleinnehaverNavn)
Alias: rolleinnehaver_navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rolleinnehaver](Rolleinnehaver.md) | Den som innehar ein rolle i ei verksemd |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Rolleinnehaver](Rolleinnehaver.md) |
| Slot URI | [ngrv:rolleinnehaverNavn](https://data.norge.no/vocabulary/ngr-virksomhet#rolleinnehaverNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:rolleinnehaverNavn |
| native | https://data.norge.no/linkml/ngr-virksomhet/rolleinnehaver_navn |




## LinkML Source

<details>
```yaml
name: rolleinnehaver_navn
description: Namn på rolleinnehavar (nyttes for institusjonelle rollehavarar).
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:rolleinnehaverNavn
alias: rolleinnehaver_navn
domain_of:
- Rolleinnehaver
range: string

```
</details>