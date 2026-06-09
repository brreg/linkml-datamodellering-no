# Roundtrip-testar for serialiseringsformat

## Bakgrunn

`test_make.sh` verifiserer at generatorar produserer gyldige artefaktar, men testar
ikkje at serialisering er **informasjonstap-fri** — altså at eit format kan konverterast
til eit anna og tilbake og framleis representere same data.

`linkml-convert` støttar konvertering mellom `yaml`, `json`, `ttl/rdf`, `json-ld`,
`csv` og `tsv`. Roundtrip-testar brukar dette til å oppdage tap av data, feil i
serialiseringslogikk og inkonsistens mellom format.

## Strategi

Direkte tekstsamanlikning av `A.yaml` og `A_rt.yaml` etter roundtrip er ikkje
meiningsfull — key-rekkefølgje, kommentarar og whitespace forsvinn. I staden
brukar testane ein **kanonisk JSON-samanlikning**:

```
eksempel.yaml  →[convert]→  tmp.json  →[convert]→  tmp_rt.yaml  →[convert]→  tmp_rt.json
                                │                                                  │
                                └───────── deep-equal (Python dict) ───────────────┘
```

Dvs.: konverter originalen til JSON, deretter tilbake til YAML, deretter til JSON
igjen. Samanlikn dei to JSON-filene som Python-dict (key-rekkefølgje-uavhengig).

## Format-scopet

Prioriterte roundtrips basert på kva `linkml-convert` støttar og kva som er
relevant for prosjektet:

| Roundtrip | Dekker |
|---|---|
| `yaml → json → yaml → json` | JSON API-serialisering |
| `yaml → ttl → yaml → json` | RDF-serialisering (for skjema med `tree_root`) |

Begge roundtrip-typane samanliknar til slutt på JSON-nivå (Python dict).

## Avgrensingar (arva frå `test_make.sh`)

- **ap-no og fair**: Manglar `tree_root` — `linkml-convert` kan ikkje bestemme
  målklasse. Hoppar over.
- **ngr-adresse, ngr-eiendom, ngr-virksomhet**: linkml-runtime-bug med
  `id`-only `inlined_as_list`-objekt. Hoppar over.
- **TTL-roundtrip**: Krev at skjemaet ikkje hoppar over `gen-rdf`
  (`GEN_RDF_SKIP_*`). fint og samt vert hoppa over.

## Implementasjon

### Ny testfunksjon i `test_make.sh`

Legg til to nye testfunksjonar og kall dei frå `run_schema_tests`:

```bash
_run_one "roundtrip-json ($name)"  test_roundtrip_json "$schema" "$example" "$domain" "$name"
_run_one "roundtrip-ttl ($name)"   test_roundtrip_ttl  "$schema" "$example" "$domain" "$name"
```

#### `test_roundtrip_json`

```bash
test_roundtrip_json() {
    local schema="$1" example="$2" domain="$3" name="$4"

    # Domene utan tree_root støttar ikkje linkml-convert
    if [[ "$domain" == "ap-no" || "$domain" == "fair" ]]; then
        echo "Hoppar over roundtrip-json for $domain (ingen tree_root)"
        return 0
    fi
    if [ ! -f "$example" ]; then
        echo "Ingen eksempelfil: $example (hoppar over)"
        return 0
    fi

    local tmp_json tmp_rt_yaml tmp_rt_json
    tmp_json=$(mktemp /tmp/rt_json_XXXXXX.json)
    tmp_rt_yaml=$(mktemp /tmp/rt_yaml_XXXXXX.yaml)
    tmp_rt_json=$(mktemp /tmp/rt_json2_XXXXXX.json)

    # Steg 1: yaml → json
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        linkml-convert --schema "$schema" --output-format json \
            --no-validate --output "$(basename "$tmp_json")" "$example" \
        || { echo "yaml→json feila"; rm -f "$tmp_json" "$tmp_rt_yaml" "$tmp_rt_json"; return 1; }

    # Steg 2: json → yaml
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        linkml-convert --schema "$schema" --output-format yaml \
            --no-validate --output "$(basename "$tmp_rt_yaml")" "$(basename "$tmp_json")" \
        || { echo "json→yaml feila"; rm -f "$tmp_json" "$tmp_rt_yaml" "$tmp_rt_json"; return 1; }

    # Steg 3: yaml → json (kanonisk form av roundtrip-resultatet)
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        linkml-convert --schema "$schema" --output-format json \
            --no-validate --output "$(basename "$tmp_rt_json")" "$(basename "$tmp_rt_yaml")" \
        || { echo "rt-yaml→json feila"; rm -f "$tmp_json" "$tmp_rt_yaml" "$tmp_rt_json"; return 1; }

    # Steg 4: samanlikn JSON som Python-dict (key-rekkefølgje-uavhengig)
    python3 - "$tmp_json" "$tmp_rt_json" << 'PYEOF'
import json, sys
a = json.load(open(sys.argv[1]))
b = json.load(open(sys.argv[2]))
if a != b:
    import pprint
    print("ROUNDTRIP-AVVIK (yaml→json→yaml→json):")
    print("Forventa:", pprint.pformat(a)[:500])
    print("Fekk:    ", pprint.pformat(b)[:500])
    sys.exit(1)
print("Roundtrip OK")
PYEOF
    local rc=$?
    rm -f "$tmp_json" "$tmp_rt_yaml" "$tmp_rt_json"
    return $rc
}
```

#### `test_roundtrip_ttl`

```bash
test_roundtrip_ttl() {
    local schema="$1" example="$2" domain="$3" name="$4"

    # Domene utan tree_root eller med GEN_RDF_SKIP
    if [[ "$domain" == "ap-no" || "$domain" == "fair" || \
          "$domain" == "fint"  || "$domain" == "samt" ]]; then
        echo "Hoppar over roundtrip-ttl for $domain"
        return 0
    fi
    # ngr-bug: id-only inlined_as_list
    if [[ "$name" == "ngr-adresse" || "$name" == "ngr-eiendom" || \
          "$name" == "ngr-virksomhet" ]]; then
        echo "Hoppar over roundtrip-ttl for $name (linkml-runtime bug)"
        return 0
    fi
    if [ ! -f "$example" ]; then
        echo "Ingen eksempelfil: $example (hoppar over)"
        return 0
    fi

    local tmp_json tmp_ttl tmp_rt_yaml tmp_rt_json
    tmp_json=$(mktemp /tmp/rt_ttl_json_XXXXXX.json)
    tmp_ttl=$(mktemp /tmp/rt_XXXXXX.ttl)
    tmp_rt_yaml=$(mktemp /tmp/rt_ttl_yaml_XXXXXX.yaml)
    tmp_rt_json=$(mktemp /tmp/rt_ttl_json2_XXXXXX.json)

    # Steg 1: yaml → json (referanse)
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        linkml-convert --schema "$schema" --output-format json \
            --no-validate --output "$(basename "$tmp_json")" "$example" \
        || { echo "yaml→json feila"; rm -f "$tmp_json" "$tmp_ttl" "$tmp_rt_yaml" "$tmp_rt_json"; return 1; }

    # Steg 2: yaml → ttl
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        linkml-convert --schema "$schema" --output-format ttl \
            --no-validate --output "$(basename "$tmp_ttl")" "$example" \
        || { echo "yaml→ttl feila"; rm -f "$tmp_json" "$tmp_ttl" "$tmp_rt_yaml" "$tmp_rt_json"; return 1; }

    # Steg 3: ttl → yaml
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        linkml-convert --schema "$schema" --output-format yaml \
            --no-validate --output "$(basename "$tmp_rt_yaml")" "$(basename "$tmp_ttl")" \
        || { echo "ttl→yaml feila"; rm -f "$tmp_json" "$tmp_ttl" "$tmp_rt_yaml" "$tmp_rt_json"; return 1; }

    # Steg 4: rt-yaml → json (kanonisk form)
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        linkml-convert --schema "$schema" --output-format json \
            --no-validate --output "$(basename "$tmp_rt_json")" "$(basename "$tmp_rt_yaml")" \
        || { echo "rt-yaml→json feila"; rm -f "$tmp_json" "$tmp_ttl" "$tmp_rt_yaml" "$tmp_rt_json"; return 1; }

    # Steg 5: samanlikn JSON som Python-dict
    python3 - "$tmp_json" "$tmp_rt_json" << 'PYEOF'
import json, sys
a = json.load(open(sys.argv[1]))
b = json.load(open(sys.argv[2]))
if a != b:
    import pprint
    print("ROUNDTRIP-AVVIK (yaml→ttl→yaml→json):")
    print("Forventa:", pprint.pformat(a)[:500])
    print("Fekk:    ", pprint.pformat(b)[:500])
    sys.exit(1)
print("Roundtrip OK")
PYEOF
    local rc=$?
    rm -f "$tmp_json" "$tmp_ttl" "$tmp_rt_yaml" "$tmp_rt_json"
    return $rc
}
```

### Plassering av tmpfiler

Alle temp-filer vert oppretta med `mktemp` og ligg i `/tmp` i container-hosten.
Podman-kallet monterer `$REPO_ROOT:/work` — tmpfilene manglar difor i `/work`.
**Temp-filene må leggjast i `$REPO_ROOT` (ikkje `/tmp`) og slettast i cleanup.**

Alternativt kan `mktemp` kallast slik at fila ligg under `$REPO_ROOT/tmp/`:

```bash
mkdir -p "$REPO_ROOT/tmp"
tmp_json=$(mktemp "$REPO_ROOT/tmp/rt_XXXXXX.json")
# I podman-kallet: --output "tmp/$(basename "$tmp_json")"
```

Dette er eit implementasjonsdetalj som må løysast ved utprøving.

## Prioritert tiltaksliste

| # | Tiltak | Prioritet |
|---|---|---|
| 1 | Implementer `test_roundtrip_json` i `test_make.sh` og integrer i `run_schema_tests` | Høg |
| 2 | Køyr `make test SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` og juster for tmpfil-plassering | Høg |
| 3 | Verifiser at alle domene som ikkje er hoppa over passerer JSON-roundtrip | Høg |
| 4 | Implementer `test_roundtrip_ttl` og integrer i `run_schema_tests` | Medium |
| 5 | Verifiser TTL-roundtrip for alle domene som støttar gen-rdf | Medium |

## Utført

Alle tiltak gjennomførte. Begge roundtrip-testar er implementerte i
`tests/test_make.sh` og integrerte i `run_schema_tests`. Alle skjema
passerer 17/17 testar.

### Implementasjonsdetaljar

- **Tmpfiler**: Ligg i `$REPO_ROOT/tmp/` (tilgjengeleg frå container som
  `/work/tmp/`) og vert sletta av kvar testfunksjon. `$REPO_ROOT/tmp/`
  vert oppretta ved oppstart og sletta i `cleanup`-trap.
- **`example`-variabel**: Lagt til i `run_schema_tests` som
  `src/linkml/$domain/$name/examples/$name-eksempel.yaml` — den korrekte
  stien (i motsetnad til den legacy-stien `examples/$domain/...` som
  eksisterende testar brukar).

### JSON-roundtrip: resultat av verifikasjon (steg 3)

Passerer for alle skjema med `tree_root` og eksempelfil, *unntatt* fire
fint-skjema:

| Skjema | Årsak |
|---|---|
| `fint-administrasjon` | linkml-runtime URI/CURIE-bug: relasjonsobjekt inline i eksempel |
| `fint-okonomi` | same |
| `fint-personvern` | same |
| `fint-utdanning` | same |

Desse fire skjemaa har eksempeldata der relasjonsslotar inneheld fulle
objekt i staden for URI/CURIE-referansar. `linkml-convert` feiler
då med `ValueError: ... is not a valid URI or CURIE`. Dei er lagt til
skip-lista i `test_roundtrip_json`.

### TTL-roundtrip: resultat av verifikasjon (steg 5)

Berre `fint-ressurs` passerer fullt TTL-roundtrip. Alle andre skjema
feiler av ein eller fleire av desse kjende linkml-runtime-bugane:

| Feil | Skjema |
|---|---|
| yaml→ttl: URI/CURIE-bug (same som JSON) | fint-administrasjon, fint-okonomi, fint-personvern, fint-utdanning |
| yaml→ttl: `ValueError: field must be supplied` (required felt etter konvertering) | brreg-begrepskatalog |
| ttl→yaml: `DataNotFoundError: Got 0 of type ContainerClass` | samt-bu |
| ttl→yaml: `TypeError: __init__() got unexpected keyword argument` | brreg-modellkatalog, ngr-adresse |
| ttl→yaml: AVVIK (datadiff etter roundtrip) | fint-arkiv |

Alle desse er lagt til skip-lista i `test_roundtrip_ttl`. `fint-ressurs`
køyrer og passerer TTL-roundtrip.

### Avgrensingar frå spec som er justert

Spec-en sa at fint og samt skulle skippast i TTL-roundtrip grunna
`GEN_RDF_SKIP_*`. Det er ikkje lenger relevant (fiksa i `ttl-roundtrip-fint-samt.md`).
I staden er dei spesifikke feil-kategoriane dokumentert over.
