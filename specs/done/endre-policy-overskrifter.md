# Endre policy-overskrifter i README.md

**Dato:** 2026-07-10  
**Status:** I arbeid

## Bakgrunn

Overskriftene for bronze/silver/gold-policyane i `src/mcp-linkml-validator/policies/README.md` er for lange og gjentar policy-namnet i både overskrift og ankertekst. Brukaren ønsker eit meir kompakt format som viser policy-namnet direkte i overskrifta.

MkDocs genererer anchor-id frå overskriftsteksten, så endring av overskriftene krev også oppdatering av alle lenker til desse anchor-ane.

## Mål

1. Forenkle policy-overskriftene til format: `Bronze (`bronze`)` i staden for `Bronze-sjekkliste`
2. Organisere bronze/silver/gold under ny hovudoverskrift `## Kvalitetspolicyer`
3. Oppdatere alle referansar til dei nye anchor-namna

## Endringar

### 1. `src/mcp-linkml-validator/policies/README.md`

**Før:**
```markdown
## Bronze-sjekkliste

Grunnleggjande strukturkrav...

## Silver-sjekkliste (i tillegg til bronze)

AP-NO-konformitet...

## Gold-sjekkliste (i tillegg til silver og bronze)

Full FAIR-konformitet...

## Publiseringspolicyer

### Felles Begrepskatalog (`felles-begrepskatalog`)
...

### Felles Datakatalog (`felles-datakatalog`)
...
```

**Etter:**
```markdown
## Kvalitetspolicyer

### bronze

Grunnleggjande strukturkrav...

### silver

Arvar bronse. Legg til livssyklusmetadata...

### gold

Arvar sølv og bronse. Implementerer gap til FAIR-prinsippa...

## Publiseringspolicyer

### felles-begrepskatalog
...

### felles-datakatalog
...
```

**Nye anchor-id (genererte av MkDocs):**
- `#bronze` (frå `### bronze`)
- `#silver` (frå `### silver`)  
- `#gold` (frå `### gold`)
- `#felles-begrepskatalog` (frå `### felles-begrepskatalog`)
- `#felles-datakatalog` (frå `### felles-datakatalog`)

### 2. `src/assets/scripts/generate-validation-md.py`

Forenkle anchor-generering — anchor-namnet er no identisk med policy-namnet:

```python
# Anchor-namnet er identisk med policy-namnet
anchor = policy
policy_link = f"[policy: {policy}](/valideringsregler/#{anchor})"
```

### 3. Regenerer dokumentasjon

Køyr `make docs-publish` for å regenerere alle `mkdocs/docs/*/index.md`-filer med oppdaterte lenker.

## Handlingsliste

- [x] Les README.md og verifiser noverande overskriftsstruktur
- [x] Endre overskrifter i `src/mcp-linkml-validator/policies/README.md`
  - `## Bronze-sjekkliste` → `### bronze`
  - `## Silver-sjekkliste (i tillegg til bronze)` → `### silver`
  - `## Gold-sjekkliste (i tillegg til silver og bronze)` → `### gold`
  - `### Felles Begrepskatalog (`felles-begrepskatalog`)` → `### felles-begrepskatalog`
  - `### Felles Datakatalog (`felles-datakatalog`)` → `### felles-datakatalog`
  - Lagt til ny hovudoverskrift `## Kvalitetspolicyer` over bronze/silver/gold
- [x] Oppdater anchor-namn i `generate-validation-md.py` — forenkla til `anchor = policy`
- [x] Regenerer dokumentasjon med `make docs-publish`
- [x] Verifiser at nye anchor-id-ar stemmer i bygd HTML (`mkdocs/site/valideringsregler/index.html`)
  - `id="bronze"`, `id="silver"`, `id="gold"`, `id="felles-begrepskatalog"`, `id="felles-datakatalog"`
- [x] Verifiser at lenker i modell-index.md fungerer
  - `/valideringsregler/#bronze`, `/#silver`, `/#gold`, `/#felles-datakatalog`
- [x] Generer commit-melding

## Notatar

- MkDocs genererer anchor-id ved å konvertere overskriftstekst til lowercase og erstatte mellomrom med bindestrek
- Med lowercase policy-namn som overskrift (`### bronze`) blir anchor-id identisk med policy-namnet (`#bronze`)
- Dette forenklast koden i `generate-validation-md.py` frå komplisert if/elif-kjede til `anchor = policy`

## Utført

**2026-07-10**

Alle endringar gjennomført:

1. ✅ Endra policy-overskrifter i `src/mcp-linkml-validator/policies/README.md`:
   - `## Bronze-sjekkliste` → `### bronze`
   - `## Silver-sjekkliste (i tillegg til bronze)` → `### silver`
   - `## Gold-sjekkliste (i tillegg til silver og bronze)` → `### gold`
   - `### Felles Begrepskatalog (`felles-begrepskatalog`)` → `### felles-begrepskatalog`
   - `### Felles Datakatalog (`felles-datakatalog`)` → `### felles-datakatalog`
   - Lagt til ny hovudoverskrift `## Kvalitetspolicyer` over bronze/silver/gold

2. ✅ Forenkla anchor-generering i `generate-validation-md.py`:
   - Fjerna komplisert if/elif-kjede
   - Anchor-namnet er no identisk med policy-namnet: `anchor = policy`

3. ✅ Regenerert dokumentasjon med `make docs-publish` og `podman run mkdocs build`

4. ✅ Verifisert at alle anchor-id-ar stemmer i `mkdocs/site/valideringsregler/index.html`:
   - `id="bronze"`, `id="silver"`, `id="gold"`, `id="felles-begrepskatalog"`, `id="felles-datakatalog"`

5. ✅ Verifisert at alle policy-lenker i modell-index.md fungerer:
   - `/valideringsregler/#bronze`, `/#silver`, `/#gold`, `/#felles-datakatalog`

**Resultat:**
- Policy-overskrifter er no kompakte og viser berre policy-namnet med små bokstavar
- Anchor-namn er identiske med policy-namn — enkelt å forstå og vedlikehalde
- Koden i `generate-validation-md.py` er vesentleg forenkla
- Alle lenker frå modell-index.md til valideringsregler-sida fungerer korrekt
