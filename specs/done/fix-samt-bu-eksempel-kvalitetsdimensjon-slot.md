# Plan: fix samt-bu-eksempel — stale har_definisjon-slot på Kvalitetsdimensjon

## Bakgrunn

`make mcp-validate SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml POLICY=bronze`
gjev `"valid": false` med 1 feil:

```
{
  "severity": "error",
  "code": "jsonschema validation",
  "target": "SamtBuContainer[0]",
  "message": "{'id': 'dqv:kvalitetsdim-completeness', 'har_anbefalt_term': [...],
    'har_definisjon': [...], 'gjelder_standard': [...]} is not valid under any
    of the given schemas in /kvalitetsdimensjoner/0"
}
```

**Rotårsak:** Commit `6fb9badc` («legg til DQV-kvalitetsmålingar») omdøypte
slotet `har_definisjon` → `har_kvalitetsdefinisjon` på klassen
`Kvalitetsdimensjon` i `src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml`
(for å løyse ein slot-namnekollisjon med `har_definisjon` på `Begrep` —
BUG-7-variant). Alle andre eksempelfiler som brukar `Kvalitetsdimensjon`
(`dqv-ap-no-eksempel.yaml`) vart oppdatert i same commit, men
`src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml` linje 99–105 vart
ikkje retta:

```yaml
kvalitetsdimensjoner:
  - id: dqv:kvalitetsdim-completeness
    har_anbefalt_term:
      - completeness
    har_definisjon:                       # ← skal vere har_kvalitetsdefinisjon
      - "https://data.norge.no/vocabulary/quality-dimension#completeness"
    gjelder_standard:
      - dqv:dcat-ap-no
```

Verifisert med `grep -rn "har_definisjon\b" src/linkml/samt/` — dette er det
einaste gjenværande tilfellet av det gamle slotnamnet brukt på ein
`Kvalitetsdimensjon`-instans i heile repoet.

**39 warnings** (`all_classes_have_concept_ref` — manglar
`annotations.begrepsidentifikator`) er **ikkje** del av dette tiltaket. Dette
er ein kjend, akseptert baseline-warning for modellar som ikkje er knytte til
Felles begrepskatalog (jf. Digdir-regel 13, allerede kartlagt i
`specs/backlog/avvik-veileder-modelldcat-ap-no.md` og
`specs/done/avvik-felles-modelleringsregler.md`). Dei påvirkar ikkje
`valid`-resultatet og krev eit eige, repo-omfattande tiltak — ikkje ein
punktfiks i samt-bu.

---

## Steg

1. ✓ **Rett slotnamn i eksempelfila**
   `src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml` linje 102:
   `har_definisjon:` → `har_kvalitetsdefinisjon:`. Utført som planlagt, ingen avvik.

2. ✓ **Re-valider**
   ```bash
   make mcp-validate SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml POLICY=bronze
   ```
   Resultat: `"valid": true`, `"errorCount": 0`, `"warningCount": 39`
   (uendra, som forventa). Utført som planlagt, ingen avvik.

3. ✓ **Roundtrip-verifisering**
   ```bash
   make roundtrip SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml
   ```
   Resultat: `roundtrip-json` → OK. `roundtrip-ttl` → FEIL, men dette er
   **BUG-3** (`specs/bugs/mappingerror-rdflib-roundtrip.md`), ein kjend,
   allerede dokumentert `rdflib_loader`-feil (`MappingError: No pred for
   https://data.norge.no/samt/samt-bu/id`) som listar `samt-bu` som eit av dei
   berørte skjemaa — uavhengig av denne fiksen, ingen regresjon. Avvik frå
   plan: forventa "framleis serialiserer korrekt til JSON/TTL" var feil
   premiss for TTL — BUG-3 var ukjend for planleggjar på skrivetidspunktet for
   steg 3, men er allerede dokumentert og ute av scope for dette tiltaket.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Type |
|---|---|---|---|
| 1 | Omdøyp `har_definisjon` → `har_kvalitetsdefinisjon` på Kvalitetsdimensjon-instans | `src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml` | Fix |
| 2 | Re-køyr bronze-validering | — | Verifikasjon |
| 3 | Roundtrip-sjekk (JSON+TTL) | — | Verifikasjon |

---

## Avhengigheiter

- Ingen skjemaendringar — feilen ligg berre i eksempeldata, ikkje i
  `samt-bu-schema.yaml` eller `dqv-core-schema.yaml`.
- Ingen nye container-images eller CI-endringar nødvendig.
- Uavhengig av dei 39 begrepsidentifikator-warningane (sjå Bakgrunn).

---

## Utført

Alle 3 steg utførte som planlagt:

1. `har_definisjon:` → `har_kvalitetsdefinisjon:` retta på
   `Kvalitetsdimensjon`-instansen i
   `src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml`.
2. Bronze-revalidering: `errorCount` 1 → 0, `valid: true`.
   `warningCount` uendra (39, kjend baseline — sjå Bakgrunn).
3. Roundtrip: `roundtrip-json` OK. `roundtrip-ttl` feiler, men dette er
   **BUG-3** (`specs/bugs/mappingerror-rdflib-roundtrip.md`) — ein allerede
   dokumentert, ikkje-relatert `rdflib_loader`-feil som allerede lista
   `samt-bu` som berørt skjema før dette tiltaket starta. Ingen regresjon
   introdusert av denne fiksen.
