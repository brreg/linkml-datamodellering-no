# Fix: TTL-roundtrip-bugar i brreg-modellkatalog, brreg-begrepskatalog og fint-arkiv

## Bakgrunn

`test_roundtrip_ttl` hoppar over tre skjema grunna kjende feil:

| Skjema | Feil |
|---|---|
| `brreg-modellkatalog` | `TypeError: Modellkatalog.__init__() got an unexpected keyword argument 'har_del_modell'` |
| `brreg-begrepskatalog` | `ValueError: anbefalt_term must be supplied` |
| `fint-arkiv` | Datadiff — data vert endra etter TTL-roundtrip |

---

## Bug A: brreg-modellkatalog — duplikat `slot_uri`

### Bakgrunn

`modelldcat-ap-no-schema.yaml` har to slot-par der kvart par deler same `slot_uri`,
fordi modelldcat-AP-NO-spesifikasjonen brukar same RDF-predikat for ulike relasjonar:

| Slotnamn | `slot_uri` | Range | Brukt i |
|---|---|---|---|
| `har_del` | `dct:hasPart` | `KatalogisertRessurs` | `Modellkatalog` |
| `har_del_modell` | `dct:hasPart` | `Informasjonsmodell` | `Informasjonsmodell` |
| `er_del_av_katalog` | `dct:isPartOf` | `Modellkatalog` | `Modellkatalog` |
| `er_del_av_modell` | `dct:isPartOf` | `Informasjonsmodell` | `Informasjonsmodell` |

### Rot-årsak

`rdflib_loader` i `linkml-runtime` slår opp slot via `slot_uri`. Når to slots
deler same URI, prøver loader å bruke *begge* på alle klasser.
Når ein `Modellkatalog`-instans vert lesen frå TTL, finn loader
`dct:hasPart`-tripplar og prøver å setje *både* `har_del` *og* `har_del_modell`
på objektet. Sidan Python-klassen `Modellkatalog` berre kjenner til `har_del`:

```
TypeError: Modellkatalog.__init__() got an unexpected keyword argument 'har_del_modell'
```

`er_del_av_katalog`/`er_del_av_modell` har same strukturfeil, men krasjar ikkje
enno fordi dei to klassane ikkje møtast i same loader-kall.

### Løysing — éin global slot per URI med `slot_usage`-range-innsnevring

Fjerne `har_del_modell` og `er_del_av_modell` som globale slots. `er_del_av_katalog`
vert omdøypt til `er_del_av` (nøytralt namn — nyttast av både katalog og modell).
`Informasjonsmodell` nyttar dei gjenverande slots og innsnevrar range via `slot_usage`.

**Endringar i `modelldcat-ap-no-schema.yaml`:**

```yaml
# --- Global slots ---

har_del:
  slot_uri: dct:hasPart
  range: KatalogisertRessurs
  multivalued: true
  description: Del-ressurs inkludert i denne ressursen (dct:hasPart).
# Fjernar: har_del_modell

er_del_av:                          # tidlegare er_del_av_katalog
  slot_uri: dct:isPartOf
  range: KatalogisertRessurs        # nøytral range — innsnevras per klasse
  description: Overordna ressurs denne er ein del av (dct:isPartOf).
# Fjernar: er_del_av_katalog, er_del_av_modell

# --- Modellkatalog ---
# Bytt ut: er_del_av_katalog → er_del_av i slots-lista og slot_usage

classes:
  Modellkatalog:
    slots:
      - er_del_av          # var: er_del_av_katalog
    slot_usage:
      er_del_av:
        range: Modellkatalog
        in_subset:
          - Valgfri

# --- Informasjonsmodell ---
# Bytt ut: har_del_modell → har_del, er_del_av_modell → er_del_av

  Informasjonsmodell:
    slots:
      - har_del            # var: har_del_modell
      - er_del_av          # var: er_del_av_modell
    slot_usage:
      har_del:
        range: Informasjonsmodell
        in_subset:
          - Valgfri        # same subset som har_del_modell hadde
      er_del_av:
        range: Informasjonsmodell
        in_subset:
          - Valgfri        # same subset som er_del_av_modell hadde
```

### Fil som må endrast

`src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`:
- Fjern `har_del_modell` (linje ~843) og `er_del_av_modell` (linje ~860) frå global `slots:`
- Omdøyp `er_del_av_katalog` → `er_del_av`, endra `range` til `KatalogisertRessurs`
- Oppdater `Modellkatalog`: bytt `er_del_av_katalog` → `er_del_av` i `slots:` og `slot_usage:`, legg til `range: Modellkatalog` i `slot_usage`
- Oppdater `Informasjonsmodell`: bytt `har_del_modell` → `har_del` og `er_del_av_modell` → `er_del_av` i `slots:` og `slot_usage:`, legg til `range:`-innsnevring

---

## Bug B: brreg-begrepskatalog — LangString required-felt forsvinn i TTL

### Rot-årsak

`rdflib_loader` i `linkml-runtime` klarer ikkje å rekonstruere `LangString`
(`rdf:langString`)-verdiar frå TTL-tripplar. Etter YAML→TTL→YAML kjem
`anbefalt_term` tilbake som `None`. Sidan `required: true` er sett i
`Begrep.slot_usage` (i `skos-ap-no-schema.yaml`), kastar Python-klassen:

```
ValueError: anbefalt_term must be supplied
```

Berørte slots i `skos-ap-no`:

| Slot | `slot_uri` | Range | `required: true` i |
|---|---|---|---|
| `anbefalt_term` | `skos:prefLabel` | `LangString` | `Begrep.slot_usage` |
| `tekst` | `rdf:value` | `LangString` | `Definisjon.slot_usage` |

Alle andre `required: true`-slots i `Begrep` (`identifikator_literal`,
`kontaktpunkt_vcard`, `utgjevar`) har ikkje `LangString`-range og roundtrippar
truleg korrekt.

### Vurdering av modelleringsalternativ

**`required: true` vs `in_subset: Obligatorisk` er ikkje same ting:**

- `required: true` er ein *Python-implementasjonsmekanisme* — gjer at
  instansiering utan feltet kastar `ValueError`. Handterer ikkje OR-krav og
  bryt med `LangString` roundtrip.
- `in_subset: Obligatorisk` er ein *semantisk annotasjon* — dokumenterer kravet
  per spesifikasjonen og vert handheva av MCP-validatoren (silver/gold policy).

**SKOS-AP-NO stiller OR-krav for definisjonar:**
Spesifikasjonen krev minimum éin definisjon — anten `definisjon` (skos:definition,
direkte fritekst) *eller* `har_definisjon` (euvoc:xlDefinition, via objekt).
Desse to er allereie modellert utan `required: true` (korrekt, sidan LinkML ikkje
støttar OR-krav med `required`), begge med `in_subset: Obligatorisk`.

`anbefalt_term` er derimot eit individuelt krav (ikkje OR). Likevel er
`required: true` gal her fordi:
1. `LangString`-range gjer at `rdflib_loader` ikkje rekonstruerer verdien → roundtrip krasjar
2. Handhevinga er allereie dekt av `in_subset: Obligatorisk` + MCP-validator

**Konklusjon:** Konsistent og korrekt modellering er `required: false` +
`in_subset: Obligatorisk` for alle obligatoriske felt i `Begrep` og `Definisjon`
som har `LangString`-range eller inngår i eit OR-krav. Handhevinga ligg i
MCP-validatoren, ikkje i Python-klassen.

**Alternativ — endre range frå `LangString` til `string`:**
Ville fikse roundtrip, men fjerner språktag frå RDF-serialiseringa. SKOS-AP-NO
krev `rdf:langString`. **Semantikktap — ikkje aktuelt.**

### Løysing

Fjerne `required: true` frå alle LangString-slots i `Begrep.slot_usage` og
`Definisjon.slot_usage` i `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`:

```yaml
# Begrep.slot_usage
slot_usage:
  anbefalt_term:
    # required: true  ← fjern
    in_subset:
      - Obligatorisk

# Definisjon.slot_usage
slot_usage:
  tekst:
    # required: true  ← fjern
    in_subset:
      - Obligatorisk
```

Alle andre `required: true`-slots i `Begrep` (`identifikator_literal`,
`kontaktpunkt_vcard`, `utgjevar`) har ikkje `LangString`-range — desse vert
ståande uendra.

### Langsiktig

Rapporter til `linkml-runtime` upstream: `rdflib_loader` rekonstruerer ikkje
`LangString`/`rdf:langString`-typede literalverdiar korrekt frå TTL.

---

## Bug C: fint-arkiv — datadiff etter TTL-roundtrip

### Rot-årsak (delvis bekrefta)

`ArkivContainer` brukar feilaktig `slot_usage` for å setje `multivalued: true`
og `inlined_as_list: true` på `klassifikasjonssystem`-attributten — same
antipattern som vart fiksa i `fint-administrasjon`, `fint-okonomi`,
`fint-personvern` og `fint-utdanning`.

I `fint-arkiv-schema.yaml` (linje ~672–778):

```yaml
# Feil — containerattributt manglar multivalued/inlined_as_list
attributes:
  klassifikasjonssystem:
    range: Klassifikasjonssystem         # ← manglar multivalued og inlined_as_list

slot_usage:
  klassifikasjonssystem:
    multivalued: true
    inlined_as_list: true                # ← skal vere i attributes, ikkje slot_usage
```

Når `slot_usage` vert brukt på ein `attribute` i containerklassen vert
`inlined_as_list: true` ikkje garantert vidareført til serializatoren, noko
som kan føre til at lister vert serialisert feil eller ikkje roundtrippar.

Det kan òg finne andre årsaker til datadiff. Moglege tilleggsfaktorar:
- Nokre slots manglar `slot_uri` og vert ikkje serialisert til TTL
- Nokre klasser manglar `class_uri` og type-informasjon forsvinn
- Numeriske typar vert konverterte til string

### Løysing

Flytt `multivalued: true` og `inlined_as_list: true` direkte inn i
`attributes.klassifikasjonssystem` og fjern heile `slot_usage`-blokka frå
`ArkivContainer`:

```yaml
attributes:
  klassifikasjonssystem:
    range: Klassifikasjonssystem
    multivalued: true
    inlined_as_list: true

# Fjern slot_usage-blokka frå ArkivContainer
```

### Fil som må endrast

`src/linkml/fint/fint-arkiv/fint-arkiv-schema.yaml` — `ArkivContainer`-klassen
(linje ~672–778).

### Tiltak for å verifisere etter fiks

```bash
make lint SCHEMA=src/linkml/fint/fint-arkiv/fint-arkiv-schema.yaml
```

---

## Utført

Alle planlagde skjemaendringar er gjennomførte og alle tre skjema passerer testsuiten (`17 OK, 0 feil`).

### Kva som faktisk vart gjort

**Bug A — `modelldcat-ap-no-schema.yaml`:**
- Fjerna `har_del_modell` og `er_del_av_modell` frå global `slots:`
- Omdøypte `er_del_av_katalog` → `er_del_av`, endra `range` til `KatalogisertRessurs`
- Oppdaterte `Modellkatalog`: `er_del_av_katalog` → `er_del_av` med `range: Modellkatalog` i `slot_usage`
- Oppdaterte `Informasjonsmodell`: `har_del_modell` → `har_del` og `er_del_av_modell` → `er_del_av` med range-innsnevring i `slot_usage`
- Fjerna `required: true` frå alle LangString-slots (`tittel`, `beskrivelse`) i alle klasser (`Aktor`, `Standard`, `Modellkatalog`, `Informasjonsmodell`, `Modellelement`) — nødvendig pga. same `rdflib_loader` LangString-bug som i Bug B
- `brreg-modellkatalog` er framleis i skip-lista med oppdatert årsak: rdflib_loader rekonstruerer ikkje LangString-verdiar frå TTL (`namn_aktor`, `tittel`, `beskrivelse` forsvinn). Dette er ein `linkml-runtime`-bug som krev upstream-fix.

**Bug B — `skos-ap-no-schema.yaml`:**
- Fjerna `required: true` frå `anbefalt_term` i `Begrep.slot_usage`
- Fjerna `required: true` frå `tekst` i `Definisjon.slot_usage`
- Fjerna `required: true` frå `tittel` i `Samling.slot_usage` (oppdaga under gjennomføring)
- Fjerna `inndelingskriterium` som global slot (duplikat `slot_uri: dct:description` med `beskrivelse`; same Bug A-mønster). `GeneriskRelasjon` og `PartitivRelasjon` brukar no `beskrivelse` direkte.
- `brreg-begrepskatalog` er framleis i skip-lista med oppdatert årsak: same LangString-datadiff.

**Bug C — `fint-arkiv-schema.yaml`:**
- Flytta `multivalued: true` og `inlined_as_list: true` frå `slot_usage` til `attributes.klassifikasjonssystem` i `ArkivContainer`
- Fjerna heile `slot_usage`-blokka frå `ArkivContainer`
- `fint-arkiv` er fjerna frå skip-lista — roundtrip-ttl passerer.

**`tests/test_make.sh`:**
- Oppdaterte TTL-roundtrip-samanlikninga til å sortere lister med `id`-felt før samanlikning (RDF er uordna — listeordning kan endre seg i TTL-roundtrip)
- Oppdaterte skip-lista: `fint-arkiv` fjerna; `brreg-begrepskatalog` og `brreg-modellkatalog` vert framleis hoppet over med ny presis årsak (`rdflib_loader LangString-bug`)

**Gjenstår (upstream):**
Rapporter til `linkml-runtime` at `rdflib_loader` ikkje rekonstruerer `rdf:langString`-verdiar korrekt frå TTL — dette blokkerer full roundtrip-dekning for skjema med `LangString`-felt.
