# Rettleiing: ny domenemodell

!!! note "Beskrivelse"

    Denne rettleiinga viser korleis du oppretter ein ny domenemodell i repoet —
    frå filstruktur til RDF-eksport klar for Felles Datakatalog.

!!! tip "Kor passar dette inn i «Orden i eget hus»?"

    Dersom organisasjonen din følgjer Digdir sin veileder
    [«Orden i eget hus»](https://www.digdir.no/informasjonsforvaltning/veileder-orden-i-eget-hus/2716),
    dekkjer denne rettleiinga steg 3 (kartlegge — modellere datasett og begrep i LinkML),
    steg 5 (beskrive — DCAT-AP-NO/SKOS-AP-NO-metadatafelt) og steg 6
    (tilgjengeleggjere — pull-basert publisering til Felles datakatalog/begrepskatalog).
    Steg 1 (planlegge), 2 (prioritere) og 4 (vurdere tilgangsnivå) er organisatoriske
    avklaringar som bør vere gjorde i eiga verksemd før de startar her — sjå
    [steg 1](https://www.digdir.no/informasjonsforvaltning/steg-1-planlegge/2718),
    [steg 2](https://www.digdir.no/informasjonsforvaltning/steg-2-prioritere/2719) og
    [steg 4](https://www.digdir.no/informasjonsforvaltning/steg-4-vurdere-tilgangsniva/2723).


## 0 — Sjekk føresetnader og bygg images (éin gong)

```bash
make check-prereqs
make build-docker-linkml && make build-docker-python && make build-docker-mcp-validator
```

## 1a. — Scaffold

```bash
make new-modell NAME=<modell> DOMAIN=<domain>
```

Dette oppretter:
```
src/linkml/<domain>/<modell>/
├── <modell>-schema.yaml       ← hovudskjema med stub-klasse og containerklasse
├── build.yaml              ← publiserings- og generatorkonfig
├── description.md             ← valfri beskrivelse av modellen (10–20 liner), injiserast i portal-index før metadata-tabellen
└── examples/
    └── <modell>-eksempel.yaml ← eksempelfil med minimal instans
```




For `make new-modell NAME=tilskudd DOMAIN=eksempel` ser dei genererte filene slik ut:

**`tilskudd-schema.yaml`**

```yaml
id: https://data.norge.no/eksempel/tilskudd
name: tilskudd
title: 'TODO: tittel for tilskudd'
description: Generert modell for 'tilskudd'.
version: 0.1.0
license: https://data.norge.no/nlod/no/2.0  # Andre gyldige lisensar: https://brreg.github.io/linkml-datamodellering-no/ap-no/common-ap-no/klasser/eulicence/
annotations:
  utgiver: https://data.norge.no/organizations/<orgnr>
  endringsdato: '<dagens dato>'
  utgivelsesdato: '<dagens dato>'
  status: http://purl.org/adms/status/UnderDevelopment

prefixes:
  linkml:   https://w3id.org/linkml/
  tilskudd: https://data.norge.no/eksempel/tilskudd/
  dct:      http://purl.org/dc/terms/
  dcat:     http://www.w3.org/ns/dcat#
  foaf:     http://xmlns.com/foaf/0.1/
  skos:     http://www.w3.org/2004/02/skos/core#
  xsd:      http://www.w3.org/2001/XMLSchema#
  rdf:      http://www.w3.org/1999/02/22-rdf-syntax-ns#
  rdfs:     http://www.w3.org/2000/01/rdf-schema#

default_prefix: https://data.norge.no/eksempel/tilskudd/
default_range: string

imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v2.13.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema  # TODO: endre/legg til imports etter behov

subsets:
  Obligatorisk:
    description: Obligatoriske eigenskapar.
  Anbefalt:
    description: Anbefalte eigenskapar.
  Valgfri:
    description: Valfrie eigenskapar.

classes:
  TilskuddContainer:
    description: containerklasse for serialisering av klasser i tilskudd modellen
    tree_root: true
    attributes:
      tilskudder:
        description: TODO: beskriv eigenskapen
        range: Tilskudd
        multivalued: true
        inlined: true
        inlined_as_list: true

  Tilskudd:                        # ← stub — alt PascalCase, men gi han eit meir meiningsfullt namn
    description: TODO: beskriv klassen
    class_uri: tilskudd:tilskudd   # ← byt med faktisk vokabular-URI
    annotations:
      begrepsidentifikator: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
    slots:
      - id

slots:
  tilskudd_kontaktinformasjon:
    description: Kontaktinformasjon for ressursen.
    slot_uri: dcat:contactPoint
    range: uriorcurie

# TODO: Gi stub-klassen eit meir meiningsfullt namn.
# TODO: Legg til slots og slot_usage for eigenskapane i modellen.
```

`id`-sloten er ikkje lokalt definert i utkastet — han vert arva via
`dcat-ap-no` sitt importerte `common-ap-no`-import, som har det delte
`id`-slotet (`identifier: true`, `range: uriorcurie`). `tilskudd_kontaktinformasjon`-sloten
vert generert globalt, prefiksa med skjemaet sitt eige, unike namn
(`tilskudd`) — strukturelt kollisjonsfritt mot alle faste AP-NO-vokabularslot
(t.d. det importerte `kontaktpunkt`-slotet frå `dcat-ap-no`, som har ein
annan `range`), sidan ingen AP-NO-profil nokon gong vil bruke akkurat ditt
skjemanamn som prefiks. Sloten er
**ikkje** automatisk lagt til i stub-klassen sin `slots:`-liste
(`dcat:contactPoint` høyrer typisk til datasett-/distribusjonsliknande
klassar, ikkje naudsynleg det generiske domenestubbet) — legg han til i
klassar der det er relevant.

**Kva TODO-stubbane betyr**

| Stubb | Kva som skal inn |
|-------|-----------------|
| `title: 'TODO: tittel for …'` | Norsk bokmål-tittel, t.d. `Tilskuddsregister` |
| `class Tilskudd` (generisk namn) | Gi klassen eit meir meiningsfullt norsk namn, t.d. `Tilskuddsvedtak` (namnet er alt PascalCase) |
| `class_uri: tilskudd:tilskudd` | Faktisk RDF-URI, t.d. `dcat:Dataset` eller eigen namespace |
| `begrepsidentifikator: …/TODO` | URI frå [data.norge.no/concepts](https://data.norge.no/concepts) |
| `description: TODO: beskriv klassen` | Norsk skildring av kva klassen representerer |
| `dcat-ap-no`-importet (TODO-kommentar på importlina) | `dcat-ap-no` er alt sett som standard AP-NO-profil, versjonslåst til ein konkret git-tag. Byt til ein annan profil eller legg til fleire imports dersom `dcat-ap-no` sine felles slots ikkje dekkjer behovet |
| `license: https://data.norge.no/nlod/no/2.0` | Alt sett til standard (NLOD 2.0) — byt berre dersom modellen krev ein annan lisens, sjå [gyldige lisensar](https://brreg.github.io/linkml-datamodellering-no/ap-no/common-ap-no/klasser/eulicence/) |
| `annotations.utgiver` | Auto-utleidd frå `CODEOWNERS.md` sitt `path_patterns`-oppslag for `DOMAIN`. Vert `https://data.norge.no/organizations/TODO` dersom domenet ikkje har ein registrert eigar der (skript skriv ei åtvaring til stderr i så fall) |
| `annotations.endringsdato`/`utgivelsesdato` | Sett til dagens dato automatisk — juster ved behov |
| `annotations.status` | Alt sett til `UnderDevelopment` («Under utarbeidelse») — oppdater etter kvart som modellen modnar (sjå ADMS-status-tabellen i `CLAUDE.md`) |

`build.yaml` og `description.md` vert òg oppretta med standardinnhald — sjå [Modellmanifest](build-config.md) for feltliste.




**`examples/tilskudd-eksempel.yaml`**

```yaml
# Eksempel for tilskudd
# Tilpass instansane med reelle verdiar etter at skjemaet er ferdigstilt.
---
tilskudder:
  - id: tilskudd:eksempel-1
```



---

## 1b. (om ønskjeleg) Generer frå eksisterande JSON Schema
Legg JSON Schema-filen i tmp/, t.d. `tmp/modell.json`

```bash
make mcp-linkml-modell-utkast SCHEMA=tmp/modell.json
# Silver-annotasjonar (utgiver, endringsdato, status) automatisk:
make mcp-linkml-modell-utkast SCHEMA=tmp/modell.json PROFILE=silver
```

→ genererer `tmp/modell-schema.yaml` og køyrer **automatisk roundtrip-test** for å verifisere at konverteringa er korrekt. Kopier til `src/linkml/<domain>/<modell>/<modell>-schema.yaml` om testen passerer.

## 2 — Rediger skjemaet

Sjå [Referanseskjema](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/referanse/referanse-schema.yaml) for eksempel på gyldig skjema med forklaringer.

Opne `src/linkml/<domain>/<modell>/<modell>-schema.yaml` og legg til klasser, slots og importar. Sjå [Importhierarki](#importhierarki) og [Kva importerer du?](#kva-importerer-du) nedanfor.



## 3 — Valider undervegs

For hurtig validering kan du linte skjemaet:
`make lint SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml`

Lint + validering mot medaljong-profil:
```bash
make mcp-linkml-valider-modell SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-linkml-valider-modell SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=silver
make mcp-linkml-valider-modell SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=gold
```

| Policy | Sjekkar |
|---|---|
| [`bronze`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/policies/README.md) | `id`, `name`, `title` (error); `default_prefix` (https-URI, error); `description`, `version`, `license` (warning); PascalCase-klasser, snake_case-slots, `class_uri`, `slot_uri`, `begrepsidentifikator` (warning) |
| [`silver`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/policies/README.md) | Bronze + `annotations.utgiver`, `annotations.endringsdato`, `annotations.status` (warning) + DCAT-AP-NO/DQV-AP-NO strukturkrav (error) |
| [`gold`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/policies/README.md) | Silver + FAIR F1-R1.3: full semantisk interoperabilitet |

Sjå [Valideringsreglar](../arkitektur/valideringsregler.md) for fullstendig oversikt over kva som vert sjekka på kvart nivå.

## 4 — Full testsuite
Lint + validering + alle generatorar for eitt skjema. Utan `SCHEMA=` køyrer testsuiten for alle skjema.
```
make test SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml
```



---

## Slette ein modell

```bash
make remove-modell NAME=<modell> DOMAIN=<domain>            # dry-run — viser sjekkar og filer, slettar ingenting
make remove-modell NAME=<modell> DOMAIN=<domain> CONFIRM=1  # slettar for reelt
```

Utan `CONFIRM=1` køyrer kommandoen berre sjekkane og viser kva som ville blitt
sletta. Kommandoen sjekkar:

| Sjekk | Type | Konsekvens |
|---|---|---|
| Modellen er lista under `submodels:` i eit anna skjema sin `build.yaml` | Blokkerande | Fjern referansen frå foreldre-manifestet før du prøver igjen |
| Modellen sitt skjema vert importert av eit anna skjema | Blokkerande | Fjern importen frå det andre skjemaet før du prøver igjen |
| `publish_external: true` og/eller `published-uris.lock` finst | Åtvaring | Eksterne katalogoppføringar vert **ikkje** automatisk fjerna — repoet pushar aldri. Vurder å deprekere i staden, sjå [publisering-begrep.md](../publisering/publisering-begrep.md) § «Deprekere eit begrep» |

Etter vellykka sletting oppdaterer kommandoen automatisk
`.github/valid-scopes.txt`. `generated/<domain>/<modell>/` og
`mkdocs/docs/<domain>/<modell>/` er byggoutput og treng ingen manuell
opprydding — dei forsvinn automatisk neste gong høvesvis generatorane og
`make docs-publish` køyrer.

---

## Importhierarki

```
linkml:types          (alltid)
    ↓
common-ap-no          (berre AP-NO-profilane importerer denne direkte)
    ↓
dcat-ap-no / dqv-ap-no / skos-ap-no / …   (AP-NO-profiler)
    ↓
domenemodell          (importerer éin eller fleire AP-NO-profiler)

fint-common           (berre FINT-domenemodellane importerer denne)
    ↓
fint-administrasjon / fint-arkiv / …

fair-metadata         (kan importerast av alle domenemodellar)
```

Domenemodellar importerer **AP-NO-profilane** — ikkje `common-ap-no` direkte. Dei arvar typar, subsets og slots frå AP-NO automatisk gjennom profilane.

---

## Kva importerer du?

| Du lagar … | Importer |
|---|---|
| Ein AP-NO-profil | `linkml:types` + `../common/common-ap-no-schema` |
| Ein domenemodell (NGR, o.l.) | `linkml:types` + aktuelle AP-NO-profil(ar) |
| Ein FINT-domenemodell | `linkml:types` + `../fint-common/fint-common-schema` |
| Modell med FAIR-metadata | `linkml:types` + `../../fair/fair-metadata/fair-metadata-schema` |

---

## Kva får du frå AP-NO-profilane

Ved å importere ein AP-NO-profil arvar du automatisk alt frå `common-ap-no` — du treng ikkje importere `common-ap-no` direkte.

**Typar frå `common-ap-no`**

| Namn | RDF-type | Bruk |
|---|---|---|
| `LangString` | `rdf:langString` | Fleirspråklege strenger (tittel, skildring …) |
| `Duration` | `xsd:duration` | Varigheit, t.d. `PT15M` |
| `GYear` | `xsd:gYear` | Årstal, t.d. `2024` |
| `NonNegativeInteger` | `xsd:nonNegativeInteger` | Telling, storleik |

**Gjenbrukbare slots (døme)**

```yaml
classes:
  MittObjekt:
    slots:
      - id          # identifier: true, range: uriorcurie
      - tittel      # slot_uri: dct:title, range: LangString
      - beskrivelse # slot_uri: dct:description, range: LangString
      - utgiver     # slot_uri: dct:publisher, range: uriorcurie
      - lisens      # slot_uri: dct:license, range: uriorcurie
```

Sjå `src/linkml/ap-no/common/common-ap-no-schema.yaml` for full liste.

---

## FAIR-konformitet med fair-metadata

For å dokumentere at ein ressurs er FAIR-konform, importer `fair-metadata`:

```yaml
imports:
  - linkml:types
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
  - ../../fair/fair-metadata/fair-metadata-schema
```

Valider mot gold-policy (gold-policy validerer spesifikt FAIR konformitet):

```bash
make mcp-linkml-valider-modell SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=gold
```

---

## Genererte artefakter

Sjå [Genererte artefakter](https://github.com/brreg/linkml-datamodellering-no#genererte-artefakter) i README for full oversikt over kva som vert generert per skjema.

---

## Tilpass manifest for generering og publisering

Kvar modell har ei `build.yaml` ved sida av skjemafila som styrer kva artefakter
som vert genererte. `make new-modell` oppretter standardkonfigen automatisk — alle
generatorar på, ingen ekstra flagg.

For å slå av ein generator eller leggje til flagg, rediger `build.yaml` og køyr:

```bash
make config.mk   # regenerer Makefile-konfig frå alle build.yaml-filer
```

Sjå [Modellmanifest](build-config.md) for feltliste og eksempel per
domenetype (standard, FINT, AP-NO/FAIR).

---

## Referanseskjema

[`src/linkml/referanse/referanse-schema.yaml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/referanse/referanse-schema.yaml) er eit annotert eksempelskjema som viser alle hovudmønster brukte i dette repoet: containerklasse, globale slots, import frå AP-NO-profil, `class_uri`/`slot_uri`, `LangString` og `in_subset`. Bruk det som oppslagsverk når du startar eit nytt skjema.

---

## Modelleringsprinsipp

**Norsk bokmål** — alle klassenamn, slotnamn og skildringar skrivast på bokmål. Unntak: tekniske omgrep fastsett i ein spesifikasjon (t.d. `dcat:Dataset` → `Datasett`).

**Slots, ikkje attributes** — alle eigenskapar definerast som globale `slots:` på toppnivå, aldri som `attributes:` inne i ein klasse.

**Lenking framfor inlining** — klasser som kan opptre sjølvstendig får `id`-slot med `identifier: true`. Referansar til slike klasser skal *ikkje* ha `inlined: true`.

**Eksplisitte URI-ar** — alle klasser skal ha `class_uri` (unntatt `tree_root`-containerklassar). Alle slots skal ha `slot_uri`.

**`slot_usage` for klassespesifikke innskrenkingar** — `required: true` og `in_subset:` setjast i `slot_usage` på klassen, ikkje i den globale slotdefinisjonen.

---

## Sjekkliste før innsjekking

```
[ ] id er ein HTTPS-URI
[ ] title og description er sett på skjemanivå
[ ] version er sett (t.d. "1.0.0")
[ ] license er sett til https://data.norge.no/nlod/no/2.0
[ ] default_prefix er ein absolutt HTTPS-URI med avsluttande /
[ ] Importerer AP-NO-profil(ar) — ikkje common-ap-no direkte
[ ] Klasse- og slotnamn er på norsk bokmål
[ ] Alle klasser (unntatt tree_root) har class_uri
[ ] Alle globale slots har slot_uri
[ ] make mcp-linkml-valider-modell POLICY=bronze gir 0 feil
[ ] Om validation_policy: silver eller høgare: annotations.utgiver, annotations.endringsdato,
    annotations.utgivelsesdato, annotations.status og annotations.oppdateringsfrekvens
    er fylt inn
[ ] make test køyrer utan feil
```

### Valfritt: engelsk skildring for internasjonalt synlege skjema

Digdirs rettleiar for åpne data anbefaler engelske skildringar for data som skal vere
synlege internasjonalt. Dette er **ikkje eit policy-krav**, men kan leggjast til som:

```yaml
annotations:
  title_en: "TODO: English title"
  description_en: "TODO: English description"
```

Omsetjinga krev fagkunnskap om innhaldet og er ei vurdering for codeowner av det
einskilde skjemaet — ikkje noko som vert generert automatisk eller krevd av CI.

---

## Kjende avgrensingar

Denne rettleiinga dekkjer grunnleggjande arbeidsflyt for domenemodellering i LinkML. 
Følgjande avgrensingar gjeld i PoC-fasen:

### Validering

- **BUG-1**: `rdflib_loader` rekonstruerer ikkje `LangString`-verdiar korrekt frå TTL ved roundtrip-testing ([specs/bugs/langstring-rdflib-roundtrip.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/bugs/langstring-rdflib-roundtrip.md))
- MCP-validator kjører berre bronze/silver/gold-policy — ingen automatisk validering mot eksterne API-ar enno

### Generatorar

- PlantUML-diagram vert ikkje genererte for skjema med meir enn 50 klasser (ytelse)
- JSON Schema-generatoren støttar ikkje `union_of` med meir enn to typar
- AsyncAPI-generering er eksperimentell og ikkje aktivert by default

### Publisering

- Publisering til Felles Begrepskatalog er delvis implementert — sjå [publisering-begrep.md](../publisering/publisering-begrep.md) for faktisk status
- Modellkatalogar med `publish_external: true` vert ikkje automatisk registrerte i data.norge.no enno — høsting må koordinerast manuelt

**Fullstendig oversikt:** Sjå [BUGS.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/BUGS.md) for komplett liste over kjende bugs og workarounds.

**Rapporter nye problem:** Opne eit [GitHub Issue](https://github.com/brreg/linkml-datamodellering-no/issues) med merkelappen `bug`.
