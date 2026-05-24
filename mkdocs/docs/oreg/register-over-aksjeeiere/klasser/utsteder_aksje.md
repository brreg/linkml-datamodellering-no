

# Slot: utsteder_aksje 


_Aksje utstedt av selskapet_





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:utsteder_aksje](https://data.norge.no/linkml/register-over-aksjeeiere/:utsteder_aksje)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aksjeselskap](aksjeselskap.md) | Selskap som utsteder aksjar og har aksjekapital |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aksje](aksje.md) |
| Domain | [Aksjeselskap](aksjeselskap.md) |
| Domain Of | [Aksjeselskap](aksjeselskap.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:utsteder_aksje |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:utsteder_aksje |




## LinkML Source

<details>
```yaml
name: utsteder_aksje
description: Aksje utstedt av selskapet
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Aksjeselskap
domain_of:
- Aksjeselskap
range: Aksje

```
</details>