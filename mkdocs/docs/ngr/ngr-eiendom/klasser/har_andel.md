

# Slot: har_andel 


_Andel(ar) i heimelsdokumentet._





URI: [ngre:harAndel](https://data.norge.no/vocabulary/ngr-eiendom#harAndel)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hjemmel](hjemmel.md) | Abstrakt klasse for heimelsdokument |  yes  |
| [HjemmelTilEiendomsrett](hjemmeltileiendomsrett.md) | Heimelsdokument for eigedomsrett (full eigarrett) |  no  |
| [HjemmelTilFesterett](hjemmeltilfesterett.md) | Heimelsdokument for festerett (langvarig bruksrett til festegrunn) |  no  |
| [HjemmelTilFramfesterett](hjemmeltilframfesterett.md) | Heimelsdokument for framfesterett (vidarefestekontrakt) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Andel](andel.md) |
| Domain Of | [Hjemmel](hjemmel.md) |
| Slot URI | [ngre:harAndel](https://data.norge.no/vocabulary/ngr-eiendom#harAndel) |

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
| self | ngre:harAndel |
| native | https://data.norge.no/ngr/ngr-eiendom/har_andel |




## LinkML Source

<details>
```yaml
name: har_andel
description: Andel(ar) i heimelsdokumentet.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:harAndel
domain_of:
- Hjemmel
range: Andel
multivalued: true

```
</details>