

# Slot: representasjonspunkt_ref 


_Geografisk punkt som representerer adressas posisjon._





URI: [ngr:harRepresentasjonspunkt](https://data.norge.no/vocabulary/ngr-adresse#harRepresentasjonspunkt)
Alias: representasjonspunkt_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](OffisiellAdresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Representasjonspunkt](Representasjonspunkt.md) |
| Domain Of | [OffisiellAdresse](OffisiellAdresse.md) |
| Slot URI | [ngr:harRepresentasjonspunkt](https://data.norge.no/vocabulary/ngr-adresse#harRepresentasjonspunkt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:harRepresentasjonspunkt |
| native | https://data.norge.no/linkml/ngr-adresse/representasjonspunkt_ref |




## LinkML Source

<details>
```yaml
name: representasjonspunkt_ref
description: Geografisk punkt som representerer adressas posisjon.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:harRepresentasjonspunkt
alias: representasjonspunkt_ref
domain_of:
- OffisiellAdresse
range: Representasjonspunkt

```
</details>