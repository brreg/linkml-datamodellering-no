# Classes-gruppering basert på in_subset

## Bakgrunn

Classes-seksjonen i `mkdocs/docs/<domain>/<schema>/index.md` grupperte klasser basert på `slot_usage.in_subset` — dette fungerte for AP-NO-profilar, men ikkje for domenemodeller der `in_subset` er sett **direkte på klassen**.

Brukar la til `in_subset: [Obligatorisk]` på klasser som `Skole`, `Skoleeier`, osv. i `samt-bu-schema.yaml`, men desse vart ikkje grupperte korrekt.

## Mål

Støtte gruppering basert på **begge**:
1. `class.in_subset` (direkte på klassen) — **prioritet 1**
2. `slot_usage.in_subset` (frå slots) — **fallback**

## Implementering

Endra `src/assets/templates/docgen/index.md.jinja2` til å:
1. Sjekke `c.in_subset` **først**
2. Dersom ikkje sett, sjekke `slot_usage.in_subset` som fallback
3. Fjerne tomme liner mellom "## Classes" og første subseksjon ved å bruke `{%- %}` konsistent

## Resultat

- **Obligatorisk**: `Rektor`, `Skole`, `Skoleeier` (frå `class.in_subset`)
- **Anbefalt**: `Basisgruppe`, `Kontaktlaerer` (frå `class.in_subset`)
- **Valgfri**: `Elev` (frå `class.in_subset`)
- **Andre**: `Fylke`, `Kommune`, `Person`, `PrivatVirksomhet` (utan `in_subset`)

AP-NO-profilar (som brukar `slot_usage.in_subset`) fungerer framleis som før via fallback-logikken.
