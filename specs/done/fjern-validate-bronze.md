# Fjern `validate-bronze`

## Bakgrunn

Oppfølging av evalueringa av alle valideringstarget (same økt). For
`validate-bronze` (`make/40-validation.mk:41-76`) vart det stadfesta at
targetet er **logisk redundant by design**, ikkje berre ergonomisk
duplisert som `validate`/`validate-linkml-merge` var:

- Alle policyar (`silver`, `gold`, `felles-datakatalog`,
  `felles-begrepskatalog`) `extends: bronze`
  (`src/mcp-linkml-validator/policies/*.yaml`) — eit skjema som består
  sin eigen konfigurerte policy-sjekk (den CI alt køyrer via
  `run-validation.sh --manifest` i `generate.yml`) har alt bestått
  bronze i same køyring. Ein tvinga bronze-omkøyring gir null ny
  informasjon for silver/gold/felles-*-skjema, og er eit reint
  duplikat av CI for bronze-skjema.
- Empirisk stadfesta: **25 git-committed `bronze.json`-loggfiler**
  finst i `src/linkml/**/validation/**/bronze.json` for skjema med ein
  annan konfigurert policy — desse vert aldri lesne av portalen
  (`mkdocs/lib/utils/metadata_parsers.sh:get_validation_json_path`
  slår alltid opp `<konfigurert-policy>.json`), reine spor etter
  historiske manuelle køyringar.
- GH-annotasjonsemisjonen (`emit-github-validation-annotations.py`)
  er meiningslaus lokalt sidan `validate-bronze` aldri køyrer i CI.
- To dokumentasjonsreferansar til targetet er alt broten
  (`domain-validate-bronze` — eit namn som aldri har eksistert som
  target): `mkdocs/docs/publisering/publisering-modell.md:181` og
  `specs/backlog/rename-schema-til-linkml-yaml.md:239-240`.

Enkeltskjema-erstatning finst alt: `make mcp-linkml-valider-modell
SCHEMA=<sti> POLICY=bronze`.

Brukaren godkjente å (1) fjerne targetet, (2) rette dei to broke
dokumentasjonsreferansane, (3) rydde bort dei 25 foreldrelause
`bronze.json`-filene.

## Steg

1. Fjern `validate-bronze`-oppskrifta frå `make/40-validation.mk`.
2. Fjern referansen til `validate-bronze` frå `COMMANDS.md`.
3. Fjern referansen til `validate-bronze` frå
   `mkdocs/docs/kom-i-gang/kommandoar.md`.
4. Rett `mkdocs/docs/publisering/publisering-modell.md:181` —
   `domain-validate-bronze`-rada skildrar steget «Valider skjema mot
   validation_policy» i `validate.yml` (kallar `run-validation.sh`
   direkte, ikkje via eit `domain-validate-bronze`-target som aldri
   har eksistert).
5. Rett `specs/backlog/rename-schema-til-linkml-yaml.md:239-240` —
   `make domain-validate-bronze DOMAIN=<domene>` → korrekt
   `make validate DOMAIN=<domene>` (verifiser import-grafen, som var
   den opphavlege intensjonen — ikkje ein policy-sjekk).
6. Slett dei 25 identifiserte foreldrelause `bronze.json`-filene under
   `src/linkml/**/validation/**/bronze.json` der konfigurert
   `validation_policy` i tilhøyrande `build.yaml` ikkje er `bronze`.
7. Sjekk om nokon `validation/<versjon>/`-katalog vart tømt heilt av
   steg 6 (ingen attverande `.json`), og i så fall om den tomme
   katalogen skal fjernast (git sporar ikkje tomme katalogar, så dette
   er normalt sjølvsanerande).
8. Valider: `make -n validate-bronze` skal feile med "No rule to make
   target"; `git status` skal vise berre dei venta sletta/endra filene.

## Handlingsliste

- [x] Steg 1 — `make/40-validation.mk`
- [x] Steg 2 — `COMMANDS.md`
- [x] Steg 3 — `mkdocs/docs/kom-i-gang/kommandoar.md`
- [x] Steg 4 — `mkdocs/docs/publisering/publisering-modell.md`
- [x] Steg 5 — `specs/backlog/rename-schema-til-linkml-yaml.md`
- [x] Steg 6 — Slett foreldrelause `bronze.json`-filer
- [x] Steg 7 — Sjekk tomme katalogar
- [x] Steg 8 — Validering

## Utført

Alle åtte steg gjennomførte. I tillegg til dei planlagde stega vart tre
ekstra, direkte avleidde referansar oppdaga og retta under
verifiseringa (steg 8): `.PHONY`-lista i `Makefile`, ein
kommentar i `make/01-containers.mk` som brukte `validate-bronze` som
eksempel, og fil-toppkommentaren i `make/40-validation.mk` sjølv
(nemnde både `validate-bronze` og det no heilt ubrukte
`emit-github-validation-annotations.py`).

Faktisk tal sletta `bronze.json`-filer vart **26**, ikkje 25 som i det
opphavlege overslaget (manuell forteljing i evalueringa var av eitt).
Alle 26 vart stadfesta foreldrelause ved å samanlikne mot
`validation_policy` i tilhøyrande `build.yaml` i sanntid før sletting.
4 av dei resulterande tomme `validation/<versjon>/`-katalogane vart
fjerna (git sporar ikkje tomme katalogar uansett). Éin femte tom
katalog (`brreg-begrepskatalog/validation/1.5.0`) vart funnen, men
stadfesta upåverka av denne økta (ingen `git status`-endring der) og
difor ikkje rørt.

**Følgje-observasjon (ikkje utført, utanfor godkjent scope):**
`src/assets/scripts/makefile/emit-github-validation-annotations.py`
er no eit heilt ubrukt script — einaste kallaren var
`validate-bronze`. Vurder å fjerne det i eit seinare, eige steg dersom
brukaren ønsker det.

Verifisert:
- `make -n validate-bronze` → "No rule to make target 'validate-bronze'"
- `make help` viser ikkje `validate-bronze`
- Ingen attverande referansar til `validate-bronze` utanom arkiverte/historiske filer (`specs/done/`, `bugs/`, `BUGS.md`, `CHANGELOG.md`)
- `make validate SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` — ingen regresjon
