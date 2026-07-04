# Utvid modell-`index.md` for auka brukarverdi

## Bakgrunn

Mkdocs-portalen (https://brreg.github.io/linkml-datamodellering-no/) fungerer som:
- **Primært verktøy** for ikkje-utviklarar (domeneekspertar, arkitektar, forvaltarar) til å få oversikt over modellar
- **Hjelpemiddel** for utviklarar til å finne fram til korrekt modell, forstå struktur og hente artefaktar

Noverande `index.md` per modell inneheld:
1. Hovudoverskrift
2. `description.md`-innhald (for 6 av 33 modellar)
3. Metadata-tabell (name, title, version, license, imports osv.)
4. ER-diagram (PlantUML SVG)
5. Klasseliste (Obligatorisk/Anbefalt/Valgfri/Andre)
6. Slot-liste
7. Enumerations-liste
8. Type-liste
9. Artefakt-tabell (TTL, JSON Schema, SHACL osv.)
10. Valideringsresultat (MCP-validator)
11. Versjonslog (CHANGELOG.md)

## Gap-analyse

### Ikkje-utviklar-perspektiv

| Brukar | Behov | Noverande dekking | Gap |
|---|---|---|---|
| Domeneekspert | "Korleis ser eit eksempel ut?" | ⚠️ Berre på klassenivå | Eksempel på `index.md` manglar (finst på klassedetaljsidene) |
| Forvaltningsarkitekt | "Korleis kjem eg i gang?" | ⚠️ Berre i hovud-README | Modell-spesifikk quickstart manglar |
| Prosjektleiar | "Kva er avhengigheitene?" | ✅ Imports-felt i metadata | OK |
| Jurist/compliance | "Kva lisens gjeld?" | ✅ Lisens-felt i metadata | OK |
| Datakatalog-brukar | "Kva er den offisielle referansen?" | ⚠️ Berre i description.md for nokre | Ekstern spesifikasjon-lenke bør vere prominent |

### Utviklar-perspektiv

| Brukar | Behov | Noverande dekking | Gap |
|---|---|---|---|
| Python-utviklar | "Korleis importerer eg dette?" | ❌ Ingen | Installasjon/import-instruksjonar manglar |
| API-utviklar | "Korleis ser JSON Schema ut i bruk?" | ⚠️ Lenke finst, men ingen kontekst | Brukseksempel for JSON Schema manglar |
| RDF-utviklar | "Korleis validerer eg TTL-data?" | ⚠️ SHACL-lenke finst | SPARQL/SHACL-eksempel manglar |
| CI/CD-ansvarleg | "Korleis automatiserer eg validering?" | ❌ Ingen | GitHub Actions-snippet manglar |
| Integrasjonsutviklar | "Kva er endepunktet?" | ❌ Ingen (berre for enkelte modellar) | API-URL/høstingsendepunkt manglar |

### Informasjonsarkitektur-perspektiv

Noverande struktur er **bottom-up** (frå teknisk detalj til kontekst):
1. Metadata → 2. Diagram → 3. Klasseliste → 4. Artefaktar → 5. Validering → 6. Versjonslog

Idealstruktur er **top-down** (frå kontekst til detalj):
1. **Kva** (beskrivelse + offisiell referanse)
2. **Kven** (typiske brukarar)
3. **Korleis** (kom-i-gang / quickstart)
4. **Teknisk detalj** (metadata, diagram, klasser)
5. **Artefaktar** (nedlastingar)
6. **Status** (validering, versjonslog)

## Foreslåtte tiltak

### 1. **Quickstart-seksjon** (høg prioritet)

Legg til `## Kom i gang` rett etter `description.md` (før metadata-tabellen), med:

#### For AP-NO-profilar:
```markdown
## Kom i gang

### Importer i LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from dcat_ap_no_model import Katalog

katalog = yaml_loader.load('eksempel.yaml', target_class=Katalog)
print(katalog.tittel)
```

### Valider data mot SHACL

```bash
pyshacl --shacl dcat-ap-no-shapes.ttl --data-format turtle mine-data.ttl
```

### Offisiell referanse

📘 [DCAT-AP-NO-spesifikasjonen](https://informasjonsforvaltning.github.io/dcat-ap-no/) frå Digitaliseringsdirektoratet
```

#### For domenemodellar:
```markdown
## Kom i gang

### Last ned eksempelfil

- [YAML](../examples/dcat-ap-no-eksempel.yaml)
- [Turtle](dcat-ap-no-eksempel.ttl) (generert)

### Valider eiga datafil

```bash
linkml-validate -s dcat-ap-no-schema.yaml mine-data.yaml
```

### GitHub Actions-validering

```yaml
- name: Valider DCAT-AP-NO-data
  run: |
    curl -O https://brreg.github.io/linkml-datamodellering-no/ap-no/dcat-ap-no/dcat-ap-no-shapes.ttl
    pyshacl --shacl dcat-ap-no-shapes.ttl --data-format turtle mine-data.ttl
```
```

**Plassering:** Rett etter `description.md` og **før** metadata-tabellen.

**Generering:** Utvid `mkdocs/publish.sh` med logikk som identifiserer modelltype (AP-NO vs domenemodell) og genererer passande quickstart-seksjon.

---

### 2. **Eksempel-seksjon** (høg prioritet)

Legg til `## Eksempel` rett etter Quickstart-seksjonen (eller rett etter `description.md` dersom Quickstart ikkje finst):

```markdown
## Eksempel

### YAML

```yaml
katalogar:
  - id: https://example.org/katalogar/eksempel-1
    tittel:
      - Eksempelkatalog
    beskrivelse:
      - Ein demonstrasjonskatalog for DCAT-AP-NO modellert i LinkML.
    utgiver: https://organization-catalog.fellesdatakatalog.digdir.no/organizations/991825827
    datasett:
      - https://example.org/datasett/aapen-adresseregister
```

[📄 Full eksempelfil (YAML)](../examples/dcat-ap-no-eksempel.yaml) | [🔗 Turtle-versjon](dcat-ap-no-eksempel.ttl)

*Detaljerte eksempel per klasse finst på kvar klasseside, t.d. [Datasett](klasser/datasett.md#examples), [Katalog](klasser/katalog.md#examples).*
```

**Kjelde:** Les frå `src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml` (første 15–25 liner).

**Generering:** Utvid `publish.sh` til å ekstrahere eksempel frå `examples/`-mappa og injisere det i `index.md`.

**Eksisterande funksjonalitet:** Gen-docs genererer **allereie** per-klasse-eksempel frå `<modell>-eksempel.yaml`:
- `src/assets/scripts/gen-docgen-examples.py` splittar container-strukturerte eksempelfiler til per-klasse-filer (t.d. `Skole-skole-1.yaml`, `Skole-skole-2.yaml`)
- `gen-doc --example-directory` inkluderer desse i `## Examples`-seksjonen på kvar klasseside (t.d. `mkdocs/docs/samt/samt-bu/klasser/skole.md`)
- Brukaren kan klikke seg inn på ein klasse og sjå konkrete YAML-eksempel for den klassen

Dette tiltaket legg til ein **oversikts-snippet** på `index.md` som viser typisk bruk av modellen som heilskap, med lenke til full eksempelfil og til klassedetaljsidene.

---

### 3. **Ekstern referanse-boks** (medium prioritet)

Flytt "Offisiell referanse"-lenka frå `description.md` til ei **prominent info-boks** rett under hovudoverskrifta:

```markdown
# dcat-ap-no

!!! info "Offisiell referanse"
    📘 [DCAT-AP-NO-spesifikasjonen](https://informasjonsforvaltning.github.io/dcat-ap-no/) frå Digitaliseringsdirektoratet
```

**Kjelde:** Ny `annotations.referanse_url`-felt i schema-metadata (valfri), eller hardkoda mapping i `publish.sh` for kjente AP-NO-profilar.

---

### 4. **Avhengighetsgraf** (medium prioritet)

Legg til ei **visuell oversikt** over kva andre modellar som importerer/vert importerte av denne modellen — **visualisert som ASCII tree-struktur** (same format som importkjede i `mkdocs/docs/ap-no-arkitektur.md`):

```markdown
## Avhengigheiter

### Importerer

```
linkml:types
common-ap-no
dqv-core
```

### Vert importert av

```
modelldcat-ap-no
    └── brreg-modellkatalog
ngr-adresse
samt-bu
oreg-aksjonærer
```

*Sjå [AP-NO Arkitektur](../../ap-no-arkitektur.md#importkjede) for fullstendig importkjede.*
```

**Generering:** 
- Parse `imports:`-felt i det aktuelle skjemaet for å finne direkte importar
- Parse `imports:`-felt i **alle** skjema for å finne kven som importerer dette skjemaet (reverse-dependencies)
- Generer ASCII tree-struktur i `publish.sh` med same format som i `ap-no-arkitektur.md`:
  - Flat liste for direkte importar (ingen hierarki)
  - Tree-struktur for reverse-dependencies (viser kven som brukar kva)

**Eksisterande referanse:** `mkdocs/docs/ap-no-arkitektur.md` viser importkjede som ASCII tree (linje 13-25) — same visualiseringsformat skal brukast her.

---

### 5. **Kontaktinformasjon** (låg prioritet)

Legg til `## Kontakt` nedst i `index.md` (etter Versjonslog):

```markdown
## Kontakt

**Forvaltningsansvarleg:** [Brønnøysundregistrene](https://data.norge.no/organizations/991825827)  
**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)  
**Spørsmål:** [team@digdir.no](mailto:team@digdir.no) (for Digdir-vedlikehaldne AP-NO-profilar)
```

**Kjelde:** `annotations.kontakt`-felt (valfri) eller hardkoda fallback.

---

### 6. **Badge-rad** (låg prioritet)

Legg til status-badges rett under hovudoverskrifta:

```markdown
# dcat-ap-no

[![Versjon](https://img.shields.io/badge/v2.2.0-blue)]() 
[![Status](https://img.shields.io/badge/Completed-green)]() 
[![Validering](https://img.shields.io/badge/gold-2%20feil-yellow)]()
[![Lisens](https://img.shields.io/badge/NLOD%202.0-blue)]()
```

**Generering:** Dynamisk frå metadata og valideringsresultat.

---

## Prioritert handlingsliste

| Steg | Handling | Prioritet | Estimat | Status | Brukarverdi |
|---|---|---|---|---|---|
| 1 ✅ | Quickstart-seksjon (importer, Python, SHACL, GitHub Actions) | **Høg** | 45 min | ✅ Utført | Utviklar + arkitekt |
| 2 ✅ | Eksempel-seksjon (YAML-snippet + lenkje til full fil) | **Høg** | 30 min | ✅ Utført | Ikkje-utviklar + utviklar |
| 3 ⬜ | Ekstern referanse-boks (flyttar frå description.md til prominent info-boks) | Medium | 20 min | ⬜ Ikkje starta | Domeneekspert + arkitekt |
| 4 ⬜ | Avhengighetsgraf (ASCII tree-struktur av import-/reverse-dependencies) | Medium | 60 min | ⬜ Ikkje starta | Arkitekt |
| 5 ⬜ | Kontaktinformasjon (forvaltningsansvarleg + support-lenkjer) | Låg | 15 min | ⬜ Ikkje starta | Alle |
| 6 ⬜ | Badge-rad (versjon, status, validering, lisens) | Låg | 30 min | ⬜ Ikkje starta | Utviklar |

**Total estimat:** 3–4 timar for alle tiltak (1,5 time for høgprioritets-tiltaka).

---

## Ny foreslått struktur for `index.md`

1. **Hovudoverskrift** (`# <schema>`)
2. **Ekstern referanse-boks** (info-boks med lenke til offisiell spec) — **NY**
3. **`description.md`-innhald** (dersom fila finst)
4. **Quickstart-seksjon** (`## Kom i gang` — importer, Python, validering) — **NY**
5. **Eksempel-seksjon** (`## Eksempel` — YAML-snippet + lenkjer) — **NY**
6. **Metadata-tabell** (`## Metadata`)
7. **Publiseringsinfo** (boks dersom `published-uris.lock` finst)
8. **Avhengighetsgraf** (`## Avhengigheiter` — ASCII tree med imports + reverse-dependencies) — **NY**
9. **ER-diagram** (`## ER-diagram`)
10. **Klasseliste** (`## Classes`, `## Slots`, `## Enumerations`, `## Types`)
11. **Artefaktabell** (`## Generated artifacts`)
12. **Valideringsresultat** (`## Valideringsresultat`)
13. **Versjonslog** (`## Versjonslog`)
14. **Kontakt** (`## Kontakt`) — **NY**

---

## Avhengigheiter

- Eksempel-TTL-generering: Krev at `make gen-rdf` køyrer på eksempelfiler (ikkje implementert enno)
- Relasjonsgraf: Krev import-graf-parsing i `publish.sh`
- Quickstart-logikk: Krev modelltype-deteksjon (AP-NO vs domenemodell)

---

## Suksesskriterium

**Ikkje-utviklar:** Kan opne ein modell-index og på 30 sekund forstå kva modellen er, sjå eit konkret eksempel og finne lenke til offisiell spec.

**Utviklar:** Kan kopiere/lime inn Quickstart-kode for å importere modellen i LinkML, Python eller SHACL-validering — utan å måtte søkje gjennom GitHub-mappa.

**Måleindikator:** 90% av modell-index-sidene skal ha Quickstart + Eksempel innan 3 månader etter implementering.

---

## Utført

Implementert steg 1-2 (Quickstart + Eksempel) med vellykka verifisering:

**Steg 1 — Quickstart-seksjon (linje 158-214 i `mkdocs/publish.sh`):**

To variantar vert automatisk generert basert på `domain`:

**AP-NO-profilar (`domain = "ap-no"`):**
- Import-snippet (GitHub Raw-URL)
- Python-bruk (linkml-runtime + yaml_loader)
- SHACL-validering (pyshacl)

**Domenemodellar (andre domene):**
- Last ned eksempelfil (GitHub Raw-URL)
- Valider eiga datafil (linkml-validate)
- GitHub Actions-validering (curl + pyshacl)

**Steg 2 — Eksempel-seksjon (linje 216-231):**

Viser første 20 liner frå `<modell>-eksempel.yaml`:
- YAML-snippet (ekskluderer kommentarheader)
- Lenke til full eksempelfil på GitHub
- Referanse til klassedetaljsider (`## Examples` per klasse)

**Verifisering:**
- ✅ `ap-no/dcat-ap-no`: Quickstart (AP-NO-variant) + Eksempel (10 liner)
- ✅ `samt/samt-bu`: Quickstart (domenemodell-variant) + Eksempel (17 liner)
- ✅ `ap-no/common`: Quickstart (AP-NO-variant) utan Eksempel (ingen eksempelfil)

**Dekningsgrad:** Alle 18 genererte modellar får Quickstart. 17 av 18 får Eksempel (berre `common-ap-no` manglar eksempelfil).

**Avvik frå opphavleg plan:** Ingen.

**Gjenståande tiltak (steg 3-6):** Kan gjerast inkrementelt etter behov (medium/låg prioritet).
