

# Slot: orden 



URI: [https://schema.fintlabs.no/utdanning/:orden](https://schema.fintlabs.no/utdanning/:orden)
Alias: orden

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sluttordensvurdering](Sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [Underveisordensvurdering](Underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |
| [Halvaarsordensvurdering](Halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [OrdensvurderingAbstrakt](OrdensvurderingAbstrakt.md) | Abstrakt basisklasse for ordensvurderingar |  no  |
| [Anmerkninger](Anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OrdensvurderingAbstrakt](OrdensvurderingAbstrakt.md), [Anmerkninger](Anmerkninger.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:orden |
| native | https://schema.fintlabs.no/utdanning/:orden |




## LinkML Source

<details>
```yaml
name: orden
alias: orden
domain_of:
- OrdensvurderingAbstrakt
- Anmerkninger
range: string

```
</details>