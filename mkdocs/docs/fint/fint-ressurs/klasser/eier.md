

# Slot: eier 


_Referanse til Organisasjonselement som har eigarskap._





URI: [res:eier](https://schema.fintlabs.no/ressurs/eier)
Alias: eier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  yes  |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Applikasjonsressurs](applikasjonsressurs.md), [DigitalEnhet](digitalenhet.md) |
| Slot URI | [res:eier](https://schema.fintlabs.no/ressurs/eier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:eier |
| native | https://schema.fintlabs.no/ressurs/:eier |




## LinkML Source

<details>
```yaml
name: eier
description: Referanse til Organisasjonselement som har eigarskap.
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:eier
alias: eier
domain_of:
- Applikasjonsressurs
- DigitalEnhet
range: uriorcurie

```
</details>