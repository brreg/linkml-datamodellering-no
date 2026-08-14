# Byt namn på generert kontaktpunkt-slot i make new-modell

## Bakgrunn

`make new-modell` genererer (via `add_kontaktpunkt_slot`-flagget i
`profiles/bronze.yaml`, implementert i `converter.py`) ein global slot
`kontaktpunkt` med `slot_uri: dcat:contactPoint`, `range: uriorcurie`.

Sidan `new-modell.sh` no alltid set inn ein absolutt versjonslåst import av
`dcat-ap-no-schema` (jf. `specs/done/gjeninnfor-dcat-ap-no-import-doc-new-modell.md`),
og `dcat-ap-no-schema.yaml` **allereie** definerer ein global slot
`kontaktpunkt` (`slot_uri: dcat:contactPoint`, men `range: Kontaktopplysning`,
`multivalued: true`) — kollisjonerer den genererte lokale sloten med den
importerte. Dei to definisjonane er ikkje kompatible (ulik `range`), så
domenemodellen ville lokalt redefinert eit slotnamn som alt finst i
importhierarkiet med ein annan definisjon.

Verifisert med eit fullstendig oppslag av alle slot-namn definerte i
`src/linkml/ap-no/*/​*-schema.yaml` (296 unike namn) at `kontaktinformasjon`
ikkje er brukt nokon stad — trygt val som generisk erstatning.

Avgrensa til `make new-modell`-flyten. Andre scaffolding-skript
(`new-begrepskatalog.sh`, `new-modellkatalog.sh`, `new-begrepssamling.sh`) og
tilhøyrande dokumentasjon brukar `kontaktpunkt`/`kontaktpunkt_vcard` korrekt
som referansar til det **importerte** dcat-ap-no-slotet i instansdata — ikkje
ein lokalt redefinert slot — og er difor ikkje ramma av same problem.

## Steg

1. `src/mcp-linkml-modell-utkast/converter.py`: byt slotnøkkel `kontaktpunkt`
   → `kontaktinformasjon` i `add_kontaktpunkt`-blokka
2. `src/mcp-linkml-modell-utkast/profiles/bronze.yaml`: oppdater
   kommentaren over `add_kontaktpunkt_slot` til å nemne det nye slotnamnet
3. `mkdocs/docs/kom-i-gang/ny-domenemodell.md`: oppdater det viste
   skjema-eksempelet og forklaringsprosa til `kontaktinformasjon`

## Handlingsliste

- [x] Steg 1: converter.py retta
- [x] Steg 2: bronze.yaml-kommentar retta
- [x] Steg 3: ny-domenemodell.md retta

## Utført

Alle tre steg utført og verifisert (Python-syntaks og YAML-parsing OK på
dei endra filene). `make new-modell` genererer no `kontaktinformasjon`
(same `slot_uri`/`range` som før) i staden for `kontaktpunkt`, som ikkje
lenger kolliderer med det importerte `kontaktpunkt`-slotet frå
`dcat-ap-no-schema`.
