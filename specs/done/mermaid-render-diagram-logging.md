# Synleggjer diagramnamn og full oppsummering i mermaid-render-loggen

## Bakgrunn

Jobben `mermaid-render` i `.github/workflows/lenkje-og-mermaid-sjekk.yml`
(steget «Rendra kvar mermaid-blokk», line 144–183) skriv i dag ei
markdown-rapport (`mermaid-render-report.md`, éi rad per diagram med
Fil/Diagram #/Status) og ei totalsum-linje — men **berre** til
`$GITHUB_STEP_SUMMARY` (Summary-fana) og som opplasta artefakt. Sjølve
jobb-loggen (rå konsoll-output, det brukaren faktisk ser når dei feilsøkjer
via `gh run view --log` eller Actions-UI-et sin "Logs"-fane) inneheld berre
éin `::warning`-linje per feila diagram:

```bash
echo "::warning file=${src}::Mermaid-diagram nr. ${idx} rendrar ikkje: ${message}"
```

`file=${src}` set filnamnet som eit annotasjons-**attributt**, men det
attributtet syner ikkje i den rå tekstlogg-linja sjølv — berre `nr. ${idx}`
(diagramindeksen *innanfor* fila) og `${message}` (siste 5 linjer av
mermaid-cli sin feillogg) er synlege i loggteksten. To ulike diagram i to
ulike filer som begge feilar med same generiske Puppeteer-feil (som ofte
skjer, sidan feilloggen sin hale ofte er ein generisk stack-trace uavhengig
av kva som faktisk er gale i mermaid-syntaksen) vert difor **umoglege å
skilje frå kvarandre** i loggen — begge visest som identisk
"Mermaid-diagram nr. 2 rendrar ikkje: ...". Dette vart stadfesta i praksis
2026-08-16: to identiske åtvaringslinjer for "nr. 2" i same jobbkøyring,
utan at det går fram om det er same eller ulike filer som feilar.

Vidare skriv steget aldri sjølve oppsummeringstabellen (alle diagram, ikkje
berre dei feila) til jobb-loggen — han hamnar berre i `$GITHUB_STEP_SUMMARY`,
som krev eit ekstra klikk inn på Summary-fana for å sjå, og som ikkje er
tilgjengeleg i rå logg-dumpar.

**Merk (utanfor omfanget til denne spec-en):** Jobben feilar aldri
(`exit`-kode) sjølv om eitt eller fleire diagram ikkje rendrar — steget har
ingen `exit 1`/`exit $fail` ved slutten, så `mermaid-render`-jobben viser
`success` i Actions sjølv når diagram er broten. Dette kan vere eit bevisst
val (åtvaringsbasert sjekk, ikkje ein hard gate), tilsvarande `|| true` i
`lenkjesjekk`-jobben — vert ikkje endra her, sidan brukarinstruksjonen
gjaldt logging, ikkje feiltoleranse.

## Steg

1. Endre `::warning`-linja (line 170) til å ta med `${src}` **i sjølve
   meldingsteksten**, ikkje berre som `file=`-attributt, slik at filnamnet
   er synleg i rå loggtekst:
   ```bash
   echo "::warning file=${src}::${src} (diagram nr. ${idx}) rendrar ikkje: ${message}"
   ```
2. Skriv den fullstendige rapporttabellen (`$report`) til jobb-loggen (stdout)
   i tillegg til `$GITHUB_STEP_SUMMARY`, rett etter at totalsum-linja er
   lagt til — t.d.:
   ```bash
   echo ""
   echo "== Mermaid-rendering: oppsummering =="
   cat "$report"
   ```
   plassert før den eksisterande `{ echo "## Mermaid-rendering"; cat
   "$report"; } >> "$GITHUB_STEP_SUMMARY"`-blokka, slik at same tabell
   (alle diagram, ikkje berre dei feila) syner både i rå logg og i
   Summary-fana.
3. Køyr `actionlint` mot den endra workflow-fila (obligatorisk etter CI-
   endring, jf. CLAUDE.md).
4. Verifiser lokalt ved å simulere steget mot ein liten manifest-fil med
   minst eitt kunstig feila diagram (t.d. ei `.mmd`-fil med ugyldig
   mermaid-syntaks), og stadfeste at:
   - Filnamnet syner i sjølve `::warning`-meldingsteksten
   - Full oppsummeringstabell syner i stdout, ikkje berre i rapportfila

## Handlingsliste

- [x] Ta med `${src}` i sjølve meldingsteksten til `::warning`-linja
- [x] Skriv full rapporttabell til stdout (jobb-logg) i tillegg til
      `$GITHUB_STEP_SUMMARY`
- [x] `actionlint` på endra workflow-fil, ingen `[expression]`-feil
- [x] Lokal verifisering med eit kunstig feila diagram

## Utført

Endra `.github/workflows/lenkje-og-mermaid-sjekk.yml` (steget «Rendra kvar
mermaid-blokk»):

- `::warning`-linja tek no med `${src}` i sjølve meldingsteksten
  (`"${src} (diagram nr. ${idx}) rendrar ikkje: ${message}"`), ikkje berre
  som `file=`-attributt.
- Full rapporttabell (`cat "$report"`) vert no skriven til stdout
  (jobb-logg) i tillegg til `$GITHUB_STEP_SUMMARY`.

`actionlint` køyrt — same pre-eksisterande `[shellcheck]`-stilråd (ubrukt
`blockfile` i eit anna steg) som før, ingen `[expression]`-feil.

Lokal verifisering: simulerte steget mot ein testmanifest med eitt gyldig
og to kunstig feila diagram (ulike filer, same generiske Puppeteer-
feilmelding — reproduserer nøyaktig problemet frå CI-loggen). Resultat:
begge `::warning`-linjene viser no tydeleg ulike filnamn
(`docs/fake-b.md` vs. `docs/fake-c.md`) i sjølve loggteksten, og full
oppsummeringstabell (`3 diagram, 2 feila`) syner i stdout.
