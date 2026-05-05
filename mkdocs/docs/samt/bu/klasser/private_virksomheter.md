

# Slot: private_virksomheter 


_Container slot for å legge tilrette for å kunne ha fleire instanser av private_virksomheter i ei datafil._





URI: [samtbuskole:private_virksomheter](https://example.no/ontology/skole#private_virksomheter)
Alias: private_virksomheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PrivatVirksomhet](privatvirksomhet.md) |
| Domain Of | [Containerklasse](containerklasse.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:private_virksomheter |
| native | samtbuskole:private_virksomheter |




## LinkML Source

<details>
```yaml
name: private_virksomheter
description: Container slot for å legge tilrette for å kunne ha fleire instanser av
  private_virksomheter i ei datafil.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
alias: private_virksomheter
domain_of:
- Containerklasse
range: PrivatVirksomhet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>