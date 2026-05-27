

# Slot: har_verdi 


_Målt verdi (xsd:boolean, xsd:double, xsd:nonNegativeInteger eller rdfs:Literal avhengig av kvalitetsmålet)._





URI: [dqv:value](http://www.w3.org/ns/dqv#value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsmaaling](kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Kvalitetsmaaling](kvalitetsmaaling.md) |
| Slot URI | [dqv:value](http://www.w3.org/ns/dqv#value) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:value |
| native | https://data.norge.no/ap-no/dqv-ap-no/har_verdi |




## LinkML Source

<details>
```yaml
name: har_verdi
description: Målt verdi (xsd:boolean, xsd:double, xsd:nonNegativeInteger eller rdfs:Literal
  avhengig av kvalitetsmålet).
from_schema: https://data.norge.no/ap-no/dqv-ap-no
slot_uri: dqv:value
domain_of:
- Kvalitetsmaaling
range: string

```
</details>