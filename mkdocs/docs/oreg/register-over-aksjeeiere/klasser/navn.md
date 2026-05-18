

# Slot: navn 


_Namn på instansen._





URI: [aksje:navn](https://example.no/ontology/aksje#navn)
Alias: navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aksjeklasse](aksjeklasse.md) | Klasse aksjar høyrer til, med eigne rettigheiter |  no  |
| [Aksjeeier](aksjeeier.md) | Person eller organisasjon som eig aksjar |  no  |
| [Aksjeselskap](aksjeselskap.md) | Selskap som utsteder aksjar og har aksjekapital |  no  |






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
| self | aksje:navn |
| native | aksje:navn |




## LinkML Source

<details>
```yaml
name: navn
description: Namn på instansen.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
alias: navn
domain_of:
- Aksjeselskap
- Aksjeklasse
- Aksjeeier
range: string
inlined: true

```
</details>