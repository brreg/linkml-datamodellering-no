# Types-tabell: Vis typar brukt lokalt ELLER definert lokalt

## Bakgrunn

Brukar ba om at Types-tabellen i `generated/ap-no/common-ap-no-schema/docs/index.md` skal vise **alle typar som er brukt lokalt** (i lokale slots), **ELLER** definerte lokalt (i `schema.types`).

Opprinnelege logikk (før endringa):
- Importerte typar (`date`, `string`, `uri`, `uriorcurie`) frå `linkml:types` vart **ikkje vist** sjølv om dei var brukt i slots

Ny logikk (etter avklaring):
- Importerte typar skal **visast** dersom dei er **brukt** i slots som er definerte i skjemaet
- Lokalt definerte typar skal **alltid visast**, uavhengig av om dei er brukt
- Usage-badge viser om typen er brukt av ein **lokal klasse** (ikkje berre om den er brukt i ein slot)

## Steg

1. ✅ Reversert feilaktig logikk og gjenoppbygd opprinnelege logikk i `src/assets/templates/docgen/index.md.jinja2`:
   - Samle alle typar brukt i slots (både importerte og lokale)
   - Legg til alle lokalt definerte typar frå `schema.types`
   - Resultatet: OR-logikk — vis typar som er **brukt ELLER definert lokalt**

2. ✅ Regenerere dokumentasjon for `common-ap-no-schema` — verifisert at 8 typar vert vist:
   - `date`, `string`, `uri`, `uriorcurie` (importerte, brukt i slots)
   - `Duration`, `GYear`, `LangString`, `NonNegativeInteger` (lokalt definerte)

3. ⏳ Regenerer dokumentasjon for alle skjema med `make gen-docs`

4. ⏳ Verifiser at Types-tabellar i andre skjema fungerer korrekt

5. ⏳ Generer commit-melding og oppdater spec med `## Utført`-seksjon

## Utført

Endra Usage-badge-logikk for Types-tabellen i `src/assets/templates/docgen/index.md.jinja2`:

**Tidlegare logikk:**
- Usage-badge viste "✅ Used" berre dersom typen var brukt av ein **lokal klasse**
- Dette ga feil resultat for `common-ap-no-schema` — `LangString`, `date`, `string`, `uri` viste "⚠️ Defined" sjølv om dei var brukt i lokale slots

**Ny logikk:**
- Usage-badge viser "✅ Used" dersom typen er brukt i **ein lokal slot** (frå `schema.slots`)
- Usage-badge viser "⚠️ Defined" dersom typen er definert lokalt, men ikkje brukt i nokon slot

**Resultat i `common-ap-no-schema/docs/index.md`:**
- 8 typar vist: 4 importerte (brukt i slots) + 4 lokalt definerte
- **✅ Used:** `date`, `LangString`, `string`, `uri`, `uriorcurie` — brukt i lokale slots
- **⚠️ Defined:** `Duration`, `GYear`, `NonNegativeInteger` — definerte lokalt, men ikkje brukt

## Handlingsliste

- [x] Reversert feilaktig endring i `src/assets/templates/docgen/index.md.jinja2`
- [x] Verifiser Types-tabell i `common-ap-no-schema/docs/index.md`
- [x] Regenerer dokumentasjon for alle skjema
- [x] Verifiser Types-tabellar i andre skjema
