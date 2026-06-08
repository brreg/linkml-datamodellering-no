

# Slot: heimeside 


_Heimeside for ressursen eller organisasjonen (foaf:homepage)._





URI: [foaf:homepage](http://xmlns.com/foaf/0.1/homepage)
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
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Modellkatalog](modellkatalog.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [foaf:homepage](http://xmlns.com/foaf/0.1/homepage) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:homepage |
| native | https://data.norge.no/ap-no/common-ap-no/heimeside |




## LinkML Source

<details>
```yaml
name: heimeside
description: Heimeside for ressursen eller organisasjonen (foaf:homepage).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: foaf:homepage
domain_of:
- Modellkatalog
- Informasjonsmodell
range: uri
multivalued: true

```
</details>