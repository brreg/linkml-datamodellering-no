# TTL-roundtrip: Aktiver gen-rdf for fint og samt

## Bakgrunn

`test_roundtrip_ttl` i `test_make.sh` hoppar over `fint`- og `samt`-domenet
fordi desse skjemaa har `rdf: false` i `manifest.yaml`. Det betyr at
`GEN_RDF_SKIP_*`-flagga er sette, og TTL-roundtrip-testen difor ikkje kan køyre.

Årsaka til at `rdf: false` vart sett er ikkje dokumentert, men analyse viser
to ulike situasjonar:

### fint (7 skjema)

Alle fint-skjema har `class_uri` for domene-klasser og `slot_uri` for alle
slots — med eitt unntak:

- `fint-common/fint-common-schema.yaml` manglar `slot_uri` på `id`-sloten.
  Sidan dette er ein `identifier: true`-slot, vert innhaldet brukt som
  emne-URI i RDF (ikkje som predikat) — `slot_uri` er difor truleg ikkje
  nødvendig for vellykka RDF-generering.
- Container-klasser manglar `class_uri`, men det er korrekt per
  modelleringsprinsippa.

fint treng truleg berre `rdf: true` i alle manifest.

### samt (1 skjema: `samt-bu`)

`samt-bu-schema.yaml` manglar RDF-URI-ar for det meste:

- **10 domene-klasser utan `class_uri`**: `Skole`, `Skoleeier`, `Kommune`,
  `Fylke`, `PrivatVirksomhet`, `Basisgruppe`, `Person`, `Elev`, `Rektor`,
  `Kontaktlaerer`
- **8 slots utan `slot_uri`**: `navn`, `trinniva`, `har_skoleeier`,
  `horer_til_basisgruppe`, `enhetsleder_for`, `tilknyttet_basisgruppe`,
  `har_saerlig_ansvar_for`, `jobber_paa_skole`

Skjemaet har prefixet `samtbuskole: https://example.no/ontology/skole#`
definert. URI-ane under er forslag basert på dette prefixet — juster om
domenet har etablerte URI-ar.

## Prioritert tiltaksliste

| # | Tiltak | Prioritet |
|---|---|---|
| 1 | Sett `rdf: true` og `example_rdf: true` i alle 7 fint-manifest | Høg |
| 2 | Køyr `make lint` og `make test` for eitt fint-skjema og sjekk at gen-rdf går gjennom | Høg |
| 3 | Legg til `class_uri` for 10 domene-klasser i `samt-bu-schema.yaml` | Høg |
| 4 | Legg til `slot_uri` for 8 slots i `samt-bu-schema.yaml` | Høg |
| 5 | Sett `rdf: true` i `samt-bu/manifest.yaml` | Høg |
| 6 | Køyr `make lint SCHEMA=...samt-bu...` og `make test SCHEMA=...samt-bu...` | Høg |
| 7 | Fjern `"$domain" == "fint"` og `"$domain" == "samt"` frå skip-lista i `test_roundtrip_ttl` i `test_make.sh` | Høg |

## Utført

Alle tiltak gjennomførte. `make test` passerer 15/15 for `fint-administrasjon`
og `samt-bu` inkludert `gen-rdf`.

### Oppdaga rot-årsak: context-URL-konstruksjon i gen-rdf

Den opphavlege analysen antok at `rdf: false` berre trengde å setjast til `true`.
Under implementasjonen vart den eigentlege årsaka avdekt:

`gen-rdf` konstruerer context-URL for kvart importert skjema som
`{default_prefix til importerande skjema}/{relativ importsti}.context.jsonld`.
For fint-sub-skjema (t.d. `default_prefix: https://schema.fintlabs.no/administrasjon/`
+ import `../fint-common/fint-common-schema`) gav dette
`https://schema.fintlabs.no/fint-common/fint-common-schema.context.jsonld` — HTTP 404.
For `samt-bu` (`default_prefix: samtbuskole` = `https://example.no/ontology/skole#`)
gav importen av `dcat-ap-no` URL-en `https://example.no/ap-no/dcat-ap-no/...` — HTTP 500.

Context-filene finst derimot på `data.norge.no` (HTTP 200).

### Endringar som avviker frå opphavleg plan

- **`default_prefix` endra i 6 fint-sub-skjema** (ikkje planlagt): frå
  `https://schema.fintlabs.no/{domene}/` til `https://data.norge.no/fint/fint-{domene}/`.
  Påverkar berre strukturelle termar (containerklasse og dens attributtar) — alle
  domene-klasser og slots har eksplisitte `class_uri`/`slot_uri` via `adm:`, `ark:` osv.
- **`default_prefix` endra i `samt-bu`** (ikkje planlagt): frå `samtbuskole`
  til `https://data.norge.no/samt/samt-bu/`. Alle domain-klasser og slots har
  eksplisitte `samtbuskole:`-URI-ar og vert ikkje påverka.
- **`fint-common` uendra** — treng ikkje `default_prefix`-endring sidan det
  er det *importerte* skjemaet, ikkje importøren.
- **`test_gen_rdf` i `tests/test_make.sh`** (ikkje `test_roundtrip_ttl` som spec-en
  nemnde) — `test_roundtrip_ttl` er ikkje implementert enno (ligg i `roundtrip-testar.md`).
  Skip for `fint` og `samt` fjerna frå `test_gen_rdf`.

## Implementasjon

### Steg 1-2: fint-manifest

I kvart av dei 7 fint-manifesta (`fint-administrasjon`, `fint-arkiv`,
`fint-common`, `fint-okonomi`, `fint-personvern`, `fint-ressurs`,
`fint-utdanning`):

```yaml
# Før
  rdf: false
  example_rdf: false

# Etter
  rdf: true
  example_rdf: true
```

Dersom `gen-rdf` feiler på `id`-sloten i `fint-common`, legg til:

```yaml
  id:
    identifier: true
    range: uriorcurie
    slot_uri: fint:id          # <- legg til
    description: URI-identifikator for ressursen.
```

### Steg 3-4: samt-bu — class_uri

Legg til `class_uri` for alle domene-klasser i
`src/linkml/samt/samt-bu/samt-bu-schema.yaml`:

```yaml
  Skole:
    class_uri: samtbuskole:Skole
    ...

  Skoleeier:
    class_uri: samtbuskole:Skoleeier
    ...

  Kommune:
    class_uri: samtbuskole:Kommune
    ...

  Fylke:
    class_uri: samtbuskole:Fylke
    ...

  PrivatVirksomhet:
    class_uri: samtbuskole:PrivatVirksomhet
    ...

  Basisgruppe:
    class_uri: samtbuskole:Basisgruppe
    ...

  Person:
    class_uri: samtbuskole:Person
    ...

  Elev:
    class_uri: samtbuskole:Elev
    ...

  Rektor:
    class_uri: samtbuskole:Rektor
    ...

  Kontaktlaerer:
    class_uri: samtbuskole:Kontaktlaerer
    ...
```

### Steg 4: samt-bu — slot_uri

Legg til `slot_uri` for dei 8 slots som manglar:

```yaml
  navn:
    slot_uri: samtbuskole:navn
    range: string
    description: Namn på ressursen.

  trinniva:
    slot_uri: samtbuskole:trinniva
    description: Grunnskolen (6-15 år) er delt opp i 10 trinn, eit for kvart år.
    range: string

  har_skoleeier:
    slot_uri: samtbuskole:harSkoleeier
    description: Skoleeier for skolen
    exact_mappings:
      - org:hasUnit
    domain: Skole
    range: Skoleeier

  horer_til_basisgruppe:
    slot_uri: samtbuskole:horerTilBasisgruppe
    description: Basisgruppe elev tilhører
    close_mappings:
      - schema:memberOf
    domain: Elev
    range: Basisgruppe

  enhetsleder_for:
    slot_uri: samtbuskole:enhetslederFor
    description: Enhet rektor er enhetsleder for
    close_mappings:
      - org:headOf
    domain: Rektor
    range: Skole

  tilknyttet_basisgruppe:
    slot_uri: samtbuskole:tilknyttetBasisgruppe
    description: Basisgruppe kontaktlærer er tilknyttet
    close_mappings:
      - schema:teaches
    domain: Kontaktlaerer
    range: Basisgruppe

  har_saerlig_ansvar_for:
    slot_uri: samtbuskole:harSaerligAnsvarFor
    description: Elev kontaktlæreren har særlig ansvar for
    domain: Kontaktlaerer
    range: Elev

  jobber_paa_skole:
    slot_uri: samtbuskole:jobberPaaSkole
    description: Skolen kontaktlæreren jobber på
    close_mappings:
      - schema:worksFor
      - org:memberOf
    domain: Kontaktlaerer
    range: Skole
```

### Steg 7: test_make.sh — fjern domene-skip

I `test_roundtrip_ttl`-funksjonen i `src/assets/scripts/test_make.sh`,
fjern `fint` og `samt` frå skip-lista:

```bash
# Før
    if [[ "$domain" == "ap-no" || "$domain" == "fair" || \
          "$domain" == "fint"  || "$domain" == "samt" ]]; then
        echo "Hoppar over roundtrip-ttl for $domain"
        return 0
    fi

# Etter
    if [[ "$domain" == "ap-no" || "$domain" == "fair" ]]; then
        echo "Hoppar over roundtrip-ttl for $domain (ingen tree_root)"
        return 0
    fi
```

Oppdater òg kommentaren i `roundtrip-testar.md` (seksjonen
«Avgrensingar») tilsvarande når tiltaka er gjennomførte.
