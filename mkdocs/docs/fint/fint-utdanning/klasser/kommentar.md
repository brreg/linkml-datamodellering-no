

# Slot: kommentar 



URI: [https://schema.fintlabs.no/utdanning/:kommentar](https://schema.fintlabs.no/utdanning/:kommentar)
Alias: kommentar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sluttordensvurdering](Sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [Underveisfagvurdering](Underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [Fraversregistrering](Fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |
| [FagvurderingAbstrakt](FagvurderingAbstrakt.md) | Abstrakt basisklasse for fagvurderingar |  no  |
| [Underveisordensvurdering](Underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |
| [Halvaarsordensvurdering](Halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [Eksamensvurdering](Eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Sluttfagvurdering](Sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [OrdensvurderingAbstrakt](OrdensvurderingAbstrakt.md) | Abstrakt basisklasse for ordensvurderingar |  no  |
| [Halvaarsfagvurdering](Halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FagvurderingAbstrakt](FagvurderingAbstrakt.md), [OrdensvurderingAbstrakt](OrdensvurderingAbstrakt.md), [Fraversregistrering](Fraversregistrering.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:kommentar |
| native | https://schema.fintlabs.no/utdanning/:kommentar |




## LinkML Source

<details>
```yaml
name: kommentar
alias: kommentar
domain_of:
- FagvurderingAbstrakt
- OrdensvurderingAbstrakt
- Fraversregistrering
range: string

```
</details>