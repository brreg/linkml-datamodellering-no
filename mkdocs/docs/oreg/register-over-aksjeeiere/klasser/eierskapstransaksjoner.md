

# Slot: eierskapstransaksjoner 


_Samling av eigarskapstransaksjonar._





URI: [aksje:eierskapstransaksjoner](https://example.no/ontology/aksje#eierskapstransaksjoner)
Alias: eierskapstransaksjoner

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eierskapstransaksjon](eierskapstransaksjon.md) |
| Domain | [Containerklasse](containerklasse.md) |
| Domain Of | [Containerklasse](containerklasse.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:eierskapstransaksjoner |
| native | aksje:eierskapstransaksjoner |




## LinkML Source

<details>
```yaml
name: eierskapstransaksjoner
description: Samling av eigarskapstransaksjonar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
alias: eierskapstransaksjoner
domain_of:
- Containerklasse
range: Eierskapstransaksjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>