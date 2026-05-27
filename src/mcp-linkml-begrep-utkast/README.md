# mcp-linkml-begrep-utkast

MCP-server for generering og validering av SKOS-AP-NO Begrep-instansar i YAML-format.
Serveren følgjer mønsteret i `specs/begrep-modellering.md` og produserer
`BegrepContainer`-blokkar klare for validering og RDF-eksport til Felles Begrepskatalog.

## Bruk

```bash
# Bygg containeren (éin gong)
make mcp-begrep-build

# List tilgjengelege profiler
make mcp-begrep-list-profiles

# Køyr serveren interaktivt (MCP stdio-transport)
make mcp-begrep-run
```

**Eksempel: generer YAML for eitt begrep med `brreg`-profilen**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "opprett_begrep",
    "arguments": {
      "profil": "brreg",
      "slug": "foretaksnavn",
      "anbefalt_term_nb": "foretaksnavn",
      "anbefalt_term_nn": "føretaksnamn",
      "definisjon_nb": "det offisielle namnet på ein næringsdrivande juridisk person og kjenneteiknet for eit enkeltpersonføretak",
      "kjelde_relasjon": "direct-from-source",
      "fagomrade_uri": "https://psi.norge.no/los/tema/naringsliv"
    }
  }
}
```

## MCP-verktøy

| Verktøy | Skildring |
|---|---|
| `opprett_begrep` | Genererer ein komplett `BegrepContainer`-YAML-blokk frå strukturerte parametrar. Støttar profil, fleirspråkleg (nb/nn/en), kjeldetype og LOS-fagområde. |
| `valider_begrep` | Validerer ei YAML-instansfil mot eit skos-ap-no-basert skjema (les skjema med importresolvering via `SchemaView`). |
| `list_profiles` | Listar tilgjengelege profiler med namn og skildring. |
| `list_los_tema` | Returnerer statisk liste over gyldige LOS-tema URI-ar (ingen nettverkskall). |

### `opprett_begrep` — parametrar

#### Påkravde

| Parameter | Type | Skildring |
|---|---|---|
| `slug` | string | Kort identifikator, t.d. `foretaksnavn` |
| `anbefalt_term_nb` | string | Anbefalt term på bokmål |
| `definisjon_nb` | string | Definisjonstekst på bokmål |
| `fagomrade_uri` | string | URI til LOS-tema — bruk `list_los_tema` |

#### Valfrie (kan setjast av profilen)

| Parameter | Type | Skildring |
|---|---|---|
| `profil` | string | Profilnamn (standard: `default`) |
| `base_uri` | string | Base-URI for organisasjonen, t.d. `https://begrep.brreg.no` |
| `kjelde_relasjon` | enum | `direct-from-source` / `self-composed` / `derived-from-source` |
| `utgjevar_uri` | string | URI til utgjevande organisasjon |
| `anbefalt_term_nn` | string | Term på nynorsk |
| `anbefalt_term_en` | string | Term på engelsk |
| `definisjon_nn` | string | Definisjon på nynorsk (fallback: nb-tekst) |
| `definisjon_en` | string | Definisjon på engelsk (fallback: nb-tekst) |
| `kontaktpunkt_uri` | string | URI til kontaktpunkt-objekt |
| `merknad` | string[] | Merknadstekstar |
| `eksempel` | string[] | Eksempelstrengjer |
| `sja_ogsa_omgrep` | string[] | URI-ar til relaterte begreper |

### `valider_begrep` — parametrar

| Parameter | Type | Skildring |
|---|---|---|
| `yaml_innhald` | string | Innhaldet i instansfila som YAML-streng |
| `skjema_sti` | string | Sti til skjemafil relativt til `/repo`, t.d. `src/linkml/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog-schema.yaml` |

Returnerer `{ gyldig, feiltal, åtvaringtal, hendingar }` med same format som
`mcp-linkml-validator`.

## Generert YAML-struktur

`opprett_begrep` produserer ein fullstendig `BegrepContainer`-blokk:

```yaml
# Generert av mcp-linkml-begrep-utkast — legg til i instansfila di
# Begrep: https://begrep.brreg.no/foretaksnavn

begrep:
  - id: https://begrep.brreg.no/foretaksnavn
    anbefalt_term:
      - foretaksnavn
      - føretaksnamn
    har_definisjon:
      - https://begrep.brreg.no/def/foretaksnavn-nb
      - https://begrep.brreg.no/def/foretaksnavn-nn
    identifikator_literal: https://begrep.brreg.no/foretaksnavn
    kontaktpunkt_vcard:
      - https://begrep.brreg.no/kontakt/begrepsansvarleg
    utgjevar: https://data.norge.no/organizations/974760673
    fagomrade:
      - https://psi.norge.no/los/tema/naringsliv

definisjoner:
  - id: https://begrep.brreg.no/def/foretaksnavn-nb
    tekst: det offisielle namnet på ein næringsdrivande juridisk person ...
    kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#direct-from-source
  - id: https://begrep.brreg.no/def/foretaksnavn-nn
    tekst: det offisielle namnet på ein næringsdrivande juridisk person ...
    kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#direct-from-source

organisasjonar:
  - id: https://data.norge.no/organizations/974760673

kontaktpunkt:
  - id: https://begrep.brreg.no/kontakt/begrepsansvarleg
```

Lim innhaldet inn i ei eksisterande instansfil under dei tilsvarande listene
(`begrep:`, `definisjoner:` osv.).

## Profiler

Profilen styrer standardverdiar og URI-mønster. Standard profil er `default`.

```bash
make mcp-begrep-list-profiles
```

Profilane ligg i `profiles/<namn>.yaml`:

| Nøkkel | Skildring |
|---|---|
| `description` | Vises av `list_profiles` |
| `uri.begrep_pattern` | URI-mønster for begrep — variablar: `{base_uri}`, `{slug}` |
| `uri.definisjon_pattern` | URI-mønster for definisjonsobjekt — + `{lang}` |
| `uri.kontaktpunkt_default` | Fallback-URI for kontaktpunktstub |
| `defaults.base_uri` | Standard base-URI (utelat for å krevje eksplisitt) |
| `defaults.utgjevar_uri` | Standard utgjevar-URI |
| `defaults.kjelde_relasjon` | Standard kjeldetype |
| `languages.required` | Språk som alltid inkluderast |
| `languages.optional` | Språk som inkluderast om parameteren er gjeven |
| `generation.add_header_comment` | Legg til kommentarblokk øvst (standard: true) |

Ny organisasjonsprofil: legg til `profiles/<org>.yaml` — ingen kodeendring nødvendig.

## NB! Etter generering — nødvendige tilpassingar

Det genererte YAML-innhaldet er eit utkast. Sjekk og fyll inn:

1. **`kontaktpunkt`-objektet** — berre `id`-stub generert. Legg til `fn`, `hasEmail`
   o.l. i instansfila slik at kontaktpunktet er fullstendig per SKOS-AP-NO.
2. **`samlingar`-seksjon** — genererast ikkje automatisk. Legg til manuelt om
   begrepssamling er aktuelt.
3. **`sja_ogsa_omgrep`-referansar** — kan peike til `data.norge.no/concepts/<uuid>`
   for relaterte begreper i Felles Begrepskatalog.
4. **Fleirspråklege definisjonar** — om `definisjon_nn` er utelaten, vert nb-teksten
   brukt som fallback. Erstatt med korrekt nn-tekst ved behov.

## Avgrensingar

- **`valider_begrep`** er eit rask syntakssjekk mot skjemaet. Køyr i tillegg:
  ```bash
  make mcp-validate SCHEMA=src/linkml/begrepskatalog/<katalognavn>/<katalognavn>-schema.yaml POLICY=bronze
  ```
- **`list_los_tema`** er ein statisk liste kompilert inn i `los_tema.py`. Ved
  oppdatering av LOS må fila oppdaterast og containeren byggjast på nytt.
- **`mcp-linkml-validator`** sin skjema-policy-validering gjeld framleis og er
  uendra — `valider_begrep` erstattar han ikkje.
