# Dokumenter/handter datetime-separator-avvik ved TTL-roundtrip (enhetsregisteret-bvrinn)

## Bakgrunn

Under verifisering av at det ikkje er ein reell race condition i
`tests/test_make.sh` (jf. `specs/done/fiks-ap-no-import-feil-new-modell.md`
sitt tillegg om ein antatt Fase A/Fase B-race — sjå «Motbevist»-notatet under),
vart ein full, rein `make test`-køyring gjennomført to gonger for å skilje
sesjons-kontaminering frå reelle feil. Den reine køyringa (589 OK, 7 feil)
synte at `roundtrip-ttl (enhetsregisteret-bvrinn)` feilar konsekvent, og at
denne feilen er **uavhengig** av både BUG-15 (CURIE-krasj),
CURIE-kompaktering (jf.
`specs/backlog/fiks-curie-kompaktering-id-roundtrip-new-modell.md`) og
BUG-3 (`MappingError` for `fint-*`/`samt-bu`).

## Motbevist: ingen race condition i test_make.sh

Den opphavlege observasjonen (34 feil, mange urelaterte `roundtrip-json`/
`roundtrip-ttl`-feil for `fint-*`, `ngr-*`, `*-modellkatalog`, `samt-bu`,
`brreg-begrepskatalog`) vart **ikkje reprodusert** i ein reint isolert
køyring (ingen restar av tidlegare feilhandterte bakgrunnsprosessar frå
denne AI-økta). To reine `make test`-køyringar gav 589 OK / 7 feil — dei
resterande ~27 feila frå den fyrste, kontaminerte køyringa skuldast med
stor sannsyn overlappande, forlatne `make test`-prosessar frå denne økta
som delte den same `$REPO_ROOT/tmp`-katalogen (kvar med sin eigen
`trap cleanup EXIT` som køyrer `rm -rf $REPO_ROOT/tmp`), ikkje ein feil i
sjølve test-orkestreringa. Denne specen gjeld difor **berre** den attverande,
stadfesta reelle feilen: `roundtrip-ttl (enhetsregisteret-bvrinn)`.

## Reprodusert og isolert

Dei fire TTL-roundtrip-stega vart køyrde manuelt (utanom `test_make.sh`) med
mellomresultat bevart for inspeksjon:

| Steg | Fil | Verdi for `innsendingstidspunkt` |
|---|---|---|
| 1. `eksempel.yaml → a.json` | `a.json` | `"2026-07-04T10:30:00"` |
| 2. `eksempel.yaml → b.ttl` | `b.ttl` | `"2026-07-04T10:30:00"^^xsd:dateTime` (korrekt) |
| 3. `b.ttl → c.yaml` | `c.yaml` | `'2026-07-04 10:30:00'` (**mellomrom** — avviket oppstår her) |
| 4. `c.yaml → d.json` | `d.json` | `"2026-07-04 10:30:00"` (arvar avviket) |

TTL-en sjølv er korrekt ISO 8601-formatert (`T`-separator). Avviket oppstår
i steg 3: `rdflib_loader` parsar `xsd:dateTime`-literalen til eit Python
`datetime.datetime`-objekt, og YAML-dumparen serialiserer det objektet med
Python sin standard `str(datetime_obj)`-representasjon (mellomrom-separert)
i staden for `.isoformat()` (T-separert) — ein formatteringsinkonsistens ved
rundtur gjennom eit `datetime`-objekt, i same familie som BUG-1
(`LangString` vert ikkje korrekt rekonstruert frå TTL).

## Berørte skjema

Stadfesta: `enhetsregisteret-bvrinn` (einaste skjema som når fram til denne
samanlikninga med eit populert `datetime`-felt i sitt roundtrip-testa
eksempel). Andre skjema med `range: datetime`-slots
(`fint-administrasjon`, `fint-okonomi`, `fint-personvern`, `fint-utdanning`)
krasjar tidlegare i pipelinen med BUG-3 sin `MappingError` — ukjent om dei
**òg** ville trigga denne feilen dersom BUG-3 vart løyst først.

## Tiltak

| # | Tiltak | Fil |
|---|---|---|
| 1 | Opprett `bugs/datetime-separator-rdflib-roundtrip.md` som **BUG-19** — dokumenter symptom, dei fire stega si rotårsaksanalyse, status `open` (ingen upstream-fiks venta, same kategori som BUG-1/2/3) | `bugs/datetime-separator-rdflib-roundtrip.md` |
| 2 | Legg BUG-19 til i `BUGS.md` sin indekstabell og under «Validering og testing»-seksjonen (utvid den eksisterande BUG-1/2/3-fellesnemninga) | `BUGS.md` |
| 3 | Legg til skip-betingelse for `enhetsregisteret-bvrinn` i `roundtrip_ttl_job()`/`test_roundtrip_ttl()` sin `case "$name"`-kjede i `tests/test_make.sh`, referert til BUG-19 — same mønster som BUG-1/BUG-2 sine eksisterande skip-betingelsar | `tests/test_make.sh` |
| 4 | Verifiser: `TEST_FILTER=roundtrip bash tests/test_make.sh src/linkml/oreg/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml` — skal no vise «Hoppar over roundtrip-ttl for enhetsregisteret-bvrinn (BUG-19: ...)» og returnere 0 |
| 5 | Verifiser: `bash -n tests/test_make.sh` (syntakssjekk etter endring) | — |

## Referanse

- `bugs/langstring-rdflib-roundtrip.md` (BUG-1) — same familie av `rdflib_loader`-rekonstruksjonsavgrensingar, same dokumentasjons- og skip-mønster BUG-19 skal følgje
- `bugs/mappingerror-rdflib-roundtrip.md` (BUG-3) — maskerer om `fint-*`-skjemaa òg er ramma av BUG-19
- `specs/done/fiks-ap-no-import-feil-new-modell.md` — der den opphavlege (feilaktige) race-condition-hypotesen vart notert
- `specs/done/fiks-curie-kompaktering-id-roundtrip-new-modell.md` — det parallelle, uavhengige `lunchregisteret`-funnet frå same verifiseringsrunde

## Utført

Alle 5 tiltak gjennomførte:

1. `bugs/datetime-separator-rdflib-roundtrip.md` oppretta som **BUG-19**.
2. BUG-19 lagt til i `BUGS.md` sin indekstabell og «Validering og testing»-seksjonen (utvida BUG-1/2/3-fellesnemninga til å inkludere BUG-19).
3. Skip-betingelse lagt til i `roundtrip_ttl_job()` (den faktiske gatingfunksjonen, brukt av både Fase A-jobblistebygging og Fase B) og tilhøyrande meldingsgrein i `test_roundtrip_ttl()`, begge referert til BUG-19.
4. Verifisert: `TEST_FILTER=roundtrip bash tests/test_make.sh .../enhetsregisteret-bvrinn-schema.yaml` — `roundtrip-ttl (enhetsregisteret-bvrinn)` hoppar no over og returnerer OK (Fase A køyrer heller ikkje lenger `roundtrip-ttl`-jobb for dette skjemaet).
5. `bash -n tests/test_make.sh` — syntaks OK.
