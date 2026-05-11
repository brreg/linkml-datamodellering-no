# Plan: Testar for alle make-targets

## Prinsipp

- Testar køyrer mot **reelle skjema** — ingen dedikert test-fixture
- For skjema utan eigen containerklasse (AP-NO, FAIR): bruk eksisterande fixtures frå `tests/fixtures/`
- Strukturert som `tests/test_make.sh` — konsistent med `tests/test_schemas.sh`
- Kvar test er ein funksjon: køyrer kommando, sjekkar output, rapporterer pass/fail med farge
- Cleanup via `trap` — ryddar opp genererte testfiler etter køyring
- Full output frå alle kommandoar vert skriven til `tests/test_make.log` — terminalen viser berre fargelagd pass/fail-samandrag

---

## Skjemaval

Testane brukar desse skjemaa, valde for å vere representative og raske:

| Skjema | Brukt i | Grunn |
|---|---|---|
| `src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml` | Dei fleste testar | Sjølvstendig (berre `linkml:types`), har `tree_root`, medium storleik |
| `src/linkml/fint/fint-personvern/fint-personvern-schema.yaml` | `gen-shacl`, `gen-owl` (FINT-variant) | Minste FINT-skjema, utøver `--exclude-imports`-stien |
| `tests/fixtures/dcat-ap-no-fixture.yaml` | Ikkje brukt direkte i make-testar (dekka av `test_schemas.sh`) | AP-NO har ikkje tree_root |
| `tests/fixtures/fair-metadata-fixture.yaml` | Ikkje brukt direkte i make-testar (dekka av `test_schemas.sh`) | FAIR har ikkje tree_root |

Generator-testane brukar `SCHEMAS`-override på kommandolinja:
```bash
make gen-shacl SCHEMAS=src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml
```

---

## Testar per target

| Test | Kommando | Output-fil | Syntaxsjekk |
|---|---|---|---|
| `validate` | `make validate SCHEMAS=ngr-adresse` | — | exit 0 |
| `gen-jsonld` | `make gen-jsonld SCHEMAS=ngr-adresse` | `ngr-adresse-context.jsonld` | `python3 -m json.tool` + `@context`-nøkkel finst |
| `gen-shacl` | `make gen-shacl SCHEMAS=ngr-adresse` | `ngr-adresse-shapes.ttl` | `rdflib.Graph().parse()` + > 0 tripler |
| `gen-shacl (fint)` | `make gen-shacl SCHEMAS=fint-personvern` | `fint-personvern-shapes.ttl` | `rdflib.Graph().parse()` + > 0 tripler |
| `gen-python` | `make gen-python SCHEMAS=ngr-adresse` | `ngr-adresse-model.py` | `python3 -m py_compile` |
| `gen-jsonschema` | `make gen-jsonschema SCHEMAS=ngr-adresse` | `ngr-adresse-schema.json` | `python3 -m json.tool` + `$defs`/`properties` finst |
| `gen-owl` | `make gen-owl SCHEMAS=ngr-adresse` | `ngr-adresse-ontology.ttl` | `rdflib.Graph().parse()` + > 0 tripler |
| `gen-owl (fint)` | `make gen-owl SCHEMAS=fint-personvern` | `fint-personvern-ontology.ttl` | `rdflib.Graph().parse()` + > 0 tripler |
| `gen-rdf` | `make gen-rdf SCHEMAS=ngr-adresse` | `ngr-adresse-schema.ttl` | `rdflib.Graph().parse()` + > 0 tripler |
| `gen-erdiagram` | `make gen-erdiagram SCHEMAS=ngr-adresse` | `ngr-adresse-erdiagram.md` | inneheld ` ```mermaid` + `erDiagram` |
| `gen-docs` | `make gen-docs SCHEMAS=ngr-adresse` | `docs/*.md` | inneheld `#`-overskrift, ikkje tom |
| `convert-rdf` | direkte podman-kall for `ngr-adresse-eksempel.yaml` | `ngr-adresse-eksempel.ttl` | `rdflib.Graph().parse()` + > 0 tripler |
| `publish` | `make publish` (etter generator-testar) | `mkdocs/docs/ngr/ngr-adresse/index.md` | finst + inneheld `#`-overskrift |
| `clean` | `make clean` | `generated/` | katalog er sletta |

---

## Utelate

| Target | Grunn |
|---|---|
| `docs-serve` | Interaktiv, kan ikkje automatiserast |
| `docs-build` / `docs-build-fast` | Deployment-test, ikkje unit-test |
| `mcp-*` | Dekka av eksisterande `tests/test_mcp_server.py` |
| `make <domene>` (fint, ngr, osv.) | For treige; dekka indirekte av generator-testane |

---

## Loggformat

Terminalen viser:
```
Test gen-shacl (ngr-adresse) ... OK
Test gen-shacl (fint-personvern) ... OK
Test gen-python (ngr-adresse) ... FEIL

Resultat: 11 OK, 1 feil
Sjå tests/test_make.log for detaljar
```

`tests/test_make.log` inneheld full output frå alle kommandoar med tidsstempel og separator per test.

---

## Dependency: rdflib

Alle Turtle-sjekkar brukar `rdflib` inne i `localhost/linkml-local:latest`-containeren (som installerer rdflib i `src/assets/containers/Dockerfile.linkml`). Ingen lokale Python-dependencies nødvendig.

---

## Integrasjon

Legg til kall til `tests/test_make.sh` i `make test`-target saman med eksisterande `tests/test_schemas.sh`.
