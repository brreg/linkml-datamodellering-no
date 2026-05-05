

# Slot: kommunenummer 


_Kommunenummer er en nummerrekke som identifiserer kommuner eller kommunefrie områder._





URI: [dcat:identifier](http://www.w3.org/ns/dcat#identifier)
Alias: kommunenummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](kommune.md) | En kommune er et geografisk avgrenset område som utgjør en egen politisk og a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kommune](kommune.md) |
| Slot URI | [dcat:identifier](http://www.w3.org/ns/dcat#identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:identifier |
| native | samtbuskole:kommunenummer |
| close | skos:notation |




## LinkML Source

<details>
```yaml
name: kommunenummer
description: Kommunenummer er en nummerrekke som identifiserer kommuner eller kommunefrie
  områder.
from_schema: https://example.no/ontology/samt-bu-skole
close_mappings:
- skos:notation
rank: 1000
slot_uri: dcat:identifier
alias: kommunenummer
domain_of:
- Kommune
range: string

```
</details>