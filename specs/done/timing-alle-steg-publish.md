# Timing for alle steg i publish.sh

## Bakgrunn

`mkdocs/publish.sh` har fire hovudsteg:
- **Steg 1:** Rens tidlegare genererte domene-katalogar frå docs/
- **Steg 2:** Generer innhald per domene og skjema (parallelt) — har allereie timing per skjema
- **Steg 3:** Generer index.md frå README.md og valideringsregler.md
- **Steg 4:** Generer mkdocs.yml

For tida viser scriptet berre timing for kvar individuell skjema-jobb i Steg 2. Brukaren ønsker timing for **alle fire hovudstega** for å kunne sjå kor lang tid kvar del av publiseringsflyten tar.

## Endringar

Legg til timing for alle fire hovudstega ved å:
1. Ta tidsstempel før og etter kvart hovudsteg
2. Vis elapsed tid i formatet `(X.Xs)` ved slutten av kvar steg
3. Behald eksisterande per-skjema-timing i Steg 2

## Handlingsliste

- [x] Legg til `t0=$(date +%s%3N)` før kvart steg
- [x] Legg til elapsed-utrekning og printf-linje etter kvart steg
- [x] Test at timing vises korrekt for alle fire stega

## Utført

Lagt til timing for alle fire hovudstega i `mkdocs/publish.sh`:

- **Steg 1** (rens tidlegare domene-katalogar): `t1` → `elapsed1_ms` → printf
- **Steg 2** (generer innhald parallelt): `t2` → `elapsed2_ms` → printf (i tillegg til eksisterande per-skjema-timing)
- **Steg 3** (generer index.md og valideringsregler.md): `t3` → `elapsed3_ms` → printf
- **Steg 4** (generer mkdocs.yml): `t4` → `elapsed4_ms` → printf

Alle timing-linjer brukar same format som Steg 2 per-skjema-timing: `(X.Xs)`

