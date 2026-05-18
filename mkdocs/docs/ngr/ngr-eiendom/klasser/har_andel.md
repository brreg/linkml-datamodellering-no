

# Slot: har_andel 


_Andel(ar) i heimelsdokumentet._





URI: [ngre:harAndel](https://data.norge.no/vocabulary/ngr-eiendom#harAndel)
Alias: har_andel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HjemmelTilFesterett](hjemmeltilfesterett.md) | Heimelsdokument for festerett (langvarig bruksrett til festegrunn) |  no  |
| [Hjemmel](hjemmel.md) | Abstrakt klasse for heimelsdokument |  yes  |
| [HjemmelTilFramfesterett](hjemmeltilframfesterett.md) | Heimelsdokument for framfesterett (vidarefestekontrakt) |  no  |
| [HjemmelTilEiendomsrett](hjemmeltileiendomsrett.md) | Heimelsdokument for eigedomsrett (full eigarrett) |  no  |






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


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:harAndel |
| native | https://data.norge.no/linkml/ngr-eiendom/har_andel |




## LinkML Source

<details>
```yaml
name: har_andel
description: Andel(ar) i heimelsdokumentet.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:harAndel
alias: har_andel
domain_of:
- Hjemmel
range: Andel
multivalued: true

```
</details>