# Enum: DqvMotivasjon 




_Gyldige motivasjonsverdiar for kvalitetsmerknader per DQV-AP-NO og dqvno-vokabularet._



URI: [https://data.norge.no/ap-no/dqv-core/DqvMotivasjon](https://data.norge.no/ap-no/dqv-core/DqvMotivasjon)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| assessing | oa:assessing | Allgemein vurdering av kvalitet |
| classifying | oa:classifying | Klassifisering av kvalitet |
| availability | dqvno:availability | Tilgjengelegheit |
| completeness | dqvno:completeness | Fullstendigheit |
| currentness | dqvno:currentness | Aktualitet |
| validity | dqvno:validity | Gyldighet |
| accuracy | dqvno:accuracy | Nøyaktigheit |




## Slots

| Name | Description |
| ---  | --- |
| [er_motivert_av](er_motivert_av.md) | Motivasjonen bak kvalitetsmerknaden |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-core






## LinkML Source

<details>
```yaml
name: DqvMotivasjon
description: Gyldige motivasjonsverdiar for kvalitetsmerknader per DQV-AP-NO og dqvno-vokabularet.
from_schema: https://data.norge.no/ap-no/dqv-core
permissible_values:
  assessing:
    text: assessing
    description: Allgemein vurdering av kvalitet.
    meaning: oa:assessing
  classifying:
    text: classifying
    description: Klassifisering av kvalitet.
    meaning: oa:classifying
  availability:
    text: availability
    description: Tilgjengelegheit.
    meaning: dqvno:availability
  completeness:
    text: completeness
    description: Fullstendigheit.
    meaning: dqvno:completeness
  currentness:
    text: currentness
    description: Aktualitet.
    meaning: dqvno:currentness
  validity:
    text: validity
    description: Gyldighet.
    meaning: dqvno:validity
  accuracy:
    text: accuracy
    description: Nøyaktigheit.
    meaning: dqvno:accuracy

```
</details>