

# Slot: poststed_ref 


_Poststedet (postnummer) denne adressa høyrer til._





URI: [ngr:referererTilPoststed](https://data.norge.no/vocabulary/ngr-adresse#referererTilPoststed)
Alias: poststed_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postboksadresse](Postboksadresse.md) | Ei postboksadresse registrert i Postboksregisteret (Posten Norge) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Poststed](Poststed.md) |
| Domain Of | [Postboksadresse](Postboksadresse.md) |
| Slot URI | [ngr:referererTilPoststed](https://data.norge.no/vocabulary/ngr-adresse#referererTilPoststed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:referererTilPoststed |
| native | https://data.norge.no/linkml/ngr-adresse/poststed_ref |




## LinkML Source

<details>
```yaml
name: poststed_ref
description: Poststedet (postnummer) denne adressa høyrer til.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:referererTilPoststed
alias: poststed_ref
domain_of:
- Postboksadresse
range: Poststed

```
</details>