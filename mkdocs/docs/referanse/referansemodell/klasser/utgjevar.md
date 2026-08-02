

# Slot: utgjevar 


_Organisasjon ansvarleg for ressursen (referert med URI)._





URI: [dct:publisher](http://purl.org/dc/terms/publisher)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Ressurs](ressurs.md) | Ein generisk ressurs med tittel, skildring og utgjevar. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Ressurs](ressurs.md) |
| Slot URI | [dct:publisher](http://purl.org/dc/terms/publisher) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/referansemodell




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:publisher |
| native | https://data.norge.no/linkml/referansemodell/utgjevar |




## LinkML Source

<details>
```yaml
name: utgjevar
description: Organisasjon ansvarleg for ressursen (referert med URI).
from_schema: https://data.norge.no/linkml/referansemodell
slot_uri: dct:publisher
domain_of:
- Ressurs
range: uriorcurie

```
</details>