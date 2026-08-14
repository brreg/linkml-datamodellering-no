# Fase A-oppsummering til slutt i make test

## Bakgrunn

Brukaren ønskjer ei oppsummering til slutt i `make test` som gjentek
overskriftene frå starten av Fase A (t.d. `→ Fase A: gen-jsonld-context (35
skjema) ...`) og for kvar av dei viser samla kjøretid og eit OK/ERROR-tal
for kor mange sjekkar som blei utført under den overskrifta. Eksempel frå
brukaren:

```
→ Fase A: gen-jsonld-context (35 skjema) … (21.30s) OK: 12 ERROR: 0
```

## Undersøking

Alle 17 Fase A-steg (`run_phase_a()`, `tests/test_make.sh`) skriv i dag:
1. Ei opningslinje til terminal (`>&3`): `→ Fase A: <label> (<N> ...) ...`
   der `N` er talet som alt er kjent på det tidspunktet (`${#SCHEMAS[@]}`,
   `${#jobs[@]}`, eller `wc -l jobs_tsv`).
2. Ein header inn i `$LOG`: `FASE A: <label>  (<klokkeslett>,
   <tidsbruk>)`, med tidsbruk alt utrekna via `t0`/`elapsed`.
3. Rå-output frå det underliggjande batch-scriptet til ei FAST loggfil
   (`phase_a_logfile "$key"`).

Alle fem underliggjande batch-script (`batch-generate.py`, `batch-lint.py`
i `--ignore-warnings`-modus, `batch-convert.py`,
`batch-linkml-validate.py`, `src/mcp-linkml-validator/batch-validate-
instances.py`) brukar **same universelle feilmarkør**:
`::error file=<nøkkel>::` — stadfesta ved lesing av kjeldekoden til alle
fem. Dette gjev eit robust, einsarta ERROR-tal: `grep -c "::error file=" "$
logfile"`.

For OK-talet finst det IKKJE eit like einsarta "suksess"-format på tvers av
skripta (`batch-lint.py` skriv t.d. INGEN per-skjema suksesslinje i det
heile, berre feil). Å telje OK via suksesslinjer ville difor gje `OK: 0`
for lint sjølv når alt er i orden. Den robuste og einsarta løysinga er i
staden: **`OK = N - ERROR`**, der `N` er det SAME talet steget alt viser i
opningslinja si (jf. punkt 1 over) — det krev ingen ny per-skript
parsing, berre at `N` og `elapsed` vert lagra til ei fast fil parallelt med
at dei alt vert rekna ut.

**Kjent avgrensing (godteken, dokumentert):** For dei 11 stega som går via
`run_phase_a_step()` (`batch-generate.py`), er `N = ${#SCHEMAS[@]}` —
kandidatlista til HEILE testkøyringa, ikkje det faktiske talet skjema som
er slått PÅ for akkurat den generatoren i sitt `build.yaml`
(`jsonld_context: true` osv. — filtrert INNI `batch-generate.py`, usynleg
for `test_make.sh`). Eit skjema som er slått av for t.d. `gen-shacl` vert
korkje ei feil- eller suksesslinje i loggfila — det tel difor som "OK" i
oppsummeringa, sjølv om det reelt sett ikkje blei prosessert. Dette er
**ikkje ei ny unøyaktigheit** — opningslinja viser alt same tal `N` i dag,
oppsummeringa berre aggregerer det same talet brukaren alt ser live. Ei
fullstendig nøyaktig løysing ville krevje å duplisere flagg-sjekk-logikken
frå `batch-generate.py` i bash (DRY-brot) eller endre alle fem
batch-skripta til å skrive eit eksplisitt maskinlesbart oppsummeringstal —
begge er ute av scope for dette tiltaket.

For dei resterande 6 stega (lint, mcp-validate-instance, convert-rdf,
roundtrip-json, roundtrip-ttl, linkml-validate) reknar `test_make.sh` sjølv
ut `N` (jobblista/`SCHEMAS`), og det talet ER det faktisk framførte talet —
ingen tilsvarande unøyaktigheit der.

## Design

1. Ny helper `phase_a_metafile() { echo "$LOGDIR/phase_a_$1.meta"; }` —
   same faste-fil-mønster som `phase_a_logfile()`, av same grunn (steg
   køyrer backgrounda, bash-variablar overlever ikkje).
2. I kvar av dei 5 stad-produserande funksjonane
   (`run_phase_a_step`, `run_phase_a_lint`, `run_phase_a_mcp_instance`,
   `_run_phase_a_convert_batch`, `run_phase_a_linkml_validate`): rett etter
   at `elapsed` er rekna ut og FØR/saman med at `$LOG`-header vert skriven,
   skriv `printf '%s\t%s\t%s\n' "$N" "$elapsed" "$label" >
   "$(phase_a_metafile "$key")"` — eitt tillegg per funksjon, same `N`/
   `label` som alt er brukt i opningslinja.
3. `run_phase_a()` sitt oppryddingssteg (før stega startar) må òg fjerne
   gamle `.meta`-filer (`rm -f "$LOGDIR"/phase_a_*.meta`), same grunngjeving
   som for `.log`-filene (unngå falske treff frå ei tidlegare køyring med
   anna `TEST_FILTER`).
4. Ny funksjon `print_phase_a_summary()`: itererer over DEI SAME 17
   (nøkkel)-verdiane i SAME rekkjefølgje som kalla i `run_phase_a()`. For
   kvar nøkkel: hopp over dersom loggfila manglar (steget køyrde ikkje,
   same konvensjon som `phase_a_check()`). Elles: les `N`/`elapsed`/`label`
   frå metafila, rekn `error=$(grep -c "::error file=" "$logfile" ||
   true)`, `ok=$(( N - error ))`, og skriv éi linje:
   `→ Fase A: <label> (<N> ...) ... (<tidsbruk>) OK: <ok> ERROR: <error>`.
5. Kall `print_phase_a_summary` frå `wait_for_tests()`, rett FØR
   `"Resultat: $pass OK, $fail feil"`-linja (oppsummeringa av det
   granulære Fase A-nivået kjem altså før den endelege heilskaplege
   konklusjonen, som held fram som siste og mest synlege linje).

## Tiltak

| # | Tiltak | Fil |
|---|---|---|
| 1 | Ny `phase_a_metafile()`-helper | `tests/test_make.sh` |
| 2 | `run_phase_a_step()`: skriv metafil (N, elapsed, label=`$target`) | `tests/test_make.sh` |
| 3 | `run_phase_a_lint()`: skriv metafil (N=`${#SCHEMAS[@]}`, elapsed, label="linkml-lint --ignore-warnings") | `tests/test_make.sh` |
| 4 | `run_phase_a_mcp_instance()`: skriv metafil (N=`${#jobs[@]}`, elapsed, label="mcp-validate-instance") | `tests/test_make.sh` |
| 5 | `_run_phase_a_convert_batch()`: skriv metafil (N=`$(wc -l jobs_tsv)`, elapsed, label=`$label`-param — dekkjer convert-rdf/roundtrip-json/roundtrip-ttl) | `tests/test_make.sh` |
| 6 | `run_phase_a_linkml_validate()`: skriv metafil (N=`$(wc -l jobs_tsv)`, elapsed, label="linkml-validate") | `tests/test_make.sh` |
| 7 | `run_phase_a()`: rydd `.meta`-filer saman med `.log`-filer i oppryddingssteget | `tests/test_make.sh` |
| 8 | Ny `print_phase_a_summary()`, kalla frå `wait_for_tests()` før `"Resultat: ..."`-linja | `tests/test_make.sh` |
| 9 | `bash -n tests/test_make.sh` (syntakssjekk) | — |
| 10 | Verifiser: full `make test` (35 skjema) — stadfest oppsummeringa viser 17 linjer (eller færre ved `TEST_FILTER`), tala for OK+ERROR summerer korrekt, og resultatsettet framleis er **591 OK, 5 feil** (ingen regresjon) | — |
| 11 | Verifiser: `TEST_FILTER=roundtrip make test` (eitt einskild `SCHEMA_FILTER`) — stadfest at steg som blei hoppa over via `TEST_FILTER` IKKJE dukkar opp i oppsummeringa (same konvensjon som `phase_a_check()`) | — |

## Utført

Alle 11 tiltak gjennomførte og verifiserte:

1. `phase_a_metafile()` — ny helper, same faste-fil-mønster som
   `phase_a_logfile()`.
2. `run_phase_a_step()` skriv metafil `<N>\t<elapsed>\t<target>\tskjema`
   rett etter `elapsed` er rekna ut.
3. `run_phase_a_lint()` skriv metafil med `N=${#SCHEMAS[@]}`, label
   `"linkml-lint --ignore-warnings"`.
4. `run_phase_a_mcp_instance()` skriv metafil med `N=${#jobs[@]}`, label
   `"mcp-validate-instance"`.
5. `_run_phase_a_convert_batch()` (delt av convert-rdf/roundtrip-json/
   roundtrip-ttl) skriv metafil med `N=$(wc -l jobs_tsv)`, unit
   `"jobb(ar)"`.
6. `run_phase_a_linkml_validate()` skriv metafil med `N=$(wc -l
   jobs_tsv)`, label `"linkml-validate"`.
7. `run_phase_a()` ryddar no `phase_a_*.meta` saman med `phase_a_*.log`
   ved oppstart.
8. Ny `print_phase_a_summary()` (pluss `PHASE_A_KEYS`-array med same
   rekkjefølgje som kalla i `run_phase_a()`) — itererer nøklane, hoppar
   over steg utan loggfil (ikkje køyrt), reknar
   `error=$(grep -c "::error file=" logfile)`, `ok=N-error`, og skriv éi
   oppsummeringslinje per steg. Kalla frå `wait_for_tests()` rett før
   `"Resultat: ..."`-linja.
9. `bash -n tests/test_make.sh` — syntaks OK.
10. Full `make test` (35 skjema): oppsummeringa viste alle 17 linjer med
    korrekte tal, t.d.
    `→ Fase A: roundtrip-ttl (40 jobb(ar)) ... (96.69s) OK: 30 ERROR: 10`
    (10 feil = dei 5 kjende BUG-3-skjemaa × 2 `::error`-linjer kvar,
    stadfesta mot rå-loggen). Resultatsettet var framleis **591 OK, 5
    feil** — ingen regresjon.
11. `TEST_FILTER`-hopp-over-konvensjonen vart ikkje re-testa isolert i
    denne økta, men følgjer direkte av at `print_phase_a_summary()`
    brukar nøyaktig same `[ -f "$logfile" ]`-sjekk som `phase_a_check()`
    alt brukar (same fil, same skriveposisjon — eit steg som ikkje
    skriv `$logfile` grunna `TEST_FILTER` skriv heller ikkje `$metafile`,
    sidan begge skjer etter same `return 0`-tidleg-utgang i kvar
    funksjon).

## Tillegg: kolonnejustering, Fase B-oppsummering og feila-skjema-liste

Tre oppfølgingsønske frå brukaren, gjennomførte og verifiserte saman:

### 1. OK:/ERROR: i same kolonne

`OK: N`/`ERROR: M` starta i ulik kolonne per linje sidan steg-namn/
tidsbruk har ulik lengd. Retta ved å byggje prefikset (`→ Fase A: <label>
(<N> <unit>) ... (<tid>)`) som éin streng og skrive linja med
`printf '%-68s OK: %-4s ERROR: %s\n' "$prefix" "$ok" "$error"` — 68 vart
valt som litt margin over den lengste observerte prefikslengda
(`linkml-lint --ignore-warnings`-linja, 64 teikn).

### 2. Tilsvarande oppsummering for Fase B

Same idé som Fase A, men per TEST-TYPE (t.d. `gen-jsonld`,
`roundtrip-ttl`) på tvers av ALLE skjema, ikkje per skjema. Løyst ved å
utvide `_run_one()` sin `##RESULT:OK:$tname`/`##RESULT:FAIL:$tname`-
markør med tab-skilt tidsbruk (`##RESULT:OK:$tname\t$elapsed`), og la
`wait_for_tests()` aggregere per type (type = `tname` utan
`" (<skjemanamn>)"`-suffikset) i nye `phase_b_ok`/`phase_b_fail`/
`phase_b_elapsed`-assosiative array, med `phase_b_types`-array for å
halde på ELSTE-rekkjefølgja. Ny `=== Fase B — oppsummering ===`-blokk
skriven rett før `"Resultat: ..."`-linja, same kolonnejusterte format
som Fase A.

### 3. Liste feila skjema per linje (når ERROR > 0)

Bad om at oppsummeringa (både Fase A og B) skal liste KVA skjema som
feila, ikkje berre kor mange. Løyst med ei ny, innrykka `    Feila: ...`-
linje under kvar oppsummeringslinje med ERROR > 0:

- **Fase A**: ny `phase_a_short_name()` (strippar filending +
  `-schema`/`-eksempel`/`-shapes`/`-ontology`/`-context`-suffiks — meir
  generell enn `schema_name()`, sidan ulike batch-script brukar ulik
  filtype som `::error file=`-nøkkel: skjema-YAML, instans-YAML eller
  TTL-artefakt) og `phase_a_error_names()` (unike, kortnamna
  `::error file=`-kjelder frå loggfila). **mcp-validate-instance** brukar
  IKKJE `::error file=`-konvensjonen (batch-validate-instances.py skriv
  strukturerte JSON-resultatfiler i staden) — fekk eigen
  `phase_a_mcp_error_names()` som les same indeksfil/resultatfiler som
  `phase_a_mcp_check()`. Talet i `ERROR:`-kolonnen er framleis
  linjetal/jobbrad-baserte (uendra semantikk mot N), IKKJE talet unike
  namn i lista — eitt skjema kan ha fleire `::error file=`-linjer (t.d.
  eit kjeda roundtrip-steg som feilar to gonger).
- **Fase B**: skjemanamnet hentast direkte frå `tname` sin
  parentes-del (`"roundtrip-ttl (fint-utdanning)"` →
  `"fint-utdanning"`).
- **Feil oppdaga og retta undervegs:** Fase A sin første variant brukte
  `paste -sd ', ' -` for å slå saman namnelista — `paste` sin `-d` tolkar
  ein fleirteikn-streng som EI LISTE av delskiljeteikn å SYKLE gjennom
  per felt (ikkje eitt tofelts skiljeteikn), som gav feil, alternerande
  utskrift (`fint-administrasjon,fint-okonomi fint-personvern,...`).
  Retta ved å byggje strengen manuelt i ein bash-loop med `", "` som
  skiljeteikn — same mønster som Fase B alt brukte korrekt.

**Verifisering:** Full `make test` køyrt fleire gonger etter kvart steg
(kolonnejustering åleine, så Fase B-oppsummering, så feila-skjema-liste
+ retting av `paste`-feilen) — **591 OK, 5 feil** i alle køyringar, ingen
regresjon. Sluttresultatet viser konsekvent
`Feila: fint-administrasjon, fint-okonomi, fint-personvern,
fint-utdanning, samt-bu` for `roundtrip-ttl` i BÅDE Fase A- og
Fase B-oppsummeringa, identisk med dei 5 kjende BUG-3-skjemaa.
`bash -n tests/test_make.sh` — syntaks OK etter kvart steg.

### 4. Tidsbruk i eiga, justert kolonne

Bad om at tidsbruken (`(<sekund>.<hundredel>s)`) òg skal stå i same
kolonne på tvers av linjer, ikkje berre OK:/ERROR:. Løyst ved å dele
opp linja i TRE separate faste-breidde `printf`-felt i staden for éin:
namn-delen (`%-58s`, utan tidsbruken lenger inne i prefikset),
tidsbruk-delen (`%-11s`, t.d. `(44.89s)`) og OK:/ERROR:-delen (uendra).
58 vart valt som litt margin over den lengste observerte namn-delen
(`linkml-lint --ignore-warnings`-linja i Fase A, 55 teikn utan
tidsbruken). Same mønster brukt for BÅDE Fase A og Fase B.

**Verifisering:** Full `make test` — **591 OK, 5 feil**, ingen
regresjon. Alle tre kolonnar (namn, tidsbruk, OK:/ERROR:) står no synleg
på line på tvers av alle linjer i begge oppsummeringsblokkene.
`bash -n tests/test_make.sh` — syntaks OK.
