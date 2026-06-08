# mcp-generate: Identifikatorar med bindestrek bryt gen-python

## Symptom

```
make mcp-generate SCHEMA=./tmp/bvrinnfelles_lm_v1.schema.json
```

Genererer `E-postadresse` som ein LinkML-type med bindestrek i namnet.
Gen-python feiler fordi `E-postadresse` ikkje er ein gyldig Python-identifikator.

## Rotårsak

`converter.py` sitt identifikator-handteringssystem er inkonsistent: slot-namn vert
saniterte, men **type-namn, enum-namn og klassenamn** vert ikkje saniterte — dei vert
tekne direkte frå `$defs`-nøklane i kjelde-JSON Schema.

Tre separate manglar:

### 1. `_collect_types()` linje 168 — type-nøkkel er ikkje sanitert

```python
types_out[name] = type_entry          # name = "E-postadresse" → bindestrek
```

Produserer:
```yaml
types:
  E-postadresse:          # ugyldig Python-identifikator
    uri: xsd:string
    ...
```

### 2. `_resolve_ref()` linje 70 — referanse er ikkje sanitert

```python
return ref.split("/")[-1]             # returnerer "E-postadresse" rått
```

Produserer:

```yaml
slots:
  e_postadresse:
    range: E-postadresse              # peikar på usanitert type-namn
```

Slot-namn (`e_postadresse`) og type-namn (`E-postadresse`) vert saniterte
ulikt: slot-sanitering (`_sanitize_slot_name`) køyrer på prop-namn, men
referanse frå `$ref` vert aldri sanitert. Dei to må vere konsistente.

### 3. `_collect_enums()` linje 189 og `_collect_classes()` linje 211, 218 — same mangel

```python
enums_out[name]   = enum_entry        # name frå $defs, ikkje sanitert
classes[name]     = {...}             # name frå $defs, ikkje sanitert
```

Klassenamn med bindestrek ville òg bryte gen-python. Enums med bindestrek
ville bryte gen-python og gen-jsonschema.

## Påverka filer og linjer

| Fil | Funksjon | Linje | Problem |
|---|---|---|---|
| `src/mcp-linkml-modell-utkast/converter.py` | `_collect_types()` | 168 | `types_out[name]` — rå nøkkel |
| `src/mcp-linkml-modell-utkast/converter.py` | `_resolve_ref()` | 70 | `ref.split("/")[-1]` — rå referanse |
| `src/mcp-linkml-modell-utkast/converter.py` | `_collect_enums()` | 189 | `enums_out[name]` — rå nøkkel |
| `src/mcp-linkml-modell-utkast/converter.py` | `_collect_classes()` | 211, 218 | `classes[name]` — rå nøkkel |

## Løysing

### Ny felles hjelpefunksjon `_sanitize_identifier()`

Legg til etter `_sanitize_slot_name()` (~linje 54):

```python
def _sanitize_identifier(name: str) -> str:
    """Gjer eit $defs-nøkkelnamn til ein gyldig LinkML/Python-identifikator.

    Translittererer særnorske bokstavar og erstattar bindestrek med understrek.
    Døme: 'E-postadresse' → 'E_postadresse'
    """
    return _transliterate(name).replace("-", "_")
```

**Merk:** `_transliterate` må køyrast *før* `replace("-", "_")` sidan bindestrek
berre kjem frå kjelda, ikkje frå translitterering.

### Tiltak 1 — Sanitér type-nøklar i `_collect_types()` (linje 168)

```python
# Før:
types_out[name] = type_entry

# Etter:
types_out[_sanitize_identifier(name)] = type_entry
```

### Tiltak 2 — Sanitér referansen i `_resolve_ref()` (linje 70)

```python
# Før:
return ref.split("/")[-1]

# Etter:
return _sanitize_identifier(ref.split("/")[-1])
```

### Tiltak 3 — Sanitér enum-nøklar i `_collect_enums()` (linje 189)

```python
# Før:
enums_out[name] = enum_entry

# Etter:
enums_out[_sanitize_identifier(name)] = enum_entry
```

### Tiltak 4 — Sanitér klassenøklar i `_collect_classes()` (linjene 211 og 218)

```python
# Før (linje 211):
classes[name] = {
    "properties": dict(defn.get("properties") or {}),
    ...
}

# Etter:
classes[_sanitize_identifier(name)] = {
    "properties": dict(defn.get("properties") or {}),
    ...
}

# Og linje 218 (fallback utan $defs):
# Før:
classes[schema_name] = {...}
# schema_name kjem frå Makefile-argumentet og er allereie kebab-case.
# Legg til sanitering her òg for konsistens:
classes[_sanitize_identifier(schema_name)] = {...}
```

**Viktig:** Etter dette tiltaket vil `cls_name` i hovudløkka i `convert()` allereie
vere sanitert — `entry["class_uri"] = f"{prefix_name}:{_transliterate(cls_name)}"` vil
da gje dobbel `_transliterate`, noko som er ufarleg (idempotent), men kan
forenklast om ønskjeleg.

## Testar som bør til

Legg til i eksisterande testsuite (t.d. `tests/test-mcp-linkml-generator.json`
eller dedikert pytest-fil):

1. **E-postadresse-typen**: JSON Schema med `"$defs": {"E-postadresse": {"type":
   "string"}}` og ein eigenskap med `"$ref": "#/$defs/E-postadresse"`. Forventa:
   generert skjema har `E_postadresse` som type-namn og `range: E_postadresse`
   i sloten.

2. **Bindestrek i klassenamn**: JSON Schema med `"$defs": {"My-Class": {"type":
   "object", "properties": {}}}`. Forventa: `My_Class` som klassenamn.

3. **Bindestrek i enum-namn**: JSON Schema med `"$defs": {"My-Enum": {"enum":
   ["a", "b"]}}`. Forventa: `My_Enum` som enum-namn.

4. **gen-python etter sanitering**: Det genererte skjemaet frå
   `bvrinnfelles_lm_v1.schema.json` skal passere `gen-python` utan feil.

## Tiltak

- [ ] Legg til `_sanitize_identifier()` i `converter.py`
- [ ] Bruk `_sanitize_identifier()` i `_collect_types()` (linje 168)
- [ ] Bruk `_sanitize_identifier()` i `_resolve_ref()` (linje 70)
- [ ] Bruk `_sanitize_identifier()` i `_collect_enums()` (linje 189)
- [ ] Bruk `_sanitize_identifier()` i `_collect_classes()` (linjene 211 og 218)
- [ ] Legg til testar for bindestrek i type-, enum- og klassenamn
- [ ] Verifiser at regenerert `bvrinnfelles_lm_v1.schema-schema.yaml` passerer
      `gen-python`
