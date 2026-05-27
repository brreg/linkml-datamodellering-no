

# Slot: personalressurs 


_Referanse til Personalressurs i Administrasjon-domenet._





URI: [ark:personalressurs](https://schema.fintlabs.no/arkiv/personalressurs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arkivressurs](arkivressurs.md) | Ansatt med rolle og rettar innanfor arkiv |  yes  |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  yes  |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Person](person.md), [Arkivressurs](arkivressurs.md), [Personalmappe](personalmappe.md) |
| Slot URI | [ark:personalressurs](https://schema.fintlabs.no/arkiv/personalressurs) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:personalressurs |
| native | https://schema.fintlabs.no/arkiv/:personalressurs |




## LinkML Source

<details>
```yaml
name: personalressurs
description: Referanse til Personalressurs i Administrasjon-domenet.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:personalressurs
domain_of:
- Person
- Arkivressurs
- Personalmappe
range: uriorcurie

```
</details>