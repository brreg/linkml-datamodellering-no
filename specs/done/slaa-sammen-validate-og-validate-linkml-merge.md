# Slå saman `validate` og `validate-linkml-merge`

## Bakgrunn

Brukaren bad om ei evaluering av alle valideringstarget for å finne
kandidatar til samanslåing/fjerning (oppfølging av ei tilsvarande
evaluering av `validate-instance`/`validate-data`/`validate-examples`
tidlegare i same økt). Evalueringa fann at `validate`
(`make/40-validation.mk:22`) og `validate-linkml-merge`
(`make/11-generator-targets.mk:29,54`) er **funksjonelt identiske**:

- Begge kallar til sjuande og sist same makro,
  `run_gen_linkml_parallel` (`batch-generate.py --generator merge`,
  fail-fast merge-imports-validering, ingen fil skriven).
- `validate` sitt fallback-uttrykk når `SCHEMA` ikkje er sett
  (`$(SCHEMAS)`) er identisk med kva `get_target_schemas`
  (brukt av `validate-linkml-merge`) fell tilbake til når verken
  `SCHEMA` eller `DOMAIN` er sett.
- Einaste reelle skilnaden er at `validate-linkml-merge` i tillegg
  støttar `DOMAIN=<domene>` — noko `validate` manglar i dag.

`validate` er det dokumenterte front-door-kommandoet
(`README.md`/`mkdocs/docs/kom-i-gang/kommandoar.md`), medan
`validate-linkml-merge` primært er pipeline-intern (kalla frå
`src/assets/scripts/makefile/run-domain-pipeline.sh` som Fase 1-steget
i `domain-<domene>`-pipelinen) og sjeldan kalla frittståande av
menneske. Brukaren godkjente forslaget om å behalde `validate`-namnet
som kanonisk og fjerne `validate-linkml-merge`.

## Steg

1. Legg til `DOMAIN=`-støtte i `validate` (`make/40-validation.mk`) ved
   å bruke `get_target_schemas`-makroen i staden for det noverande
   `$(if $(SCHEMA),$(SCHEMA),$(SCHEMAS))`-uttrykket.
2. Fjern `validate-linkml-merge` frå `make/11-generator-targets.mk`
   (generator-eval-linja og hjelpetekst-linja).
3. Oppdater `src/assets/scripts/makefile/run-domain-pipeline.sh` til å
   kalle `validate DOMAIN="$domain"` i staden for
   `validate-linkml-merge DOMAIN="$domain"`.
4. Oppdater kommentaren i `make/20-domain-targets.mk` (Fase 1-lista)
   frå `validate-linkml-merge` til `validate`.
5. Oppdater `COMMANDS.md`: slå saman dei to radene til éi rad for
   `make validate [DOMAIN=<domene>|SCHEMA=<sti>]`, fjern det no
   ubrukte ankeret `<a id="validate-linkml-merge">` (verifisert ingen
   inngåande lenkjer til det).
6. Oppdater referansen i `bugs/relativ-import-via-versjonslast-url.md`
   frå `validate-linkml-merge` til `validate`.
7. Oppdater `mkdocs/docs/kom-i-gang/kommandoar.md` sin `make
   validate`-rad til å nemne `DOMAIN=`-støtte.
8. Valider: `make validate SCHEMA=<eit skjema>`, `make validate
   DOMAIN=<eit domene>`, `make -n domain-<domene>` (stadfest pipelinen
   framleis refererer eit gyldig target).

## Handlingsliste

- [x] Steg 1 — `make/40-validation.mk`
- [x] Steg 2 — `make/11-generator-targets.mk`
- [x] Steg 3 — `run-domain-pipeline.sh`
- [x] Steg 4 — `make/20-domain-targets.mk`
- [x] Steg 5 — `COMMANDS.md`
- [x] Steg 6 — `bugs/relativ-import-via-versjonslast-url.md`
- [x] Steg 7 — `mkdocs/docs/kom-i-gang/kommandoar.md`
- [x] Steg 8 — Validering

## Utført

Alle sju steg gjennomførte som planlagt. `validate-linkml-merge` er
fjerna som eige target — `validate` er no einaste kommandoen for
merge-imports-validering, med `DOMAIN=`/`SCHEMA=`-støtte via
`get_target_schemas`-makroen (same mekanisme som dei andre `gen-*`-
targeta).

Verifisert:
- `make validate SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` — OK
- `make validate DOMAIN=samt` — OK
- `make -n domain-samt` viser at pipelinen no kallar `make validate DOMAIN=samt` (tidlegare `validate-linkml-merge`)
- `make help` viser `validate [DOMAIN=<domene>|SCHEMA=<sti>]`, ingen spor av `validate-linkml-merge`
- Ingen attverande referansar til `validate-linkml-merge` utanom denne specen og det arkiverte (urørte) `specs/done/make-target-namn-vs-funksjon.md`
- Ingen genererte artefakt vart skrivne av testkøyringane (`validate` skriv ikkje fil, som forventa)
