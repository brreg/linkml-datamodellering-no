

# Slot: prosjektart 



URI: [https://schema.fintlabs.no/administrasjon/:prosjektart](https://schema.fintlabs.no/administrasjon/:prosjektart)
Alias: prosjektart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](Kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Prosjekt](Prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Kontostreng](Kontostreng.md), [Prosjekt](Prosjekt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:prosjektart |
| native | https://schema.fintlabs.no/administrasjon/:prosjektart |




## LinkML Source

<details>
```yaml
name: prosjektart
alias: prosjektart
domain_of:
- Kontostreng
- Prosjekt
range: string

```
</details>