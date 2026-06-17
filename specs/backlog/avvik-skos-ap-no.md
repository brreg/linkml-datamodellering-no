# Kartlegging: Avvik mot Forvaltningsstandard for omgrepsbeskrivingar (SKOS-AP-NO-Begrep)

**Kjelde:** [digdir.no/standarder/forvaltningsstandard-omgrepsbeskrivingar-skos-ap-no-begrep/1682](https://www.digdir.no/standarder/forvaltningsstandard-omgrepsbeskrivingar-skos-ap-no-begrep/1682)  
**Teknisk spec:** [informasjonsforvaltning.github.io/skos-ap-no-begrep](https://informasjonsforvaltning.github.io/skos-ap-no-begrep/)  
**Gyldig frå:** 1. januar 2023  
**Implementasjon i repoet:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`

---

## Bakgrunn

`skos-ap-no-schema.yaml` implementerer SKOS-AP-NO-Begrep som ein LinkML-profil.
Skjemaet brukas som grunnlag for `brreg-begrepskatalog` og andre begrepskatalog-modeller.

---

## Kartlegging av avvik

### 1 — `GeneriskRelasjon` har begge retningsslots som Obligatorisk

Standarden seier:
> Bruk *anten* `skosno:hasGenericConcept` (overomgrep) *eller* `skosno:hasSpecificConcept`
> (underomgrep) — **ikkje begge** i same relasjonsobjekt.

I `skos-ap-no-schema.yaml` er begge merka `required: true` og `in_subset: [Obligatorisk]`:

```yaml
GeneriskRelasjon:
  slot_usage:
    har_generisk_omgrep:      # skosno:hasGenericConcept
      in_subset: [Obligatorisk]
    har_spesifikt_omgrep:     # skosno:hasSpecificConcept
      in_subset: [Obligatorisk]
```

Dette tyder at validatoren krev *begge* — som er feil. Ein generisk relasjon
skal berre innehalde eitt av dei to slotsa.

**Status:** ⚠️ Strukturelt avvik — krev endring

---

### 2 — `PartitivRelasjon` har begge retningsslots som Obligatorisk

Same problem som avvik 1. Standarden seier bruk *anten* `skosno:hasPartitiveConcept`
(delomgrep) *eller* `skosno:hasComprehensiveConcept` (heilskapleg omgrep), ikkje begge.

```yaml
PartitivRelasjon:
  slot_usage:
    har_partitivt_omgrep:     # skosno:hasPartitiveConcept
      in_subset: [Obligatorisk]
    har_heilskapleg_omgrep:   # skosno:hasComprehensiveConcept
      in_subset: [Obligatorisk]
```

**Status:** ⚠️ Strukturelt avvik — krev endring

---

### 3 — `definisjon` og `har_definisjon` begge merka Obligatorisk

Standarden krev *minst éin definisjon*, anten som:
- direkte fritekst (`skos:definition`) — brukas når kjelde/målgruppe ikkje trengst
- via objekt (`euvoc:xlDefinition`) — brukas når kjelde, relasjon eller målgruppe skal spesifiserast

Det er alternativ, ikkje kumulative krav. Noverande schema krev *begge*:

```yaml
Begrep:
  slot_usage:
    definisjon:       # skos:definition
      in_subset: [Obligatorisk]
    har_definisjon:   # euvoc:xlDefinition
      in_subset: [Obligatorisk]
```

Ein instans med berre `skos:definition` vil feilvalidere mot `har_definisjon`.
Korrekt krav: minst eitt av dei to.

**Status:** ⚠️ Avvik — bør rettast til `in_subset: [Anbefalt]` for begge, med
SHACL-regel om at minst eitt er påkravd

---

### 4 — `kjelde_relasjon` (`skosno:relationshipWithSource`) har feil `range`

Standarden seier `skosno:relationshipWithSource` skal peike på eit omgrep frå
eit kontrollert norsk vokabular for kjelderelasjonar (t.d. «sitat frå», «basert på»,
«inspirert av»).

Noverande implementasjon:
```yaml
kjelde_relasjon:
  slot_uri: skosno:relationshipWithSource
  range: Begrep           # ← feil: peikar på lokale Begrep-instansar
```

Korrekt `range` er `Konsept` (generisk `skos:Concept` frå eksternt vokabular),
ikkje `Begrep` (lokalt definert klasse for omgrep i katalogen).

**Status:** ⚠️ Semantisk feil — krev endring

---

### 5 — `malgruppe_def` (`dct:audience`) har feil `range`

Same problem som avvik 4. `dct:audience` på `Definisjon` skal peike på eit
omgrep frå Digdir sitt Audience Type-vokabular (t.d. «allmennheit», «fagpersonell»).

```yaml
malgruppe_def:
  slot_uri: dct:audience
  range: Begrep           # ← feil: skal vere Konsept frå eksternt vokabular
```

**Status:** ⚠️ Semantisk feil — krev endring

---

### 6 — `euvoc_status` har feil `range`

`euvoc:status` skal peike på EU sitt Concept Status-vokabular
(t.d. `<http://publications.europa.eu/resource/authority/concept-status/CURRENT>`).

```yaml
euvoc_status:
  slot_uri: euvoc:status
  range: Begrep           # ← feil: skal vere Konsept frå EU-vokabular
```

**Status:** ⚠️ Semantisk feil — krev endring

---

### 7 — `fagomrade` (`dct:subject`) har feil `range`

Standarden seier `dct:subject` representerer fagområde og kan peike på eit
omgrep frå *kva som helst* SKOS-vokabular. `range: Begrep` avgrensar til
berre lokale omgrep i same katalog.

```yaml
fagomrade:
  slot_uri: dct:subject
  range: Begrep           # ← for avgrensande: skal vere Konsept (eksternt eller lokalt)
```

**Status:** ⚠️ Avvik — middels prioritet

---

### 8 — `relasjontype` (`skosno:relationRole`) støttar berre fritekst

Standarden seier `skosno:relationRole` kan vere anten `rdf:langString` (fritekst)
*eller* `skos:Concept` (omgrep frå kontrollert vokabular).

Noverande:
```yaml
relasjontype:
  slot_uri: skosno:relationRole
  range: LangString       # ← berre fritekst, ikkje URI-referanse
```

**Status:** ⚠️ Avvik — låg prioritet (fritekst er gyldig, berre URI-alternativet manglar)

---

### 9 — `verdiomrade` (`skosno:valueRange`) støttar berre `LangString`

Standarden seier `skosno:valueRange` kan vere `rdf:langString` (fritekstbeskriving)
*eller* `xsd:anyURI` (lenke til t.d. eit kodeverks-URI).

```yaml
verdiomrade:
  slot_uri: skosno:valueRange
  range: LangString       # ← berre fritekst, URI-alternativet manglar
```

**Status:** ⚠️ Avvik — låg prioritet

---

### 10 — `anbefalt_term` krev ikkje begge målformer (bokmål + nynorsk)

Standarden har ein kardinalet på 2..n for `skos:prefLabel` og krev at omgrepet
er beskriven på *begge* norske skriftspråk (bokmål og nynorsk).

LinkML støttar ikkje å uttrykke «minst éin med `@nb` og minst éin med `@nn`»
direkte i slot-definisjonen. Kravet manglar difor heilt som valideringsregel.

**Status:** ⚠️ Avvik — kan ikkje løysast i LinkML-schema åleine; krev SHACL-regel

---

### 11 — Språkkonsistenskrav ikkje modellert

Standarden seier:
> «Minst éin kombinasjon av anbefalt term og definisjon må dele same språk.»

Dette er eit tverr-slot-krav som ikkje kan uttrykksast i LinkML.
Det krev ein eigen SHACL-regel.

**Status:** ⚠️ Avvik — krev SHACL-regel utanom skjemaet

---

## Samandrag

| # | Avvik | Alvor | Prioritet |
|---|---|---|---|
| 1 | `GeneriskRelasjon`: begge retningsslots Obligatorisk | Strukturell feil | **Høg** |
| 2 | `PartitivRelasjon`: begge retningsslots Obligatorisk | Strukturell feil | **Høg** |
| 3 | `definisjon` + `har_definisjon` begge Obligatorisk | Avvik | **Høg** |
| 4 | `kjelde_relasjon.range: Begrep` → skal vere `Konsept` | Semantisk feil | **Høg** |
| 5 | `malgruppe_def.range: Begrep` → skal vere `Konsept` | Semantisk feil | **Høg** |
| 6 | `euvoc_status.range: Begrep` → skal vere `Konsept` | Semantisk feil | **Høg** |
| 7 | `fagomrade.range: Begrep` → skal vere `Konsept` | Avvik | Middels |
| 8 | `relasjontype` støttar ikkje `skos:Concept`-range | Avvik | Låg |
| 9 | `verdiomrade` støttar ikkje URI-range | Avvik | Låg |
| 10 | Tospråkskrav (bokmål + nynorsk) ikkje modellert | Avvik | Middels |
| 11 | Språkkonsistenskrav ikkje modellert | Avvik | Låg |

---

## Tilrådde tiltak

### SK1 — Fiks retningsslots i `GeneriskRelasjon` og `PartitivRelasjon` (Avvik 1–2)

Endre begge til `in_subset: [Anbefalt]` (ikkje `Obligatorisk`), og legg til
SHACL-regel om at nøyaktig eitt av dei to er påkravd.

Alternativt: modeller to separate underklassar —
`GeneriskRelasjonOppover` (med `har_generisk_omgrep`) og
`GeneriskRelasjonNedover` (med `har_spesifikt_omgrep`).

**Filer:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`

---

### SK2 — Juster subset for `definisjon` og `har_definisjon` (Avvik 3)

Begge bør vere `in_subset: [Anbefalt]`. Ein SHACL-regel bør krevje minst éin
av dei to per `Begrep`. Ei enkeltare løysing er å setje berre `har_definisjon`
som `Obligatorisk` (den rikare varianten), men dette avvik frå standarden sin
intensjon om at enkel fritekst er nok.

**Filer:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`

---

### SK3 — Rett `range` på `kjelde_relasjon`, `malgruppe_def`, `euvoc_status` (Avvik 4–6)

Alle tre skal bruke `range: Konsept` (den generiske `skos:Concept`-hjelpeklassen
frå `common-ap-no-schema`), ikkje `range: Begrep`:

```yaml
kjelde_relasjon:
  slot_uri: skosno:relationshipWithSource
  range: Konsept    # frå kontrollert norsk vokabular
  description: Forholdet mellom definisjonen og kjelda (kontrollert vokabular).

malgruppe_def:
  slot_uri: dct:audience
  range: Konsept    # frå Digdir Audience Type-vokabular
  description: Målgruppe definisjonen er retta mot (kontrollert vokabular).

euvoc_status:
  slot_uri: euvoc:status
  range: Konsept    # frå EU Concept Status-vokabular
  description: Status frå EU Concept Status-vokabularet.
```

**Filer:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`

---

### SK4 — Rett `range` på `fagomrade` (Avvik 7)

```yaml
fagomrade:
  slot_uri: dct:subject
  range: Konsept    # eksternt eller lokalt SKOS-omgrep
```

**Filer:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`

---

### SK5 — Legg til SHACL-reglar for språkkrav (Avvik 10–11)

Desse krava kan ikkje modellerast i LinkML og krev eigne SHACL-reglar:

1. **Tospråkskrav**: `skos:prefLabel` må ha minst éin verdi med `@nb` og minst
   éin med `@nn`.
2. **Språkkonsistens**: minst eitt par `(skos:prefLabel, skos:definition)` eller
   `(skos:prefLabel, euvoc:xlDefinition)` må dele same språktag.

Lag `src/linkml/ap-no/skos-ap-no/skos-ap-no-shapes.ttl` med desse reglane.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | SK3: Rett `range` på `kjelde_relasjon`, `malgruppe_def`, `euvoc_status` | `skos-ap-no-schema.yaml` | — |
| 2 | SK4: Rett `range` på `fagomrade` | `skos-ap-no-schema.yaml` | — |
| 3 | SK1: Fiks retningsslots i `GeneriskRelasjon` og `PartitivRelasjon` | `skos-ap-no-schema.yaml` | — |
| 4 | SK2: Juster subset for `definisjon` / `har_definisjon` | `skos-ap-no-schema.yaml` | — |
| 5 | SK5: SHACL-reglar for tospråkskrav og språkkonsistens | `skos-ap-no-shapes.ttl` (ny) | SK1–SK4 |

---

## Avhengigheiter

- SK3 og SK4 er reine range-endringar og kan gjerast uavhengig av kvarandre
- SK1 og SK2 krev gjennomgang av eksisterande `brreg-begrepskatalog`-datafiler
  for å sikre at reelle instansar framleis validerer etter endringa
- SK5 (SHACL) bør kome etter SK1–SK4 er på plass
- Endringar i `skos-ap-no-schema.yaml` vil krevje ny validering og regenerering
  av alle skjema som importerer dette (`brreg-begrepskatalog-schema.yaml`)
