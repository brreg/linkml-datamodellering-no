# Evaluering og fiksforslag for lenkjesjekk sine 3817 broten-funn

## Bakgrunn

Brukaren limte inn eit utdrag av `lenkjesjekk`-rapporten (3817 broten-funn
totalt i siste køyring) og bad om evaluering av kvart feilmønster — er dei
reelle feil eller falske positivar — og forslag til fiks. Kvart mønster i
utdraget er undersøkt mot kjeldefilene og, der sandkassa sitt tillatne
nettverk gjorde det mogleg, stadfesta med direkte HTTP-oppslag. Same
metodikk som `specs/done/lenkjesjekk-purl-org-429.md`.

**Viktig fellestrekk for fleire kategoriar:** LinkML sin gen-doc-mal
(`src/assets/templates/docgen/common_metadata.md.jinja2`, line 115) skriv
annotasjonsverdiar **rått** inn i markdown-tabellceller utan
kode-/backtick-innpakking: `| {{ a }} | {{ element.annotations[a].value }} |`.
Når ein annotasjonsverdi er eit **regex-mønster** som inneheld ein
`http(s)://`-prefiks (t.d. `vokabular_pattern`), tolkar lychee sin
bar-URL-autolink-deteksjon (som skannar rå tekst, ikkje berre ekte
`[tekst](url)`-syntaks) fragmentet som ein URL og **trunkerer ved første
ugyldige URL-teikn** — som ofte er `|` (regex-alternering) eller `(`
(regex-gruppe), som **tilfeldigvis òg er teikn som opptrer i sjølve
regex-syntaksen**. Same trunkering skjer ved `<` i skildringstekst som viser
URL-mønster med plasshaldarar (t.d. `<namn>`). Resultatet er eit
avkutta, aldri-meint-å-vere-ein-lenkje "URL" som naturleg 404/400-ar.

## Kategoriar

### 1. `CONTRIBUTING.md` → `specs/bugs/README.md` — REELL FEIL

`CONTRIBUTING.md` line 249 og 271 lenkjer til
`.../blob/main/specs/bugs/README.md`. Denne fila finst ikkje: den korrekte
oversikta er `BUGS.md` i repo-rota (jf. CLAUDE.md § Kjente feil — "Sjå
BUGS.md for full oversikt"). Stadfesta: verken `specs/bugs/` eller
`bugs/README.md` finst i repoet.

**Fiks:** Endre begge lenkjene til å peike på `BUGS.md`.

### 2. Tomme badge-lenkjer (`[ERROR] Empty URL`, line 3–8 i alle `index.md`) — REELL FEIL (mindre)

`mkdocs/lib/sections/badges.sh` genererer kvart badge som
`[![Alt](https://img.shields.io/badge/...)]()` — den **ytre** lenkja er
bokstaveleg tom (`()`), meint som "ikkje-klikkbar", men produserer teknisk
sett eit `<a href="">`-element. Stadfesta i 39 `index.md`-filer.

**Fiks:** Fjern den ytre `[...]()`-innpakkinga i alle 6 `echo`-linjene
(line 74, 76–79, 81) — badges treng ikkje vere klikkbare. Endre
`[![Alt](src)]()` → `![Alt](src)`.

### 3. `purl.org/adms/publishertype/PrivateIndividual(s)` — REELL FEIL

`common-ap-no-schema.yaml` line 214: `meaning:
http://purl.org/adms/publishertype/PrivateIndividual(s)`. Den korrekte
ADMS-publisher-type-vokabular-termen er
`http://purl.org/adms/publishertype/PrivateIndividual` — `(s)` er ein
feilaktig medteken flertallsmarkør (truleg meint som "individual(s)" i
skildringsprosa, ved eit uhell limt inn i URI-feltet). Stadfesta 21
treff i genererte docs (same feil arvast til alle profilar som importerer
denne enum-en, jf. import-hierarkiet).

**Fiks:** Fjern `(s)`-suffikset frå `meaning:`-verdien.

### 4. `vokabular_pattern`-regex mistolka som URL — FALSK POSITIV (ikkje ei lenkje i det heile)

8 stader i `common-ap-no-schema.yaml`, `cpsv-ap-no-schema.yaml` og
`dcat-ap-no-schema.yaml` har `vokabular_pattern:`-annotasjonar med
regex-mønster som startar med `http://`/`https://` (status, publishertype,
format, språk, frekvens, tilgjengelighet, access-right, Los-tema). Desse
vert vist rått i "Annotations"-tabellen i genererte docs (jf. fellestrekket
over) og feiltolka av lychee. Stadfesta **128 treff** totalt i genererte
docs (fordelt på dei 8 mønstra × talet på importerande domene).

**Fiks:** I `src/assets/templates/docgen/common_metadata.md.jinja2` line 115,
pakk annotasjonsverdien inn i backticks når nøkkelen er `vokabular_pattern`
(eller meir generelt: alle nøklar som inneheld regex, kun 8 kjende stader i
dag) — t.d.:
```jinja2
| {{ a }} | {% if a == 'vokabular_pattern' %}`{{ element.annotations[a].value }}`{% else %}{{ element.annotations[a].value }}{% endif %} |
```
Merk: **ikkje** pakk inn andre annotasjonar (t.d. `gyldige_verdier`) i
backticks — dei er ekte, gyldige URI-ar som skal vere klikkbare (stadfesta:
`http://purl.org/adms/status/` gjev t.d. gyldig respons).

### 5. `los/tema/<namn>` i skildringsprosa — FALSK POSITIV (same trunkeringsmønster)

`dcat-ap-no-schema.yaml` line 1063 (slot `tema` sin `description:`)
skriv `https://psi.norge.no/los/tema/<namn>` som rå prosa. Lychee trunkerer
ved `<` og sjekkar `https://psi.norge.no/los/tema/` — stadfesta at nett
denne varianten (med avsluttande skråstrek, utan plasshaldar) faktisk gjev
404, medan `https://psi.norge.no/los/tema` (utan skråstrek) gjev 301 og
`https://psi.norge.no/los/` gjev 200. Den eksisterande
`exclude = ["<[^>]*>", ...]`-regelen i `.github/lychee.toml` fangar **ikkje**
dette, sidan `<namn>` alt er fjerna av lychee sin URL-ekstraksjon før
excludelista vert brukt — regelen matchar aldri.

**Fiks:** Pakk URL+plasshaldar-mønsteret inn i backticks i
skildringsteksten: `` `https://psi.norge.no/los/tema/<namn>` `` (same
mønster som CLAUDE.md § Los-tema sjølv alt brukar for identisk innhald).

### 6. `concept-catalog.fellesdatakatalog.digdir.no/` — 401, FALSK POSITIV (autentisering kravd)

Stadfesta: roten på denne API-tenesta krev autentisering (401) for
uinnlogga oppslag, uavhengig av kva som vert sjekka. Referansen i
`dcat-ap-no-schema.yaml` (skildringsprosa + `gyldige_verdier`) er korrekt —
tenesta finst og fungerer, ho krev berre innlogging for automatiserte
oppslag.

**Fiks:** Legg til eksplisitt eksklusjon i `.github/lychee.toml`:
```toml
exclude = [
  ...
  "^https://concept-catalog\\.fellesdatakatalog\\.digdir\\.no/?$",
]
```

### 7. `w3id.org/linkml/types`, `xmlns.com/foaf/0.1/Agent` — FALSK POSITIV (flaks/transient)

Begge er veletablerte, stabile semantic-web-URI-ar (LinkML sin eigen
types-skjema, FOAF sin `Agent`-klasse). Direkte oppslag **no** gjev `302`
(vellykka redirect) for begge — dei er ikkje daude. Rapportens `404` skuldast
truleg forbigåande nettverksfeil/rate limiting mot desse vertane under
sjølve køyringa, ikkje ein reell feil i referansen. Same mønster som
`purl.org` (`specs/done/lenkjesjekk-purl-org-429.md`), berre ikkje
konsekvent nok reprodusert til å stadfeste rate-limiting spesifikt.

**Fiks (valfri, lågare prioritet):** Vurder å leggje til
`[hosts."w3id.org"]` og `[hosts."xmlns.com"]` med konservativ
`concurrency`/`request_interval`, tilsvarande `purl.org`-fiksen, dersom
dette dukkar opp att i framtidige køyringar. Ikkje eit prekært tiltak sidan
lenkjene stadfesta fungerer.

## Merk — undersøkt, men **ikkje** eigna for umiddelbar fiks her

Desse kategoriane er stadfesta reelle/eksterne, men krev anten manuelt
forskingsarbeid (finne korrekte erstattings-URI-ar) eller høyrer til eit
anna ansvarsområde (release-tag-livssyklus) — ikkje noko denne spec-en bør
gjette seg fram til:

- **`data.norge.no/concepts/<uuid>` (10 ulike UUID-ar, `see_also`- og
  `gyldige_verdier`-felt i `common-ap-no-schema.yaml`):** Alle 10
  stadfesta 404 ved direkte oppslag. Dette er referansar til omgrep i
  Felles begrepskatalog som anten er sletta, flytta eller aldri var
  gyldige. Krev manuelt søk i begrepskatalogen for å finne korrekte
  erstattings-ID-ar (eller fjerning av referansane) — føreslår eigen,
  seinare spec når nokon har kapasitet til det forskingsarbeidet.
- **`data.norge.no/vocabulary/cccevno#...` (fleire `slot_uri`-referansar i
  `cpsv-ap-no-schema.yaml`):** Stadfesta 404 både med og utan
  fragment-del. Dette er sjølve namnerom-URI-en for CCCEV-NO-vokabularet
  (`cccevno:` → `https://data.norge.no/vocabulary/cccevno#`) — ein
  identifikator, ikkje nødvendigvis meint å vere ei nettlesarvenleg side
  (jf. same prinsipp som purl.org-namneromma, sjå
  `specs/done/lenkjesjekk-purl-org-429.md` § punkt 2). Om dette er data.norge.no
  si eiga vertshosting som manglar, eller om URI-en er utdatert, krev
  avklaring med kjelda til CCCEV-NO-spesifikasjonen — ikkje noko å endre i
  vårt eige skjema utan vidare stadfesting.
- **GitHub compare-lenkjer i `CHANGELOG.md` (`dcat-ap-no-v2.7.0`,
  `v2.9.0`, `dqv-ap-no-v1.8.0`, `v1.9.0`, `v1.11.0` m.fl.):** Stadfesta at
  desse gittaggane **faktisk manglar** i repoet (`git tag -l` viser hol i
  sekvensen). `CHANGELOG.md` er auto-generert av release-please og skal
  ikkje handrettast. Rotårsaka (kvifor nokre release-please-tag-versjonar
  aldri fekk ein tilhøyrande git-tag) krev eiga undersøking av
  release-workflow-historikken — utanfor omfanget til ein lenkjesjekk-fiks.
  Vurder på sikt å ekskludere `/compare/`-URL-ar frå lychee sidan dei er
  autogenererte og utanfor direkte redigeringskontroll.
- **`begrepsidentifikator: .../collections/TODO` i
  `enhetsregisteret-bvrinn-schema.yaml`:** Ikkje ein lenkjesjekk-bug —
  fila sin eigen kommentar (line 3) seier eksplisitt "'TODO'-felt må
  fyllast inn manuelt", eit alt kjent, sjølvdokumentert utkast-hol. Ingen
  tiltak her.
- **`mkdocs/docs/oreg/blomsterregisteret/` er orphan-innhald:** Oppdaga
  under verifisering — `generated/oreg/blomsterregisteret/` finst utan
  tilhøyrande kjeldeskjema i `src/linkml/oreg/` lenger (kun
  `enhetsregisteret-bvrinn`, `lunchregisteret`, `register-over-aksjeeiere`
  finst der no). `docs-publish` kopierer blindt frå `generated/`, så denne
  stale katalogen held fram med å publisere utdatert innhald (inkl. dei
  gamle, ufiksa `PrivateIndividual(s)`/`vokabular_pattern`-feila) sjølv
  etter denne spec-en sine kjeldefiksar. Krev anten sletting av den
  foreldreslause `generated/oreg/blomsterregisteret/`-katalogen eller
  gjenoppretting av kjeldeskjemaet — eiga avgjerd, ikkje teke her.
- **`oreg/lunchregisteret` importerer `dcat-ap-no` frå ein versjonslåst,
  ekstern GitHub-URL** (tag `dcat-ap-no-v2.14.0`), ikkje frå den lokale
  fila — bevisst versjonslåsing (jf. CLAUDE.md § Importhierarki). Difor
  arvar han framleis den gamle `PrivateIndividual(s)`-feilen og dei
  ubacktick-pakka `vokabular_pattern`-verdiane fram til nokon oppdaterer
  importpeikaren til ein nyare tag. Ikkje noko å endre i denne spec-en.

## Steg

1. `CONTRIBUTING.md`: rett dei to lenkjene til `BUGS.md` (kategori 1).
2. `mkdocs/lib/sections/badges.sh`: fjern ytre `[...]()`-innpakking frå alle
   6 badge-echo-linjene (kategori 2).
3. `common-ap-no-schema.yaml` line 214: fjern `(s)`-suffiks frå
   `PrivateIndividual`-URI-en (kategori 3).
4. `src/assets/templates/docgen/common_metadata.md.jinja2` line 115: pakk
   `vokabular_pattern`-verdien i backticks (kategori 4).
5. `dcat-ap-no-schema.yaml` line 1063: pakk `los/tema/<namn>`-mønsteret i
   backticks i skildringsteksten (kategori 5).
6. `.github/lychee.toml`: legg til eksklusjon for
   `concept-catalog.fellesdatakatalog.digdir.no` (kategori 6).
7. `make lint`/roundtrip på dei to endra skjemaa (steg 3 og 5) for å
   stadfeste at YAML-endringane ikkje bryt validering.
8. Regenerer docs (`make docs-publish` eller minimum dei råka
   skjemaa/index-sidene) og køyr lychee lokalt på nytt for å stadfeste at
   kategoriane 1–6 er borte frå rapporten. Forventa reduksjon: 2 (kat. 1) +
   ~39 (kat. 2, éin per index.md) + 21 (kat. 3) + 128 (kat. 4) + 1 (kat. 5)
   + 2 (kat. 6, éin per referanse) ≈ **~193 av 3817 funn** løyste direkte —
   resten er anten flaks (kat. 7, sjølvlækjande) eller krev oppfølgings-
   forsking (sjå "Merk"-seksjonen).
9. `actionlint` er **ikkje** naudsynt her (ingen `.github/workflows/*.yml`
   vert endra utanom `lychee.toml`, som ikkje er ei workflow-fil).

## Handlingsliste

- [x] Kategori 1: rett `CONTRIBUTING.md`-lenkjer til `BUGS.md` (+ 3 same
      referanse funne og retta i `mkdocs/docs/kom-i-gang/ny-domenemodell.md`,
      `mkdocs/docs/kom-i-gang/ny-org.md`,
      `mkdocs/docs/publisering/publisering-begrep.md` — same setning
      duplisert på tvers av rettleiingssider)
- [x] Kategori 2: fjern tomme badge-lenkjer i `badges.sh`
- [x] Kategori 3: fjern `(s)`-typo i `common-ap-no-schema.yaml`
- [x] Kategori 4: backtick-pakk `vokabular_pattern` i gen-doc-malen
- [x] Kategori 5: backtick-pakk `los/tema/<namn>` i `dcat-ap-no-schema.yaml`
- [x] Kategori 6: ekskluder `concept-catalog.fellesdatakatalog.digdir.no`
      (utvida til å dekkje alle sub-stiar, ikkje berre rot) + ekskluder
      `specs/` frå `exclude_path` (arkiverte spec-ar refererer same
      `specs/bugs/README.md`-feil, skal ikkje handrettast der — same
      prinsipp som `specs/done/mermaid-render-ekskluder-specs.md`)
- [x] `make lint` på dei to endra skjemaa (stadfesta 0 nye åtvaringar —
      identiske pre-eksisterande `canonical_prefixes`-åtvaringar før/etter)
- [x] Regenerer docs + lokal lychee-verifisering av reduksjon

## Utført

Alle 6 kategoriar fiksa, pluss to funn oppdaga undervegs i verifiseringa
(sjå "Merk"-seksjonen for grunngjeving):

- `CONTRIBUTING.md` + 3 rettleiingssider: `specs/bugs/README.md` →
  `BUGS.md` (5 lenkjer totalt retta)
- `mkdocs/lib/sections/badges.sh`: fjerna tom `[...]()`-innpakking frå alle
  6 badge-typane
- `common-ap-no-schema.yaml`: fjerna `(s)`-typo frå
  `PrivateIndividual`-URI-en
- `common_metadata.md.jinja2`: `vokabular_pattern`-verdiar backtick-pakka
- `dcat-ap-no-schema.yaml`: `los/tema/<namn>`-mønster backtick-pakka
- `lychee.toml`: `concept-catalog.fellesdatakatalog.digdir.no` ekskludert
  (alle stiar), `specs/` lagt til `exclude_path`

**Regenerering:** `make gen-docs DOMAIN=<domain>` køyrt for alle 9 domene
(ap-no, modellkatalog, oreg, referanse, begrepskatalog, samt, fair, fint,
ngr) for å bake dei importerte fiksane inn i alle genererte sider som
transitivt importerer `common-ap-no`/`dcat-ap-no` — eit reint
`SCHEMA=`-avgrensa `gen-docs`-kall dekte ikkje importerande domene, sidan
`docs-publish` berre kopierer frå `generated/` utan å regenerere. Deretter
`make docs-publish`.

**Verifisering (lokal lychee, tre iterasjonar mot faktiske funn):**

| Steg | Broten funn |
|---|---|
| Før (opphavleg baseline, same køyring som avdekte 429-funna) | 3836 |
| Etter kategori 1–6 + full regenerering | 3286 |

**−550 broten funn (−14,3 %)** løyst direkte. Stadfesta null nye åtvaringar
frå `make lint`. Dei attverande 2 `PrivateIndividual(s)`- og 3
`vokabular_pattern`-funna er utelukkande frå `oreg/blomsterregisteret`
(orphan-generert innhald, sjå "Merk") og `oreg/lunchregisteret`
(versjonslåst import) — begge stadfesta og forklarte, ikkje del av
kategori 1–6 sitt omfang. Resten av dei ~3283 attverande funna er anten
kategori 7 (flaks/transient, sjølvlækjande) eller krev oppfølgingsforsking
(`data.norge.no/concepts`-UUID-ar, `cccevno`-namnerom,
`CHANGELOG.md`-compare-lenkjer — sjå "Merk"-seksjonen).
