# Spesifikasjon: Publiseringskontroll for ekstern katalog

## Mål

Innføre ein eksplisitt mekanisme som angir om ein LinkML-modell eller eit begrep
skal publiserast til ein ekstern katalog (Felles Datakatalog eller Felles Begrepskatalog).
Mekanismen gjer det mogleg å ha upubliserte skjema og begrep i repoet utan at dei
kjem ut i produksjon — ned til granulariteten eitt og eitt begrep.

Mekanismen skal fungere likt i to ulike repo-oppsett:

| Oppsett | Skildring |
|---|---|
| **Mono-repo** | Fleire domene i same repo (t.d. `linkml-datamodellering-no`) |
| **Per-domene-repo** | Eitt repo per organisasjon/domene — repoet er sjølv domenet |

---

## Motivasjon

Per i dag er publiseringsomfanget implisitt:

- **Modellar**: alle `generate.yaml`-filer køyrer gjennom CI utan omsyn til om
  modellen er produksjonsklar
- **Begrep**: alle filer under `data/` publiserast; det finst ingen mekanisme for
  å halde eit enkelt begrep upublisert medan resten av katalogfila går ut

---

## Tilhøve til DCAT-AP-NO

DCAT-AP-NO har ingen eigeskap som direkte svarar til ein «publiser til ekstern katalog»-kontroll.
Dei to kandidatane som ligg nærast er:

| Eigeskap | Slot-URI | Føremål | Kvifor ikkje |
|---|---|---|---|
| `adms:status` | `adms:status` | Livssyklus-status: `UnderDevelopment`, `Completed`, `Deprecated` | Skildrar kor ferdig *ressursen* er — ikkje om han skal haustast |
| `dcatap:availability` | `dcatap:availability` | Planlagd tilgjengelegheit: `AVAILABLE`, `EXPERIMENTAL`, `STABLE`, `TEMPORARY` | Skildrar kor stabil *distribusjonen* er — ikkje publikasjonsintensjon |

Den eigentlege DCAT-AP-mekanismen for å kontrollere kva som vert publisert er
**katalogmedlemskap**: berre ressursar som er oppførte i kataloginstansfila
(`dcat:Catalog` + `dct:hasPart`) vert eksponerte til haustaren. Det er altså
*fråvær frå katalogfila* — ikkje eit flagg på ressursen — som hindrar publisering
i DCAT-modellen.

Publiseringskontrollen i dette repoet er difor eit reint CI-verktøy. Vil ein i
tillegg spegle tilstanden i metadata, kan `adms:status: UnderDevelopment` nyttast
på ressursen — men det er eit skildringsfelt, ikkje eit styringsverktøy.

---

## Vurdering: éi fil per begrep

Ei naturleg tilnærming for per-begrep-kontroll er å leggje kvart begrep i
éi eiga fil:

```
src/linkml/begrep/brreg-begrep/data/
  foretaksnavn.yaml
  nestleder.yaml
  aksjeklasser.yaml    ← utkast, ikkje i manifest
```

**Krav**: kvar fil må vere ein komplett samling av alle SKOS-klassar som inngår i
begrepsmodellen for det aktuelle begrepet. I SKOS-AP-NO-Begrep tyder det at fila
må innehalde både `begrep:`-oppføring og alle tilhøyrande `definisjoner:`-objekt
(eitt per språkversjon). Dersom fila berre inneheld `begrep:`-oppføringa utan
definisjonsobjekta, vil validering feile.

**Fordelar**
- Enkelt manifest — éi fil tilsvarar eitt begrep
- Rein git-historikk: endringar i eitt begrep rører berre éi fil

**Ulemper**
- Ein katalog med 50 begrep gjev 50+ filer — vanskeleg å få oversikt over heile
  katalogen på ein gong, og vanskeleg å sjå samanheng mellom nærskylde begrep.
- Validering må køyre per fil, eller ein treng eit eige aggregeringssteg.

**Konklusjon**: passar for svært granulære katalogar der kvart begrep har ulik
eigar eller livssyklus. For ein samla organisasjonskatalog er filproliferasjonen
ei unødvendig ulempe.

---

## Feltdefinisjonar

| Felt | Gjeld | Standardverdi | Gyldige verdiar |
|---|---|---|---|
| `publish_external` | Begge manifesttypar | `false` | `true` / `false` |
| `data_policy` | Begge manifesttypar | — | `bronze`, `silver`, `gold`, `felles-datakatalog`, `felles-begrepskatalog` |
| `generators` | Skjema-manifest | — | Sjå eksempel |
| `concepts` | Datafil-manifest | *(heile fila)* | Liste med begrep-URI-ar |

Policyhierarkiet frå lågast til høgast: `bronze` < `silver` < `gold` < `felles-datakatalog` / `felles-begrepskatalog`. Dei to spesialiserte policy-ane er sideordna og skil seg på kva katalog dei validerer mot.

---

## Katalogstruktur

Sidan begrepsdatafiler er i LinkML instansformat, høyrer dei heime under `src/linkml/`
saman med skjemaet dei er instansar av. Instansdata vert lagt i ein `data/`-underkatalog
direkte under skjemakatalogen.

```
src/
  linkml/
    <domene>/
      <modell>/
        <modell>-schema.yaml
        manifest.yaml             ← skjema-manifest
        examples/
          <modell>-eksempel.yaml  ← illustrasjonsdøme (ko-lokalisert med skjema)
        data/                     ← berre for skjema med produksjonsdata
          <katalog>/
            <katalog>.yaml
            manifest.yaml         ← datafil-manifest

generated/                        ← byggoutput, ikkje kjeldekode
tests/
```

I dette repoet er det berre `begrep/brreg-begrep/` som har produksjonsdata:

```
src/linkml/begrep/brreg-begrep/
  brreg-begrep-schema.yaml
  manifest.yaml
  examples/
    brreg-begrep-eksempel.yaml
  data/
    brreg-begrep/
      brreg-begrep.yaml
      manifest.yaml
```

Noverande struktur → ny struktur:

```
Før:
  src/linkml/<domene>/<modell>/generate.yaml
  examples/<domene>/<modell>-eksempel.yaml
  data/begrep/<katalog>.yaml

Etter:
  src/linkml/<domene>/<modell>/manifest.yaml
  src/linkml/<domene>/<modell>/examples/<modell>-eksempel.yaml
  src/linkml/begrep/<modell>/data/<katalog>/
    <katalog>.yaml
    manifest.yaml
```

---

## Løysing: kombinert manifest per modell

All publiserings- og generatorkonfig vert samla i eitt `manifest.yaml` per modell.
CI skil manifesttypen på innhald: skjema-manifest har `generators:`, datafil-manifest
har `concepts:` (valfri) og manglar `generators:`.

| Artefakt | Plassering |
|---|---|
| Skjema-manifest | `src/linkml/<domene>/<modell>/manifest.yaml` |
| Datafil-manifest | `src/linkml/<domene>/<modell>/data/<katalog>/manifest.yaml` |

Eksisterande `generate.yaml`-filer vert omdøypte til `manifest.yaml`. Innhaldet
er identisk — berre filnamnet endrar seg.

---

## Manifestformat

### Skjema — `manifest.yaml`

```yaml
publish_external: true        # publiser til ekstern katalog (standard: false)
data_policy: felles-datakatalog

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
```

### Datafil — `data/<katalog>/manifest.yaml`

`concepts:`-lista er valfri: utan ho publiserast heile datafila.

```yaml
publish_external: true        # publiser til ekstern katalog (standard: false)
data_policy: felles-begrepskatalog

concepts:                     # valfri — utelat for å publisere heile fila
  - https://begrep.brreg.no/foretaksnavn
  - https://begrep.brreg.no/nestleder
  # https://begrep.brreg.no/aksjeklasser  — utkast
```

---

## Eksempel

### Publisert NGR-skjema

```yaml
# src/linkml/ngr/ngr-adresse/manifest.yaml
publish_external: true
data_policy: felles-datakatalog

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
```

### Upublisert utkast-skjema

```yaml
# src/linkml/samt/samt-bu/manifest.yaml
publish_external: false       # utkast — ikkje klar enno
data_policy: silver

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: false
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
```

### Begrepskatalog — heile fila publisert

```
src/linkml/begrep/brreg-begrep/data/brreg-begrep/
  brreg-begrep.yaml
  manifest.yaml
```

```yaml
# src/linkml/begrep/brreg-begrep/data/brreg-begrep/manifest.yaml
publish_external: true
data_policy: felles-begrepskatalog
```

### Begrepskatalog — nokre begrep er utkast

```yaml
# src/linkml/begrep/brreg-begrep/data/brreg-begrep/manifest.yaml
publish_external: true
data_policy: felles-begrepskatalog

concepts:
  - https://begrep.brreg.no/foretaksnavn
  - https://begrep.brreg.no/nestleder
  # https://begrep.brreg.no/aksjeklasser  — utkast, ikkje klar enno
```

### Per-domene-repo

Strukturen er identisk — stiane er kortare sidan det ikkje er domene-nesting:

```yaml
# src/linkml/aksjeeier/manifest.yaml
publish_external: true
data_policy: felles-datakatalog

generators:
  shacl: true
  json_schema: true
  docs: true
  example_rdf: true
```

```yaml
# src/linkml/begrep/brreg-begrep/data/brreg-begrep/manifest.yaml
publish_external: true
data_policy: felles-begrepskatalog

concepts:
  - https://begrep.example.org/begrep-1
  - https://begrep.example.org/begrep-2
```

---

## Korleis CI brukar manifesta

CI skanner alt under `src/linkml/` etter `manifest.yaml`-filer. Typen vert avgjort
av innhald:

| Diskriminator | Type |
|---|---|
| Har `generators:`-seksjon | Skjema-manifest |
| Manglar `generators:`-seksjon | Datafil-manifest |

```
finn manifest.yaml med generators: under src/linkml/
  → publish_external: true  → skjema som skal genererast og publiserast til Felles Datakatalog
  → publish_external: false → berre lokal validering og artefaktgenerering

finn manifest.yaml utan generators: under src/linkml/
  → publish_external: true  → datafil som skal filtrerast og publiserast til Felles Begrepskatalog
  → publish_external: false → CI validerer fila, men eksponerer ikkje

data/-underkatalog utan manifest.yaml
  → CI validerer datafila automatisk med bronze-policy, IKKJE eksponering
```

### Skjema

```
src/linkml/ngr/ngr-adresse/manifest.yaml: publish_external: true
    → make convert-rdf   → generated/ngr/ngr-adresse/…eksempel.ttl
    → GitHub Pages       → Felles Datakatalog (høster)

src/linkml/samt/samt-bu/manifest.yaml: publish_external: false
    → berre lokal validering og artefaktgenerering (jsonschema, shacl, …)
    → IKKJE Turtle / IKKJE GitHub Pages-eksponering
```

### Begrep

```
src/linkml/begrep/brreg-begrep/data/brreg-begrep/manifest.yaml: publish_external: true, ingen concepts:
    → heile brreg-begrep.yaml → generated/begrep/brreg-begrep.ttl
    → GitHub Pages → Felles Begrepskatalog (høster)

src/linkml/begrep/brreg-begrep/data/brreg-begrep/manifest.yaml: publish_external: true, med concepts:
    → filtrer på lista URI-ar → generated/begrep/brreg-begrep.ttl
    → GitHub Pages → Felles Begrepskatalog (høster berre dei filtrerte)

data/-underkatalog utan manifest.yaml
    → CI validerer datafila automatisk med bronze-policy, IKKJE eksponering
```

`definisjoner:`-objekt vert filtrerte i takt med `begrep`-oppføringane: berre
definisjonar som høyrer til eit publisert begrep-ID vert inkluderte i Turtle-outputen.

---

## Validering

Publiseringskontrollen påverkar ikkje *kva* policy som køyrer — berre *om*
artefakten vert publisert.

| Situasjon | CI-åtferd |
|---|---|
| Skjema-manifest (`generators:` til stades) | Validerer med `data_policy` uavhengig av `publish_external` |
| Datafil-manifest (manglar `generators:`) | Validerer med `data_policy` uavhengig av `publish_external` |
| `data/`-underkatalog utan `manifest.yaml` | CI validerer datafila automatisk med `bronze`-policy |
| `publish_external: true` + `data_policy` < `gold` | CI åtvarar (warning) — sjå policyhierarkiet i §Feltdefinisjonar |

---

## Implementasjonstiltak

| Steg | Kvar | Kva |
|---|---|---|
| 1 | `src/linkml/` (alle skjema) | Omdøyp alle 22 `generate.yaml` → `manifest.yaml` |
| 2 | Eksisterande `manifest.yaml`-filer | Legg til `publish_external: true/false` og `data_policy` der det manglar |
| 3 | `examples/` | Flytt eksempelfiler inn under kvart skjema: `src/linkml/<domene>/<modell>/examples/` |
| 4 | `data/begrep/` | Flytt til `src/linkml/begrep/brreg-begrep/data/brreg-begrep/`; opprett `manifest.yaml` |
| 5 | CI (`generate.yml` / `publish.yml`) | Skann etter `manifest.yaml` under `src/linkml/`; skil type på `generators:`-felt; handter `publish_external`, `data_policy` og `concepts:` |
| 6 | CI | Legg til automatisk `bronze`-validering for `data/`-underkatalogar utan `manifest.yaml` |
| 7 | Makefile, `mkdocs/publish.sh`, alle stiar | Oppdater alle referansar til `examples/` og `data/` til nye plasseringar |
| 8 | `CLAUDE.md` | Dokumenter ny katalogstruktur og manifestformatet |

---

## Avgrensingar

- Manifesta kontrollerer berre om artefakten *vert eksponert*. Dei endrar ikkje
  URI-ar, schema-`id` eller andre metadata.
- `publish_external: true` for eit skjema krev at `published-uris.lock` finst i
  skjemamappa (sjå `specs/publisering-felles-datakatalog.md § URI-stabilitet`).
  CI bør feile med ein forklarande feilmelding dersom lock-fila manglar.
- `publish_external: true` for ein begrepsdatafil krev at dei publiserte konsepta
  passerer `felles-begrepskatalog`-policyen. CI bør køyre denne policyen automatisk.
- Strukturendringa (steg 3–4) krev oppdatering av alle referansar i Makefile,
  CI-workflow og `mkdocs/publish.sh`. Dette er den mest arbeidskrevjande delen
  av implementasjonen.
