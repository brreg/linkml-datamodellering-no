

# Slot: verdi 


_Verdien til identifikatoren._





URI: [brreg_felles_aktoer:verdi](https://data.norge.no/felles/brreg-felles-aktoer/verdi)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personidentifikator](personidentifikator.md) | Ein identifikator for ein person, med ein type som seier kva slag identifikator det er. |  yes  |
| [Virksomhetsidentifikator](virksomhetsidentifikator.md) | Ein identifikator for ei verksemd, med ein type som seier kva slag identifikator det er. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Personidentifikator](personidentifikator.md), [Virksomhetsidentifikator](virksomhetsidentifikator.md) |
| Slot URI | [brreg_felles_aktoer:verdi](https://data.norge.no/felles/brreg-felles-aktoer/verdi) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-aktoer




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_aktoer:verdi |
| native | https://data.norge.no/felles/brreg-felles-aktoer/verdi |




## LinkML Source

<details>
```yaml
name: verdi
description: Verdien til identifikatoren.
from_schema: https://data.norge.no/felles/brreg-felles-aktoer
slot_uri: brreg_felles_aktoer:verdi
domain_of:
- Personidentifikator
- Virksomhetsidentifikator
range: string

```
</details>