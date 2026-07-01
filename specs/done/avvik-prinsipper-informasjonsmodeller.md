# Kartlegging: Avvik mot Prinsipper for informasjonsmodeller

**Kjelde:** [digdir.no/informasjonsforvaltning/prinsipper-informasjonsmodeller/3030](https://www.digdir.no/informasjonsforvaltning/prinsipper-informasjonsmodeller/3030)  
**Utgjevar:** Digitaliseringsdirektoratet  
**Karakter:** Høgnivå-rettesnor (ikkje teknisk spesifikasjon)  
**Relatert dokument:** Felles modelleringsregler for offentlig forvaltning ([/3029](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029))

---

## Bakgrunn

Digdir sitt prinsippdokument inneheld ni prinsipp for informasjonsmodellar, utan
underpunkt eller tekniske krav. Prinsippa er normative retningslinjer som vert
konkretiserte i «Felles modelleringsregler for offentlig forvaltning» (15 reglar),
som MCP-validatoren i dette repoet allereie implementerer (sjå `src/mcp-linkml-validator/policies/README.md`).

Denne kartlegginga evaluerer difor repoet på to nivå:

1. **Strukturelle gap** — krav prinsippa stiller som MCP-validatoren ikkje fangar
2. **Etterlevingsgap** — krav validatoren fangar (warning/error), men der repoet konsekvent ikkje etterlever

| Prinsipp | MCP-dekning | Hovudgap | Status |
|---|---|---|---|
| P1 Sammenheng | Delvis (regel 4, 12) | Inkonsistent slot-definisjon på tvers av skjema | Ope |
| P2 Brukerperspektiv | Delvis (regel 1, 5) | 22/28 skjema manglar portaltekst (`description.md`) | Ope |
| P3 Terminologi | Delvis (regel 13) | `begrepsidentifikator` manglar på nær alle klasser | Ope |
| P4 Dokumentasjon | Delvis (regel 1, 9) | ~~`license:` manglar i alle 25 skjema~~ → alle 28 skjema har `license:` | **Lukka** |
| P5 Tilgjengelighet | Delvis (regel 7, 8) | ~~`license:` og SHACL/OWL~~ → brreg-skjema har no SHACL/OWL og `license:` | **Lukka** |
| P6 Gjenbruk og utveksling | Godt dekt | Manglande kryssreferansar mellom skjema | Ope (låg prio) |
| P7 Modularitet | Delvis (regel 6) | FINT-skjema overskrider 50-klasse-grensa (bronze warning, akseptert avvik) | Ope (akseptert) |
| P8 Stabilitet og utvidbarhet | Delvis (regel 9-11) | ~~`version:` manglar~~ → alle har `version:`; ~~2 sub-skjema manglar `annotations.status`~~ → lukka | **Lukka** |
| P9 Verktøyuavhengighet | Godt dekt | — | — |

---

## Vurdering per prinsipp

### P1 — Sammenheng

> *Modellene skal være sammenhengende på tvers av de forskjellige fasene av modelleringsprosessen
> og på tvers av abstraksjonsnivåer.*

**Implementert i repoet:**
- Importhierarkiet (`common-ap-no → AP-NO-profil → domenemodell`) gjev tydelege
  abstraksjonsnivå, dokumentert i `CLAUDE.md` ✓
- `in_subset: [Obligatorisk/Anbefalt/Valgfri]` er konsekvent brukt på tvers av AP-NO-profilan ✓
- `annotations.begrepsidentifikator` kobler logisk modell til begrepsnivå (konseptuelt) ✓
- Genererte artefaktar (JSON Schema, SHACL, OWL) er det fysiske nivået ✓

**Gap — inkonsistent `tema`-slot på tvers av skjema:**

Same slotnamn er definert med ulike `slot_uri` og `range` i fire skjema:

| Slotnamn | Skjema | `slot_uri` | `range` | Planlagt |
|---|---|---|---|---|
| `tema` | `dcat-ap-no-schema.yaml` | `dcat:theme` | ~~`uriorcurie`~~ → `Konsept` ✓ | Utført |
| `tema` | `modelldcat-katalog-schema.yaml` | `dcat:theme` | `Konsept` | — |
| `tema` | `xkos-ap-no-schema.yaml` | `dct:subject` | `Konsept` | Vurder omdøyping |
| `tema` | `cpsv-ap-no-schema.yaml` | `dct:subject` | `Konsept` | Vurder omdøyping |

Faktiske definisjonar frå skjema:

```yaml
# dcat-ap-no-schema.yaml (linje 841)
tema:
  slot_uri: dcat:theme
  range: uriorcurie
  multivalued: true
  description: >-
    Tema frå eit kontrollert vokabular. For norske offentlege datasett skal Los
    (https://psi.norge.no/los/) brukast som primærvokabular.
  annotations:
    gyldige_verdier: https://psi.norge.no/los/

# modelldcat-katalog-schema.yaml (linje 287)
tema:
  slot_uri: dcat:theme
  range: Konsept
  multivalued: true
  description: Tema frå eit kontrollert vokabular (dcat:theme).

# xkos-ap-no-schema.yaml (linje 281)
tema:
  slot_uri: dct:subject
  range: Konsept
  multivalued: true
  description: Fagleg tema klassifikasjonen dekkjer (dct:subject).

# cpsv-ap-no-schema.yaml (linje 905)
tema:
  slot_uri: dct:subject
  range: Konsept
  multivalued: true
  description: Emne/tema tenesta handlar om.
```

Det er to ulike inkonsistenstypar:

1. **Same predikat, ulik `range`**: `dcat-ap-no` og `modelldcat-katalog` begge brukar
   `dcat:theme`, men `dcat-ap-no` har `range: uriorcurie` medan `modelldcat-katalog`
   har `range: Konsept`. Ein Los-URI er ikkje ein `Konsept`-instans i skjemaet.
   **Avgjerd:** Endre `tema.range` frå `uriorcurie` til `Konsept` i den globale
   slotdefinisjonen i `dcat-ap-no-schema.yaml`. Ingen andre skjema vert endra.

2. **Ulikt predikat, same slotnamn**: `xkos-ap-no` og `cpsv-ap-no` brukar `dct:subject`
   for ein semantisk ulik eigenskap (fagleg klassifisering / emne), ikkje `dcat:theme`.
   Desse to bør vurderast omdøypte til `fagomrade` (i tråd med `skos-ap-no`-praksisen)
   for å unngå at `tema` assosierast med `dcat:theme` på tvers av alle skjema.

**Merk:** `xkos-ap-no`-feilen (`dct:startDate` for `tidsrom_start`) er dokumentert
som XK1 i `specs/backlog/avvik-xkos-ap-no.md`.

**Tiltak:** Sjå PI1 under.

---

### P2 — Brukerperspektiv

> *Modellene skal være så enkle som mulig for å dekke behovet, og det skal være enkelt
> for aktuelle målgrupper å forstå dem.*

**Implementert i repoet:**
- Norsk bokmål i alle `description:`-felt i modellane ✓
- Dokumentasjonsportal (mkdocs) for genererte sider ✓
- ER-diagram og PlantUML-diagram generert per skjema ✓
- Nynorsk i all portaldokumentasjon (rettleiarar, `description.md`) ✓

**Gap — `description.md` manglar i 25 av 28 skjema:**

Portaltekst-filer (`description.md`) finst no i seks skjema:
- `brreg-begrepskatalog`
- `enhetsregisteret-bvrinn`
- `register-over-aksjeeiere`
- `dcat-ap-no` *(lagt til 2026-06-19)*
- `skos-ap-no` *(lagt til 2026-06-19)*
- `modelldcat-ap-no` *(lagt til 2026-06-19)*

Repoet har vakse frå 23 til 28 skjema (`cpsv-ap-no`, `referanse-schema`, `dqv-core-schema`,
`modelldcat-katalog-schema`, `modelldcat-modell-schema` er lagt til), utan at nokon av dei
nye har fått `description.md`.

Dei resterande 22 skjema manglar ein menneskevenleg introduksjonstekst på portalen.
Utan `description.md` får eit skjema berre ein automatisk generert oversiktsside
— ingen kontekst om formål, målgruppe, avgrensing eller relasjon til andre modellar.

Dette er eit gjennomgåande gap mot «det skal være enkelt for aktuelle målgrupper å forstå dem».

**Tiltak:** Sjå PI2 under.

---

### P3 — Terminologi

> *Modellene skal etableres i samsvar med eksisterende termer og definisjoner
> så langt det lar seg gjøre.*

**Implementert i repoet:**
- AP-NO-profilan brukar terminologi frå W3C, EU og norske offentlege standardar ✓
- `see_also:` kobler klasser til begrepsdefinisjonar på `data.norge.no/concepts/` ✓
- SKOS-AP-NO-skjema representerer sjølve termar og definisjonar ✓

**Gap — `begrepsidentifikator` manglar konsekvent på domenemodell-klasser:**

Bronze-sjekken krev `annotations.begrepsidentifikator` (link til Felles begrepskatalog)
på alle klasser (unntatt `tree_root`). I praksis er dette berre tilfredsstilt i
AP-NO-profilane — ikkje i domenemodellane (`ngr-*`, `fint-*`, `oreg-*`, `samt-bu`).

Utan `begrepsidentifikator` er det ingen maskinlesbar kobling frå ein klasse til
ein kontrollert definisjon, noko som bryt prinsippet om å etablere modellar i
samsvar med eksisterande terminologi.

Dette er registrert som bronze-warning i MCP-validatoren, men er aldri systematisk
løyst opp i nokon av dei nyare domenemodellane.

**Tiltak:** Sjå PI3 under.

---

### P4 — Dokumentasjon

> *Modellene skal ha dokumentasjon som kan presenteres til aktuelle målgrupper.*

**Implementert i repoet:**
- Alle skjema har `title:` og `description:` på schema-nivå ✓
- Alle klasser og slots har `description:`-felt ✓ (94 slike i dcat-ap-no aleine)
- Dokumentasjonsportal med generated docs per skjema ✓
- Spesifikasjonar i `specs/`-mappa ✓
- `GOVERNANCE.md` og `CONTRIBUTING.md` ✓
- Alle 28 skjema har `license: https://data.norge.no/nlod/no/2.0` ✓ *(tidlegare gap — lukka)*

**Ingen gjenståande gap for P4.** Sjå P2 for det pågåande gapet om `description.md`.

---

### P5 — Tilgjengelighet

> *Modellene skal gjøres tilgjengelige på standardformater.*

**Implementert i repoet:**

Dei fleste skjema genererer eit breitt sett standardformat via `manifest.yaml`:

| Format | Dekning |
|---|---|
| JSON-LD kontekst | 21/22 skjema med manifest |
| SHACL | 20/22 skjema |
| JSON Schema | 22/22 skjema |
| OWL | 20/22 skjema |
| RDF/Turtle | 22/22 skjema |
| Protobuf | 20/22 skjema |
| ER-diagram | 22/22 skjema |
| PlantUML | 21/22 skjema |

GitHub Pages publiserer genererte artefaktar ✓

**Gap — `brreg-begrepskatalog` og `brreg-modellkatalog` mangla SHACL og OWL:**
*(Lukka — begge manifest.yaml har no `shacl: true` og `owl: true`.)*

**Gap — schema-URI-ar returnerer HTML, ikkje RDF** (sjå `avvik-peikarar-til-offentlege-ressursar.md` avvik 4):
`https://data.norge.no/ap-no/dcat-ap-no` returnerer Felles datakatalog sin HTML-side —
ikkje maskinlesbar RDF. Content negotiation er ikkje implementert. (Framleis ope.)

---

### P6 — Gjenbruk og utveksling av data

> *Modellene skal understøtte gjenbruk, utveksling og deling av data
> i og mellom virksomheter.*

**Implementert i repoet:**
- Importhierarkiet gjer AP-NO-profilane gjenbrukbare for alle domenemodeller ✓
- `class_uri`/`slot_uri` i alle AP-NO-skjema mappar til standardiserte RDF-URI-ar ✓
- Fleire serializeringsformat (JSON, RDF, Protobuf) støttar ulike utvekslingsbehov ✓
- FINT-skjema arvar frå `fint-common` for konsekvent gjenbruk av basisklassar ✓
- `lenking framfor inlining`-prinsippet sikrar at instansar kan krysskoblas via URI ✓

**Gap — ingen eksplisitt kryssreferanse mellom skjema for overlappande klasser:**

Fleire domenemodeller har klasser som semantisk overlappar med klasser i andre skjema
(t.d. `Virksomhet` / `Aktor` / `foaf:Agent` på tvers av NGR, DCAT, FINT), utan at
dette er dokumentert via `owl:sameAs` eller `skos:exactMatch` i skjemaet.

Dette gjer det vanskelegare å slå saman data frå ulike modellar, noko som er kjernen
i prinsippet om gjenbruk og utveksling.

**Tiltak:** Sjå PI6 under — låg prioritet, men relevant ved modell-integrasjon.

---

### P7 — Modularitet

> *Modellene skal deles opp i gjenbrukbare moduler.*

**Implementert i repoet:**
- Heile strukturen er bygd på modularitetsprinsippet ✓
- `common-ap-no` som delt basislag for alle AP-NO-profilar ✓
- `fint-common` som delt basislag for alle FINT-domenemodeller ✓
- Eitt skjema per domene, éin katalog per organisasjon ✓
- `CLAUDE.md` dokumenterer importhierarkiet eksplisitt ✓
- `import` i stad for copy-paste sikrar at endringar i basislag propagerer ✓

**Gap — FINT-skjema overskrider 50-klasse-grensa:**

Bronze-policy evaluerer no klassetal og gir warning for skjema med over 50 klasser
(Digdir-regel 6 — Modularitet). I praksis triggar dette på FINT-skjema:

```
fint-utdanning-schema.yaml    → 200+ klasser  (warning)
fint-administrasjon-schema.yaml → 100+ klasser  (warning)
```

Ingen av desse er splitta i undermodular endå, sjølv om importstrukturen gjer det teknisk enkelt.
Dette er eit kjent avvik — FINT-skjema arvar storleiken frå FINT API-spesifikasjonen og vert
ikkje splitta utan eksplisitt avtale med FINT-miljøet.

**Tiltak:** Sjå PI7 under.

---

### P8 — Stabilitet og utvidbarhet

> *Modellene skal være stabile og utvidbare. Nye versjoner skal utvikles ved behov,
> i kontakt med aktuelle målgrupper og innenfor et definert forvaltningsregime.*

**Implementert i repoet:**
- `GOVERNANCE.md` med RFC-prosess for brotande endringar ✓
- Semantisk versjonering med conventional commits (`specs/done/conventional-commits-modellversjonering.md`) ✓
- `adms:status`-annotasjon på dei fleste skjema (`Completed`, `UnderDevelopment` osb.) ✓
- Release-please for automatisk changelog og GitHub Releases ✓

**Gap — fire skjema mangla `version:`-felt:**
*(Lukka — alle 28 skjema har no `version:`.)*

**Gap — versjonsnummeret vert heva manuelt:**

Sjølv om `specs/done/conventional-commits-modellversjonering.md` er implementert for
commit-meldingsformatet, vert ikkje `version:`-feltet i `.yaml`-filene automatisk
oppdatert frå commit-meldingane. Det er framleis manuell prosess.

**Gap — to sub-skjema manglar `annotations.status`:**

Dei opprinnelege tre skjema som mangla status (`brreg-begrepskatalog`, `brreg-modellkatalog`,
`register-over-aksjeeiere`) har alle fått `annotations.status: Completed`.

Men to sub-skjema som vart splitta ut frå hovudskjema manglar framleis statusannotasjon:

| Skjema | `annotations.status` |
|---|---|
| `dqv-core-schema.yaml` | ✗ |
| `modelldcat-modell-schema.yaml` | ✗ |

Desse er importerte delar av høvesvis `dqv-ap-no` og `modelldcat-ap-no`, ikkje sjølvstendige
publiserte skjema. Lågare prioritet enn dei opphavlege tre.

**Tiltak:** Sjå PI8 under.

---

### P9 — Verktøyuavhengighet

> *Modellene skal være uavhengig av et spesielt IT-verktøy.*

**Implementert i repoet:**
- LinkML er open kjelde og verktøynøytralt ✓
- Genererte artefaktar (JSON Schema, SHACL, OWL, RDF, Protobuf) er opne standardar ✓
- Podman i stad for Docker — ingen kommersiell container-runtime nødvendig ✓
- GitHub Pages for publisering — standardisert statisk webpublisering ✓
- `make`-basert byggesystem — fungerer på alle POSIX-kompatible system ✓

**Ingen vesentlege gap.** CI-pipelinen er bunden til GitHub Actions, men dette er
ein teknisk avhengigheit (ikkje ei prinsippiell), og alle skript kan køyrast lokalt.

---

## Samandrag

*(Sist oppdatert 2026-06-19. Repoet har 28 skjema, opp frå 25 ved fyrste kartlegging.)*

| # | Avvik | Alvor | Prinsipp | Prioritet | Status |
|---|---|---|---|---|---|
| 1 | ~~`license:`-felt manglar i alle 25 skjema~~ | Bronze warning | P4, P5 | ~~Høg~~ | **Lukka** |
| 2 | 22/28 skjema manglar `description.md` portaltekst | Dokumentasjonsgap | P2, P4 | Middels | Ope |
| 3 | ~~4 skjema manglar `version:`-felt (inkl. common-ap-no)~~ | Bronze warning | P8 | ~~Middels~~ | **Lukka** |
| 4 | Inkonsistent `tema`-slot-definisjon på tvers av skjema | Samanhengsbrot | P1 | Middels | Ope |
| 5 | `begrepsidentifikator` manglar på dei fleste klasser | Bronze warning (ignorert) | P3 | Middels | Ope |
| 6 | ~~2 sub-skjema manglar `annotations.status` (dqv-core, modelldcat-modell)~~ | Silver warning | P8 | ~~Låg~~ | **Lukka** |
| 7 | ~~`brreg-begrepskatalog`/`-modellkatalog` manglar SHACL/OWL~~ | Tilgjengelegheitsgap | P5 | ~~Låg~~ | **Lukka** |
| 8 | FINT-skjema overskrider 50-klasse-grensa (bronze warning) | Bronze warning (akseptert avvik) | P7 | Låg | Ope (akseptert) |
| 9 | Ingen `owl:sameAs` for overlappande klasser | Gjenbruksgap | P6 | Låg | Ope |

---

## Tilrådde tiltak

### PI1 — Endre `tema.range` til `Konsept` i `dcat-ap-no-schema.yaml` ✓ *Utført*

`dcat-ap-no-schema.yaml` linje 843: `range: uriorcurie` → `range: Konsept`.
`dcat-ap-no` er no harmonert med `modelldcat-katalog` på dette feltet.

---

### PI2 — Skriv `description.md` for dei viktigaste skjema

| Skjema | Prioritet | Status |
|---|---|---|
| `dcat-ap-no` | **Høg** — hovudprofilet | ✓ Utført 2026-06-19 |
| `skos-ap-no` | **Høg** — brukt for begrepskatalog | ✓ Utført 2026-06-19 |
| `modelldcat-ap-no` | **Høg** — modellkatalog-grunnlag | ✓ Utført 2026-06-19 |
| `ngr-adresse`, `ngr-virksomhet` | Middels | Ope |
| `fint-*` | Låg — intern bruk | Ope |

---

### PI3 — Legg til `begrepsidentifikator` på nøkkelklasser i domenemodellane

Start med dei høgast-prioriterte domenemodellane og legg til
`annotations.begrepsidentifikator` på nøkkelklassene:

```yaml
# Døme for ngr-adresse-schema.yaml
Adresse:
  class_uri: ex:Adresse
  annotations:
    begrepsidentifikator: https://concept-catalog.fellesdatakatalog.digdir.no/collections/<UUID>/concepts/<UUID>
```

Sjå `specs/backlog/avvik-skos-ap-no.md` og `CLAUDE.md` for URI-format.

---

### PI4 — Legg til `license:`-felt i alle skjema ✓ *Utført*

Alle 28 skjema har `license: https://data.norge.no/nlod/no/2.0`.
Bronze-warning for Digdir-regel 7 er løyst.

---

### PI5 — Aktiver SHACL og OWL for `brreg-begrepskatalog` og `brreg-modellkatalog` ✓ *Utført*

Begge manifest.yaml har `shacl: true` og `owl: true`.

---

### PI6 — Dokumenter `owl:sameAs` for semantisk like klasser

Ved integrasjon mellom skjema (t.d. NGR ↔ DCAT) bør `see_also:` eller ein eigen
annotasjon dokumentere at klassen er semantisk ekvivalent med ein annan klasse.
Lav prioritet — relevant fyrst ved konkrete integrasjonsbehov.

---

### PI7 — Innfør klassetal-warning i MCP-validatoren ✓ *Utført*

Bronze-policy evaluerer no klassetal og gir warning for skjema med over 50 klasser
(Digdir-regel 6 — Modularitet). FINT-skjema triggar denne, men vert ikkje splitta
utan eksplisitt avtale med FINT-miljøet — avviket er akseptert og dokumentert.

---

### PI8 — Legg til manglande versjonsfelt og statusannotasjonar

**Steg 1:** ✓ *Utført* — Alle 28 skjema har `version:`.

**Steg 2:** ✓ *Utført* — `brreg-begrepskatalog`, `brreg-modellkatalog` og
`register-over-aksjeeiere` har alle `annotations.status: Completed`.

**Steg 3:** ✓ *Utført* — `dqv-core-schema.yaml` og `modelldcat-modell-schema.yaml`
har fått `annotations.status: http://purl.org/adms/status/Completed`.

---

## Prioritert handlingsliste

| # | Tiltak | Fil(ar) | Avhengigheit | Status |
|---|---|---|---|---|
| 1 | ~~PI4: `license:`-felt i alle skjema~~ | ~~Alle `*-schema.yaml`~~ | — | **Utført** |
| 2 | ~~PI8 steg 1: `version:` i 4 skjema~~ | ~~4 skjema~~ | — | **Utført** |
| 3 | ~~PI8 steg 2: `annotations.status` i 3 skjema~~ | ~~3 skjema~~ | — | **Utført** |
| 4 | ~~PI5: SHACL/OWL for begrepskatalog og modellkatalog~~ | ~~2 `manifest.yaml`~~ | — | **Utført** |
| 5 | ~~PI2: `description.md` for dcat-ap-no, skos-ap-no, modelldcat-ap-no~~ | ~~Nye filer~~ | — | **Utført** |
| 6 | ~~PI1: Endre `tema.range` til `Konsept` i `dcat-ap-no-schema.yaml`~~ | ~~`dcat-ap-no-schema.yaml`~~ | — | **Utført** |
| 7 | PI3: `begrepsidentifikator` i domenemodellane | Fleire `*-schema.yaml` | Krev begrepskatalog-avklaring | Ope |
| 8 | ~~PI8 steg 3: `annotations.status` i 2 sub-skjema (dqv-core, modelldcat-modell)~~ | ~~2 skjema~~ | — | **Utført** |
| 9 | ~~PI7: Klassetal-warning i MCP-validator~~ | ~~`mcp-linkml-validator/`~~ | — | **Utført** |

---

## Merknader

### Tilhøvet mellom prinsippa og dei 15 modelleringsreglane

«Prinsipper for informasjonsmodeller» (9 prinsipp, dette dokumentet) og «Felles
modelleringsregler for offentlig forvaltning» (15 reglar, dekt av MCP-validatoren)
er komplementære:

- Prinsippa er overordna — dei seier *kva* som er målet
- Reglane er konkrete — dei seier *korleis* målet vert nådd

Dei største gapa mot prinsippa er såleis gaper mot reglane som validatoren kjenner
til, men som ikkje er retta opp. Særleg `license:` (PI4) og `version:` (PI8) er
bronze-warnings som aldri er løyst.

### Prinsippa er rettesnor, ikkje formelle krav

Sidan standarden berre inneheld einsetningsmessige prinsipp utan underpunkt eller
sanksjonar, er dette repoet samla sett **godt i samsvar med intensjonen** bak
prinsippa. Dei strukturelle vala (modulær import-hierarki, standardformat,
fleirspråkleg terminologi, open kjeldekode) reflekterer prinsippa P6, P7, P8 og P9
på ein grunnleggjande måte.

Gapa handlar primært om metadata-felt som er lette å fylle inn (P4/PI4) og
dokumentasjon som krev meir arbeid å skrive (P2/PI2).

---

## Utført

Kartlegging og tiltaksgjennomføring fullført 2026-06-19. Følgjande tiltak er utførte:

- **PI1:** `dcat-ap-no-schema.yaml` — `tema.range` endra frå `uriorcurie` til `Konsept`
- **PI2:** `description.md` oppretta for `dcat-ap-no`, `skos-ap-no` og `modelldcat-ap-no`
- **PI4:** `license: https://data.norge.no/nlod/no/2.0` lagt til i alle 28 skjema
- **PI5:** `shacl: true` og `owl: true` aktivert i `brreg-begrepskatalog` og `brreg-modellkatalog`
- **PI7:** Bronze-policy for klassetal-warning (>50 klasser) implementert i MCP-validatoren
- **PI8 steg 1:** `version: "1.0.0"` lagt til i alle skjema som mangla det
- **PI8 steg 2:** `annotations.status` lagt til i `brreg-begrepskatalog`, `brreg-modellkatalog` og `register-over-aksjeeiere`
- **PI8 steg 3:** `annotations.status` lagt til i `dqv-core-schema.yaml` og `modelldcat-modell-schema.yaml`

Gjenståande opne punkt (ikkje utførte som del av denne spesifikasjonen):
- **PI2 (delvis):** `description.md` for `ngr-*` og `fint-*` ikkje oppretta
- **PI3:** `begrepsidentifikator` på klasser i domenemodellane — avventar begrepskatalog-avklaring
- **Gap 4 (delvis):** `xkos-ap-no` og `cpsv-ap-no` sin bruk av `dct:subject` for `tema` — separat frå PI1, avventar XK1
