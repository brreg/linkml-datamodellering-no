# Bug: `validate-informasjonsmodell-instance` peikar på ein utdatert sti

**ID:** BUG-11
**Status:** `løyst`
**Komponent:** `make/30-instances.mk`
**Oppdaga:** 2026-08-06
**Løyst:** 2026-08-06

## Symptom

`make validate-informasjonsmodell-instance SCHEMA=<sti>` feiler for praktisk
talt alle skjema med:

```
metadata/modelldcat.yaml eksisterer ikkje. Køyr først: make gen-informasjonsmodell-instance SCHEMA=...
```

— sjølv rett etter at `make gen-informasjonsmodell-instance SCHEMA=<same sti>`
faktisk har køyrt og produsert output.

## Rot-årsak

`generate-informasjonsmodell.py` skriv til `metadata/<modell>-manifest.yaml`
(éi fil per skjema — sjå `generate-informasjonsmodell.py:381-383`), men
`validate-informasjonsmodell-instance` (`make/30-instances.mk:72`) ser
framleis etter den gamle, delte stien `metadata/modelldcat.yaml`. Scriptet
sin eigen docstring (`generate-informasjonsmodell.py:13`) er heller ikkje
oppdatert og seier framleis "Skriv: metadata/modelldcat.yaml".

Navnemønsteret vart altså endra frå éi delt fil (`modelldcat.yaml`) til éi
fil per skjema (`<modell>-manifest.yaml`), utan at make-targetet eller
docstringen vart oppdatert til å følgje med.

Éin fil i repoet følgjer framleis det gamle navnemønsteret og gjer at
targetet "tilfeldigvis" fungerer for akkurat det skjemaet:
`src/linkml/ap-no/dqv-ap-no/metadata/modelldcat.yaml`.

## Berørte skjema

Alle skjema med `tree_root`/Informasjonsmodell-generering, bortsett frå
`dqv-ap-no` (sjå over). `validate-informasjonsmodell-instance` er strukturelt
broten for resten.

## Workaround

Ingen aktiv workaround nødvendig — targetet er **ikkje** kalla frå CI
(`generate.yml`/`validate.yml`, sjå `mkdocs/docs/automasjon/artefakt-generering.md` § 5),
berre eit manuelt utviklarverktøy. Bugen blokkerer difor ikkje bygg eller
publisering, men gjer targetet ubrukeleg som lokalt verifikasjonssteg.

## Løysing

Retta stien i `make/30-instances.mk:72` til å utleie `<modell>-manifest.yaml`
frå `SCHEMA` via `basename "$(SCHEMA)" -schema.yaml` (same utleiingsmønster
som `generate-informasjonsmodell.py` sjølv brukar for output-filnavnet), og
oppdaterte docstringen i `generate-informasjonsmodell.py:13` til å seie
`metadata/<modell>-manifest.yaml` i staden for `metadata/modelldcat.yaml`.

**Filer:** `make/30-instances.mk`, `src/assets/scripts/makefile/generate-informasjonsmodell.py`

Oppdaga under arbeid med `mkdocs/docs/automasjon/artefakt-generering.md` § 3.6.

### Utført (2026-08-06)

1. ✓ `make/30-instances.mk:71-73`: la til `MODELL_NAME=$(basename "$(SCHEMA)" -schema.yaml)`
   og endra `MODELLDCAT_YAML` til `$$SCHEMA_DIR/metadata/$$MODELL_NAME-manifest.yaml`.
2. ✓ `generate-informasjonsmodell.py:13`: retta docstring til
   `metadata/<modell>-manifest.yaml`.
3. ✓ Verifisert med `make validate-informasjonsmodell-instance SCHEMA=...` for
   `ngr-adresse`, `samt-bu` og `dqv-ap-no` (sistnemnde er skjemaet som
   tidlegare "tilfeldigvis" fungerte via den gamle stien) — alle tre gir no
   `✓ Full LinkML-validering OK` / `✓ Validering fullført`.
4. ✓ Status oppdatert til `løyst`.
