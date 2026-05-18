

# Slot: personalressurs 


_Referanse til Personalressurs i Administrasjon-domenet._





URI: [utd:personalressurs](https://schema.fintlabs.no/utdanning/personalressurs)
Alias: personalressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skoleressurs](skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  yes  |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Person](person.md), [Skoleressurs](skoleressurs.md) |
| Slot URI | [utd:personalressurs](https://schema.fintlabs.no/utdanning/personalressurs) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:personalressurs |
| native | https://schema.fintlabs.no/utdanning/:personalressurs |




## LinkML Source

<details>
```yaml
name: personalressurs
description: Referanse til Personalressurs i Administrasjon-domenet.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:personalressurs
alias: personalressurs
domain_of:
- Person
- Skoleressurs
range: uriorcurie

```
</details>