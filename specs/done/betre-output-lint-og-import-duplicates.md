# Plan: menneskeleg-lesbar positiv/negativ output frå `make lint` og `make check-import-duplicates`

## Bakgrunn

Brukaren peika på to manglar i terminal-output frå desse to make-måla:

1. `make check-import-duplicates` gir i dag **ingen** output i det heile ved
   suksess — verken positiv stadfesting ("ingen kollisjonar funne") eller
   noko anna. Ein brukar som køyrer målet må stole blindt på exit-koden for
   å vite om sjekken faktisk køyrde og fann noko.
2. `make lint` skriv i dag `✓ No problems found` ved suksess. Brukaren
   opplever teksten som for generisk og ville forventa noko meir i retning
   av "Schema is valid".

Brukaren ba om ei evaluering av dagens output frå begge måla og eit forslag
til forbetring — denne specen dekkjer punkt 3 i arbeidsflyten (spesifikasjon
før utføring); ingen kode er endra enno.

## Evaluering av dagens output

### `make check-import-duplicates` (`src/assets/scripts/makefile/check-import-duplicates.py`)

- **Suksess:** `main()` returnerer `0` utan å skrive noko som helst, korkje
  til stdout eller stderr (linje 90-100). Total stille.
- **Feil:** allereie god — `log_error()` (linje 58-59) skriv
  `[ERROR] ::error file=<sti>::dublett-navn '<navn>' finst i to skjema i
  importkjeda (...) — gi det lokale elementet eit meir spesifikt navn
  (...)` — presis, handlingsretta, på norsk.
- **Konklusjon:** einaste mangelen er fråveret av eit positivt suksess-svar.

### `make lint` (`src/assets/scripts/makefile/batch-lint.py`)

- Scriptet er ein tynn wrapper rundt linkml sine **eigne** vendored
  klassar `linkml.linter.linter.Linter` og
  `linkml.linter.formatters.TerminalFormatter` — same klassar CLI-en
  (`linkml lint`) sjølv byggjer på (jf. moduldocstring linje 12-15). Det er
  desse klassane, ikkje vårt eige script, som skriv `✓ No problems found`
  (`TerminalFormatter.end_report()`, engelsk, `click.style`-grønfarga).
- **Viktig arkitektur-detalj:** `batch-lint.py` køyrer éin delt
  `Linter`/`TerminalFormatter`-sesjon for **alle** skjema i lista (linje
  80-114) — `end_report()` skriv difor **éi** oppsummeringslinje for **heile
  batchen**, ikkje éi linje per skjema. `COMMANDS.md` (linje 154-155)
  skildrar i dag outputen som "OK/FEIL per skjema til stdout", som ikkje
  heilt stemmer med den faktiske åtferda for skjema **utan** problem — dei
  får ingen synleg linje i det heile, berre skjema **med** problem listast
  (schema-namn understreka + nivå + melding, linje 28-42 i
  `terminal_formatter.py`).
- **Feilcase er allereie funksjonelt godt:** per-skjema-lista med
  feil/åtvaringar er tydeleg og handlingsretta, berre på engelsk.
- **Viktig presisering til brukaren sitt forslag:** `"Schema is valid"`
  ville vore misvisande ordlyd for eit **lint**-resultat. `make lint`
  sjekkar stil-/konvensjonsreglar (`.linkmllint.yaml`) — ikkje strukturell
  skjemagyldigheit. Strukturell gyldigheit er jobben til `make validate`
  (som **også** køyrer `check-import-duplicates.py`, jf.
  `make/40-validation.mk` linje 21-30). Å skrive "Schema is valid" etter
  ein lint-køyring ville gitt eit feilaktig inntrykk av kva som faktisk vart
  sjekka. Sjå "Opne spørsmål" for føreslått alternativ ordlyd.
- Vi bør **ikkje** endre eller monkey-patche `TerminalFormatter` sjølv —
  han er upstream/vendored kode (installert via `pip`/kontainerbilete, ikkje
  ein fil i dette repoet), og å overstyre han aukar vedlikehaldskostnaden
  ved kvar linkml-oppgradering. Rett stad å leggje til forbetra tekst er i
  vårt **eige** script, som eit tillegg *etter* `formatter.end_report()` —
  same additive mønster som `--ignore-warnings`-grenen alt bruker (linje
  106-110: ein ekstra `::error file=`-linje lagt attmed, ikkje i staden
  for, linkml sin eigen output).

### Manglande farge-/nivå-plumbing (felles for begge script)

`make/01-containers.mk` sin `LINKML_RUN` (linje 23-32) sender i dag
`LOGLVL`, `CLR_STEP`, `CLR_RST` og `CLR_OK` inn i kontaineren (same mønster
som `batch-generate.py` alt les via `os.environ`, jf. linje 75-79 der).
`CLR_ERR` og `CLR_WARN` er **ikkje** vidareførte. Begge scripta i denne
specen brukar i dag berre eit hardkoda `[ERROR]`-prefiks utan farge og utan
noko `log_info()`-tilsvarande (LOGLVL-respekterande) funksjon for positiv
output — dei har ingen av dei bash-sida sine `LOG_FUNCTIONS`
(`log_info`/`log_debug`) tilgjengeleg, sidan dei er reine Python-script.

## Status — omfang for denne runda

Tiltak 3 (`batch-lint.py`/`make lint`) og 4 (exit-kode-invarianten som
gjaldt saman med 3) er **droppa** frå denne runda, jf. brukarens
avgjerd 2026-08-24. `make lint`-outputen rørast difor ikkje no — han
er framleis linkml sin eigen `TerminalFormatter`-tekst, uendra. Dei opne
spørsmåla i evalueringa som gjaldt lint-ordlyd og per-skjema-status for
`make lint` (sjå "Opne spørsmål" under) står difor også ved lag, uavklarte,
og gjeld ei eventuell seinare runde — ikkje denne. Berre
`check-import-duplicates` (tiltak 1, 2, 5, 6 under) er utført no.

## Forslag til tiltak

1. **`make/01-containers.mk`:** legg `-e CLR_ERR` til `LINKML_RUN` (same
   stad som dei eksisterande `-e CLR_STEP`/`-e CLR_OK`), slik at
   `check-import-duplicates.py` kan fargeleggje den negative
   oppsummeringslinja raudt. `CLR_WARN` er **ikkje** lagt til — han hadde
   berre ein konsument i det droppa lint-tiltaket (3), og ville vore ubrukt
   død kode i denne runda.

2. **`check-import-duplicates.py`:** legg til ein `log_info()`-funksjon
   (LOGLVL-respekterande, speglar `log_error()` sitt mønster og
   `batch-generate.py` sin `LOGLVL != "ERROR"`-sjekk) og skriv éi positiv
   linje til stdout når **ingen** skjema har kollisjonar:
   ```
   ✓ Ingen import-kollisjonar funne (N skjema sjekka)
   ```
   Feilcaset (eksisterande `::error file=`-linjer) held uendra — legg i
   tillegg til éi avsluttande oppsummeringslinje ved delvis/full feil
   (fleire skjema, nokre feila), t.d. `✗ N av M skjema har
   import-kollisjonar`, skriven til stderr via `log_error` (alltid synleg,
   jf. "Ingen stille feil"-prinsippet).

3. ~~`batch-lint.py`~~ — droppa, sjå "Status" over.

4. ~~Exit-kodar (tiltak-punkt)~~ — droppa som eige punkt, sjå "Status"
   over. Konstatert likevel som ufråvikeleg krav for tiltak 2:
   `check-import-duplicates.py` sin returkode (0/1) skal vere bit-for-bit
   uendra, berre tekstleg output endrar seg.

5. **`COMMANDS.md`:** oppdater rada for `make check-import-duplicates`
   (linje 163) til å skildre den faktiske nye outputen presist. Rada for
   `make lint` (linje 154-155) rørast **ikkje** i denne runda.

6. **Verifiser:**
   - `make check-import-duplicates` mot eit reint skjema — stadfest ny
     positiv linje, exit-kode 0.
   - `make check-import-duplicates` mot eit skjema med medvite (mellombels)
     namnekollisjon — stadfest eksisterande feilmelding uendra, ny
     oppsummeringslinje, exit-kode 1.

## Opne spørsmål (avklar med brukaren før implementering)

- **Ordlyd:** er `"Lint fullført utan merknadar"` ei god erstatning for
  brukaren sitt opphavlege forslag `"Schema is valid"`? Sjå grunngjeving i
  evalueringa over (lint ≠ strukturell validering). Alternativ:
  `"Ingen lint-brot funne"`.
- **Per-skjema-status for `make lint`:** ønskjer brukaren i staden ei
  **bokstaveleg** OK/FEIL-linje for **kvart einaste** skjema (også dei utan
  problem), slik `COMMANDS.md` sin noverande tekst antyder? Det krev meir
  enn ei tilleggslinje — `batch-lint.py` må då skrive sitt eige
  per-skjema-resultat i staden for å stole på at linkml sin
  `TerminalFormatter` berre listar skjema **med** problem. Vurdert som eige
  (større) tiltak, ikkje del av denne specen med mindre brukaren ønskjer
  det.
- **Synleg ved LOGLVL=ERROR?** Skal den nye positive linja alltid skrivast
  til stdout, eller stille ved `LOGLVL=ERROR` (default-nivået), i tråd med
  `log_info()`-mønsteret elles i repoet? Førebels forslag: gate på LOGLVL,
  for konsistens — men dette betyr at `make lint`/`make check-import-
  duplicates` køyrt med default `LOGLVL=INFO` frå kommandolinja alltid vil
  vise linja (default er `INFO`, jf. `make/00-settings.mk` linje 38), så i
  praksis synleg for vanleg interaktiv bruk uansett.

## Utført

Berre tiltak 1, 2, 5 og 6 (`check-import-duplicates`) er realiserte — tiltak
3/4 (`make lint`/`batch-lint.py`) er droppa frå denne runda, jf. "Status"
over. Alle opne spørsmål som gjeld lint står difor uavklarte og gjeld ei
eventuell ny spec seinare, ikkje denne.

- `make/01-containers.mk`: `-e CLR_ERR` lagt til `LINKML_RUN` (`CLR_WARN`
  medvite utelaten, jf. tiltak 1)
- `src/assets/scripts/makefile/check-import-duplicates.py`: ny
  `log_info()`-funksjon (LOGLVL-respekterande), `main()` skriv no
  `✓ Ingen import-kollisjonar funne (N skjema sjekka)` ved suksess (grøn,
  stdout) og `✖ N av M skjema har import-kollisjonar` ved feil (raud,
  stderr, i tillegg til dei eksisterande `::error file=`-linjene) —
  returkode uendra (0/1)
- `COMMANDS.md`: rada for `make check-import-duplicates` (linje 163)
  oppdatert til å skildre ny output. Rada for `make lint` uendra.
- Verifisert manuelt: `make check-import-duplicates SCHEMA=<reint skjema>`
  (positiv linje, kode 0) og mot eit mellombels skjema med medvite
  `beskrivelse`-namnekollisjon mot `common-ap-no-schema` saman med eit reint
  skjema (`1 av 2 skjema har import-kollisjonar`, kode 1). Testfila er
  sletta att etter verifisering, ingen spor att i repoet.
