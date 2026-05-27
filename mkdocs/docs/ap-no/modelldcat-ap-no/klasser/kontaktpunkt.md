

# Slot: kontaktpunkt 


_Kontaktinformasjon for ressursen (dcat:contactPoint)._





URI: [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modellkatalog](modellkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modellkatalog (modelldcatno:... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktopplysning](kontaktopplysning.md) |
| Domain Of | [Modellkatalog](modellkatalog.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:contactPoint |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/kontaktpunkt |




## LinkML Source

<details>
```yaml
name: kontaktpunkt
description: Kontaktinformasjon for ressursen (dcat:contactPoint).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_uri: dcat:contactPoint
domain_of:
- Modellkatalog
- Informasjonsmodell
range: Kontaktopplysning
multivalued: true

```
</details>