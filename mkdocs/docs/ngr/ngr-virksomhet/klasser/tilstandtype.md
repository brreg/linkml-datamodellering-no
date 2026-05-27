# Enum: TilstandType 




_Status for ei verksemd registrert i Enhetsregisteret._



URI: [https://data.norge.no/ngr/ngr-virksomhet/TilstandType](https://data.norge.no/ngr/ngr-virksomhet/TilstandType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| AKTIV | None | Aktiv og registrert eining |
| UNDER_TVANGSAVVIKLING | None | Under tvangsavvikling |
| UNDER_KONKURS | None | Under konkursbehandling |
| AVVIKLET | None | Avvikla |
| SLETTET | None | Sletta frå registeret |
| OPPLØST | None | Oppløyst |




## Slots

| Name | Description |
| ---  | --- |
| [tilstandstype](tilstandstype.md) | Type tilstand (AKTIV, UNDER_KONKURS o |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet






## LinkML Source

<details>
```yaml
name: TilstandType
description: Status for ei verksemd registrert i Enhetsregisteret.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
permissible_values:
  AKTIV:
    text: AKTIV
    description: Aktiv og registrert eining
  UNDER_TVANGSAVVIKLING:
    text: UNDER_TVANGSAVVIKLING
    description: Under tvangsavvikling
  UNDER_KONKURS:
    text: UNDER_KONKURS
    description: Under konkursbehandling
  AVVIKLET:
    text: AVVIKLET
    description: Avvikla
  SLETTET:
    text: SLETTET
    description: Sletta frå registeret
  OPPLØST:
    text: OPPLØST
    description: Oppløyst

```
</details>