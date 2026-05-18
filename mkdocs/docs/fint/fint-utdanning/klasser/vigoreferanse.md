

# Slot: vigoreferanse 


_Referanse til Vigo-systemet._





URI: [utd:vigoreferanse](https://schema.fintlabs.no/utdanning/vigoreferanse)
Alias: vigoreferanse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  yes  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  yes  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |  yes  |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Skole](skole.md), [Arstrinn](arstrinn.md), [Programomrade](programomrade.md), [Utdanningsprogram](utdanningsprogram.md), [Fag](fag.md), [Karakterskala](karakterskala.md) |
| Slot URI | [utd:vigoreferanse](https://schema.fintlabs.no/utdanning/vigoreferanse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:vigoreferanse |
| native | https://schema.fintlabs.no/utdanning/:vigoreferanse |




## LinkML Source

<details>
```yaml
name: vigoreferanse
description: Referanse til Vigo-systemet.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:vigoreferanse
alias: vigoreferanse
domain_of:
- Skole
- Arstrinn
- Programomrade
- Utdanningsprogram
- Fag
- Karakterskala
range: uriorcurie

```
</details>