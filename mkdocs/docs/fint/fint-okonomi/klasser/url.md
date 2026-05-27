

# Slot: url 


_URL til eksternt dokument._





URI: [okn:url](https://schema.fintlabs.no/okonomi/url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bilag](bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Bilag](bilag.md) |
| Slot URI | [okn:url](https://schema.fintlabs.no/okonomi/url) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:url |
| native | https://schema.fintlabs.no/okonomi/:url |




## LinkML Source

<details>
```yaml
name: url
description: URL til eksternt dokument.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:url
domain_of:
- Bilag
range: string

```
</details>