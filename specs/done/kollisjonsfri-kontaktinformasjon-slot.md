# Gjer generert kontaktinformasjon-slot i make new-modell strukturelt kollisjonsfri

## Bakgrunn

`specs/done/rename-kontaktpunkt-slot-new-modell.md` bytte den genererte
slotnøkkelen frå `kontaktpunkt` til `kontaktinformasjon` for å unngå
kollisjon med det importerte `kontaktpunkt`-slotet frå `dcat-ap-no-schema`.
Verifikasjonen då var eit **punkt-i-tid-oppslag** mot dei 296 slot-namna som
finst i AP-NO-profilane i dag — ikkje ein strukturell garanti. Dersom eit
framtidig AP-NO-skjema (eller anna importert skjema) nokon gong definerer eit
slot kalla `kontaktinformasjon`, oppstår same kollisjonsproblem på nytt.

Løysing: prefiks slotnøkkelen med skjemaet sitt eige, garantert unike
`schema_name` (same verdi som alt vert brukt til å byggje class_uri-prefiks,
containerklassenamn osv. i `converter.py`). Sidan `schema_name` er unikt per
genererte modell, kan ingen fast, kjend AP-NO-vokabularslot nokon gong
kollidere med `<schema_name>_kontaktinformasjon` — kollisjonsfridomen følgjer
av konstruksjonen, ikkje av eit oppslag som kan verte utdatert.

## Steg

1. `src/mcp-linkml-modell-utkast/converter.py`: bytt slotnøkkelen frå det
   faste `kontaktinformasjon` til `f"{schema_name}_kontaktinformasjon"`
2. `src/mcp-linkml-modell-utkast/profiles/bronze.yaml`: oppdater kommentaren
   over `add_kontaktpunkt_slot` til å forklare den nye, namneromsbaserte
   kollisjonsfridomen
3. `mkdocs/docs/kom-i-gang/ny-domenemodell.md`: oppdater det viste
   skjema-eksempelet (bruker `tilskudd` som schema_name i eksempelet) til
   `tilskudd_kontaktinformasjon`, og oppdater forklaringsprosaen

## Handlingsliste

- [x] Steg 1: converter.py retta
- [x] Steg 2: bronze.yaml-kommentar retta
- [x] Steg 3: ny-domenemodell.md retta

## Utført

Alle tre steg utført og verifisert (Python-syntaks og YAML-parsing OK).
`make new-modell` genererer no `<schema_name>_kontaktinformasjon`
(t.d. `designregisteret_kontaktinformasjon`) i staden for det faste
`kontaktinformasjon` — kollisjonsfridomen følgjer strukturelt av at
`schema_name` er unikt per genererte modell, ikkje av eit punkt-i-tid-oppslag
mot dagens AP-NO-slotnamn.
