

# Slot: skoleaar 



URI: [https://schema.fintlabs.no/utdanning/:skoleaar](https://schema.fintlabs.no/utdanning/:skoleaar)
Alias: skoleaar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sluttordensvurdering](Sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [Eksamensgruppe](Eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Underveisfagvurdering](Underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [Persongruppe](Persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Klasse](Klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Anmerkninger](Anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |  no  |
| [FagvurderingAbstrakt](FagvurderingAbstrakt.md) | Abstrakt basisklasse for fagvurderingar |  no  |
| [Kontaktlaerergruppe](Kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Underveisordensvurdering](Underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Halvaarsordensvurdering](Halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [Eksamensvurdering](Eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Faggruppe](Faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [Undervisningsgruppe](Undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [OrdensvurderingAbstrakt](OrdensvurderingAbstrakt.md) | Abstrakt basisklasse for ordensvurderingar |  no  |
| [Halvaarsfagvurdering](Halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Sluttfagvurdering](Sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Elevforhold](Elevforhold.md), [Klasse](Klasse.md), [Kontaktlaerergruppe](Kontaktlaerergruppe.md), [Persongruppe](Persongruppe.md), [Faggruppe](Faggruppe.md), [Undervisningsgruppe](Undervisningsgruppe.md), [FagvurderingAbstrakt](FagvurderingAbstrakt.md), [OrdensvurderingAbstrakt](OrdensvurderingAbstrakt.md), [Anmerkninger](Anmerkninger.md), [Eksamensgruppe](Eksamensgruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:skoleaar |
| native | https://schema.fintlabs.no/utdanning/:skoleaar |




## LinkML Source

<details>
```yaml
name: skoleaar
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
range: string

```
</details>