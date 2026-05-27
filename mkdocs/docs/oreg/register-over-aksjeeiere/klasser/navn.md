

# Slot: navn 


_Namn på instansen._





URI: [https://data.norge.no/oreg/register-over-aksjeeiere/:navn](https://data.norge.no/oreg/register-over-aksjeeiere/:navn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aksjeselskap](aksjeselskap.md) | Selskap som utsteder aksjar og har aksjekapital |  no  |
| [Aksjeklasse](aksjeklasse.md) | Klasse aksjar høyrer til, med eigne rettigheiter |  no  |
| [Aksjeeier](aksjeeier.md) | Person eller organisasjon som eig aksjar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Aksjeselskap](aksjeselskap.md), [Aksjeklasse](aksjeklasse.md), [Aksjeeier](aksjeeier.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/oreg/register-over-aksjeeiere/:navn |
| native | https://data.norge.no/oreg/register-over-aksjeeiere/:navn |




## LinkML Source

<details>
```yaml
name: navn
description: Namn på instansen.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain_of:
- Aksjeselskap
- Aksjeklasse
- Aksjeeier
range: string
inlined: true

```
</details>