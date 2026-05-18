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
Alle egenskaper modelleres som globale slots under `slots:` på toppnivå i skjemaet — aldri som `attributes:` inne i en klasse. Klasser refererer til slots via `slots:`-listen. Klassespesifikke innskrenkninger (`required`, `in_subset` o.l.) legges i `slot_usage` på klassen.

```yaml
# Riktig
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

# Feil
classes:
  Datasett:
    attributes:
      tittel:
        slot_uri: dct:title
        range: string
        required: true
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
Alle toppnivå domenemodeller skal ha Containerklasse som har eit attributt for hver klasse som kan serialiseres i tilhørende datasettfil.
Containerklassens attributter skrives alltid i flertallsform.
Alle verdiområde/range for attributter må mappes til linkml klasser definert i skjema eller inkluderte skjema, eller linkml innebygde typar.
Alle containerslots skal ha:
    multivalued: true
    inlined: true
    inlined_as_list: true
Alle ap-no modeller og fair modeller skal alltid inkluderes i en annen domenemodell, og skal derfor ikkje ha eigen Containerklasse.

### Endringer i koderepoet
Forsøk alltid å utføre minimale endringer som kun løser den spesifikke oppgava.

### Ny profil eller domenemodell
Sjå `docs/ny-domenemodell.md` for steg-for-steg-rettleiing.
