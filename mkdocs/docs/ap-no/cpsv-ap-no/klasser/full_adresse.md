

# Slot: full_adresse 


_Full adresse som fritekst._





URI: [locn:fullAddress](http://www.w3.org/ns/locn#fullAddress)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adresse](adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Adresse](adresse.md) |
| Slot URI | [locn:fullAddress](http://www.w3.org/ns/locn#fullAddress) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:fullAddress |
| native | https://data.norge.no/linkml/cpsv-ap-no/full_adresse |




## LinkML Source

<details>
```yaml
name: full_adresse
description: Full adresse som fritekst.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: locn:fullAddress
domain_of:
- Adresse
range: string
multivalued: true

```
</details>