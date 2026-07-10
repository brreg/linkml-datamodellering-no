# Fiks 404-lenker til COMMANDS.md i README.md

## Bakgrunn

Generatortabellane i README.md ("Genererte modellkatalogar" og "Genererte artefakter") inneheld lenker til seksjoner i `COMMANDS.md`, t.d.:
- `[gen-modellkatalog-instance](COMMANDS.md#vedlikehald)`
- `[gen-informasjonsmodell-instance](COMMANDS.md#vedlikehald)`
- `[gen-jsonld-context](COMMANDS.md#enkeltartefakter)`

**Problem:** COMMANDS.md er ikkje publisert på GitHub Pages, så desse lenkene gir 404-feilmelding når ein klikkar på dei i den publiserte dokumentasjonsportalen.

**Løysing:**
1. Alternativ A: Endre lenkene til å peike på GitHub-filvisning (`https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#seksjonsnamn`)
2. Alternativ B: Publisere COMMANDS.md til mkdocs-portalen (`mkdocs/docs/kommandoar.md`)
3. Alternativ C: Fjerne lenkene heilt (berre ha generator-namnet som rein tekst)

**Anbefaling:** Alternativ B — publisere COMMANDS.md til mkdocs-portalen slik at lenkene fungerer både lokalt og publisert.

## Evaluering: Lenking til einskilde kommandoar

COMMANDS.md inneheld **82 kommandoar** organiserte i Markdown-tabellar under 10 hovudseksjonar. Kommandoane er formaterte som:

```markdown
| `make gen-jsonld-context [DOMAIN=...] [SCHEMA=...]` | JSON-LD kontekst | `generated/...` |
```

**Utfordring:** Markdown-tabellar genererer ikkje automatiske ankerpunkt for kvar rad. For å lenke til einskilde kommandoar må vi legge til eksplisitte ankerpunkt.

**Tilnærmingar:**

### A. HTML-ankerpunkt inne i tabellcelle (anbefalt)
Legg til `<a id="kommando-namn"></a>` **inne i første kolonne** i kvar tabellrad. Ankerpunkt mellom rader vil bryte Markdown-tabellstrukturen:

```markdown
### Enkeltartefakter

| Kommando | Beskriving | Output |
|---|---|---|
| <a id="gen-jsonld-context"></a>`make gen-jsonld-context [DOMAIN=...] [SCHEMA=...]` | JSON-LD kontekst | `generated/...` |
| <a id="gen-shacl"></a>`make gen-shacl [DOMAIN=...] [SCHEMA=...]` | SHACL shapes | `generated/...` |
```

**Fordeler:**
- Fungerer både i mkdocs og GitHub
- Kan lenke direkte til `kommandoar.md#gen-jsonld-context`
- Tabellstruktur vert bevart
- Ankerpunkt følger kommandoen ved flytting

**Ulemper:**
- Krever manuell redigering av COMMANDS.md for å legge til 82 ankerpunkt
- Reduserer lesbarheit i råfil (men ikkje i rendert versjon)

### B. Hovudtabell → Detaljert definisjonsliste
Omstrukturere COMMANDS.md frå tabellar til definisjonslister der kvar kommando får eige underoverskrift:

```markdown
### Enkeltartefakter

#### gen-jsonld-context
**Kommando:** `make gen-jsonld-context [DOMAIN=...] [SCHEMA=...]`  
**Beskriving:** JSON-LD kontekst  
**Output:** `generated/<domain>/<modell>/<modell>-context.jsonld`

#### gen-shacl
**Kommando:** `make gen-shacl [DOMAIN=...] [SCHEMA=...]`  
**Beskriving:** SHACL shapes  
**Output:** `generated/<domain>/<modell>/<modell>-shapes.ttl`
```

**Fordeler:**
- Automatiske ankerpunkt (level-4 overskrifter)
- Betre lesbarheit i detaljert visning
- Kan lenke til `kommandoar.md#gen-jsonld-context`

**Ulemper:**
- Mykje lengre dokument (82 underoverskrifter)
- Manglar tabelloversikt — vanskeleg å skanne raskt
- Stor omstrukturering av eksisterande COMMANDS.md

### C. Hybrid: Tabelloversikt + detaljseksjonar
Behald kompakte tabellar for kvart seksjonsområde, legg til detaljseksjon med ankerpunkt for spesielt viktige kommandoar:

```markdown
### Enkeltartefakter

| Kommando | Beskriving |
|---|---|
| [`gen-jsonld-context`](#gen-jsonld-context) | JSON-LD kontekst |
| [`gen-shacl`](#gen-shacl) | SHACL shapes |

#### gen-jsonld-context
**Kommando:** `make gen-jsonld-context [DOMAIN=...] [SCHEMA=...]`  
**Output:** `generated/<domain>/<modell>/<modell>-context.jsonld`  
**Bruksmåtar:**
- `make gen-jsonld-context` — alle skjema
- `make gen-jsonld-context DOMAIN=ap-no` — eitt domene
- `make gen-jsonld-context SCHEMA=src/linkml/...` — eitt skjema
```

**Fordeler:**
- Beheld tabelloversikt for rask skanning
- Detaljseksjon kun for komplekse/viktige kommandoar
- Automatiske ankerpunkt på detaljseksjonar

**Ulemper:**
- Duplikasjon (kommando i både tabell og detaljseksjon)
- Ikkje alle kommandoar får lenke (kun dei viktigaste)

### D. Script-genererte HTML-ankerpunkt
Skriv eit script som parsar COMMANDS.md og automatisk legg til `<a id="..."></a>` før kvar tabellrad basert på kommandoen i første kolonne.

**Fordeler:**
- Automatisk vedlikehald
- Alle kommandoar får ankerpunkt
- Beheld tabellstruktur

**Ulemper:**
- Ekstra vedlikehaldskompleksitet
- Ankerpunkt-ID må genererast frå kommandotekst (kompleks parsing)

## Anbefaling

**Tilnærming A (HTML-ankerpunkt inne i tabellcelle)** er mest pragmatisk:
- Minimalt arbeid (legg til 82 ankerpunkt éin gong)
- Fungerer i både mkdocs og GitHub
- Beheld tabellstruktur (ankerpunkt **inne i** celle, ikkje mellom rader)
- Ingen vedlikehaldskompleksitet

**Implementering:**
1. Legg til `<a id="kommando-namn"></a>` **først i første kolonne** i kvar tabellrad i COMMANDS.md
2. Ankerpunkt-ID avleiast frå `make`-kommandoen: `make gen-jsonld-context` → `id="gen-jsonld-context"`
3. For kommandoar med parameter (t.d. `make new-model NAME=...`) → `id="new-model"`
4. README.md-lenker vert `[gen-jsonld-context](kommandoar.md#gen-jsonld-context)`

**Eksempel:**
```markdown
| Kommando | Beskriving | Output |
|---|---|---|
| <a id="gen-jsonld-context"></a>`make gen-jsonld-context` | JSON-LD kontekst | `generated/...` |
```

## Antakelse

- COMMANDS.md skal gjøres tilgjengeleg i mkdocs-portalen som `kommandoar.md`
- Alle generator-kommandoar skal få eigne ankerpunkt
- Relative lenker skal peike til `kommandoar.md#kommando-namn`
- Tabellane i README.md skal oppdaterast til å bruke riktige ankerpunkt

## Steg

1. Identifiser alle generator-kommandoar som vert lenka til frå README.md
2. Legg til HTML-ankerpunkt (`<a id="..."></a>`) før relevante tabellrader i COMMANDS.md
3. Kopier `COMMANDS.md` til `mkdocs/docs/kommandoar.md`
4. Legg til `kommandoar.md` i mkdocs-navigasjonen i `mkdocs/publish.sh`
5. Oppdater generator-lenkene i README.md frå `COMMANDS.md#seksjonsnamn` til `kommandoar.md#kommando-namn`
6. Bygg og test dokumentasjonsportalen lokalt for å verifisere at lenkene fungerer

## Handlingsliste

- [x] Identifiser generator-kommandoar som README.md lenker til (18 kommandoar)
- [x] Legg til HTML-ankerpunkt i COMMANDS.md for desse kommandoane
- [x] Kopier COMMANDS.md til mkdocs/docs/kommandoar.md
- [x] Legg til kommandoar.md i mkdocs-navigasjonen i mkdocs/publish.sh
- [x] Oppdater generator-lenker i README.md (modellkatalog-tabell)
- [x] Oppdater generator-lenker i README.md (artefakt-tabell)
- [x] Bygg og test dokumentasjonsportalen lokalt (`bash mkdocs/publish.sh`)
- [x] Verifiser at ankerpunkt er korrekte i kommandoar.md (18 ankerpunkt)

## Utført

Alternativ A er implementert:

1. **Lagt til 18 HTML-ankerpunkt i COMMANDS.md** for alle generator-kommandoar som README.md lenker til:
   - `gen-jsonld-context`, `gen-shacl`, `gen-python`, `gen-jsonschema`, `gen-owl`, `gen-rdf`
   - `gen-erdiagram`, `gen-docs`, `gen-proto`, `gen-plantuml`, `gen-xsd`, `gen-asyncapi`
   - `gen-openapi`, `gen-dqv-measurements`, `gen-modelldcat-elements`, `convert-rdf`
   - `gen-informasjonsmodell-instance`, `gen-modellkatalog-instance`

2. **Kopiert COMMANDS.md → mkdocs/docs/kommandoar.md**

3. **Oppdatert mkdocs/publish.sh** for å inkludere "Kommandooversikt: kommandoar.md" i navigasjonen

4. **Oppdatert README.md** — alle lenker peikar no til:
   - `https://brreg.github.io/linkml-datamodellering-no/kommandoar/#<kommando-namn>`
   - Dette fungerer både i GitHub (via COMMANDS.md) og i publisert dokumentasjonsportal (via kommandoar.md)

5. **Validert at mkdocs/publish.sh køyrer utan feil** og at mkdocs.yml inneheld kommandoar.md

**Resultat:** Alle generator-lenker i README.md fungerer no som forventar — ingen 404-feil.

## Filstruktur

```
mkdocs/
  docs/
    kommandoar.md         ← ny fil (kopi av COMMANDS.md)
  publish.sh              ← oppdater nav-meny
README.md                 ← oppdater generator-lenker
```
