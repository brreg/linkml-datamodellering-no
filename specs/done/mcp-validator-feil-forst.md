# List errors før warnings i MCP-validator-output

## Bakgrunn

Brukaren spurde om det er enkelt å endre `make mcp-linkml-valider-modell`
til å liste ut feil (errors) først. Undersøking av
`src/mcp-linkml-validator/server.py` viste at `validate_schema()`
(linje ~939-945) og `validate_instance()` (linje ~1041-1047) alt
splittar `issues` i separate `errors`/`warnings`-lister for å telje
`errorCount`/`warningCount` — men `"issues"`-feltet i det returnerte
resultatet brukar framleis den **usorterte** originallista, i den
rekkjefølga policy-sjekkane vart køyrde i. Praktisk konsekvens
(stadfesta empirisk mot `src/linkml/samt/samt-bu/validation/1.0.0/
silver.json`): dei to reelle `error`-oppføringane ligg sist i ei liste
på 39 oppføringar, bak 37 `warning`-oppføringar — lett å oversjå ved
manuell gjennomlesing av `make mcp-linkml-valider-modell`-output.

Dette er ein reint presentasjonsendring — `errorCount`/`warningCount`
og kva som vert flagga som issue er uendra, berre rekkjefølga i
`issues`-arrayet. Ingen indeksbaserte assertions på `issues[N]` finst i
`tests/test_mcp_policies.py` (alle sjekkar brukar `any()`/filter), så
endringa er trygg.

## Steg

1. Legg til ein delt sorteringskonstant (`error` → 0, `warning` → 1,
   alt anna → 2, t.d. `info` frå linter/instansvalidering) rett etter
   `issue()`-hjelpefunksjonen i `server.py`.
2. Sorter `issues` med denne rekkjefølga (stabil sort — behald
   original rekkjefølge innanfor same alvorsgrad) rett før
   retur-dictet i `validate_schema()`.
3. Same sortering i `validate_instance()`.
4. Valider: `make mcp-linkml-valider-modell-test` (køyrer
   `tests/test_mcp_policies.py`) skal framleis passere uendra.
5. Valider manuelt mot eit skjema med kjende feil+åtvaringar
   (`samt-bu`) at errors no ligg først i output.

## Handlingsliste

- [x] Steg 1-3 — `src/mcp-linkml-validator/server.py`
- [x] Steg 4-5 — Validering

## Utført

Sortering implementert som planlagt: `_SEVERITY_SORT_ORDER` +
`_sort_issues_by_severity()` (stabil sort) lagt til rett etter
`issue()`-hjelpefunksjonen, kalla i begge `validate_schema()` og
`validate_instance()` rett før `errors`/`warnings` vert utleia.

Verifisert:
- `make mcp-linkml-valider-modell SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml POLICY=silver` — dei 8 errors ligg no først, dei 8 warnings sist (tidlegare spreidd/usortert)
- `make mcp-linkml-valider-modell-test`: eitt testfeil (`TestGold.test_gyldig_skjema_har_ingen_feil`, `errorCount 2 != 0`) — stadfesta **føreeksisterande** ved `git stash`/gjenkøyring av testsuiten mot uendra `server.py`, altså urelatert til denne endringa. Ikkje retta som del av denne oppgåva (utanfor scope, angår sjølve gold-policy-reglane, ikkje issue-sorteringa).
