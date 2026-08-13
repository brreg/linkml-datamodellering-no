# MCP-validator: vis reelle feilmeldingar + versjonslåste importar over relativ import-djupne

## Bakgrunn

`make mcp-linkml-valider-modell SCHEMA=src/linkml/oreg/blomsterregisteret/blomsterregisteret-schema.yaml POLICY=bronze`
feila med ein kryptisk `KeyError: 'result'` i staden for ei brukbar feilmelding.

Grave fram to separate problem:

### 1. `flatten-and-validate.bash` gøymer den reelle feilmeldinga

`src/mcp-linkml-validator/flatten-and-validate.bash` (linje 68-74) filtrerer
MCP-serveren sitt stdout med:

```python
r = json.loads(line)
if r.get('id') == 2:
    print(r['result']['content'][0]['text'])
```

Når `tools/call` sjølv feilar, returnerer serveren korrekt
`{"jsonrpc": "2.0", "id": 2, "error": {...}}` (jf. `server.py` linje 1195-1196),
men filteret føreset ubetinga at `result` finst. Resultatet er at
`r['result']` kastar `KeyError: 'result'`, og den faktiske feilmeldinga
(`"Unknown CURIE prefix: https"` i dette tilfellet) går tapt.

### 2. Underliggande årsak: upstream-bug i `linkml_runtime` sin import-oppløysing

`blomsterregisteret-schema.yaml` (nytt, ikkje-committa scaffold) importerer
`dcat-ap-no-schema` via ein versjonslåst `raw.githubusercontent.com`-URL i
staden for relativ sti — eit brot på konvensjonen i
[mkdocs/docs/arkitektur/importhierarki.md](../../mkdocs/docs/arkitektur/importhierarki.md#import-på-tvers-av-domenemodellar),
som seier AP-NO-profilar skal importerast **relativt** (dei endrar seg
sjeldan), medan **versjonslåsing** (pinning via git-tag-URL) er meint for
import mellom domenemodellar.

Rotårsaka vart stadfesta ved å køyre `linkml_runtime` direkte inne i
validator-kontaineren (sjå transkript i denne specen sin PR/commit-historikk
— ikkje reprodusert her). `SchemaView.imports_closure()` i
`linkml_runtime/utils/schemaview.py` inneheld denne grenen for å løyse
relative importar i det importerte skjemaet sitt eige `imports:`-felt:

```python
if "/" in sn and ":" not in i:
    todo.append(os.path.normpath(str(Path(sn).parent / i)))
```

Når `sn` (namnet/nøkkelen på skjemaet som nett vart lasta) er ein full URL
som `https://raw.githubusercontent.com/.../dcat-ap-no/dcat-ap-no-schema`, og
det importerte skjemaet sjølv har ein relativ import som
`../dqv-ap-no/dqv-core-schema`, brukar koden `pathlib.Path` og
`os.path.normpath` — verktøy laga for filsystem-stiar. `pathlib.Path`
kollapsar **doble skråstrekar** som ikkje står heilt fremst i strengen, så
`Path("https://raw.githubusercontent.com/.../dcat-ap-no-schema").parent`
vert til `https:/raw.githubusercontent.com/.../dcat-ap-no` — **éin
skråstrek**, ikkje to. Det etterfølgjande CURIE-oppslaget
(`Namespaces.uri_for`) ser ingen `"://"`, tolkar strengen som ein CURIE, og
feilar med `Unknown CURIE prefix: https` fordi `https` ikkje er ein
registrert prefiks.

Dette er **ikkje** avgrensa til `blomsterregisteret`. Det treff **alle**
skjema som vert importerte via versjonslåst URL **og** som sjølv har meir
enn eitt nivå med relative importar (`../`) i importkjeda si. Eksempelet i
importhierarki.md fungerer i dag berre fordi `ngr-adresse-schema` berre
importerer `linkml:types` (ingen vidare relativ import) — men t.d.
`samt-bu-schema` (som importerer `dqv-ap-no-schema` relativt, som igjen
importerer `dcat-ap-no-schema` relativt) ville truffe akkurat same bug
dersom nokon prøvde å importere han via versjonslåst URL slik dokumentet
elles anbefaler for domenemodell-til-domenemodell-import.

## Steg

1. **Fiks feilvising i `flatten-and-validate.bash`** — det andre
   `python3 -c`-filteret skal sjekke om responsen har `error` før det
   føreset `result`, og skrive `error.message` til stderr med ikkje-null
   exit code i staden for å krasje med `KeyError`.
2. **Proposer** (ikkje implementer utan godkjenning) ein fiks som let
   versjonslåste (`raw.githubusercontent.com`)-importar halde fram å
   fungere sjølv når det importerte skjemaet har fleire nivå med relative
   importar. Sjå vurderte alternativ under.

## Vurderte alternativ for steg 2

| Alternativ | Skildring | Vurdering |
|---|---|---|
| A — Behald berre relativ import for AP-NO-profilar (status quo, ingen kodeendring) | Fiks berre `blomsterregisteret-schema.yaml` sin import til relativ sti, slik konvensjonen alt seier. Versjonslåsing vert avgrensa til skjema utan vidare relative importar (t.d. reine NGR-skjema). | Trygt og null risiko, men innsnevrar kva "versjonslåst import" faktisk kan brukast til i praksis — dokumentet sitt løfte held ikkje for skjema som importerer AP-NO-profilar. |
| B — Monkeypatch `SchemaView.imports_closure` sin relative-oppløysingsgrein i eigne script | Overstyr den buggy grenen (`Path(sn).parent / i` → `urllib.parse.urljoin` når `sn` inneheld `"://"`, elles uendra filsystem-åtferd) i eit lite delt hjelpemodul, importert av `server.py`, `batch-linkml-validate.py`, `gen-modelldcat-elements.py` og `validate-modelldcat.py` (dei fire stadene `SchemaView(...)` vert kalla direkte). | Løyser problemet fullt ut for alle versjonslåste importkjeder, men bind oss til den interne implementasjonen av ein spesifikk `linkml_runtime`-versjon — må kontrollerast på nytt ved kvar `linkml_runtime`-oppgradering (byggfeil er venta symptom dersom upstream endrar signaturen). |
| C — Meld saka oppstraums til `linkml`/`linkml-runtime` og vent | Ingen eigen kodeendring; blokkert på ekstern fiks. | Riktig langsiktig løysing, men løyser ikkje noko no. Bør gjerast uavhengig av A/B. |

**Val:** Brukar valde alternativ B (monkeypatch). C (meld oppstraums til
linkml-runtime) er dokumentert som open oppfølging i `bugs/`-fila, men ikkje
utført av LLM (ekstern handling — brukar avgjer sjølv om/når).

`blomsterregisteret-schema.yaml` sin versjonslåste URL-import av
`dcat-ap-no-schema` er **ikkje** endra til relativ sti — det var heile
poenget med å velje alternativ B at pinna importar skal halde fram å
fungere. Verifisert med full roundtrip gjennom
`flatten-and-validate.bash`: `Unknown CURIE prefix`-feilen er borte, skjemaet
validerer no reelt (0 feil, 5 åtvaringar om ufullstendige scaffold-metadata).

Merk: dette betyr at `blomsterregisteret-schema.yaml` framleis avvik frå
konvensjonen i importhierarki.md (som seier AP-NO-profilar skal importerast
**relativt**, ikkje versjonslåst) — men sidan skjemaet no fungerer korrekt
med pinna import, og brukar eksplisitt bad om å kunne halde fram å bruke
versjonslåste importar, er dette late urørt. Om ønskt kan doc-teksten
justerast seinare til å nemne at versjonslåst import no er trygt for
skjema med djupare importkjeder òg.

## Handlingsliste

- [x] `src/mcp-linkml-validator/flatten-and-validate.bash`: vis `error.message` i staden for å krasje på manglande `result`
- [x] Avklar med brukar kva for alternativ (A/B/C) som skal implementerast for steg 2 — valde B
- [x] Implementer B: `src/assets/scripts/utils/linkml_relative_import_patch.py` + kall frå dei 4 stadene `SchemaView(...)` vert brukt direkte (`server.py`, `batch-linkml-validate.py`, `gen-modelldcat-elements.py`, `validate-modelldcat.py`)
- [x] `bugs/relativ-import-via-versjonslast-url.md` (BUG-15) + oppføring i `BUGS.md`
- [x] Verifisert: `flatten-and-validate.bash` mot `blomsterregisteret-schema.yaml` med uendra pinna import — går no gjennom (`valid: true`, 0 feil)

## Utført

- `src/mcp-linkml-validator/flatten-and-validate.bash`: filteret skil no `error`- frå `result`-responsar, skriv `error.message` til stderr og returnerer exit 1 i staden for å krasje med `KeyError: 'result'`
- `src/assets/scripts/utils/linkml_relative_import_patch.py` (ny fil): monkeypatchar `SchemaView.imports_closure()` sin relative-import-oppløysing til å bruke `urllib.parse.urljoin` for URL-baserte skjemanamn — sjølv-verifiserande (hoppar over med tydeleg åtvaring dersom upstream-kjeldekoden ikkje lenger matchar det forventa mønsteret)
- Patch-kall lagt til i dei fire stadene `SchemaView(...)` vert instansiert direkte: `src/mcp-linkml-validator/server.py`, `src/assets/scripts/makefile/batch-linkml-validate.py`, `src/assets/scripts/makefile/gen-modelldcat-elements.py`, `src/assets/scripts/makefile/validate-modelldcat.py`
- `bugs/relativ-import-via-versjonslast-url.md` (BUG-15, ny fil) + oppføring i `BUGS.md`
- Verifisert end-to-end: `bash src/mcp-linkml-validator/flatten-and-validate.bash src/linkml/oreg/blomsterregisteret/blomsterregisteret-schema.yaml bronze` går frå `Unknown CURIE prefix: https`-krasj til `valid: true` (0 feil, 5 åtvaringar om ufullstendige scaffold-metadata) — utan å endre skjemaet sin versjonslåste import
