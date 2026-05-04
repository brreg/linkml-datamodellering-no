

# Slot: identifikasjonstype 


_Type utanlandsk identifikasjon (t.d. DUF-nummer, tax identification)._





URI: [ngrp:identifikasjonstype](https://data.norge.no/vocabulary/ngr-person#identifikasjonstype)
Alias: identifikasjonstype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personidentifikasjon](Personidentifikasjon.md) | Utanlandsk eller alternativ identifikasjon av ein person, t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Personidentifikasjon](Personidentifikasjon.md) |
| Slot URI | [ngrp:identifikasjonstype](https://data.norge.no/vocabulary/ngr-person#identifikasjonstype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:identifikasjonstype |
| native | https://data.norge.no/linkml/ngr-person/identifikasjonstype |




## LinkML Source

<details>
```yaml
name: identifikasjonstype
description: Type utanlandsk identifikasjon (t.d. DUF-nummer, tax identification).
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:identifikasjonstype
alias: identifikasjonstype
domain_of:
- Personidentifikasjon
range: string

```
</details>