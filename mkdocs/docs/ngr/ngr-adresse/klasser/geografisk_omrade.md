

# Slot: geografisk_omrade 


_Geografiske inndelingar (kommune, poststed, grunnkrets osv.) adressa ligg i._





URI: [ngr:referererTilGeografiskOmrade](https://data.norge.no/vocabulary/ngr-adresse#referererTilGeografiskOmrade)
Alias: geografisk_omrade

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](OffisiellAdresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeografiskOmrade](GeografiskOmrade.md) |
| Domain Of | [OffisiellAdresse](OffisiellAdresse.md) |
| Slot URI | [ngr:referererTilGeografiskOmrade](https://data.norge.no/vocabulary/ngr-adresse#referererTilGeografiskOmrade) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:referererTilGeografiskOmrade |
| native | https://data.norge.no/linkml/ngr-adresse/geografisk_omrade |




## LinkML Source

<details>
```yaml
name: geografisk_omrade
description: Geografiske inndelingar (kommune, poststed, grunnkrets osv.) adressa
  ligg i.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:referererTilGeografiskOmrade
alias: geografisk_omrade
domain_of:
- OffisiellAdresse
range: GeografiskOmrade
multivalued: true

```
</details>