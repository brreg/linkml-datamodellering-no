

# Slot: tilstandstype 


_Type tilstand (AKTIV, UNDER_KONKURS o.l.)._





URI: [ngrv:tilstandstype](https://data.norge.no/vocabulary/ngr-virksomhet#tilstandstype)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tilstand](tilstand.md) | Registrert tilstand (status) for ei verksemd i Enhetsregisteret, med gyldighe... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TilstandType](tilstandtype.md) |
| Domain Of | [Tilstand](tilstand.md) |
| Slot URI | [ngrv:tilstandstype](https://data.norge.no/vocabulary/ngr-virksomhet#tilstandstype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:tilstandstype |
| native | https://data.norge.no/ngr/ngr-virksomhet/tilstandstype |




## LinkML Source

<details>
```yaml
name: tilstandstype
description: Type tilstand (AKTIV, UNDER_KONKURS o.l.).
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slot_uri: ngrv:tilstandstype
domain_of:
- Tilstand
range: TilstandType

```
</details>