# Plan: Oppdater mcp-linkml-validator README med publiseringspolicyer

## Mål

Oppdatere `src/mcp-linkml-validator/README.md` til å dokumentere dei to nye
publiseringspolicyane `felles-begrepskatalog` og `felles-datakatalog` slik at
brukarar forstår kva dei er for, korleis dei arvar frå `bronze`, og korleis dei
nyttast i praksis.

---

## Kva må leggjast til

README har i dag desse seksjonane:

1. Intro-avsnitt + tabell over steg
2. **Bruk** — `make mcp-validate POLICY=bronze/silver/gold`
3. **Medaljongnivå** — bronze, sølv, gull
4. **Policyarv** — arvetre for medaljongnivåa
5. **MCP-verktøy** — verktøyoversikt

Følgjande manglar:

- Referanse til `felles-begrepskatalog` og `felles-datakatalog` i **Bruk**-seksjonen
- Ein ny seksjon **Publiseringspolicyer** som dokumenterer dei to policyane
- Oppdatert **Policyarv**-diagram som inkluderer dei to nye policyane

---

## Endringar

### 1. Bruk-seksjonen

Legg til døme med dei to publiseringspolicyane under eksisterande `make mcp-validate`-døme:

```bash
# Medaljongnivå:
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=gold

# Publisering — med datafil/instans:
make mcp-validate \
  SCHEMA=src/linkml/begrep/<katalog>/<katalog>-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=data/begrep/<katalog>.yaml

make mcp-validate \
  SCHEMA=src/linkml/modell/<katalog>/<katalog>-schema.yaml \
  POLICY=felles-datakatalog \
  INSTANCE=examples/modell/<katalog>-eksempel.yaml
```

### 2. Ny seksjon: Publiseringspolicyer

Legg til etter **Gull**-seksjonen og før **Policyarv**, med denne strukturen:

#### Felles Begrepskatalog

Kort intro (éin setning): kva den er og kven som brukar ho.

Tabellar:

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Importerer `skos-ap-no-schema` | `schema_importerer_skos_ap_no` |
| **error** | Deklarerer `skos:`-prefix | `schema_brukar_skos_prefix` |
| **error** | Deklarerer `dct:`-prefix | `schema_brukar_dct_prefix` |
| **error** | Container har attributt med range `Begrep` | `container_har_begrep` |
| **error** | `Begrep` har `skos:prefLabel` | `begrep_har_anbefalt_term` |
| **error** | `Begrep` har `skos:definition` eller `euvoc:xlDefinition` | `begrep_har_definisjon` |
| **error** | `Begrep` har `dct:identifier` | `begrep_har_identifikator` |
| **error** | `Begrep` har `dct:publisher` | `begrep_har_utgjevar` |
| **error** | `Begrep` har `dcat:contactPoint` | `begrep_har_kontaktpunkt` |
| **error** | `Definisjon` har `rdf:value` | `definisjon_har_tekst` |
| **error** | `Samling` har `dct:identifier`, `dct:title`, `dct:publisher`, `dcat:contactPoint`, `skos:member` | (fleire kode-ar) |
| **error** | `dct:publisher`-instansverdi er gyldig `data.norge.no/organizations/<orgnr>`-URI | `utgjevar_er_kjend_org` |
| warning | Container bør ha range `Samling` | `container_har_samling` |
| warning | `Begrep` bør ha `dct:subject`, `dct:creator`, m.fl. | (fleire kode-ar) |

Merknad om arvehierarki: arvar `bronze`.

#### Felles Datakatalog

Kort intro (éin setning): kva den er og kven som brukar ho.

Tabellar:

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Importerer `modelldcat-ap-no-schema` | `schema_importerer_modelldcat_ap_no` |
| **error** | Deklarerer `dct:`-prefix | `schema_brukar_dct_prefix` |
| **error** | Deklarerer `dcat:`-prefix | `schema_brukar_dcat_prefix` |
| **error** | Container har attributt med range `Modellkatalog` | `container_har_modellkatalog` |
| **error** | Container har attributt med range `Informasjonsmodell` | `container_har_informasjonsmodell` |
| **error** | `Modellkatalog` har `dct:title`, `dct:description`, `dct:identifier`, `dct:publisher`, `dcat:contactPoint`, `dct:hasPart` | (fleire kodar) |
| **error** | `Informasjonsmodell` har `dct:title`, `dct:publisher` | (fleire kodar) |
| **error** | `dct:publisher`-instansverdi er gyldig `data.norge.no/organizations/<orgnr>`-URI | `utgjevar_er_kjend_org` |
| warning | `Modellkatalog` bør ha `dct:license`, `modelldcatno:model` | (fleire kodar) |
| warning | `Informasjonsmodell` bør ha `dct:description`, `dct:identifier`, `modelldcatno:informationModelIdentifier`, m.fl. | (fleire kodar) |

Merknad om arvehierarki: arvar `bronze`.

### 3. Oppdatert Policyarv-diagram

Utvid eksisterande diagram til å vise at dei to publiseringspolicyane er
sidegrengar frå `bronze` — ikkje ein del av medaljonghierarkiet:

```
bronze
  ├── silver  (extends: bronze)
  │     └── gold  (extends: silver)
  ├── felles-begrepskatalog  (extends: bronze)
  └── felles-datakatalog  (extends: bronze)
```

Legg til ein kort forklaringstekst: publiseringspolicyane er domene-spesifikke
og er meinte brukt i tillegg til (ikkje i staden for) medaljongnivåa.

---

## Filendring

Éin fil: `src/mcp-linkml-validator/README.md`

- Ingen nye filer
- Eksisterande seksjonar 1–5 vert ikkje endra, berre utvidda
