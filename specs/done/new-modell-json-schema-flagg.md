# Plan: `JSON_SCHEMA=`-flagg til `make new-modell`

## Bakgrunn

Dagens arbeidsflyt for å opprette ein ny LinkML-modell frå eit eksportert JSON Schema
er tre manuelle steg:

```bash
make new-modell DOMAIN=oreg NAME=enhetsregisteret-bvrstiftelsesdokument
make mcp-linkml-modell-utkast SCHEMA=src/tmp/bvrstiftelsesdokument_lm_v0.schema.json
# manuelt: kopier src/tmp/bvrstiftelsesdokument_lm_v0.schema-schema.yaml til
#          src/linkml/oreg/enhetsregisteret-bvrstiftelsesdokument/enhetsregisteret-bvrstiftelsesdokument-schema.yaml
```

Dette har to konkrete svakheiter, synlege i dei fem nyoppretta katalogane under
`src/linkml/oreg/enhetsregisteret-bvr*/` (git status ved starten av denne spec-en):

1. **Manuell kopiering droppar all etterbehandling.** `make new-modell` (utan JSON-schema)
   køyrer `src/assets/scripts/scaffolding/new-modell.sh`, som set korrekt `id`/`name`/
   `title`, slår opp `annotations.utgiver` frå CODEOWNERS, set `endringsdato`/
   `utgivelsesdato`, og injiserer versjonslåst `dcat-ap-no`-import. `make
   mcp-linkml-modell-utkast` (med JSON Schema) gjer **ingenting** av dette — han skriv
   resultatet frå MCP-serveren rått til `$(basename $(SCHEMA))-schema.yaml`. Når fila
   deretter berre vert kopiert inn, står `id: https://example.org/generated`,
   `name: generated` og `title: 'TODO: tittel for generated'` att uendra i den
   ferdige modellen — sjå `enhetsregisteret-bvrbekreftelse-schema.yaml` i dag.
2. **`examples/<namn>-eksempel.yaml` vert aldri fylt ut.** `new-modell.sh` skriv ein
   hardkoda minimal stub (kun `id: <namn>:eksempel-1`) uansett kva veg som vart brukt
   til å generere sjølve skjemaet. For JSON-schema-genererte modellar med mange
   klassar er denne stubben ikkje eit reelt utgangspunkt — alle fem
   `enhetsregisteret-bvr*`-eksempla står framleis med denne uendra malen.

Talet på steg og den manuelle kopieringa gjer arbeidsflyten feilsett-utsett (lett å
gløyme å oppdatere id/namn/annotations) og hindrar eit fungerande startpunkt for
eksempeldata.

## Mål

Eitt kommando skal kunne ta eit eksportert JSON Schema som input og produsere ein
ferdig etterbehandla modell **direkte i den nye katalogstrukturen**, saman med ei
eksempeldatafil som allereie validerer:

```bash
make new-modell DOMAIN=oreg NAME=enhetsregisteret-bvrstiftelsesdokument \
  JSON_SCHEMA=src/tmp/bvrstiftelsesdokument_lm_v0.schema.json
```

`make new-modell` **utan** `JSON_SCHEMA` skal halde fram å fungere akkurat som i dag
(`--input-format empty`) — flagget er reint additivt.

## Kvifor `JSON_SCHEMA`, ikkje `JSON-SCHEMA`

Brukarinstruksjonen nemnde `JSON-SCHEMA=` som flaggnamn. Alle eksisterande
make-variablar i dette repoet (`DOMAIN`, `NAME`, `SCHEMA`, `POLICY`, `FORMAT`, ORG,
CONFIRM, INSTANCE) er utan bindestrek — GNU Make tillèt teknisk bindestrek i
variabelnamn, men det er eit usemantisk avvik frå resten av kodebasen og kan lett
mistolkast som eit make-target-namn i skallet. Denne spec-en brukar
**`JSON_SCHEMA`** (understrek, som `mcp-linkml-modell-utkast` sitt `FORMAT`) —
**stadfesta av brukar**, sjå Avklaringar.

## Design

### Steg 1 — Utvid `new-modell`-target i `make/70-scaffolding.mk`

```makefile
new-modell: ## Opprett katalogstruktur og boilerplate for ny domenemodell (DOMAIN=<domene> NAME=<modell> [JSON_SCHEMA=<sti til json-schema>])
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-modell DOMAIN=<domene> NAME=<modell> [JSON_SCHEMA=<sti>]"; exit 1; }
	$(call print_header,new-modell,DOMAIN=$(DOMAIN)  NAME=$(NAME)$(if $(JSON_SCHEMA),  JSON_SCHEMA=$(JSON_SCHEMA)))
	@podman image exists $(LINKML_MOD_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-modell-utkast
	bash src/assets/scripts/scaffolding/new-modell.sh "$(NAME)" "$(DOMAIN)" "$(JSON_SCHEMA)"
```

Berre éin ekstra, valfri posisjonsparameter til scriptet — ingen brot på eksisterande
kallmønster (`new-modell.sh` sitt tredje argument vert tom streng når `JSON_SCHEMA`
er ubrukt).

### Steg 2 — Grein `new-modell.sh` på `--input-format`

I dag (linje 47–53) kallar scriptet alltid:

```bash
python3 "$REQUEST_SCRIPT" \
    --input-format empty \
    --schema-id "$SCHEMA_ID" \
    --schema-name "$SCHEMA_NAME" \
    --schema-title "TODO: tittel for $NAME" \
    --policy silver \
    --no-validate \
  | podman run ... \
  | python3 "$RESPONSE_SCRIPT"
```

Legg til eit tredje argument `JSON_SCHEMA="${3:-}"` og bygg request ut frå det:

```bash
if [[ -n "$JSON_SCHEMA" ]]; then
    if [[ ! -f "$JSON_SCHEMA" ]]; then
        echo "Feil: $JSON_SCHEMA finst ikkje." >&2
        exit 1
    fi
    INPUT_FORMAT=json-schema
    INPUT_FILE_ARGS=(--input-file "$JSON_SCHEMA")
else
    INPUT_FORMAT=empty
    INPUT_FILE_ARGS=()
fi

LINKML_YAML=$(python3 "$REQUEST_SCRIPT" \
    --input-format "$INPUT_FORMAT" \
    "${INPUT_FILE_ARGS[@]}" \
    --schema-id "$SCHEMA_ID" \
    --schema-name "$SCHEMA_NAME" \
    --schema-title "TODO: tittel for $NAME" \
    --policy silver \
    --no-validate \
  | podman run -i --rm ... \
  | python3 "$RESPONSE_SCRIPT")
```

`--schema-id`/`--schema-name`/`--schema-title` er allereie format-uavhengige i
`mcp-build-modell-utkast-request.py` (verifisert: argparse tek dei uansett
`--input-format`-verdi) — det er **nettopp fråveret** av desse flagga i dagens
`mcp-linkml-modell-utkast`-target (`make/60-mcp.mk` linje 66–68) som gjer at
`id`/`name` endar som `example.org`/`generated`. Å sende dei med her løyser punkt 1
i Bakgrunn nesten gratis, utan endring i MCP-serveren.

### Steg 3 — Generaliser PascalCase-steget i etterbehandlinga

Dagens Python-blokk (linje 74–172 i `new-modell.sh`) føreset **éin** ikkje-container-
klasse («stub») og PascalCase-ar berre den (`else: stub_name = cname` i ei
for-løkke som overskriv, held berre siste treff). JSON-schema-vegen produserer
typisk mange klassar som allereie er PascalCase (verifisert mot
`enhetsregisteret-bvrbekreftelse-schema.yaml`: `Bekreftelse`, `Rolle`, `Virksomhet`,
`Person`, `EierskifteAktivitet`, `DelerEierskifte` — alle korrekt kasa av
MCP-konverteraren sjølv).

Endre løkka til å samle **alle** ikkje-container-klassar og PascalCase-ar kvar av
dei (idempotent når namnet alt er PascalCase, så trygt å køyre uansett input-format).
**Stadfesta av brukar:** containerklassen skal same stad PascalCase-ast om att til
`<Domene>Container`-konvensjonen (ikkje berre MCP-serveren sitt rå
`<SchemaName>Container`-namn, som kan ha understrek frå bindestrek-transformasjonen
av `NAME`) — gjenbruk `to_pascal_case` på `container_name` i tillegg til stubbane:

```python
classes = schema.get('classes') or {}
container_name = None
stub_names = []
for cname, cdef in classes.items():
    if cdef.get('tree_root'):
        container_name = cname
    else:
        stub_names.append(cname)

for stub_name in stub_names:
    new_stub_name = to_pascal_case(stub_name)
    if new_stub_name != stub_name:
        classes[new_stub_name] = classes.pop(stub_name)
        if container_name:
            for slot_def in (classes[container_name].get('attributes') or {}).values():
                if slot_def.get('range') == stub_name:
                    slot_def['range'] = new_stub_name

if container_name:
    new_container_name = to_pascal_case(container_name)
    if new_container_name != container_name:
        classes[new_container_name] = classes.pop(container_name)
        container_name = new_container_name
```

**Merk:** `slots.pop('id', None)` (linje 122) fjernar eit eventuelt globalt
`id`-slot ut frå at det skal arvast frå `dcat-ap-no`-importet. For JSON-schema-
genererte modellar med mange sjølvstendige klassar er dette ikkje sikkert korrekt —
kvar klasse kan ha sitt eige `id`-slot med anna semantikk enn DCAT sin. **Stadfesta
av brukar:** denne antakinga skal verifiserast manuelt mot eit par faktiske JSON
Schema-eksempel (sjå handlingsliste-punkt 4) før steget vert generalisert
ukritisk til den automatiske flyten.

### Steg 4 — Generer eksempeldatafil frå det ferdige skjemaet

I dag skriv `new-modell.sh` (linje 174–180) alltid ein hardkoda éin-linjes stub:

```bash
cat > "$EXAMPLE_FILE" << EOF
$CONTAINER_SLOT:
  - id: ${SCHEMA_NAME}:eksempel-1
EOF
```

`src/mcp-linkml-modell-utkast/validator.py` har allereie logikken som trengst for
eit betre startpunkt: `_build_dummy_data(sv, container_class)` bygger nett éin
instans per container-attributt med alle `required`/`identifier`-slots utfylte med
type-baserte placeholder-verdiar (`_PLACEHOLDERS`-tabellen: `string→"dummy"`,
`integer→0`, `date→"2024-01-01"`, `uriorcurie→"ex:dummy-1"` osv.), og verifiserer
alt at resultatet validerer via `linkml.validator.validate(...)`. Dette køyrer i
dag berre internt i `validate_generated()` for å teste at skjemaet er gyldig — det
vert aldri skrive til fil.

Føreslått endring: bryt `_build_dummy_data`/`_build_dummy_instance` ut til ein
liten, delt funksjon (t.d. `src/mcp-linkml-modell-utkast/example_builder.py`, eller
behald i `validator.py` og importer derifrå), og legg til eit nytt steg i
`new-modell.sh` sin etterbehandlings-Python som:

1. Kallar same funksjon på det **ferdig etterbehandla** skjemaet (etter PascalCase-
   rename, annotations, import-injeksjon over) — ikkje det rå MCP-svaret, sidan
   klassenamn kan ha endra seg i steg 3.
2. Dumpar resultatet som YAML under container-attributtet, med same
   `id: <navn>:eksempel-N`-mønster som i dag for identifikator-slots.
3. Skriv ein kommentarlinje øvst som minner om at placeholder-verdiar (`dummy`,
   `0`, `2024-01-01`) må erstattast med reelle verdiar før modellen er
   produksjonsklar — same TODO-konvensjon som skjemafila allereie brukar.

**Omfang, v1:** behald placeholder-tilnærminga slik ho er i dag (kun
`required`/`identifier`-slots) i staden for å fylle ut alle valfrie slots — ei
eksempelfil med berre obligatoriske felt er eit korrekt, minimalt startpunkt og
unngår å blåse opp fila med gjettverdiar for felt brukaren uansett må vurdere
manuelt. Dette er i tråd med prinsippet «minimale endringar» i CLAUDE.md.

**Akseptansekriterium:** den genererte eksempelfila skal validere direkte via
`make validate-instance SCHEMA=<ny-modell-schema.yaml> INSTANCE=<ny-eksempel.yaml>`
utan manuell retting — dette er allereie sannsynleggjort ved at
`validate_generated()` i dag køyrer nøyaktig denne valideringa internt (steg B i
`validator.py`) og rapporterer `dummy_validation.valid`.

### Steg 5 — Dokumentasjon

- `COMMANDS.md`: oppdater skildringa av `new-modell`-targetet med det nye flagget
  og eit døme.
- `mkdocs/docs/kom-i-gang/ny-domenemodell.md`: legg til eit alternativt spor for
  «opprett modell frå eksisterande JSON Schema» som viser eitt-kommando-flyten, og
  merk det gamle trestegs-mønsteret (`new-modell` → `mcp-linkml-modell-utkast` →
  manuell kopiering) som framleis gyldig for tilfelle der ein vil inspisere/justere
  det rå konverteringsresultatet før det landar i endeleg katalog (t.d. via
  `src/tmp/`) før det vert vedteke.

## Avklaringar (stadfesta av brukar)

Brukaren har stadfesta alle fire tilrådde vala under — ingen av desse er lenger
opne spørsmål, men dokumentert her slik at grunngjevinga følgjer vedtaket:

1. **Flaggnamn:** `JSON_SCHEMA` (understrek, konsistent med resten av repoet sine
   make-variablar) — ikkje brukar sin opphavlege `JSON-SCHEMA`-staving med
   bindestrek. Sjå grunngjeving i «Kvifor `JSON_SCHEMA`, ikkje `JSON-SCHEMA`».
2. **`slots.pop('id', None)`-steget** (Steg 3) skal **ikkje** generaliserast
   ukritisk til JSON-schema-vegen utan verifisering først. Handlingsliste-punkt 4
   held fram som eit obligatorisk steg: testast mot minst to av dei eksisterande
   `src/tmp/*.schema.json`-filene (t.d. `bvrfriv_lm_v1.schema.json`,
   `bvrettersendingavvedlegg_lm_v1.schema.json`) før dette vert ein del av den
   automatiske flyten, for å unngå å fjerne eit `id`-slot som faktisk trengst
   lokalt i ein av dei genererte klassane.
3. **Container-klassenamn:** containerklassen for JSON-schema-vegen skal
   omdøypast frå MCP-serveren sitt rå `<SchemaName>Container`-mønster (t.d.
   `Enhetsregisteret_bvrbekreftelseContainer` — sidan `SCHEMA_NAME` har
   bindestrek→understrek-transformasjon) til PascalCase utan understrek
   (`EnhetsregisteretBvrbekreftelseContainer`), i tråd med konvensjonen i
   CLAUDE.md (`<Domene>Container` i PascalCase). Innarbeidd i Steg 3-koden over
   (gjenbruk av `to_pascal_case` på `container_name`).
4. **Det gamle trestegsmønsteret held fram som dokumentert og støtta**, sidan det
   gjev eit punkt der ein kan inspisere/rette det rå konverteringsresultatet i
   `src/tmp/` før det landar i `src/linkml/` — nyttig for større eller uvanlege
   JSON Schema. Det nye flagget er eit tillegg, ikkje ei erstatning (jf. Steg 5).

## Prioritert handlingsliste

| # | Steg | Fil |
|---|---|---|
| 1 | Utvid target-signatur | `make/70-scaffolding.mk` |
| 2 | Grein `--input-format` på nytt argument | `src/assets/scripts/scaffolding/new-modell.sh` |
| 3 | Generaliser PascalCase-rename til alle stub-klassar + containerklasse | `src/assets/scripts/scaffolding/new-modell.sh` |
| 4 | Verifiser/juster `id`-slot-fjerning for multi-klasse-modellar | `src/assets/scripts/scaffolding/new-modell.sh` (sjå Opne spørsmål #2) |
| 5 | Bryt ut delt dummy-instans-byggjar | `src/mcp-linkml-modell-utkast/validator.py` (eller ny `example_builder.py`) |
| 6 | Generer eksempelfil frå ferdig etterbehandla skjema | `src/assets/scripts/scaffolding/new-modell.sh` |
| 7 | Oppdater dokumentasjon | `COMMANDS.md`, `mkdocs/docs/kom-i-gang/ny-domenemodell.md` |
| 8 | Manuell verifisering | Køyr full flyt mot minst to av `src/tmp/*.schema.json` (t.d. `bvrfriv_lm_v1.schema.json`), samanlikn resultat mot dagens manuelt kopierte `enhetsregisteret-bvr*`-skjema |

## Avhengigheiter

- Ingen nye container-images.
- Ingen endring i MCP-serverens JSON-RPC-kontrakt (`generate_linkml`,
  `list_policies`) — alt gjenbruk skjer på eksisterande, allereie format-uavhengige
  parametrar.
- `validator.py` sin dummy-instans-logikk må gjerast importerbar frå
  `new-modell.sh` sin inline Python-blokk (anten via `PYTHONPATH` mot
  `src/mcp-linkml-modell-utkast/`, eller via same podman-basert kall-mønster som
  MCP-serveren allereie brukar for konvertering).

## Utført

Alle åtte handlingsliste-punkta er gjennomførte. To avvik frå den opphavlege
planen, begge oppdaga undervegs i implementering og testing:

1. **`slots.pop('id', None)`** (handlingsliste-punkt 4) vart verifisert
   **trygt å generalisere utan endring** — ikkje juster. Inspeksjon av
   `enhetsregisteret-bvrbekreftelse-schema.yaml` (JSON-schema-generert) viste
   at `id`-slotet der er **identisk** generisk boilerplate
   (`identifier: true, range: uriorcurie`) til det som vert popa i
   `--input-format empty`-vegen, injisert av same policy-mal uavhengig av
   input-format. Steget treng difor ingen input-format-gren.
2. **Eksempeldata-generering** (handlingsliste-punkt 5–6) enda opp enklare
   enn spec-en føreslo: i staden for å byggje ein separat
   `example_builder.py` (eller ei snapshot-omveg for å unngå eit
   importoppløysings-problem oppdaga undervegs), viste det seg at
   problemet allereie er eit kjent, dokumentert avvik —
   **BUG-15** (`bugs/relativ-import-via-versjonslast-url.md`) — med ein
   ferdig, testa monkeypatch-modul
   (`src/assets/scripts/utils/linkml_relative_import_patch.py`) alt brukt 5
   andre stader i repoet. Løysinga vart å (a) leggje ein CLI-inngang
   (`if __name__ == "__main__":`) rett i `validator.py`, som kallar
   `linkml_relative_import_patch.apply()` før `SchemaView` vert bygd, og (b)
   montere `src/assets/scripts/utils/` inn i den same podman-containeren
   `new-modell.sh` alt brukar. `bugs/relativ-import-via-versjonslast-url.md`
   er oppdatert med denne som sjette patcha kallestad, og med eit nytt,
   eksplisitt dokumentert gap: **`make validate-instance` er framleis ikkje
   patcha** (kallar `linkml`-CLI-binæren direkte, ikkje via eit
   Python-wrapper-skript) — stadfesta at dette er eit generelt, pre-
   eksisterande avvik (reprodusert på det tidlegare committa
   `oreg/javazonetalk/javazonetalk-schema.yaml`), ikkje noko denne spec-en
   innførte. Vurdert som eige, avgrensa endringsforslag utanfor scope her.
3. **Eit tredje, ikkje-planlagt funn** dukka opp under generalisering av
   PascalCase-steget (Steg 3): `to_pascal_case()` sin bruk av
   `str.capitalize()` per del er **ikkje idempotent** — kalla på eit namn
   som alt er korrekt PascalCase/camelCase utan `_`/`-` å splitte på (t.d.
   eit JSON-schema-avleidd klassenamn som `MeldingForEttersendingAvVedlegg`,
   eller sjølve containerklassenamnet frå MCP-serveren) øydelegg
   kasinga (`Meldingforettersendingavvedlegg`). Retta ved å byte
   `p.capitalize()` med `p[:1].upper() + p[1:]` (kun stor forbokstav per
   del, resten uendra) — idempotent, ingen regresjon for det opphavlege
   `empty`-input-bruksmønsteret (`generated` → `Generated`,
   `bvr-innfelles` → `BvrInnfelles` framleis korrekt).

**Testa mot to reelle JSON Schema-filer** (handlingsliste-punkt 8, ny scratch-
DOMAIN=zztest, sletta etter test):
`src/tmp/bvrettersendingavvedlegg_lm_v1.schema.json` og
`src/tmp/bvrfriv_lm_v1.schema.json`. Begge: `make lint` → 0 problem,
klassenamn/containerklasse korrekt PascalCase, eksempelfil generert med
reelle placeholder-verdiar (ikkje minimal-stub-fallback),
`make mcp-linkml-valider-modell` (den offisielt tilrådde «Neste steg»-
kommandoen) køyrer utan krasj. `--input-format empty`-vegen (utan
`JSON_SCHEMA`) verifisert uendra/framleis fungerande. Alle 44 eksisterande
einingstestar i `test_mcp_linkml_generator.py` passerer framleis.

**Endra filer:** `make/70-scaffolding.mk`, `src/assets/scripts/scaffolding/new-modell.sh`,
`src/mcp-linkml-modell-utkast/validator.py`, `COMMANDS.md`,
`mkdocs/docs/kom-i-gang/ny-domenemodell.md`, `bugs/relativ-import-via-versjonslast-url.md`.
