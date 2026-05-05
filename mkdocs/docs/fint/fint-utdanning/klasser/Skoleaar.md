

# Slot: skoleaar 



URI: [https://schema.fintlabs.no/utdanning/:skoleaar](https://schema.fintlabs.no/utdanning/:skoleaar)
Alias: skoleaar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |
| [Sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [FagvurderingAbstrakt](fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |  no  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md) | Abstrakt basisklasse for ordensvurderingar |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [Anmerkninger](anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Klasse](klasse.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Persongruppe](persongruppe.md), [Faggruppe](faggruppe.md), [Undervisningsgruppe](undervisningsgruppe.md), [FagvurderingAbstrakt](fagvurderingabstrakt.md), [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md), [Anmerkninger](anmerkninger.md), [Eksamensgruppe](eksamensgruppe.md) |

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