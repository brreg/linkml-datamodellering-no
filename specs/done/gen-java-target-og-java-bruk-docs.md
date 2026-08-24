# make gen-java + "Java-bruk"-seksjon i Kom i gang

## Bakgrunn

Repoet har i dag `make gen-python` (LinkML sin `PythonGenerator`) som gjer det
enkelt å bruke ein modell frå Python-kode, med eit tilhøyrande "Python-bruk"-
eksempel i "Kom i gang"-seksjonen på kvar modell si `index.md`-side. Det
finst ingen tilsvarande veg inn for Java. LinkML 1.11.1 (versjonen bygd inn i
`docker.io`-biletet `src/assets/containers/Dockerfile.linkml`) leverer ein
`JavaGenerator` (`linkml.generators.javagen`, CLI-namn `gen-java`) som
genererer éin `.java`-fil per klasse/enum, med Lombok `@Data`-annotasjonar
(getters/setters/equals/hashCode) i standardmalen.

Målet er eit `make gen-java`-target som følgjer same batch-mønster som dei
andre reint LinkML-baserte generatorane (`gen-python`, `gen-proto`,
`gen-graphql` m.fl. — sjå `make/10-generator-macros.mk`), pluss ei ny
"Java-bruk"-underoverskrift i "Kom i gang" på **kvar** modell si `index.md`,
plassert rett før "Python-bruk". "Java-bruk" skal — i likskap med
"Python-bruk" i dag — visast **uavhengig** av om `java: true` er sett i
modellen sin `build.yaml` (det er eit generisk døme på korleis dei genererte
klassane *kan* brukast, ikkje eit bevis på at dei er generert i dette
konkrete bygget).

### Avklarte val (sjå spørsmål stilt til brukar 2026-08-24)

- **Java-package:** utleia automatisk frå skjemaet sin `id:`-URI via
  reversert domenenotasjon (standard Java-konvensjon, t.d. `com.example` for
  `example.com`). `https://data.norge.no/samt/samt-bu` →
  host `data.norge.no` reversert = `no.norge.data`, sti-segment
  `samt/samt-bu` (bindestrek fjerna) = `samt.samtbu` → fullt package
  `no.norge.data.samt.samtbu`. Ingen ny `build.yaml`-nøkkel treng leggjast
  til.
- **Aktivering (`java: true` i `build.yaml`):** dei same 11 skjemaa som alt
  har `python: true` i dag (speglar eksisterande mønster for "konkrete
  domenemodellar", ikkje AP-NO-baseprofilar):
  `samt-bu`, `referansemodell`, `referansemodell-bronze`,
  `referansemodell-gold`, `referansemodell-silver`, `oreg/javazonetalk`,
  `oreg/register-over-aksjeeiere`, `ngr-adresse`, `ngr-eiendom`,
  `ngr-person`, `ngr-virksomhet`.

## Steg

1. **`src/assets/scripts/makefile/batch-generate.py`** — registrer ny
   generator `"java"` i `REGISTRY`:
   - `module="linkml.generators.javagen"`, `flag="java"`,
     `out_suffix=None` (`JavaGenerator.serialize()` skriv sjølv `.java`-filer
     til `--output-directory`, same mønster som `"doc"`)
   - ny `extra_argv_fn=_java_extra_argv(domain, name)` som:
     - opprettar `$(GEN_DIR)/<domain>/<name>/java/`
     - les `id:`-feltet frå `src/linkml/<domain>/<name>/<name>-schema.yaml`
     - bereknar Java-package via ein ny hjelpefunksjon
       `_java_package_from_id(schema_id)` (reversert domene + sti-segment
       med bindestrek fjerna, sjå algoritme over)
     - returnerer `["--output-directory", <sti>, "--package", <package>]`
   - oppdater modul-docstringen sin `<kind>:`-liste (linje ~38) med `java`
   - oppdater kommentaren i `REGISTRY`-header (linje ~6-14, lista over reint
     linkml-baserte batcha generatorar) med `java`

2. **`make/11-generator-targets.mk`** — legg til
   `$(eval $(call make_gen_target,gen-java,run_gen_parallel,java))` saman
   med dei andre `make_gen_target`-kalla, og ei hjelpetekstlinje
   `gen-java: ## Generer Java-klassar [DOMAIN=<domene>|SCHEMA=<sti>]`.

3. **`make/10-generator-macros.mk`** — legg `java` til i kommentaren over
   `run_gen_parallel` (linje ~30, "dekkar generatorar utan spesiell
   etterhandsaming (jsonld-context, python, json-schema, proto)").

3b. **`src/assets/scripts/makefile/run-domain-pipeline.sh`** og
    **`make/20-domain-targets.mk`** — legg `gen-java` til i Fase 1-lista
    (saman med `proto`/`graphql`), elles køyrer `domain-<domain>` aldri
    `gen-java` sjølv om `java: true` er sett i `build.yaml` (oppdaga under
    gjennomgang, ikkje i det opphavlege steglista — `gen-java` er, i likskap
    med `gen-graphql`, IKKJE del av `domain_target`-pipelinen berre fordi
    generatoren finst i `REGISTRY`).

4. **11 `build.yaml`-filer** — legg til `java: true` under `generators:` i
   dei 11 skjemaa lista under "Avklarte val" over (same stad som
   `python: true` står i dag).

5. **`mkdocs/lib/copy_artifacts.sh`** — kopier `java/`-underkatalogen
   (dersom han finst i `$schema_dir`) til `$out/java/`, same mønster som
   `diagrams/`-blokka (linje ~46-50).

6. **`mkdocs/lib/sections/generated_artifacts.sh`** — legg til ein ny
   artefakt-rad for Java-klassar (dersom `$out/java/*.java` finst), i stil
   med PlantUML-blokka: lenkjer til kvar `.java`-fil i katalogen, skilt med
   ` · `.

7. **`mkdocs/lib/scripts/collect-schema-metadata.py`** — i
   `read_schema_file()`: les `id:`-feltet (alt tilgjengeleg via `d`) og
   bereken Java-package med same algoritme som i steg 1 (implementert på
   nytt her — to identiske implementasjonar i to separate Python-skript som
   køyrer i kvar sin kontainar krev ikkje felles abstraksjon per DRY-regelen
   i `CLAUDE.md`, terskel er tre). Legg `java_package` til i returtuppelen
   og i `main()` sin `print(US.join([...]))`-linje.

8. **`mkdocs/lib/sections/kom_i_gang.sh`** — les det nye `java_package`-
   feltet frå metadata-linja (utvid `IFS=$'\x1f' read -r`-lista), legg til
   ei ny `### Java-bruk`-underoverskrift **rett før** `### Python-bruk`
   (linje 56), med:
   - eit `pom.xml`-utdrag som viser Lombok- og
     `jackson-dataformat-yaml`-avhengigheitene som trengst for å kompilere
     og lese YAML-data inn i dei genererte klassane
   - eit Java-kodeeksempel som importerer `$java_package.$example_class` og
     brukar `ObjectMapper(new YAMLFactory())` til å lese `mine-data.yaml`
     inn i `$example_class` — strukturelt parallelt med det eksisterande
     Python-eksempelet (`yaml_loader.load(...)`)

9. **`COMMANDS.md`** — legg til ei rad for `gen-java` i generator-tabellen
   (linje ~220-233), same format som `gen-proto`-rada.

10. **`mkdocs/docs/automasjon/artefakt-generering.md`** — legg til ei rad
    for Java i per-artefakt-tabellen (linje ~53-69), same format som
    Protobuf-rada, med `build.yaml`-flagg `java`.

11. **`make/README.md`** — legg `gen-java` til i lista over
    `batch-generate.py`-baserte targets (linje 34).

12. **Valider** — køyr `make gen-java SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`
    og stadfest at `.java`-filer vert generert med korrekt `package`-
    deklarasjon i `generated/samt/samt-bu/java/`. Køyr
    `make docs-publish` (eller tilsvarande lokalt steg) for éin modell og
    stadfest at `index.md` viser "Java-bruk" rett før "Python-bruk", og at
    artefakttabellen listar dei genererte `.java`-filene.

## Handlingsliste

- [x] Steg 1: `java`-generator registrert i `batch-generate.py`
- [x] Steg 2: `gen-java`-target i `make/11-generator-targets.mk`
- [x] Steg 3: kommentaroppdatering i `make/10-generator-macros.mk`
- [x] Steg 3b: `gen-java` lagt til Fase 1 i `run-domain-pipeline.sh`/`make/20-domain-targets.mk`
- [x] Steg 4: `java: true` i dei 11 relevante `build.yaml`-filene
- [x] Steg 5: `java/`-katalog kopiert i `copy_artifacts.sh`
- [x] Steg 6: Java-artefaktrad i `generated_artifacts.sh`
- [x] Steg 7: `java_package` bereikna i `collect-schema-metadata.py`
- [x] Steg 8: "Java-bruk"-seksjon i `kom_i_gang.sh` (før "Python-bruk")
- [x] Steg 9: `gen-java`-rad i `COMMANDS.md`
- [x] Steg 10: Java-rad i `mkdocs/docs/automasjon/artefakt-generering.md`
- [x] Steg 11: `gen-java` nemnd i `make/README.md`
- [x] Steg 12: validert med `make gen-java SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` (11 `.java`-filer generert, korrekt `package no.norge.data.samt.samtbu;`) og `make docs-publish` (Java-bruk-seksjon rett før Python-bruk stadfesta på `samt/samt-bu` og `ap-no/dcat-ap-no`, artefakttabell listar dei 11 genererte `.java`-filene for samt-bu, `make lint` framleis grøn)

## Utført

Alle 12 steg + tilleggssteg 3b gjennomførte 2026-08-24. Validert med:
- `make gen-java SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` — 11 `.java`-filer med korrekt `package no.norge.data.samt.samtbu;`, utleia frå `id: https://data.norge.no/samt/samt-bu`
- `LOGLVL=DEBUG make gen-java SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` — korrekt hoppa over (`java: true` ikkje sett for AP-NO-baseprofilar)
- `make lint SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` — framleis "✓ No problems found"
- `make docs-publish` (full køyring, 8 domene) — "Java-bruk" vises rett før "Python-bruk" på **alle** modellar (uavhengig av `java: true`, same mønster som "Python-bruk"), med korrekt utleia Java-package i importen (t.d. `no.norge.data.apno.dcatapno.Aktoer` for dcat-ap-no sjølv om `java: true` ikkje er sett der); artefakttabellen på `samt/samt-bu` listar dei 11 genererte `.java`-filene under "Java-klassar"
