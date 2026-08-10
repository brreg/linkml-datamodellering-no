# Gap-analyse: repoet mot Digdir sin veileder "Slik blir du en god datatilbyder"

**Opprett:** 2026-08-10
**Status:** Kartlagt, verifisert mot primærkjelde — ikkje utført

## Bakgrunn

Brukaren ba om å evaluere gapet mellom dette repoet og Digdir si side
[«Slik blir du en god datatilbyder»](https://www.digdir.no/datadeling/slik-blir-du-en-god-datatilbyder/2248),
inkludert underside
[«Sjekkliste for datatilbyder»](https://www.digdir.no/datadeling/sjekkliste-datatilbyder/2273).

`digdir.no` var mellombels nede for vedlikehald ved første forsøk. Begge
sidene er no henta direkte og verifisert — denne versjonen av specen
byggjer på fullstendig sidetekst, ikkje søkefragment som i eit tidlegare
utkast.

### Hovudinnhald på sida

- **Datakatalog og oversikt:** krav om å skaffe oversikt over eigne data
  (lenkjer vidare til "Orden i eget hus" og veiledning for
  datasettbeskrivingar)
- **Distribusjonsmetodar:** tilrår standardiserte datatenester og
  grensesnitt basert på beste praksis — nemner eksplisitt **OpenAPI
  Specification** og **GraphQL**
- **Dokumentasjon og skildring:** obligatoriske felt for eit datasett —
  tittel, nøkkelord, skildring, lenke til begrepsdefinisjonar, ansvarleg
  utgjevar med kontaktinfo, publiserings-/endringsdatoar,
  tilgangsnivåkategorisering, lenke til distribusjonar, datatenestens
  tittel og endepunkt
- **Tilgangsnivå:** tre EU-standardiserte kategoriar — Allmenn tilgang /
  Betinget tilgang / Ingen allmenn tilgang
- **Krav til offentlege verksemder:** synleggjere datasett/datatenester på
  data.norge.no jf. Digitaliseringsrundskrivet (via registreringsløysing
  på data.norge.no, Geonorge.no for kart-/eigedomsdata, eller
  standardisert katalog til høsting)
- **Forvaltning:** rutinar for drift saman med konsumentar,
  tenesteavtale (SLA), konfidensialitet/integritet/tilgjengelegheit,
  vedlikehald av datasettskildringar
- **Sikkerheit/personvern:** NSM grunnprinsipp, Datatilsynets veileder for
  innebygd personvern, referansearkitektur for datautveksling
- **Autentisering/autorisasjon:** Maskinporten, ID-porten, Altinn
  autorisasjon, data.altinn.no
- **Styringsdokument:** Regjeringas retningslinjer ved
  tilgjengeliggjøring av offentlege data (15 punkt) — **allereie
  gap-analysert separat**, sjå
  [`specs/done/avvik-retningslinjer-apne-data.md`](../done/avvik-retningslinjer-apne-data.md)
- **Støtteressursar:** Datalandsbyen, Nasjonalt ressurssenter for deling
  og bruk av data, nasjonale fellesløysingar

### Sjekklista (alle punkt, verifisert ordrett)

**Steg 1: Holde orden i data og ansvar**
- Kartlagt informasjon som vert oppretta/handsama
- Oversikt over kva data som kan delast
- Data skildra etter felles standardar, begrep og informasjonsmodellar
- Heimelsgrunnlag for å dele skjerma data
- Kjennskap til eige ansvar som datatilbydar

**Steg 2: Gjøre data tilgjengelig og klargjøre for deling**
- Etablert teknisk løysing for publisering av datasett
- Publisert datasett og API-ar på data.norge.no
- Angitt om dataa er ei autoritativ kjelde
- Skildra korleis konsument får tilgang til dataa
- Etablert standardiserte grensesnitt for maskinell dataoverføring

**Steg 3: Vurdere tilgang til data**
- Lovheimel for å dele skjerma data
- Konsumenten har behandlingsgrunnlag
- Dataminimering (ikkje delt personopplysningar konsumenten ikkje treng)
- Roller og ansvar mellom partane avklart
- Naudsynte avtalar inngått (deling, bruk, behandling, drift, forvaltning)

**Steg 4: Gi tilgang til data**
- Deler som opne offentlege data der mogleg
- Etablert teknisk løysing for utveksling
- Nyttar fellesløysingar/-komponentar
- Nyttar standardiserte grensesnitt for utveksling
- Vernar konfidensialitet/integritet/tilgjengelegheit ved overføring
- Identifisert rett mottakarnivå hos verksemda
- God tilgangsstyring ved utveksling
- Risikovurdering av vald løysing

**Steg 5: Dele data**
- Gode rutinar for drift/forvaltning av tekniske løysingar
- Godt samarbeid om endringshandtering + risikovurdering ved store endringar
- Alle partar bidreg til informasjonssikkerheit/forbetring
- Gode rutinar for forvaltning av inngåtte avtalar

## Samandrag

Sjekklista sitt **Steg 1** overlappar sterkt med Digdir sin systerveileder
"Orden i eget hus", som allereie er grundig gap-analysert i
[`specs/done/avvik-veileder-orden-i-eget-hus.md`](../done/avvik-veileder-orden-i-eget-hus.md).
**Steg 3-5** er i all hovudsak juridiske, organisatoriske og
driftsmessige krav retta mot den einskilde verksemda si eiga
datadelingsinfrastruktur (avtalar, roller, tilgangsstyring,
risikovurdering, fellesløysingar for autentisering) — dette er tydeleg
**utanfor scope** for eit reint informasjonsmodelleringsverktøy, jf.
[SCOPE.md](../../SCOPE.md) ("Ein integrasjonsplattform", "Eit verktøy for
enkeltverksemder").

**Steg 2** er der repoet har mest å seie:

- Dei obligatoriske felta for datasettskildring (tittel, nøkkelord,
  skildring, begrepslenke, utgjevar+kontaktinfo, datoar, tilgangsnivå,
  distribusjonslenke) er **alle til stades** i
  `dcat-ap-no-schema.yaml`, og dei fleste handheva som `Obligatorisk`
  eller `Anbefalt` på `Datasett`-klassen.
- "Datatenestens tittel og endepunkt" er **fullt dekt** av
  `Datatjeneste`-klassen (`dcat:DataService`,
  `dcat-ap-no-schema.yaml:655-701`) — `tittel`, `kontaktpunkt`,
  `utgiver` og `endepunkts_url` er alle `Obligatorisk`.
- Dei tre EU-standardiserte tilgangsnivåa (Allmenn/Betinget/Ingen
  allmenn) samsvarar **eksakt** med `PUBLIC`/`RESTRICTED`/`NON_PUBLIC` i
  `tilgangsrettigheter`-feltet, som alt er handheva som `warning`
  (silver) / `error` (gold) etter førre gap-analyse.
- "Angi om dataa er ei autoritativ kjelde" er **delvis dekt** av
  `eierskapshistorikk`/`dct:provenance` (sjå Gap 2).
- "Etablert standardiserte grensesnitt for maskinell dataoverføring" er
  **sterkt dekt** av artefaktgenereringa (JSON Schema, SHACL, OpenAPI,
  AsyncAPI, Protobuf, XSD) — men eitt konkret namngjeve standard manglar:
  **GraphQL** (sjå Gap 3).

**Ingen** av gapa som er identifiserte krev skjemabrytande endringar.

## Identifiserte gap

### Gap 1: Ingen kryssreferanse til «Slik blir du en god datatilbyder»/«Sjekkliste for datatilbyder» i repoet

`grep` etter "datatilbyder" i normativ dokumentasjon gir ingen treff
utanom denne specen. Ein brukar som kjem frå sjekklista sitt Steg 2 (t.d.
"har de publisert datasett og API-ar på data.norge.no?", "er det
etablert standardiserte grensesnitt for maskinell overføring?") får
ingen peikepinn i `mkdocs/docs/publisering/publisering-oversikt.md` eller
`SCOPE.md` om at:
- repoet sitt artefaktbibliotek direkte svarar på det tekniske
  grensesnitt-punktet
- publiseringsflyten til data.norge.no alt er dokumentert i
  `publisering-oversikt.md`
- Steg 1 i sjekklista i stor grad er dekt av arbeidet skildra i
  `avvik-veileder-orden-i-eget-hus.md`

**Forslag:** Legg til eit kort avsnitt i
`mkdocs/docs/publisering/publisering-oversikt.md` (nær innleiinga) som
lenkjer til «Slik blir du en god datatilbyder»/«Sjekkliste for
datatilbyder» og forklarer kva for sjekklistepunkt (Steg 1-2 særleg)
repoet dekkjer, med tydeleg avgrensing mot Steg 3-5 som er utanfor scope.

### Gap 2 (lite, sannsynlegvis alt tilstrekkeleg dekt): "Autoritativ kjelde"-indikator

Sjekklista sitt Steg 2 spør eksplisitt "har dere angitt om dataene er en
autoritativ kilde?". Den førre gap-analysen løyste eit tilsvarande punkt
frå "orden i eget hus" ved å presisere `eierskapshistorikk`-slotens
(`dct:provenance`) `description` med kjeldetype-bruk
(autoritativ/sjølvinnsamla vs. avleidd/samanstilt), jf.
`dcat-ap-no-schema.yaml:1162-1168`.

Feltet er fritekst, ikkje eit strukturert/handheva ja/nei-signal, så det
er ei mjuk løysing på eit krav som kan tolkast som å ønske eit tydelegare
maskinlesbart svar. Gitt at feltet og forklaringa alt finst, og DRY-
prinsippet i CLAUDE.md, føreslår denne analysen **ikkje** ei ny
skjemaendring — berre at kryssreferansen i Gap 1 peikar hit, slik at
sjekklistebrukarar finn den eksisterande løysinga.

### Gap 3: GraphQL er ikkje blant repoets standardiserte grensesnitt-artefakt

Digdir nemner **eksplisitt** OpenAPI Specification og GraphQL som
standardiserte teknologiar for datatenester under "Distribusjonsmetoder".
Repoet genererer OpenAPI (`make gen-openapi`, `openapi: true` i
`build.yaml`) og AsyncAPI, men har **ingen GraphQL-generator** —
`grep` etter `gen-graphql` i `make/*.mk` gir ingen treff, og ingen
`build.yaml` har eit `graphql`-flagg.

**Stadfesta:** LinkML har ein innebygd GraphQL-generator —
[`gen-graphql`](https://linkml.io/linkml/generators/graphql.html),
implementert av `linkml.generators.graphqlgen.GraphqlGenerator`. Han tek
eit LinkML-skjema (YAML) som input og produserer GraphQL-typedefinisjonar
(`.graphql`-fil med SDL), med støtte for arv via GraphQL sitt
`implements`-nøkkelord og valfri metadata-inkludering. Generatoren er
**output-only** — han lagar berre skjemadefinisjonar, ikkje
runtime-bindingar/resolverar, same avgrensing som repoet allereie har for
t.d. `gen-openapi` (spesifikasjon, ikkje kjørande API).

**Versjon verifisert:** `src/assets/containers/Dockerfile.linkml:7` pinnar
`linkml==1.11.1`. Kontrollert direkte mot GitHub-taggen `v1.11.1`
(`api.github.com/repos/linkml/linkml/contents/...`):
`packages/linkml/src/linkml/generators/graphqlgen.py` finst i denne
versjonen, og `packages/linkml/pyproject.toml` registrerer CLI-kommandoen
(`gen-graphql = "linkml.generators.graphqlgen:cli"`). Generatoren er
altså tilgjengeleg i containerbiletet slik det er i dag — **ingen ny
Dockerfile-avhengigheit eller versjonsoppgradering trengst**, og dermed
heller ingen ny attribution i `mkdocs/docs/om.md`.

**Forslag:** Legg til `make gen-graphql` etter same mønster som
`gen-openapi` (`make/*.mk`), med tilhøyrande `graphql`-flagg i
`build.yaml`-manifestet (default `false`, aktiverast per skjema) og ei ny
rad i artefakttabellen i `SCOPE.md`, i tråd med korleis dei andre
generatorane (`gen-jsonschema`, `gen-shacl` osv.) alt er kopla på.
Framleis eiga sak/spec, ikkje bunta inn i Gap 1/2-utføringa, sidan det er
eit nytt artefakt-generator-arbeid.

## Ikkje-gap (vurdert, men ingen tiltak)

- **Steg 1 (Holde orden i data og ansvar):** Overlappar med "orden i eget
  hus", som alt er grundig dekt av
  `specs/done/avvik-veileder-orden-i-eget-hus.md`. Ingen nye tiltak.
- **Steg 2 — obligatoriske datasettfelt:** Alle til stades og handheva
  (`tittel`, `kontaktpunkt`, `tema`, `utgiver`, `beskrivelse` er
  `Obligatorisk`; `nokkelord`, `begrep`, `utgivelsesdato`,
  `endringsdato`, `tilgangsrettigheter` er `Anbefalt`/handheva via
  policy). Ingen tiltak.
- **Steg 2 — "datatenestens tittel og endepunkt":** Fullt dekt av
  `Datatjeneste`-klassen (`dcat:DataService`). Ingen tiltak.
- **Steg 2 — publisering til data.norge.no:** Pull-arkitekturen
  (`publish_external: true`, `felles-datakatalog`-policy, GitHub Pages
  som høstingsendepunkt) er alt dokumentert i `publisering-oversikt.md`
  og handsama grundig tidlegare i
  `specs/done/gap-sharing-data-norge-no.md`. Ingen tiltak utover
  kryssreferansen i Gap 1.
- **Steg 2 — publisering av API-ar på data.norge.no spesifikt:** Dette
  gjeld API-katalogen, som er ein separat katalog frå datasett-/
  begrepskatalogen. Repoet genererer OpenAPI/AsyncAPI som artefakt, men
  publisering til API-katalogen er ikkje sett opp. Vurdert som eiga,
  potensiell framtidig sak — ikkje bunta inn her, sidan det krev
  avklaring av kva API-katalogen forventar av innhaldsformat.
- **Steg 3-5 (Vurdere tilgang / Gi tilgang / Dele data):** Juridiske
  avtalar, rolleavklaring, tilgangsstyring, risikovurdering,
  autentiseringsløysingar (Maskinporten/ID-porten/Altinn),
  fellesløysingar/-komponentar, driftsrutinar. Alt organisatorisk/
  infrastrukturelt hos den einskilde verksemda, eksplisitt utanfor
  SCOPE.md sine avgrensingar ("Ein integrasjonsplattform", "Eit verktøy
  for enkeltverksemder"). Ingen tiltak.
- **15-punkts retningslinjer for tilgjengeliggjøring:** Allereie
  gap-analysert separat i
  `specs/done/avvik-retningslinjer-apne-data.md`. Ingen nytt arbeid her.
- **Sikkerheit/personvern (NSM, Datatilsynet, referansearkitektur for
  datautveksling):** Driftssikkerheitskrav for den einskilde løysinga,
  ikkje eit skjemamodelleringsspørsmål. Ingen tiltak.

## Handlingsliste

- [ ] Legg til kryssreferanse-avsnitt i
      `mkdocs/docs/publisering/publisering-oversikt.md` som lenkjer til
      «Slik blir du en god datatilbyder»/«Sjekkliste for datatilbyder»,
      kartlegg kva repoet dekkjer (Steg 1-2) og peikar til
      `avvik-veileder-orden-i-eget-hus.md` for Steg 1-overlappen (Gap 1)
- [ ] I same avsnitt: nemn at "autoritativ kjelde"-punktet er dekt av
      `eierskapshistorikk`/`dct:provenance` (Gap 2, ingen skjemaendring)
- [x] Legg til `make gen-graphql` og `graphql`-flagg i `build.yaml`-
      manifestet (Gap 3) — utført som eiga sak, sjå
      `specs/done/gen-graphql-generator.md`

Gap 1 og 2 er reint dokumentasjonsarbeid og kan gjerast saman. Gap 3 er
eit separat, større spørsmål og bør ikkje blandast inn i same
commit/spec-utføring.
