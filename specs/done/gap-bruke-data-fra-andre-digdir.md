# Gap-analyse: repoet mot digdir.no/datadeling/slik-kommer-du-i-gang-med-bruke-data-fra-andre

**Opprett:** 2026-08-11
**Status:** Utført

## Bakgrunn

Brukaren ba om å evaluere gapet mellom dette repoet og rettleiinga
[«Slik kommer du i gang med å bruke data fra andre»](https://www.digdir.no/datadeling/slik-kommer-du-i-gang-med-bruke-data-fra-andre/2255)
hos Digitaliseringsdirektoratet. Sida er retta mot **databrukarar** —
organisasjonar som skal *finne* og *ta i bruk* data frå andre verksemder —
og dekkjer:

1. **Finne data** — data.norge.no sitt søk, Geonorge, transportportal.no;
   presiserer at katalogane berre inneheld *skildringar av og lenker til*
   data, ikkje sjølve dataa
2. **Tilgang og bruksvilkår** — ope tilgjengelege data (CC BY 4.0),
   allmenn tilgang (offentleglova), vilkårsbunden tilgang (betaling,
   avtale) og ikkje-offentleg tilgang (heimel kravd, evt. anonymisering)
3. **Offentlege dokument** — eInnsyn for journalar/dokument hos statlege verksemder
4. **Ressursar for databrukarar** — Nasjonalt ressurssenter for deling og
   bruk av data, NSM sine IKT-sikkerheitsprinsipp, Datatilsynet sitt
   personvern-i-designverktøy, referansearkitektur for datadeling,
   Maskinporten/ID-porten/Altinn for autentisering/autorisasjon mot API-ar
5. Lenke til ei eiga «Sjekkliste for datakonsument»

Samanlikninga er gjort mot `SCOPE.md` (særleg tabellen «Kva repoet IKKJE
er»), `PRINCIPLES.md`, `GOVERNANCE.md`, `mkdocs/docs/om.md`, README.md og
`specs/backlog/nasjonal-datamesh-arkitektur.md` (lagmodellen der repoet er
plassert i «Modelleringslaget», med data.norge.no sitt søk i eit eige
«Oppdagelseslag»).

## Samandrag

Digdir-sida er skriven for **databrukarar** (den som skal finne og
konsumere andre sine data). Dette repoet er verktøy for **datamodellerarar
og datatilbydarar** (den som skildrar og publiserer metadata om eigne data)
— den andre sida av same relasjon. Dei to rollene er eksplisitt skilde i
`SCOPE.md` sin tabell «Kva repoet IKKJE er» (repoet er verken ein
datakatalog, eit API eller ein integrasjonsplattform) og i
lagmodellen i `nasjonal-datamesh-arkitektur.md`, der «Oppdagelseslaget»
(data.norge.no sitt søk — sida denne analysen gjeld) ligg **over**
«Modelleringslaget» (dette repoet).

Konklusjonen er difor at **så godt som heile guiden er ikkje-gap** — han
skildrar eit brukstilfelle repoet bevisst ikkje dekkjer. Det eine funnet er
eit reint dokumentasjonsgap: repoet peikar ikkje ein feilnavigert
databrukar vidare til rett stad.

## Identifiserte gap

### Gap 1: Ingen peikar til databrukar-rettleiinga for lesarar som kjem feil

`SCOPE.md` sin tabell «Kva repoet IKKJE er» slår fast at repoet ikkje er
ein datakatalog, ikkje eit API og ikkje ein integrasjonsplattform — men
seier ikkje **kor** ein databrukar (i staden for ein datatilbydar) bør gå.
Nokon som søkjer etter "korleis bruke data frå andre" og hamnar i dette
repoet via generelt søk, finn ingen peikar vidare til data.norge.no sitt
søk eller til Digdir-guiden.

**Forslag:** Legg til éi kort kryssreferanse-linje i `SCOPE.md`, rett under
tabellen «Kva repoet IKKJE er», som peikar databrukarar til
data.norge.no sitt søk og Digdir sin guide.

## Ikkje-gap (vurdert, men ingen tiltak)

- **Finne data (søkjefunksjonen på data.norge.no, Geonorge,
  transportportal.no):** Reint oppdagelseslag-funksjonalitet. Repoet
  publiserer metadata *til* desse katalogane (pull-basert, jf.
  [PRINCIPLES.md § 6](../../PRINCIPLES.md#6-pull-ikkje-push)), men er
  ikkje sjølv eit søkjegrensesnitt. `SCOPE.md` presiserer alt at repoet
  ikkje er ein datakatalog.
- **Tilgang og bruksvilkår (CC BY 4.0, allmenn tilgang,
  vilkårsbunden/ikkje-offentleg tilgang):** Gjeld tilgang til *faktiske
  datasett*. Repoet inneheld ikkje produksjonsdata (med unntak av
  begreps-/modellkatalog-data under `data/`-katalogar, som er metadata om
  modellar — ikkje datasett med tilgangsvilkår). Lisensfeltet i repoet sine
  skjema (`license: NLOD 2.0`, jf. `CONVENTIONS.md`) er alt handtert som
  eit *skjemametadata*-felt, ikkje eit tilgangsstyring-mekanisme —
  konsistent med at repoet ikkje sjølv styrer datatilgang.
- **eInnsyn (dokumentinnsyn):** Gjeld journalførte dokument hos statlege
  verksemder, heilt utanfor `SCOPE.md` sitt virkeområde (informasjonsmodellering,
  ikkje dokumentforvaltning).
- **Maskinporten/ID-porten/Altinn for API-autentisering:** Guiden nemner
  desse som autentiseringsmekanismar ein databrukar treng for å *kalle*
  API-ar hos datatilbydarar. Repoet eksponerer ikkje API-ar
  (`SCOPE.md`: "Eit API — NEI"), så dette gjeld ikkje repoet direkte.
  ID-porten/Altinn er alt dokumentert i repoet i ein annan, relevant
  samanheng: registrering av **høstingsendepunkt** hos Digitaliseringsdirektoratet
  (`GOVERNANCE.md`, `mkdocs/docs/publisering/publisering-modell.md`,
  `publisering-begrep.md`) — det er datatilbydar-sida av same
  Digdir-infrastruktur, alt dekt.
- **Referansearkitektur for datadeling, NSM-prinsipp,
  Datatilsynet-verktøy, Nasjonalt ressurssenter:** Generelle
  databrukar-ressursar utan direkte kopling til LinkML-modellering eller
  skjemapublisering. `nasjonal-datamesh-arkitektur.md` har alt plassert
  desse konseptuelt i lag utanfor repoet sitt ansvarsområde.
- **«Sjekkliste for datakonsument»:** Same grunngjeving — sjekklista er
  bygd for databrukar-rolla, som er motsett rolle av det repoet støttar.

## Handlingsliste

- [x] Legg til kryssreferanse-linje i `SCOPE.md` under tabellen «Kva
      repoet IKKJE er» som peikar databrukarar til data.norge.no og
      Digdir-guiden (Gap 1)

## Utført

- `SCOPE.md`: lagt til eit merknadsavsnitt rett under tabellen «Kva
  repoet IKKJE er» som forklarer at repoet er bygd for datatilbydar-rolla
  (modellering/publisering), med lenke vidare til data.norge.no sitt søk
  og til Digdir sin guide
  [«Slik kommer du i gang med å bruke data fra andre»](https://www.digdir.no/datadeling/slik-kommer-du-i-gang-med-bruke-data-fra-andre/2255)
  for lesarar som eigentleg søkjer etter data, ikkje modelleringsverktøy
