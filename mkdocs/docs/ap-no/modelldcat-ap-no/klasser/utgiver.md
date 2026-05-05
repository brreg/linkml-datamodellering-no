

# Slot: utgiver 


_Aktøren ansvarleg for å tilgjengeleggjere ressursen (dct:publisher)._





URI: [dct:publisher](http://purl.org/dc/terms/publisher)
Alias: utgiver

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
| Range | [Aktor](aktor.md) |
| Domain Of | [Modelkatalog](modelkatalog.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [dct:publisher](http://purl.org/dc/terms/publisher) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:publisher |
| native | https://data.norge.no/linkml/modelldcat-ap-no/utgiver |




## LinkML Source

<details>
```yaml
name: utgiver
description: Aktøren ansvarleg for å tilgjengeleggjere ressursen (dct:publisher).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dct:publisher
alias: utgiver
domain_of:
- Modelkatalog
- Informasjonsmodell
range: Aktor

```
</details>