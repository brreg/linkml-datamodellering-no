

# Slot: adressenavn_tekst 


_Tekstleg namn på vegen eller stadnamnet (locn:thoroughfare)._





URI: [locn:thoroughfare](http://www.w3.org/ns/locn#thoroughfare)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adressenavn](adressenavn.md) | Offisielt namn på ei veglenke eller eit adresseobjekt i ein kommune, tildelt ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Adressenavn](adressenavn.md) |
| Slot URI | [locn:thoroughfare](http://www.w3.org/ns/locn#thoroughfare) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:thoroughfare |
| native | https://data.norge.no/ngr/ngr-adresse/adressenavn_tekst |




## LinkML Source

<details>
```yaml
name: adressenavn_tekst
description: Tekstleg namn på vegen eller stadnamnet (locn:thoroughfare).
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: locn:thoroughfare
domain_of:
- Adressenavn
range: string

```
</details>