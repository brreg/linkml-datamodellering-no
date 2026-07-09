# README.md-oppdatering — manglar nye skjema og domene

## Bakgrunn

Evaluering av `README.md` viser at fleire nye skjema og katalogar som er lagt til i repoet ikkje er dokumenterte i hovuddokumentasjonen.

## Status quo

**Skjema i repoet (30 stk):**
```
brreg-begrepskatalog, brreg-modellkatalog, common-ap-no, cpsv-ap-no, dcat-ap-no,
digdir-modellkatalog, dqv-ap-no, enhetsregisteret-bvrinn, fair-metadata,
fint-administrasjon, fint-arkiv, fint-common, fint-okonomi, fint-personvern,
fint-ressurs, fint-utdanning, kartverket-modellkatalog, ksdigital-modellkatalog,
modelldcat-ap-no, ngr-adresse, ngr-eiendom, ngr-person, ngr-virksomhet,
novari-modellkatalog, referanse, register-over-aksjeeiere, samt-bu,
skatteetaten-modellkatalog, skos-ap-no, xkos-ap-no
```

**Skjema dokumenterte i README.md (21 stk):**
```
fair-metadata, common-ap-no, cpsv-ap-no, dcat-ap-no, dqv-ap-no, modelldcat-ap-no,
skos-ap-no, xkos-ap-no, fint-common, fint-administrasjon, fint-arkiv, fint-okonomi,
fint-personvern, fint-ressurs, fint-utdanning, ngr-adresse, ngr-eiendom, ngr-person,
ngr-virksomhet, register-over-aksjeeiere, samt-bu
```

## Manglar

### Nye skjema som manglar i README.md

**begrepskatalog-domenet:**
- `brreg-begrepskatalog` — manglar i skjema-tabellen

**modellkatalog-domenet:**
- `brreg-modellkatalog` — dokumentert i README.md (linje 147), men manglar i skjema-tabellen
- `digdir-modellkatalog` — manglar både i domene-tabell og skjema-tabell
- `kartverket-modellkatalog` — manglar både i domene-tabell og skjema-tabell
- `ksdigital-modellkatalog` — manglar både i domene-tabell og skjema-tabell
- `novari-modellkatalog` — manglar både i domene-tabell og skjema-tabell
- `skatteetaten-modellkatalog` — manglar både i domene-tabell og skjema-tabell

**oreg-domenet:**
- `enhetsregisteret-bvrinn` — manglar i skjema-tabellen
- `register-over-aksjeeiere` — dokumentert (linje 174), OK

**referanse-domenet:**
- `referanse` — manglar både i domene-tabell og skjema-tabell

### Domene som manglar i README.md

**`modellkatalog`-domenet:**
- Dokumentert på linje 147-148, men ikkje i domene-tabellen (linje 136-148)
- Har no **6 modellkatalogar** (brreg, digdir, kartverket, ksdigital, novari, skatteetaten)

**`referanse`-domenet:**
- Eit nytt domene som ikkje er dokumentert i det heile
- **Formål:** Gir enkle eksempel på gyldige LinkML-modellar (referanseimplementasjonar)

## Avvik frå struktur

~~**`common-ap-no` er dokumentert i skjema-tabellen (linje 156), men ligg fysisk som `src/linkml/ap-no/common/`:**~~
~~- Tabellen viser `common-ap-no` som skjema-namn, men katalognamnet er `common`~~
~~- Dette er enten ein feil i dokumentasjonen eller ein inkonsistens i filstrukturen~~

**Oppdatering 2026-07-09:** Katalogen heiter `src/linkml/ap-no/common-ap-no/` — dokumentasjonen og filstrukturen er konsistente.

## Arbeidsflyt

**VIKTIG:** Alle endringar skal først utførast mot `test_README.md` slik at brukaren kan manuelt samanlikne med eksisterande `README.md` før endring vert godkjent.

1. Opprett `test_README.md` som kopi av `README.md`
2. Utfør alle tiltak (1-4) mot `test_README.md`
3. Brukaren samanliknar `test_README.md` med `README.md` manuelt
4. Brukaren avgjer om `test_README.md` skal erstatte `README.md`

## Tiltak

### 1. Oppdater domene-tabell (linje 136-148)
- [x] Legg til `modellkatalog`-domenet med skildring og referanse til ModelDCAT-AP-NO
- [x] Legg til `referanse`-domenet med skildring: "Enkle eksempel på gyldige LinkML-modellar (referanseimplementasjonar)"

### 2. Oppdater skjema-tabell (linje 149-176)
- [x] Legg til `brreg-begrepskatalog` under `begrepskatalog`-domenet
- [x] Legg til `enhetsregisteret-bvrinn` under `oreg`-domenet
- [x] Legg til `referanse` under `referanse`-domenet med skildring: "Enkel eksempelmodell for å demonstrere gyldig LinkML-struktur"
- [x] Rett path for `common-ap-no` frå `src/linkml/ap-no/common/` til `src/linkml/ap-no/common-ap-no/`

### 2b. Legg til "Genererte modellkatalogar"-seksjon i README.md
- [x] Opprett ny seksjon med overskrift "Genererte modellkatalogar"
- [x] Lag tabell med kolonnane: Modellkatalog | Organisasjon | Skildring
- [x] Legg til alle 6 modellkatalogar som eigne rader:
  - `brreg-modellkatalog` | Brønnøysundregistra | Modellkatalog for Brønnøysundregistra sine informasjonsmodellar
  - `digdir-modellkatalog` | Digitaliseringsdirektoratet | Modellkatalog for Digitaliseringsdirektoratet sine informasjonsmodellar
  - `kartverket-modellkatalog` | Kartverket | Modellkatalog for Kartverket sine informasjonsmodellar
  - `ksdigital-modellkatalog` | KS Digital | Modellkatalog for KS Digital sine informasjonsmodellar
  - `novari-modellkatalog` | Novari | Modellkatalog for Novari sine informasjonsmodellar
  - `skatteetaten-modellkatalog` | Skatteetaten | Modellkatalog for Skatteetaten sine informasjonsmodellar

### 3. ~~Avklar `common-ap-no` vs `common`~~
- [x] ~~Sjekk om `src/linkml/ap-no/common/` skal heite `common-ap-no/` for konsistens~~
- [x] ~~Alternativt: endre dokumentasjonen til å referere til `common` i staden for `common-ap-no`~~

**Løyst:** Katalogen heiter allereie `common-ap-no/` — ingen handling nødvendig.

### 4. Verifiser at dokumentasjonslenkjer er korrekte
- [x] Alle nye skjema har:
  - Lenkje til `src/linkml/<domain>/<skjema>/` (kolonne 2)
  - Skildring (kolonne 3)
  - Dokumentasjonslenkje (kolonne 4) — dersom relevant
- [x] Alle path-ar er verifiserte mot faktisk filsystemstruktur

### 4b. Manuell godkjenning
- [x] Brukaren samanliknar `test_README.md` med `README.md`
- [x] Brukaren avgjer om `test_README.md` skal erstatte `README.md`
- [x] Dersom godkjent: `mv test_README.md README.md` — **UTFØRT**

## Tilleggstiltak: Omstrukturering av dokumentasjon

### 5a. Splitt og flytt `specs/done/oversikt-avgrensingar-prinsipp.md`
- [x] Opprett `SCOPE.md` på root med: Kva er dette repoet, Avgrensingar, Funksjonalitet
- [x] Opprett `PRINCIPLES.md` på root med: Dei 6 designprinsippa
- [x] Opprett `CONVENTIONS.md` på root med: Namnekonvensjonar, manifestformat, commit-meldingar
- [x] Oppdater `GOVERNANCE.md` med "Roller og eigarskap"-seksjonen
- [x] Oppdater `test_README.md` med lenkjer til dei nye filene
- [x] Oppdater `CLAUDE.md` med referanse-seksjon til dei nye filene
- [x] Slett `specs/done/oversikt-avgrensingar-prinsipp.md` (erstattet av dei 3 nye filene)

### 5. Implementer automatisering
- [x] Opprett `scripts/generate-readme-tables.sh` som genererer domene-tabell, skjema-tabell og modellkatalog-tabell
- [x] Legg til placeholder-kommentarar i README.md: `<!-- BEGIN AUTO-GENERATED: ... -->` / `<!-- END AUTO-GENERATED: ... -->`
- [x] Test scriptet mot `test_README.md` — ✅ fungerer
- [x] Skjema-tabell: gruppere skjema etter domene i same rekkefølgje som domene-tabellen
- [x] Skjema-tabell: filtrer vekk underskjema (t.d. modelldcat-katalog, modelldcat-modell) — berre hovudskjema
- [x] Integrer scriptet i `make docs-publish` (køyr før mkdocs-publisering) — ✅ **UTFØRT**: Makefile oppdatert, scriptet køyrer automatisk før mkdocs/publish.sh

### 5 (opprinnelig beskrivelse). Vurder automatisering
**Problem:** README.md vert lett utdatert når nye skjema vert lagt til.

**Vurdering av kva som eignar seg for automatisk generering:**

| Innhald | Automatiserbar? | Kjelde | Merknad |
|---------|-----------------|--------|---------|
| Domene-liste | ✅ Ja | `src/linkml/`-katalogstruktur | Kan hente alle domene-katalogar automatisk |
| Skjema-liste | ✅ Ja | `src/linkml/<domain>/<schema>/*-schema.yaml` | Kan finne alle skjema-filer automatisk |
| Skjema-tabell (kolonne 1-2) | ✅ Ja | Katalogstruktur + skjema-filnamn | Namn og path kan hentast direkte |
| Skjema-tabell (kolonne 3: skildring) | ⚠️ Delvis | `title`/`description` i `*-schema.yaml` | `description` kan vere for lang — treng evt. `description.md` eller manually curated kort-skildring |
| Skjema-tabell (kolonne 4: dokumentasjon) | ✅ Ja | Generert `mkdocs/docs/<domain>/<schema>/` | Sjekk om katalog finst → lenk til publisert site |
| Modellkatalog-tabell | ✅ Ja | `src/linkml/modellkatalog/*/` + `annotations.utgiver` i schema | Hent organisasjonsnamn frå utgiver-URI (slå opp i Enhetsregisteret-API eller hardkoda mapping) |
| Domene-skildringar | ❌ Nei | Manuell tekst | Policy-driven, krev kontekst og motivasjon |
| Innleiande tekst | ❌ Nei | Manuell tekst | Formål, målgruppe, bruksinstruksjonar |
| Versjonsnummer og status | ✅ Ja | `version` og `annotations.status` i schema | Kan visast i tabell |

**Anbefaling:**

1. **Generer automatisk:** Domene-liste, skjema-liste, skjema-tabell (namn, path, dokumentasjonslenkjer), modellkatalog-tabell
2. **Behald manuell:** Innleiande tekst, domene-skildringar, kort-skildringar av skjema (dersom `description` i schema er for teknisk/lang)
3. **Implementasjonsforslag:**
   - Utvid `mkdocs/publish.sh` eller opprett nytt script `scripts/generate-readme-tables.sh`
   - Generer Markdown-tabellar frå katalogstruktur og schema-metadata
   - Bruk placeholder-kommentarar i README.md for å markere auto-genererte seksjoner:
     ```markdown
     <!-- BEGIN AUTO-GENERATED: SCHEMA TABLE -->
     | Skjema | Path | Skildring | Dokumentasjon |
     ...
     <!-- END AUTO-GENERATED: SCHEMA TABLE -->
     ```
   - Køyr script i CI (`make docs-publish`) for å oppdatere README.md før publisering
4. **Alternativ:** CI-sjekk som validerer at alle skjema i `src/linkml/` er dokumenterte i README.md (enklare, men gir ikkje automatisk oppdatering)

## Spørsmål til brukar

1. ~~**Kva er formålet med `referanse`-domenet?** Er det ein testdomene, eller skal det dokumenterast i README.md?~~ **Løyst** — gir enkle eksempel på gyldige LinkML-modellar (referanseimplementasjonar).
2. ~~**Er `common-ap-no` vs `common`-inkonsistensen bevisst?** Skal katalogen omdøypast til `common-ap-no`, eller skal dokumentasjonen endre til `common`?~~ **Løyst** — katalogen heiter `common-ap-no/`.
3. ~~**Skal modellkatalogar ha individuelle skildringar i README.md?** Eller kan dei grupperas under éi linje som "Modellkatalogar for ulike organisasjonar (Brønnøysundregistrene, Digitaliseringsdirektoratet, Kartverket, KS Digital, Novari, Skatteetaten)"?~~ **Løyst** — skal ha eigen seksjon "Genererte modellkatalogar" med tabell der kvar modellkatalog vert skildra på ei rad.

## Verifisering
1. Køyr `make docs-publish && make docs-serve` og sjekk at alle domene og skjema er synlege i dokumentasjonsportalen
2. Sjekk at alle lenkjer i README.md fungerer
3. Verifiser at nye skjema har `build.yaml` og `examples/`-katalog

## Tilleggstiltak: Flytting av bugs-dokumentasjon

### 6. Flytt `specs/bugs/` til root
- [x] Flytt `specs/bugs/` til `bugs/` på root
- [x] Flytt `specs/bugs/README.md` til `BUGS.md` på root
- [x] Oppdater interne referansar i `BUGS.md` (lenker til GOVERNANCE.md, mkdocs-filer, bug-filer)
- [x] Oppdater referansar i `README.md` og `test_README.md`
- [x] Oppdater referansar i `SCOPE.md`
- [x] Oppdater referansar i `CLAUDE.md`
- [x] Oppdater referansar i `tests/test_make.sh`

**Grunngiving:** `specs/` er for spesifikasjonar (planlegging), ikkje dokumentasjon av noverande tilstand. `BUGS.md` er referansedokumentasjon som passar inn med andre root-dokument (GOVERNANCE.md, SCOPE.md, PRINCIPLES.md, CONVENTIONS.md).

## Tilleggstiltak: Eliminering av lenkjeduplisering i PoC-warning

### 7. Erstatt direkte lenkjer med anchor-lenkjer i PoC-warning
- [x] Endre lenke til `BUGS.md` → `#kjende-avgrensingar` (anchor til README-seksjon)
- [x] Endre lenke til `GOVERNANCE.md` → `#for-bidragsytarar` (anchor til README-seksjon)
- [x] Forkort teksten for GOVERNANCE-lenka

**Grunngiving:** Eliminerer duplisering av eksterne lenkjer — PoC-warning guidar brukarar gjennom README.md i rett rekkefølgje. Beheld "stop and think"-signalet i warning-boksen.

## Tilleggstiltak: Flytt "Versjonerte adresser" til ekstern-bruk.md

### 8. Flytt "Versjonerte adresser"-blokk frå README.md til mkdocs/docs/ekstern-bruk.md
- [x] Opprett ny seksjon "Versjonerte artefaktar" i `mkdocs/docs/ekstern-bruk.md` (mellom "AP-NO-skjema-URL-ar" og "GitHub Actions: reusable workflows")
- [x] Utvid innhaldet med døme på import med versjonert URL og anbefaling om å bruke konkret versjon-tag
- [x] Erstatt blokka i README.md med kort lenke til den nye seksjonen

**Grunngiving:** 
- Målgruppe: "Versjonerte adresser" er kritisk informasjon for eksterne brukarar som skal importere skjema — primærmålgruppa for `ekstern-bruk.md`
- Kontekst: Dokumentet har allereie relaterte seksjoner ("AP-NO-skjema-URL-ar" og "Versjonsfesta oppsett") — naturleg mellomsteg
- DRY: README.md skal vere oversikt med lenkjer til autoritative rettleiingar, ikkje duplisere detaljert bruksrettleiing

## Tilleggstiltak: Flytt "Kva publiserast til eksterne system" til arkitektur-oversikt.md

### 9. Flytt "Kva publiserast til eksterne system" frå README.md og index.md til arkitektur-oversikt.md
- [x] Legg til ny seksjon "Kva publiserast til eksterne system" i `mkdocs/docs/arkitektur-oversikt.md` (etter "Prinsipp: Pull, ikkje push" og før "Private system som kan høste")
- [x] Utvid innhaldet med detaljar om GitHub Pages-publisering, høstingsprosess og validering
- [x] Legg til lenkjer til detaljerte publiseringsrettleiingar (publisering-begrep.md, publisering-modell.md)
- [x] Erstatt seksjonen i README.md med kort lenke til arkitektur-oversikt.md
- [x] Erstatt duplikatet i mkdocs/docs/index.md med same lenke

**Grunngiving:**
- Eliminerer duplikasjon: Seksjonen var identisk i README.md og index.md
- Naturleg plassering: `arkitektur-oversikt.md` handlar om publiseringsflyt og arkitekturprinsipp
- DRY: Éin autoritative kjelde for publiseringsinformasjon
- Kontekst: Seksjonen passar perfekt mellom "Pull, ikkje push"-prinsippet og "Private system som kan høste"

## Tilleggstiltak: Omdøyp arkitektur-oversikt.md til publisering-oversikt.md

### 10. Omdøyp arkitektur-oversikt.md til publisering-oversikt.md
- [x] `mv mkdocs/docs/arkitektur-oversikt.md mkdocs/docs/publisering-oversikt.md`
- [x] Oppdater alle referansar i mkdocs/docs/index.md
- [x] Oppdater alle referansar i mkdocs/docs/monitorering.md (lenketekst → "Publiseringsoversikt")
- [x] Oppdater alle referansar i README.md og test_README.md

**Grunngiving:** Filnamnet `publisering-oversikt.md` er meir presis — dokumentet handlar om publiseringsflyt, høsting og artefaktar, ikkje generell systemarkitektur.

---

## Utført

Alle tiltak 1-10 er gjennomførte, inkludert Makefile-integrasjon.

**Resultat:**

- ✅ README.md oppdatert med nye skjema (brreg-begrepskatalog, enhetsregisteret-bvrinn, referanse)
- ✅ README.md oppdatert med nye domene (modellkatalog, referanse)
- ✅ Ny seksjon "Genererte modellkatalogar" med tabell over 6 modellkatalogar
- ✅ Dokumentasjonsstruktur omorganisert: SCOPE.md, PRINCIPLES.md, CONVENTIONS.md opprett på root
- ✅ Automatisert generering av domene-, skjema- og modellkatalog-tabellar med `scripts/generate-readme-tables.sh`
- ✅ Makefile-integrasjon: `make docs-publish` køyrer no generate-readme-tables.sh automatisk før mkdocs-publisering
- ✅ Bugs-dokumentasjon flytta frå specs/bugs/ til root (BUGS.md, bugs/)
- ✅ README.md kompakt: lenkjer til autoritative dokument i staden for å duplisere innhald
  - "Kjende avgrensingar" og "Designprinsipp og konvensjonar" flytta tidlegare i README.md
  - "Versjonerte adresser" flytta til mkdocs/docs/ekstern-bruk.md
  - "Kva publiserast til eksterne system" flytta til mkdocs/docs/publisering-oversikt.md (tidlegare arkitektur-oversikt.md)
- ✅ Eliminert duplisering:
  - PoC-warning brukar anchor-lenkjer i staden for direkte fillenker
  - Publiseringsseksjon fjerna frå mkdocs/docs/index.md (lenker til publisering-oversikt.md)
- ✅ Omdøypt mkdocs/docs/arkitektur-oversikt.md → publisering-oversikt.md for å spegle faktisk innhald

**Dato gjennomført:** 2026-07-09
