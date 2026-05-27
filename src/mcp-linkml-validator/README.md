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
# Medaljongnivå:
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=gold

# Publisering — med datafil/instans:
make mcp-validate \
  SCHEMA=src/linkml/begrepskatalog/<katalog>/<katalog>-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=data/begrep/<katalog>.yaml

make mcp-validate \
  SCHEMA=src/linkml/modellkatalog/<katalog>/<katalog>-schema.yaml \
  POLICY=felles-datakatalog \
  INSTANCE=examples/modell/<katalog>-eksempel.yaml
```

## Medaljongnivå for datasett

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
| warning | Alle klasser (unntatt `tree_root`) har `annotations.begrepsidentifikator` som peikar på `https://concept-catalog.fellesdatakatalog.digdir.no/collections/…` | `all_classes_have_concept_ref` |

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

## Publiseringspolicyer

Domene-spesifikke policyer for publisering til nasjonale katalogar. Dei arvar `bronze`
og er meinte brukt i tillegg til medaljongnivåa — typisk i CI-pipelinen for skjema
som har ein tilhøyrande datafil.

---

### Felles Begrepskatalog (`felles-begrepskatalog`)

For begrepskatalogskjema som publiserer til [data.norge.no/concepts](https://data.norge.no/concepts)
via SKOS-AP-NO-Begrep. Sjå [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/) for full rettleiing.

**Import og prefiks:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Importerer `skos-ap-no-schema` | `schema_importerer_skos_ap_no` |
| **error** | Deklarerer `skos:`-prefix | `schema_brukar_skos_prefix` |
| **error** | Deklarerer `dct:`-prefix | `schema_brukar_dct_prefix` |

**Containerklasse:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Container har attributt med range `Begrep` | `container_har_begrep` |
| warning | Container har attributt med range `Samling` | `container_har_samling` |

**`Begrep`-krav (obligatoriske per SKOS-AP-NO-Begrep):**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `skos:prefLabel` | `begrep_har_anbefalt_term` |
| **error** | `skos:definition` eller `euvoc:xlDefinition` | `begrep_har_definisjon` |
| **error** | `dct:identifier` | `begrep_har_identifikator` |
| **error** | `dct:publisher` | `begrep_har_utgjevar` |
| **error** | `dcat:contactPoint` | `begrep_har_kontaktpunkt` |
| warning | `dct:subject` | `begrep_har_fagomrade` |
| warning | `dct:creator` | `begrep_har_ansvarleg_verksemd` |
| warning | `euvoc:startDate` | `begrep_har_gyldig_fra` |
| warning | `euvoc:endDate` | `begrep_har_gyldig_til` |
| warning | `dct:created` | `begrep_har_opprettingsdato` |
| warning | `dct:modified` | `begrep_har_endringsdato` |
| warning | `skos:scopeNote` | `begrep_har_merknad` |
| warning | `skos:altLabel` | `begrep_har_tillate_term` |

**`Definisjon`-, `AssosiativRelasjon`-, `GeneriskRelasjon`-, `PartitivRelasjon`- og `Samling`-krav** er dokumenterte i [`policies/felles-begrepskatalog.yaml`](policies/felles-begrepskatalog.yaml).

**Instanssjekk:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `dct:publisher`-verdi er `https://data.norge.no/organizations/<9-sifra orgnr>` og er i lista over kjende utgivarar | `utgjevar_er_kjend_org` |

---

### Felles Datakatalog (`felles-datakatalog`)

For modellkatalogskjema som publiserer til [data.norge.no/models](https://data.norge.no/models)
via ModelDCAT-AP-NO. Sjå [Publiser til Felles Datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-modell/) for full rettleiing.

**Import og prefiks:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Importerer `modelldcat-ap-no-schema` | `schema_importerer_modelldcat_ap_no` |
| **error** | Deklarerer `dct:`-prefix | `schema_brukar_dct_prefix` |
| **error** | Deklarerer `dcat:`-prefix | `schema_brukar_dcat_prefix` |

**Containerklasse:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Container har attributt med range `Modellkatalog` | `container_har_modellkatalog` |
| **error** | Container har attributt med range `Informasjonsmodell` | `container_har_informasjonsmodell` |

**`Modellkatalog`-krav (obligatoriske per ModelDCAT-AP-NO):**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `dct:title` | `modellkatalog_har_tittel` |
| **error** | `dct:description` | `modellkatalog_har_beskrivelse` |
| **error** | `dct:identifier` | `modellkatalog_har_identifikator` |
| **error** | `dct:publisher` | `modellkatalog_har_utgjevar` |
| **error** | `dcat:contactPoint` | `modellkatalog_har_kontaktpunkt` |
| **error** | `dct:hasPart` | `modellkatalog_har_del` |
| warning | `dct:license` | `modellkatalog_har_lisens` |
| warning | `modelldcatno:model` | `modellkatalog_har_modell` |

**`Informasjonsmodell`-krav (obligatoriske per ModelDCAT-AP-NO):**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `dct:title` | `informasjonsmodell_har_tittel` |
| **error** | `dct:publisher` | `informasjonsmodell_har_utgjevar` |
| warning | `dct:description` | `informasjonsmodell_har_beskrivelse` |
| warning | `dct:identifier` | `informasjonsmodell_har_identifikator` |
| warning | `modelldcatno:informationModelIdentifier` | `informasjonsmodell_har_modellidentifikator` |
| warning | `dcat:contactPoint` | `informasjonsmodell_har_kontaktpunkt` |
| warning | `dct:license` | `informasjonsmodell_har_lisens` |
| warning | `dcat:theme` | `informasjonsmodell_har_tema` |
| warning | `modelldcatno:containsModelElement` | `informasjonsmodell_har_modellelement` |

**Instanssjekk:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `dct:publisher`-verdi er `https://data.norge.no/organizations/<9-sifra orgnr>` og er i lista over kjende utgivarar | `utgjevar_er_kjend_org` |

---

## Policyarv

```
bronze
  ├── silver  (extends: bronze)
  │     └── gold  (extends: silver)
  ├── felles-begrepskatalog  (extends: bronze)
  └── felles-datakatalog  (extends: bronze)
```

`make mcp-validate POLICY=gold` køyrer alle bronse-, sølv- og gull-krav i éin gjennomgang.

Publiseringspolicyane er sidegreinar — dei arvar bronse, men ikkje sølv eller gull.
Bruk dei saman med medaljongnivåa for fullstendig dekning:

```bash
make mcp-validate SCHEMA=... POLICY=bronze
make mcp-validate SCHEMA=... POLICY=felles-begrepskatalog INSTANCE=...
```

## MCP-verktøy

| Verktøy | Skildring |
|---|---|
| `validate_linkml_schema` | Validerer eit skjema med lint + instansvalidering + policy-sjekkar. Parametrar: `schemaText` (påkravd), `policy` (standard: `bronze`), `instanceText` (valfri). |
| `validate_linkml_instance` | Validerer ein instans mot eit skjema. Tilsvarar `linkml validate --schema`. Parametrar: `schemaText`, `instanceText`, `targetClass` (valfri). |
