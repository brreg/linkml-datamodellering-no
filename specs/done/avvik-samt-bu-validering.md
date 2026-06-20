# Plan: Fiks valideringsfeil i samt-bu

**Kortnamn:** `avvik-samt-bu-validering`
**Dato:** 2026-06-20

---

## Bakgrunn

`make lint`, `make validate-instance` og `make roundtrip` er køyrde mot
`src/linkml/samt/samt-bu/samt-bu-schema.yaml` og avdekte to heilt ulike
problemklassar:

1. **Eit skjemafeil i `dqv-ap-no-schema.yaml`** (delt AP-NO-profil, importert
   transitivt av samt-bu) — eit «class override»-mønster for klassa `Standard`
   som er fundamentalt ødelagt og påvirkar **alle** modellar som importerer
   dqv-ap-no, ikkje berre samt-bu.
2. **Instansdata-feil i `samt-bu-eksempel.yaml`** — feil verdiar/strukturar
   som ikkje følgjer skjemaet (typisk skrivefeil, feil feltnamn, manglande
   liste-innpakking).

Desse er uavhengige av kvarandre og bør fiksast i denne rekkjefølga: skjemafeilet
først (det endrar kva som er «riktig» struktur for `Standard`), deretter
instansdatafeilet.

---

## SB0 — Rotårsak: «class override» av `Standard` i dqv-ap-no-schema.yaml er ødelagt ✓

**Utført:** Override-blokka fjerna frå `dqv-ap-no-schema.yaml`. Nytt slot
`gjelder_standard` lagt til `Kvalitetsdimensjon` i `dqv-core-schema.yaml`.
**Avvik frå plan-utkastet:** `range` vart **`uriorcurie`, ikkje `Standard`**
som skissert i utkastet — ein direkte klassereferanse til `Standard` frå
`dqv-core-schema.yaml` er ikkje mogleg utan å skape sirkulær import
(`dqv-core` importerer med vilje **ikkje** `dcat-ap-no`, sjå filhovudet i
`dqv-core-schema.yaml`). Brukar samme `range: uriorcurie`-mønster som det
eksisterande `har_maal`-slottet i samme fil, av identisk grunn. `slot_uri`
sett til `dqvno:appliesToStandard` (ingen eksisterande DQV/dqvno-term funnen
for denne relasjonen). Bug dokumentert som **BUG-6** i
`specs/bugs/dqv-standard-class-override.md` (status `workaround`) —
verifisert empirisk at å fylle ut heile slot-lista i overstyringa **ikkje**
løyser `ValueError`-krasjen; berre fullstendig fjerning av redeklareringa
fungerer.

### Funn

`src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml` (linje 53–64) redeklarerer
klassa `Standard` — som er definert i `dcat-ap-no-schema.yaml` og importert
transitivt — for å «leggje til» slottet `er_i_kvalitetsdimensjon`:

```yaml
classes:
  # Standard-klassen er definert i dcat-ap-no-schema.yaml (importert).
  # Her vert berre det DQV-spesifikke slottet lagt til via class override.
  Standard:
    description: Ein standard eller spesifikasjon som eit datasett er i samsvar med.
    slots:
      - er_i_kvalitetsdimensjon
    slot_usage:
      er_i_kvalitetsdimensjon:
        in_subset:
          - Anbefalt
```

LinkML har **ingen** mekanisme for å «utvide» ei importert klasse på denne
måten — ei lokal redeklarering av eit klassenamn som finst i eit importert
skjema vert **ikkje** unionert med originalen. Konsekvensane er ulike avhengig
av kva generator som brukar `mergeimports` (standard er `True`):

| Generator | Konsekvens | Verifisert |
|---|---|---|
| `gen-json-schema`, `gen-shacl`, `gen-owl` | Lokal redeklarering **erstattar** heile klassa — `Standard` mistar `id`, `tittel`, `har_referanse`, `har_merknad`, `versjon` og sit berre med `er_i_kvalitetsdimensjon` | ✓ Stadfesta i `generated/samt/samt-bu/samt-bu-schema.json`: `Standard`-definisjonen har `additionalProperties: false` og berre éi property |
| `gen-python`, `gen-rdf`, `gen-jsonld-context`, `linkml-convert` (roundtrip) | Hard krasj: `ValueError: Conflicting URIs (..., ...) for item: Standard` i `linkml/utils/mergeutils.py::merge_dicts` | ✓ Reprodusert direkte på `dqv-ap-no-schema.yaml` **isolert** — krasjar sjølv utan samt-bu involvert |

Dette **forklarar direkte** to av valideringsfeila i SB-lista nedanfor
(`i_samsvar_med` forventar objekt, `standarder[0]` har «uventa» property-ar),
og er årsaka til at `make roundtrip` feiler heilt (`0 OK, 2 feil`).

**Verifisert i isolert testkopi (ikkje i repoet):**
- Å fylle ut heile det opphavlege slot-settet i overstyringa (`id`, `tittel`,
  `har_referanse`, `har_merknad`, `versjon` + `er_i_kvalitetsdimensjon`) **løyser
  ikkje** `ValueError`-krasjen — `merge_dicts` kastar uansett så snart to
  `ClassDefinition`-objekt med samme namn har ulik `from_schema`.
- Å **fjerne** override-blokka heilt løyser krasjen umiddelbart — `Standard`
  genererast korrekt frå `dcat-ap-no-schema.yaml` med identifikator-slottet
  intakt (ingen uventa inlining).

### Vedteke val: fjern class override, inverter relasjonen

Sidan LinkML-mønsteret er strukturelt ødelagt (ikkje ein enkel skrivefeil),
er rett fiks å **ikkje** redeklarere `Standard` i dqv-ap-no-schema.yaml i det
heile. `Kvalitetsmerknad`-klassa (som DQV allereie eig) har **allereie**
`er_i_kvalitetsdimensjon` (dqv-core-schema.yaml linje 117). Behovet for at
*ein standard* skal kunne knytast til ein kvalitetsdimensjon kan dekkast utan
å røre `Standard`, ved at retninga på relasjonen vendast: legg til eit nytt
slot på `Kvalitetsdimensjon` (som DQV eig) som peikar **til** `Standard`,
i staden for omvendt.

```yaml
# I dqv-core-schema.yaml — Kvalitetsdimensjon får eit nytt, valgfritt slot:
classes:
  Kvalitetsdimensjon:
    slots:
      - id
      - har_anbefalt_term
      - har_definisjon
      - gjelder_standard      # NYTT — peikar til Standard (dcat-ap-no)
    slot_usage:
      gjelder_standard:
        in_subset:
          - Anbefalt

slots:
  gjelder_standard:
    slot_uri: dqvno:appliesTo   # eller passande dqv/dqvno-term — avklar i SB1
    range: Standard
    multivalued: true
    description: Standard(ar) denne kvalitetsdimensjonen gjeld for.
```

**Alternativ vurdert og forkasta:** å flytte `er_i_kvalitetsdimensjon` inn i
`dcat-ap-no-schema.yaml` sin `Standard`-definisjon direkte. Forkasta fordi
det ville krevd at `dcat-ap-no` (oppstrøms i importhierarkiet) refererer
`Kvalitetsdimensjon` (ein DQV-klasse), som inverterer importretninga og
bryt med det dokumenterte hierarkiet i `CLAUDE.md`
(`dcat-ap-no`/`dqv-ap-no` er søsken under `common-ap-no`, dqv skal ikkje
flyte oppover i dcat).

### Steg

1. Fjern `Standard`-override-blokka frå `dqv-ap-no-schema.yaml` (linje 53–64)
2. Avklar korrekt `slot_uri` for det nye `gjelder_standard`-slottet (sjekk om
   DQV/dqvno-vokabularet har ein eksisterande term — t.d. `dqv:inDimension`
   sin invers, eller bruk eit `dqvno:`-namnerom-spesifikt term dersom DQV ikkje
   har ein standard URI for dette)
3. Legg `gjelder_standard` til `Kvalitetsdimensjon` i `dqv-core-schema.yaml`
   sine `classes:`- og `slots:`-seksjonar
4. Oppdater `dqv-ap-no-eksempel.yaml` og `samt-bu-eksempel.yaml` slik at
   `kvalitetsdimensjoner[].gjelder_standard` (om ønskt i eksempeldata) viser
   den nye relasjonen — **eller** utelat frå eksempel dersom relasjonen ikkje
   er obligatorisk å demonstrere
5. Køyr `make roundtrip SCHEMA=src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`
   og `make roundtrip SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` —
   begge skal gje `2 OK, 0 feil`
6. Køyr `make schema-gen-python`, `schema-gen-rdf`, `schema-gen-context` for
   begge skjema for å stadfeste at `ValueError`-krasjen er borte
7. Diff `generated/ap-no/dqv-ap-no/dqv-ap-no-schema.json` og
   `generated/samt/samt-bu/samt-bu-schema.json` før/etter — stadfest at
   `Standard` no har alle sine opphavlege felt (`id`, `tittel`,
   `har_referanse`, `har_merknad`, `versjon`) i tillegg til at referansar til
   `Standard` (`i_samsvar_med` i `Datasett`) serialiserast som streng-URI,
   ikkje inline-objekt

---

## SB1 — Feil verdi i `er_motivert_av` (instansdata) ✓

**Utført:** Som planlagt — bytt til `assessing` på begge stadar
(`kvalitetsmerknader[0]` og `brukertilbakemeldinger[0]`).

**Feil:** `samt-bu-eksempel.yaml` linje 72 og 79 brukar
`er_motivert_av: dqv:qualityAssessment`, som ikkje er ein gyldig verdi i
`DqvMotivasjon`-enumet. Gyldige verdiar (frå `dqv-core-schema.yaml`):
`assessing`, `classifying`, `availability`, `completeness`, `currentness`,
`validity`, `accuracy`.

**Fiks:** Bytt `dqv:qualityAssessment` → `assessing` (`oa:assessing` —
nærmaste semantiske treff for «generell kvalitetsvurdering») på begge stadar
(`kvalitetsmerknader[0]` og `brukertilbakemeldinger[0]`).

---

## SB2 — `har_tekstdel` manglar liste-innpakking (instansdata) ✓

**Utført:** Som planlagt — pakka i liste på begge stadar.

**Feil:** `har_tekstdel` er `multivalued: true`, men
`samt-bu-eksempel.yaml` linje 75 og 82 set verdien som ein bar streng
(`har_tekstdel: dqv:tekstdel-2`) i staden for ei liste.

**Fiks:**
```yaml
har_tekstdel:
  - dqv:tekstdel-2
```
(tilsvarande for `brukertilbakemeldinger[0]` med `dqv:tekstdel-1`).

---

## SB3 — Feil feltnamn i `kvalitetsmaalinger` (instansdata) ✓

**Utført:** Som planlagt — bytt `har_verdi: "true"` → `har_boolean_verdi: true`.

**Feil:** `samt-bu-eksempel.yaml` linje 87 brukar feltnamnet `har_verdi`, som
ikkje finst på `Kvalitetsmaaling`. Gyldige felt er type-spesifikke:
`har_boolean_verdi`, `har_numerisk_verdi`, `har_tekst_verdi`.

**Fiks:** Verdien `"true"` tyder på ei boolsk måling (er datasettet i
samsvar med kvalitetsmålet eller ikkje) — bytt til:
```yaml
har_boolean_verdi: true
```
(merk: utan hermetegn — ekte YAML-boolean, ikkje streng).

---

## SB4 — Lint-advarslar: manglande `description` på 23 containerattributtar ✓

**Utført:** Som planlagt — `description` lagt til på alle 23 attributt i
`SamtBuContainer`, inkludert `id`-attributtet (som heilt mangla innhald
før fiksen). `make lint` gir no «✓ No problems found».

**Funn:** `make lint` rapporterer 23 `recommended`-advarslar — alle
containerattributtane i `SamtBuContainer` (`kontaktpunkter`, `utgivere`,
`organisasjoner` osv.) manglar `description`. Per `CLAUDE.md` skal
containerattributtar **ikkje** ha `slot_uri` (dei er strukturelle), men
fila har ingen unntak frå `description`-anbefalinga — dette er reint
dokumentasjonsarbeid, ikkje ein strukturell feil.

**Fiks:** Legg til ein kort `description` på alle 23 attributta i
`SamtBuContainer` (`tree_root: true`-klassa) i `samt-bu-schema.yaml`. Eitt
døme:
```yaml
attributes:
  kontaktpunkter:
    range: Kontaktpunkt
    multivalued: true
    inlined: true
    inlined_as_list: true
    description: Kontaktpunkt som kan refereres til frå datasett.
```

---

## Prioritert handlingsliste

| # | Tiltak | Fil(ar) | Avheng av |
|---|--------|---------|-----------|
| 1 | SB0: Fjern `Standard`-override, inverter relasjon via `gjelder_standard` på `Kvalitetsdimensjon` | `dqv-ap-no-schema.yaml`, `dqv-core-schema.yaml` | — |
| 2 | SB0: Oppdater `dqv-ap-no-eksempel.yaml` til ny relasjon (om aktuelt) | `dqv-ap-no-eksempel.yaml` | 1 |
| 3 | SB1: Rett `er_motivert_av`-verdi til `assessing` | `samt-bu-eksempel.yaml` | — |
| 4 | SB2: Pakk `har_tekstdel` i liste på to stadar | `samt-bu-eksempel.yaml` | — |
| 5 | SB3: Rett `har_verdi` → `har_boolean_verdi: true` | `samt-bu-eksempel.yaml` | — |
| 6 | SB4: Legg til `description` på 23 containerattributtar | `samt-bu-schema.yaml` | — |
| 7 | Verifiser: `make lint`, `make validate-instance`, `make roundtrip` for samt-bu — alle skal vere grøne | — | 1–6 |
| 8 | Verifiser: `make roundtrip SCHEMA=dqv-ap-no-schema.yaml` — stadfest at fiksen ikkje regredderer dqv-ap-no isolert | — | 1 |

## Avhengigheiter

- Tiltak 3–6 (instansdata + lint) er heilt uavhengige av tiltak 1–2
  (skjemafiks) og kan utføras i hvilken som helst rekkjefølge, men `make
  validate-instance` for samt-bu vil **ikkje** bli fullstendig grøn før
  **begge** kategoriar er fiksa (skjemaet definerer kva som er «riktig»
  struktur som instansdataen må følgje)
- SB0 påvirkar `dqv-ap-no` direkte og `samt-bu` transitivt — begge sine
  `examples/`-filer bør re-valideres etter fiksen
- Ingen avhengigheit til `specs/done/verktoy-lisensoversikt.md` (urelatert)

## Utført (2026-06-20)

Alle åtte tiltaka er gjennomførte:

- **SB0:** Override-blokk fjerna frå `dqv-ap-no-schema.yaml`; nytt slot
  `gjelder_standard` (`range: uriorcurie`, **avvik frå plan-utkastet som
  skisserte `range: Standard`** — sjå forklaring under SB0 ovanfor) lagt til
  `Kvalitetsdimensjon` i `dqv-core-schema.yaml`. Dokumentert som BUG-6 i
  `specs/bugs/dqv-standard-class-override.md` og lagt til i
  `specs/bugs/README.md`-indeksen.
- **SB1–SB3:** Tre instansdatafeil retta i `samt-bu-eksempel.yaml`
  (`er_motivert_av`, `har_tekstdel`-liste, `har_boolean_verdi`). I tillegg
  flytta `er_i_kvalitetsdimensjon`-verdien frå `standarder[0]` til den nye
  `kvalitetsdimensjoner[0].gjelder_standard` (konsekvens av SB0).
- **SB4:** `description` lagt til alle 23 containerattributt i
  `samt-bu-schema.yaml`, inkludert `id` (som mangla heile attributtkroppen).
- **Verifisert grønt:** `make lint`, `make validate-instance` og
  `roundtrip-json` for samt-bu; `make roundtrip` (json+ttl) for `dqv-ap-no`
  isolert; `gen-python`/`gen-rdf`/`gen-jsonld-context`/`gen-json-schema` for
  samt-bu kjører nå feilfritt, og generert `Standard`-skjema har alle
  opphavlege felt intakt (stadfesta med direkte inspeksjon av generert JSON
  Schema).

**Avvik frå plan, utover SB0 sitt `range`-val:**
- `roundtrip-ttl` for samt-bu feiler framleis — men med det **allereie
  dokumenterte BUG-3** (`rdflib_loader MappingError`, identisk
  feilsignatur som i `specs/bugs/mappingerror-rdflib-roundtrip.md`, der
  samt-bu allereie var lista som kjent feilande). Dette er **ikkje** ein
  regresjon og var **ikkje** i scope for denne planen.
- `make lint`/`make validate-instance` køyrd direkte mot `dqv-ap-no-schema.yaml`
  som ein ekstra sanity-sjekk (utover plan sitt punkt 8, som berre kravde
  roundtrip): lint viser ein **pre-eksisterande, urelatert** advarsel
  (`dct` vs. `dcterms` canonical prefix), og validate-instance feiler med
  «Multiple potential target classes» — forventa for AP-NO-profilskjema utan
  containerklasse (jf. `CLAUDE.md`: AP-NO-modellar skal ikkje ha
  containerklasse). Begge er urelaterte til SB0-fiksen og utanfor scope.
