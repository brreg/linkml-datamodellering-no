# Slots-gruppering etter range-type

## Bakgrunn

Slots-seksjonen i `mkdocs/docs/<domain>/<schema>/index.md` viser no ei flat liste av alle slots. Det er vanskeleg å skilje mellom:
- **Verdiar**: slots som held primitive verdiar (t.d. `tittel: string`, `startdato: date`)
- **Referansar**: slots som peikar til andre klasser (t.d. `utgiver: Aktoer`, `tema: Konsept`)
- **Kodar**: slots som held enumverdiar (t.d. `status: StatusEnum`)

## Mål

Gruppere Slots-seksjonen i tre underseksjonar basert på `slot.range`:

1. **Verdiar** (`### Verdiar`): slots med `range` som er ein **Type** (frå `linkml:types`, `common-ap-no` osv.)
2. **Referansar** (`### Referansar`): slots med `range` som er ein **Class**
3. **Kodar** (`### Kodar`): slots med `range` som er ein **Enum**

Visuelt skal dette sjå ut som Classes sin gruppering etter subsets (Obligatorisk, Anbefalt, Valgfri, Andre).

## Foreslått løysing

Endre `src/assets/templates/docgen/index.md.jinja2` til å:
1. Iterere over alle slots **tre gonger** (ein gong per kategori)
2. For kvar slot: sjekk om `schemaview.get_type(s.range)`, `schemaview.get_class(s.range)` eller `schemaview.get_enum(s.range)` returnerer noko
3. Vis slot i riktig kategori

Rekkjefølgje:
```markdown
## Slots

### Verdiar
| Slot | Description |
| --- | --- |
| tittel | ... |
| startdato | ... |

### Referansar
| Slot | Description |
| --- | --- |
| utgiver | ... |
| tema | ... |

### Kodar
| Slot | Description |
| --- | --- |
| status | ... |
```

## Tiltak

1. [✓] Endre Slots-seksjonen i `index.md.jinja2`:
   - Fjerna eksisterande flat liste
   - La til tre underseksjonar (Verdiar, Referansar, Kodar)
   - Klassifiserer basert på `schemaview.get_enum()`, `get_class()` (fallback til Verdiar)
2. [✓] Handter edge-cases:
   - Slots utan range eller med uspesifisert range → fallback til "Verdiar"
   - Sjekkar enum **før** class (fordi enum kan også vere class-basert i nokre tilfelle)
3. [✓] Test med `samt-bu` og verifiser at slots vert korrekt grupperte
   - Verdiar: `fylkesnummer`, `kommunenummer`, `navn`, `organisasjonsnummer`, `trinniva`
   - Referansar: `del_av_skole`, `enhetsleder_for`, `har_saerlig_ansvar_for`, osv.
   - Kodar: ingen i samt-bu (seksjon vert ikkje vist)
4. [✓] Sjekk at containerklasse-attributtar framleis er ekskluderte
   - `ns_root.attr_names`-logikken fungerer framleis

## Akseptansekriterium

- ✅ Slots-seksjonen skal ha tre underseksjonar: Verdiar, Referansar, Kodar
- ✅ `tittel`, `beskrivelse`, `startdato` osv. skal vere under "Verdiar"
- ✅ `utgiver`, `tema`, `kontaktpunkt` osv. skal vere under "Referansar"
- ✅ Slots med enum-range skal vere under "Kodar"
- ✅ Containerklasse-attributtar skal framleis vere ekskluderte
- ✅ Dersom ein kategori er tom, skal den ikkje visast

## Utført

Implementerte slot-gruppering i `src/assets/templates/docgen/index.md.jinja2`:

1. **Samle slots i tre kategoriar**:
   - Enum-sjekk først: `schemaview.get_enum(s.range)` → Kodar
   - Class-sjekk: `schemaview.get_class(s.range)` → Referansar
   - Elles → Verdiar (inkluderer types og uspesifiserte ranges)

2. **Vis berre ikkje-tomme kategoriar**:
   - Kvar kategori har eigen `{%- if ns_slots_X.items %}` -sjekk
   - Dersom ingen slots i kategorien, vert seksjonen ikkje vist

3. **Bevart eksisterande funksjonalitet**:
   - Containerklasse-attributtar (`ns_root.attr_names`) vert framleis ekskluderte
   - Sortering (`|sort(attribute=sort_by)`) fungerer som før

**Resultat**: samt-bu sin Slots-seksjon har no "Verdiar" (5 slots) og "Referansar" (7 slots).

## Avhengigheiter

- Kjennskap til LinkML `SchemaView` API (`get_type()`, `get_class()`, `get_enum()`)
