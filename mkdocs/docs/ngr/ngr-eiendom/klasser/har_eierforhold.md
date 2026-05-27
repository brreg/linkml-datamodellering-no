

# Slot: har_eierforhold 


_Eigarforhold knytt til eigedommen eller burettslagsandelen._





URI: [ngre:harEierforhold](https://data.norge.no/vocabulary/ngr-eiendom#harEierforhold)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FastEiendom](fasteiendom.md) | Fast eiendom er eit grunnomgrep i eigedomsdomenet |  yes  |
| [Borettslagsandel](borettslagsandel.md) | Ein andel i eit burettslag som gir eksklusiv bruksrett til ein bestemt bustad... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eierforhold](eierforhold.md) |
| Domain Of | [FastEiendom](fasteiendom.md), [Borettslagsandel](borettslagsandel.md) |
| Slot URI | [ngre:harEierforhold](https://data.norge.no/vocabulary/ngr-eiendom#harEierforhold) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:harEierforhold |
| native | https://data.norge.no/ngr/ngr-eiendom/har_eierforhold |




## LinkML Source

<details>
```yaml
name: har_eierforhold
description: Eigarforhold knytt til eigedommen eller burettslagsandelen.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:harEierforhold
domain_of:
- FastEiendom
- Borettslagsandel
range: Eierforhold
multivalued: true

```
</details>