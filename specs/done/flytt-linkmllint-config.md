# Flytt .linkmllint.yaml til src/assets/containers/

## Bakgrunn

`.linkmllint.yaml` ligg no i rotmappa og konfigurererer `linkml lint`-verktøyet.
For å samle alle container-relaterte konfigurasjonsfiler på éin stad, skal denne
flyttast til `src/assets/containers/` og Makefile oppdaterast til å bruke
`--config`-flagget.

## Steg

1. ✅ Flytt `.linkmllint.yaml` til `src/assets/containers/.linkmllint.yaml`
2. ✅ Oppdater `lint`-target i Makefile til å bruke `--config src/assets/containers/.linkmllint.yaml`
3. ✅ Test at `make lint SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` fungerer
4. ✅ Generer commit-melding

## Handlingsliste

- [x] Flytt konfigurasjonsfil
- [x] Oppdater Makefile
- [x] Verifiser lint-kommando

## Utført

Alle steg er fullførte:
- `.linkmllint.yaml` flytta frå rotmappa til `src/assets/containers/`
- `lint`-target i Makefile oppdatert til å bruke `--config src/assets/containers/.linkmllint.yaml`
- Verifisert at `make lint` fungerer med ny konfigurasjon
