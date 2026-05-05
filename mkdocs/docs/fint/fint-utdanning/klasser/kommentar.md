

# Slot: kommentar 



URI: [https://schema.fintlabs.no/utdanning/:kommentar](https://schema.fintlabs.no/utdanning/:kommentar)
Alias: kommentar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |
| [Sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [FagvurderingAbstrakt](fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |  no  |
| [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md) | Abstrakt basisklasse for ordensvurderingar |  no  |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [Underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [FagvurderingAbstrakt](fagvurderingabstrakt.md), [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md), [Fraversregistrering](fraversregistrering.md) |

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