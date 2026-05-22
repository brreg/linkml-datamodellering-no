# mcp-linkml-validator

MCP-server for policy-basert validering av LinkML-skjema.

Valideringa køyrer i tre steg, men **lint og instansvalidering køyrer berre éin gong — på bronsenivå**. Silver og gull arvar bronse og legg berre til fleire policy-sjekkar; dei køyrer ikkje lint eller instansvalidering på nytt.

| Steg | Bronze | Silver | Gold |
|---|---|---|---|
| Lint skjema (`linkml lint --validate`) | ✓ | — | — |
| Valider instans mot skjema | ✓ | — | — |
| Policy-sjekkar | bronse | bronse + sølv | bronse + sølv + gull |

## Bruk

```bash
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=gold
```

## Medaljongnivå

Kvart nivå arvar alle krav frå lågare nivå. Brot på eit nivå gir alltid `error` for det nivået — unntaket er åtvarslane på bronse som blir oppgradert til `error` på gull.

---

### Bronse

Grunnleggjande strukturkrav. Eit skjema som passerer bronse er syntaktisk korrekt og har nødvendig metadata.

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `schema.id` er ein HTTP(S)-URI | `schema_id_is_http_uri` |
| **error** | `schema.id` er til stades | `missing_required_metadata` |
| **error** | `schema.name` er til stades | `missing_required_metadata` |
| warning | `schema.description` er til stades | `missing_recommended_metadata` |
| warning | `schema.title` er til stades | `missing_recommended_metadata` |
| warning | `schema.version` er til stades | `missing_recommended_metadata` |
| warning | `class.description` er til stades for alle klasser | `missing_recommended_metadata` |
| warning | `slot.description` er til stades for alle slots | `missing_recommended_metadata` |
| warning | Alle klasser (unntatt `tree_root`) har `class_uri` | `all_classes_have_class_uri` |
| warning | Alle globale slots har `slot_uri` | `all_slots_have_slot_uri` |
| warning | Alle klasser (unntatt `tree_root`) har ein slot med `identifier: true` | `all_classes_have_identifier` |
| warning | Alle klasser (unntatt `tree_root`) har `annotations.begrepsidentifikator` som peikar på `https://data.norge.no/concepts/…` | `all_classes_have_concept_ref` |

---

### Sølv

Arvar bronse. Legg til krav frå DCAT-AP-NO 2 og DQV-AP-NO for domenemodeller i norsk offentleg sektor.

Alle brot på sølv-krav gir `error`.

**Klasse-slot-krav (obligatoriske per DCAT-AP-NO / DQV-AP-NO):**

| Klasse | Påkravd slot (`slot_uri`) |
|---|---|
| `Katalog` | `dct:title`, `dct:description`, `dcat:contactPoint`, `dct:publisher` |
| `Katalogpost` | `dct:modified`, `foaf:primaryTopic` |
| `Datasett` | `dct:title`, `dct:description`, `dcat:contactPoint`, `dcat:theme`, `dct:publisher` |
| `Distribusjon` | `dcat:accessURL` |
| `Datatjeneste` | `dcat:endpointURL`, `dcat:contactPoint`, `dct:title`, `dct:publisher` |
| `Aktør` | `foaf:name` |

**Containerklasse-krav:**

| Alvor | Krav |
|---|---|
| **error** | Containerklassen (`tree_root`) har attributt med range `Katalog`, `Datasett`, `Kvalitetsmaal`, `Kvalitetsmaaling` |
| warning | Containerklassen har attributt med range `Distribusjon`, `Datatjeneste`, `Kvalitetsdimensjon`, `Kvalitetsmerknad` |

---

### Gull

Arvar sølv og bronse. Implementerer FAIR-prinsippa (Findable, Accessible, Interoperable, Reusable). Alle brot gir `error` — også dei som er åtvarslane på bronse.

| FAIR | Krav | Kode |
|---|---|---|
| F1 | `schema.id` er HTTP(S)-URI *(arva frå bronse, oppgradert til error)* | `schema_id_is_http_uri` |
| F2 | `schema.title` er til stades | `fair_f2` |
| F3 | Alle klasser (unntatt `tree_root`) har `class_uri` *(arva frå bronse, oppgradert til error)* | `all_classes_have_class_uri` |
| F4 | `schema.version` er til stades | `fair_f4` |
| I1 | Alle globale slots har `slot_uri` *(arva frå bronse, oppgradert til error)* | `all_slots_have_slot_uri` |
| I2 | Skjemaet deklarerer minst eitt standard vokabularprefiks (`dct`, `dcat`, `skos`, `prov`, `rdf`, `rdfs`, `owl`, `foaf`, `xsd`) | `fair_i2` |
| R1.1 | Skjemaet har ein slot med `dct:license` | `fair_r11` |
| R1.2 | Skjemaet har ein slot for proveniens (`prov:wasAttributedTo`, `prov:wasGeneratedBy`, `dct:creator`, `dct:publisher` eller `dct:contributor`) | `fair_r12` |

---

## Policyarv

```
bronze
  └── silver  (extends: bronze)
        └── gold  (extends: silver)
```

`make mcp-validate POLICY=gold` køyrer alle bronse-, sølv- og gull-krav i éin gjennomgang.

## MCP-verktøy

| Verktøy | Skildring |
|---|---|
| `validate_linkml_schema` | Validerer eit skjema med lint + instansvalidering + policy-sjekkar. Parametrar: `schemaText` (påkravd), `policy` (standard: `bronze`), `instanceText` (valfri). |
| `validate_linkml_instance` | Validerer ein instans mot eit skjema. Tilsvarar `linkml validate --schema`. Parametrar: `schemaText`, `instanceText`, `targetClass` (valfri). |
