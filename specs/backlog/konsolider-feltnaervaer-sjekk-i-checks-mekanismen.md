# Konsolider feltnærvær-sjekk til éin mekanisme (`required`/`recommended` → `checks:`)

## Bakgrunn

`specs/backlog/full-gjennomgang-policy-alvorsgrad-og-overlapp.md`
(Funn B5) kartla at repoet i dag har **to uavhengige mekanismar** for å
uttrykkje «dette feltet skal/bør vere til stades» på eit LinkML-skjema:

1. Den generiske `required:`/`recommended:`-lista i kvar policy-YAML —
   handtert av ein anonym closure (`_check()`) i `validate_schema()`
   (`server.py`), med **fast** alvorsgrad (`error` for required,
   `warning` for recommended) og **inga** støtte for overstyring per
   policy-nivå. Gjeld tre scope: `schema`, `class`, `slot`.
2. Eksplisitte `checks:`-oppføringar med `check: schema_field_present`
   (brukt for `default_prefix`, `license`) — handtert av
   `_check_schema_field_present`, som **støttar** alvorsgrad-progresjon
   per nivå via den vanlege `{**parent, **child}`-nøkkeloverstyringa i
   `_merge_policies()`. Gjeld i dag berre `schema`-scope.

**Rotårsak til at begge finst:** mekanisme 1 kan strukturelt ikkje
uttrykkje «warning på bronse, error på gull» for eitt felt (union av
lister, ingen overstyring) — difor vart mekanisme 2 oppfunnen for felt
som treng nettopp det (`license`: warning på bronse/sølv, error på gull).
Felt utan progresjonsbehov (`id`, `name`, `title`, `description`) vart
verande i den enklare, eldre mekanisme 1.

**Stadfesta skadeverknad (verifisert direkte, sjå kommandoen under):** eit
felt som endar opp i BÅDE `required` og `recommended` samstundes — noko
som skjer i dag for `title` under `felles-datakatalog`/
`felles-begrepskatalog`-policyane — gjev **to separate issues** (éin
`error`, éin `warning`) for identisk manglande felt:

```bash
podman run --rm -v "$(pwd):/work:ro" mcp-linkml-validator python3 -c "
import sys; sys.path.insert(0, '/work/src/mcp-linkml-validator')
from server import validate_schema
print(validate_schema('id: https://example.org/schema\nname: T\ndescription: D\nprefixes: {ex: https://example.org/}\ndefault_prefix: ex\n', 'felles-datakatalog'))"
```

Ein **minimal patch** for akkurat dette symptomet (hopp over eit
`recommended`-felt som alt er `required` for same scope) er gjennomført
separat i `full-gjennomgang-policy-alvorsgrad-og-overlapp.md` sitt steg 7a.
**Denne specen** gjeld den **fulle konsolideringa** brukaren ønskjer
«i utgangspunktet» — éin einsarta mekanisme for feltnærvær-sjekk, slik at
denne typen dobbeltsignal-feil vert **strukturelt umogleg**, ikkje berre
lappa på symptomnivå.

## Målbilete

Fjern `required:`/`recommended:` som eigne policy-YAML-nøklar heilt.
Uttrykk alle felt-nærvær-krav (`id`, `name`, `title`, `description`,
`version`, `default_prefix`, `license`, og alle framtidige) som vanlege
`checks:`-oppføringar, nøkla på sjekknavn, med full støtte for
alvorsgrad-progresjon per policy-nivå — same mønster som dei ~30 andre
sjekkane i repoet alt følgjer.

## Kartlagt omfang (frå Funn B5.4 — grunnlag for denne specen)

### Ny/generalisert sjekk-type i `server.py`

`_check_schema_field_present` handterer i dag berre `schema`-scope.
Treng éin av:

- **(a)** To nye sjekktypar `class_field_present`/`slot_field_present`
  som itererer høvesvis `schema.classes`/`schema.slots` (same
  iterasjonsmønster som `_check()` gjer i dag).
- **(b)** Éin generalisert `_check_field_present(sv, schema, config,
  issues)` parametrisert med `config["scope"]` ∈ {schema, class, slot} —
  **tilrådd**, sidan dette er éi kjelde for logikken i tråd med
  DRY-prinsippet i CLAUDE.md, i staden for tre nesten-like funksjonar.

Fjern `_check()`-closuren og dei tre kalla til han i `validate_schema()`
(schema/class/slot-løkkene), og fjern
`policy.get("required"/"recommended")`-oppslaga heilt.

### Migrering av alle fem policy-YAML-filer

- **`bronze.yaml`:** 3 required-felt (`id`, `name`, `title`) + 4
  recommended-felt (`description` × 3 scope, `version`) = **7 nye
  `checks:`-oppføringar**. Dette er den einaste fila som treng reelt nye
  oppføringar.
- **`silver.yaml`, `gold.yaml`, `felles-datakatalog.yaml`,
  `felles-begrepskatalog.yaml`:** kvar sine `required`/`recommended`-
  lister er i dag reint **redundante delmengder** av det som alt er arva
  frå bronse (ingen nye felt utover det bronse alt dekkjer) — dei kan
  **fjernast heilt** ved konsolidering, ikkje migrerast, sidan felta dei
  listar alt får `checks:`-oppføringar frå bronse-nivået og vert arva som
  normalt.
- **Særskilt:** `felles-datakatalog.yaml`/`felles-begrepskatalog.yaml`
  sin eigen `recommended: [title, version]` er kjelda til
  dobbeltsignal-buggen omtalt over — desse to linjene fjernast heilt ved
  konsolidering (dei var feilen, ikkje eit reelt krav).

### Alvorsgrad-progresjon som må uttrykkjast eksplisitt i dei nye `checks:`-oppføringane

For at konsolideringa ikkje skal **endre** noverande åtferd (kun
mekanismen, ikkje utfallet), må kvar ny `checks:`-oppføring i `bronze.yaml`
ha nøyaktig den alvorsgrada feltet har i dag via `required`/`recommended`:

| Felt | Scope | Noverande alvorsgrad (alle nivå) |
|---|---|---|
| `id` | schema | `error` |
| `name` | schema | `error` |
| `title` | schema | `error` |
| `description` | schema | `warning` |
| `description` | class | `warning` |
| `description` | slot | `warning` |
| `version` | schema | `warning` (men sjå steg 4 i `full-gjennomgang-…`-specen: skal bli `error` på gull — planlegg denne progresjonen inn i den nye `checks:`-oppføringa direkte, ikkje som eit eige `required`-triks) |

### `tree_root`-avgjerd (må takast eksplisitt før koding)

Den noverande `_check()`-closuren filtrerer **ikkje** vekk `tree_root`-
klassen frå `class`-scope-sjekkane (i motsetnad til
`all_classes_have_identifier`/`all_classes_have_class_uri`/
`all_classes_have_concept_ref`, som alle eksplisitt hoppar over
`tree_root`). Før implementering må det avgjerast om den nye
`class_field_present`/generaliserte sjekken skal:

- **(a)** halde fram med noverande, ufiltrerte åtferd (containerklassen
  vert framleis sjekka for `description`) — **ingen åtferdsendring**, eller
- **(b)** leggje til same `tree_root`-filter som dei andre klasse-
  sjekkane, for konsistens — **ei åtferdsendring** (containerklassar
  sluttar å få `description`-åtvaring).

**Tilråding:** vel (a) som standard for å halde konsolideringa
åtferdsnøytral, med mindre brukaren eksplisitt ønskjer (b) som ei
separat, medviten innstramming/lemping.

### Testpåverknad

Berre **2 stader** i `tests/test_mcp_policies.py` assertar direkte på
kodane `missing_required_metadata`/`missing_recommended_metadata` (funne
ved `grep -n "missing_required_metadata\|missing_recommended_metadata"
tests/test_mcp_policies.py`). Desse må oppdaterast til å forvente den nye
`checks:`-genererte koden i staden. Låg risiko, låg innsats — men **heile
testsuiten** bør likevel køyrast på nytt etter migreringa, sidan
`required`/`recommended`-mekanismen i dag påverkar `errorCount`/
`warningCount` implisitt i fleire av dei eksisterande fixture-baserte
testane (`_BRONZE_PASS`, `_SILVER_PASS`, `_GOLD_PASS` har alle `title`,
`description`, `version` sett nettopp for å tilfredsstille denne
mekanismen — dei skal framleis validere reint etter migrering, men bør
verifiserast eksplisitt).

### README-påverknad

Ingen — README dokumenterer **utfall** («schema.title til stades —
error»), ikkje mekanisme, og treng ikkje endrast av denne refaktoreringa
i seg sjølv (kvar rad si Alvor-verdi er uendra).

## Steg

1. Implementer `_check_field_present(sv, schema, config, issues)` i
   `server.py`, parametrisert med `scope` ∈ {schema, class, slot} (sjå
   `tree_root`-avgjerd over for `class`-scope-åtferd).
2. Registrer `field_present` som ny sjekktype i `_CHECK_HANDLERS`.
3. Fjern `_check()`-closuren og dei tre kalla til han i
   `validate_schema()`, og fjern `required`/`recommended`-oppslaga.
4. Legg til 7 nye `checks:`-oppføringar i `bronze.yaml` (sjå tabellen
   over for feltnavn/scope/alvorsgrad), inkludert `version` sin planlagde
   error-progresjon på gullnivå (som ei direkte `severity: error`-
   redeklarering i `gold.yaml`, ikkje som eit `required`-triks — dette
   er nettopp poenget med konsolideringa).
5. Fjern `required:`/`recommended:`-blokkene heilt frå `bronze.yaml`,
   `silver.yaml`, `gold.yaml`, `felles-datakatalog.yaml`,
   `felles-begrepskatalog.yaml`.
6. Oppdater dei 2 testane i `tests/test_mcp_policies.py` som assertar
   direkte på `missing_required_metadata`/`missing_recommended_metadata`,
   til å forvente den nye koden.
7. Køyr `make mcp-linkml-valider-modell-test` — verifiser at
   `errorCount`/`warningCount` er **uendra** for alle eksisterande
   fixturar (`_BRONZE_PASS`, `_SILVER_PASS`, `_GOLD_PASS`) samanlikna med
   før migreringa, sidan denne specen skal vere ei rein
   mekanisme-konsolidering, ikkje ei åtferdsendring (utover det som alt
   er gjort separat i `full-gjennomgang-…`-specen).
8. Køyr `make mcp-linkml-valider-modell SCHEMA=... POLICY=<kvar>` mot eit
   utval reelle skjema (t.d. dei same brukt i tidlegare
   regresjonssjekkar i denne policy-serien) for å stadfeste at
   `errorCount`/`warningCount` er uendra i praksis, ikkje berre i
   testfixturane.

## Handlingsliste

- [ ] Steg 1: `_check_field_present`-funksjon
- [ ] Steg 2: Registrer `field_present`-sjekktype
- [ ] Steg 3: Fjern `_check()`-closuren og required/recommended-oppslag
- [ ] Steg 4: 7 nye `checks:`-oppføringar i bronze.yaml
- [ ] Steg 5: Fjern required:/recommended: frå alle fem policyfiler
- [ ] Steg 6: Oppdater dei 2 påverka testane
- [ ] Steg 7: Testverifisering (uendra errorCount/warningCount)
- [ ] Steg 8: Regresjonssjekk mot reelle skjema
