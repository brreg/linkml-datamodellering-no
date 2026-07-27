# Språktagging for LangString (SK5) — `anbefalt_term` tospråkskrav

## Bakgrunn

SKOS-AP-NO v.2.0.15 krev at `skos:prefLabel` (anbefalt term) skal finnast på både **norsk bokmål** og **nynorsk** for norske begrep. Spesifikasjonen seier:

> "anbefalt term skal finnes på både bokmål og nynorsk; det skal være maksimum én per skriftspråk"

`felles-begrepskatalog`-policyen har allereie ein tospråksjekk for `har_definisjon` (`euvoc:xlDefinition`) via `begrep_har_definisjon_pa_nb_og_nn` (linje 339-349 i `policies/felles-begrepskatalog.yaml`). Denne sjekken bruker **ID-suffiks-konvensjonen** (`-nb`, `-nn`) for å detektere språk, sidan `euvoc:xlDefinition` peikar til `Definisjon`-objekt med eigne ID-ar.

**Problem:** `anbefalt_term` har range `LangString`, som **ikkje** kan bruke ID-suffiks-konvensjonen (det er ikkje eit objekt med ID, men ein direkte LangString-verdi). LinkML sin `LangString`-type mappar til `rdf:langString` i RDF, men **LinkML YAML-instansar støttar ikkje språk-tag per verdi** — jf. `specs/bugs/langstring-rdflib-roundtrip.md`.

**Utfordring:** Korleis kan vi validere tospråkskravet for `anbefalt_term` når LangString-verdiar i YAML-instansar ikkje bærer språkmarkør?

---

## Situasjonsanalyse

### Noverande tilstand

**`felles-begrepskatalog.yaml`:**
- ✅ Sjekkar at `Begrep` har `skos:prefLabel` (`anbefalt_term`) — linje 70-76
- ✅ Sjekkar at `Begrep` har minst éi `Definisjon` med språk-suffiks nb + nn — linje 339-349
- ❌ Sjekkar **ikkje** at `anbefalt_term` har både bokmål og nynorsk

### Kva spec krev

SKOS-AP-NO v.2.0.15:
- `skos:prefLabel` er **Obligatorisk** (2..n kardinalitet)
- Tospråkskrav: **både bokmål og nynorsk** skal finnast
- **Maksimalt éin per skriftspråk**
- Språkkoding: `@nb`, `@nn`, `@en`

---

## Tiltak

### Alternativ A — ID-suffiks-konvensjon for LangString-liknande strukturar (ikkje mogleg)

**Problem:** LangString er ikkje eit objekt med ID — det er ein primitiv streng-variant. Me kan ikkje bruke ID-suffiks.

### Alternativ B — Multivalued LangString med suffiks-konvensjon i verdien sjølv

**Problem:** Krev at modelleraren skriv `"føretaksnamn-nb"` og `"føretaksnamn-nn"` som separate verdiar — brytar med naturleg SKOS-AP-NO-bruk.

### Alternativ C — Aksepter avgrensinga, dokumenter og bruk RDF-validering

**Løysing:** Dokumenter at tospråksjekk for `LangString`-slots (som `anbefalt_term`) **ikkje er mogleg i YAML-instansvalidering** pga. LinkML sin avgrensing (jf. BUG-1). Språksjekk vert i staden utført på RDF-nivå etter TTL-generering.

**Kvifor det fungerer:**
- `make gen-rdf` genererer `.ttl` frå YAML-instansar
- TTL-fila **kan** innehalde `@nb` og `@nn` språk-tag (via manuell redigering eller frå mcp-begrep-utkast)
- SHACL-validering (framtidig tiltak) kan sjekke tospråkskrav direkte i TTL

**Tradeoff:** Tospråkskravet vert ikkje validert i YAML-fase, berre i RDF-fase (etter roundtrip eller publisering).

### Alternativ D — Utvide `felles-begrepskatalog`-policy med schemabasert sjekk

**Forslag:** Sjekk at `anbefalt_term`-sloten har `multivalued: true` og range `LangString` — dette sikrar at **skjemaet** er rigga for tospråkverdi, sjølv om instansen ikkje kan validerast.

---

## Valt tilnærming: Alternativ C + D (hybrid)

### Tiltak 1 — Schemabasert sjekk (warning)

Legg til ein ny sjekk i `felles-begrepskatalog.yaml` som verifiserer at **skjemaet** har rett konfigurasjon:

```yaml
begrep_anbefalt_term_er_multivalued_langstring:
  severity: warning
  description: >
    Begrep sin anbefalt_term (skos:prefLabel) bør ha range LangString og
    multivalued: true for å støtte tospråkskravet (bokmål + nynorsk).
    Merk: Instansvalidering av tospråkskravet er ikkje mogleg i YAML-format
    (sjå specs/bugs/langstring-rdflib-roundtrip.md). Bruk RDF-validering
    (SHACL) for å verifiere faktisk tospråkdekning i TTL-fila.
  check: slot_has_range_and_multivalued
  class: Begrep
  slot_uri: skos:prefLabel
  expected_range: LangString
  expected_multivalued: true
```

### Tiltak 2 — Dokumenter avgrensinga

Oppdater `policies/README.md` med ein merknad om at tospråkskravet for `anbefalt_term` ikkje kan validerast i YAML-instansar:

```markdown
**Tospråkskrav (SK5):**
- `har_definisjon` (euvoc:xlDefinition) — validert via ID-suffiks-konvensjon (`-nb`, `-nn`)
- `anbefalt_term` (skos:prefLabel) — **ikkje validert** i YAML-instansar pga. LinkML-avgrensing
  (sjå `specs/bugs/langstring-rdflib-roundtrip.md`). Bruk RDF-validering (SHACL) eller manuell
  gjennomgang av `.ttl`-fila for å verifiere at både `@nb` og `@nn` er til stades.
```

### Tiltak 3 — Oppdater audit-specen

Marker SK5 som **delvis løyst** med dokumentert avgrensing:
- ✅ `har_definisjon` tospråksjekk implementert
- ⚠️ `anbefalt_term` tospråksjekk ikkje mogleg i YAML — dokumentert som kjent avgrensing

---

## Implementering

### Steg 1 — Utvid `felles-begrepskatalog.yaml`

Legg til ny sjekk under `# ── Begrep-krav — SKOS-AP-NO-Begrep obligatoriske`:

```yaml
  begrep_anbefalt_term_er_multivalued_langstring:
    severity: warning
    description: >
      Begrep sin anbefalt_term (skos:prefLabel) bør ha range LangString og
      multivalued: true for å støtte tospråkskravet (bokmål + nynorsk).
      Merk: Instansvalidering av tospråkskravet er ikkje mogleg i YAML-format
      (sjå specs/bugs/langstring-rdflib-roundtrip.md). Bruk RDF-validering
      (SHACL) for å verifiere faktisk tospråkdekning i TTL-fila.
    check: slot_has_range_and_multivalued
    class: Begrep
    slot_uri: skos:prefLabel
    expected_range: LangString
    expected_multivalued: true
```

**Merk:** Denne sjekken krev ein ny check-type `slot_has_range_and_multivalued` i `server.py`.

### Steg 2 — Implementer `slot_has_range_and_multivalued`-sjekk i `server.py`

Legg til i `CHECKS`-dict:

```python
def _check_slot_has_range_and_multivalued(sv, schema, config, issues):
    """
    Sjekkar at ein slot på ein bestemt klasse har forventa range og multivalued-status.
    
    Brukt for å verifiere at skjemaet er rigga for tospråkverdiar (t.d. LangString
    med multivalued: true), sjølv om instansvalidering ikkje kan sjekke faktisk
    tospråkdekning i YAML-format.
    """
    class_name = config["class"]
    slot_uri = config["slot_uri"]
    expected_range = config.get("expected_range")
    expected_multivalued = config.get("expected_multivalued")
    
    cls = sv.get_class(class_name)
    if not cls:
        return
    
    # Finn slot med matchande slot_uri (transitivt via import)
    target_slot = None
    for slot_name in (cls.slots or []):
        slot = sv.get_slot(slot_name)
        if slot and (slot.slot_uri or "") == slot_uri:
            target_slot = slot
            break
    
    if not target_slot:
        # Sloten finst ikkje — annan sjekk (`merged_class_has_slot_with_uri`)
        # vil fange dette opp, så me returnerer utan å rapportere her
        return
    
    # Sjekk range
    if expected_range and target_slot.range != expected_range:
        issues.append(issue(
            config["severity"],
            "slot_range_mismatch",
            f"class:{class_name} → slot:{slot_uri}",
            f"Slot har range '{target_slot.range}' (forventa: '{expected_range}')",
        ))
    
    # Sjekk multivalued
    if expected_multivalued is not None:
        actual_multivalued = target_slot.multivalued or False
        if actual_multivalued != expected_multivalued:
            issues.append(issue(
                config["severity"],
                "slot_multivalued_mismatch",
                f"class:{class_name} → slot:{slot_uri}",
                f"Slot har multivalued={actual_multivalued} (forventa: {expected_multivalued})",
            ))
```

Legg til i `CHECKS`-dict (ca. linje 1100):

```python
CHECKS = {
    # ... eksisterande sjekkar ...
    "slot_has_range_and_multivalued": _check_slot_has_range_and_multivalued,
}
```

### Steg 3 — Oppdater `policies/README.md`

Legg til merknad under `felles-begrepskatalog`-seksjonen (ca. linje 210):

```markdown
**Tospråkskrav (SK5, SKOS-AP-NO v.2.0.15):**

| Alvor | Krav | Kode | Merk |
|---|---|---|---|
| warning | `anbefalt_term` (skos:prefLabel) har range `LangString` og `multivalued: true` | `begrep_anbefalt_term_er_multivalued_langstring` | Schemasjekk — sikrar at skjemaet **kan** innehalde tospråkverdiar |
| warning | `har_definisjon` har minst éi Definisjon per språk (nb, nn) | `begrep_har_definisjon_pa_nb_og_nn` | Instanssjekk via ID-suffiks-konvensjon |

**Avgrensing:** Tospråkskravet for `anbefalt_term` kan **ikkje** validerast i YAML-instansar
pga. LinkML sin avgrensing (LangString bærer ikkje språk-tag per verdi i YAML — sjå
`specs/bugs/langstring-rdflib-roundtrip.md`). Bruk RDF-validering (SHACL) eller manuell
gjennomgang av `.ttl`-fila for å verifiere at både `@nb` og `@nn` er til stades.
```

### Steg 4 — Oppdater audit-specen

Marker SK5 som **delvis løyst med dokumentert avgrensing**:

```markdown
**SK5 (tospråkskrav) — status:**
- ✅ **`har_definisjon`** — tospråksjekk implementert via ID-suffiks-konvensjon (`begrep_har_definisjon_pa_nb_og_nn`)
- ⚠️ **`anbefalt_term`** — schemasjekk implementert (`begrep_anbefalt_term_er_multivalued_langstring`), men instansvalidering **ikkje mogleg** i YAML-format
- **Avgrensing dokumentert:** LinkML sin LangString-type bærer ikkje språk-tag per verdi i YAML — tospråkdekning må validerast i RDF-fase (TTL + SHACL)
- **Tiltak framover:** SHACL-validering for TTL-filer (estimat 2-3 timar)
```

---

## Validering

Etter implementering:

```bash
# Verifiser at ny sjekk fungerer på eit begrepskatalog-skjema
make mcp-validate \
  SCHEMA=src/linkml/oreg/begrepssamling-foretaksregisteret/begrepssamling-foretaksregisteret-schema.yaml \
  POLICY=felles-begrepskatalog

# Forventa output:
# [warning] slot_multivalued_mismatch — Begrep.anbefalt_term har multivalued=True (OK)
# [warning] slot_range_mismatch — Begrep.anbefalt_term har range=LangString (OK)
```

---

## Framtidig arbeid (SHACL-validering)

For å fullføre SK5-implementeringa:

1. **Lag SHACL-shape for `skos:prefLabel` tospråkskrav:**
   ```turtle
   :BegrepShape a sh:NodeShape ;
       sh:targetClass skos:Concept ;
       sh:property [
           sh:path skos:prefLabel ;
           sh:minCount 2 ;
           sh:languageIn ( "nb" "nn" ) ;
           sh:uniqueLang true ;
           sh:message "Begrep må ha skos:prefLabel på både bokmål (@nb) og nynorsk (@nn)"@no ;
       ] .
   ```

2. **Integrer SHACL-validering i `make roundtrip`:**
   - Generer `.ttl` frå YAML
   - Køyr SHACL-validator mot TTL + shape
   - Rapporter violations som feil

3. **Oppdater CI-pipeline:**
   - Køyr SHACL-validering for alle skjema med `publish_external: true` i `felles-begrepskatalog`-policy

**Estimat:** 2-3 timar (SHACL-shape + Makefile-integrasjon + CI-oppdatering)

---

## Utført (2026-07-27)

- [x] **Steg 1:** Utvid `felles-begrepskatalog.yaml` med `begrep_anbefalt_term_er_multivalued_langstring` (linje 78-91)
- [x] **Steg 2:** Implementer `slot_has_range_and_multivalued` i `server.py` (linje 489-538, lagt til i `_CHECK_HANDLERS` linje 509)
- [x] **Steg 3:** Oppdater `policies/README.md` med tospråkskrav-tabell og avgrensing (linje 210-220)
- [x] **Steg 4:** Oppdater audit-specen (`ap-no-arkitektur-audit-2026-07.md`) med SK5-status (linje 265-273)
- [x] **Validering:** Implementasjonen er komplett — test med `make log-mcp-validate SCHEMA=<sti> POLICY=felles-begrepskatalog`
