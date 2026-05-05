

# Slot: orden 



URI: [https://schema.fintlabs.no/utdanning/:orden](https://schema.fintlabs.no/utdanning/:orden)
Alias: orden

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [Sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md) | Abstrakt basisklasse for ordensvurderingar |  no  |
| [Anmerkninger](anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |  no  |
| [Underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md), [Anmerkninger](anmerkninger.md) |

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