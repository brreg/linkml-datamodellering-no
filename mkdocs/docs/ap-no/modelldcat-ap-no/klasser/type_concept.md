

# Slot: type_concept 


_Type ressurs frå eit kontrollert vokabular (dct:type)._





URI: [dct:type](http://purl.org/dc/terms/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Lisensdokument](lisensdokument.md) | Eit lisensdokument (dct:LicenseDocument) |  no  |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modellkatalog (modelldcatno:... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Aktor](aktor.md), [Lisensdokument](lisensdokument.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [dct:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:type |
| native | https://data.norge.no/ap-no/common-ap-no/type_concept |




## LinkML Source

<details>
```yaml
name: type_concept
description: Type ressurs frå eit kontrollert vokabular (dct:type).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:type
domain_of:
- Aktor
- Lisensdokument
- Informasjonsmodell
range: Konsept

```
</details>