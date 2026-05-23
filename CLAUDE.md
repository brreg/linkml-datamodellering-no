# CLAUDE.md

## Førende prinsipper
- Ingen avhengigheter skal installeres lokalt. Alt skal kjøres som containere med podman i WSL2.

## LinkML Importhierarki

```
linkml:types
    ↓
common-ap-no          ← bare AP-NO-profilene importerer denne direkte
    ↓
dcat-ap-no / dqv-ap-no / skos-ap-no / …
    ↓
domenemodeller        ← importerer AP-NO-profilene, ikke common-ap-no direkte

fint-common           ← bare FINT-domenemodellene importerer denne
    ↓
fint-administrasjon / fint-arkiv / …

oreg-modeller         ← offentlige registre (importerer AP-NO-profil(er) etter behov)

fair-metadata         ← kan importeres av alle domenemodeller
```

## Valider arbeidet ditt

```bash
# Lint og valider eksempel etter kvar endring i eit skjema:
./tests/validate_schema.bash ./src/linkml/samt/samt-bu/samt-bu-schema.yaml ./examples/samt/samt-bu-eksempel.yaml

# MCP-validator dersom dette er angitt av bruker:
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=gold
```

## Modelleringsprinsipper

### Modelleringsspråk
Standard modelleringsspråk er **norsk bokmål** — klasse- og slotnavn, beskrivelser og kommentarer skrives på bokmål. Unntaket er tekniske begreper som er fastsatt i en spesifikasjon (f.eks. `dcat:Dataset` → `Datasett`).

### Slots, ikke attributes
Alle domenemodellklassar modellerer eigenskapane sine som globale slots under `slots:` på toppnivå i skjemaet. Klasser refererer til slots via `slots:`-lista. Klassespesifikke innskrenkingar (`required`, `in_subset` o.l.) ligg i `slot_usage`.

**Unntaket er containerklassen** (`tree_root: true`): her skal kvar klasse-referanse modellerast som eit inline `attribute` direkte under containerklassen — ikkje som ein global slot. Containerklassen er eit serialiseringsankerpunkt, ikkje ein semantisk klasse, og attributtane hennar treng ikkje `slot_uri`.

```yaml
# Riktig — domeneklasse brukar globale slots
slots:
  tittel:
    slot_uri: dct:title
    range: string

classes:
  Datasett:
    slots:
      - tittel
    slot_usage:
      tittel:
        required: true

# Riktig — containerklassen brukar attributes
classes:
  Containerklasse:
    tree_root: true
    attributes:
      datasett:
        range: Datasett
        multivalued: true
        inlined: true
        inlined_as_list: true

# Feil — domeneklasse brukar attributes
classes:
  Datasett:
    attributes:
      tittel:
        slot_uri: dct:title
        range: string

# Feil — containerklassen brukar globale slots
slots:
  datasett:
    range: Datasett
    slot_uri: ex:datasett
    multivalued: true
    inlined: true
    inlined_as_list: true
```

### Lenking fremfor inlining
Alle klasser som kan opptre selvstendig får et `id`-slot med `identifier: true` og `range: uriorcurie`. Referanser til andre klasser har **ikke** `inlined: true` (som er standard når målklassen har en identifikator). Dette sikrer at instanser refereres med URI i stedet for å bygges inn.

### Klassenavn
Norske bokmålsnavn brukes for alle klasser (f.eks. `Datasett`, `Katalog`, `Distribusjon`). Hjelpeklasser for W3C-vokabulartermer kan bruke kortere engelske navn (`Begrep`, `Spraak`, `Mediatype`).

### Slot-uri og class-uri
Alle klasser og slots har eksplisitt `class_uri` / `slot_uri` som mapper til de korrekte RDF-vokabularene (dcat:, dct:, foaf:, vcard: osv.). `tree_root`-containerklasser er unntatt fra kravet om `class_uri`.

### Obligatorisk/anbefalt/valgfri
`slot_usage` med `in_subset` brukes for å markere om en egenskap er `Obligatorisk`, `Anbefalt` eller `Valgfri` i henhold til spesifikasjonen. `required: true` settes kun på obligatoriske egenskaper.

### Flerspråklige strenger
`LangString` (type `rdf:langString`) brukes for alle egenskaper som er definert som `rdf:langString` i spesifikasjonen (tittel, beskrivelse, nøkkelord osv.).

### Containerklasse
Alle toppnivå domenemodeller skal ha éin containerklasse med `tree_root: true`. Containerklassen er inngangspunktet for validering og serialisering.

Containerklassen brukar **`attributes:`** (ikkje `slots:`) for å referere til kvar klasse som kan serialiserast i tilhøyrande datafil:

```yaml
Containerklasse:
  tree_root: true
  attributes:
    datasett:          # attributtnamn i fleirtal
      range: Datasett
      multivalued: true
      inlined: true
      inlined_as_list: true
```

- Attributtnamna skrives alltid i **fleirtal** (t.d. `datasett`, `katalogar`, `aktørar`)
- `range` må peike på ein klasse definert i skjemaet eller importerte skjema
- Ingen `slot_uri` — containerattributtar er strukturelle, ikkje semantiske
- Containerklassen treng ikkje `class_uri` (unntatt frå kravet per bronze-policy)
- AP-NO-modellar og fair-modellar skal ikkje ha eigen containerklasse

### Endringer i koderepoet
Forsøk alltid å utføre minimale endringer som kun løser den spesifikke oppgava.

### Ny profil eller domenemodell
Sjå `specs/ny-domenemodell.md` for steg-for-steg-rettleiing.
