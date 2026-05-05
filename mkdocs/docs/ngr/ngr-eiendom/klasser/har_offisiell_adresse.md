

# Slot: har_offisiell_adresse 


_Offisiell adresse for den ytre inngangen eller brukseininga._





URI: [ngre:harOffisiellAdresse](https://data.norge.no/vocabulary/ngr-eiendom#harOffisiellAdresse)
Alias: har_offisiell_adresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [YtreInngang](ytreinngang.md) | Ytre inngang til ein bygning |  yes  |
| [Bruksenhet](bruksenhet.md) | Ei brukseining (leilegheit, kontor o |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OffisiellAdresse](offisielladresse.md) |
| Domain Of | [YtreInngang](ytreinngang.md), [Bruksenhet](bruksenhet.md) |
| Slot URI | [ngre:harOffisiellAdresse](https://data.norge.no/vocabulary/ngr-eiendom#harOffisiellAdresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:harOffisiellAdresse |
| native | https://data.norge.no/linkml/ngr-eiendom/har_offisiell_adresse |




## LinkML Source

<details>
```yaml
name: har_offisiell_adresse
description: Offisiell adresse for den ytre inngangen eller brukseininga.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:harOffisiellAdresse
alias: har_offisiell_adresse
domain_of:
- YtreInngang
- Bruksenhet
range: OffisiellAdresse

```
</details>