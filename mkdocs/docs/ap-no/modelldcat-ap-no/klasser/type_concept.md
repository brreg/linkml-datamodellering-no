

# Slot: type_concept 


_Type ressurs frå eit kontrollert vokabular (dct:type)._





URI: [dct:type](http://purl.org/dc/terms/type)
Alias: type_concept

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktor](Aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Informasjonsmodell](Informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |
| [Lisensdokument](Lisensdokument.md) | Eit lisensdokument (dct:LicenseDocument) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](Konsept.md) |
| Domain Of | [Aktor](Aktor.md), [Lisensdokument](Lisensdokument.md), [Informasjonsmodell](Informasjonsmodell.md) |
| Slot URI | [dct:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:type |
| native | https://data.norge.no/linkml/modelldcat-ap-no/type_concept |




## LinkML Source

<details>
```yaml
name: type_concept
description: Type ressurs frå eit kontrollert vokabular (dct:type).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dct:type
alias: type_concept
domain_of:
- Aktor
- Lisensdokument
- Informasjonsmodell
range: Konsept

```
</details>