

# Slot: beskrivelse 


_Beskriven namn eller omtale._





URI: [fint:beskrivelse](https://schema.fintlabs.no/beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  yes  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |
| [Rolle](rolle.md) | Rettighet eller type fullmakt |  yes  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Periode](periode.md), [Lonn](lonn.md), [Rolle](rolle.md) |
| Slot URI | [fint:beskrivelse](https://schema.fintlabs.no/beskrivelse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:beskrivelse |
| native | https://schema.fintlabs.no/:beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
description: Beskriven namn eller omtale.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:beskrivelse
alias: beskrivelse
domain_of:
- Periode
- Lonn
- Rolle
range: string

```
</details>