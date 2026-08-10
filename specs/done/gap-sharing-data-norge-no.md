# Gap-analyse: repoet mot data.norge.no/nb/docs/sharing-data

**Opprett:** 2026-08-10
**Status:** Utført

## Bakgrunn

Brukaren ba om å evaluere gapet mellom dette repoet og rettleiingsdokumentasjonen
på [data.norge.no/nb/docs/sharing-data](https://data.norge.no/nb/docs/sharing-data)
("Del data"). Denne sida er sjølve inngangsporten for korleis norske
verksemder deler data på den nasjonale portalen, og er difor det naturlege
målet å samanlikne repoets prinsipp og publiseringsmekanisme mot.

Sida sjølv er ein navigasjonsportal utan mykje konkret innhald — dei reelle
krava ligg i undersidene. Følgjande undersider vart henta og analyserte:

- `/sharing-data/how-to-dataset` — Datasettbeskrivelse frå A-Å
- `/sharing-data/publishing-data-descriptions` — Publisere datasettbeskrivelser
- `/sharing-data/rdf` — RDF: kva og kvifor
- `/sharing-data/login-and-access` — Få tilgang og logge inn
- `/docs/metadata-quality` — Metadatakvalitet
- `/docs/catalogs/information-models` — Informasjonsmodellar (ModellDCAT-AP-NO)
- `/docs/catalogs/concepts` — Begrep (SKOS-AP-NO-Begrep)

Samanlikninga er gjort mot `SCOPE.md`, `PRINCIPLES.md`, `GOVERNANCE.md`,
`CONVENTIONS.md`, `src/mcp-linkml-validator/policies/README.md`, og
skjemaa `dcat-ap-no-schema.yaml` / `skos-ap-no-schema.yaml`.

## Samandrag

Repoet er **allereie godt tilpassa** data.norge.no sin publiseringsmodell.
Dei to sentrale funna frå data.norge.no styrkar eksisterande prinsipp i
repoet, i staden for å avdekkje nye krav:

1. **Publiseringsmodellen stemmer overeins.** Data.norge.no støttar to
   publiseringsmåtar: eit innebygd skjema-verktøy, eller at ei verksemd
   registrerer eit **hausting-endepunkt** som data.norge.no pullar frå.
   Dokumentasjonen seier eksplisitt at *informasjonsmodellar* (og hendingar)
   **ikkje** kan skildrast i det innebygde verktøyet — hausting frå eige
   endepunkt er einaste veg. Dette er ei direkte stadfesting av
   [PRINCIPLES.md § 6 "Pull, ikkje push"](../../PRINCIPLES.md#6-pull-ikkje-push)
   og [GOVERNANCE.md](../../GOVERNANCE.md) sin publiseringspolicy — repoet sin
   arkitektur er den einaste farbare vegen for modellkatalog-bruk, ikkje berre
   eit designval.
2. **Skjemastandardane stemmer overeins.** Data.norge.no krev ModellDCAT-AP-NO
   for informasjonsmodellar og SKOS-AP-NO-Begrep for begrep — begge er
   allereie implementerte som AP-NO-profilskjema i repoet
   (`modelldcat-ap-no-schema.yaml`, `skos-ap-no-schema.yaml`) og handheva via
   `felles-datakatalog`- og `felles-begrepskatalog`-policyane.

Gapa som er identifiserte er difor **presiserings- og dokumentasjonsgap**,
ikkje strukturelle manglar.

## Identifiserte gap

### Gap 1: Metadatakvalitet-skalaen til data.norge.no er ikkje det same som bronze/silver/gold

Data.norge.no skårar publisert metadata på ein FAIR-basert prosentskala med
fire nivå (Utmerket ≥75 %, God 50–75 %, Tilstrekkeleg 25–50 %, Dårleg <25 %),
berekna **på hausta instansdata** (kvar publiserte datasett-/modelloppføring).
Repoet sine bronze/silver/gold-nivå validerer derimot **skjemakvaliteten**
(strukturelle krav på sjølve LinkML-skjemaet), ikkje dei hausta oppføringane.

Dette er allereie presisert delvis i `CLAUDE.md` ("Bronze/silver/gold
validerer skjemakvalitet, ikkje instansdata"), men det er ikkje eksplisitt
kopla til data.norge.no sin eigen kvalitetsskala noko stad. Ein brukar som
kjenner data.norge.no sin firetrinnsskala kan lett tru at "gold" i dette
repoet garanterer "Utmerket" hos data.norge.no — det er ikkje same måleeining.

**Forslag:** Legg til ei kort forklarande merknad i
`src/mcp-linkml-validator/policies/README.md` (der policy-hierarkiet
skildrast) som presiserer skiljet mot data.norge.no sin instansbaserte
kvalitetsskala, med lenke til `/nb/docs/metadata-quality`.

### Gap 2: Tekniske krav til hausting-endepunkt er ikkje dokumenterte i repoet

Data.norge.no sine sider oppgir ikkje presist kva tekniske krav som gjeld for
sjølve hausting-endepunktet (innhaldstype/content negotiation, forventa
serialisering, oppdateringsfrekvens). Repoet publiserer TTL-filer statisk via
GitHub Pages/Releases, og `GOVERNANCE.md` seier korrekt at hausting må
koordinerast manuelt med Digitaliseringsdirektoratet — men det finst ingen
sjekkliste i repoet for **kva den koordineringa konkret må avklare** (URL-ar
til dei publiserte TTL-filene, forventa content-type, om Digdir treng ei
enkelt indeks-fil eller kan crawle katalogstrukturen).

**Forslag:** Legg ei kort sjekkliste til i ein av filene under
`mkdocs/docs/publisering/` (t.d. `publisering-oversikt.md`, som allereie
skildrar hausting-flyten til eksterne katalogar) med dei konkrete spørsmåla
ein organisasjon må avklare med Digdir før `publish_external: true` vert
sett, jf. `GOVERNANCE.md` § "Krav i PoC-fasen" punkt 4. Dette er reint
dokumentasjonsarbeid, ingen skjemaendring.

### Gap 3: Tilgang/pålogging-prosessen hos data.norge.no er ikkje nemnd i onboarding-sjekklista

`GOVERNANCE.md` sin onboarding-sjekkliste for nye organisasjonar dekkjer
GitHub-tilgang og CODEOWNERS, men nemner ikkje at organisasjonen **også** må
gjennom data.norge.no sin eigen tilgangsprosess (verksemdsadministrator
godkjenner bruksvilkår via Altinn/ID-porten, nivå 3) før dei kan registrere
eit hausting-endepunkt der. Dette er eit steg utanfor repoet, men det er
ein føresetnad for at publiseringa i praksis skal fungere, og bør nemnast
som eit informasjonspunkt slik at nye organisasjonar ikkje vert overraska.

**Forslag:** Legg til eitt punkt i onboarding-sjekklista i `GOVERNANCE.md`
(§ "Onboarding av ny organisasjon") som opplyser om at
verksemdsadministrator separat må godkjenne bruksvilkår på data.norge.no
via Altinn/ID-porten før hausting kan setjast opp, med lenke til
`/nb/docs/sharing-data/login-and-access`.

### Ikkje-gap (vurdert, men ingen tiltak)

- **RDF-format/serialisering:** Data.norge.no grunngjev RDF-bruken med
  interoperabilitet og samanheng med data.europa.eu. Repoet genererer
  allereie TTL, JSON-LD og OWL — godt dekt, ingen tiltak.
- **Datasettbeskrivelse frå A-Å (distribusjon/datatjeneste):** Gjeld
  publisering av faktiske datasett. Repoet er ikkje ein datakatalog
  (`SCOPE.md`) og publiserer ikkje datasett direkte — kun begrep- og
  modellkatalog-artefakt. Denne rettleiinga er difor ikkje direkte
  relevant for repoet sitt virkeområde.
- **Behandlingsoversikt (records of processing activities):** Ikkje
  relevant — gjeld GDPR-artikkel 30-oversikt, utanfor repoets scope.
- **SKOS-AP-NO-Begrep feltdekning:** Data.norge.no krev definisjon,
  gyldigheit, tillatne/frårådde termar, fagområde og kontaktpunkt.
  `skos-ap-no-schema.yaml` har alle desse (`definisjon`, `gyldig_fra`,
  `gyldig_til`, `tillate_term`, `forkasta_term`, `fagomrade`,
  `kontaktpunkt_vcard`) — ingen tiltak.
- **Lisensfelt i DCAT-AP-NO:** `lisens`-slot finst og er obligatorisk på
  relevante klassar i `dcat-ap-no-schema.yaml` — ingen tiltak.

## Handlingsliste

- [x] Legg til presisering om data.norge.no sin kvalitetsskala i
      `src/mcp-linkml-validator/policies/README.md` (Gap 1)
- [x] Legg til sjekkliste for hausting-koordinering med Digdir i
      `mkdocs/docs/publisering/publisering-oversikt.md` (Gap 2)
- [x] Legg til informasjonspunkt om data.norge.no-tilgang i
      onboarding-sjekklista i `GOVERNANCE.md` (Gap 3)

Alle tre tiltak er reint dokumentasjonsarbeid (ingen skjema- eller
kodeendringar) og kan gjerast uavhengig av kvarandre.

## Utført

- `src/mcp-linkml-validator/policies/README.md`: lagt til merknad under
  "Nivå for skjemakvalitet" som presiserer at bronze/silver/gold måler
  skjemakvalitet, ikkje det same som data.norge.no sin instansbaserte
  FAIR-prosentskala, med lenke til `/nb/docs/metadata-quality`
- `mkdocs/docs/publisering/publisering-oversikt.md`: lagt til sjekkliste
  ("Sjekkliste før registrering av høstingsendepunkt hos
  Digitaliseringsdirektoratet") i seksjonen om Felles
  Begrepskatalog/Datakatalog, med kryssreferansar til `monitorering.md`
  og `GOVERNANCE.md`
- `GOVERNANCE.md`: lagt til punkt 4 "Tilgang på data.norge.no" i
  onboarding-sjekklista, som opplyser om separat bruksvilkår-godkjenning
  via Altinn/ID-porten, med lenke til data.norge.no og til den nye
  sjekklista i `publisering-oversikt.md`
