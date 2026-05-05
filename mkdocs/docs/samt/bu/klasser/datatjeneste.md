

# Slot: datatjeneste 


_Datatjeneste som er del av katalogen._





URI: [dcat:service](http://www.w3.org/ns/dcat#service)
Alias: datatjeneste

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datatjeneste](datatjeneste.md) |
| Domain Of | [Katalog](katalog.md) |
| Slot URI | [dcat:service](http://www.w3.org/ns/dcat#service) |

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
| self | dcat:service |
| native | samtbuskole:datatjeneste |




## LinkML Source

<details>
```yaml
name: datatjeneste
description: Datatjeneste som er del av katalogen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:service
alias: datatjeneste
domain_of:
- Katalog
range: Datatjeneste
multivalued: true

```
</details>