

# Slot: kontaktpunkt 


_Kontaktinformasjon for ressursen (dcat:contactPoint)._





URI: [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint)
Alias: kontaktpunkt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modelkatalog](Modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |
| [Informasjonsmodell](Informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktopplysning](Kontaktopplysning.md) |
| Domain Of | [Modelkatalog](Modelkatalog.md), [Informasjonsmodell](Informasjonsmodell.md) |
| Slot URI | [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:contactPoint |
| native | https://data.norge.no/linkml/modelldcat-ap-no/kontaktpunkt |




## LinkML Source

<details>
```yaml
name: kontaktpunkt
description: Kontaktinformasjon for ressursen (dcat:contactPoint).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dcat:contactPoint
alias: kontaktpunkt
domain_of:
- Modelkatalog
- Informasjonsmodell
range: Kontaktopplysning
multivalued: true

```
</details>