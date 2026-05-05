

# Slot: heimeside 


_Heimeside for ressursen eller organisasjonen (foaf:homepage)._





URI: [foaf:homepage](http://xmlns.com/foaf/0.1/homepage)
Alias: heimeside

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](uri.md) |
| Domain Of | [Katalog](katalog.md) |
| Slot URI | [foaf:homepage](http://xmlns.com/foaf/0.1/homepage) |

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
| self | foaf:homepage |
| native | samtbuskole:heimeside |




## LinkML Source

<details>
```yaml
name: heimeside
description: Heimeside for ressursen eller organisasjonen (foaf:homepage).
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: foaf:homepage
alias: heimeside
domain_of:
- Katalog
range: uri
multivalued: true

```
</details>