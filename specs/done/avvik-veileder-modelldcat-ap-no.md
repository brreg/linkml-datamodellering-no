# Kartlegging: Avvik mot Veileder for beskrivelse av informasjonsmodeller (ModellDCAT-AP-NO)

**Kjelde:** [data.norge.no/guide/veileder-modelldcat-ap-no](https://data.norge.no/guide/veileder-modelldcat-ap-no)  
**Versjon:** 1.0.1, oppdatert 2025-08-22  
**Samanheng:** ModellDCAT-AP-NO v1.1, DCAT-AP-NO 2.0

---

## Bakgrunn

Rettleiaren forklarer korleis informasjonsmodellar og modellkatalogar
skal beskrivas i ModellDCAT-AP-NO for publisering til Felles datakatalog.

Repoet har:
- `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml` — LinkML-implementasjon av ModellDCAT-AP-NO
- `src/linkml/modellkatalog/brreg-modellkatalog/` — datafile med éin modellkatalog og to informasjonsmodellar
- `data_policy: felles-datakatalog` — datafila vert publisert til Felles datakatalog

---

## Kartlegging av avvik

### 1 — Berre 2 av ~21 skjema er registrerte i modellkatalogen

`brreg-modellkatalog.yaml` listar berre `ngr-virksomhet` og
`register-over-aksjeeiere`. Alle andre skjema (FINT-modellane, NGR-adresse,
samt-bu, AP-NO-profilane osb.) er ikkje eksponerte i Felles datakatalog.

Rettleiaren: *«det er enklere å finne, forstå, sammenligne og gjenbruke
informasjonsmodeller i offentlig sektor»* — dette forutset at modellane faktisk
er tilgjengelege i katalogen.

**Avklart:** Det skal autogenereres éin modellkatalog per organisasjon i
`CODEOWNERS.md`, med eit innhald styrt av `annotations.utgiver` i kvart skjema
(same mønster som `update-modellkatalog.py` og `make new-org-catalog ORG=<alias>`
allerede implementerer, jf. `CODEOWNERS.md`). Infrastrukturen for dette finst
altso allerede — det som manglar er at `make new-org-catalog` faktisk er køyrt
for dei resterande 5 organisasjonane (berre `brreg-modellkatalog` har ein
katalogkatalog i dag), og at `make update-modellkatalog` er køyrt etterpå for
å fylle katalogane.

**Avklart — domeneeksklusjon:** Domena `referanse`, `modellkatalog` og
`begrepskatalog` skal **ekskluderast** frå autogenereringa sitt kildeskan.
Grunngjeving:
- `modellkatalog` er **outputdomenet** — autogenereringa produserer sjølve
  katalogane (`src/linkml/modellkatalog/<org>-modellkatalog/`) der. Skannar
  scriptet dette domenet som kildeskjema, vil ein katalog kunne ende opp med
  eit oppslag for seg sjølv (sjølvreferanse).
- `begrepskatalog` beskriv SKOS-AP-NO-baserte begrepskatalogar (Felles
  begrepskatalog), ikkje ModellDCAT-AP-NO-informasjonsmodellar — desse er ein
  annan artefakttype og skal ikkje listast som `Informasjonsmodell` i ein
  modellkatalog.
- `referanse` er eit ikkje-produksjonsskjema (sjå under) og skal heller ikkje
  inkluderast, sjølv om sti-djupna i dag uansett hindrar at det blir
  plukka opp (sjå avsnittet om `referanse-schema.yaml` under).

Dette krev ei endring i `update-modellkatalog.py`: legg til ei
ekskluderingsliste (`EXCLUDED_DOMAINS = {"referanse", "modellkatalog",
"begrepskatalog"}`) i `load_annotated_schemas()`, slik at domenet hoppast
over uavhengig av sti-djupne eller `annotations.utgiver`.

Tabellen under viser kva modellkatalog som vil bli generert med kva skjema,
basert på dagens `annotations.utgiver`-verdiar i skjema-YAML-filene, **etter**
at domeneeksklusjonen er innført:

| Katalog (`catalog_slug`) | Org-URI (orgnr) | Skjema (basert på `annotations.utgiver`) |
|---|---|---|
| `brreg-modellkatalog` | `974760673` | `ngr-virksomhet`, `oreg/enhetsregisteret-bvrinn`, `oreg/register-over-aksjeeiere`, `fair/fair-metadata` |
| `digdir-modellkatalog` | `991825827` | `ap-no/common`, `ap-no/cpsv-ap-no`, `ap-no/dcat-ap-no`, `ap-no/dqv-ap-no`, `ap-no/modelldcat-ap-no`, `ap-no/skos-ap-no`, `ap-no/xkos-ap-no` |
| `novari-modellkatalog` | `985870714` | `fint-administrasjon`, `fint-arkiv`, `fint-common`, `fint-okonomi`, `fint-personvern`, `fint-ressurs`, `fint-utdanning` |
| `ksdigital-modellkatalog` | `971032146` | `samt/samt-bu` |
| `skatteetaten-modellkatalog` | `974761076` | `ngr/ngr-person` |
| `kartverket-modellkatalog` | `971040238` | `ngr/ngr-adresse`, `ngr/ngr-eiendom` |

`begrepskatalog/brreg-begrepskatalog` og `modellkatalog/brreg-modellkatalog`
(sjølv) er fjerna frå `brreg-modellkatalog`-rada i tabellen sidan domena deira
no er ekskludert frå skanninga.

**Utført (steg 1 av MD2):** `modelldcat-katalog-schema.yaml` hadde ingen
`annotations`-blokk — lagt til `utgiver: https://data.norge.no/organizations/991825827`
(digdir), så skjemaet no høyrer til `digdir-modellkatalog`.

`referanse-schema.yaml` sin `utgiver: TODO` er retta til
`https://data.norge.no/organizations/974760673` (brreg). **Avvik frå plan:**
under arbeidet vart det avdekt at `update-modellkatalog.py` brukar eit
glob-mønster (`src/linkml/*/*/*.yaml`, krev domene/modell/fil — 3 nivå) som
ikkje matchar `referanse-schema.yaml` (ligg direkte i `src/linkml/referanse/`,
2 nivå). Filen blir altso **ikkje** plukka opp av scriptet uansett — retting
av `utgiver` der var ei generell annotasjons-opprydding, ikkje ei
føresetnad for at filen skal dukke opp i ein modellkatalog. Filen er òg
uttrykkelig eit ikkje-produksjonsskjema («Ikkje ein del av produksjonsdomenet»).

**Status:** ✓ MD2 fullført (steg 1-5, sjå MD2 under) — alle 6 organisasjonar
har no eigen modellkatalog med alle ~23 skjema registrerte. Gjenstår berre
redaksjonelt innhald (`tema`, kontaktpunkt-namn, katalogskildring) som
medvite er utelate frå autogenereringa — krev forretningskunnskap, ikkje
teknisk arbeid.

---

### 2 — Modelltype (`dct:type`) manglar i alle informasjonsmodellar

Rettleiaren definerer eit vokabular for klassifisering av modelltypar:

| Type | Skildring |
|---|---|
| Konseptuell modell | Skildrar viktige konsept og samanhengar i eit fagdomene |
| Logisk modell | Skildrar kva informasjon som inngår, uavhengig av teknologi |
| Fysisk modell | Logisk modell tilpassa datautveksling/lagring for ei konkret løysing |
| Fellesmodell | Til felles bruk på tvers av verksemder og forretningsområde |
| Anvendelsesmodell | Retta mot eit spesifikt bruksområde i ein avgrensa kontekst |

Ingen av informasjonsmodellane i `brreg-modellkatalog.yaml` har `dct:type`
satt. `modelldcat-ap-no-schema.yaml` har `type_concept`-slot (valgfri) men den
er ikkje fylt ut i datafila, og det er heller ikkje tydeleg kva kontrollert
vokabular som skal brukast.

**Forslag til løysing:** Den kontrollerte vokabularen finst allerede
dokumentert i skjemaet — `modelldcat-katalog-schema.yaml` har ein
`type_concept`-`slot_usage` på `Informasjonsmodell` med
`annotations.gyldige_verdier`:

```
https://data.norge.no/vocabulary/modelldcatno#LogicalDataModel
https://data.norge.no/vocabulary/modelldcatno#ConceptualDataModel
https://data.norge.no/vocabulary/modelldcatno#PhysicalDataModel
```

Berre 3 av dei 5 typane rettleiaren listar (Konseptuell, Logisk, Fysisk) har
ein kjent `modelldcatno#`-URI i repoet i dag — det finst ingen dokumentert
URI for Fellesmodell eller Anvendelsesmodell. I tråd med konvensjonen for
Los-URI-ar (CLAUDE.md: «finst ikkje — berre bruk dei som faktisk finst»),
bør vi **ikkje** finne opp lokale URI-ar for desse to, men la `type_concept`
stå tom for modellar som ikkje passar dei 3 dokumenterte typane, til Digdir
publiserer fullstendig vokabular.

Foreslått klassifiseringsregel for utfylling:
- **Logisk modell** (`LogicalDataModel`) — standardvalet for domenemodellane
  (NGR, OREG, FINT, SAMT-BU osb.), sidan LinkML-skjema skildrar
  informasjonsinnhald uavhengig av lagringsteknologi (jf. rettleiarens
  definisjon, og prinsippet «Lenking fremfor inlining»)
- **Konseptuell modell** (`ConceptualDataModel`) — AP-NO-profilane
  (dcat-ap-no, skos-ap-no, dqv-ap-no, cpsv-ap-no, modelldcat-ap-no, xkos-ap-no,
  common-ap-no), sidan desse skildrar konsept og samanhengar definert av
  W3C/EU-standardar, ikkje ei konkret datautvekslingsløysing
- **Fysisk modell** (`PhysicalDataModel`) — vurderast individuelt; ingen
  skjema i repoet er tydeleg identifisert som dette i dag
- **Fellesmodell/Anvendelsesmodell** — ikkje sett `type_concept` før gyldig
  URI finst; eventuelt søk Digdir om vokabularet er utvida

**Status:** ✓ Forslag klart — krev verifisering av URI-ane mot spesifikasjonen
og klassifisering av enkeltmodellar før utfylling (sjå MD3)

---

### 3 — `inneholder_modellelement` (anbefalt) er tom for alle modellar

Rettleiaren skil mellom to publiseringsformar:
1. Utan modellelement — berre lenke til heimeside (minimum, akseptabelt)
2. **Med modellelement** — heile modellen eksponert for automatisk høsting

Alle informasjonsmodellar i datafila brukar alternativ 1: berre
`informasjonsmodellidentifikator` (lenke til portalen). Ingen modellelement
(`Objekttype`, `Attributt`, `Kodeliste` osb.) er inkluderte.

Dette er det største funksjonelle gapet mot rettleiaren. Automatisk høsting
av modellinnhald til Felles datakatalog krev alternativ 2.

**Avklart:** Vi går for alternativ 2 — heile modellen skal eksponeres med
faktiske modellelement (`Objekttype`, `Attributt`, `Kodeliste` osb.) for
automatisk høsting, ikkje berre lenke til portalen.

**Status:** ✓ Avklart — skal implementeres (sjå MD5)

---

### 4 — `utgiver`-URI-format avvik frå rettleiaren

Rettleiaren anbefaler:
```
dct:publisher <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/974760673>
```

Datafila og `CLAUDE.md` brukar:
```
utgiver: https://data.norge.no/organizations/974760673
```

**Forkasta etter nærare vurdering:** `specs/done/publisering-felles-datakatalog.md`
viser at `data.norge.no/organizations/<orgnr>` for `dct:publisher` var ei
**medviten, allerede gjennomført designavgjerd** for heile «Felles
datakatalog»-pipelinen — ikkje ein forglemmelse spesifikk for modellkatalog.
Same format brukast identisk for NGR (`ngr-adresse`, `ngr-eiendom`,
`ngr-person`, `ngr-virksomhet`) og OREG (`register-over-aksjeeiere`), og alle
6 datafilene valideras av **éin delt** `felles-datakatalog`-policy med éin
`instance_slot_uri_pattern`-sjekk (`^https://data\.norge\.no/organizations/\d{9}$`)
og éin `known_values`-liste.

Å byte formatet berre for modellkatalog ville gjort `dct:publisher` inkonsistent
mellom artefakttypar som valideras av den **same** policy-sjekken — enten ved å
bryte det delte regexet, eller ved å gjere policyen artefakt-type-avhengig.
Det er verre enn avviket frå rettleiaren. `data.norge.no/organizations/<orgnr>`
står ved lag for alle felles-datakatalog-publiseringar, inkludert modellkatalog.

**Status:** ✗ Forkasta — eksisterande, medviten konvensjon i
`specs/done/publisering-felles-datakatalog.md` veg tyngre enn rettleiar-tilrådinga.
Ingen tiltak (MD1 utgår).

---

### 5 — `versjonsnummer` og `versjonsmerknad` manglar

Rettleiaren anbefaler `owl:versionInfo` (versjonsnummer) og
`adms:versionNotes` (versjonsmerknad) for å dokumentere endringar utan
å opprette ny instans.

Informasjonsmodellane i datafila har ikkje desse felta fylt ut, sjølv
om slota finst i `modelldcat-ap-no-schema.yaml`. Versjonssporet frå
`release-please` (t.d. `ngr-virksomhet` = `1.0.0`) vert ikkje
synkronisert til modellkatalogen.

**Avklart:** `versjonsnummer` skal synkroniseres automatisk frå
`release-please` (versjonen pr. skjema i `release-please-manifest.json`)
i staden for å fyllast ut manuelt i `brreg-modellkatalog.yaml`.

**Status:** ✓ Avklart — skal implementeres (sjå MD4)

---

### 6 — `status` og `endringsdato` manglar i informasjonsmodell-instansar

Slota `status` og `endringsdato` finst i `modelldcat-ap-no-schema.yaml`
(valgfrie), men er ikkje fylt ut i `brreg-modellkatalog.yaml`. Dette er
dei same annotasjonane som silver-policy krev i skjema-YAML-filene, men
dei vert ikkje propagert til modellkatalog-instansen.

**Avklart:** `status` og `endringsdato` skal hentes frå `annotations.status`
og `annotations.endringsdato` i kvart skjema-YAML (jf. silver-annotasjonane
i CLAUDE.md) og propageres automatisk til modellkatalog-instansen — ikkje
fyllast ut manuelt.

**Status:** ✓ Avklart — skal implementeres (sjå MD4)

---

### 7 — Ingen relasjoner til begreper, datasett eller datatjenester

Rettleiaren har ein eigen seksjon om å knytte informasjonsmodellar til
tilhøyrande omgrep (`dct:references` → begrepskatalog-oppslag) og
datasett (`dcat:servesDataset`). 

Datafila har ingen slike koplingar, sjølv om repoet har både
begrepskatalog (`brreg-begrepskatalog`) og modellkatalog.

**Avklart:** `annotations.begrepsidentifikator` er forkasta som mekanisme her
— det er ein LinkML-metadata-annotasjon for skjemaforfattarar og serialiseres
ikkje til RDF på instansnivå, så den samsvarar ikkje direkte med rettleiarens
krav om faktiske triples. I staden skal det leggjast til nye RDF-property-slots
i `modelldcat-katalog-schema.yaml`:
- `relatert_begrep` (`slot_uri: dct:references`, `range: Konsept`, multivalued)
  på `Informasjonsmodell` (og evt. `Modellelement`)
- `tilgjengeliggjoer_datasett` (`slot_uri: dcat:servesDataset`, `range: Datasett`,
  multivalued) på `Informasjonsmodell`

`Konsept` og `Datasett` finst allerede i importkjeda (via `dcat-ap-no-schema`)
og følgjer lenking-fremfor-inlining-prinsippet, så slottene peikar naturleg
til eksterne URI-ar — same mønster som det eksisterande `begrep`-slottet
(`dct:subject`) som `Informasjonsmodell` allerede har via arv frå
`dcat-ap-no-schema`.

**Status:** ✓ Avklart — nye slots i skjemaet (sjå MD6)

---

## Samandrag

| # | Avvik | Status | Prioritet |
|---|---|---|---|
| 1 | Berre 2 av ~21 skjema i modellkatalogen | ✓ Utført (MD2 — alle 23 skjema registrerte i 6 org-katalogar) | Høg |
| 2 | Modelltype (`dct:type`) manglar | ✓ Utført (MD3 — 23 instansar klassifiserte) | Middels |
| 3 | `inneholder_modellelement` er tom | ✓ Avklart (alt. 2) | Høg (kompleks) |
| 4 | `utgiver`-URI-format avvik frå rettleiar | ✗ Forkasta (kolliderer med medviten konvensjon) | — |
| 5 | `versjonsnummer` og `versjonsmerknad` manglar | ✓ `versjonsnummer` utført (MD4); `versjonsmerknad` medvite utelate (ingen kjelde) | Middels |
| 6 | `status` og `endringsdato` manglar i instansar | ✓ Utført (MD4 — fanst allerede, no faktisk køyrt) | Låg |
| 7 | Ingen relasjonar til begrep/datasett | ✓ Utført (MD6 — relatert_begrep fylt; datasett-slot kopla, men umogleg å fylle, ingen Datasett-instansar finst) | Låg |

---

## Tilrådde tiltak

### MD1 — ~~Rett `utgiver`-URI-format~~ (Avvik 4) — **utgår**

~~Avklart: `dct:publisher` skal bruke
`https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/<orgnr>`~~

**Forkasta** (sjå avvik 4 over): `data.norge.no/organizations/<orgnr>` er ein
medviten, allerede dokumentert konvensjon delt med NGR/OREG under same
`felles-datakatalog`-policy. Ingen endring. MD2-MD6 har **ingen avhengigheit**
til MD1 lenger (sjå oppdatert avhengigheitsliste under).

---

### MD2 — Rull ut per-org-modellkatalogar for alle organisasjonar (Avvik 1)

Avklart: bruk den eksisterande autogenererings-infrastrukturen
(`update-modellkatalog.py`, `make new-org-catalog ORG=<alias>`,
`CODEOWNERS.md`-frontmatter) i staden for å vedlikeholde
`brreg-modellkatalog.yaml` manuelt. Steg:

1. ✓ Legg til domeneeksklusjon i `update-modellkatalog.py` (`load_annotated_schemas()`):
   hopp over skjema i domena `referanse`, `modellkatalog` og `begrepskatalog`
   (sjå avvik 1 for grunngjeving). Verifisert: 26 → 23 skjema med
   `annotations.utgiver` etter eksklusjonen (dei 3 ekskluderte domena trekt frå).
2. ✓ Utvida `update-modellkatalog.py` (`process_org()`) til å faktisk
   *skrive* `unmatched`-stubs til katalogfila, ikkje berre printe dem.
   `make_stub()`-resultatet vert no lagt til `entries`-lista og
   `modellkataloger[0].har_del`/`.modell` (same mønster som eksisterande
   oppføringar i `brreg-modellkatalog.yaml`). Verifisert med
   `--dry-run --org brreg`: 2 oppdaterte (`ngr-virksomhet`,
   `register-over-aksjeeiere`) + 2 nye stubs (`fair-metadata`,
   `enhetsregisteret-bvrinn`) — stemmer med dei 4 brreg-skjemaa i tabellen
   under avvik 1.
3. ✓ Køyrt `make new-org-catalog ORG=<alias>` for `digdir`, `novari`,
   `ksdigital`, `skatteetaten`, `kartverket`. **Avvik frå plan:** oppdaga og
   retta ein eksisterande bug i `new-org-catalog.sh` — `eval "$ORG_META"`
   brukte uquota `key=value`-linjer frå Python, som brakk for verdiar med
   mellomrom (t.d. `catalog_title=Digitaliseringsdirektoratet - Modellkatalog`
   feila med «-: command not found», `name=Novari IKS` feila med «IKS: command
   not found»). Fiksa med `shlex.quote()` rundt Python-outputverdiane før
   `eval`. Alle 5 katalogar oppretta etter fiksen.
4. ✓ Køyrt `make update-modellkatalog` for å fylle alle 6 katalogane frå
   `annotations.*` i skjema-YAML-filene, med autoinnsette stubs frå steg 2.
   Resultat (etter eksklusjonen i steg 1): 23 skjema fordelt nøyaktig som
   tabellen over tilsa — brreg 4 (2 oppdaterte, 2 nye stubs: `fair-metadata`,
   `enhetsregisteret-bvrinn`), digdir 8 nye, novari 7 nye, ksdigital 1 ny,
   skatteetaten 1 ny, kartverket 2 nye.

   **Avvik frå plan (3 funne underveis, alle rettra):**
   - **Bug i `new-org-catalog.sh`:** `eval "$ORG_META"` brukte uquota
     `key=value`, brakk på verdiar med mellomrom (sjå steg 3-notatet over).
     Fiksa med `shlex.quote()`.
   - **Bug i samme skript sin YAML-mal:** `- TODO: <tekst>` parsa som
     ein nøsta dict (`{TODO: "<tekst>"}`) i staden for ein streng — braut
     `jsonschema`-validering (`beskrivelse`/`navn_aktoer` forventar `string`).
     Fiksa med anførselstegn (`- "TODO: <tekst>"`) i malen, og sed-retta dei
     5 allereie genererte datafilene.
   - **Stale `annotations.utgivelsesdato`/`endringsdato: "TODO"`** i
     `register-over-aksjeeiere-schema.yaml` — `update-schema-dates.py` fyller
     berre `utgivelsesdato` når feltet er *heilt fraværande*, ikkje når det
     allereie står som placeholder-streng, så denne var permanent fastlåst.
     Retta til dei reelle datoane (`2024-01-01`/`2026-06-19`) som allereie
     fanst i den gamle hand-vedlikehaldne `brreg-modellkatalog.yaml`.
   - Alle 6 katalogar validerer no `0 errorCount` under
     `POLICY=felles-datakatalog`.
   - **TTL-roundtrip:** Alle 5 nye org-katalogar feiler `roundtrip-ttl` med
     samme rotårsak som **BUG-1** (`specs/bugs/langstring-rdflib-roundtrip.md`)
     — utvida BUG-1 sin skip-liste i `tests/test_make.sh` og
     «Berørte skjema»-tabellen til å inkludere dei 5 nye katalognamna.
5. ✓ Delvis utført: `lisens: TODO` retta til
   `http://publications.europa.eu/resource/authority/licence/CC_BY_4_0` for
   alle nye stub-oppføringar i alle 6 katalogar (klar presedens — same verdi
   som alle eksisterande oppføringar i `brreg-modellkatalog.yaml` allereie
   brukte). **Avklart med brukar:** `tema` (krev Los-taksonomi-vurdering per
   skjema), kontaktpunkt-namn (`navn_aktoer`) og katalogskildring
   (`beskrivelse` på `Modellkatalog`-nivå) står ved lag som `TODO` — krev
   forretningskunnskap/redaksjonelt innhald, ikkje teknisk utleidbart. Alle
   6 katalogar validerer med `errorCount: 0` under `felles-datakatalog`
   etter lisens-fiksen.

✓ **Utført:** `annotations.utgiver` sett på `modelldcat-katalog-schema.yaml`
(digdir, `991825827`) og retta på `referanse-schema.yaml` (brreg, `974760673`,
generell annotasjons-opprydding — filen blir ikkje skanna av scriptet uansett,
sjå avvik 1). Alle steg 1-5 over er no utførte (sjå detaljar per steg over) —
MD2 er fullført, med unntak av medvite utelate redaksjonelle TODO-felt
(tema, kontaktpunkt-namn, katalogskildring).

**Filer:** `CODEOWNERS.md` (verifisering), nye `src/linkml/modellkatalog/<org>-modellkatalog/`-katalogar,
`modelldcat-katalog-schema.yaml` ✓, `referanse-schema.yaml` ✓

---

### MD3 — Legg til modelltype for alle informasjonsmodellar (Avvik 2)

Bruk vokabularet som allerede er dokumentert i
`modelldcat-katalog-schema.yaml` (`type_concept`-`slot_usage`,
`annotations.gyldige_verdier`):

| Type | URI |
|---|---|
| Konseptuell modell | `https://data.norge.no/vocabulary/modelldcatno#ConceptualDataModel` |
| Logisk modell | `https://data.norge.no/vocabulary/modelldcatno#LogicalDataModel` |
| Fysisk modell | `https://data.norge.no/vocabulary/modelldcatno#PhysicalDataModel` |
| Fellesmodell | *ingen dokumentert URI — ikkje sett `type_concept`* |
| Anvendelsesmodell | *ingen dokumentert URI — ikkje sett `type_concept`* |

Steg:
1. ✓ URI-ane var allerede i bruk i skjemaet (ingen endring nødvendig)
2. ✓ Klassifisert alle 23 informasjonsmodell-instansar i alle 6
   `<org>-modellkatalog.yaml`: 14 domenemodellar (`ngr-*`, `oreg/*`,
   `samt-bu`, `fint-*`) → **Logisk modell**; 9 profil/overbygningsskjema
   (`*-ap-no`, `modelldcat-katalog`, `fair-metadata`) → **Konseptuell
   modell** (`fair-metadata` klassifisert som konseptuell ved analogi —
   det er ein overbygnings-/profilskjema som AP-NO, ikkje ein domenemodell,
   sjå skildringa i `fair-metadata-schema.yaml`)
3. ✓ Ingen instansar klassifisert som Fellesmodell/Anvendelsesmodell —
   ingen treng `type_concept` usett

Verifisert: alle 6 katalogar validerer med `errorCount: 0` under
`POLICY=felles-datakatalog` etter klassifiseringa.

**Filer:** `<org>-modellkatalog.yaml`-datafiler (sjå MD2) — alle 6 oppdaterte

---

### MD4 — Synkroniser `versjonsnummer`, `status` og `endringsdato` (Avvik 5, 6) ✓

Avklart: `versjonsnummer` skal synkroniseres automatisk frå
`release-please-manifest.json`, ikkje fyllast ut manuelt. `status` og
`endringsdato` (frå skjema-YAML `annotations`) skal på samme måte
propageres til modellkatalog-instansane.

**Avvik frå plan:** `status`/`endringsdato`/`utgivelsesdato`-synkroniseringa
fanst **allerede** i `update-modellkatalog.py` sin `ANNOTATION_FIELD_MAP`
(implementert før denne specen, brukt av MD2) — berre `versjonsnummer`
var faktisk manglande. Trengte derfor ikkje noko nytt, separat skript;
utvida `update-modellkatalog.py` i staden for å skrive eit nytt
`gen-modelldcat-elements`-aktig skript (DRY — same kode allerede les
skjema/annotasjonar per org).

**Viktig empirisk funn:** Antok først at skjemaet sitt eige `version:`-felt
var pålitelig (sidan release-please sin `extra-files`-mekanisme *skal*
skrive versjonen dit). Verifisert mot `.release-please-manifest.json`:
**alle 22 pakkar** har ulik versjon i `version:`-feltet enn i manifestet
(t.d. `dcat-ap-no`: skjema=`2.0.0`, manifest=`2.1.1`) — `extra-files`-skrivinga
fungerer ikkje slik forventa i dette repoet. Implementerte derfor
`versjonsnummer`-oppslag direkte mot `.release-please-manifest.json`
(nøkkel: skjemaet sin katalogsti), med fallback til `schema.version` berre
for dei 3 skjemaa som ikkje er release-please-pakkar (`common-ap-no`,
`xkos-ap-no`, `enhetsregisteret-bvrinn`). `modelldcat-katalog-schema.yaml`
løyses korrekt sjølv om det ikkje er ein eigen pakke, sidan det deler
katalogsti (og dermed versjon) med `modelldcat-ap-no`.

Verifisert: alle 6 katalogar validerer med `errorCount: 0` etter
synkroniseringa.

**Ikkje implementert (medvite utelate, ikkje del av avvik 5/6):**
`versjonsmerknad` (`adms:versionNotes`) har ingen etablert kjelde i repoet —
ville krevd å parse `CHANGELOG.md` sine commit-meldingar til kortfatta,
menneskelesarvenlege tekst med rette språkmerke, som er reint
tekstforfattararbeid, ikkje datasynkronisering. CI-integrasjon i
`release-please.yml` (automatisk køyring av `make update-modellkatalog`
ved release) er òg utelate — krev separat avklaring av når i CI-flyten
dette skal køyre.

**Filer:** alle 6 `<org>-modellkatalog.yaml` ✓,
`src/assets/scripts/update-modellkatalog.py` ✓ (utvida, ikkje nytt skript)

---

### MD5 — Eksponér modellelement for maskinhøsting (Avvik 3)

Avklart: vi går for alternativ 2. Dette er det mest komplekse tiltaket.
For at Felles datakatalog skal kunne vise modellinnhald direkte (ikkje
berre lenke til portalen), må kvar `Informasjonsmodell` innehalde
`inneholder_modellelement` med faktiske `Objekttype`-, `Attributt`- og
`Kodeliste`-instansar.

Dette krev eit konverteringsskript (`gen-modelldcat-elements.py`) som
les LinkML-skjema og skriv tilsvarande ModellDCAT-AP-NO-element til
modellkatalog-datafila.

**Retta avvik mot MD2:** Filomfanget var opphavleg skrive som éin fil
(`brreg-modellkatalog.yaml`), men etter MD2 finst det 6 separate
per-org-katalogar (`<org>-modellkatalog.yaml`, sjå tabellen under avvik 1).
`gen-modelldcat-elements.py` må derfor iterere over **alle**
`<org>-modellkatalog.yaml`-datafilene MD2 produserer, ikkje berre brreg sin.

**Filer:** Nytt `src/assets/scripts/gen-modelldcat-elements.py`,
alle `<org>-modellkatalog.yaml`-datafiler (sjå MD2), Makefile

**Avhengigheit (oppdatert):** Krev at MD2 sin per-org-utrulling — inkludert
autoinnsetjing av stubs (sjå MD2 steg 2) — er fullført først, sidan
`gen-modelldcat-elements.py` ellers manglar fila eller
`Informasjonsmodell`-oppslaget å skrive inn i for dei ~19 skjemaa som i dag
ikkje er registrerte (avvik 1).

**Anbefaling:** Utsett gjennomføring til MD2-MD4 er på plass (ulik
avhengigheit, ikkje fordi retninga er uviss). Dette er ein eigen
større spec.

---

### MD6 — Legg til relasjon-slots for begrep og datasett (Avvik 7) ✓

Avklart etter evaluering: `annotations.begrepsidentifikator` er forkasta —
den serialiseres ikkje til RDF på instansnivå og samsvarar derfor ikkje
direkte med rettleiaren. I staden er det lagt til to RDF-property-slots
på `Informasjonsmodell` i `modelldcat-katalog-schema.yaml`:

- ✓ **`relatert_begrep`** — ny global slot, `slot_uri: dct:references`,
  `range: Konsept`, multivalued.
- ✓ **`tilgjengeliggjor_datasett`** — `slot_uri: dcat:servesDataset`,
  `range: Datasett`, multivalued.
  **Avvik frå plan:** ikkje ein ny slot. Verifisert ved kodelesing at
  `dcat-ap-no-schema.yaml` allerede definerer ein global slot med nøyaktig
  denne `slot_uri`/`range` (brukt på `Datatjeneste`) — namnet der er
  `tilgjengeliggjor_datasett` (utan «e» før «r», ikkje `tilgjengeliggjoer_datasett`
  som i opphavleg plan-tekst). Gjenbrukte den eksisterande slotten i staden
  for å definere ein duplikat — DRY, og unngår BUG-7-klassen av
  duplikat-slot-namn-krasj i importgrafen.

`Konsept` og `Datasett` var allerede tilgjengelege via importkjeda
(`dcat-ap-no-schema`, importert direkte av `modelldcat-katalog-schema.yaml`),
ingen ny import nødvendig.

**Datafylling i `brreg-modellkatalog.yaml`:**
- ✓ `relatert_begrep` fylt for `ngr-virksomhet`
  (`https://begrep.brreg.no/foretaksnavn`) og `register-over-aksjeeiere`
  (`https://begrep.brreg.no/nestleder`, `https://begrep.brreg.no/aksjeklasser`)
  — reelle omgrep frå `brreg-begrepskatalog.yaml`.
- ✗ **`tilgjengeliggjor_datasett` ikkje fylt — medvite.** Søkte gjennom heile
  repoet etter faktiske `dcat:Dataset`-instansar (`class_uri: dcat:Dataset`
  i datafiler) — fann **ingen**. NGR/OREG-domena har ikkje publiserte
  DCAT-Datasett-instansar i dette repoet i dag. Å fylle slottet ville kravd
  å finne opp URI-ar til ressursar som ikkje finst, i strid med prinsippet
  om at identifikatorar (Los-URI-ar o.l.) berre skal brukast når dei faktisk
  finst. Slottet er likevel korrekt kopla på skjemanivå og klart til bruk
  når/om reelle Datasett-instansar dukkar opp i repoet.

Verifisert: `make lint` (berre kjend, akseptert `dct`-vs-`dcterms`-warning),
`make roundtrip` for `modelldcat-ap-no` (2 OK), og alle 6 org-katalogar
validerer med `errorCount: 0` under `felles-datakatalog` etter endringa.

**Filer:** `modelldcat-katalog-schema.yaml` ✓, `brreg-modellkatalog.yaml` ✓
(delvis — sjå over)

**Avhengigheit:** Ingen for `Informasjonsmodell`-nivå; relasjon på
`Modellelement`-nivå krev MD5

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | ~~MD1: Avklar og fiks `utgiver`-URI~~ | — | **Utgår** (forkasta, sjå avvik 4) |
| 2 | MD2: Rull ut per-org-modellkatalogar | `CODEOWNERS.md`, nye `<org>-modellkatalog/`-katalogar | — |
| 3 | MD3: Legg til modelltype | `<org>-modellkatalog.yaml`-datafiler | MD2 |
| 4 | MD4: Synkroniser versjon/status/dato | `brreg-modellkatalog.yaml` | — |
| 5 | MD5: Eksponér modellelement | Nytt skript, alle `<org>-modellkatalog.yaml`-filer (sjå MD2) | MD2-MD4, MD2 steg 2 (autoinnsetjing) |
| 6 | MD6: Legg til relasjon-slots for begrep/datasett | `modelldcat-katalog-schema.yaml`, `brreg-modellkatalog.yaml` | — (MD5 for Modellelement-nivå) |

---

## Avhengigheiter

- MD1 er forkasta (sjå avvik 4) — ingen avhengigheit til MD2 lenger
- MD3 (modelltype) krev at MD2 sine `<org>-modellkatalog.yaml`-datafiler
  finst, sidan klassifiseringa skal fyllast ut i desse
- MD5 er eit sjølvstendig, større tiltak som krev eigen plan — men er **ikkje**
  uavhengig av MD2: `gen-modelldcat-elements.py` skal skrive
  `inneholder_modellelement` inn i dei same `Informasjonsmodell`-oppslaga som
  MD2 sin autoinnsetjing (steg 2) opprettar. Avvik 1 og avvik 3 vert derfor
  **ikkje** slått sammen til eitt tiltak (ulik kompleksitet og prioritet —
  MD2 er klar til å rulles ut no, MD5 er uttrykkeleg utsatt), men plan-omfanget
  for MD5 er retta til å dekkje alle 6 per-org-filer i staden for berre
  `brreg-modellkatalog.yaml`, og MD5 sin avhengigheitstabell-rad er oppdatert
  til å vise det eksplisitte steg-nivå-behovet for MD2 steg 2
- MD6 kan implementeres på `Informasjonsmodell`-nivå uavhengig av MD5; berre
  relasjon på `Modellelement`-nivå krev at MD5 finst først

---

## Utført

Alle 7 avvik er no avklarte — enten utførte, forkasta, eller spunne ut i ein
eigen plan:

- **Avvik 1 (MD2 — per-org-modellkatalogar):** Fullført. Alle 23 skjema
  registrerte i 6 organisasjonskatalogar (var 2 av 21). Undervegs fiksa 2
  reelle bugs i `new-org-catalog.sh` (`eval`-krasj på verdiar med mellomrom;
  `TODO`-placeholder som parsa som nøsta dict i staden for streng) og ein
  stale `"TODO"`-datoannotasjon i `register-over-aksjeeiere-schema.yaml`.
- **Avvik 2 (MD3 — modelltype):** Fullført. Alle 23 `Informasjonsmodell`-
  instansar klassifiserte (`Logisk`/`Konseptuell` modell).
- **Avvik 3 (MD5 — modellelement for maskinhøsting):** **Ikkje utført her** —
  spunne ut i eigen plan `specs/backlog/eksponer-modellelement-maskinhosting.md`
  etter brukarønske, sidan dette er det mest komplekse tiltaket (krev ny
  LinkML-skjema-introspeksjon, `SchemaView`, og avklaring av fleire opne
  modelleringsspørsmål før implementasjon).
- **Avvik 4 (MD1 — `utgiver`-URI-format):** Forkasta. Kolliderer med ein
  allereie dokumentert, medviten konvensjon i
  `specs/done/publisering-felles-datakatalog.md` (delt `felles-datakatalog`-
  policy mellom modellkatalog, NGR og OREG).
- **Avvik 5/6 (MD4 — versjonsnummer/status/endringsdato):** Utført.
  `versjonsnummer` synkronisert frå `.release-please-manifest.json` (oppdaga
  at skjemaa sitt eige `version:`-felt var universelt stale i forhold til
  manifestet). `status`/`endringsdato` fanst allerede i
  `update-modellkatalog.py`. `versjonsmerknad` medvite utelate — ingen
  etablert kjelde i repoet.
- **Avvik 7 (MD6 — relasjon-slots for begrep/datasett):** Utført.
  `relatert_begrep` (ny slot, `dct:references`) og `tilgjengeliggjor_datasett`
  (gjenbrukt eksisterande slot frå `dcat-ap-no-schema`, ikkje duplisert) lagt
  til på `Informasjonsmodell`. `relatert_begrep` fylt med reelle verdiar for
  brreg; datasett-slottet kopla på skjemanivå men ikkje fylt — ingen reelle
  `Datasett`-instansar finst i repoet å lenke til.

**Avvik frå opphavleg plan:** BUG-1 (`specs/bugs/langstring-rdflib-roundtrip.md`)
sitt omfang vart utvida til å inkludere dei 5 nye org-katalogane (samme
rotårsak som `brreg-modellkatalog`). Sjå detaljerte avvik per tiltak i
tekstene over (MD1-MD6).
