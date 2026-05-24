

# Slot: har_eierposisjon 


_Eierposisjon aksjeeigaren har._





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:har_eierposisjon](https://data.norge.no/linkml/register-over-aksjeeiere/:har_eierposisjon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aksjeeier](aksjeeier.md) | Person eller organisasjon som eig aksjar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eierposisjon](eierposisjon.md) |
| Domain | [Aksjeeier](aksjeeier.md) |
| Domain Of | [Aksjeeier](aksjeeier.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:har_eierposisjon |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:har_eierposisjon |




## LinkML Source

<details>
```yaml
name: har_eierposisjon
description: Eierposisjon aksjeeigaren har.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Aksjeeier
domain_of:
- Aksjeeier
range: Eierposisjon

```
</details>