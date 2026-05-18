

# Slot: personalressurs 


_Referanse til Personalressurs (Administrasjon)._





URI: [res:personalressurs](https://schema.fintlabs.no/ressurs/personalressurs)
Alias: personalressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |
| [Identitet](identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |  yes  |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Person](person.md), [DigitalEnhet](digitalenhet.md), [Identitet](identitet.md) |
| Slot URI | [res:personalressurs](https://schema.fintlabs.no/ressurs/personalressurs) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:personalressurs |
| native | https://schema.fintlabs.no/ressurs/:personalressurs |




## LinkML Source

<details>
```yaml
name: personalressurs
description: Referanse til Personalressurs (Administrasjon).
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:personalressurs
alias: personalressurs
domain_of:
- Person
- DigitalEnhet
- Identitet
range: uriorcurie

```
</details>