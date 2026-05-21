

# Slot: adresse_ref 


_Postadresse knytt til aktøren._





URI: [locn:address](http://www.w3.org/ns/locn#address)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktor](aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |  yes  |
| [OffentligOrganisasjon](offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Aktor](aktor.md) |
| Slot URI | [locn:address](http://www.w3.org/ns/locn#address) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:address |
| native | https://data.norge.no/linkml/cpsv-ap-no/adresse_ref |




## LinkML Source

<details>
```yaml
name: adresse_ref
description: Postadresse knytt til aktøren.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: locn:address
domain_of:
- Aktor
range: Adresse

```
</details>