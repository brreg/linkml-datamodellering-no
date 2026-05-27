# Enum: VarslingType 




_Kanaltype for varsling til verksemda._



URI: [https://data.norge.no/ngr/ngr-virksomhet/VarslingType](https://data.norge.no/ngr/ngr-virksomhet/VarslingType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| EPOST | None | Varsling via e-post |
| MOBILTELEFON | None | Varsling via SMS til mobiltelefon |




## Slots

| Name | Description |
| ---  | --- |
| [varslingstype](varslingstype.md) | Kanaltype for varsling (EPOST eller MOBILTELEFON) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet






## LinkML Source

<details>
```yaml
name: VarslingType
description: Kanaltype for varsling til verksemda.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
permissible_values:
  EPOST:
    text: EPOST
    description: Varsling via e-post
  MOBILTELEFON:
    text: MOBILTELEFON
    description: Varsling via SMS til mobiltelefon

```
</details>