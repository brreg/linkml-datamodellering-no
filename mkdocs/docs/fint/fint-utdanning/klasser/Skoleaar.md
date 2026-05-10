

# Slot: skoleaar 


_Skoleåret._





URI: [utd:skoleaar](https://schema.fintlabs.no/utdanning/skoleaar)
Alias: skoleaar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |
| [FagvurderingAbstrakt](fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |  yes  |
| [Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [Halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  yes  |
| [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md) | Abstrakt basisklasse for ordensvurderingar |  yes  |
| [Anmerkninger](anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |  yes  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  yes  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  yes  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  yes  |
| [Sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  yes  |
| [Underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skoleaar](skoleaar.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Klasse](klasse.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Persongruppe](persongruppe.md), [Faggruppe](faggruppe.md), [Undervisningsgruppe](undervisningsgruppe.md), [FagvurderingAbstrakt](fagvurderingabstrakt.md), [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md), [Anmerkninger](anmerkninger.md), [Eksamensgruppe](eksamensgruppe.md) |
| Slot URI | [utd:skoleaar](https://schema.fintlabs.no/utdanning/skoleaar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:skoleaar |
| native | https://schema.fintlabs.no/utdanning/:skoleaar |




## LinkML Source

<details>
```yaml
name: skoleaar
description: Skoleåret.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:skoleaar
alias: skoleaar
domain_of:
- UtdanningContainer
- Elevforhold
- Klasse
- Kontaktlaerergruppe
- Persongruppe
- Faggruppe
- Undervisningsgruppe
- FagvurderingAbstrakt
- OrdensvurderingAbstrakt
- Anmerkninger
- Eksamensgruppe
range: Skoleaar

```
</details>