

# Slot: er_medlem_av 


_Samling dette omgrepet er medlem av (uneskos:memberOf)._





URI: [uneskos:memberOf](http://purl.org/umu/uneskos#memberOf)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Eit omgrep med definisjon og tilhøyrande metadata (skos:Concept) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Samling](samling.md) |
| Domain Of | [Begrep](begrep.md) |
| Slot URI | [uneskos:memberOf](http://purl.org/umu/uneskos#memberOf) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | uneskos:memberOf |
| native | https://data.norge.no/ap-no/skos-ap-no/er_medlem_av |




## LinkML Source

<details>
```yaml
name: er_medlem_av
description: Samling dette omgrepet er medlem av (uneskos:memberOf).
from_schema: https://data.norge.no/ap-no/skos-ap-no
rank: 1000
slot_uri: uneskos:memberOf
domain_of:
- Begrep
range: Samling
multivalued: true

```
</details>