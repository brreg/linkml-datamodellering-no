# Gap-analyse: repoet mot data.norge.no/nb/docs (heile dokumentasjonsrota)

**Opprett:** 2026-08-10
**Status:** Utført

## Bakgrunn

Brukaren ba om å evaluere gapet mellom repoet og dokumentasjonsrota på
[data.norge.no/nb/docs](https://data.norge.no/nb/docs). Ein tilsvarande
gap-analyse mot undersida `/nb/docs/sharing-data` (+ `metadata-quality`,
`catalogs/information-models`, `catalogs/concepts`) vart allereie gjort same
dag og arkivert i `specs/done/gap-sharing-data-norge-no.md`, med alle tre
funne gap retta.

Brukaren stadfesta (via avklaringsspørsmål) at denne runda skal avgrensast
til dei sidene som **ikkje** vart dekte av den førre analysen:

- `/nb/docs/catalogs` — oversikt over katalogtypar
- `/nb/docs/catalogs/datasets` — datasettkatalogar (DCAT-AP-NO)
- `/nb/docs/catalogs/data-services` — API/datatenestekatalogar (DCAT-AP-NO)
- `/nb/docs/catalogs/public-services-and-events` — tenester/hendingar (CPSV-AP-NO)
- `/nb/docs/finding-data` — korleis brukarar søkjer/finn data
- `/nb/docs/resources` — verktøy- og læringsressursar
- `/nb/docs/community` — "Datalandsbyen"

`/nb/docs/records-of-processing-activities` er allereie vurdert som ikkje
relevant (GDPR-artikkel 30, utanfor scope) i den førre analysen og er ikkje
gjennomgått på nytt.

Samanlikninga er gjort mot `SCOPE.md`, README.md, `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
(klassane `Datasett` og `Datatjeneste`), `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`,
og `mkdocs/docs/publisering/publisering-oversikt.md`.

## Samandrag

Repoet dekkjer alle fem katalogtypane data.norge.no definerer
(`/nb/docs/catalogs`) gjennom AP-NO-importprofilane sine, med fullstendig
feltdekning samanlikna med krava på data.norge.no sine sider:

| Katalogtype (data.norge.no) | AP-NO-profil i repoet | Status |
|---|---|---|
| Datasett | `dcat-ap-no` → `Datasett` | Alle obligatoriske/anbefalte felt dekte |
| API/datatenester | `dcat-ap-no` → `Datatjeneste` | Alle obligatoriske/anbefalte felt dekte |
| Begrep | `skos-ap-no` | Dekt (verifisert i førre analyse) |
| Informasjonsmodellar | `modelldcat-ap-no` | Dekt (verifisert i førre analyse) |
| Tenester og hendingar | `cpsv-ap-no` | Fullstendig klassesett (OffentligTjeneste, Hendelse, Livshendelse, Virksomhetshendelse m.fl.) |

README.md har allereie ein tabell (linje ~199-203) som lenkjer kvar
AP-NO-profil til rett data.norge.no-spesifikasjon. Dette er difor **ikkje
eit gap**, men ei stadfesting av at importhierarkiet allereie realiserer
heile breidda av data.norge.no sine katalogtypar.

Det er identifisert **eitt reelt dokumentasjonsgap** og **eitt valfritt
forbetringspunkt**.

## Identifiserte gap

### Gap 1: Repoet si eiga skjemavalidering vert ikkje kryssjekka mot data.norge.no sin offisielle instansvalidator

`/nb/docs/resources` listar ein offisiell valideringstenestefor RDF-instansar:
[data.norge.no/validator](https://data.norge.no/validator), som validerer
"datasettbeskrivelser (DCAT-AP-NO), begrepsbeskrivelser (SKOS-AP-NO) og
tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO) i RDF-format". Merk at denne
validatoren **ikkje** dekkjer ModellDCAT-AP-NO (informasjonsmodellar).

Repoet sin eigen valideringsflyt (`make mcp-linkml-valider-modell ...
POLICY=felles-begrepskatalog/felles-datakatalog`, sjå steg 1 i sjekklista i
`publisering-oversikt.md`) validerer **skjemakvaliteten** til LinkML-skjemaet
og genererer SHACL-shapes automatisk derifrå. Denne SHACL-en er avleidd frå
LinkML-strukturen, ikkje identisk med dei kanoniske SHACL-shapes data.norge.no
sjølv brukar i sin offisielle validator. Ein datafil kan difor bestå repoet
sin eigen validering utan at den genererte RDF-instansen naudsynleg består
data.norge.no sin offisielle validator.

Dette er same type presiseringsbehov som Gap 1 i `gap-sharing-data-norge-no.md`
(bronze/silver/gold ≠ data.norge.no sin kvalitetsskala), men gjeld eit anna
konkret verktøy (instansvalidator, ikkje kvalitetsskåre) som ikkje vart
handsama i den førre analysen.

**Forslag:** Legg til eit punkt i sjekklista i
`mkdocs/docs/publisering/publisering-oversikt.md` (§ "Felles Begrepskatalog
/ Felles Datakatalog") som tilrår å køyre den genererte RDF-instansen
(`.ttl`-fila som vert publisert til GitHub Pages) gjennom
[data.norge.no/validator](https://data.norge.no/validator) før
høstingsendepunktet vert registrert, med presisering om at validatoren
ikkje dekkjer ModellDCAT-AP-NO.

## Ikkje-gap (vurdert, men ingen tiltak)

- **Datasett-feltdekning (`/nb/docs/catalogs/datasets`):** Alle påkravde felt
  (eigar/`utgiver`, tittel/`tittel`, formål/tema-dekt via `beskrivelse`+`tema`,
  geografisk dekning/`dekningsomraade`, oppdateringsfrekvens/`frekvens`,
  tilgangsrettar/`tilgangsrettigheter`, språk/`spraak`, kontaktpunkt/`kontaktpunkt`,
  relasjonar/`relatert_ressurs`, relaterte begrep/`begrep`,
  distribusjonar/`datasettdistribusjon`) finst i `Datasett`-klassa i
  `dcat-ap-no-schema.yaml` — ingen tiltak.
- **API/datateneste-feltdekning (`/nb/docs/catalogs/data-services`):** Alle
  nemnde felt (skildring, tilgjengelege format, kontaktinfo, relaterte
  datasett) finst i `Datatjeneste`-klassa — ingen tiltak.
- **Tenester og hendingar (`/nb/docs/catalogs/public-services-and-events`):**
  Sida sjølv listar ingen konkrete tekniske krav utover å nemne katalogtypen.
  `cpsv-ap-no-schema.yaml` har eit fullstendig klassesett som dekkjer CPSV-AP-NO
  — ingen tiltak.
- **Finn data / søkbarheit (`/nb/docs/finding-data`):** Krev rike, presise
  titlar/skildringar/nøkkelord for søkbarheit. Dette er allereie grunngjevinga
  bak fleire gold-policy-reglar (t.d. `schema.title til stades`, grunngjeve med
  "gjer ressursen søkbar" i `src/mcp-linkml-validator/policies/README.md` linje
  166) — ingen tiltak.
- **Verktøyressursar (`/nb/docs/resources`):** Sida listar Python-bibliotek
  for å konvertere eksisterande datakjelder til RDF (`datacatalogtordf`,
  `concepttordf`, `modelldcatnotordf`, `servicecatalogtordf`, `oastodcat`,
  `atlasdcat`, `jsonschematordf`). Desse løyser same problem som repoet sin
  eigen LinkML-baserte genereringspipeline, men for organisasjonar utan
  LinkML-skjema. Å referere desse i repoet ville vore eit alternativt
  verktøyspor utanfor `SCOPE.md` — ingen tiltak.
- **Datalandsbyen (`/nb/docs/community`):** Ope diskusjonsforum utan
  spesifikke krav til publiserande organisasjonar. Ikkje eit gap, men kan
  vurderast som ei valfri lenke i støtte-/hjelpeseksjonar — sjå eiga vurdering
  under.

## Handlingsliste

- [x] Legg til tilråding om å køyre generert RDF-instans gjennom
      [data.norge.no/validator](https://data.norge.no/validator) før
      registrering av høstingsendepunkt, i sjekklista i
      `mkdocs/docs/publisering/publisering-oversikt.md` (Gap 1)

## Utført

- `mkdocs/docs/publisering/publisering-oversikt.md`: utvida punkt 1 i
  høstingssjekklista (§ "Felles Begrepskatalog / Felles Datakatalog") med
  presisering om at repoet sin eigen SHACL-validering er avleidd frå
  LinkML-skjemaet og skil seg frå data.norge.no sine kanoniske shapes, og
  tilråding om å køyre generert `.ttl` gjennom data.norge.no/validator
  (med merknad om at ModellDCAT-AP-NO ikkje er dekt der) før
  høstingsregistrering
