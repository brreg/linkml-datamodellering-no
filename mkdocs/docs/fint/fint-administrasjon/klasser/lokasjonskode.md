

# Slot: lokasjonskode 


_Kode som identifiserer ein arbeidslokasjon._





URI: [adm:lokasjonskode](https://schema.fintlabs.no/administrasjon/lokasjonskode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Arbeidslokasjon](arbeidslokasjon.md) |
| Slot URI | [adm:lokasjonskode](https://schema.fintlabs.no/administrasjon/lokasjonskode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:lokasjonskode |
| native | https://schema.fintlabs.no/administrasjon/:lokasjonskode |




## LinkML Source

<details>
```yaml
name: lokasjonskode
description: Kode som identifiserer ein arbeidslokasjon.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:lokasjonskode
domain_of:
- Arbeidslokasjon
range: Identifikator
inlined: true

```
</details>