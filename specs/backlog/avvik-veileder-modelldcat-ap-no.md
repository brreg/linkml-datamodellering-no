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

**Status:** ⚠️ Avvik — høg prioritet

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

**Status:** ⚠️ Avvik — middels prioritet

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

**Status:** ⚠️ Avvik — høg funksjonell verdi, men kompleks å implementere

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

Det er uklart om `data.norge.no/organizations/`-URIar vert aksepterte av
Felles datakatalog som gyldige utgjevar-referansar. Viss ikkje, vil
publiserte modellar mangla utgjevar-oppslag i katalogen.

**Status:** ⚠️ Treng avklaring — potensielt høg prioritet

---

### 5 — `versjonsnummer` og `versjonsmerknad` manglar

Rettleiaren anbefaler `owl:versionInfo` (versjonsnummer) og
`adms:versionNotes` (versjonsmerknad) for å dokumentere endringar utan
å opprette ny instans.

Informasjonsmodellane i datafila har ikkje desse felta fylt ut, sjølv
om slota finst i `modelldcat-ap-no-schema.yaml`. Versjonssporet frå
`release-please` (t.d. `ngr-virksomhet` = `1.0.0`) vert ikkje
synkronisert til modellkatalogen.

**Status:** ⚠️ Avvik — middels prioritet

---

### 6 — `status` og `endringsdato` manglar i informasjonsmodell-instansar

Slota `status` og `endringsdato` finst i `modelldcat-ap-no-schema.yaml`
(valgfrie), men er ikkje fylt ut i `brreg-modellkatalog.yaml`. Dette er
dei same annotasjonane som silver-policy krev i skjema-YAML-filene, men
dei vert ikkje propagert til modellkatalog-instansen.

**Status:** ⚠️ Avvik — låg prioritet (valgfri, men god praksis)

---

### 7 — Ingen relasjoner til begreper, datasett eller datatjenester

Rettleiaren har ein eigen seksjon om å knytte informasjonsmodellar til
tilhøyrande omgrep (`dct:references` → begrepskatalog-oppslag) og
datasett (`dcat:servesDataset`). 

Datafila har ingen slike koplingar, sjølv om repoet har både
begrepskatalog (`brreg-begrepskatalog`) og modellkatalog.

**Status:** ⚠️ Avvik — låg prioritet, men gjer katalogen meir nyttig

---

## Samandrag

| # | Avvik | Status | Prioritet |
|---|---|---|---|
| 1 | Berre 2 av ~21 skjema i modellkatalogen | ⚠️ Avvik | Høg |
| 2 | Modelltype (`dct:type`) manglar | ⚠️ Avvik | Middels |
| 3 | `inneholder_modellelement` er tom | ⚠️ Avvik | Høg (kompleks) |
| 4 | `utgiver`-URI-format avvik frå rettleiar | ⚠️ Treng avklaring | Høg |
| 5 | `versjonsnummer` og `versjonsmerknad` manglar | ⚠️ Avvik | Middels |
| 6 | `status` og `endringsdato` manglar i instansar | ⚠️ Avvik | Låg |
| 7 | Ingen relasjonar til begrep/datasett | ⚠️ Avvik | Låg |

---

## Tilrådde tiltak

### MD1 — Avklar `utgiver`-URI-format (Avvik 4)

Sjekk om `https://data.norge.no/organizations/<orgnr>` vert akseptert av
Felles datakatalog som `dct:publisher`, eller om
`https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/<orgnr>`
er påkravd. Oppdater datafila og `CLAUDE.md` deretter.

**Filer:** `brreg-modellkatalog.yaml`, `CLAUDE.md`

---

### MD2 — Utvid modellkatalogen med fleire skjema (Avvik 1)

Legg til oppslag for alle skjema med `publish_external: true` eller
`data_policy: silver/gold` i `brreg-modellkatalog.yaml`. Prioriter:
1. NGR-skjema (adresse, eigedom, person) — allereie `publish_external: true`
2. OREG-skjema (`register-over-aksjeeiere` er allereie med)
3. AP-NO-profilane (dcat, skos, dqv, modelldcat, cpsv)

For kvart skjema krev dette: `id`, `tittel`, `utgiver`,
`informasjonsmodellidentifikator` (lenke til portalen), `lisens`, `tema`.

**Filer:** `brreg-modellkatalog.yaml`

---

### MD3 — Legg til modelltype for alle informasjonsmodellar (Avvik 2)

Finn URI-ar for ModellDCAT-AP-NO-vokabularet for modelltypar og legg til
`type_concept` i alle informasjonsmodell-instansar. Sannsynlege URIar:

| Type | Forventa URI |
|---|---|
| Logisk modell | `https://data.norge.no/vocabulary/information-model-type#logical-model` |
| Fellesmodell | `https://data.norge.no/vocabulary/information-model-type#common-model` |
| Anvendelsesmodell | `https://data.norge.no/vocabulary/information-model-type#application-model` |

Verifiser korrekte URIar mot ModellDCAT-AP-NO-spesifikasjonen.

**Filer:** `brreg-modellkatalog.yaml`, `modelldcat-ap-no-schema.yaml`

---

### MD4 — Synkroniser `versjonsnummer`, `status` og `endringsdato` (Avvik 5, 6)

Legg til `versjonsnummer` (frå `release-please-manifest.json`), `status`
og `endringsdato` (frå skjema-YAML `annotations`) i modellkatalog-instansane.

Vurder om CI-pipelinen kan automatisere dette: eit skript les versjon frå
skjema-YAML og skriv det inn i modellkatalog-datafila.

**Filer:** `brreg-modellkatalog.yaml`

---

### MD5 — Eksponér modellelement for maskinhøsting (Avvik 3)

Dette er det mest komplekse tiltaket. For at Felles datakatalog skal
kunne vise modellinnhald direkte (ikkje berre lenke til portalen), må
kvar `Informasjonsmodell` innehalde `inneholder_modellelement` med
faktiske `Objekttype`-, `Attributt`- og `Kodeliste`-instansar.

Dette krev eit konverteringsskript (`gen-modelldcat-elements.py`) som
les LinkML-skjema og skriv tilsvarande ModellDCAT-AP-NO-element til
modellkatalog-datafila.

**Filer:** Nytt `src/assets/scripts/gen-modelldcat-elements.py`,
`brreg-modellkatalog.yaml`, Makefile

**Anbefaling:** Utsett til MD1–MD4 er på plass. Dette er ein eigen
større spec.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | MD1: Avklar og fiks `utgiver`-URI | `brreg-modellkatalog.yaml`, `CLAUDE.md` | — |
| 2 | MD2: Utvid katalogen med fleire skjema | `brreg-modellkatalog.yaml` | MD1 |
| 3 | MD3: Legg til modelltype | `brreg-modellkatalog.yaml` | — |
| 4 | MD4: Synkroniser versjon/status/dato | `brreg-modellkatalog.yaml` | — |
| 5 | MD5: Eksponér modellelement | Nytt skript, `brreg-modellkatalog.yaml` | MD1–MD4 |

---

## Avhengigheiter

- MD1 bør avklarast først — feil `utgiver`-URI kan gjere at Felles datakatalog
  ikkje godtek publiseringa uavhengig av dei andre tiltaka
- MD2 (fleire skjema) bør kome etter MD1 slik at alle oppslag brukar rett URI
- MD5 er eit sjølvstendig, større tiltak som krev eigen plan
