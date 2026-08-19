# Plan: Konsekvent DOMAIN/SCHEMA-rekkjefølgje

## Bakgrunn

Same mønster som [[domain-name-argumentrekkjefolge]], no for `SCHEMA`/`DOMAIN`:
alle `gen-*`-target (og `gen-informasjonsmodell-instance`) viser argumenta
sine i `make/11-generator-targets.mk`/`make/30-instances.mk` som
`[SCHEMA=<sti>|DOMAIN=<domain>]` (SCHEMA først), medan `COMMANDS.md` og
`mkdocs/docs/kom-i-gang/kommandoar.md` allereie viser `[DOMAIN=...] [SCHEMA=...]`
(DOMAIN først) for nøyaktig same target. Brukaren ønskjer DOMAIN alltid
først, og at `make help`-kjeldeteksten skal matche `COMMANDS.md`.

16 førekomstar av `[SCHEMA=<sti>|DOMAIN=<domain>]` funne:
- `make/11-generator-targets.mk`: 15 (alle `gen-*`-target)
- `make/30-instances.mk`: 1 (`gen-informasjonsmodell-instance`)

`COMMANDS.md` og `mkdocs/docs/kom-i-gang/kommandoar.md` treng **ingen**
endring — dei har alt DOMAIN før SCHEMA for desse 16 targeta. Unntak:
`gen-informasjonsmodell-instance`-raden i `COMMANDS.md` viser i dag berre
`SCHEMA=<sti>` (ikkje DOMAIN i det heile, og utan hakeparentes = ser ut som
obligatorisk) — dette er eit **eksisterande, ikkje-relatert** avvik (ordninga
gjeld ikkje der sidan DOMAIN ikkje er nemnt), og vert ikkje retta her då det
er eit fullstendigheitsspørsmål, ikkje eit rekkjefølgje-spørsmål.

**Avgrensing:** Berre rekkjefølgja på ordet-nivå inni det eksisterande
`[SCHEMA=<sti>|DOMAIN=<domain>]`-uttrykket vert endra til
`[DOMAIN=<domain>|SCHEMA=<sti>]`. Sjølve alternasjons-notasjonen (eitt
hakeparentespar med `|`, i staden for `COMMANDS.md` sin to-separate-
hakeparentesar-stil) vert ikkje endra — det er eit separat
formateringsspørsmål brukaren ikkje har bedt om, og `help.sh` handterer
begge stilar likt (heile den avsluttande gruppa vert vist ordrett).

## Handlingsliste

1. [x] `make/11-generator-targets.mk`: byt om alle 15 førekomstar
2. [x] `make/30-instances.mk`: byt om 1 førekomst
3. [x] Verifiser med `make help` at alle 16 target no viser
   `[DOMAIN=<domain>|SCHEMA=<sti>]`

## Utført

Alle 16 førekomstar av `[SCHEMA=<sti>|DOMAIN=<domain>]` bytte om til
`[DOMAIN=<domain>|SCHEMA=<sti>]` (`replace_all` i `make/11-generator-targets.mk`,
éin manuell i `make/30-instances.mk`). `COMMANDS.md` og
`mkdocs/docs/kom-i-gang/kommandoar.md` var alt korrekte (DOMAIN før SCHEMA) —
ingen endring naudsynt der. Verifisert med `make help`.
