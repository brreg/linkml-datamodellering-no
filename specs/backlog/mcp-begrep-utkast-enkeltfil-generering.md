# mcp-linkml-begrep-utkast: støtt enkeltfil-generering til begrepssamling

## Bakgrunn

Etter innføring av ny begrepssamling-struktur (spec: `begrep-per-fil-og-begrepskatalog-automatikk.md`) ligg begrep no som éin fil per begrep under `src/linkml/<domain>/begrepssamling-<namn>/begrep/<slug>.yaml`.

`mcp-linkml-begrep-utkast` genererer i dag ein heil `BegrepContainer`-blokk (begrep, definisjoner, organisasjonar, kontaktpunkt) som skal limast inn i ei eksisterande fil. Dette passar ikkje lenger til den nye strukturen.

**Mål:** Oppdatere `mcp-linkml-begrep-utkast` til å skrive begrep direkte til den nye filstrukturen.

## Endringar

### 1. Ny funksjon: `skriv_begrep_til_fil`

Legg til ny funksjon i `generator.py`:

```python
def skriv_begrep_til_fil(
    profile: dict,
    output_path: Path,
    slug: str,
    anbefalt_term_nb: str,
    definisjon_nb: str,
    fagomrade_uri: str,
    # ... same parametrar som opprett_begrep
) -> Path:
    """
    Genererer og skriv begreps-YAML til fil.
    
    Returns:
        Path til den skrivne fila
    """
```

Denne funksjonen skal:
- Generere **berre begreps-objektet** (ikkje definisjoner, organisasjonar, kontaktpunkt)
- Skrive YAML til `output_path`
- Returnere `output_path`

### 2. Nytt MCP-verktøy: `skriv_begrep_fil`

Legg til nytt verktøy i `server.py`:

```python
TOOL_SKRIV_BEGREP_FIL = {
    "name": "skriv_begrep_fil",
    "description": (
        "Genererer begreps-YAML og skriv direkte til begrepssamling-struktur. "
        "Skriv til src/linkml/<domain>/begrepssamling-<namn>/begrep/<slug>.yaml. "
        "Returnerer filsti."
    ),
    "inputSchema": {
        "type": "object",
        "required": ["domain", "begrepssamling", "slug", ...],
        "properties": {
            "domain": {
                "type": "string",
                "description": "Domene, t.d. 'oreg'",
            },
            "begrepssamling": {
                "type": "string",
                "description": "Begrepssamling-namn, t.d. 'begrepssamling-foretaksregisteret'",
            },
            # ... same parametrar som opprett_begrep
        }
    }
}
```

### 3. Behold `opprett_begrep` for bakoverkompatibilitet

`opprett_begrep` skal framleis generere `BegrepContainer`-YAML-blokk for dei som vil lime inn manuelt. Endre berre internt: faktoriser ut begreps-generering til eigen funksjon `_generate_begrep_dict()` som kan brukast av både `opprett_begrep` og `skriv_begrep_til_fil`.

## Filformat for enkeltbegrep

```yaml
# Generert av mcp-linkml-begrep-utkast
id: https://begrep.brreg.no/foretaksnavn
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
  - https://psi.norge.no/los/tema/naring
  - https://psi.norge.no/los/tema/naringsliv
```

**OBS:** Definisjoner, organisasjonar og kontaktpunkt **skal ikkje** vere med i enkeltfila — desse vert aggregerte av `collect-concepts.py` seinare (framtidig funksjonalitet).

## Tiltak

- [ ] Faktoriser `_generate_begrep_dict()` ut frå `opprett_begrep()` i `generator.py`
- [ ] Legg til `skriv_begrep_til_fil()` i `generator.py`
- [ ] Legg til `TOOL_SKRIV_BEGREP_FIL` i `server.py`
- [ ] Legg til `_handle_skriv_begrep_fil()` i `server.py`
- [ ] Oppdater `handle()`-funksjonen til å handtere `skriv_begrep_fil`-verktøyet
- [ ] Oppdater README.md med ny seksjon om `skriv_begrep_fil`
- [ ] Test at `skriv_begrep_fil` skriv korrekt fil til riktig katalog

## Test

```bash
# Test at skriv_begrep_fil skriv til riktig katalog
make mcp-begrep-run

# Send MCP-melding:
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "skriv_begrep_fil",
    "arguments": {
      "domain": "oreg",
      "begrepssamling": "begrepssamling-foretaksregisteret",
      "profil": "brreg",
      "slug": "testbegrep",
      "anbefalt_term_nb": "testbegrep",
      "definisjon_nb": "eit testbegrep",
      "fagomrade_uri": "https://psi.norge.no/los/tema/naring"
    }
  }
}

# Verifiser:
ls src/linkml/oreg/begrepssamling-foretaksregisteret/begrep/testbegrep.yaml
cat src/linkml/oreg/begrepssamling-foretaksregisteret/begrep/testbegrep.yaml
```

## Framtidig arbeid (ikkje del av denne spec-en)

- [ ] `collect-concepts.py`: samle definisjoner, organisasjonar, kontaktpunkt frå profil-metadata
- [ ] `collect-concepts.py`: generer `definisjoner`-, `organisasjonar`- og `kontaktpunkt`-blokkar i aggregert begrepskatalog
