# Vurdering: trengst ein eigen mcp-linkml-begrep-validator?

## Konklusjon

**Nei** — ein eigen server er ikkje nødvendig no.

Dei begrep-spesifikke valideringsgapa som er att etter `linkml-validate` vert best
dekka ved å utvide `valider_begrep`-verktøyet i `mcp-linkml-begrep-generator`.
Ein tredje container og eit tredje MCP-grensesnitt aukar driftskostnaden utan å
gje tilsvarande gevinst.

---

## Kva finst allereie

### `mcp-linkml-validator` — skjemanivå

Køyrer to typar sjekkar:

1. **Strukturell schema-validering**: `linkml.linter.Linter` og `linkml.validator.validate`
   — fangar opp manglande `required`-felt, typefeil og referansefeil som LinkML
   kjenner til gjennom skjemaet.

2. **Policy-sjekkar**: alle `_check_*`-funksjonane i `server.py` opererer på
   `SchemaView` — det vil seie på *skjemastrukturen*, ikkje på instansdata.
   Bronze-policyen sjekkar t.d. at klasser har `class_uri`, at slots har `slot_uri`,
   og at skjemaet har `id`.

Validatoren har **inga instansnivå-domenesjekkar** og er ikkje designa for det —
`_CHECK_HANDLERS` tek `(sv, schema, config, issues)`, ikkje instansdata.

### `valider_begrep` i `mcp-linkml-begrep-generator` — instansnivå (enkel)

Køyrer `linkml.validator.validate` med skos-ap-no-skjemaet som mål. Fangar opp:

- Manglande `required`-slot (t.d. `anbefalt_term`)
- Typefeil (feil range)
- Strukturfeil i YAML

Dette er det same som `validate_linkml_instance` i den generelle validatoren —
inga begrep-domenekunnskap er involvert.

---

## Identifiserte gap

Desse sjekktypane vert *ikkje* fanga av nokon av dei eksisterande serverane:

| Gap | Forklaring |
|---|---|
| `fagomrade` må vere ein gyldig LOS-tema-URI | Skjemaet har `range: uriorcurie` — `linkml-validate` godtek kva som helst gyldig URI |
| `kjelde_relasjon` må vere ein av tre FBK-vokabular-URI-ar | Skjemaet bør ha ein enum, men begrep-spesifikk kontekst krevst for god feilmelding |
| `identifikator_literal` skal vere lik `id` | Kryss-felt-konsistens; ikkje mogleg å uttrykke i LinkML-skjema |
| `sja_ogsa_omgrep`-verdiar bør følgje `data.norge.no/concepts/<uuid>` | Regex-sjekk på URI-mønster |
| FBK-klarleik: minst éin `anbefalt_term` på nb og nn | Krev å telle over instansdata per språk |

---

## Kvifor ikkje ein eigen server

### Arkitektonisk overlap

Ein `mcp-linkml-begrep-validator` ville gjere nøyaktig det same som
`valider_begrep`-utvidinga (sjå nedanfor), berre i ein eigen container og med eit
eige MCP-grensesnitt. Det er inga funksjonalitet som krev prosess-isolasjon.

### Deling av domenelogikk

Gapa ovanfor krev tilgang til:
- `los_tema.py` — allereie i `mcp-linkml-begrep-generator`
- Kunnskap om begrep-skjemastrukturen — allereie kodet inn i generatoren

Ein eigen validator måtte anten duplisere desse, eller dei måtte trekkjast ut til
eit delt bibliotek — noko som aukar kompleksiteten meir enn problemet fortener.

### Driftskostnad

Tre MCP-serverane for begrep (generator, validator, og den generelle validatoren)
betyr tre Dockerfile, tre Makefile-mål, tre release-jobbar og tre containers som
ein AI-assistent må velje mellom. To er nok.

---

## Tilrådde endringar i `mcp-linkml-begrep-generator`

Utvid `valider_begrep` med eit valfritt `nivå`-parameter som styrer kvar
strengt ein validerer. Alle nivå køyrer `linkml-validate` som grunnlag.

### Nytt `nivå`-parameter

| Nivå | Dekkjer |
|---|---|
| `skjema` (standard) | `linkml-validate` mot skos-ap-no-skjemaet |
| `domene` | `skjema` + alle begrep-spesifikke instanssjekkar |
| `fbk-klar` | `domene` + FBK-klarleikskrav (nb+nn term, definisjon på begge) |

### Instanssjekkane på `domene`-nivå

Desse vert implementerte som reine Python-funksjonar i ei ny `checker.py` i same
container som generatoren:

```python
def sjekk_instans(data: dict, los_tema_uris: set) -> list[dict]:
    """Returnerer liste med hendingar på same format som mcp-linkml-validator."""
```

Konkrete sjekkar:

```
1. For kvart Begrep-objekt i data["begrep"]:
   a. Alle fagomrade-URI-ar må vere i los_tema_uris
   b. identifikator_literal (om til stades) skal matche id
   c. Alle URI-ar i sja_ogsa_omgrep bør matche
      ^https://data\.norge\.no/concepts/[0-9a-f-]{36}$

2. For kvart Definisjon-objekt i data["definisjoner"]:
   a. kjelde_relasjon (om til stades) skal vere ein av dei tre gyldige
      https://data.norge.no/vocabulary/relationship-with-source-type#...
```

### Ekstra sjekkar på `fbk-klar`-nivå

```
3. Kvart Begrep må ha minst éin anbefalt_term der objectet er tagga "nb"
   (eller har ein nb Definisjon via har_definisjon)
4. Kvart Begrep bør ha minst éin anbefalt_term der objectet er tagga "nn"
   (eller har ein nn Definisjon via har_definisjon)
5. Kvart Begrep må ha anten definisjon eller har_definisjon
```

Merk: `anbefalt_term` i instansfila er ein liste med reine strenger — språktagging
skjer i RDF/Turtle-outputen via `lang`-annotering i skjemaet. `fbk-klar`-nivået
kan difor berre sjekke at `har_definisjon`-lista har Definisjon-objekt med
`nb`- og `nn`-ID-suffiksar (t.d. `-nb` og `-nn` i URI). Dette er ein heuristikk,
ikkje ein garantert korrekt sjekk — dokumenter det som det.

### Oppdatert `valider_begrep`-signatur

```json
{
  "yaml_innhald": "...",
  "skjema_sti": "src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml",
  "nivaa": "domene"
}
```

Output vert same format som i dag — lista med `{alvorlegheit, kode, mål, melding}`.

---

## Når bør ein revurdere?

Ein eigen `mcp-linkml-begrep-validator` gjer meir meining dersom eitt eller fleire
av desse vert sanne:

- Valideringskoden (`checker.py`) veks til meir enn ~200 linjer og krev eiga
  testdekning som ikkje passar i generatorens kontekst
- Det dukkar opp eit behov for å validere begrep-instansar *utan* å bruke
  generatoren (t.d. validering av eksisterande filer frå eit anna system)
- Behovet for FBK-integrasjon krev nettverkskall (t.d. slå opp om ein FBK-URI
  faktisk eksisterer) — noko som klart bør isolerast frå generatoren
