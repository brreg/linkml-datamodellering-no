# Gap-analyse: repoet mot digdir.no/datadeling/nasjonale-grunndata

**Opprett:** 2026-08-11
**Status:** Utført

## Bakgrunn

Brukaren ba om å evaluere gapet mellom dette repoet og Digdir-sida
[«Nasjonale grunndata»](https://www.digdir.no/datadeling/nasjonale-grunndata/7575).
Sida forklarer kva nasjonale grunndata er, kvifor det finst eit rammeverk for
dei, og peikar vidare til:

- [Rammeverk for Nasjonale grunndata](https://data.norge.no/specification/nasjonale-grunndata-rammeverk)
  (versjon 1.0, 15. oktober 2025) — organisering/roller (styrande organ,
  nasjonal grunndatakoordinator, grunndataforvaltar), kriterium og prinsipp
  for kva som kvalifiserer som nasjonale grunndata, og utviklingsfasar
  (behov → vurdering → rammer → forvaltning/drift)
- [Statusrapport 2025](https://www.digdir.no/7528)
- [Grunndataoversikten](https://informasjonsforvaltning.github.io/nasjonale-grunndata/) —
  verktøy for oversikt over datasamanhengar

Kjerneinnhaldet: fire felles offentlege register vert i dag rekna som
Nasjonale grunndata — **Enhetsregisteret**, **Folkeregisteret**,
**Kontakt- og reservasjonsregisteret (KRR)** og **Matrikkelen** — fordi dei
er autoritative kjelder som mange verksemder er avhengige av på tvers av
sektorar. Rammeverket etablerer «kun én gang»-prinsippet, kriterium for kva
som kan bli grunndata, og eit sett roller/prosessar for korleis dette skal
forvaltast nasjonalt.

Samanlikninga er gjort mot `src/linkml/ngr/` (NGR-domenet: `ngr-adresse`,
`ngr-eiendom`, `ngr-person`, `ngr-virksomhet`), `SCOPE.md`, `PRINCIPLES.md`,
`GOVERNANCE.md` og `README.md`.

## Samandrag

Digdir-sida og rammeverk-dokumentet er primært eit **styrings-/
organiseringsdokument** — roller (styrande organ, grunndatakoordinator,
grunndataforvaltar), kriterium for kva som kvalifiserer som grunndata, og
prosessfasar. Det stiller **ingen** konkrete tekniske krav til
skjemaformat, vokabular eller URI-struktur (ingen omtale av DCAT-AP-NO,
SKOS, LinkML e.l.) — det er eit forvaltningslag over dette repoet sitt
modelleringslag.

Repoet har alt eit fullverdig NGR-domene som dekkjer alle fire registera
rammeverket peikar på:

| Register (rammeverket) | Dekt av | Grunndataforvaltar (`utgiver`) |
|---|---|---|
| Enhetsregisteret | `ngr-virksomhet` | Brønnøysundregistrene (org. 974760673) ✓ |
| Folkeregisteret | `ngr-person` | Skatteetaten (org. 974761076) ✓ |
| Kontakt- og reservasjonsregisteret (KRR) | Klassane `ReservasjonMotKommunikasjonPaaNett` og `Kontaktopplysninger` i `ngr-person`, med kommentar «Forvaltast av Kontakt- og reservasjonsregisteret (KRR)» | — (embedda i person-modellen, korrekt merkt) |
| Matrikkelen | `ngr-eiendom` (eigedom/bygning) + `ngr-adresse` (adressekomponentar, del av Matrikkelen hos Kartverket) | Kartverket (org. 971040238) ✓ |

Alle fire NGR-skjema har alt `see_also`/manifest-lenkjer til
[Grunndataoversikten](https://informasjonsforvaltning.github.io/nasjonale-grunndata/)
(det tekniske datamodell-verktøyet rammeverket viser til), og `utgiver`-feltet
er korrekt sett til den faktiske grunndataforvaltaren for kvart register.
Konklusjonen er difor at **det meste av rammeverket er ikkje-gap** — det
gjeld eit forvaltningslag repoet ikkje sjølv er ein aktør i (repoet er
verken styrande organ, grunndatakoordinator eller grunndataforvaltar — det
er eit *modelleringsverktøy* som grunndataforvaltarar og andre kan bruke).
Det eine funnet er eit dokumentasjonsgap: NGR-domenet manglar ei
kryssreferanse til **kvifor** desse fire registera er valde ut (den
nasjonale definisjonen/visjonen), ikkje berre til det tekniske
datamodell-verktøyet.

## Identifiserte gap

### Gap 1: NGR-domenebeskrivinga manglar kryssreferanse til den nasjonale definisjonen av grunndata

`src/linkml/ngr/description.md` og NGR-radene i `README.md` peikar alt til
[Grunndataoversikten](https://informasjonsforvaltning.github.io/nasjonale-grunndata/)
(det tekniske datamodell-verktøyet), men ikkje til Digdir-sida som forklarer
**kva** nasjonale grunndata er og **kvifor** akkurat desse fire registera
har den statusen (kun-éin-gang-prinsippet, autoritativ kjelde-kriteria). Ein
lesar som opnar NGR-domenesida i den publiserte dokumentasjonsportalen får
dermed teknisk kontekst, men ikkje den nasjonale grunngjevinga.

**Forslag:** Legg til éi kort setning med lenkje til
[digdir.no/datadeling/nasjonale-grunndata](https://www.digdir.no/datadeling/nasjonale-grunndata/7575)
i `src/linkml/ngr/description.md`, som forklarar at dei fire modellane
svarar til dei fire registera rammeverket for Nasjonale grunndata peikar på.

## Ikkje-gap (vurdert, men ingen tiltak)

- **Organisering/roller (styrande organ, nasjonal grunndatakoordinator,
  grunndataforvaltar):** Reint forvaltningslag. Repoet er sjølv ikkje ein
  aktør i denne rollemodellen — det er eit verktøy grunndataforvaltarar
  *kan* bruke til å modellere skjemaa sine, jf. `SCOPE.md` sin tabell «Kva
  repoet IKKJE er» (ikkje ein kjeldesystem for produksjonsdata, ikkje ein
  integrasjonsplattform).
- **Kriterium og prinsipp for kva som kvalifiserer som grunndata
  («kun éin gang», autoritativ kjelde, verdi på tvers av sektorar):**
  Kriteria brukast av grunndatakoordinator/-forvaltar til å *avgjere* kva
  som får status som nasjonale grunndata — eit steg før modellering. Repoet
  har alt implementert resultatet av denne vurderinga (dei fire registera
  som NGR-domenemodellar) og treng ikkje duplisere sjølve
  kvalifiseringskriteria.
- **Utviklingsfasane (behov → vurder effekt → beslutt rammer → løpande
  forvaltning):** Prosessrammeverk for korleis *nye* grunndata-kandidatar
  vert vurderte nasjonalt — ikkje eit krav til korleis eksisterande grunndata
  skal *modellerast* i LinkML. Utanfor repoet sitt virkeområde.
- **FAIR-prinsippa** (nemnt i rammeverket som ei anbefaling til
  etterlevelse for datadeling): Repoet har alt ein eigen `fair-metadata`-modell
  (`src/linkml/fair/`) for FAIR-konform **datasett**-metadata (utfyller
  DCAT-AP-NO). NGR-domenet modellerer *entitetar* (Person, Eigedom,
  Verksemd), ikkje datasett — `fair-metadata` er difor ikkje relevant å
  importere her, konsistent med korleis modellen alt er avgrensa i
  `PRINCIPLES.md`.
- **Statusrapport 2025** (`digdir.no/7528`): Historisk statusdokument utan
  konkrete krav — ingen tiltak.
- **Kontakt- og reservasjonsregisteret som eige register:** Alt dekt som
  embedda klassar i `ngr-person` (`ReservasjonMotKommunikasjonPaaNett`,
  `Kontaktopplysninger`) med eksplisitt kommentar om at dei er forvalta av
  KRR. Ikkje behov for eigen `ngr-krr`-modell sidan KRR-data i praksis er
  ein del av persondomenet (kontaktinformasjon knytt til
  folkeregisteridentifikator).

## Handlingsliste

- [x] Legg til kryssreferanse til
      [digdir.no/datadeling/nasjonale-grunndata](https://www.digdir.no/datadeling/nasjonale-grunndata/7575)
      i `src/linkml/ngr/description.md` (Gap 1)

## Utført

- `src/linkml/ngr/description.md`: lagt til ei setning som koplar dei fire
  NGR-domenemodellane til dei fire registera som Digdir sitt
  [Rammeverk for Nasjonale grunndata](https://www.digdir.no/datadeling/nasjonale-grunndata/7575)
  definerer som nasjonale grunndata
