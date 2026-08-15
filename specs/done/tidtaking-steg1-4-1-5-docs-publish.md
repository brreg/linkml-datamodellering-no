# Tidtaking for Steg 1.4/1.5 i publish.sh (manglande delsteg forklarer gap)

## Bakgrunn

Etter forrige endring (rens tidteke via `timed_run`, sjå
`specs/done/logging-tidtaking-rens-docs-publish.md`) er det framleis eit gap
mellom summen av dei loggførte delstega i Steg 1 og den samla
`✓ Steg 1 ferdig`-tida.

Årsak: Steg 1 i `mkdocs/publish.sh` består av **seks** reelle arbeidsblokker,
men berre **fire** var individuelt tidtekne/loggførte via `timed_run()`:

1. Rens tidlegare genererte domene-katalogar (tidteke)
2. Oppdater README.md-tabellar (tidteke)
3. Generer index.md frå README.md (tidteke)
4. Generer valideringsregler.md (tidteke)
5. **Steg 1.4: Finn domene/skjema-struktur frå `generated/`** — fleire
   `find`-kall over `$GEN`-treet (linje ~218, 221) — **ikkje tidteke**
6. **Steg 1.5: Bygg delmodell-/metadata-oppslag** — inkluderer eit
   `find`-kall over heile `src/linkml/` (kjend dyrt på NTFS-monterte
   `/mnt/c` under WSL2, sjå kommentar i koden) OG det samla
   `collect-schema-metadata.py`-containerkallet
   (`run_python_container`, linje ~312) — sannsynlegvis den tyngste enkelt
   operasjonen i heile Steg 1 — **ikkje tidteke**

Summen av dei fire `timed_run`-linjene var difor alltid mindre enn den
samla `elapsed1_ms`, fordi Steg 1.4 og 1.5 sitt arbeid (inkludert
container-kallet) forsvann inn i differansen utan eiga logglinje.

## Kvifor ikkje berre wrappe 1.4/1.5 i funksjonar og bruke `timed_run` (som resten av Steg 1)?

Vurdert og forkasta: Steg 1.4 gjer `declare -a ALL_DOMAINS=()` og
`declare -A DOMAIN_SCHEMA_LIST=()`, og Steg 1.5 gjer tilsvarande for
`SCHEMA_PARENT_MODEL`/`SCHEMA_SUBMODELS` m.fl. — desse må vere synlege i
hovudshell-scope for Steg 2/3 lenger ned. Ei `declare -a`/`declare -A` inni
ein bash-funksjon utan eksplisitt `-g`-flagg er **lokal** for funksjonen
(bash sin standardoppførsel), så å pakke desse blokkene inn i funksjonar
kalla via `timed_run` ville gjort arrayane usynlege utanfor funksjonen og
brote Steg 2/3. Løysinga brukar difor manuell `t/elapsed`-tidtaking direkte
i hovudshell (same mønster som Steg 2/Steg 3 sin `✓ Steg N ferdig`-linje
alt brukar i same fil), ikkje `timed_run`.

## Steg

1. Legg til `t1_4=$(date +%s%3N)` rett før Steg 1.4-blokka startar, og
   logg `→ Steg 1.4: Finn domene/skjema-struktur (X.Xs)` (CLR_STEP) rett
   etter blokka er ferdig.
2. Legg til `t1_5=$(date +%s%3N)` rett før Steg 1.5-blokka startar, og
   logg `→ Steg 1.5: Bygg delmodell-/metadata-oppslag (X.Xs)` (CLR_STEP)
   rett etter blokka er ferdig (rett før den samla `elapsed1_ms`-linja).
3. Behald `t1`/`elapsed1_ms` uendra — dekkjer framleis heile Steg 1.
4. Verifiser: summen av dei no seks loggførte delstega skal vere
   (tilnærma) lik `✓ Steg 1 ferdig`-tida, med berre neglisjerbar
   overhead frå `$GEN`-eksistenssjekken og éitt `date`-kall for
   `BUILD_TIMESTAMP` att utanfor.

## Handlingsliste

- [x] `mkdocs/publish.sh`: manuell tidtaking + logging for Steg 1.4 og
      Steg 1.5
- [x] `bash -n` syntakssjekk OK
- [ ] Verifisert med reell `make docs-publish`-køyring (ikkje gjort i denne
      økta — krev `generated/`-innhald frå full domenegenerering)
