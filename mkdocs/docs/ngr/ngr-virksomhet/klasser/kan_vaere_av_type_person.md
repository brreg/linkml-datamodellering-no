

# Slot: kan_vaere_av_type_person 


_Personen som er rolleinnehavar (frå Folkeregisteret)._





URI: [ngrv:kanVaereAvTypePerson](https://data.norge.no/vocabulary/ngr-virksomhet#kanVaereAvTypePerson)
Alias: kan_vaere_av_type_person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rolleinnehaver](rolleinnehaver.md) | Den som innehar ein rolle i ei verksemd |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [Rolleinnehaver](rolleinnehaver.md) |
| Slot URI | [ngrv:kanVaereAvTypePerson](https://data.norge.no/vocabulary/ngr-virksomhet#kanVaereAvTypePerson) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:kanVaereAvTypePerson |
| native | https://data.norge.no/linkml/ngr-virksomhet/kan_vaere_av_type_person |




## LinkML Source

<details>
```yaml
name: kan_vaere_av_type_person
description: Personen som er rolleinnehavar (frå Folkeregisteret).
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:kanVaereAvTypePerson
alias: kan_vaere_av_type_person
domain_of:
- Rolleinnehaver
range: Person

```
</details>