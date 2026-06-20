# Kartlegging: Avvik mot Veileder for tilgjengeliggjøring av åpne data

**Kjelde:** [data.norge.no/guide/veileder-apne-data](https://data.norge.no/guide/veileder-apne-data)  
**Utgitt av:** Digitaliseringsdirektoratet (Digdir), oppdatert 2026-01-23  
**Lisens:** CC BY 4.0

---

## Bakgrunn

Digdirs rettleiar definerer 15 krav/anbefalingar (frå regjeringas *Retningslinjer ved
tilgjengeliggjøring av offentlige data*) som offentlege verksemder skal følgje når dei
tilbyr åpne data. Dette repoet publiserer informasjonsmodellar og begrepsdata som åpne
data — rettleiaren gjeld difor òg her.

Kartlegginga nedanfor går gjennom kvart av dei 15 punkta og vurderer om repoet er i
samsvar, har eit delvis avvik eller eit fullstendig avvik. Prioriterte tiltak er lista til
slutt.

---

## Kartlegging av avvik

### Punkt 1 — Bruk åpne standardlisenser

**Krav:** Data skal ha klare vilkår for bruk. Digdir anbefaler CC0 eller CC BY 4.0.
Lisens skal angis i samsvar med DCAT-AP-NO (`dct:license`) og synleggjørast på portalen.

| Kilde | Status | Merknad |
|---|---|---|
| LinkML-skjema (`.yaml`) | ✅ Løst | Alle 28 skjema har `license: https://data.norge.no/nlod/no/2.0`; bronse-policy har `schema_has_license`-sjekk (`policies/bronze.yaml`) |
| Portalen (GitHub Pages) | ✅ Løst 2026-06-20 | `copyright:`-felt lagt til i `mkdocs/publish.sh` (Steg 4) — vises i footer på alle sider via MkDocs Material, lenkjer til MIT-lisens + viser til `license:`-feltet per skjema |
| Modellkatalog-instansar | ✅ Løst | `brreg-modellkatalog.yaml` har `lisens: .../CC_BY_4_0` på alle oppføringar (manuelt utfylt — `lisens` er ikkje del av `ANNOTATION_FIELD_MAP` i `update-modellkatalog.py`, så feltet vert ikkje automatisk oppdatert ved skjemaendring) |
| Begrepskatalog-instansar | ✅ Ikkje avvik (revidert 2026-06-20) | SKOS har ikkje noko lisens-attributt på `skos:Concept`/`Begrep` — lisens gjeld heile katalogen, ikkje enkeltbegrep. `brreg-begrepskatalog-schema.yaml` har allereie `license: https://data.norge.no/nlod/no/2.0` på skjemanivå, som dekker dette. Eit lisensfelt på `Begrep`/`BegrepContainer` ville vore eit avvik frå SKOS, ikkje ei oppretting. |

**Verifisert 2026-06-20:** Skjemametadata, modellkatalog-instansar og begrepskatalog er
allereie i orden — opphavleg avvik der er ikkje lenger aktuelt. Gjenstående scope for T1 er
smalna ned til berre portal-lisenserklæring. Sjå revidert T1 under «Tilrådde tiltak».

---

### Punkt 2 — Tilby data gratis

**Krav:** Data skal vere gratis.

| Status | Merknad |
|---|---|
| ✅ Samsvar | GitHub Pages og GitHub Releases er gratis og ope tilgjengeleg |

---

### Punkt 3 — Tilby data uten brukerregistrering

**Krav:** Data skal vere tilgjengeleg utan at brukaren must søkje om løyve eller registrere seg.

| Status | Merknad |
|---|---|
| ✅ Samsvar | GitHub Pages krev ingen innlogging |

---

### Punkt 4 — Dokumenter datasettene

**Krav:** Beskrivingar skal gjere det mogleg å oppdage, forstå og bruke data — for både
menneske og maskiner. For API-ar anbefaler rettleiaren OpenAPI Specification.

| Kilde | Status | Merknad |
|---|---|---|
| Portalen | ✅ Samsvar | Portalen har menneskeleseleg dokumentasjon per skjema |
| OpenAPI-spesifikasjonar | ✅ Løst 2026-06-20 | `openapi: true` er no standard for alle 23 skjema (sjå T6) |
| Maskinlesbar katalogoversikt | ⚠️ Avvik | Ingen `catalog.json` eller tilsvarende maskinlesbar oversikt over alle skjema |
| Registrering på data.norge.no | ⚠️ Delvis | Berre skjema med `publish_external: true` registrerast via modellkatalogen |

---

### Punkt 5 — Tilby informasjon om datakvalitet

**Krav:** Datakvalitet bør dokumenterast, kjente utfordringar skal nemnast eksplisitt.
DQV-AP-NO er det relevante rammeverket.

| Status | Merknad |
|---|---|
| ⚠️ Avvik | Bronze/silver/gold-policy dekker *skjemakvalitet*, ikkje *datakvalitet* i DQV-forstand |
| ⚠️ Avvik | Repoet har `dqv-ap-no`-skjema, men brukar det ikkje til å beskrive eigen datakvalitet |
| ⚠️ Avvik | Kjente feil er dokumenterte i `specs/bugs/`, men er ikkje eksponerte i skjemametadata |

**Tiltak:** Vurder å leggje til `dqv:hasQualityAnnotation` eller tilsvarende i skjemametadata,
t.d. med referanse til kjent mangel/avvik.

---

### Punkt 6 — Tilby oppdaterte data

**Krav:** Verksemda bør tilby oppdaterte data og vere tydeleg på oppdateringsfrekvens.

| Status | Merknad |
|---|---|
| ✅ Samsvar | GitHub Pages vert oppdatert automatisk ved kvar push til `main` |
| ⚠️ Delvis | `annotations.endringsdato` er påkravd ved silver/gold, men oppdateringsfrekvens er ikkje eksponert som metadata |
| ✅ Løst 2026-06-20 | `annotations.oppdateringsfrekvens` (`dct:accrualPeriodicity`) lagt til som silver-sjekk (sjå T7) |

---

### Punkt 7 — Gjør data synlige

**Krav:** Beskrivingar av datasett skal vere tilgjengelege på data.norge.no.
Rettleiaren anbefaler òg engelske beskrivingar.

| Status | Merknad |
|---|---|
| ⚠️ Delvis | Berre skjema med `publish_external: true` er synlege på data.norge.no |
| ⚠️ Avvik | Fleste skjema har berre `publish_external: false` og er ikkje registrerte nokon stad utanfor portalen |
| ⚠️ Avvik (konvensjon dokumentert) | Alle skildringer er på norsk bokmål — ingen engelske omsetjingar. `annotations.title_en`/`description_en` dokumentert som valfri konvensjon (sjå T8), men ingen skjema er faktisk omsett enno |

---

### Punkt 8 — Bruk maskinlesbare og standardiserte formater

**Krav:** Data skal vere i maskinlesbare og standardiserte formater (CSV, XML, JSON, RDF-serialiseringar).

| Status | Merknad |
|---|---|
| ✅ Samsvar | JSON Schema, JSON-LD, SHACL, OWL, RDF/Turtle, XSD, OpenAPI, AsyncAPI, Protobuf — svært god formatdekning |

---

### Punkt 9 — Tilby data gjennom et programmeringsgrensesnitt

**Krav:** API gjer det mogleg for programvare å gjere oppslag direkte. Rettleiaren
anbefaler REST-API med OpenAPI-dokumentasjon og Semantic Versioning.

| Status | Merknad |
|---|---|
| ✅ Løst 2026-06-20 | `openapi: true` er no standard for alle 23 skjema (sjå T6) |
| ⚠️ Avvik | Det finst ikkje noko live querybart API — berre statiske filer på GitHub Pages |
| ⚠️ Avvik | `raw.githubusercontent.com`-tilgangen er funksjonell men udokumentert som offisiell API-overflate |

**Merknad:** For informasjonsmodeller er statiske filer på faste URL-ar eit akseptabelt
alternativ til live API, men det bør dokumenterast eksplisitt.

---

### Punkt 10 — Tilby komplett nedlasting

**Krav:** Brukare skal kunne laste ned komplette datasett.

| Status | Merknad |
|---|---|
| ✅ Samsvar | Alle artefaktar er tilgjengelege som nedlastbare filer på GitHub Pages og GitHub Releases |

---

### Punkt 11 — Bruk faste adresser og unike identifikatorer

**Krav:** Data skal ha unike, permanente og hensiktsmessige adressar. Versionar og
dataelement bør vere adresserbare.

| Status | Merknad |
|---|---|
| ✅ Samsvar | Kvart skjema har `id`-felt med absolutt HTTPS-URL |
| ✅ Samsvar | GitHub Releases gir stabile versjonerte nedlastings-URL-ar |
| ⚠️ Delvis | GitHub Pages-URL-ar er stabile, men utan eksplisitt versjonssegment — `https://brreg.github.io/…/samt-bu/` peikar alltid til siste versjon |
| ✅ Løst 2026-06-20 | Dokumentert i `README.md` (vises på portalen via `index.md`): GitHub Pages = siste versjon, GitHub Releases / tag-spesifikk `raw.githubusercontent.com`-URL = kanonisk adresse for historiske versjonar |

---

### Punkt 12 — Publiser oversikt over virksomhetens data

**Krav:** Verksemda bør vedlikehalde og publisere ei oversikt over kva data dei forvaltar —
òg for data som ikkje er tilgjengelege enno. Oversikten må vere maskinlesbar (DCAT-AP-NO).

| Status | Merknad |
|---|---|
| ✅ Samsvar | Portalen listar alle skjema med menneskeleseleg oversikt |
| ⚠️ Delvis | Maskinlesbar katalogoversikt finst allereie som mekanisme (per-org modellkatalog under `src/linkml/modellkatalog/`, ModelDCAT-AP-NO `Informasjonsmodell`-instansar, vedlikehalde via `update-modellkatalog.py`) — men dekker i dag truleg berre allereie publiserte skjema, ikkje utkast/under utarbeidelse |
| ✅ Ikkje avvik (revidert 2026-06-20) | At skjema med `publish_external: false` ikkje er registrerte på data.norge.no er **tilsikta** — codeowner styrer sjølv, via modellkatalogens `informasjonsmodeller:`-liste, kva av sine skjema som skal eksponeres for ekstern hausting. Dette er ein kureringsmekanisme, ikkje eit avvik. |

**Revidert vurdering 2026-06-20:** Repoet har ein arkitektur der verksemder oppretter eigen
katalog under `src/linkml/modellkatalog/<org>-modellkatalog/` og sjølv vel kva av sine
skjema (som dei er codeowner for) som skal tilgjengeleggjøres for hausting til Felles
Datakatalog — via `informasjonsmodeller:`-lista og datafilmanifestet sitt `publish_external`.
Dette dekker det meste av Punkt 12, men rettleiaren krev òg at oversikta skal vise
*data som ikkje er tilgjengelege enno*. Det gjenstående gapet er derfor ein **konvensjon**,
ikkje ein manglande funksjon: codeowner bør liste **alle** sine skjema i modellkatalogen
(inkludert utkast, med `adms:status: UnderDevelopment`), ikkje berre dei som allereie er
ferdige/publiserte. Sjå revidert T2 og T3 under «Tilrådde tiltak».

---

### Punkt 13 — Tilpass data til brukernes behov

**Krav:** Data bør tilpassast slik at brukarar enkelt kan ta dei i bruk.

| Status | Merknad |
|---|---|
| ✅ Samsvar | Mange format (JSON Schema, Python, Protobuf, OpenAPI osb.) dekker ulike brukargrupper |
| ⚠️ Delvis | Bootstrap-scriptet gjer det enklare å bruke AP-NO-profilene ekstern, men det er ikkje tydeleg dokumentert kva format som er meint for kva brukargruppe |

---

### Punkt 14 — Oppmuntre til bruk

**Krav:** Utgivarar bør samhandle med brukarar og aktivt oppmuntre til bruk.

| Status | Merknad |
|---|---|
| ⚠️ Delvis | Bootstrap-scriptet og portalen er passive tiltak |
| ⚠️ Avvik | Ingen aktiv promotering, workshops, hackathon-deltaking eller brukarundersøkingar |

---

### Punkt 15 — Legg til rette for tilbakemeldinger

**Krav:** Brukare skal kunne gje tilbakemeldingar. Verksemda skal ha rutinar for å følgje
opp innspel.

| Status | Merknad |
|---|---|
| ✅ Løst (repo-nivå) | `CONTRIBUTING.md` forklarer korleis innspel gjevast (PR), `GOVERNANCE.md` forklarer korleis dei handsamast (RFC-prosess, konflikthandtering), `SECURITY.md` for sårbarheiter — sjå `specs/done/governance-contributing.md` |
| ✅ Løst 2026-06-20 | Ny «Om»-side (`mkdocs/docs/om.md`) lenkjer til GitHub Issues, `CONTRIBUTING.md`, `GOVERNANCE.md`, `SECURITY.md` og lisens — lagt til i nav-menyen i `mkdocs/publish.sh` |

**Verifisert 2026-06-20:** Rutina for innspel og handsaming finst no på repo-nivå (T9 er
løst). Det gjenstående gapet — synleggjøring *på portalen* for dataforbrukarar — er identisk
med T4 sitt mål. T9 er derfor avslutta og absorbert i T4.

---

## Samandrag av avvik

| # | Punkt | Status | Prioritet |
|---|---|---|---|
| 1 | Åpne standardlisenser | ⚠️ Avvik | Høg |
| 2 | Data gratis | ✅ | — |
| 3 | Uten registrering | ✅ | — |
| 4 | Dokumentasjon av datasett | ⚠️ Delvis | Høg |
| 5 | Datakvalitet | ⚠️ Avvik | Middels |
| 6 | Oppdaterte data | ⚠️ Delvis | Låg |
| 7 | Synlegheit på data.norge.no | ⚠️ Delvis | Høg |
| 8 | Maskinlesbare format | ✅ | — |
| 9 | Programmeringsgrensesnitt | ⚠️ Delvis | Middels |
| 10 | Komplett nedlasting | ✅ | — |
| 11 | Faste adresser og identifikatorar | ⚠️ Delvis | Middels |
| 12 | Oversikt over data | ⚠️ Delvis (revidert) | Middels |
| 13 | Tilpassing til brukarar | ⚠️ Delvis | Låg |
| 14 | Oppmuntre til bruk | ⚠️ Delvis | Låg |
| 15 | Tilbakemeldingar | ⚠️ Delvis | Middels |

---

## Tilrådde tiltak

### Høg prioritet

**T1 — ✅ Utført 2026-06-20**
- ~~Legg til `annotations.lisens` i silver-policy~~ — unødvendig: skjema har allereie eit
  validert `license:`-felt (sjekka av bronse-policy); ein duplikat annotasjon gir ingen ny verdi
- ~~Legg til `dct:license` i silver/gold-skjema~~ — allereie gjort, alle 28 skjema har
  `license: https://data.norge.no/nlod/no/2.0`
- ~~Legg til lisensfooter/-erklæring på portalen~~ — `copyright:`-felt lagt til i
  `mkdocs/publish.sh` Steg 4 (heredoc-blokka som genererer `mkdocs.yml`)
- ~~Vurder om `BegrepContainer`/`Begrep` i begrepskatalog bør ha eit lisensfelt~~ — ikkje
  aktuelt: SKOS modellerer ikkje lisens per `skos:Concept`, og skjemaet har allereie
  `license:` på katalognivå som dekker heile begrepskatalogen

**T2 — ✅ Utført 2026-06-20 (delvis)**
- ~~Generer `catalog.json` til GitHub Pages med metadata om alle skjema~~ — truleg unødvendig:
  per-org modellkatalog (`src/linkml/modellkatalog/`) er allereie ein maskinlesbar
  ModelDCAT-AP-NO-oversikt
- ~~Dokumenter konvensjonen at codeowner skal liste **alle** sine skjema i modellkatalogen~~ —
  lagt til i `mkdocs/docs/ny-org.md` (steg 4) og `CONTRIBUTING.md` (ny seksjon «Modellkatalog»):
  alle skjema, inkludert utkast med `adms:status: UnderDevelopment`, skal listast
- Aggregator-side på portalen som lenkjer til hver org sin modellkatalog-TTL/JSON-LD —
  **utsett**: portalen listar allereie alle skjema menneskeleg under domene-indeksane;
  ein eigen aggregator vurderes berre om data.norge.no faktisk trenger eitt samlepunkt

**T3 — ✅ Kartlagt 2026-06-20, gjenstående krev codeowner-innhald**
- ~~Vurder om fleire skjema bør ha `publish_external: true`~~ — feil verktøy: dette flagget
  styrer valideringsstrenghet for *skjemaet sjølv*, ikkje ekstern hausting
- Eksponering til Felles Datakatalog styres av om skjemaet er lista i organisasjonen sin
  modellkatalog (`informasjonsmodeller:`) **og** at modellkatalog-datafila har
  `publish_external: true` — dette er ein tilsikta codeowner-kureringsmekanisme, ikkje eit avvik
- Køyrde `python3 src/assets/scripts/update-modellkatalog.py --dry-run` for å kartlegge gapet:
  - **brreg**: `enhetsregisteret-bvrinn` (reell domenemodell) er ikkje i katalogen.
    `brreg-begrepskatalog`, `fair-metadata` og `brreg-modellkatalog` (infrastruktur/meta-skjema)
    manglar òg, men er tvilsame kandidatar for `Informasjonsmodell`-oppføring
  - **digdir, novari, ksdigital, skatteetaten, kartverket**: har registrerte skjema i
    `CODEOWNERS.md`, men **ingen modellkatalog-scaffold finst enno**
    (`make new-org-catalog ORG=<alias>` er ikkje køyrt)
  - Kan ikkje fylle inn `tittel`/`beskrivelse`/`tema`/`kontaktpunkt`/`lisens` for desse —
    krev codeowner sin fagkunnskap, ikkje noko ein kan fabrikere
- **Gjenstående handling (utenfor mitt mandat):** be brreg-codeowner legge
  `enhetsregisteret-bvrinn` til i `brreg-modellkatalog.yaml`, og be dei fem andre org-ane
  køyre `make new-org-catalog ORG=<alias>` for å opprette katalog-scaffold

### Middels prioritet

**T4 — ✅ Utført 2026-06-20**
- `mkdocs/docs/om.md` oppretta med avsnitt Bakgrunn, Kontakt (Audun Vindenes Egge,
  ave@brreg.no), Bidra og gje tilbakemelding (GitHub Issues, CONTRIBUTING.md,
  GOVERNANCE.md, SECURITY.md) og Lisens (MIT + peikar til skjema sitt `license:`-felt)
- Lagt til i nav-menyen i `mkdocs/publish.sh` (`- Om: om.md` under `- Rettleiingar:`)

**T5 — ✅ Utført 2026-06-20**
- Lagt til avsnitt i `README.md` (umiddelbart etter «Pull, ikkje push») som dokumenterer
  GitHub Releases / tag-spesifikk `raw.githubusercontent.com`-URL som kanonisk adresse
  for historiske versjonar; GitHub Pages er tydeleggjort som «alltid siste versjon»

**T6 — ✅ Utført 2026-06-20**
- Flippa `openapi: false` → `openapi: true` i alle 23 eksisterande skjema-`manifest.yaml`-filer
- La til `openapi: true` i manifest-malane i `new-model.sh`, `new-org-catalog.sh` og
  `new-begrepskatalog.sh`, og i alle fire eksempelblokkene i `manifest-config.md`
- Verifiserte risikoen for skjema utan `tree_root` (AP-NO, FAIR) før utrulling: køyrde
  `gen-openapi.py` lokalt mot allereie genererte JSON Schema for `dcat-ap-no`,
  `fair-metadata`, `fint-administrasjon`, `brreg-begrepskatalog` og `brreg-modellkatalog`
  — alle produserte gyldig OpenAPI-struktur med komponentskjema (`paths: {}`,
  schema-bibliotek utan endepunkt). Full validering med `openapi-spec-validator` krev
  podman-bygd container — anbefalt som oppfølging via `make gen-openapi` før neste publish

**T7 — ✅ Utført 2026-06-20**
- Ny sjekk `schema_has_annotation_oppdateringsfrekvens` i `policies/silver.yaml` (warning),
  same mønster som `utgiver`/`endringsdato`/`status` — krev URI frå EU sin Frequency
  Named Authority List (`dct:accrualPeriodicity`)
- Lagt til rad i `policies/README.md` sin silver-sjekkliste
- Lagt til i eksempel-annotasjonsblokka i `mkdocs/docs/ny-org.md` (steg 3)
- **Utenfor scope:** å vise `oppdateringsfrekvens` i genererte `Informasjonsmodell`-instansar
  (modellkatalogen) krev ein ny slot i delt infrastruktur (`modelldcat-ap-no-schema.yaml`)
  og endring i `update-modellkatalog.py` sin `ANNOTATION_FIELD_MAP` — det er ei endring i
  felles infrastruktur som krev eigen vurdering/godkjenning (sjå `GOVERNANCE.md`), ikkje
  noko som høyrer til denne spesifikke validator-policy-endringa

### Låg prioritet

**T8 — ✅ Vurdert og dokumentert 2026-06-20 (konvensjon, ikkje policy-krav)**
- Vurdering: `title_en`/`description_en` bør **ikkje** vere eit enforced silver-policy-krav
  — omsetjing av 28 skjema sine titlar/skildringar krev fagkunnskap per skjema og kan
  ikkje fabrikeres på vegne av codeowner-ar
- Dokumentert som valfri konvensjon i `mkdocs/docs/ny-domenemodell.md`:
  `annotations.title_en` / `annotations.description_en`, fylt inn av codeowner ved behov
- Ingen eksisterande skjema er omsette — det er ei separat, frivillig oppgåve per skjema

**T9 — Tilbakemeldingsrutinar (Punkt 14, 15) — ✅ Løst, avslutta 2026-06-20**
- ~~Opprett ein enkel `CONTRIBUTING.md` eller portalside som forklarer korleis brukarar
  kan gje innspel og korleis dei vert handsama~~ — `CONTRIBUTING.md` + `GOVERNANCE.md`
  finst og dekker dette (sjå `specs/done/governance-contributing.md`)
- Gjenstående gap (synleggjøring på portalen) er identisk med T4 og er flytta dit

---

## Prioritert handlingsliste

| # | Tiltak | Fil / område | Avhengigheit |
|---|---|---|---|
| 1 | ~~T1: Lisens i silver-policy og portal~~ | `mkdocs/publish.sh` | ✅ Utført 2026-06-20 |
| 2 | ~~T2: Dokumenter konvensjon — list alle skjema (inkl. utkast) i org-modellkatalog~~ | `CONTRIBUTING.md`, `mkdocs/docs/ny-org.md` | ✅ Utført 2026-06-20 |
| 3 | ~~T3: Kartlegg codeowner-kuratering av modellkatalog~~ — gjenstående krev codeowner-handling | `update-modellkatalog.py`, org sine `informasjonsmodeller:`-lister | ✅ Kartlagt 2026-06-20 |
| 4 | ~~T4: Ny «Om»-side (`om.md`) med kontakt, lenkjer og lisens~~ | `mkdocs/docs/om.md`, `mkdocs/publish.sh` (nav) | ✅ Utført 2026-06-20 |
| 5 | ~~T5: Dokument versjonerte URL-ar~~ | `README.md` | ✅ Utført 2026-06-20 |
| 6 | ~~T6: `openapi: true` som standard for alle skjema~~ | `manifest.yaml`-malen + 23 eksisterande `manifest.yaml`-filer | ✅ Utført 2026-06-20 |
| 7 | ~~T7: `dct:accrualPeriodicity` i silver~~ | `mcp-linkml-validator/policies/` | ✅ Utført 2026-06-20 |
| 8 | ~~T8: Engelske beskrivingar~~ — vurdert, dokumentert som valfri konvensjon | `mkdocs/docs/ny-domenemodell.md` | ✅ Utført 2026-06-20 |
| 9 | ~~T9: CONTRIBUTING.md / tilbakemeldingsside~~ — ✅ løst, absorbert i T4 | — | — |

---

## Avhengigheiter

- T1 bør gjennomførast før T3 sidan `dct:license` er ein DCAT-AP-NO-føresetnad for
  registrering på data.norge.no
- T2 (`catalog.json`) er grunnlag for maskinlesbar oppdaging og er uavhengig av dei andre
  tiltaka — kan gjennomførast raskt

---

## Utført (2026-06-20)

Alle tiltak (T1–T9) er utførte, kartlagte eller medvite avgrensa i scope:

- **T1 (lisens):** `copyright:`-felt lagt til i `mkdocs/publish.sh` (Steg 4, genererer
  `mkdocs.yml`) — viser MIT-lisens for repoet + peikar til `license:`-feltet per skjema.
  Skjemametadata, modellkatalog-instansar og begrepskatalog var allereie i orden ved
  verifisering — ingen avvik der.
- **T2 (maskinlesbar katalogoversikt):** Konvensjon dokumentert i `mkdocs/docs/ny-org.md`
  (steg 4) og ny seksjon «Modellkatalog» i `CONTRIBUTING.md`: codeowner skal liste **alle**
  sine skjema i modellkatalogen, inkludert utkast med `adms:status: UnderDevelopment`.
  Eit eige `catalog.json`-artefakt vart vurdert som unødvendig — modellkatalogen er
  allereie ein maskinlesbar ModelDCAT-AP-NO-oversikt. Ein aggregator-side er **utsett**.
- **T3 (codeowner-kuratering):** Kartlagt via `update-modellkatalog.py --dry-run`:
  `enhetsregisteret-bvrinn` manglar i brreg sin modellkatalog; digdir, novari, ksdigital,
  skatteetaten og kartverket har registrerte skjema men ingen modellkatalog-scaffold enno.
  Faktisk tillegging av oppføringar er **ikkje gjort** — krev codeowner sin fagkunnskap
  (tittel, tema, kontaktpunkt) og kan ikkje fabrikeres.
- **T4 (Om-side):** `mkdocs/docs/om.md` oppretta (Bakgrunn, Kontakt, Bidra og gje
  tilbakemelding, Lisens) og lagt til i nav-menyen i `mkdocs/publish.sh`.
- **T5 (versjonerte URL-ar):** Dokumentert i `README.md` rett etter «Pull, ikkje push»-merknaden.
- **T6 (OpenAPI):** `openapi: true` satt som standard i alle 23 eksisterande
  skjema-`manifest.yaml`-filer og i scaffold-malane (`new-model.sh`, `new-org-catalog.sh`,
  `new-begrepskatalog.sh`). Risiko for skjema utan `tree_root` verifisert lokalt med
  `gen-openapi.py` mot fem representative skjema før utrulling.
- **T7 (oppdateringsfrekvens):** Ny silver-sjekk `schema_has_annotation_oppdateringsfrekvens`
  i `policies/silver.yaml`, dokumentert i `policies/README.md` og `ny-org.md`. Å vise feltet
  i genererte `Informasjonsmodell`-instansar er **utenfor scope** — krev endring i delt
  AP-NO-infrastruktur (`modelldcat-ap-no-schema.yaml`) som krev eigen godkjenning.
  Faktisk utfylling av `annotations.oppdateringsfrekvens` på eksisterande skjema er **ikkje gjort**.
- **T8 (engelske skildringar):** Vurdert og avgjort at dette **ikkje** skal vere eit
  enforced policy-krav (omsetjing krev fagkunnskap per skjema). Dokumentert som valfri
  konvensjon (`annotations.title_en`/`description_en`) i `mkdocs/docs/ny-domenemodell.md`.
  Ingen eksisterande skjema er faktisk omsette.
- **T9 (tilbakemeldingsrutinar):** Var allereie løst via `CONTRIBUTING.md`/`GOVERNANCE.md`
  (sjå `specs/done/governance-contributing.md`); det gjenstående gapet blei absorbert i T4.

**Avvik frå opphavleg plan:** T2, T3 og T7 har delar som krev innhald/fagkunnskap frå
codeowner-ar (faktiske katalogoppføringar, utfylte annotasjonsverdiar) som ikkje kan
fabrikeres — desse er kartlagte/dokumenterte som konvensjon, men ikkje fullt gjennomførte
i datainnholdet. T1 sitt opphavlege forslag om eit eige `annotations.lisens`-felt og T6 sitt
opphavlege forslag om eit nytt `catalog.json`-script vart forlatne som unødvendige etter
verifisering mot eksisterande mekanismer.
