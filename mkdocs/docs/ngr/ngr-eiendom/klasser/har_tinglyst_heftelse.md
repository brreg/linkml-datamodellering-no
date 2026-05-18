

# Slot: har_tinglyst_heftelse 


_Tinglyste heftingar knytt til eigedommen eller burettslagsandelen._





URI: [ngre:harTinglystHeftelse](https://data.norge.no/vocabulary/ngr-eiendom#harTinglystHeftelse)
Alias: har_tinglyst_heftelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Borettslagsandel](borettslagsandel.md) | Ein andel i eit burettslag som gir eksklusiv bruksrett til ein bestemt bustad... |  yes  |
| [FastEiendom](fasteiendom.md) | Fast eiendom er eit grunnomgrep i eigedomsdomenet |  yes  |






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


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:harTinglystHeftelse |
| native | https://data.norge.no/linkml/ngr-eiendom/har_tinglyst_heftelse |




## LinkML Source

<details>
```yaml
name: har_tinglyst_heftelse
description: Tinglyste heftingar knytt til eigedommen eller burettslagsandelen.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:harTinglystHeftelse
alias: har_tinglyst_heftelse
domain_of:
- FastEiendom
- Borettslagsandel
range: TinglystHeftelse
multivalued: true

```
</details>