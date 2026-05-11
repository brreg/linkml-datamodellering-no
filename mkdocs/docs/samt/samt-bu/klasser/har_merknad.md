

# Slot: har_merknad 


_Fritekstmerknad (rdfs:comment)._





URI: [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment)
Alias: har_merknad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsmaaling](kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |  yes  |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  yes  |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  yes  |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Kvalitetsmerknad](kvalitetsmerknad.md), [Kvalitetsmaaling](kvalitetsmaaling.md), [Standard](standard.md) |
| Slot URI | [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:comment |
| native | https://data.norge.no/linkml/common-ap-no/har_merknad |




## LinkML Source

<details>
```yaml
name: har_merknad
description: Fritekstmerknad (rdfs:comment).
from_schema: https://data.norge.no/linkml/common-ap-no
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