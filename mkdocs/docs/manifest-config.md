# Modellmanifest (manifest.yaml)

!!!note "Kva er `manifest.yaml`?"

    Kvar modell under `src/linkml/<domain>/<modell>/` har ei `manifest.yaml` som styrer kva artefaktar som vert genererte, kva flagg som vert brukte, og om modellen skal publiserast til ein ekstern katalog. `make new-model` oppretter fila automatisk med standardkonfigen.

## To typar manifest

### Skjema-manifest (har `generators:`-seksjon)

Ligg ved sida av skjemafila:

```
src/linkml/<domain>/<modell>/manifest.yaml
```

```yaml
publish_external: false          # true for å utløyse publisering til ekstern katalog
validation_policy: silver        # bronze / silver / gold / felles-datakatalog / felles-begrepskatalog
external_spec_url: https://informasjonsforvaltning.github.io/cpsv-ap-no/  # lenke til offisiell spesifikasjon


generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
  openapi: true
```

### Datafil-manifest (manglar `generators:`-seksjon)

Ligg inne i `data/<datafil-katalog>/`:

```
src/linkml/<domain>/<modell>/data/<datafil-katalog>/manifest.yaml
```

```yaml
publish_external: true
validation_policy: felles-begrepskatalog

concepts:                   # valfri — utelat for å publisere heile datafila
  - https://begrep.brreg.no/foretaksnavn
  - https://begrep.brreg.no/nestleder
```

CI skil dei to typane på om `generators:`-seksjonen er til stades.

## Felta i skjema-manifest

### `submodels` (valfritt)

Liste over delmodellar som høyrer til denne hovudmodellen. Delmodellane må ligge i same 
katalog som hovudmodellen sitt skjema (t.d. `src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml`).

Dokumentasjonsportalen (`make docs-publish`) vil:
- Vise delmodellane som innrykka undermenypunkt under hovudmodellen i nav-menyen
- Legg til "Delmodellar"-seksjon på hovudmodellen sin `index.md`
- Legg til "Delmodell av"-boks på kvar delmodell sin `index.md`

**Brukstilfelle:** Modellar som er splitta i fleire skjema for å handtere sirkulær import
(t.d. `dqv-core` importert av `dcat-ap-no`, `dqv-ap-no` importerer `dcat-ap-no`) eller
for å separere logiske komponentar (t.d. `modelldcat-modell` og `modelldcat-katalog`).

**Eksempel:**
```yaml
submodels:
  - dqv-core
```

**Eksempel (fleire delmodellar):**
```yaml
submodels:
  - modelldcat-modell
  - modelldcat-katalog
```

### `external_spec_url` (valfritt)

URL til offisiell spesifikasjon hos standardiseringsorganisasjon (t.d. Digdir). 
Dersom sett, vis ein infoboks i `index.md` med lenke til den eksterne spesifikasjonen.

**Brukstilfelle:** AP-NO-profilar som er baserte på Digdir-standardar (DCAT-AP-NO, 
SKOS-AP-NO osv.). Domenemodell-skjema har vanlegvis ikkje dette feltet.

**Eksempel:**
```yaml
external_spec_url: https://informasjonsforvaltning.github.io/dcat-ap-no/
```

### `external_spec_label` (valfritt)

Lenke-tekst for den offisielle spesifikasjonen. Dersom utelatt, vert skjemanamnet brukt.

**Brukstilfelle:** Gje ein deskriptiv tittel til lenka i "Offisiell referanse"-boksen
i staden for det korte skjemanamnet (t.d. "Spesifikasjon for tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO)"
i staden for "cpsv-ap-no").

**Eksempel:**
```yaml
external_spec_url: https://informasjonsforvaltning.github.io/cpsv-ap-no/
external_spec_label: "Spesifikasjon for tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO)"
```

### `publish_external`

`true` utløyser publisering til ekstern katalog (Felles Datakatalog eller Felles
Begrepskatalog) i CI. Standard: `false`.

### `validation_policy`

Peikar til valideringspolicyen som `make domain-validate-data` nyttar for datafiler
under `data/`. Gyldige verdiar:

| Verdi | Brukstilfelle |
|---|---|
| [`bronze`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md#bronse) | Minimumskrav — strukturelt korrekt LinkML |
| [`silver`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md#s%C3%B8lv) | Tilrådde felt er fylt ut |
| [`gold`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md#gull) | Alle felt utfylt, med kvalitetskontrollar |
| [`felles-datakatalog`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md#felles-datakatalog-felles-datakatalog) | ModelDCAT-AP-NO — publisering til Felles Datakatalog |
| [`felles-begrepskatalog`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md#felles-begrepskatalog-felles-begrepskatalog) | SKOS-AP-NO-Begrep — publisering til Felles Begrepskatalog |

### Generatorflag

Dei boolske felta svarar 1:1 til `manifest.yaml flag`-kolonnen i
[tabellen over genererte artefakter](https://github.com/brreg/linkml-datamodellering-no#genererte-artefakter)
i README. Alle har standardverdi `true`.

I tillegg kjem to flagg-felt for generatorar som treng ekstra parametrar:

| Felt | Type | Standard | Skildring |
|---|---|---|---|
| `shacl_flags` | streng | `""` | Ekstra flagg til `gen-shacl`, t.d. `"--exclude-imports"` |
| `owl_flags` | streng | `""` | Ekstra flagg til `gen-owl`, t.d. `"--log_level ERROR"` |

## Eksempel

**Standardkonfig** (NGR, OREG — alle generatorar på, ingen flagg):

```yaml
publish_external: false
validation_policy: silver

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
  openapi: true
```

**FINT** (`rdf: false` pga. HTTP-feil ved JSON-LD-kontekstoppslag; SHACL- og OWL-flagg
for å handtere kryss-skjema klassearv; `example_rdf: false` der eksempelfila nyttar
FINT-stile CURIEs som ikkje er gyldige URI-ar):

```yaml
publish_external: false
validation_policy: silver

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: "--exclude-imports"
  python: true
  json_schema: true
  owl: true
  owl_flags: "--log_level ERROR"
  rdf: false
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
  openapi: true
```

**AP-NO / FAIR** (`example_rdf: false` — desse skjemaa har ingen `tree_root` og kan
ikkje konverterast til RDF av `linkml-convert`):

```yaml
publish_external: false
validation_policy: bronze

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
  openapi: true
```

## Korleis det fungerer

`gen-config.sh` les alle skjema-`manifest.yaml`-filer og skriv `config.mk` — eit
Makefile-fragment med per-modell-variablar som Makefile-en inkluderer automatisk.
`config.mk` vert automatisk regenerert når ei `manifest.yaml`-fil endrar seg. Du
kan òg regenerere manuelt:

```bash
make config.mk
```

`config.mk` er generert og skal ikkje redigerast for hand.

## Nye modellar

`make new-model NAME=... DOMAIN=...` oppretter ei standard `manifest.yaml` saman med
skjemafila. Juster henne etterpå viss domenet krev det — til dømes for FINT-modellar
der `rdf` og `example_rdf` skal vera `false`.
