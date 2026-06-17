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

| Prinsipp | MCP-dekning | Hovudgap |
|---|---|---|
| P1 Sammenheng | Delvis (regel 4, 12) | Inkonsistent slot-definisjon på tvers av skjema |
| P2 Brukerperspektiv | Delvis (regel 1, 5) | 20/23 skjema manglar portaltekst (`description.md`) |
| P3 Terminologi | Delvis (regel 13) | `begrepsidentifikator` manglar på nær alle klasser |
| P4 Dokumentasjon | Delvis (regel 1, 9) | `license:` manglar i alle 25 skjema |
| P5 Tilgjengelighet | Delvis (regel 7, 8) | `license:` manglar; 2 skjema manglar SHACL og OWL |
| P6 Gjenbruk og utveksling | Godt dekt | Manglande kryssreferansar mellom skjema |
| P7 Modularitet | Delvis (regel 6) | Ingen grense for klassetal per skjema |
| P8 Stabilitet og utvidbarhet | Delvis (regel 9–11) | 4 skjema manglar `version:`, ingen automatisk versjonsheving |
| P9 Verktøyuavhengighet | Godt dekt | — |

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

**Gap — inkonsistent slot-definisjon på tvers av skjema:**

Same slotnamn er definert med ulike `slot_uri` og `range` i ulike skjema:

| Slotnamn | Skjema | `slot_uri` | `range` |
|---|---|---|---|
| `tema` | `dcat-ap-no-schema.yaml` | `dcat:theme` | `string` |
| `tema` | `modelldcat-ap-no-schema.yaml` | `dcat:theme` | `Konsept` |
| `tema` | `xkos-ap-no-schema.yaml` | `dct:subject` | `Konsept` |
| `tidsrom_start` | `dcat-ap-no-schema.yaml` | `dcat:startDate` | `date` |
| `tidsrom_start` | `xkos-ap-no-schema.yaml` | `dct:startDate` (**feil**) | `date` |

Kvar skjema definerer desse lokalt i staden for å arve frå `common-ap-no-schema`.
Dette bryt prinsippet om samanheng på tvers av abstraksjonsnivå — same dataelement
representerar ulike semantikkar avhengig av kva skjema ein les.

**Merk:** `xkos-ap-no`-feilen (`dct:startDate`) er allereie dokumentert som XK1
i `specs/backlog/avvik-xkos-ap-no.md`.

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

**Gap — `description.md` manglar i 20 av 23 skjema:**

Portaltekst-filer (`description.md`) finst berre i tre skjema:
- `brreg-begrepskatalog`
- `enhetsregisteret-bvrinn`
- `register-over-aksjeeiere`

Dei resterande 20 skjema manglar ein menneskevenleg introduksjonstekst på portalen.
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

**Gap — `license:`-felt manglar i alle 25 skjema:**

Inga av dei 25 skjemafilene i repoet har eit `license:`-felt. Bronze-policy sjekkar
dette som warning (Digdir-regel 7 — Tilgjengeleggjering). Mangelen gjer at dokumentasjonen
er ufullstendig: ein brukar som les skjemaet kan ikkje maskinelt bestemme under kva
vilkår dei kan gjenbruke modellen.

```yaml
# Manglar i alle skjema — bør leggjast til:
license: https://data.norge.no/nlod/no/2.0   # eller CC BY 4.0
```

**Tiltak:** Sjå PI4 under.

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

**Gap — `brreg-begrepskatalog` og `brreg-modellkatalog` manglar SHACL og OWL:**

Desse to skjema er konfigurerte utan SHACL- og OWL-generering i `manifest.yaml`:

```yaml
# brreg-begrepskatalog/manifest.yaml og brreg-modellkatalog/manifest.yaml
shacl: false   # → ingen validering via SHACL
owl: false     # → ingen OWL-ontologi
```

Grunnen er sannsynlegvis at desse er datafiler framfor reine modellskjema. Men
mangelen gjer at dei to produksjonskatalogane ikkje er tilgjengelege i dei same
standardformata som dei andre skjema.

**Gap — `license:`-felt manglar** (sjå P4): utan `license:` er tilgangen formelt
udefinert, noko som hindrar gjenbruk.

**Gap — schema-URI-ar returnerer HTML, ikkje RDF** (sjå `avvik-peikarar-til-offentlege-ressursar.md` avvik 4):
`https://data.norge.no/ap-no/dcat-ap-no` returnerer Felles datakatalog sin HTML-side —
ikkje maskinlesbar RDF. Content negotiation er ikkje implementert.

**Tiltak:** Sjå PI5 under.

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

**Gap — ingen formell grense for klassetal per skjema:**

Digdir-regel 6 (Modularitet) seier at ein modell skal innehalde ei «handterleg mengde
modellelement». MCP-validatoren merkar dette som «Ikkje evaluert». I praksis er nokre
av FINT-skjema svært store:

```
fint-utdanning-schema.yaml    → 200+ klasser
fint-administrasjon-schema.yaml → 100+ klasser
```

Ingen av desse er splitta i undermodular endå, sjølv om importstrukturen gjer det teknisk enkelt.

**Tiltak:** Informasjons-gap — vurder å innføre ei soft limit (f.eks. warning over 50 klasser per skjema) i MCP-validatoren.

---

### P8 — Stabilitet og utvidbarhet

> *Modellene skal være stabile og utvidbare. Nye versjoner skal utvikles ved behov,
> i kontakt med aktuelle målgrupper og innenfor et definert forvaltningsregime.*

**Implementert i repoet:**
- `GOVERNANCE.md` med RFC-prosess for brotande endringar ✓
- Semantisk versjonering med conventional commits (`specs/done/conventional-commits-modellversjonering.md`) ✓
- `adms:status`-annotasjon på dei fleste skjema (`Completed`, `UnderDevelopment` osb.) ✓
- Release-please for automatisk changelog og GitHub Releases ✓

**Gap — fire skjema manglar `version:`-felt:**

| Skjema | `version:` til stades |
|---|---|
| `common-ap-no-schema.yaml` | ✗ |
| `xkos-ap-no-schema.yaml` | ✗ |
| `enhetsregisteret-bvrinn-schema.yaml` (bvrinn) | ✗ |
| `samt-bu-schema.yaml` | ✗ |

`common-ap-no` er spesielt kritisk: det er det grunnleggjande basislaget som alle
AP-NO-profilar er avhengige av, men det har inga versjonering.

**Gap — versjonsnummeret vert heva manuelt:**

Sjølv om `specs/done/conventional-commits-modellversjonering.md` er implementert for
commit-meldingsformatet, vert ikkje `version:`-feltet i `.yaml`-filene automatisk
oppdatert frå commit-meldingane. Det er framleis manuell prosess.

**Gap — to skjema manglar `annotations.status`:**

| Skjema | `annotations.status` |
|---|---|
| `brreg-begrepskatalog-schema.yaml` | ✗ |
| `brreg-modellkatalog-schema.yaml` | ✗ |
| `register-over-aksjeeiere-schema.yaml` | ✗ |

Utan statusannotasjon er det uklart om desse skjema er under utarbeiding, ferdigstilte
eller forelda.

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

| # | Avvik | Alvor | Prinsipp | Prioritet |
|---|---|---|---|---|
| 1 | `license:`-felt manglar i alle 25 skjema | Bronze warning (ignorert) | P4, P5 | **Høg** |
| 2 | 20/23 skjema manglar `description.md` portaltekst | Dokumentasjonsgap | P2, P4 | Middels |
| 3 | 4 skjema manglar `version:`-felt (inkl. common-ap-no) | Bronze warning (ignorert) | P8 | Middels |
| 4 | Inkonsistent `tema`-slot-definisjon på tvers av skjema | Samanhengsbrot | P1 | Middels |
| 5 | `begrepsidentifikator` manglar på dei fleste klasser | Bronze warning (ignorert) | P3 | Middels |
| 6 | 3 skjema manglar `annotations.status` | Silver warning | P8 | Middels |
| 7 | `brreg-begrepskatalog`/`-modellkatalog` manglar SHACL/OWL | Tilgjengelegheitsgap | P5 | Låg |
| 8 | Ingen klassetal-grense for store skjema (FINT) | Ikkje evaluert | P7 | Låg |
| 9 | Ingen `owl:sameAs` for overlappande klasser | Gjenbruksgap | P6 | Låg |

---

## Tilrådde tiltak

### PI1 — Flytt `tema`-slotsdefinisjon til `common-ap-no-schema`

Gjeldande situasjon: `tema`-sloten er definert lokalt i tre skjema med ulik `slot_uri`
og `range`. Samle dei i `common-ap-no-schema.yaml`:

```yaml
# I common-ap-no-schema.yaml
tema:
  slot_uri: dcat:theme
  range: uriorcurie
  multivalued: true
  description: >-
    Tema frå eit kontrollert vokabular (dcat:theme). For norske offentlege datasett
    nyttast Los (https://psi.norge.no/los/) som primærvokabular.
```

Fjernn lokale definisjonar i `dcat-ap-no`, `modelldcat-ap-no` og `xkos-ap-no`.
(Merk: `xkos-ap-no` brukar `dct:subject` for eit semantisk ulikt felt — dette bør
eventuelt gi sloten eit anna namn, t.d. `fagomrade`, i tråd med eksisterande praksis
i `skos-ap-no-schema.yaml`.)

**Avhengigheit:** XK1 i `specs/backlog/avvik-xkos-ap-no.md`

---

### PI2 — Skriv `description.md` for dei viktigaste skjema

Prioriter `description.md`-filer for skjema som vert publisert eksternt eller
er mykje brukte:

| Skjema | Prioritet |
|---|---|
| `dcat-ap-no` | **Høg** — hovudprofilet |
| `skos-ap-no` | **Høg** — brukt for begrepskatalog |
| `modelldcat-ap-no` | **Høg** — modellkatalog-grunnlag |
| `ngr-adresse`, `ngr-virksomhet` | Middels |
| `fint-*` | Låg — intern bruk |

Format: nynorsk, max 300 ord, inkluder formål, typisk brukar og relasjon til relevante
standardar. Sjå `mkdocs/docs/ny-domenemodell.md` for mal.

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

### PI4 — Legg til `license:`-felt i alle skjema

Legg til i toppen av kvart skjema (etter `annotations:`):

```yaml
license: https://data.norge.no/nlod/no/2.0
```

Dette er eit enkelt tiltak som løyser bronze-warning for alle 25 skjema og oppfyller
krav frå Digdir-regel 7, Retningslinjer for opne data (RÅ1), og prinsipp P4/P5.

**Filer:** Alle `src/linkml/**/*-schema.yaml`

---

### PI5 — Aktiver SHACL og OWL for `brreg-begrepskatalog` og `brreg-modellkatalog`

```yaml
# brreg-begrepskatalog/manifest.yaml og brreg-modellkatalog/manifest.yaml
shacl: true
owl: true
```

Vurder om `shacl_flags:` eller `owl_flags:` trengst, og køyr
`make lint` + `make roundtrip` etter endringa.

---

### PI6 — Dokumenter `owl:sameAs` for semantisk like klasser

Ved integrasjon mellom skjema (t.d. NGR ↔ DCAT) bør `see_also:` eller ein eigen
annotasjon dokumentere at klassen er semantisk ekvivalent med ein annan klasse.
Lav prioritet — relevant fyrst ved konkrete integrasjonsbehov.

---

### PI7 — Innfør klassetal-warning i MCP-validatoren

Legg til ein ny bronze-sjekk i `mcp-linkml-validator`:

```yaml
# Pseudokode for ny policy-sjekk
- id: class_count_limit
  message: "Skjema inneheld {count} klasser — vurder å dele opp i undermodular"
  severity: warning
  threshold: 50
```

Gjeld Digdir-regel 6 (Modularitet) som i dag er merka «Ikkje evaluert».

---

### PI8 — Legg til manglande versjonsfelt og statusannotasjonar

**Steg 1:** Legg `version: "1.0.0"` til skjema som manglar det:
- `common-ap-no-schema.yaml`
- `xkos-ap-no-schema.yaml`
- `enhetsregisteret-bvrinn-schema.yaml`
- `samt-bu-schema.yaml`

**Steg 2:** Legg til `annotations.status` i:
- `brreg-begrepskatalog-schema.yaml`
- `brreg-modellkatalog-schema.yaml`
- `register-over-aksjeeiere-schema.yaml`

```yaml
annotations:
  status: http://purl.org/adms/status/Completed
```

---

## Prioritert handlingsliste

| # | Tiltak | Fil(ar) | Avhengigheit |
|---|---|---|---|
| 1 | PI4: `license:`-felt i alle skjema | Alle `*-schema.yaml` | — |
| 2 | PI8 steg 1: `version:` i 4 skjema | 4 skjema | — |
| 3 | PI8 steg 2: `annotations.status` i 3 skjema | 3 skjema | — |
| 4 | PI2: `description.md` for dcat-ap-no, skos-ap-no, modelldcat-ap-no | Nye filer | — |
| 5 | PI5: SHACL/OWL for begrepskatalog og modellkatalog | 2 `manifest.yaml` | — |
| 6 | PI1: Samle `tema`-slot i common-ap-no | `common-ap-no-schema.yaml` + 3 skjema | XK1 |
| 7 | PI3: `begrepsidentifikator` i domenemodellane | Fleire `*-schema.yaml` | Krever begrepskatalog-avklaring |
| 8 | PI7: Klassetal-warning i MCP-validator | `mcp-linkml-validator/` | — |

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
