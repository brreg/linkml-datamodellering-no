

# Slot: heimeside 


_Heimeside for ressursen eller organisasjonen (foaf:homepage)._





URI: [foaf:homepage](http://xmlns.com/foaf/0.1/homepage)
Alias: heimeside

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |
| [Modelkatalog](modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Modelkatalog](modelkatalog.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [foaf:homepage](http://xmlns.com/foaf/0.1/homepage) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:homepage |
| native | https://data.norge.no/linkml/common-ap-no/heimeside |




## LinkML Source

<details>
```yaml
name: heimeside
description: Heimeside for ressursen eller organisasjonen (foaf:homepage).
from_schema: https://data.norge.no/linkml/common-ap-no
slot_uri: foaf:homepage
alias: heimeside
domain_of:
- Modelkatalog
- Informasjonsmodell
range: uri
multivalued: true

```
</details>