# mcp-linkml-validator

MCP-server for policy-basert validering av LinkML-skjema.

Valideringa køyrer i tre steg, men **lint og instansvalidering køyrer berre éin gong — på bronsenivå**. Silver og gull arvar bronse og legg berre til fleire policy-sjekkar; dei køyrer ikkje lint eller instansvalidering på nytt.

| Steg | Bronze | Silver | Gold |
|---|---|---|---|
| Lint skjema (`linkml lint --validate`) | ✓ | — | — |
| Valider instans mot skjema | ✓ | — | — |
| Policy-sjekkar | bronse | bronse + sølv | bronse + sølv + gull |

## Bruk

```bash
# Medaljongnivå:
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=gold

# Publisering — med datafil/instans:
make mcp-validate \
  SCHEMA=src/linkml/begrepskatalog/<katalog>/<katalog>-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=data/begrep/<katalog>.yaml

make mcp-validate \
  SCHEMA=src/linkml/modellkatalog/<katalog>/<katalog>-schema.yaml \
  POLICY=felles-datakatalog \
  INSTANCE=examples/modell/<katalog>-eksempel.yaml
```

## Policyarv

```
bronze
  ├── silver  (extends: bronze)
  │     └── gold  (extends: silver)
  ├── felles-begrepskatalog  (extends: bronze)
  └── felles-datakatalog  (extends: bronze)
```

`make mcp-validate POLICY=gold` køyrer alle bronse-, sølv- og gull-krav i éin gjennomgang.

Publiseringspolicyane er sidegreinar — dei arvar bronse, men ikkje sølv eller gull.
Bruk dei saman med medaljongnivåa for fullstendig dekning:

```bash
make mcp-validate SCHEMA=... POLICY=bronze
make mcp-validate SCHEMA=... POLICY=felles-begrepskatalog INSTANCE=...
```

---

## Fullstendig sjekkliste

Sjekkar i bronze-, silver- og gold-policyane realiserer både
[Felles modelleringsregler for offentlig forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)
(Digitaliseringsdirektoratet) og [FAIR-prinsippa](https://www.go-fair.org/fair-principles/).

**Sjå [`policies/README.md`](policies/README.md) for fullstendig sjekkliste, Digdir-regel-mapping og FAIR-prinsipp-oversikt.**

---

## MCP-verktøy

| Verktøy | Skildring |
|---|---|
| `validate_linkml_schema` | Validerer eit skjema med lint + instansvalidering + policy-sjekkar. Parametrar: `schemaText` (påkravd), `policy` (standard: `bronze`), `instanceText` (valfri). |
| `validate_linkml_instance` | Validerer ein instans mot eit skjema. Tilsvarar `linkml validate --schema`. Parametrar: `schemaText`, `instanceText`, `targetClass` (valfri). |
