# Logging og tidtaking for rens av tidlegare genererte docs/-katalogar

## Bakgrunn

`mkdocs/publish.sh` Steg 1 slettar tidlegare genererte domene-katalogar i
`mkdocs/docs/` (to for-løkker, linje 149-174) før nytt innhald vert generert
i Steg 2. Denne slettinga har ingen eiga logging (kva som vert sletta, ved
DEBUG-nivå) og ingen eiga tidtaking — han er berre implisitt inkludert i den
samla `t1`/`elapsed1_ms`-tidtakinga for heile Steg 1, som også dekkjer
metadata-innhenting og README-tabellgenerering (linje 194-196, 371-374).

Andre operasjonar i same Steg 1 (`generate-readme-tables.sh`,
`write_index_from_readme`, `generate_validation_docs`) er alt individuelt
tidtekne og loggførte via `timed_run()` (definert i `make/00-settings.mk:73`,
eksportert via `LOG_FUNCTIONS`). Rensa av `docs/`-katalogar manglar
tilsvarande synlegheit.

## Steg

1. Pakk dei to eksisterande for-løkkene (linje 149-174 i `mkdocs/publish.sh`)
   inn i ein ny funksjon `clean_previous_docs()`, utan å endre logikken i
   løkkene.
2. Legg til `log_debug "→ Slettar $DOCS/$domain"` rett før
   `find "${DOCS}/${domain}" -mindepth 1 -depth -delete` i den fyrste
   løkka, slik at kva som vert sletta er synleg ved `LOGLVL=DEBUG`.
3. Kall `clean_previous_docs` via `timed_run "Rens tidlegare genererte
   domene-katalogar" clean_previous_docs` i staden for direkte
   løkke-utføring — gjev namn+tidtaking på linje med søsken-operasjonane
   lenger ned i same steg.
4. Behald eksisterande samla `t1`/`elapsed1_ms`-tidtaking for heile Steg 1
   uendra (dekkjer framleis alle sub-operasjonane, inkludert den nye).
5. Verifiser: køyr `make docs-publish` (eller `bash mkdocs/publish.sh`
   direkte med `LOG_FUNCTIONS` eksportert) og stadfest at ei ny
   `→ Rens tidlegare genererte domene-katalogar (X.Xs)`-linje visast i
   Steg 1, og at `LOGLVL=DEBUG` viser per-domene slette-linjer.

## Handlingsliste

- [x] `mkdocs/publish.sh`: ny `clean_previous_docs()`-funksjon, `log_debug`
      per sletta domene, kalla via `timed_run`
- [x] Verifisert (`bash -n` — syntaks OK; ikkje køyrt `make docs-publish`
      i denne økta, sjå merknad under)

## Utført

- `mkdocs/publish.sh`: dei to eksisterande for-løkkene som rensar
  `mkdocs/docs/<domain>/` vart pakka inn i ny funksjon
  `clean_previous_docs()`, kalla via
  `timed_run "Rens tidlegare genererte domene-katalogar" clean_previous_docs`
  — gjev no eiga `→ Rens tidlegare genererte domene-katalogar (X.Xs)`-linje
  på linje med søsken-operasjonane i same steg (README-tabellar, index.md,
  valideringsregler.md). Lagt til `log_debug "→ Slettar $DOCS/$domain"`
  per domene-katalog som vert sletta, synleg ved `LOGLVL=DEBUG`.
- Ikkje endra: den samla `t1`/`elapsed1_ms`-tidtakinga for heile Steg 1
  (dekkjer framleis alle sub-operasjonane).
- **Merknad:** `make docs-publish` vart ikkje køyrt i denne økta (krev
  `generated/`-innhald frå ein full domenegenerering). Verifiser med
  `LOGLVL=DEBUG make docs-publish` ved neste høve for å stadfeste at
  linjene visast som venta.
