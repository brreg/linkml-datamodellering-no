# Rett rekkjefølge på nøklar i valideringslogg-JSON (fjern alfabetisk sortering)

## Bakgrunn

Brukaren bad tidlegare om at issues i valideringsresultatet frå
`make mcp-linkml-valider-modell` skulle visast med errors før warnings. Dette
vart implementert som `_sort_issues_by_severity()` i
`src/mcp-linkml-validator/server.py` (linje 33–41), kalla frå `validate_schema()`
(linje 950) og `validate_instance()` (linje 1053) — og fungerer korrekt: begge
funksjonane returnerer allereie `issues` som siste nøkkel i resultat-dict-en
(etter `valid`, `errorCount`, `warningCount`), og kvart issue-objekt har
felta i rekkjefølga `severity, code, target, message`.

Problemet er eit anna stad: `write_validation_log()` i
`src/assets/scripts/utils/validation_log.py` (linje 41–47) serialiserer heile
loggobjektet med `json.dumps(entry, indent=2, ensure_ascii=False, sort_keys=True)`.
`sort_keys=True` sorterer **alle** dict-nøklar rekursivt i alfabetisk
rekkjefølge — både topnivånøklane i `entry` (`schema`, `domain`, `version`,
`validation_policy`, `validated_at`, `result`) og nøklane inni `result`
(`valid`, `errorCount`, `warningCount`, `issues`) og inni kvart issue-objekt
(`severity`, `code`, `target`, `message`). Resultatet er at heile den fila
brukaren ser (`validation/<versjon>/<policy>.json`) verkar alfabetisk sortert,
sjølv om den *tiltenkte* severity-sorteringa av sjølve `issues`-**lista**
(rekkjefølga på elementa, ikkje nøklane) framleis er intakt under overflata —
`sort_keys` påverkar berre dict-nøkkelrekkjefølge, ikkje listeelement-rekkjefølge.

Dette var ikkje det brukaren ønskte. Ønskt åtferd: alle key-value-par utanom
`issues` skal visast først (i den rekkjefølga dei naturleg vert bygde), og
`issues` skal visast sist, sortert på severity (error før warning).

**Verifisert:** `build_validation_log_entry()` (validation_log.py:17–38) byggjer
allereie `entry` i rekkjefølga `schema, domain, version, validation_policy,
validated_at, result`. `validate_schema()`/`validate_instance()` i server.py
byggjer allereie `result` i rekkjefølga `valid, errorCount, warningCount,
issues` — altså `issues` sist. `issue()` (server.py:29–30) byggjer kvart
issue-objekt i rekkjefølga `severity, code, target, message`. Alt dette er
allereie i den ønskte rekkjefølga — einaste hindringa er `sort_keys=True` i
`write_validation_log()`.

**Merk:** `src/mcp-linkml-validator/validate-and-log.py` (linje 91–95) har
same `sort_keys=True`-mønster i eit strukturelt identisk `json.dump`-kall,
men er ein separat CLI-inngang som ikkje vert kalla av
`make mcp-linkml-valider-modell` (brukast direkte via
`python3 validate-and-log.py ...`). Held seg utanfor scope for dette
tiltaket sidan brukaren spesifikt nemnde `make mcp-linkml-valider-modell`,
men nemnast her slik at inkonsistensen er dokumentert dersom nokon støyter
på same problem via den inngangen seinare.

## Steg

1. Fjern `sort_keys=True` frå `json.dumps(...)`-kallet i `write_validation_log()`
   i `src/assets/scripts/utils/validation_log.py` (linje 45), slik at
   `entry`-dict-en (og alle nøsta dict-ar/lister i han) skriv i naturleg
   innsettingsrekkjefølge i staden for alfabetisk.
2. Køyr `make mcp-linkml-valider-modell SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml POLICY=silver`
   og inspiser den genererte `validation/<versjon>/silver.json` manuelt:
   verifiser at topnivånøklane står i rekkjefølga
   `schema, domain, version, validation_policy, validated_at, result`, at
   `result` har `issues` sist (etter `valid, errorCount, warningCount`), og
   at issue-objekta har `severity` først og er sorterte error-før-warning.
3. Ingen eksisterande testar verifiserer nøkkel- eller list-rekkjefølgje i
   valideringslogg-JSON-en (verifisert — ingen treff på `sort_keys` eller
   ordresjekk av `issues` i `tests/`), så ingen testoppdatering er naudsynt.

## Handlingsliste

- [x] Fjern `sort_keys=True` i `validation_log.py::write_validation_log()`
- [x] Manuell verifisering av generert `silver.json` for javazonetalk-skjemaet

## Utført

`sort_keys=True` fjerna frå `json.dumps()`-kallet i
`write_validation_log()` (`src/assets/scripts/utils/validation_log.py:45`).

Verifisert med
`make mcp-linkml-valider-modell SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml POLICY=silver`:
generert `src/linkml/oreg/javazonetalk/validation/0.1.0/silver.json` har no
topnivånøklane i rekkjefølga `schema, domain, version, validation_policy,
validated_at, result`, `result` har `issues` sist (etter `valid,
errorCount, warningCount`), og `issues`-lista er sortert error-før-warning
med kvart issue-objekt i rekkjefølga `severity, code, target, message`.

Ingen testar måtte oppdaterast (ingen eksisterande test verifiserte
nøkkel- eller listerekkjefølgje).
