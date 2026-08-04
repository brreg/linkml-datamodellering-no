# Uppercase Domene-kolonna i Skjema-tabellen (README.md)

## Bakgrunn

Følgjer opp `specs/done/referanse-nav-omdoyping.md`, som gjorde "Domene"-kolonna
i Domener-tabellen uppercase (med `REF` for referanse). Skjema-tabellen
(auto-generert av `generate_schema_table()` i
`src/assets/scripts/makefile/generate-readme-tables.sh`) brukar framleis
småbokstavar mappenamn som lenkjetekst i "Domene"-kolonna (t.d.
`[referanse](referanse/)`, `[ap-no](ap-no/)`). Skal endrast til same mønster:
uppercase, `REF` for referanse.

## Steg

### 1. Legg til `domain_short_label()`-funksjon

I `generate-readme-tables.sh`, før `generate_schema_table()`:

```bash
domain_short_label() {
  case "$1" in
    referanse) echo "REF" ;;
    *) echo "$1" | tr '[:lower:]' '[:upper:]' ;;
  esac
}
```

### 2. Bruk funksjonen i `generate_schema_table()`

Endre output-linja (linje ~89) frå:

```bash
echo "| [$domain]($domain/) | [$schema_name]($ghpages_schema_link/) | $description | $doc_link"
```

til:

```bash
echo "| [$(domain_short_label "$domain")]($domain/) | [$schema_name]($ghpages_schema_link/) | $description | $doc_link"
```

Lenkje-URL-en (`$domain/`) er uendra — berre lenkjeteksten vert uppercase.

### 3. Regenerer README.md

Køyr scriptet på nytt for å oppdatere den auto-genererte Skjema-tabellen:

```bash
./src/assets/scripts/makefile/generate-readme-tables.sh README.md
```

## Steg 4 (oppdaga undervegs): Fiks regex-bug i BEGIN/END AUTO-GENERATED-gjenkjenning

Regex-mønstera som identifiserer auto-generert-blokker leitte etter literal
`SCHEMA TABLE` / `BEGREPSKATALOG TABLE` / `MODELLKATALOG TABLE` (store
bokstavar, mellomrom), medan markørane i README.md faktisk inneheld
`generate_schema_table` / `generate_begrepskatalog_table` /
`generate_modellkatalog_table` (funksjonsnamn, snake_case) — eit format som
vart innført i ein tidlegare commit utan at regex vart oppdatert til å matche.
Konsekvens: scriptet har sidan då aldri faktisk regenerert desse tre
tabellane — det har berre kopiert eksisterande innhald uendra, sjølv om
`✅ README.md er oppdatert`-meldinga vart skriven ut (stille feil).

Retta ved å endre alle seks regex-mønster til å matche funksjonsnamnet i
staden for det gamle "TABLE"-suffikset.

**Konsekvens av fiksen:** ved regenerering kom Skjema-tabellen no i synk med
faktisk skjema på disk — 3 nye rader for `referansemodell-bronze/-silver/-gold`
(frå bronze/silver/gold-oppsplittinga) og oppdatert skildring for
`fair-metadata` som ikkje hadde kome inn tidlegare. Brukar stadfesta at full
regenerering (ikkje berre uppercase) er ønskt.

## Handlingsliste

- [x] Legg til `domain_short_label()` i `generate-readme-tables.sh`
- [x] Bruk funksjonen i `generate_schema_table()`
- [x] Fiks regex-bug som hindra auto-generering av Skjema-/Begrepskatalog-/Modellkatalog-tabellane
- [x] Regenerer README.md og verifiser Domene-kolonna i Skjema-tabellen

## Utført

- `src/assets/scripts/makefile/generate-readme-tables.sh`: la til `domain_short_label()` (REF for referanse, elles uppercase), brukt i `generate_schema_table()`; retta seks regex-mønster (`SCHEMA/BEGREPSKATALOG/MODELLKATALOG TABLE` → `generate_schema_table`/`generate_begrepskatalog_table`/`generate_modellkatalog_table`) som hindra auto-generering
- `README.md`: regenerert Skjema-tabellen — uppercase Domene-kolonne, nye rader for `referansemodell-bronze/-silver/-gold`, oppdatert `fair-metadata`-skildring
