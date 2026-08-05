# Fjern redundant policy-logglinje i flatten-and-validate.bash

## Bakgrunn

I validate-workflowen (`validate.yml`, steget "Valider skjema mot
validation_policy") køyrer `run-validation.sh` fleire skjema parallelt.
Kvart kall skriv ut `→ Validerer $domain/$model (vX) med policy: $POLICY`
(run-validation.sh:122) rett før det kallar `flatten-and-validate.bash`,
som deretter skriv ut `→ Flattar ut $SCHEMA ...` og
`→ Validerer (policy: $POLICY) ...` (flatten-and-validate.bash:40 og :73).

Den siste linja (`→ Validerer (policy: $POLICY) ...`) er reint duplikat:
han gjentek berre policyen, utan å identifisere kva for skjema det gjeld.
Når 6+ skjema valideres parallelt i CI vert resultatet fleire identiske
`→ Validerer (policy: gold) ...`-linjer på rad, utan nokon informasjonsverdi
utover det `run-validation.sh` allereie har logga.

## Steg

1. Fjern linje 73 (`echo "→ Validerer (policy: $POLICY) ..." >&2`) frå
   `src/mcp-linkml-validator/flatten-and-validate.bash`.
2. Behald `→ Flattar ut $SCHEMA ...` (linje 40) — han identifiserer kva
   for skjema som vert flatta ut, og er nyttig for standalone-bruk
   (t.d. `make lint`) der `run-validation.sh` ikkje er i kallstacken.

## Handlingsliste

- [x] Fjern redundant echo-linje i `flatten-and-validate.bash`
- [x] Verifiser med `make mcp-linkml-validate SCHEMA=<eit skjema>` at output
      framleis er tydeleg og utan tomrom/feil

## Utført

Fjerna `echo "→ Validerer (policy: $POLICY) ..." >&2` frå
`flatten-and-validate.bash`. Verifisert med
`make mcp-linkml-validate SCHEMA=src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml`
— berre `→ Flattar ut ...`-linja vert no skriven ut, valideringsresultatet
er uendra.
