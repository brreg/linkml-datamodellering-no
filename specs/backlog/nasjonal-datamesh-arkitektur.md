# Nasjonal datamesh-arkitektur: overordna plan

## Visjon

Eit norsk offentleg **datamesh** der:
- kvar verksemd eig og publiserer sine eigne dataprodukt
- informasjonsmodellar er maskinlesbare, gjenbrukbare og harmoniserte på tvers
- omgrep, klassifikasjonar og identifikatorar peikar på same autoritative kjelder
- dette repoet leverer den felles metoden og infrastrukturen for å modellere og publisere

---

## Lag-modell

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  OPPDAGELSESLAG                                                     │
  ├─────────────────────────────────────────────────────────────────────┤
  │  -> portalar og spørjegrensesnitt for databrukarar                  │
  │                                                                     │
  │  data.norge.no (søk, SPARQL)  ·  KUDAF-portalen                     │
  └─────────────────────────────────────────────────────────────────────┘
                                 ▲
                                 │  eksponerer via søk og SPARQL
                                 │
  ┌─────────────────────────────────────────────────────────────────────┐
  │  PUBLISERINGSLAG                                                    │
  ├─────────────────────────────────────────────────────────────────────┤
  │  -> katalogtenester som hauster og lagrar metadata                  │
  │                                                                     │
  │  Felles Datakatalog  ·  Felles Begrepskatalog                       │
  │  Felles Modellkatalog  ·  KUDAF-datafellesskap                      │
  └─────────────────────────────────────────────────────────────────────┘
                                 ▲
                                 │  høster W3C semantiske format:
                                 │  TTL · JSON-LD · SHACL · OWL (via GitHub Pages)
                                 │  
  ╔═════════════════════════════════════════════════════════════════════╗
  ║  MODELLERINGSLAG                            ← dette repoet          ║
  ╠═════════════════════════════════════════════════════════════════════╣
  ║  -> implementerer AP-NO-profiler og domenemodeller i LinkML         ║
  ║                                                                     ║
  ║  linkml-datamodellering-no                                          ║
  ║  AP-NO som LinkML  ·  domenemodeller  ·  MCP-serverar  ·  CI/CD     ║
  ║  bronze / silver / gold / felles-*-policy                           ║
  ╚═════════════════════════════════════════════════════════════════════╝
                                 ▲
                                 │  persistente URI-ar for omgrep, kodeverk og tema
                                 │
  ┌─────────────────────────────────────────────────────────────────────┐
  │  SEMANTIKKLAG                                                       │
  ├─────────────────────────────────────────────────────────────────────┤
  │  -> semantiske standardar og autoritative URI-ar for norsk          │
  │     offentleg sektor                                                │
  │                                                                     │
  │  AP-NO-profiler  ·  SSB Klass  ·  LOS                               │
  │  Felles Begrepskatalog (begrepsidentifikator)                       │
  └─────────────────────────────────────────────────────────────────────┘
                                 ▲
                                 │  informasjonsstrukturar og format
                                 │
  ┌─────────────────────────────────────────────────────────────────────┐
  │  KJELDELAG                                                          │
  ├─────────────────────────────────────────────────────────────────────┤
  │  -> autoritative register og felleskomponentar                      │
  │                                                                     │
  │  Kartverket NGR  ·  BRREG Enhetsreg  ·  FINT  ·  Altinn 3           │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## Innputt-flyt til modelleringslaget (T-form)

```
  ┌────────────────────────────────┐   ┌────────────────────────────────┐
  │  SEMANTIKKLAG                  │   │  KJELDELAG                     │
  ├────────────────────────────────┤   ├────────────────────────────────┤
  │  semantiske standardar og      │   │  autoritative register og      │
  │  autoritative URI-ar           │   │  felleskomponentar             │
  │                                │   │                                │
  │  AP-NO-profiler (Digdir)       │   │  Kartverket NGR · BRREG        │
  │  SSB Klass · LOS               │   │  Enhetsreg · FINT · Altinn 3   │
  │  Felles Begrepskatalog         │   │                                │
  └────────────────┬───────────────┘   └───────────────┬────────────────┘
  persistente URI-ar,                  informasjonsstrukturar
  omgrep og tema                       og format
                  │                                    │
                  └─────────────────────┬──────────────┘
                                        │
                                        ▼
  ╔═════════════════════════════════════════════════════════════════════╗
  ║  MODELLERINGSLAG                                   ← dette repoet   ║
  ╠═════════════════════════════════════════════════════════════════════╣
  ║  implementerer AP-NO-profiler og domenemodeller i LinkML            ║
  ║                                                                     ║
  ║  AP-NO som LinkML  ·  domenemodeller  ·  MCP-serverar  ·  CI/CD     ║
  ║  bronze / silver / gold / felles-*-policy                           ║
  ╚═════════════════════════════════════════════════════════════════════╝
                                        │
                                        │  TTL · JSON-LD · SHACL · OWL
                                        │  (via GitHub Pages)
                                        ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  PUBLISERINGSLAG                                                    │ 
  ├─────────────────────────────────────────────────────────────────────┤
  │  katalogtenester som hauster og lagrar metadata                     │
  │                                                                     │ 
  │  Felles Datakatalog  ·  Felles Begrepskatalog                       │
  │  Felles Modellkatalog  ·  KUDAF-datafellesskap                      │
  └─────────────────────────────────────────────────────────────────────┘
                                        │
                                        │  eksponerer via søk og SPARQL
                                        ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  OPPDAGELSESLAG                                                     │
  ├─────────────────────────────────────────────────────────────────────┤
  │  portalar og spørjegrensesnitt for databrukarar                     │
  │                                                                     │
  │  data.norge.no (søk, SPARQL)  ·  KUDAF-portalen                     │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## Noverande tilstand i dette repoet

```
linkml-datamodellering-no
│
├── AP-NO-profiler (LinkML)          → importerbare skjema for alle norske AP-ar
│   dcat-ap-no, skos-ap-no,
│   modelldcat-ap-no, cpsv-ap-no,
│   dqv-ap-no, xkos-ap-no
│
├── Domenemodeller (LinkML)          → konkrete informasjonsmodellar
│   NGR, FINT, SAMT, BRREG
│
├── MCP-serverar                     → KI-assistert modellering og validering
│   mcp-linkml-modell-utkast
│   mcp-linkml-begrep-utkast
│   mcp-linkml-validator
│
├── CI/CD-pipeline (GitHub Actions)
│   validate → generate → publish
│
└── Publisering (eksisterande)
    Felles Datakatalog (ModelDCAT-AP-NO)     ✓ live
    Felles Begrepskatalog (SKOS-AP-NO)       ✓ live
```

---

## Integrasjonsoversikt

### A — Allereie integrert

| Teneste | Standard | Korleis |
|---|---|---|
| **Felles Datakatalog** (data.norge.no) | ModelDCAT-AP-NO | `publish_external: true` i manifest + høsting via GitHub Pages |
| **Felles Begrepskatalog** (data.norge.no/concepts) | SKOS-AP-NO | MCP-server genererer YAML → CI konverterer til Turtle → GitHub Pages → høsting |
| **LOS** (psi.norge.no/los) | SKOS | `fagomrade:`-felt i begrep + `dcat:theme` i skjema nyttar LOS-URI-ar |
| **BRREG Enhetsregisteret** | REST/HAL | `utgjevar:`-felt brukar `data.norge.no/organizations/{orgnr}` |
| **Kartverket NGR** | SOSI/OGC | `ngr-adresse`, `ngr-eiendom`, `ngr-person`, `ngr-virksomhet` modellerer Matrikkelen |
| **FINT** | HAL/XMI | `fint-administrasjon`, `fint-arkiv` m.fl. |

---

### B — Planlagde integrasjonar

---

#### B1 — KUDAF (Kunnskapssektorens datafellesskap)

**Kva:** Sikt/HK-dir sin fødererte metadatakatalog for kunnskapssektoren (UH + forsking).
Haustar DCAT-AP-NO-metadata frå dataprodusentar; brukar RAIRD/GSIM for variabel-nivå-metadata.

**Kvifor:** KUDAF brukar DCAT-AP-NO, som allereie er modellert her. Ein LinkML-modell av
GSIM-variablar gjer at utdanningsdata kan skildrast ned på variabelnivå med koplingar
til omgrep i Felles Begrepskatalog.

**Integrasjonsmodell:**

```
src/linkml/kudaf/
├── gsim-variabel-schema.yaml      ← RAIRD-variabelmodell i LinkML
└── examples/
    └── gsim-variabel-eksempel.yaml

Publiseringsflyt:
  manifest.yaml (data_policy: kudaf)
      → CI validerer mot kudaf-policy
      → konverterer til DCAT-AP-NO Turtle
      → GitHub Pages
      → KUDAF haustar via kudaflib
```

**Kva som må lagast:**
- `src/linkml/kudaf/gsim-variabel-schema.yaml` — modellerer GSIM-konseptar:
  `IdentifiedConcept`, `Variable`, `UnitType`, `EnumeratedValueDomain`,
  `DescribedValueDomain`, med `annotations.begrepsidentifikator` til Felles Begrepskatalog
- `src/mcp-linkml-validator/policies/kudaf.yaml` — valideringspolicy
- Profil for KUDAF-spesifikke metadata i `mcp-linkml-begrep-utkast`

---

#### B2 — SSB Klass (Klassifikasjonar og kodelister)

**Kva:** SSB sin API for ~130 offisielle statistiske klassifikasjonar (kommunar, NACE,
utdanningsnivå, yrker, m.fl.) med SKOS/RDF-eksport. Stabilt tilgjengeleg på
`https://data.ssb.no/api/klass/v1/`.

**Kvifor:** SSB Klass er kjelda for kodeverk som vert brukt i nesten alle norske
offentlege datasett. I dag duplikerast desse kodeverka i kvart datasett. Ein datamesh
bør referere SSB Klass direkte i `enum`-definisjonar.

**Integrasjonsmodell:**

```yaml
# I LinkML-skjema: enum med meaning-URI frå SSB Klass
enums:
  Naeringshovedgruppe:
    enum_uri: urn:ssb:classification:klass:6
    permissible_values:
      A:
        meaning: "urn:ssb:classification:klass:6/code/A"
        description: Jordbruk, skogbruk og fiske
      B:
        meaning: "urn:ssb:classification:klass:6/code/B"
        description: Bergverksdrift og utvinning
```

**Kva som må lagast:**
- Skript `src/assets/scripts/klass-to-linkml-enum.py` — hentar klassifikasjon frå
  SSB Klass API og genererer LinkML `enum`-blokk med `meaning`-URI-ar
- Integrasjon i MCP-server: ny `list_klass_codes`-funksjon i
  `mcp-linkml-modell-utkast` (kallar SSB Klass REST API)

---

#### B3 — Felles Modellkatalog — automatisk metadata-generering

**Kva:** data.norge.no/information-models (ModelDCAT-AP-NO).
Allereie i bruk, men katalogoppføringane vert i dag hand-redigerte i
`brreg-modellkatalog-eksempel.yaml` / `data/brreg-modellkatalog.yaml`.

**Kvifor:** Manuell vedlikehald av `brreg-modellkatalog.yaml` er feilutsett og
vert stale. Med `manifest.yaml`-metadata kan ModellDCAT-AP-NO-blokker genererast
automatisk.

**Integrasjonsmodell:**

```yaml
# manifest.yaml utvidast:
modelldcat:
  tittel: "Nasjonale grunndata – Adresse"
  beskrivelse: "Informasjonsmodell for offisielle adresser frå Matrikkelen."
  tema:
    - https://psi.norge.no/los/tema/bolig-og-eiendom
  lisens: http://publications.europa.eu/resource/authority/licence/CC_BY_4_0
```

CI-steget les `modelldcat:`-seksjonen og genererer ei `modellkatalog`-oppføring
automatisk — same mønster som `generate-config.sh` allereie brukar for generator-flagg.

---

#### B4 — Altinn Studio / XSD-eksport

**Kva:** Altinn Studio brukar XSD for datamodellar i digitale skjema.

**Kvifor:** Offentlege skjema i Altinn som brukar same informasjonsmodell som
LinkML-skjemaet kan gjenbruke LinkML som einaste kjelde. Reduserer dobbeltarbeid
mellom informasjonsarkitektur og digitaliseringsprosjekt.

**⚠ Avklart:** LinkML har ingen offisiell `gen-xsd`-generator (ikkje i
[generatoroversikta](https://linkml.io/linkml/generators/index.html)). Mogleg
alternativ tilnærming:

```
LinkML-skjema
    → gen-json-schema  (offisiell generator)
    → JSON Schema
    → json-schema-to-xsd (tredjeparts konverteringsverktøy)
    → <modell>.xsd
    → Altinn Studio
```

**Status:** Krev vidare undersøking av om JSON Schema → XSD-konvertering er
tilstrekkeleg for Altinn Studio sine krav, eller om ein eigen XSD-generator må
utviklast som eit bidrag til LinkML-prosjektet.

---

### C — Identifiserte gap (lav prioritet / lengre sikt)

| Gap | Teneste | Kva som manglar |
|---|---|---|
| Folkeregisteret | DSF/FREG | Personmodell med `freg:`-URI-ar som `meaning` |
| Matrikkelen WFS | Kartverket | SHACL-validering av WFS GML-respons mot `ngr-adresse`-skjema |
| eFormidling | Digdir | Dokumenttypemodell for SBD-konvoluttar i LinkML |
| NHN Grunndata | Norsk Helsenett | FHIR R4-profil generert frå LinkML (sektorspesifikt) |
| INSPIRE / EuroVoc | EU | Europeisk harmonisering av domenemodeller |

---

## Fullstendig arkitektur (målbilete)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         OPPDAGELSESLAG                                       │
│                                                                               │
│  data.norge.no          KUDAF               SSB Klass      LOS               │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────┐   ┌──────────┐        │
│  │Datasett      │    │Variabel-     │    │Kodelist  │   │Tema-     │        │
│  │Begrep        │    │metadata      │    │SKOS/RDF  │   │taksonomi │        │
│  │Modell        │◄───│DCAT-AP-NO    │    │JSON      │   │SKOS      │        │
│  │API           │    │RAIRD/GSIM    │    └──────────┘   └──────────┘        │
│  └──────┬───────┘    └──────┬───────┘         ▲               ▲             │
│         │ høsting           │ høsting          │ klass-to-     │ LOS-URI     │
└─────────┼───────────────────┼──────────────────┼───────────────┼─────────────┘
          │                   │                  │               │
┌─────────▼───────────────────▼──────────────────┼───────────────┼─────────────┐
│                         MODELLERINGSLAG                         │             │
│                                                                 │             │
│            linkml-datamodellering-no                            │             │
│  ┌─────────────────────────────────────────────────────────┐   │             │
│  │  AP-NO-profiler      Domenemodeller       MCP-serverar  │   │             │
│  │  dcat-ap-no          ngr, fint, samt      modell-utkast │   │             │
│  │  skos-ap-no          kudaf, brreg         begrep-utkast │   │             │
│  │  modelldcat-ap-no    altinn-xsd           validator     │   │             │
│  │                                                         │   │             │
│  │  manifest.yaml ─► CI/CD ─► GitHub Pages                │   │             │
│  │  (bronze/silver/gold/felles-*/kudaf policies)           │   │             │
│  └─────────────────────────────────────────────────────────┘   │             │
│                    │ publiserer TTL/XSD/JSON                    │             │
└────────────────────┼───────────────────────────────────────────┼─────────────┘
                     │                                            │
┌────────────────────▼────────────────────────────────────────────────────────┐
│                         SEMANTIKKLAG                                         │
│                                                                               │
│  Felles Begrepskatalog      SSB Klass           LOS            BRREG        │
│  ┌──────────────────┐    ┌──────────────┐   ┌────────┐    ┌──────────┐     │
│  │SKOS-omgrep       │    │Klassifika-   │   │Tema-   │    │Org-nr    │     │
│  │begrepsidentifi-  │    │sjonar med    │   │URI-ar  │    │org-URI   │     │
│  │kator-URI         │    │URN-ar        │   │        │    │          │     │
│  └──────────────────┘    └──────────────┘   └────────┘    └──────────┘     │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                         KJELDELAG                                             │
│                                                                               │
│  Kartverket NGR       BRREG Enhetsreg      FINT              Altinn 3        │
│  (adresse, eigedom)   (organisasjonar)     (HR, utdanning)   (skjema/API)   │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Datamesh-prinsipp — korleis dette repoet støttar dei

| Prinsipp | Korleis støtta av dette repoet |
|---|---|
| **Domene-eige** | Kvar organisasjon/verksemd lagar sitt eige skjema i `src/linkml/<org>/` med eigen `manifest.yaml`. CI/CD og MCP-serverar er sjølvbetjening. |
| **Data som produkt** | `manifest.yaml` definerer kva som genererast (JSON Schema, SHACL, OWL, TTL) og publiserast. Kvar modell får ein stabil URI og ein GitHub Pages-URL. |
| **Sjølvbetjent infrastruktur** | `bootstrap.sh` + reusable workflows gjer at ekstern verksemd kan ta i bruk verktøykassa utan å jobbe i monorepoet. MCP-serverar gir KI-assistert modellering utan lokal installasjon. |
| **Føderert styring** | Bronze/silver/gold/felles-*-policyer håndhever felles standardar (AP-NO-samsvar, URI-stabilitet, omgrepsreferansar) utan å sentralisere eigarskapet til enkelte modeller. |

---

## Maskinlesbarheit — krav og gap

Alle publiserte artefakter frå dette repoet er maskinlesbare i dag:

| Artefakt | Format | Maskinlesbar |
|---|---|---|
| Skjema-dokumentasjon | JSON-LD context | ✓ |
| Datavalidering | SHACL (TTL) | ✓ |
| Semantikk | OWL (TTL) | ✓ |
| Datainstansar | RDF/Turtle | ✓ |
| Katalogoppføring | ModelDCAT-AP-NO TTL | ✓ |
| Variabelmetadata (KUDAF) | RAIRD/DCAT-AP-NO | ✗ manglar |
| XSD for Altinn | XSD | ✗ manglar |
| FHIR-profil | StructureDefinition JSON | ✗ ut av scope |

---

## Tilrådde neste steg (prioritert)

| # | Tiltak | Verdi | Kostnad |
|---|---|---|---|
| 1 | **KUDAF GSIM/RAIRD-profil** — `src/linkml/kudaf/gsim-variabel-schema.yaml` + policy | Høg (kunnskapssektoren) | Medium |
| 2 | **SSB Klass-til-enum skript** — `klass-to-linkml-enum.py` + MCP-tool `list_klass_codes` | Høg (kodeverk-harmonisering) | Lav |
| 3 | **Automatisk ModelDCAT-AP-NO-metadata** — `modelldcat:`-seksjon i `manifest.yaml` | Medium (reduserer manuelt arbeid) | Medium |
| 4 | **XSD-generator** — `xsd: true` i manifest, gen-xsd i CI | Medium (Altinn-integrasjon) | Lav |
| 5 | **SPARQL-oppslag i MCP-serverar** — sjekk om omgrep/modell finst før oppretting | Medium (unngå duplikat) | Medium |

---

## Avgrensingar og prinsipp

- **Ingen sentral datalagring** — dette repoet lagrar aldri rådata (utenom begreper), berre skjema, metadata og begreper
- **Pull-modell for publisering** — katalogtenestene haustar frå GitHub Pages; ingen direkte push-API
- **Maskinporten er infrastruktur** — publisering til katalogane krev Maskinporten-token, men dette er eit driftsansvar, ikkje eit modellansvar
- **SERES er avvikla** — ingen integrasjon planlagt; Altinn Studio (XSD) er etterfølgjaren
- **Helsesektoren** (NHN/FHIR) er bevisst halde utanfor — krev eige fagdomene

---

## Relaterte spesifikasjonar

- [`dx-prof-linkml-modell.md`](dx-prof-linkml-modell.md) — Profiles Vocabulary for formell profilskildring
- [`publisering-felles-datakatalog.md`](publisering-felles-datakatalog.md) — teknisk publiseringsflyt
- [`publisering-felles-begrepskatalog.md`](publisering-felles-begrepskatalog.md) — teknisk publiseringsflyt
