

# Slot: grepreferanse 


_Referanse til GREP-registeret._





URI: [utd:grepreferanse](https://schema.fintlabs.no/utdanning/grepreferanse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  yes  |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  yes  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  yes  |
| [Fag](fag.md) | Eit skulefag |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Arstrinn](arstrinn.md), [Programomrade](programomrade.md), [Utdanningsprogram](utdanningsprogram.md), [Fag](fag.md) |
| Slot URI | [utd:grepreferanse](https://schema.fintlabs.no/utdanning/grepreferanse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:grepreferanse |
| native | https://schema.fintlabs.no/utdanning/:grepreferanse |




## LinkML Source

<details>
```yaml
name: grepreferanse
description: Referanse til GREP-registeret.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:grepreferanse
domain_of:
- Arstrinn
- Programomrade
- Utdanningsprogram
- Fag
range: uriorcurie

```
</details>