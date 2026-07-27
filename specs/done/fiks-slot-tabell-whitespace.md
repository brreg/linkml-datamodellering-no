# Fiks slot-tabell whitespace i index.md.jinja2

## Bakgrunn

Etter at vi la til klikkbare "Defined in"-lenkjer i slot-tabellane i commit
`74e235ab` (feat(docgen): klikkbare "Defined in"-lenkjer i alle tabellar),
fekk `common-ap-no/index.md` øydelagte "Verdiar"- og "Referansar"-tabellar.

**Symptom:**

Alle tabellinjer vart klemt saman på éi linje utan linjeskift:

```markdown
| Slot | Description | Defined in | Usage |
| --- | --- | --- | --- || [anbefalt_term](anbefalt_term.md) | ... | ... | ... || [beskrivelse](beskrivelse.md) | ... | ... | ... || ...
```

**Rotårsak:**

Jinja-templaten `src/assets/templates/docgen/index.md.jinja2` hadde feil
whitespace-kontroll i slot-tabell-blokkene:

- Linje 147: `{%- for s in ns_slots_verdiar.items|sort(...) %}` — strippar
  linjeskift **før** taggen, som fjernar linjeskiftet mellom header og første rad
- Linje 165: `{%- endfor %}` — strippar linjeskift **før** taggen, som fjernar
  linjeskiftet mellom kvar tabellrad

Markdown-tabellar krev linjeskift mellom kvar rad, så dette øydela tabellen.

## Løysing

Endre whitespace-kontroll i slot-tabell-blokkene til same mønster som
enum- og types-tabellar (som fungerer korrekt):

- `{% for ... -%}` (ikkje `{%- for`) → beheld linjeskift etter header
- `{% endfor -%}` (ikkje `{%- endfor`) → beheld linjeskift før endif

Dette følgjer same prinsipp som dokumentert i `CLAUDE.md` under
"Jinja2-template whitespace-kontroll".

## Steg

1. ✅ Endre `ns_slots_verdiar`-blokk (linje 147, 165) til `{% for -%}` og `{% endfor -%}`
2. ✅ Endre `ns_slots_referansar`-blokk (linje 173, 191) til `{% for -%}` og `{% endfor -%}`
3. ✅ Endre `ns_slots_kodar`-blokk (linje 199, 217) til `{% for -%}` og `{% endfor -%}`
4. ✅ Regenerer dokumentasjon for `common-ap-no` med `make gen-docs`
5. ✅ Verifiser at tabellane har korrekte linjeskift

## Utført

**Endra filer:**
- `src/assets/templates/docgen/index.md.jinja2`: Endra whitespace-kontroll i
  tre slot-tabell-blokker (Verdiar, Referansar, Kodar)

**Resultat:**

Alle slot-tabellar i `common-ap-no/index.md` viser no kvar rad på eiga linje:

```markdown
| Slot | Description | Defined in | Usage |
| --- | --- | --- | --- |
| [anbefalt_term](anbefalt_term.md) | ... | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) | ⚠️ Defined |
| [beskrivelse](beskrivelse.md) | ... | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) | ⚠️ Defined |
...
```

**Verifisering:**

- ✅ `make gen-docs SCHEMA=src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml`
- ✅ Verdiar-tabell: 13 rader, kvar på eiga linje
- ✅ Referansar-tabell: 7 rader, kvar på eiga linje
- ✅ Enumerations-tabell: 7 rader (uendra, fungerte før og etter)
- ✅ Types-tabell: 8 rader (uendra, fungerte før og etter)
