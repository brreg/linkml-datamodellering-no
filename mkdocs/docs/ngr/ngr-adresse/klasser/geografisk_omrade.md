

# Slot: geografisk_omrade 


_Geografiske inndelingar (kommune, poststed, grunnkrets osv.) adressa ligg i._





URI: [ngr:referererTilGeografiskOmrade](https://data.norge.no/vocabulary/ngr-adresse#referererTilGeografiskOmrade)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](offisielladresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeografiskOmrade](geografiskomrade.md) |
| Domain Of | [OffisiellAdresse](offisielladresse.md) |
| Slot URI | [ngr:referererTilGeografiskOmrade](https://data.norge.no/vocabulary/ngr-adresse#referererTilGeografiskOmrade) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:referererTilGeografiskOmrade |
| native | https://data.norge.no/ngr/ngr-adresse/geografisk_omrade |




## LinkML Source

<details>
```yaml
name: geografisk_omrade
description: Geografiske inndelingar (kommune, poststed, grunnkrets osv.) adressa
  ligg i.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: ngr:referererTilGeografiskOmrade
domain_of:
- OffisiellAdresse
range: GeografiskOmrade
multivalued: true

```
</details>