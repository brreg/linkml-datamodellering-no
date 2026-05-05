

# Slot: relatert_ressurs 


_Generisk relasjon til ein annan ressurs._





URI: [dct:relation](http://purl.org/dc/terms/relation)
Alias: relatert_ressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](uri.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dct:relation](http://purl.org/dc/terms/relation) |

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
| self | dct:relation |
| native | samtbuskole:relatert_ressurs |




## LinkML Source

<details>
```yaml
name: relatert_ressurs
description: Generisk relasjon til ein annan ressurs.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:relation
alias: relatert_ressurs
domain_of:
- Datasett
range: uri
multivalued: true

```
</details>