# Fiks id-only klasser i inlined_as_list for NGR-skjema

## Bakgrunn og rotårsak

`linkml-convert` og `linkml-runtime` har ein bug i `_normalize_inlined_as_list`
der objekt med **berre `id`-slot og ingen andre eigenskapar**, lagra i ein
`inlined_as_list: true`-attributt, vert feilaktig handsama: runtime klarer ikkje
skilje mellom `{id: "URI"}` og ein plain URI-streng, og sender `JsonObj`-instansen
som id-verdi i staden for å trekkje ut strengen.

Dette gjer at `linkml-convert`, roundtrip-testar og serialisering til JSON/TTL
feiler for alle tre skjemaa.

## Berørte klasser

### `ngr-adresse-schema.yaml`

| Klasse | Problem | Brukt i container-attr | Referert av slot |
|---|---|---|---|
| `Bygning` | id-only | `bygningar` (`inlined_as_list`) | `adresserer_bygning` |
| `Bruksenhet` | id-only | `bruksenheter` (`inlined_as_list`) | `adresserer_bruksenhet` |

`GeografiskAdresse` er id-only men er ikkje i noko `inlined_as_list`-attributt — ikkje berørt.

### `ngr-eiendom-schema.yaml`

| Klasse | Problem | Brukt i container-attr | Referert av slot |
|---|---|---|---|
| `Teig` | id-only | `teiger` (`inlined_as_list`) | `er_del_av_teig`, `har_teig` |
| `TinglystHeftelse` | id-only | `tinglystHeftelser` (`inlined_as_list`) | `har_tinglyst_heftelse` |
| `RettighetForAaBenytteEiendom` | id-only | `rettigheter` (`inlined_as_list`) | `bestar_av_rettighet` |

Andre id-only klasser (`Anleggsprojeksjonsflate`, `OffisiellAdresse`, `Person`,
`Hovedenhet`) er ikkje i container-attributtar med `inlined_as_list` — ikkje berørte.

### `ngr-virksomhet-schema.yaml`

`GeografiskAdresse` og `Person` er id-only, men ingen av dei er brukt i
`inlined_as_list`-attributtar i containeren. Skjemaet er **ikkje berørt** av buggen.
Ekskluderinga i `test_make.sh` er dermed unødvendig og kan fjernast.

## Løysing

**Prinsipp:** Alle fem berørte klassane (`Bygning`, `Bruksenhet`, `Teig`,
`TinglystHeftelse`, `RettighetForAaBenytteEiendom`) er referansar til objekt
som er forvalta av eksterne register (Matrikkelen, Grunnboka). Dei har
berre `id` fordi domenemodellen ikkje beskriver deira indre eigenskapar —
dei er URI-peikararar, ikkje dataobjekt.

Riktig modellering er å **ikkje inline slike eksternt forvalta referansar i containeren**.
Referanseslotar (`adresserer_bygning`, `har_teig` o.l.) behaldar `range: ClassName`
for semantisk presisjon — berre container-attributtane vert fjerna.

### Tiltak per skjema

#### `ngr-adresse-schema.yaml`

1. Fjern `bygningar`-attributtet frå `AdresseContainer`
2. Fjern `bruksenheter`-attributtet frå `AdresseContainer`
3. Hald `Bygning`- og `Bruksenhet`-klassane (dei er framleis nyttige som
   typemarkørar for `adresserer_bygning` og `adresserer_bruksenhet`)

#### `ngr-adresse-eksempel.yaml`

Fjern desse listene (deira URI-ar er allereie representert som referansar):

```yaml
# Fjern:
bygningar:
  - id: https://example.org/bygning/12345

bruksenheter:
  - id: https://example.org/bruksenhet/1
```

`adresserer_bygning` og `adresserer_bruksenhet` på `OffisiellAdresse`-instansen
er URI-referansar og treng inga endring.

#### `ngr-eiendom-schema.yaml`

1. Fjern `teiger`-attributtet frå `EiendomContainer`
2. Fjern `tinglystHeftelser`-attributtet frå `EiendomContainer`
3. Fjern `rettigheter`-attributtet frå `EiendomContainer`
4. Hald klassane `Teig`, `TinglystHeftelse` og `RettighetForAaBenytteEiendom`
   (framleis nyttige som typemarkørar for referanseslotar)

#### `ngr-eiendom-eksempel.yaml`

Fjern id-only listene:

```yaml
# Fjern:
teiger:
  - id: ngre:eksempel/teig-1
```

`tinglystHeftelser` og `rettigheter` er ikkje i eksempelfila per no — ingen
endring der.

#### `test_make.sh`

Fjern `ngr-virksomhet` frå skip-lista for roundtrip-testar sidan det skjemaet
ikkje er berørt av buggen:

```bash
# Før:
if [[ "$name" == "ngr-adresse" || "$name" == "ngr-eiendom" || \
      "$name" == "ngr-virksomhet" ]]; then

# Etter:
if [[ "$name" == "ngr-adresse" || "$name" == "ngr-eiendom" ]]; then
```

Etter at ngr-adresse og ngr-eiendom er fiksa og roundtrip-testane er på plass,
skal desse to òg fjernast frå skip-lista.

## Prioritert tiltaksliste

| # | Fil | Endring | Prioritet |
|---|---|---|---|
| 1 | `ngr-adresse-schema.yaml` | Fjern `bygningar` og `bruksenheter` frå `AdresseContainer` | Høg |
| 2 | `ngr-adresse-eksempel.yaml` | Fjern `bygningar`- og `bruksenheter`-listene | Høg |
| 3 | `ngr-eiendom-schema.yaml` | Fjern `teiger`, `tinglystHeftelser` og `rettigheter` frå `EiendomContainer` | Høg |
| 4 | `ngr-eiendom-eksempel.yaml` | Fjern `teiger`-lista | Høg |
| 5 | `test_make.sh` | Fjern `ngr-virksomhet` frå roundtrip-skip-lista | Medium |
| 6 | `test_make.sh` | Fjern `ngr-adresse` og `ngr-eiendom` frå roundtrip-skip-lista etter verifisering | Medium |
