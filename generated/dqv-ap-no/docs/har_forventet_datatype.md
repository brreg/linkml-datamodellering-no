

# Slot: har_forventet_datatype 


_Forventa XSD-datatype for verdien av ei kvalitetsmåling._





URI: [dqv:expectedDataType](http://www.w3.org/ns/dqv#expectedDataType)
Alias: har_forventet_datatype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsmaal](Kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Kvalitetsmaal](Kvalitetsmaal.md) |
| Slot URI | [dqv:expectedDataType](http://www.w3.org/ns/dqv#expectedDataType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:expectedDataType |
| native | https://data.norge.no/linkml/dqv-ap-no/har_forventet_datatype |




## LinkML Source

<details>
```yaml
name: har_forventet_datatype
description: Forventa XSD-datatype for verdien av ei kvalitetsmåling.
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: dqv:expectedDataType
alias: har_forventet_datatype
domain_of:
- Kvalitetsmaal
range: uriorcurie

```
</details>