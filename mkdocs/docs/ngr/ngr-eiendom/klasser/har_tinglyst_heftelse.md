

# Slot: har_tinglyst_heftelse 


_Tinglyste heftingar knytt til eigedommen eller burettslagsandelen._





URI: [ngre:harTinglystHeftelse](https://data.norge.no/vocabulary/ngr-eiendom#harTinglystHeftelse)
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
| Range | [TinglystHeftelse](tinglystheftelse.md) |
| Domain Of | [FastEiendom](fasteiendom.md), [Borettslagsandel](borettslagsandel.md) |
| Slot URI | [ngre:harTinglystHeftelse](https://data.norge.no/vocabulary/ngr-eiendom#harTinglystHeftelse) |

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
| self | ngre:harTinglystHeftelse |
| native | https://data.norge.no/ngr/ngr-eiendom/har_tinglyst_heftelse |




## LinkML Source

<details>
```yaml
name: har_tinglyst_heftelse
description: Tinglyste heftingar knytt til eigedommen eller burettslagsandelen.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:harTinglystHeftelse
domain_of:
- FastEiendom
- Borettslagsandel
range: TinglystHeftelse
multivalued: true

```
</details>