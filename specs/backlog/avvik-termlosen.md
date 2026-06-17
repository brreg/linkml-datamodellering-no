# Kartlegging: Avvik mot Termlosen (standard for omgrepsanalyse og terminologiarbeid)

**Kjelde:** [digdir.no/standarder/termlosen/1733](https://www.digdir.no/standarder/termlosen/1733)  
**Teknisk spec:** [informasjonsforvaltning.github.io/termlosen](https://informasjonsforvaltning.github.io/termlosen/)  
**Utgjevar:** Språkrådet / Digitaliseringsdirektoratet  
**Status:** Tilrådd (ikkje obligatorisk)  
**Implementasjon i repoet:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`

---

## Bakgrunn

Termlosen er ein *metodologisk* standard — han beskriv prosess og kvalitetskrav for
terminologiarbeid, ikkje eit RDF-dataformat. Han supplerer SKOS-AP-NO-Begrep (som
beskriv *korleis* omgrep representerast i RDF) med rettleiing om *korleis* omgrep
skal analyserast og beskrivas.

Kartlegginga her fokuserer på kva *schema-strukturelle* konsekvensar Termlosen har
for `skos-ap-no-schema.yaml` og tilhøyrande datafiler. Krav om prosess, tekstkvalitet
og arbeidsform er dokumentert for oversiktens skuld, men dei høyrer ikkje heime i
eit LinkML-skjema.

---

## Termlosen sitt innhald — oversikt

Termlosen er organisert i 6 hovudkapitlar:

1. **Omgrepsanalyse** — relasjonar mellom referentar, omgrep, definisjonar og termar
2. **Definisjonar** — typar, struktur og kvalitetskrav
3. **Termar** — typologiar og utvalsreglar
4. **Omgrepsharmonisering og termharmonisering** — koordinering på tvers
5. **Trinn i terminologiprosjekt** — praktisk framgangsmåte
6. **Presentasjon av terminologiske data** — terminografi

---

## Kartlegging av avvik

### 1 — Definisjonsmønster: innhaldsdefinisjon vs. omfangsdefinisjon ikkje skilde

Termlosen definerer to hovudtypar definisjonar:

| Type | Norsk | Beskriving |
|---|---|---|
| Innhaldsdefinisjon | Intensjonell | Skildrar vesentlege og åtskiljande kjenneteikn |
| Omfangsdefinisjon | Ekstensjonell | Reknar opp alle referentar — må vere komplett |

SKOS-AP-NO (og schema-implementasjonen) skil berre mellom:
- `skos:definition` — direkte fritekst (utan typen innhald vs. omfang)
- `euvoc:xlDefinition` — objekt med kjelde og målgruppe (utan typen)

Det finst ingen eigenskap i schema for å angi *kva type* definisjon ein instans er.
I praksis betyr dette at omfangsdefinisjonar (som Termlosen åtvarar mot å bruke
med «t.d.» eller «o.l.») ikkje skiljast frå innhaldsdefinisjonar.

**Moglege løysingar:**
- Legg til `skosno:definitionType` (`range: Konsept`) på `Definisjon`-klassen dersom
  Digdir/Språkrådet publiserer eit kontrollert vokabular for dette
- Alternativt: dokumenter som rettleiar-krav i `description`-feltet, ikkje schema

**Status:** ⚠️ Avvik — låg prioritet (SKOS-AP-NO-spec har heller ikkje dette skillet)

---

### 2 — Assosiative relasjonar manglar strukturert typologi

Termlosen definerer 8 underkategoriar av assosiative relasjonar:

| Kategori | Eksempel |
|---|---|
| Årsak / verknad | brann → brannskade |
| Produsent / produkt | ku → mjølk |
| Aktivitet / aktør | operasjon → kirurg |
| Aktivitet / stad | utstilling → museum |
| Føremål / stad | gravplass → kyrkjegard |
| Føremål / aktivitet | mat → ete |
| Verkty / funksjon | kalkulator → rekne |
| Materiale / produkt | tre → møbel |

I schema-implementasjonen er `AssosiativRelasjon.relasjontype` modellert som
fritekst (`range: LangString`). Dette gjer det umogleg å validere at ein brukt
relasjontype høyrer til Termlosen sin typologi, og vanskeleggjer maskinell
handsaming og søk.

**Moglege løysingar:**
- Publiser eit `skosno:AssociativeConceptRelationRole`-vokabular med dei 8
  Termlosen-kategoriane, og endre `relasjontype.range` til `Konsept`
- Alternativt: legg til `enum`-verdiar for dei 8 typane i schema (rigid, men
  validerbart)

**Status:** ⚠️ Avvik — middels prioritet  
**Merknad:** Avvik 8 i `avvik-skos-ap-no.md` (SK3) er ein føresetnad for dette tiltaket.

---

### 3 — Samsvarsspots: `broadMatch`, `narrowMatch`, `relatedMatch` manglar

Termlosen krev at fleirspråkleg ekvivalens dokumenterast med *grad* av samsvar
(nøyaktig, tilnærma, ingen ekvivalent). SKOS har fem samsvarspredikat:

| SKOS-predikat | Termlosen-ekvivalens | Status i schema |
|---|---|---|
| `skos:exactMatch` | Nøyaktig samsvar | ✓ `noyaktig_samsvar` |
| `skos:closeMatch` | Tilnærma samsvar | ✓ `naert_samsvar` |
| `skos:broadMatch` | Breiare omgrep i eksternt vokabular | ✗ manglar |
| `skos:narrowMatch` | Smalare omgrep i eksternt vokabular | ✗ manglar |
| `skos:relatedMatch` | Relatert i eksternt vokabular | ✗ manglar |

Dei tre siste er Valgfri per SKOS-AP-NO-spec men gjer det umogleg å fullstendig
dokumentere fleirspråklege omgrepssystem (som Termlosen krev for harmonisering).

**Status:** ⚠️ Avvik — låg prioritet (Valgfri i SKOS-AP-NO)

---

### 4 — Illustrasjonar ikkje modellert

Termlosen seier eksplisitt at illustrasjonar *kan utfylle* (men ikkje avløyse)
definisjonar, og at dei helst skal stå same side som termposten.

Schema har inga eigenskap for bilde/illustrasjon til eit `Begrep`. SKOS-standarden
har heller ikkje eit slikt predikat, men `foaf:depiction` eller `schema:image`
kunne brukast.

**Status:** ⚠️ Avvik — låg prioritet (ikkje krav i SKOS-AP-NO)

---

### 5 — `kjelde.range: uri` ekskluderer kjelder utan URI

Termlosen seier «alt relevant materiale på fagområdet bør nyttast» som kjelder —
inkludert trykte lover, forskrifter, standardar, lærebøker og tidsskrift som
*ikkje* har ein stabil URI.

I schema er `kjelde` (`dct:source`) definert med `range: uri`, som betyr at berre
nett-adresserbare kjelder kan registerast maskinelt. Papirbøker og trykte
lovtekstar utan URI fell utanfor.

**Moglege løysingar:**
- Legg til `kjelde_tekst` (fritekst `LangString`) ved sida av `kjelde` (URI)
- Eller endre `kjelde.range` til `string` / `uriorcurie` og tilate fritekstkilder

**Status:** ⚠️ Avvik — middels prioritet

---

## Krav utanfor skjemaets scope

Desse Termlosen-krava kan ikkje modellerast i eit LinkML-schema. Dei gjeld
for innhaldskvaliteten på definisjonane, ikkje datastrukturen.

### Definisjonskvalitetskrav (kap. 2)

| Krav | Kan modellerast? |
|---|---|
| Definisjon skal gjelde berre eitt omgrep | Nei — krev tekstanalyse |
| Kortfatta, berre vesentlege kjenneteikn | Nei — krev tekstanalyse |
| Ikkje sirkeldefinisjon (direkte eller indirekte) | Nei — krev grafanalyse |
| Unngå negative definisjonar | Nei — krev tekstanalyse |
| Utan punktum, substantiv i ubestemt eintal | Nei — krev NLP |
| Utskiftingsprinsippet | Nei — krev tekstanalyse |
| Ikkje byrje med «som er», «betegnar», «benyttes til» | Delvis — SHACL regex |

Kan vurderast som SHACL-reglar for det siste punktet (regex på `skos:definition`).

### Terminologiprosjektprosess (kap. 5)

- Arbeidsgruppe på 5–8 deltakarar + terminolog som konsulent
- Prosjekt skal avgrensast til under 200 omgrep
- Kjeldearbeid, strukturering og termval følgjer bestemte trinn

Desse er prosess- og organiseringskrav og høyrer ikkje heime i datamodellen.

### Termkvalitetskrav (kap. 3)

- Term skal vere motivert (reflektere kjenneteikn)
- Skal tillate bøying og avleiing
- Berre éin anbefalt term per omgrep ideelt sett

Eitt anbefalt term per omgrep er ein *rettleiar*, ikkje eit datastrukturkrav.
Fleire `skos:prefLabel` (eitt per språk) er gyldig per SKOS-spesifikasjonen.

---

## Samandrag

| # | Avvik | Alvor | Prioritet |
|---|---|---|---|
| 1 | Definisjonsmønster (innhald/omfang) ikkje skild | Avvik | Låg |
| 2 | `AssosiativRelasjon.relasjontype` manglar Termlosen-typologi | Avvik | Middels |
| 3 | `broadMatch`, `narrowMatch`, `relatedMatch` manglar | Avvik | Låg |
| 4 | Illustrasjonar ikkje modellert | Avvik | Låg |
| 5 | `kjelde.range: uri` ekskluderer ikkje-URI-kjelder | Avvik | Middels |

---

## Tilrådde tiltak

### TL1 — Strukturer `relasjontype` mot Termlosen-typologi (Avvik 2)

Når SK3 i `avvik-skos-ap-no.md` er gjennomført (range: Konsept), publiser
eit kontrollert vokabular for assosiative relasjonskategoriar basert på
Termlosen sine 8 typar.

Kandidat-URI: `https://data.norge.no/vocabulary/skosno/associative-relation-role`

**Filer:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`  
**Avhengigheit:** SK3 i `avvik-skos-ap-no.md`

---

### TL2 — Legg til `kjelde_tekst` for ikkje-URI-kjelder (Avvik 5)

```yaml
kjelde_tekst:
  slot_uri: dct:bibliographicCitation
  range: LangString
  multivalued: true
  description: >-
    Fritekstbeskriving av kjelde til definisjonen, for kjelder utan URI
    (t.d. trykte lover, standardar eller lærebøker).
```

Legg til i `Definisjon.slots` og `Definisjon.slot_usage` som Valgfri.

**Filer:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`

---

### TL3 — Legg til manglande samsvarsspots (Avvik 3)

```yaml
breitt_samsvar:
  slot_uri: skos:broadMatch
  range: Begrep
  multivalued: true
  description: Omgrep med breiare meining i eksternt vokabular (skos:broadMatch).

smalt_samsvar:
  slot_uri: skos:narrowMatch
  range: Begrep
  multivalued: true
  description: Omgrep med smalare meining i eksternt vokabular (skos:narrowMatch).

relatert_samsvar:
  slot_uri: skos:relatedMatch
  range: Begrep
  multivalued: true
  description: Relatert omgrep i eksternt vokabular (skos:relatedMatch).
```

Legg til i `Begrep.slots` og `Begrep.slot_usage` som `in_subset: [Valgfri]`.

**Filer:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`

---

### TL4 — SHACL-regel for definisjonskvalitet (Avvik frå kap. 2)

Legg til ein SHACL-regel i `skos-ap-no-shapes.ttl` (ny fil per SK5 i
`avvik-skos-ap-no.md`) som varslar dersom `skos:definition` byrjar med
strenger som «som er», «betegnar», «benyttes til» eller «term som».

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | TL2: Legg til `kjelde_tekst` (fritekst-kjelde) | `skos-ap-no-schema.yaml` | — |
| 2 | TL3: Legg til `breitt_samsvar`, `smalt_samsvar`, `relatert_samsvar` | `skos-ap-no-schema.yaml` | — |
| 3 | TL1: Kontrollert vokabular for assosiative relasjonskategoriar | nytt vokabular-YAML | SK3 frå `avvik-skos-ap-no.md` |
| 4 | TL4: SHACL-regel for definisjonskvalitet | `skos-ap-no-shapes.ttl` | SK5 frå `avvik-skos-ap-no.md` |

---

## Avhengigheiter

- TL1 (relasjonskategoriar) er avhengig av SK3 i `avvik-skos-ap-no.md`
  (endre `relasjontype.range` frå `LangString` til `Konsept`)
- TL4 er avhengig av at `skos-ap-no-shapes.ttl` vert oppretta (SK5)
- TL2 og TL3 kan gjerast uavhengig av kvarandre og resten
- Endringar i `skos-ap-no-schema.yaml` krev ny validering av `brreg-begrepskatalog`
