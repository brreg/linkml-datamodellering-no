

# Slot: prosjektart 


_Deloppgåve eller delprosjekt._





URI: [adm:prosjektart](https://schema.fintlabs.no/administrasjon/prosjektart)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  yes  |
| [Prosjekt](prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Prosjektart](prosjektart.md) |
| Domain Of | [Kontostreng](kontostreng.md), [Prosjekt](prosjekt.md) |
| Slot URI | [adm:prosjektart](https://schema.fintlabs.no/administrasjon/prosjektart) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:prosjektart |
| native | https://schema.fintlabs.no/administrasjon/:prosjektart |




## LinkML Source

<details>
```yaml
name: prosjektart
description: Deloppgåve eller delprosjekt.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:prosjektart
domain_of:
- Kontostreng
- Prosjekt
range: Prosjektart

```
</details>