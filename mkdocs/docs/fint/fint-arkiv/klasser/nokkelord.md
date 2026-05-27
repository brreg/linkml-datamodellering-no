

# Slot: nokkelord 


_Nøkkelord som skildrar innhaldet (Registrering)._





URI: [ark:nokkelord](https://schema.fintlabs.no/arkiv/nokkelord)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Registrering](registrering.md) |
| Slot URI | [ark:nokkelord](https://schema.fintlabs.no/arkiv/nokkelord) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:nokkelord |
| native | https://schema.fintlabs.no/arkiv/:nokkelord |




## LinkML Source

<details>
```yaml
name: nokkelord
description: Nøkkelord som skildrar innhaldet (Registrering).
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:nokkelord
domain_of:
- Registrering
range: string
multivalued: true

```
</details>