

# Slot: navn 


_Hovudnamn for ressursen._





URI: [fint:navn](https://schema.fintlabs.no/navn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  yes  |
| [Leverandorgruppe](leverandorgruppe.md) | Gruppering av leverandørar |  yes  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  yes  |
| [Merverdiavgift](merverdiavgift.md) | Kodeverk for merverdiavgifter |  yes  |
| [OkonomiValuta](okonomivaluta.md) | Valuta for transaksjonsbeløp |  yes  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Begrep](begrep.md), [Fakturautsteder](fakturautsteder.md), [Leverandorgruppe](leverandorgruppe.md), [Vare](vare.md), [Merverdiavgift](merverdiavgift.md), [OkonomiValuta](okonomivaluta.md) |
| Slot URI | [fint:navn](https://schema.fintlabs.no/navn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:navn |
| native | https://schema.fintlabs.no/:navn |




## LinkML Source

<details>
```yaml
name: navn
description: Hovudnamn for ressursen.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:navn
domain_of:
- Begrep
- Fakturautsteder
- Leverandorgruppe
- Vare
- Merverdiavgift
- OkonomiValuta
range: string

```
</details>