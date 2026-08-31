

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/felles/brreg-felles-tid/id](https://data.norge.no/felles/brreg-felles-tid/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsperiode](tidsperiode.md) | Ei tidsperiode avgrensa av ein frå- og til-dato. |  no  |
| [TidsperiodeDatoKlokkeslett](tidsperiodedatoklokkeslett.md) | Ei tidsperiode avgrensa av frå- og til-tidspunkt (dato og klokkeslett). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Tidsperiode](tidsperiode.md), [TidsperiodeDatoKlokkeslett](tidsperiodedatoklokkeslett.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-tid




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/felles/brreg-felles-tid/id |
| native | https://data.norge.no/felles/brreg-felles-tid/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/felles/brreg-felles-tid
identifier: true
domain_of:
- Tidsperiode
- TidsperiodeDatoKlokkeslett
range: uriorcurie
required: true

```
</details>