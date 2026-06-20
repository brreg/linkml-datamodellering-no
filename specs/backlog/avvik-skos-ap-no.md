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

### SK5 (revidert 2026-06-20) — Avvik 10–11 må realiserast som `instance_checks` i medaljong-policyen, ikkje SHACL

Den opphavlege SK5 (hand-skriven SHACL-fil) er forlate — repoet har ingen
mekanisme for hand-skrivne SHACL-tillegg utanom den auto-genererte SHACL-en
frå `make publish`, og brukaren har valt å ikkje innføre ein slik mekanisme
(jf. forrige avklaringsrunde).

Den korrekte staden å realisere Avvik 10–11 er i stedet
**`src/mcp-linkml-validator/policies/felles-begrepskatalog.yaml`**, som
allereie har eit presedens for instans-validering via `instance_checks:`
(sjå `utgjevar_er_kjend_org` — validerer `dct:publisher`-URI-format på faktiske
`Begrep`-instansar). Dette er «medaljong»-policysystemet (bronze → silver →
gold → felles-begrepskatalog) som validerer skjema- og datakvalitet med
`make mcp-validate POLICY=<nivå>`. Dette er konsistent med korleis
`src/mcp-linkml-validator/policies/README.md` skil mellom skjemakvalitet og
datakvalitet — Avvik 10–11 er begge **datakvalitet** (krav til faktiske
språktaggverdiar i instansar), ikkje skjemastruktur.

#### Oppdaga avgrensing i datamodellen

Før ein sjekk kan skrivast, vart følgende undersøkt i
`src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`:

- `anbefalt_term` (`skos:prefLabel`) er lagra som ei **rein strengliste utan
  språk-tag per verdi**: `["nestleder", "nestleiar", "deputy chair"]`. Det finst
  ingen `@nb`/`@nn`-markering eller anna metadata som skiller dei frå
  hverandre.
- JSON-LD-konteksten (`brreg-begrepskatalog-context.jsonld`) markerer feltet
  som `"@type": "rdf:langString"`, men har **ingen per-verdi
  `@language`-mekanisme** — `LangString` er definert som `base: str` i
  `common-ap-no-schema.yaml` (brukt av *alle* AP-NO-profilar, ikkje berre
  SKOS-AP-NO).
- Dette heng saman med `specs/bugs/langstring-rdflib-roundtrip.md` (BUG-1):
  `rdf:langString`-verdiar rundtrippar ikkje korrekt via TTL i det heile, så
  språk-informasjon er upålitelig i denne delen av pipelinen uavhengig av
  Avvik 10–11.
- **Derimot** er språk *inferarbart* for `Definisjon`-objekt (`har_definisjon`
  → `euvoc:xlDefinition`), via den etablerte ID-suffiks-konvensjonen som
  allereie er i bruk: `https://begrep.brreg.no/def/nestleder-nb`,
  `...-nn`, `...-en`.

**Konsekvens:** ein fullstendig maskinell sjekk av Avvik 10 (krav til
`skos:prefLabel`) kan ikkje skrivast i dag, sidan datalaget ikkje uttrykker
kva språk ein gitt `anbefalt_term`-streng har. Ein sjekk avgrensa til
`har_definisjon`-varianten er derimot gjennomførbar utan skjemaendring.

#### Forslag A — Avgrensa sjekk for Avvik 10, gjennomførbar no (ingen skjemaendring)

Ny `instance_check` i `felles-begrepskatalog.yaml`, etter mønsteret til
`utgjevar_er_kjend_org`:

```yaml
instance_checks:
  begrep_har_definisjon_pa_nb_og_nn:
    severity: warning
    description: >
      Begrep med har_definisjon bør ha minst éi Definisjon med id som endar
      på «-nb» og minst éi som endar på «-nn» (tospråkskravet, Avvik 10 i
      avvik-skos-ap-no.md). Sjekken er avgrensa til ID-suffiks-konvensjonen
      sidan LangString ikkje bærer språk-tag per verdi (jf. BUG-1).
    check: instance_begrep_definisjon_language_coverage
    relasjon_slot_uri: euvoc:xlDefinition   # har_definisjon
    krev_spraak: [nb, nn]
    id_suffiks_pattern: "-([a-z]{2})$"
```

Tilhøyrande Python-handler i `server.py` (ny `_INSTANCE_CHECK_HANDLERS`-nøkkel
`instance_begrep_definisjon_language_coverage`):
1. Finn alle `Begrep`-instansar og deira `har_definisjon`-lister (URI-ar).
2. For hvert `Begrep`, sjekk om minst eitt referert `Definisjon.id` endar på
   `-nb` og minst eitt endar på `-nn` (mønster frå `id_suffiks_pattern`).
3. Generer `warning` for `Begrep` som har `har_definisjon` men manglar éin av
   dei to.
4. `Begrep` utan `har_definisjon` (berre `definisjon`/fritekst) hoppast over —
   sjå avgrensing under.

**Avgrensing:** dekker berre `har_definisjon`-varianten. `Begrep` som berre
brukar `definisjon` (fritekst, `skos:definition`) kan ikkje sjekkast, av same
grunn som `anbefalt_term` — ingen språk-tag per strengverdi.

**Status: Forslag A er IMPLEMENTERT (2026-06-20).** Sjekken
`begrep_har_definisjon_pa_nb_og_nn` (`check: instance_begrep_definisjon_language_coverage`)
er lagt til i `src/mcp-linkml-validator/policies/felles-begrepskatalog.yaml`,
med tilhøyrande handler i `src/mcp-linkml-validator/server.py`. Verifisert mot
reell produksjonsdata (`data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`):
gir `warning` for `foretaksnavn` og `aksjeklasser` (manglar `-nn`), ingen
varsel for `nestleder` (har `-nb`, `-nn` og `-en`). `make mcp-val-test` viser
same 12 pre-eksisterande testfeil som før endringa (ikkje relatert til denne
sjekken — stadfesta ved `git stash`-sammenligning).

**Oppdaga sideeffekt (ikkje fiksa, utanfor denne oppgåva):** under
verifisering vart det avdekt at den eksisterande `_check_instance_slot_uri_pattern`
(brukt av `utgjevar_er_kjend_org`) sin `walk()`-funksjon ikkje rekursivt går inn
i lister av objekt (t.d. `begrep: [...]`), og dermed aldri når nøsta `utgjevar`-felt
i praksis — stadfesta empirisk ved å sette inn ein ugyldig orgnr-verdi i
produksjonsdata utan at sjekken slo ut. Den nye
`instance_begrep_definisjon_language_coverage`-handleren bruker ein korrekt
rekursiv `walk()` som også går inn i lister, og er ikkje påvirka. Den
eksisterande latente feilen bør vurderast som eigen bugfix/spec ved eit senere
tilfelle.

#### Forslag B — Full løysing for Avvik 10–11 (krev skjemaendring, eigen spec)

For å dekke Avvik 10 fullt ut (også for `anbefalt_term`/fritekst-`definisjon`)
og Avvik 11 (språkkonsistens mellom `anbefalt_term` og definisjon), må
`LangString`-verdiar bære ein språk-tag per element. Dette er eit
skjemadesign-spørsmål som påverkar *alle* AP-NO-profilar som brukar
`LangString` (ikkje berre SKOS-AP-NO), og bør derfor utformast som ein eigen
spesifikasjon (t.d. `specs/backlog/spraaktagging-av-langstring.md`) med minst
to alternativ å vurdere:

1. **Strukturert verdi** — bytt multivalued `LangString`-slots til ei liste av
   eit `SprakTaggetTekst`-objekt med `verdi` (string) og `spraak` (range
   `Spraak`/`string`). Mest i tråd med repoets prinsipp om lenking/objekt
   framfor strengkonvensjonar, men eit brot med dagens `LangString: base: str`
   og krev migrering av alle eksisterande datafiler som brukar `LangString`.
2. **Inline språkkode i strengen** — t.d. `"nestleder@nb"`, parsa av
   validator/generatorar. Krev ingen skjemaendring, men er ein uvanleg,
   skjult konvensjon som ikkje er synleg i `range`-typen og lett å bryte.

Begge alternativ krev òg ei vurdering av om/korleis BUG-1
(`rdflib_loader`-roundtrip) påverkar løysinga, sidan språk-taggen må overleve
TTL-roundtrip for å vere nyttig i praksis.

**Til Avvik 11 (språkkonsistens) spesifikt:** krev i tillegg Forslag A eller B
for `Definisjon`/`har_definisjon`-sida er på plass — sjekken «minst eitt par
(anbefalt_term, definisjon) deler språk» kan først skrivast når begge sider av
paret har ein verifiserbar språk-tag.

**Status:** Forslag A og B er **ikkje implementerte** — dette er eit
dokumentert løysingsforslag for vidare avklaring, ikkje eit utført tiltak.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | SK3: Rett `range` på `kjelde_relasjon`, `malgruppe_def`, `euvoc_status` | `skos-ap-no-schema.yaml` | — |
| 2 | SK4: Rett `range` på `fagomrade` | `skos-ap-no-schema.yaml` | — |
| 3 | SK1: Fiks retningsslots i `GeneriskRelasjon` og `PartitivRelasjon` | `skos-ap-no-schema.yaml` | — |
| 4 | SK2: Juster subset for `definisjon` / `har_definisjon` | `skos-ap-no-schema.yaml` | — |
| 5 | SK5 (revidert): `instance_checks` for tospråkskrav og språkkonsistens | `felles-begrepskatalog.yaml` + `server.py` | SK1–SK4, og for Forslag B: ny spec `spraaktagging-av-langstring.md` |

---

## Avhengigheiter

- SK3 og SK4 er reine range-endringar og kan gjerast uavhengig av kvarandre
- SK1 og SK2 krev gjennomgang av eksisterande `brreg-begrepskatalog`-datafiler
  for å sikre at reelle instansar framleis validerer etter endringa
- SK5 (revidert) — Forslag A er uavhengig av SK1–SK4 og kan gjerast når som helst;
  Forslag B krev ein separat spec sidan det påverkar `LangString` på tvers av
  alle AP-NO-profilar
- Endringar i `skos-ap-no-schema.yaml` vil krevje ny validering og regenerering
  av alle skjema som importerer dette (`brreg-begrepskatalog-schema.yaml`)

---

## Utført (2026-06-20, delvis)

**SK1–SK4 er implementerte** i `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`:

- **SK1:** `har_generisk_omgrep`/`har_spesifikt_omgrep` (`GeneriskRelasjon`) og
  `har_partitivt_omgrep`/`har_heilskapleg_omgrep` (`PartitivRelasjon`) endra frå
  `in_subset: [Obligatorisk]` til `in_subset: [Anbefalt]`. Ingen `required: true`
  fanst på desse i utgangspunktet (avvik frå det spesifikasjonen viste som
  «noverande» kode — kontrollert direkte i schemaet).
- **SK2:** `definisjon` og `har_definisjon` på `Begrep` endra frå
  `in_subset: [Obligatorisk]` til `in_subset: [Anbefalt]`.
- **SK3:** `kjelde_relasjon`, `malgruppe_def`, `euvoc_status` har no
  `range: Konsept` (var `range: Begrep`).
- **SK4:** `fagomrade` har no `range: Konsept` (var `range: Begrep`).

**SK5 er DELVIS utført (oppdatert 2026-06-20).** Den opphavlege
SHACL-tilnærminga vart forlate — ingen mekanisme for hand-skrivne
SHACL-tillegg finst i repoet, og brukaren valde å ikkje innføre ein slik
mekanisme. SK5 vart i stedet revidert til `instance_checks` i
`felles-begrepskatalog.yaml` (medaljong-policysystemet). **Forslag A er no
implementert** — sjekken `begrep_har_definisjon_pa_nb_og_nn` validerer
tospråkskravet (Avvik 10) for `har_definisjon`-varianten via
ID-suffikskonvensjonen (sjå detaljar i seksjonen over). **Forslag B
(full løysing for Avvik 10 på `anbefalt_term` + Avvik 11 språkkonsistens) er
ikkje implementert** — krev språktagging av `LangString` på tvers av alle
AP-NO-profilar og ein eigen spec (`spraaktagging-av-langstring.md`), per
brukaren sitt valde scope for denne runda.
**Spesifikasjonen flyttast ikkje til `specs/done/` før SK5 er fullstendig
utført** (jf. CLAUDE.md: berre flytt når alle tiltak er utførte) — Avvik 11
og delen av Avvik 10 som gjeld `anbefalt_term` står framleis open.

**Ikkje adressert (ingen tilsvarande tiltak i spesifikasjonen):** Avvik 8
(`relasjontype` støttar ikkje `skos:Concept`-range) og Avvik 9 (`verdiomrade`
støttar ikkje URI-range) hadde ingen `SK`-tiltak i «Tilrådde tiltak»-seksjonen,
og er derfor ikkje rørte.

**Validering:** `make lint` viser same 4 pre-eksisterande
`canonical_prefixes`-advarslar som før endringa. `make roundtrip` (JSON + TTL)
OK for `skos-ap-no-schema.yaml` og det avhengige
`brreg-begrepskatalog-schema.yaml`. `make validate-instance` mot både
`brreg-begrepskatalog-eksempel.yaml` og produksjonsdatafila
`data/brreg-begrepskatalog/brreg-begrepskatalog.yaml` gav «No issues found» —
range-endringa frå `Begrep` til `Konsept` er trygg sidan eksisterande data
allereie brukar eksterne vokabular-URI-ar (ikkje lokale `Begrep`-instansar)
for `fagomrade` og `kjelde_relasjon`.
