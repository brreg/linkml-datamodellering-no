

# Slot: mottar_post_paa 


_Adressa personen mottar post på._





URI: [ngrp:mottarPostPaa](https://data.norge.no/vocabulary/ngr-person#mottarPostPaa)
Alias: mottar_post_paa

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Postadresse](Postadresse.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [ngrp:mottarPostPaa](https://data.norge.no/vocabulary/ngr-person#mottarPostPaa) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:mottarPostPaa |
| native | https://data.norge.no/linkml/ngr-person/mottar_post_paa |




## LinkML Source

<details>
```yaml
name: mottar_post_paa
description: Adressa personen mottar post på.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:mottarPostPaa
alias: mottar_post_paa
domain_of:
- Person
range: Postadresse

```
</details>