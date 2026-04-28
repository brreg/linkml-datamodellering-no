

# Slot: har_merknad 


_Fritekstmerknad (rdfs:comment)._





URI: [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment)
Alias: har_merknad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Standard](Standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  yes  |
| [Kvalitetsmerknad](Kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  yes  |
| [Brukartilbakemelding](Brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Kvalitetssertifikat](Kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |
| [Kvalitetsmaaling](Kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Kvalitetsmerknad](Kvalitetsmerknad.md), [Kvalitetsmaaling](Kvalitetsmaaling.md), [Standard](Standard.md) |
| Slot URI | [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:comment |
| native | https://data.norge.no/linkml/dqv-ap-no/har_merknad |




## LinkML Source

<details>
```yaml
name: har_merknad
description: Fritekstmerknad (rdfs:comment).
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: rdfs:comment
alias: har_merknad
domain_of:
- Kvalitetsmerknad
- Kvalitetsmaaling
- Standard
range: LangString
multivalued: true

```
</details>