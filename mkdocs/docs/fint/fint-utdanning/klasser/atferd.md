

# Slot: atferd 


_Åtferdskarakter._





URI: [utd:atferd](https://schema.fintlabs.no/utdanning/atferd)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md) | Abstrakt basisklasse for ordensvurderingar |  yes  |
| [Anmerkninger](anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |  yes  |
| [Halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [Sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [Underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterverdi](karakterverdi.md) |
| Domain Of | [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md), [Anmerkninger](anmerkninger.md) |
| Slot URI | [utd:atferd](https://schema.fintlabs.no/utdanning/atferd) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:atferd |
| native | https://schema.fintlabs.no/utdanning/:atferd |




## LinkML Source

<details>
```yaml
name: atferd
description: Åtferdskarakter.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:atferd
domain_of:
- OrdensvurderingAbstrakt
- Anmerkninger
range: Karakterverdi

```
</details>