

# Slot: vigoreferanse 


_Referanse til Vigo-systemet._





URI: [utd:vigoreferanse](https://schema.fintlabs.no/utdanning/vigoreferanse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  yes  |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  yes  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  yes  |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |  yes  |






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


* from schema: https://data.norge.no/fint/fint-utdanning




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
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:vigoreferanse
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