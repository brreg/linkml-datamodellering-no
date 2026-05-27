

# Slot: kontaktpunkt_vcard 


_Kontaktpunkt (vCard) for omgrepet eller samlinga (dcat:contactPoint)._





URI: [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Eit omgrep med definisjon og tilhøyrande metadata (skos:Concept) |  yes  |
| [Samling](samling.md) | Ei namngitt samling av omgrep (skos:Collection) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VCardKontakt](vcardkontakt.md) |
| Domain Of | [Begrep](begrep.md), [Samling](samling.md) |
| Slot URI | [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:contactPoint |
| native | https://data.norge.no/ap-no/skos-ap-no/kontaktpunkt_vcard |




## LinkML Source

<details>
```yaml
name: kontaktpunkt_vcard
description: Kontaktpunkt (vCard) for omgrepet eller samlinga (dcat:contactPoint).
from_schema: https://data.norge.no/ap-no/skos-ap-no
rank: 1000
slot_uri: dcat:contactPoint
domain_of:
- Begrep
- Samling
range: VCardKontakt
multivalued: true

```
</details>