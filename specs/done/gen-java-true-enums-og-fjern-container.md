# gen-java: --true-enums og fjern containerklasse-fila

## Bakgrunn

`make gen-java` (registrert i `src/assets/scripts/makefile/batch-generate.py`,
sjå `specs/done/gen-java-target-og-java-bruk-docs.md`) genererer i dag Java-
klassar via `linkml.generators.javagen` med berre `--output-directory` og
`--package` som ekstra argument. To forbetringar er ønskte:

1. **`--true-enums`** — `JavaGenerator` sitt CLI-flagg
   `--true-enums/--no-true-enums` (standard `False` i sjølve linkml-pakken,
   sjå `linkml/generators/javagen.py`) styrer om LinkML-`enum`-typar vert
   generert som eigne Java-`enum`-typar (`--true-enums`) eller som vanlege
   strengar (standard). Strengbasert representasjon gjev ingen
   kompileringstids-typetryggleik for gyldige verdiar — ønskt oppførsel er
   ekte Java-enums.

2. **Containerklasse-fila** — per `.claude/rules/linkml-schema.md` §
   Containerklasse er containerklassen (`tree_root: true`,
   namnemønster `<Domene>Container`) «eit serialiseringsankerpunkt, ikkje ein
   semantisk klasse». `DocGenerator`-outputen filtrerer alt vekk
   Container-referansar frå `index.md` via `_doc_post()` (strengmatch på
   `"Container"` i genererte linjer). `JavaGenerator` har ikkje tilsvarande
   filter — containerklassen sin `.java`-fil (t.d. `SamtBuContainer.java`)
   vert generert saman med dei semantisk relevante klassane, men har ingen
   praktisk bruk i Java (containeren sitt einaste føremål er YAML/JSON/RDF-
   serialisering via LinkML sjølv, ikkje eit Java-API).

### Avklarte val

- `--true-enums` vert **alltid** aktivert for `gen-java` (ingen ny
  `build.yaml`-brytar) — same mønster som OWL/SHACL sine faste
  `default_extra_argv` (t.d. `--skip-vacuous-local-range-axioms` for owl).
- Containerklassen identifiserast **via skjemaet** (`tree_root: true` i
  `classes:`), ikkje via eit filnavn-mønster (`*Container.java`) — meir
  robust enn strengmatch, og krev ikkje at namnekonvensjonen
  `<Domene>Container` held 100 % (sjølv om ho gjer det i dag, jf.
  `.claude/rules/linkml-schema.md`).

## Steg

1. **`src/assets/scripts/makefile/batch-generate.py`** — `REGISTRY["java"]`:
   - legg til `default_extra_argv=["--true-enums"]` (kombinerast med
     eksisterande `extra_argv_fn=_java_extra_argv` — begge argv-listene vert
     slått saman i `_build_argv()`, sjå linje ~262-271)
   - ny funksjon `_java_post(domain: str, name: str) -> None`: les
     `src/linkml/<domain>/<name>/<name>-schema.yaml`, finn klassen(e) med
     `tree_root: true` i `classes:`, og slett tilhøyrande
     `$(GEN_DIR)/<domain>/<name>/java/<Klassenavn>.java` dersom fila finst
     (`Path.unlink(missing_ok=True)`) — same funksjonssignatur/mønster som
     `_doc_post`
   - legg `post_fn=_java_post` til `REGISTRY["java"]`

2. **Valider**:
   - `make gen-java SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` —
     stadfest at ingen `SamtBuContainer.java` finst i
     `generated/samt/samt-bu/java/` etter køyring, og at minst éin genererte
     `.java`-fil for ein `enum`-slot i skjemaet no er ein Java-`enum`
     (`public enum ... { ... }`) i staden for eit `String`-felt/type
   - `make lint SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` —
     framleis grøn (ingen skjemaendring, berre generator-argument)
   - stadfest at `mkdocs/lib/sections/generated_artifacts.sh` sin
     Java-artefaktrad (frå `specs/done/gen-java-target-og-java-bruk-docs.md`
     steg 6) ikkje lenger listar containerklassen si `.java`-fil

## Handlingsliste

- [x] Steg 1: `--true-enums` og `_java_post()` (containerklasse-filtrering) i `batch-generate.py`
- [x] Steg 2: validert med `make gen-java` + `make lint` på samt-bu, stadfesta at Container-fila er borte og enum-felt er ekte Java-enums

## Utført

`default_extra_argv=["--true-enums"]` og ny `post_fn=_java_post` (slettar
`<Klassenavn>.java` for klassen med `tree_root: true`) lagt til
`REGISTRY["java"]` i `batch-generate.py`. Validert 2026-08-24:
`make gen-java SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` — ingen
`SamtBuContainer.java` i `generated/samt/samt-bu/java/`, `ADMSStatus.java`
(og dei andre enum-filene) er no ekte `public enum` med
`@JsonCreator`/`fromString` i staden for strengfelt. `make lint` framleis
"✓ No problems found". `mkdocs/lib/sections/generated_artifacts.sh` sin
Java-rad globbar `*.java` i outputkatalogen direkte, så containerklassen
fell automatisk ut av artefakttabellen utan eiga endring der.
