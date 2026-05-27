

# Slot: avskrivningsdato 


_Dato og klokkeslett for avskrivinga._





URI: [ark:avskrivningsdato](https://schema.fintlabs.no/arkiv/avskrivningsdato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Avskrivning](avskrivning.md) | Avskriving av ein journalpost (markering som ferdigbehandla) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Avskrivning](avskrivning.md) |
| Slot URI | [ark:avskrivningsdato](https://schema.fintlabs.no/arkiv/avskrivningsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:avskrivningsdato |
| native | https://schema.fintlabs.no/arkiv/:avskrivningsdato |




## LinkML Source

<details>
```yaml
name: avskrivningsdato
description: Dato og klokkeslett for avskrivinga.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:avskrivningsdato
domain_of:
- Avskrivning
range: datetime

```
</details>