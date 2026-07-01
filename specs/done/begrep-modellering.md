# Modellering av begreper i LinkML

## Bakgrunn og mål

Begreper som skal publiserast til Felles Begrepskatalog skal følgje
[SKOS-AP-NO-Begrep](https://informasjonsforvaltning.github.io/skos-ap-no-begrep/).
Målet er å:

1. Skrive begrepsinstansar i YAML-format med validering mot standarden
2. Generere SKOS/RDF (Turtle) for publisering til Felles Begrepskatalog
3. Bruke den same CI-pipeline som alle andre domenemodeller i repoet

---

## Kva finst allereie

`src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml` modellerer **alle klassar og
slots** frå SKOS-AP-NO-Begrep:

| Klasse | URI |
|---|---|
| `Begrep` | `skos:Concept` |
| `Definisjon` | `euvoc:XlNote` |
| `AssosiativRelasjon` | `skosno:AssociativeConceptRelation` |
| `GeneriskRelasjon` | `skosno:GenericConceptRelation` |
| `PartitivRelasjon` | `skosno:PartitiveConceptRelation` |
| `Samling` | `skos:Collection` |

Ein ny omgrepskatalog treng berre å **importere dette skjemaet** og legge til ein
containerklasse. All semantikk er allereie på plass.

---

## Filstruktur for ein ny omgrepskatalog

```
src/linkml/begrep/
└── <katalognavn>/
    ├── <katalognavn>-schema.yaml   ← berre import + containerklasse
    └── generate.yaml               ← skru på example_rdf

examples/begrep/
└── <katalognavn>-eksempel.yaml     ← sjølve begrepsinstansane
```

`<katalognavn>` bør reflektere organisasjonen eller fagdomenet,
t.d. `digdir-begrep`, `felles-datakatalog`, `ngr-begrep`.

---

## Identifikatorstrategi

Begreper som modellerast lokalt er **ikkje publiserte** enno og manglar permanente
URI-ar frå Felles Begrepskatalog. Bruk organisasjonens eige domene som base for
midlertidige URI-ar:

```
https://<org-domene>/begrep/<slug-eller-uuid>
```

Døme for Registerenheten i Brønnøysund: `https://begrep.brreg.no/foretaksnavn`

Etter import til Felles Begrepskatalog vert begrepsidentifikatoren:
```
https://data.norge.no/concepts/<uuid>
```

Organisasjonen vel sjølv om dei vil behalde eige domene eller bruke FBK-URI som
den kanoniske identifikatoren.

### Kva som IKKJE skal referere til Felles Begrepskatalog

Alle attributtane til eit begrep (utgjevar, kontaktpunkt, fagområde osv.) må ha
lokalt bestemte verdiar i datafila. **Einaste unntaket** er `sja_ogsa_omgrep`
(rdfs:seeAlso), som kan peike til relaterte begreper i andre katalogar.

| Attributt | Krav |
|---|---|
| `id` / `identifikator_literal` | Bruk org-eige domene som base |
| `utgjevar` | Enhetsregisteret-URI for eigen organisasjon er OK |
| `kontaktpunkt_vcard` | Definer lokalt i datafila |
| `fagomrade` | URI til eit LOS-tema under `https://psi.norge.no/los/ontologi/tema` |
| `sja_ogsa_omgrep` | **Kan** referere til `data.norge.no/concepts/<uuid>` |

---

## Skjema

Skjemaet er minimalt — all modellering ligg i `skos-ap-no`. Containaren treng
lister for alle objekttypar som kan opptre som sjølvstendige ressursar, inkludert
`Organisasjon` og `VCardKontakt` sidan desse må definerast lokalt i datafila:

```yaml
id: https://data.norge.no/linkml/<katalognavn>
name: <katalognavn>
title: <Organisasjon> - Begrepskatalog
version: "1.0.0"

prefixes:
  linkml: https://w3id.org/linkml/

default_prefix: https://data.norge.no/linkml/<katalognavn>/
default_range: string

imports:
  - linkml:types
  - ../../ap-no/skos-ap-no/skos-ap-no-schema

classes:
  BegrepContainer:
    tree_root: true
    attributes:
      begrep:
        range: Begrep
        multivalued: true
        inlined: true
        inlined_as_list: true
      samlingar:
        range: Samling
        multivalued: true
        inlined: true
        inlined_as_list: true
      definisjoner:
        range: Definisjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      generiske_relasjonar:
        range: GeneriskRelasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      partitive_relasjonar:
        range: PartitivRelasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      assosiative_relasjonar:
        range: AssosiativRelasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      organisasjonar:
        range: Organisasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      kontaktpunkt:
        range: VCardKontakt
        multivalued: true
        inlined: true
        inlined_as_list: true
```

### Kvifor fleire top-level-lister?

Repoet nyttar **lenking framfor inlining**: eit `Begrep` refererer til
`Organisasjon`- og `VCardKontakt`-objekt via URI, ikkje via innebygde objekt.
Desse objekta må difor stå som eigne innslag i sine respektive top-level-lister i
containaren — saman med `Begrep`, `Samling`, `Definisjon` og `*Relasjon`.

---

## `generate.yaml`

```yaml
generators:
  jsonld_context: true
  shacl: false
  python: false
  json_schema: true
  owl: false
  rdf: true
  protobuf: false
  erdiagram: true
  docs: true
  plantuml: false
  example_rdf: true    # ← VIKTIG: konverterer instansar til RDF/Turtle
```

`example_rdf: true` er det som gjer at `linkml-convert` køyrer på instansfila og
produserer SKOS/Turtle til `generated/begrep/<katalognavn>/`.

---

## Instansfil (YAML)

Instansfila (`examples/begrep/<katalognavn>-eksempel.yaml`) inneheld sjølve
begrepsdata. Nedanfor er tre begreper frå Registerenheten i Brønnøysund modellert
med lokale URI-ar — klare for validering og RDF-eksport, men **ikkje publiserte**
til Felles Begrepskatalog enno.

Dei illustrerer tre ulike situasjonar:
- `foretaksnavn` — enkelt begrep, definisjon henta direkte frå kjelde
- `nestleder` — fleirspråkleg begrep (nb, nn, en) med egendefinert definisjon
- `aksjeklasser` — begrep med merknad og eksempel, definisjon avleda frå kjelde

```yaml
# Tre begreper frå Registerenheten i Brønnøysund — under utvikling, ikkje publisert.
# Midlertidige URI-ar under brreg.no. Felles Begrepskatalog tildeler permanente
# URI-ar (data.norge.no/concepts/<uuid>) ved import.

# ── Begrep ────────────────────────────────────────────────────────────────────

begrep:

  # Foretaksnavn
  # Etter publisering: https://data.norge.no/concepts/5916c2a0-e5d3-31f7-b8d4-02938091f11f
  - id: https://begrep.brreg.no/foretaksnavn
    anbefalt_term:
      - foretaksnavn
    har_definisjon:
      - https://begrep.brreg.no/def/foretaksnavn-nb
    identifikator_literal: "https://begrep.brreg.no/foretaksnavn"
    kontaktpunkt_vcard:
      - https://begrep.brreg.no/kontakt/begrepsansvarleg
    utgjevar: https://data.norge.no/organizations/974760673
    fagomrade:
      - https://psi.norge.no/los/tema/naringsliv
    sja_ogsa_omgrep:
      - https://data.norge.no/concepts/68944a03-76d8-38f5-894e-88265d962b36
      - https://data.norge.no/concepts/e9074b72-758d-3500-bf6e-253a920a6900

  # Nestleder / nestleiar / deputy chair — fleirspråkleg, eitt definisjonsobjekt per språk
  # Etter publisering: https://data.norge.no/concepts/68944a03-76d8-38f5-894e-88265d962b36
  - id: https://begrep.brreg.no/nestleder
    anbefalt_term:
      - nestleder
      - nestleiar
      - deputy chair
    har_definisjon:
      - https://begrep.brreg.no/def/nestleder-nb
      - https://begrep.brreg.no/def/nestleder-nn
      - https://begrep.brreg.no/def/nestleder-en
    identifikator_literal: "https://begrep.brreg.no/nestleder"
    kontaktpunkt_vcard:
      - https://begrep.brreg.no/kontakt/begrepsansvarleg
    utgjevar: https://data.norge.no/organizations/974760673
    fagomrade:
      - https://psi.norge.no/los/tema/naringsliv

  # Aksjeklasser — med merknad og eksempel
  # Etter publisering: https://data.norge.no/concepts/e9074b72-758d-3500-bf6e-253a920a6900
  - id: https://begrep.brreg.no/aksjeklasser
    anbefalt_term:
      - aksjeklasser
    har_definisjon:
      - https://begrep.brreg.no/def/aksjeklasser-nb
    identifikator_literal: "https://begrep.brreg.no/aksjeklasser"
    kontaktpunkt_vcard:
      - https://begrep.brreg.no/kontakt/begrepsansvarleg
    utgjevar: https://data.norge.no/organizations/974760673
    fagomrade:
      - https://psi.norge.no/los/tema/naringsliv
    merknad:
      - I utgangspunktet skal alle aksjer gi lik rett i selskapet, men vedtektene kan bestemme at aksjene skal deles inn i forskjellige aksjeklasser.
    eksempel:
      - A-aksjer, b-aksjer, preferanseaksjer

# ── Definisjonsobjekt — eitt per begrep per språk ─────────────────────────────
# Bruk har_definisjon når kjeldetype (sitatdefinisjon, egendefinert, avleda) skal angis.
# Bruk heller slots definisjon: [...] for enkel fritekst utan kjeldemetadata.

definisjoner:

  - id: https://begrep.brreg.no/def/foretaksnavn-nb
    tekst: det offisielle navnet på en næringsdrivende juridisk person og kjennetegnet for et enkeltpersonforetak
    kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#direct-from-source

  - id: https://begrep.brreg.no/def/nestleder-nb
    tekst: styremedlem som opptrer som styreleder ved leders fravær
    kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#self-composed

  - id: https://begrep.brreg.no/def/nestleder-nn
    tekst: styremedlem som opptrer som styreleiar i fråværet til leiaren
    kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#self-composed

  - id: https://begrep.brreg.no/def/nestleder-en
    tekst: board member who acts as the chair in the absence of the chair.
    kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#self-composed

  - id: https://begrep.brreg.no/def/aksjeklasser-nb
    tekst: inndeling av aksjer som gir aksjene ulike rettigheter
    kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#derived-from-source

# ── Kontaktpunkt og utgjevar — definerast lokalt i datafila ───────────────────

kontaktpunkt:
  - id: https://begrep.brreg.no/kontakt/begrepsansvarleg

organisasjonar:
  - id: https://data.norge.no/organizations/974760673

# ── Samling ───────────────────────────────────────────────────────────────────

samlingar:
  - id: https://begrep.brreg.no/samlingar/registerbegrep-2025
    identifikator_literal: "https://begrep.brreg.no/samlingar/registerbegrep-2025"
    tittel:
      - Registerenheten i Brønnøysund - begrepskatalog 2025
    kontaktpunkt_vcard:
      - https://begrep.brreg.no/kontakt/begrepsansvarleg
    utgjevar: https://data.brreg.no/enhetsregisteret/api/enheter/974760673
    beskrivelse:
      - Begreper knytt til Enhetsregisteret, Foretaksregisteret og registerforvaltning.
    medlem:
      - https://begrep.brreg.no/foretaksnavn
      - https://begrep.brreg.no/nestleder
      - https://begrep.brreg.no/aksjeklasser
```

### Obligatoriske felt per `Begrep`

| Felt | Merknad |
|---|---|
| `id` | Lokal URI under org-eige domene |
| `anbefalt_term` | Minst éin per språk; nb og nn er obligatorisk per standarden |
| `definisjon` eller `har_definisjon` | Minst éin; bruk `har_definisjon` når kjeldetype skal angis |
| `identifikator_literal` | Same verdi som `id` (`dct:identifier`) |
| `kontaktpunkt_vcard` | URI til `VCardKontakt`-objekt definert lokalt i fila |
| `utgjevar` | URI til `Organisasjon`-objekt definert lokalt i fila |

### Fagområde (LOS)

`fagomrade` skal peike til eit tema i LOS (Linked Open Skjema for offentleg sektor).
ConceptScheme-en er `https://psi.norge.no/los/ontologi/tema`, og dei individuelle
temaa har URI-ar på forma:

```
https://psi.norge.no/los/tema/<slug>
```

Merk: LOS brukar ASCII i slug-ane — norske bokstavar vert translittererte
(`æ` → `a`, `ø` → `o`, `å` → `a`). Til dømes: `næringsliv` → `naringsliv`.

Fullstendig liste: `https://psi.norge.no/los/ontologi/tema.html`

Relevante tema for næringslivsdomenet:

| URI | Namn |
|---|---|
| `https://psi.norge.no/los/tema/naringsliv` | Næringsliv |
| `https://psi.norge.no/los/tema/naring` | Næring |
| `https://psi.norge.no/los/tema/naringsutvikling` | Næringsutvikling |
| `https://psi.norge.no/los/tema/handel-og-service` | Handel og service |
| `https://psi.norge.no/los/tema/arbeidsliv` | Arbeidsliv |

---

### `definisjon` vs. `har_definisjon`

`definisjon` (skos:definition) er enkel fritekst — bruk dette dersom kjeldetypen
ikkje er viktig:
```yaml
definisjon:
  - det offisielle navnet på en næringsdrivende juridisk person
```

`har_definisjon` (euvoc:xlDefinition) peikar til eit `Definisjon`-objekt og let deg
angi kjeldetype (`kjelde_relasjon`). Kjeldetypane er:

| URI-suffiks | Meining |
|---|---|
| `#direct-from-source` | Sitatdefinisjon — henta direkte frå kjelde |
| `#self-composed` | Egendefinert — formulert av verksemda sjølv |
| `#derived-from-source` | Avleda frå kjelde — basert på, men omformulert |

Prefiks: `https://data.norge.no/vocabulary/relationship-with-source-type`

### Fleirspråkleg begrep

For begrep med termar og definisjonar på fleire språk lagar ein eitt
`Definisjon`-objekt per språk og refererer alle frå `har_definisjon`-lista.
URI-ar for objekta konstruerast med eit `/def/<slug>-<språkkode>`-mønster.

### `sja_ogsa_omgrep` og eksterne referansar

`sja_ogsa_omgrep` (rdfs:seeAlso) er det **einaste** feltet som kan referere til
offentlege URI-ar frå Felles Begrepskatalog (`data.norge.no/concepts/<uuid>`).
Desse finst ikkje som eigne instansar i datafila — det er tilsikta. Lenkebasert
modellering medfører at validatoren berre krev syntaktisk gyldige URI-ar, ikkje
at dei er definerte lokalt.

### Komplekse relasjonar

For generiske relasjonar (over-/underomgrep) nyttast separate objekt:

```yaml
begrep:
  - id: https://begrep.brreg.no/underomgrep
    har_generisk_relasjon:
      - https://begrep.brreg.no/rel/underomgrep-overomgrep

generiske_relasjonar:
  - id: https://begrep.brreg.no/rel/underomgrep-overomgrep
    har_generisk_omgrep:
      - https://begrep.brreg.no/overomgrep
    har_spesifikt_omgrep:
      - https://begrep.brreg.no/underomgrep
    inndelingskriterium:
      - grad av formell registrering
```

---

## Validering

```bash
# Lint og instansvalidering (køyrer schema-lint + linkml-validate):
./tests/validate_schema.bash \
  src/linkml/begrep/<katalognavn>/<katalognavn>-schema.yaml \
  examples/begrep/<katalognavn>-eksempel.yaml

# MCP-validering mot bronze-policy (tilrår å starte her):
make mcp-validate \
  SCHEMA=src/linkml/begrep/<katalognavn>/<katalognavn>-schema.yaml \
  POLICY=bronze
```

---

## RDF-generering

Når `example_rdf: true` er sett i `generate.yaml` konverterer pipelinen
instansfila til RDF/Turtle:

```bash
make domain-gen-examples DOMAIN=begrep
```

Output: `generated/begrep/<katalognavn>/<katalognavn>-eksempel.ttl`

Denne Turtle-fila er SKOS-kompatibel og kan lastast opp til Felles Begrepskatalog
via [Begrepskatalog-API](https://fellesdatakatalog.digdir.no/docs/begrep-api).

---

## Steg-for-steg

```
1. Opprett filstruktur
   mkdir -p src/linkml/begrep/<katalognavn>
   mkdir -p examples/begrep

2. Skriv <katalognavn>-schema.yaml
   → Importer skos-ap-no, legg til BegrepContainer

3. Skriv generate.yaml
   → Set example_rdf: true

4. Skriv examples/begrep/<katalognavn>-eksempel.yaml
   → Start med eitt begrep og éi samling

5. Valider
   make mcp-validate SCHEMA=... POLICY=bronze

6. Generer RDF
   make domain-gen-examples DOMAIN=begrep

7. Iterér
   → Legg til fleire begrep, relasjonar og samlingar
   → Valider mot silver- og gold-policy etter kvart
```

---

## Avvegingar

**Lokale vs. permanente URI-ar**: Lokale URI-ar er stabile interne identifikatorar
som kan brukast som kanoniske URI-ar også etter import til FBK — FBK kan bruke dei
som-dei-er. Alternativt kan FBK minte nye URI-ar og dei lokale vert berre
`dct:identifier`-verdiar. Avklar dette med FBK før import.

**Definisjon som fritekst vs. objekt**: `definisjon` (skos:definition) er enklast og
dekker dei fleste behov. `har_definisjon` (euvoc:xlDefinition) nyttast berre når ein
treng å angi kjeldetype eller målgruppe eksplisitt.

**Språk**: SKOS-AP-NO krev at minst éin `anbefalt_term` og tilhøyrande `definisjon`
er i same språk. Standarden tilrår tilstedeværing på både bokmål og nynorsk.

**Relasjonar**: Generiske og partitive relasjonar modellerast som eigne objekt og
ikkje som direkte referansar mellom begrep. Dette er eit krav i SKOS-AP-NO.

**Omgrep vs. Begrepssamling**: Ein `Samling` er ikkje eit hierarki, men ei
namngitt gruppe. Hierarki modellerast med `GeneriskRelasjon`.
