# Bug: `walk()` i instans-sjekkarar hoppar over lister av objekt

**ID:** BUG-5
**Status:** `løyst`
**Komponent:** `mcp-linkml-validator` (`server.py`)
**Oppdaga:** 2026-06-20
**Løyst:** 2026-06-20

## Symptom

`instance_checks` av typen `instance_slot_uri_pattern` (brukt av
`utgjevar_er_kjend_org` i `felles-begrepskatalog.yaml`) gir **ingen varsel**
sjølv når feltet dei skal validere har ein ugyldig verdi, så lenge feltet ligg
nøsta inni ei liste av objekt — som er den vanlege strukturen for AP-NO-data
(t.d. `begrep:` i `brreg-begrepskatalog.yaml`).

Stadfesta empirisk: ved å bytte ut ein gyldig `utgjevar`-URI med ein ugyldig
(`https://data.norge.no/organizations/000000000`, ikkje i `known_values`) i
`src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`
og køyre

```bash
make mcp-validate SCHEMA=src/linkml/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml
```

ga **ingen** `instance_slot_invalid_uri_pattern`/`instance_slot_unknown_value`-varsel,
sjølv om sjekken `utgjevar_er_kjend_org` er aktiv i policyen. Sjekken er altså
ein no-op for denne datastrukturen.

## Rot-årsak

`_check_instance_slot_uri_pattern` i `src/mcp-linkml-validator/server.py`
(linje 467–493) har:

```python
def walk(obj, path=""):
    if not isinstance(obj, dict):
        return
    for key, val in obj.items():
        if key in target_slots:
            ...
        walk(val, f"{path}.{key}" if path else key)

walk(instance)
```

Toppnivå-instansen er typisk `{"begrep": [...], "definisjoner": [...], ...}`.
`walk(instance)` går inn i denne dict-en, finn key `"begrep"` med
`val = [...]` (ei liste), og kallar `walk(val, "begrep")`. Men `val` er ei
liste, ikkje ein dict — funksjonen sin **første linje** (`if not isinstance(obj, dict): return`)
returnerer då umiddelbart, **utan å gå inn i listeelementa**. Dermed blir
`utgjevar`-feltet inni hvert `begrep[i]`-objekt aldri besøkt, og sjekken kan
aldri produsere eit treff.

Dette gjeld for **alle** instansar i AP-NO-strukturen, sidan toppnivå-lister
(`begrep:`, `datasett:`, `samlingar:`, osb.) er standardmønsteret for
datafiler i dette repoet (jf. CLAUDE.md § "Containerklasse").

## Berørte sjekkar

| Sjekk | Policy | Handler |
|---|---|---|
| `utgjevar_er_kjend_org` | `felles-begrepskatalog.yaml` | `_check_instance_slot_uri_pattern` |

Alle framtidige `instance_checks` som bruker `check: instance_slot_uri_pattern`
vil ha samme problem. Den nyare handleren
`_check_instance_begrep_definisjon_language_coverage` (lagt til same dag, for
`begrep_har_definisjon_pa_nb_og_nn`) er **ikkje** affisert — den har ein
korrekt `walk()` som også rekurserer inn i lister (sjå
`specs/done/avvik-skos-ap-no.md`, SK5 Forslag A).

## Workaround

Ingen workaround vart nødvendig — fiksa direkte (sjå "Løysing").

## Løysing

Rett `walk()` i `_check_instance_slot_uri_pattern` slik at den også
rekurserer inn i lister, etter mønsteret som allereie er brukt i
`_check_instance_begrep_definisjon_language_coverage`:

```python
def walk(obj, path=""):
    if isinstance(obj, dict):
        for key, val in obj.items():
            new_path = f"{path}.{key}" if path else key
            if key in target_slots:
                values = val if isinstance(val, list) else [val]
                for v in values:
                    if not isinstance(v, str):
                        continue
                    loc = f"instance:{new_path}"
                    if not pattern.match(v):
                        issues.append(issue(
                            config["severity"],
                            "instance_slot_invalid_uri_pattern",
                            loc,
                            f"'{v}' passar ikkje mønsteret {config['pattern']} "
                            f"for {slot_uri_target}",
                        ))
                    elif known_values and v not in known_values:
                        issues.append(issue(
                            config["severity"],
                            "instance_slot_unknown_value",
                            loc,
                            f"'{v}' er ikkje i lista over kjente utgivarar: "
                            f"{', '.join(known_values)}",
                        ))
            walk(val, new_path)
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            walk(item, f"{path}[{idx}]")

walk(instance)
```

**Filer:** `src/mcp-linkml-validator/server.py`, `tests/test_mcp_policies.py`

### Utført (2026-06-20)

1. ✓ Retta `_check_instance_slot_uri_pattern` sin `walk()`-funksjon som vist over.
2. ✓ Reprodusert regresjonen frå "Symptom"-seksjonen: sette ein ugyldig
   `utgjevar`-URI inn i `data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`
   (midlertidig, reverte etterpå) og stadfesta at sjekken no gir
   `instance_slot_unknown_value` for `instance:begrep[0].utgjevar`,
   `instance:begrep[1].utgjevar`, `instance:begrep[2].utgjevar` og
   `instance:samlingar[0].utgjevar`. Med original (gyldig) data: 0 feil, som før.
3. ✓ Lagt til `TestInstanceCheckWalk` i `tests/test_mcp_policies.py` — to
   testar: ein som stadfester at ugyldig verdi **nøsta inni ei liste** blir
   funne (regresjonstest for denne buggen), og ein for verdi på toppnivå.
4. ✓ `make mcp-val-test` køyrt: 28 testar (var 26), dei 12 pre-eksisterande
   feila i `TestGold`/`TestSilver` (urelaterte FAIR-sjekkar, kjende frå før
   denne endringa) er framleis dei einaste feila — dei 2 nye testane passerer.
5. ✓ Status oppdatert til `løyst`.
