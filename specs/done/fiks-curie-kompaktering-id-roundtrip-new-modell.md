# Fiks CURIE-kompaktering av id-verdi ved TTL-roundtrip for scaffolda eksempel

## Bakgrunn

Under verifisering av `specs/done/fiks-ap-no-import-feil-new-modell.md` vart
`roundtrip-ttl (lunchregisteret)` stadfesta å feile — men med ei **anna,
tidlegare maskert** feilmelding enn CURIE-krasjen (BUG-15) den specen retta:

```
ROUNDTRIP-AVVIK (yaml→ttl→yaml→json):
Forventa: {'@type': 'LunchregisteretContainer',
 'lunchregistereter': [{'id': 'https://data.norge.no/oreg/lunchregisteret/eksempel-1'}]}
Fekk:     {'@type': 'LunchregisteretContainer',
 'lunchregistereter': [{'id': 'lunchregisteret:eksempel-1'}]}
```

`id`-verdien kjem attende som ein **kompaktert CURIE**
(`lunchregisteret:eksempel-1`) i staden for den opphavlege **fulle URI-en**
(`https://data.norge.no/oreg/lunchregisteret/eksempel-1`) etter
yaml→ttl→yaml→json-roundtrip.

## Rotårsak — stadfesta empirisk

Turtle-serialisering kompakterer alltid ein full URI til ein CURIE når URI-en
sitt namnerom matchar eit registrert skjema-prefiks (standard,
deterministisk rdflib/LinkML-åtferd). `rdflib_loader` re-ekspanderer
derimot **ikkje** ein slik kompaktert CURIE tilbake til den fulle URI-strengen
når han les TTL-en attende for eit `range: uriorcurie`-slot med
`identifier: true` — verdien blir verande som den kompakterte CURIE-strengen.

Dette slår berre inn når identifikator-**verdien** sitt namnerom **nøyaktig
matchar** eit av skjemaet sine eigne registrerte prefiks. Stadfesta ved
samanlikning av tre `oreg`-skjema:

| Skjema | Id-verdiform i eksempelet | Eige namnerom? | Roundtrip-ttl |
|---|---|---|---|
| `lunchregisteret` | Full URI: `https://data.norge.no/oreg/lunchregisteret/eksempel-1` | **Ja** (matchar `default_prefix`) | **FEIL** |
| `register-over-aksjeeiere` | CURIE alt frå kjelda: `aksje:Aksjeselskap1` | Ja, men alt CURIE | OK |
| `enhetsregisteret-bvrinn` | Full URI: `https://example.org/innrapportering/1` | Nei (framand plassholder-namnerom) | OK |

Berre `lunchregisteret` er ramma, fordi det er det einaste skjemaet med ein
id-verdi som **både** er skriven som full URI **og** ligg i skjemaet sitt
eige namnerom — akkurat mønsteret `new-modell.sh` sin scaffolda
eksempelfil-heredoc alltid produserer:

```bash
# new-modell.sh
cat > "$EXAMPLE_FILE" << EOF
---
$CONTAINER_SLOT:
  - id: $SCHEMA_ID/eksempel-1
EOF
```

`$SCHEMA_ID` er per konstruksjon alltid same URI som dannar grunnlaget for
skjemaet sitt eige `default_prefix` — så **kvar einaste** `make new-modell`-
scaffolda modell vil ha denne roundtrip-ttl-feilen frå fødselen av, uansett
domene.

**Stadfesta fiks:** å endre eksempelet sin id-verdi til CURIE-form
(`id: lunchregisteret:eksempel-1`, matchar mønsteret
`register-over-aksjeeiere` alt brukar) gjer at BÅDE `roundtrip-json` OG
`roundtrip-ttl` passerer reint — verifisert direkte ved mellombels
redigering av den scaffolda `lunchregisteret-eksempel.yaml` og køyring av
`TEST_FILTER=roundtrip bash tests/test_make.sh <schema>` (endringa vart
reversert etter verifisering, ikkje behalden).

## Tiltak

| # | Tiltak | Fil |
|---|---|---|
| 1 | Endre `EXAMPLE_FILE`-heredocen i `new-modell.sh` frå `id: $SCHEMA_ID/eksempel-1` til CURIE-form basert på skjemaet sitt eige namnprefiks (t.d. `id: ${SCHEMA_NAME}:eksempel-1`, matchar `prefix_name`-konvensjonen alt brukt i `converter.py`) | `src/assets/scripts/scaffolding/new-modell.sh` |
| 2 | Oppdater den ikkje-committa `src/linkml/oreg/lunchregisteret/examples/lunchregisteret-eksempel.yaml` tilsvarande | `src/linkml/oreg/lunchregisteret/examples/lunchregisteret-eksempel.yaml` |
| 3 | Opprett `bugs/curie-id-ikkje-reekspandert-ttl-roundtrip.md` som **BUG-18** — dokumenter den underliggande `rdflib_loader`-avgrensinga (kompaktert CURIE vert ikkje re-ekspandert til full URI for `uriorcurie`-identifikatorar), sidan avgrensinga i prinsippet framleis kan ramme **handskrivne** eksempel som uavhengig vel ein id-verdi i eige namnerom — ikkje berre scaffolda modellar. Status `workaround` (unngå mønsteret i scaffolding, jf. tiltak 1) | `bugs/curie-id-ikkje-reekspandert-ttl-roundtrip.md` |
| 4 | Legg BUG-18 til i `BUGS.md` sin indekstabell | `BUGS.md` |
| 5 | Oppdater `mkdocs/docs/kom-i-gang/ny-domenemodell.md` sitt dokumenterte eksempel-oppsett dersom det viser same `id: <full-URI>`-mønster, til CURIE-form | `mkdocs/docs/kom-i-gang/ny-domenemodell.md` |
| 6 | Verifiser: `make roundtrip SCHEMA=src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml` — både `roundtrip-json` og `roundtrip-ttl` skal passere | — |
| 7 | Verifiser: `bash -n src/assets/scripts/scaffolding/new-modell.sh` (syntakssjekk etter endring) | — |
| 8 | Verifiser ingen regresjon: køyr `make roundtrip` for eit par andre, uendra skjema (t.d. `register-over-aksjeeiere`, `enhetsregisteret-bvrinn`) | — |

## Referanse

- `bugs/langstring-rdflib-roundtrip.md` (BUG-1), `bugs/inlined-as-list-rdflib-roundtrip.md` (BUG-2), `bugs/mappingerror-rdflib-roundtrip.md` (BUG-3) — same familie av `rdflib_loader`-TTL-roundtrip-avgrensingar, same dokumentasjonsmønster BUG-18 skal følgje
- `specs/done/fiks-ap-no-import-feil-new-modell.md` — der dette funnet først vart observert (utanfor scope der)
- `src/assets/scripts/scaffolding/new-modell.sh` — kjelda til det scaffolda eksempelmønsteret

## Utført

Alle 8 tiltak gjennomførte:

1. `new-modell.sh` sin `EXAMPLE_FILE`-heredoc endra frå `id: $SCHEMA_ID/eksempel-1` til `id: ${SCHEMA_NAME}:eksempel-1` (CURIE-form).
2. Den ikkje-committa `lunchregisteret-eksempel.yaml` retta tilsvarande (`id: lunchregisteret:eksempel-1`).
3. `bugs/curie-id-ikkje-reekspandert-ttl-roundtrip.md` oppretta som **BUG-18**.
4. BUG-18 lagt til i `BUGS.md` sin indekstabell.
5. `mkdocs/docs/kom-i-gang/ny-domenemodell.md` sitt dokumenterte eksempel (`examples/tilskudd-eksempel.yaml`-visinga) endra til CURIE-form (`id: tilskudd:eksempel-1`), matchar `class_uri: tilskudd:tilskudd`-mønsteret alt vist same stad.
6. Verifisert: `make roundtrip SCHEMA=.../lunchregisteret-schema.yaml` — både `roundtrip-json` og `roundtrip-ttl` passerer no.
7. `bash -n new-modell.sh` — syntaks OK.
8. Ingen regresjon: `register-over-aksjeeiere` sin roundtrip framleis grøn. `enhetsregisteret-bvrinn` sin roundtrip-ttl feilar framleis, men **uendra** — det er BUG-19 (datetime-separator, handtert i eiga spec `fiks-datetime-separator-roundtrip-enhetsregisteret-bvrinn.md`), ikkje ramma av denne fiksen.
