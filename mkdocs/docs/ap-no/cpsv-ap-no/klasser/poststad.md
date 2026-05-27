

# Slot: poststad 


_Poststad/by._





URI: [locn:postName](http://www.w3.org/ns/locn#postName)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adresse](adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Adresse](adresse.md) |
| Slot URI | [locn:postName](http://www.w3.org/ns/locn#postName) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:postName |
| native | https://data.norge.no/ap-no/cpsv-ap-no/poststad |




## LinkML Source

<details>
```yaml
name: poststad
description: Poststad/by.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: locn:postName
domain_of:
- Adresse
range: LangString
multivalued: true

```
</details>