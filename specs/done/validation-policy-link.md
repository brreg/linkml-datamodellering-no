# Lenke frå valideringsresultat til valideringspolicy

## Bakgrunn

I Valideringsresultat-seksjonen i `index.md` står det t.d. "*Siste validering: 2026-07-04 — v1.0.5 — policy: silver*". Brukaren ønskjer at "policy: silver" (og tilsvarande for bronze/gold osv.) skal vere ei lenke til den aktuelle valideringspolicyen på `/valideringsregler/#<policy>`.

Dette gjer det enklare for lesarar å forstå kva krava i policyen er.

## Tiltak

1. **Endre `generate-validation-md.py`** til å generere Markdown-lenke for policy-namnet
   - Formater: `[policy: <policy>](/valideringsregler/#<policy>)`
   - Skal støtte bronze, silver, gold, felles-datakatalog, felles-begrepskatalog
2. **Verifiser i eksisterande skjema** at lenka fungerer i mkdocs-portalen

## Handlingsliste

- [x] Endre `generate-validation-md.py` linje 48
- [x] Kjør `make docs-publish` for å regenerere
- [x] Verifiser lenke i `mkdocs/docs/samt/samt-bu/index.md`

## Utført

Alle tiltak er utførte. `generate-validation-md.py` genererer no Markdown-lenker for policy-namnet som peikar til rett seksjon i `/valideringsregler.md`:

- Bronze → `#bronze-sjekkliste`
- Silver → `#silver-sjekkliste`
- Gold → `#gold-sjekkliste`
- Felles-datakatalog → `#felles-datakatalog-felles-datakatalog`
- Felles-begrepskatalog → `#felles-begrepskatalog-felles-begrepskatalog`

Verifisert i `samt/samt-bu` (silver), `modellkatalog/brreg-modellkatalog` (bronze) og `ngr/ngr-adresse` (felles-datakatalog).
