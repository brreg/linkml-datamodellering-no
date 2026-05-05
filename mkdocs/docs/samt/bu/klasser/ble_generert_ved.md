

# Slot: ble_generert_ved 


_Aktiviteten som genererte datasettet._





URI: [prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy)
Alias: ble_generert_ved

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProvAktivitet](provaktivitet.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasGeneratedBy |
| native | samtbuskole:ble_generert_ved |




## LinkML Source

<details>
```yaml
name: ble_generert_ved
description: Aktiviteten som genererte datasettet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: prov:wasGeneratedBy
alias: ble_generert_ved
domain_of:
- Datasett
range: ProvAktivitet

```
</details>