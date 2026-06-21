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

**Status:** ✓ Avklart og delvis utført — `annotations.utgiver` retta på begge
skjema; resten av MD2 (køyre `make new-org-catalog`/`make update-modellkatalog`
for dei 5 manglande organisasjonane) står ved lag

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

**Avklart:** `organization-catalogue.fellesdatakatalog.digdir.no/organizations/<orgnr>`
er den korrekte URI-forma for `dct:publisher` og skal brukast i staden for
`data.norge.no/organizations/<orgnr>`.

**Status:** ✓ Avklart — skal rettast (sjå MD1)

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
| 1 | Berre 2 av ~21 skjema i modellkatalogen | ✓ Delvis utført (per-org-autogenerering) | Høg |
| 2 | Modelltype (`dct:type`) manglar | ✓ Forslag klart (bruk dokumentert modelldcatno#-vokabular) | Middels |
| 3 | `inneholder_modellelement` er tom | ✓ Avklart (alt. 2) | Høg (kompleks) |
| 4 | `utgiver`-URI-format avvik frå rettleiar | ✓ Avklart | Høg |
| 5 | `versjonsnummer` og `versjonsmerknad` manglar | ✓ Avklart (auto frå release-please) | Middels |
| 6 | `status` og `endringsdato` manglar i instansar | ✓ Avklart (auto frå annotations) | Låg |
| 7 | Ingen relasjonar til begrep/datasett | ✓ Avklart (nye slots: dct:references/dcat:servesDataset) | Låg |

---

## Tilrådde tiltak

### MD1 — Rett `utgiver`-URI-format (Avvik 4)

Avklart: `dct:publisher` skal bruke
`https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/<orgnr>`,
ikkje `https://data.norge.no/organizations/<orgnr>`. Oppdater datafila
(`brreg-modellkatalog.yaml`) og referansen i `CLAUDE.md`
(seksjon «Silver-annotasjonar», `annotations.utgiver`) til den nye URI-forma.

**Filer:** `brreg-modellkatalog.yaml`, `CLAUDE.md`

---

### MD2 — Rull ut per-org-modellkatalogar for alle organisasjonar (Avvik 1)

Avklart: bruk den eksisterande autogenererings-infrastrukturen
(`update-modellkatalog.py`, `make new-org-catalog ORG=<alias>`,
`CODEOWNERS.md`-frontmatter) i staden for å vedlikeholde
`brreg-modellkatalog.yaml` manuelt. Steg:

1. Legg til domeneeksklusjon i `update-modellkatalog.py` (`load_annotated_schemas()`):
   hopp over skjema i domena `referanse`, `modellkatalog` og `begrepskatalog`
   (sjå avvik 1 for grunngjeving)
2. Køyr `make new-org-catalog ORG=<alias>` for dei 5 organisasjonane som
   manglar katalogkatalog: `digdir`, `novari`, `ksdigital`, `skatteetaten`,
   `kartverket` (sjå tabellen over for kva skjema som vil dukke opp i
   kvar katalog)
3. Køyr `make update-modellkatalog` for å fylle alle 6 katalogane frå
   `annotations.*` i skjema-YAML-filene
4. Fyll ut manuelt vedlikehaldne stub-felt (`tema`, `lisens`, `kontaktpunkt`
   m.m.) som scriptet legg inn som `TODO` for nye oppslag

✓ **Utført:** `annotations.utgiver` sett på `modelldcat-katalog-schema.yaml`
(digdir, `991825827`) og retta på `referanse-schema.yaml` (brreg, `974760673`,
generell annotasjons-opprydding — filen blir ikkje skanna av scriptet uansett,
sjå avvik 1). Resten (steg 1–3 over) står ved lag.

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
1. Verifiser dei 3 URI-ane mot ModellDCAT-AP-NO-spesifikasjonen (dei er
   allerede i bruk i skjemaet, men bør stadfestast mot kjelda før utrulling)
2. Klassifiser hver informasjonsmodell-instans i alle `<org>-modellkatalog.yaml`
   (sjå MD2): domenemodellar → Logisk modell, AP-NO-profilar → Konseptuell
   modell (sjå avvik 2 for full grunngjeving)
3. La `type_concept` stå usett for modellar som ikkje passar dei 3 typane

**Filer:** `<org>-modellkatalog.yaml`-datafiler (sjå MD2)

---

### MD4 — Synkroniser `versjonsnummer`, `status` og `endringsdato` (Avvik 5, 6)

Avklart: `versjonsnummer` skal synkroniseres automatisk frå
`release-please-manifest.json`, ikkje fyllast ut manuelt. `status` og
`endringsdato` (frå skjema-YAML `annotations`) skal på samme måte
propageres til modellkatalog-instansane.

Dette krev eit skript som les versjon frå `release-please-manifest.json`
og `annotations`-feltene frå skjema-YAML, og skriv dei inn i
modellkatalog-datafila — same mønster som `gen-dqv-measurements.py`
(jf. CI-steg i `release-please.yml`).

**Filer:** `brreg-modellkatalog.yaml`, nytt skript i
`src/assets/scripts/`, `.github/workflows/release-please.yml`

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

**Filer:** Nytt `src/assets/scripts/gen-modelldcat-elements.py`,
`brreg-modellkatalog.yaml`, Makefile

**Anbefaling:** Utsett gjennomføring til MD1–MD4 er på plass (ulik
avhengigheit, ikkje fordi retninga er uviss). Dette er ein eigen
større spec.

---

### MD6 — Legg til relasjon-slots for begrep og datasett (Avvik 7)

Avklart etter evaluering: `annotations.begrepsidentifikator` er forkasta —
den serialiseres ikkje til RDF på instansnivå og samsvarar derfor ikkje
direkte med rettleiaren. I staden skal det leggjast til to nye RDF-property-slots
i `modelldcat-katalog-schema.yaml`:
- `relatert_begrep` — `slot_uri: dct:references`, `range: Konsept`, multivalued
  — på `Informasjonsmodell` (og evt. `Modellelement` når MD5 er på plass)
- `tilgjengeliggjoer_datasett` — `slot_uri: dcat:servesDataset`, `range: Datasett`,
  multivalued — på `Informasjonsmodell`

`Konsept` og `Datasett` er allerede tilgjengelege via importkjeda
(`dcat-ap-no-schema`), så ingen ny import er nødvendig. Slottene gir
faktiske RDF-triples på instansnivå, i tråd med rettleiaren, og fyll deretter
ut verdiar i `brreg-modellkatalog.yaml` (begrep-URI-ar frå
`brreg-begrepskatalog`, datasett-URI-ar frå relevante datakataloginstansar).

**Filer:** `modelldcat-katalog-schema.yaml`, `brreg-modellkatalog.yaml`

**Avhengigheit:** Ingen for `Informasjonsmodell`-nivå; relasjon på
`Modellelement`-nivå krev MD5

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | MD1: Avklar og fiks `utgiver`-URI | `brreg-modellkatalog.yaml`, `CLAUDE.md` | — |
| 2 | MD2: Rull ut per-org-modellkatalogar | `CODEOWNERS.md`, nye `<org>-modellkatalog/`-katalogar | MD1 |
| 3 | MD3: Legg til modelltype | `<org>-modellkatalog.yaml`-datafiler | MD2 |
| 4 | MD4: Synkroniser versjon/status/dato | `brreg-modellkatalog.yaml` | — |
| 5 | MD5: Eksponér modellelement | Nytt skript, `brreg-modellkatalog.yaml` | MD1–MD4 |
| 6 | MD6: Legg til relasjon-slots for begrep/datasett | `modelldcat-katalog-schema.yaml`, `brreg-modellkatalog.yaml` | — (MD5 for Modellelement-nivå) |

---

## Avhengigheiter

- MD1 (avklart format) bør rettast først — feil `utgiver`-URI kan gjere at
  Felles datakatalog ikkje godtek publiseringa uavhengig av dei andre tiltaka
- MD2 (per-org-katalogar) bør kome etter MD1 slik at alle oppslag brukar rett
  `utgiver`-URI før `make update-modellkatalog` køyrer
- MD3 (modelltype) krev at MD2 sine `<org>-modellkatalog.yaml`-datafiler
  finst, sidan klassifiseringa skal fyllast ut i desse
- MD5 er eit sjølvstendig, større tiltak som krev eigen plan
- MD6 kan implementeres på `Informasjonsmodell`-nivå uavhengig av MD5; berre
  relasjon på `Modellelement`-nivå krev at MD5 finst først
