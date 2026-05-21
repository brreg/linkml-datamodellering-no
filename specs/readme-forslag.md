# Forslag: forkorta README.md

## Kva er problemet

Noverande README er 389 linjer og 100 tabellerader. Den har fire typar repetisjon:

1. **Føresetnadar nemnde to gongar** — i "Kom i gang" og i "Krav"-seksjonen.
2. **Same skjemaoversikt i tre tabellar** — ein kort AP-NO-tabell, ein kort domene-tabell og ei full skjemaliste. Ein ny lesar veit ikkje kva han skal lese.
3. **Importhierarki kopiert frå CLAUDE.md** — vert utdatert kvar gong eitt av dei vert oppdatert.
4. **Policy-beskriving to gongar** — som tabell midt i teksten og som fritekst heilt sist.

I tillegg er det utdatert innhald (`json2linkml-*`-kommandoar, `mcp-json2linkml/`-sti, policynamn `default`/`ap-no-catalog`).

## Kva bør skje med innhaldet

| Innhald | No | Forslag |
|---|---|---|
| Føresetnadar | README (2×) | README (1×) |
| Skjemaoversikt | README (3 tabellar) | README (1 tabell) |
| Typisk arbeidsflyt | README | README (kortare) |
| Alle make-kommandoar | README | `docs/kommandoar.md` |
| MCP-server-internalar | README | `docs/kommandoar.md` |
| Katalogstruktur | README | `docs/struktur.md` |
| Importhierarki | README + CLAUDE.md | Berre CLAUDE.md |
| Domene-beskriving | README (lang) | README (ei linje per domene) |
| Policyar | README (2×) | Berre i `docs/kommandoar.md` |

---

## Foreslått README.md

```markdown
# linkml-datamodellering-no

Norske W3C-applikasjonsprofiler og domenemodeller i [LinkML-format](https://linkml.io/).

## Kom i gang

**Føresetnadar:** [Podman](https://podman.io/), WSL2 og GNU make.

```bash
# Scaffold ein ny modell
make new-model NAME=mitt-register DOMAIN=oreg

# Valider eit skjema
make mcp-validate SCHEMA=src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml POLICY=bronze

# Generer alle artefaktar for eit domene, publiser og start dev-server
make oreg && make publish && make docs-serve   # → http://localhost:8000
```

Nye skjema under `src/linkml/<domene>/<namn>/` vert oppdaga automatisk.

Sjå [CLAUDE.md](CLAUDE.md) for modelleringsprinsipp og [docs/kommandoar.md](docs/kommandoar.md) for alle tilgjengelege kommandoar.

## Skjema

| Domene | Skjema | Beskriving |
|---|---|---|
| ap-no | [common-ap-no](src/linkml/ap-no/common/) | Felles slot-definisjonar for alle AP-NO-profiler |
| ap-no | [cpsv-ap-no](src/linkml/ap-no/cpsv-ap-no/) | Offentlege tenester og hendingar |
| ap-no | [dcat-ap-no](src/linkml/ap-no/dcat-ap-no/) | Datakatalogar og datasett |
| ap-no | [dqv-ap-no](src/linkml/ap-no/dqv-ap-no/) | Datakvalitet |
| ap-no | [modelldcat-ap-no](src/linkml/ap-no/modelldcat-ap-no/) | Informasjonsmodellar |
| ap-no | [skos-ap-no](src/linkml/ap-no/skos-ap-no/) | Begrepssamlingar |
| ap-no | [xkos-ap-no](src/linkml/ap-no/xkos-ap-no/) | Utvidet klassifikasjon |
| fair | [fair-metadata](src/linkml/fair/fair-metadata/) | FAIR-metadataoverbygning (F/A/I/R-prinsippa) |
| fint | [fint-common](src/linkml/fint/fint-common/) | Felles abstrakte klassar for FINT |
| fint | [fint-administrasjon](src/linkml/fint/fint-administrasjon/) | Lønn, arbeidsforhold, organisasjon |
| fint | [fint-arkiv](src/linkml/fint/fint-arkiv/) | Sak, journal, dokument |
| fint | [fint-okonomi](src/linkml/fint/fint-okonomi/) | Økonomi og rekneskap |
| fint | [fint-personvern](src/linkml/fint/fint-personvern/) | Personvernmeldingar |
| fint | [fint-ressurs](src/linkml/fint/fint-ressurs/) | Ressursar |
| fint | [fint-utdanning](src/linkml/fint/fint-utdanning/) | Utdanning og skole |
| ngr | [ngr-eiendom](src/linkml/ngr/ngr-eiendom/) | Fast eiendom, matrikkelenhet og bygning |
| ngr | [ngr-person](src/linkml/ngr/ngr-person/) | Person, identifikasjon og familierelasjonar |
| ngr | [ngr-virksomhet](src/linkml/ngr/ngr-virksomhet/) | Verksemder, roller og organisasjonsstruktur |
| oreg | [register-over-aksjeeiere](src/linkml/oreg/register-over-aksjeeiere/) | Aksjeeigarar og eigendelar |
| samt | [samt-bu](src/linkml/samt/samt-bu/) | Skolar og barnehagar |

AP-NO-profilane og FAIR-metadata er bibliotek utan eigen `tree_root` — dei er meint å importerast av domenemodeller.

```

---

## Kva fell ut av README

Følgjande seksjonar er for detaljerte for ei oversikts-README og bør ligge i `docs/kommandoar.md`:

- Alle make-targets (den lange tabellen med `gen-jsonld`, `gen-shacl` osv.)
- `make publish`-internalar (6-punktslista om kva publish.sh gjer)
- Rått `podman run`-eksempel for lint
- MCP-validator-detaljar (smoke-test, flatten-and-validate, JSON-RPC-døme)
- `mcp-linkml-generator`-kommandoar
- Katalogstruktur-tre (eige dokument: `docs/struktur.md`)
- Arkitekturprinsipp / importhierarki (berre i CLAUDE.md)
- Policy-beskriving (berre i `docs/kommandoar.md`)

`docs/kommandoar.md` bør alltid vere den autoritative kjelda for kommandoar slik at README ikkje treng oppdaterast kvar gong eit make-target vert endra.
```
