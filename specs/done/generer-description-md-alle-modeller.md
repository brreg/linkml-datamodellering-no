# Generer description.md for alle modellar

## Bakgrunn

`description.md` er ein valfri portaltekst som vert vist i `index.md` for kvar modell,
rett etter metadata-tabellen. Fila gjev brukaren ein kort introduksjon til modellen,
brukstilfelle, nøkkelklasser og relasjonar til andre modellar.

For tida har berre 8 av 29 modellar ein `description.md`:
- `ap-no/dcat-ap-no`
- `ap-no/modelldcat-ap-no`
- `ap-no/skos-ap-no`
- `samt/samt-bu`
- `fair/fair-metadata`
- `oreg/enhetsregisteret-bvrinn`
- `oreg/register-over-aksjeeiere`
- `begrepskatalog/brreg-begrepskatalog`

**Mål:** Generere `description.md` for alle 29 modellar (inkl. oppdatere eksisterande) etter
same mal som `ap-no/dcat-ap-no/description.md`.

## Mal

`dcat-ap-no/description.md` følgjer denne strukturen:

1. **Ingress** (1 setning): Kva modellen er, basert på kva (EU/W3C-standard), modellert i LinkML
2. **Formål** (1 setning): Kva modellen definerer (metadata, domeneomgrep, struktur)
3. **Typisk brukar** (1 setning): Kven skal bruke modellen og til kva
4. **Nøkkelklasser** (1 linje): Liste over dei viktigaste klassane (4-8 stk)
5. **Relasjon til andre modellar i dette repoet** (bullet-liste): Import-hierarki og brukarar av modellen
6. **Avvik frå spesifikasjonen** (valfritt): Lenke til `specs/done/avvik-<modell>.md` dersom relevant

## Gruppering av modellar

Modellane kan delast inn i fire kategoriar:

### 1. AP-NO-profilar (8 stk)

Norske applikasjonsprofiler av EU/W3C-standardar:

- `common-ap-no` — basislaget, ingen spesifikasjon
- `cpsv-ap-no` — tjeneste- og hendelsesbeskrivingar
- `dcat-ap-no` — datasettbeskrivingar (har description.md)
- `dqv-ap-no` — datakvalitetsannotasjonar (hovudskjema)
- `dqv-core` — delmodell av `dqv-ap-no`
- `modelldcat-ap-no` — informasjonsmodellbeskrivingar (har description.md)
- `skos-ap-no` — omgrepskatalogar (har description.md)
- `xkos-ap-no` — klassifikasjonar

**Felles mønster:**
- Ingress: "[Profil-namn] er den norske applikasjonsprofilen av [standard], modellert i LinkML."
- Formål: "Profilen definerer korleis [ressurstypar] skal beskrivas med metadata — etter krava i [spesifikasjon-lenke]."
- Typisk brukar: "Offentlege verksemder som skal publisere [ressurstypar] til [Felles katalog], og utviklare..."
- Relasjon: Alle importerer `common-ap-no`, fleire importerer kvarandre

### 2. Domenemodeller (5 stk)

NGR (Nasjonale grunndata — registermodeller):

- `ngr-adresse` — adressemodell (POC)
- `ngr-eiendom` — eiendomsmodell (POC)
- `ngr-person` — personmodell (POC)
- `ngr-virksomhet` — virksomhetsmodell (POC)

OREG (Offentlege registre):

- `enhetsregisteret-bvrinn` — Enhetsregisteret (har description.md, POC)
- `register-over-aksjeeiere` — Aksjeeigarregisteret (har description.md, POC)

SAMT (Samarbeid om modernisering av tenesteforvalting):

- `samt-bu` — barn og unge (har description.md, POC)

**Felles mønster:**
- Ingress: "LinkML-modell av [registernavn/domene] — [kort forklaring]."
- Formål: "Modellen definerer [nøkkelressursar] og metadata for [brukstilfelle]."
- Typisk brukar: "[Aktør] som skal [bruken]."
- Relasjon: Importerer `dcat-ap-no` for katalogstøtte, nokre importerer `common-ap-no`

### 3. FINT-modellar (7 stk)

Konverterte frå FINT API-spesifikasjonen (Java-modell → LinkML):

- `fint-common` — basislaget for FINT-modellar
- `fint-administrasjon` — administrasjon
- `fint-arkiv` — arkiv
- `fint-okonomi` — økonomi
- `fint-personvern` — personvern
- `fint-ressurs` — ressurs
- `fint-utdanning` — utdanning

**Felles mønster:**
- Ingress: "LinkML-modell av FINT [domene]-API, konvertert frå FINT sin Java-baserte modell."
- Formål: "Modellen definerer [nøkkelklasser] for integrasjon med FINT [domene]-tenester."
- Typisk brukar: "Utdanningssektorverksemder som brukar FINT [domene]-API."
- Relasjon: Alle importerer `fint-common`, ingen AP-NO-profiler

### 4. Katalogmodellar og andre (9 stk)

Modellkatalogar (6 stk):

- `brreg-modellkatalog` — Brønnøysundregistrene
- `digdir-modellkatalog` — Digitaliseringsdirektoratet
- `kartverket-modellkatalog` — Kartverket
- `ksdigital-modellkatalog` — KS Digital
- `novari-modellkatalog` — Novari
- `skatteetaten-modellkatalog` — Skatteetaten

Omgrepskatalogar (1 stk):

- `brreg-begrepskatalog` — Brønnøysundregistrene (har description.md)

Andre (1 stk):

- `fair-metadata` — FAIR-metadata for forskingsdata (har description.md)

**Felles mønster (modellkatalogar):**
- Ingress: "Modellkatalog for [organisasjon] sine informasjonsmodellar, basert på ModelDCAT-AP-NO."
- Formål: "Katalogen inneheld metadata om [organisasjon] sine LinkML-modellar, publiserte til [Felles modellkatalog]."
- Typisk brukar: "[Organisasjon] sine modelladministratorar og eksterne brukarar."
- Relasjon: Importerer `modelldcat-ap-no`, ingen eigne klasser (berre `Containerklasse`)

## Automatisering

Genereringa kan anten vere:

1. **Heilt automatisert** — Python-script les skjema og genererer description.md
2. **Semi-automatisert** — Script genererer mal med placeholder, manuell fylling
3. **Manuelt** — Skriv kvar description.md manuelt etter malen

**Vurdering:** Semi-automatisert er mest realistisk. Script kan hente:
- `title`, `description` frå skjema-YAML
- `imports`-liste for relasjonar
- Top-5 klassar (sortert etter antal slots eller `tree_root`-status)
- `external_spec_url` frå manifest

**Manuell fylling:**
- "Typisk brukar"-setning (kontekst-avhengig)
- Utvida relasjonsbeskrivingar (kven importerer kven, kvifor)
- Avvik-lenke (valfritt)

## Handlingsliste

- [x] Identifiser alle 29 modellar og kategoriser dei (AP-NO, domene, FINT, katalog)
- [x] Generer description.md for alle AP-NO-profilar (4 nye: common, cpsv-ap-no, xkos-ap-no, dqv-ap-no)
- [x] Generer description.md for alle NGR-domenemodeller (4 nye: ngr-adresse, ngr-eiendom, ngr-person, ngr-virksomhet)
- [x] Generer description.md for alle FINT-modellar (7 nye: fint-common, fint-administrasjon, fint-arkiv, fint-utdanning, fint-okonomi, fint-personvern, fint-ressurs)
- [x] Generer description.md for alle modellkatalogar (6 nye)
- [x] Oppdater eksisterande description.md (5 stk: fair-metadata, enhetsregisteret-bvrinn, register-over-aksjeeiere, samt-bu, brreg-begrepskatalog)
- [x] Generer description.md for referanse-skjemaet (test/læring)
- [x] Verifiser med `make docs-publish` at alle description.md vert vist korrekt

## Utført

Alle 33 modellar har no `description.md` etter same mal som `dcat-ap-no`:

**AP-NO-profilar (9 stk):**
- `common-ap-no` — basislaget (ny)
- `cpsv-ap-no` — tjeneste- og hendelsesbeskrivingar (ny)
- `dcat-ap-no` — datasettbeskrivingar (eksisterte)
- `dqv-ap-no` + `dqv-core` — datakvalitetsannotasjonar (ny)
- `modelldcat-ap-no` — informasjonsmodellbeskrivingar (eksisterte)
- `skos-ap-no` — omgrepskatalogar (eksisterte)
- `xkos-ap-no` — klassifikasjonar (ny)

**Domenemodeller (7 stk):**
- NGR: `ngr-adresse`, `ngr-eiendom`, `ngr-person`, `ngr-virksomhet` (4 nye)
- OREG: `enhetsregisteret-bvrinn`, `register-over-aksjeeiere` (oppdatert)
- SAMT: `samt-bu` (oppdatert)

**FINT-modellar (7 stk):**
- `fint-common`, `fint-administrasjon`, `fint-arkiv`, `fint-utdanning`, `fint-okonomi`, `fint-personvern`, `fint-ressurs` (alle nye)

**Katalogmodellar og andre (10 stk):**
- Modellkatalogar: `brreg-modellkatalog`, `digdir-modellkatalog`, `kartverket-modellkatalog`, `ksdigital-modellkatalog`, `novari-modellkatalog`, `skatteetaten-modellkatalog` (6 nye)
- Omgrepskatalog: `brreg-begrepskatalog` (oppdatert)
- FAIR-metadata: `fair-metadata` (oppdatert)
- Referanse: `referanse` (ny, test/læring)

Implementasjonen følgde alternativ 1 (LLM-basert generering) — eg genererte alle description.md manuelt basert på malen, kategorisert per domene. Alle filer er testa med `make docs-publish` og vert vist korrekt i `mkdocs/docs/<domain>/<schema>/index.md`.

## Alternativ

**Alternativ 1: LLM-basert generering**

Bruk Claude til å generere `description.md` for kvar modell basert på:
- Skjema-YAML (`title`, `description`, `classes`, `imports`)
- Manifest (`external_spec_url`, `external_spec_label`)
- Kontekst frå CLAUDE.md og eksisterande description.md

**Vurdering:** Dette er mest effektivt for ein eingongsjobb. Script kan kalle Claude API
eller bruke MCP-server til å generere kvart description.md-utkast.

**Alternativ 2: Berre manuell fylling**

Ingen script — skriv alle 21 manglande description.md manuelt etter malen.

**Vurdering:** Tidkrevjande, men garanterer høg kvalitet og kontekst-tilpassing.

**Anbefaling:** Kombinasjon av alternativ 1 og 2 — LLM genererer draft, manuell gjennomgang
og kvalitetssikring før commit.
