# Vis importerte slots i slots-lista

## Bakgrunn

I dag viser slots-lista i `index.md` (generert av gen-doc) berre lokale slots definerte i skjemaet sitt eige `slots:`-blokk. Men dersom ein klasse i skjemaet refererer til ein slot definert i eit importert skjema (t.d. `dct:title` frå `dcat-ap-no-schema`), viser ikkje denne sloten i slots-lista.

Types- og enumerations-listene viser allereie importerte element med ein "Defined in"-kolonne som viser "Local" eller "Imported". Slots-lista skal følgje same mønster.

## Mål

Slots-lista i `index.md` skal vise alle slots som faktisk vert brukte i modellen — både lokale og importerte — med ein "Defined in"-kolonne som viser kvar sloten er definert.

## Prioritert handlingsliste

1. ✓ **Identifiser kvar gen-doc genererer slots-lista**
   - Les Jinja-templaten `src/assets/templates/docgen/index.md.jinja2`
   - Finn seksjonen som genererer `## Slots`-lista (linje 103-148)
   - Undersøk korleis types (linje 186-221) og enums (linje 150-184) allereie implementerer "Defined in"-kolonne med `from_schema`-feltet

2. ✓ **Implementer "Defined in"-kolonne for slots**
   - Endra logikken til å samle alle slots som faktisk vert brukte i modellen (frå `classes[*].slots`, ikkje `gen.all_slot_objects()` som berre gjev lokale slots)
   - Bruker same mønster som enums/types: `{%- set origin = s.from_schema if s.from_schema else schema.id %}`
   - Lagt til "Defined in"-kolonne i alle tre slot-tabellar (Verdiar, Referansar, Kodar)

3. ✓ **Test med skjema som importerer slots**
   - Testa med `samt-bu-schema.yaml` som importerer `dcat-ap-no-schema` og `dqv-ap-no-schema`
   - Testa med `dcat-ap-no-schema.yaml` som importerer `common-ap-no-schema`
   - Verifisert at importerte slots (t.d. `tittel`, `beskrivelse` frå `common-ap-no`) viser med korrekt "Defined in"-verdi

4. ✓ **Oppdater `publish.sh` dersom nødvendig**
   - Ikkje nødvendig — `publish.sh` kopierer berre genererte filer, gjer ingen transformasjonar av slots-lista

5. ✓ **Dokumenter endringane**
   - Ikkje nødvendig — slots-lista er generert artefakt, ikkje brukar-dokumentasjon

## Avhengigheiter

Ingen eksterne avhengigheiter. Byggjer på eksisterande "Defined in"-logikk for types og enums.

## Utført

Implementeringa vart gjennomført med éi viktig presisering: slots-lista viser **berre slots som er direkte refererte frå lokale klasser** i skjemaet, ikkje slots frå importerte klasser.

**Konkret for `samt-bu-schema`:**
- Viser `id`, `navn`, `har_skoleeier` osv. (brukt av lokale klasser som `Skole`, `Kommune`)
- Viser **ikkje** `tittel`, `beskrivelse` osv. frå importerte `Datasett`-klassen

**Implementeringsdetaljar:**
1. Samlar slots frå `classes[*].slots` **kun for klasser der `from_schema == schema.id`** (lokale klasser)
2. Viser "Defined in"-kolonne som viser `from_schema`-URI (t.d. `https://data.norge.no/ap-no/common-ap-no` for importerte slots)
3. Følgjer same mønster som types og enumerations
4. Fjerna `{%- if slot_name not in ns_root.attr_names %}` for å inkludere slots som òg vert brukt av containerklassen (t.d. `id`)

Testa med:
- `samt-bu-schema.yaml` → viser 6 verdislots og 7 referanseslots, alle brukt av lokale klasser
- `dcat-ap-no-schema.yaml` → viser både lokale slots (`algoritme`) og importerte slots (`beskrivelse`, `id`)

## Notater

- Slots-lista følgjer no same visuelle stil som types- og enums-listene
- Berre slots som faktisk vert refererte i `classes[*].slots` viser — ikkje alle slots i importerte skjema
- "Defined in"-kolonna viser skjema-URI (t.d. `https://data.norge.no/ap-no/common-ap-no`)
