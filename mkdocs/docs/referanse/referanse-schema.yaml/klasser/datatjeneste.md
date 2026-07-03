

# Slot: datatjeneste 


_Datatjeneste som er del av katalogen._





URI: [dcat:service](http://www.w3.org/ns/dcat#service)
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


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:service |
| native | https://data.norge.no/ap-no/dcat-ap-no/datatjeneste |




## LinkML Source

<details>
```yaml
name: datatjeneste
description: Datatjeneste som er del av katalogen.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dcat:service
domain_of:
- Katalog
range: Datatjeneste
multivalued: true

```
</details>