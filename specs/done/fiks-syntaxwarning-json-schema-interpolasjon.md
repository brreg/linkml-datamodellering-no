# Plan: Fiks `SyntaxWarning: invalid escape sequence` i `new-modell.sh` (og latent datakorrupsjonsrisiko)

## Bakgrunn

`make new-modell DOMAIN=oreg NAME=enhetsregisteret-bvrfriv
JSON_SCHEMA=src/tmp/bvrfriv_lm_v1.schema.json` skriv ut:

```
<string>:10: SyntaxWarning: invalid escape sequence '\d'
```

## Rotårsak — stadfesta

`src/assets/scripts/scaffolding/new-modell.sh` byggjer eit stort
`python3 -c "..."`-skript ved å interpolere bash-variablar direkte inn i
Python-kjeldekode. Éin av desse variablane, `$LINKML_YAML` (den rå
LinkML-YAML-teksten frå MCP-serveren), vert lima rått inn i eit Python
triple-quoted-strenglitteral:

```python
raw = '''$LINKML_YAML'''
```

Dette er **linje 10** i `-c`-strengen (talt frå den tomme linja rett etter
opnings-`"`), som stemmer eksakt med `<string>:10` i åtvaringa.

`bvrfriv_lm_v1.schema.json` inneheld fleire `"pattern"`-felt med
JSON-escapa regex-uttrykk, t.d.:

```json
"pattern": "^(\\d+\\.)?(\\d+\\.)?(\\*|\\d+)$"
```

Etter at MCP-serveren (`converter.py`) har lese JSON Schema-en og skrive
mønsteret vidare inn i den genererte LinkML-YAML-en, inneheld
`$LINKML_YAML` den literale delstrengen `pattern: ^(\d+\.)?(\d+\.)?(\*|\d+)$`
— éin bakover-skråstrek, ikkje to. Når bash interpolerer denne teksten inn i
`raw = '''...'''`, ser Python-tolkaren `\d` som eit strenglitteral-escape han
ikkje kjenner att (`\d` er ikkje eit gyldig Python-escape), og åtvarar.

**Stadfesta empirisk** (minimal reproduksjon, identisk åtvaringstekst og
linjenummer-mønster):

```bash
python3 -c "
import warnings
warnings.simplefilter('always')
s = '''pattern: ^(\d+\.)?(\d+\.)?(\*|\d+)\$'''
"
# → <string>:4: SyntaxWarning: invalid escape sequence '\d'
```

**Stadfesta at dette er den einaste staden i heile `src/assets/scripts/`**
som brukar dette interpolasjonsmønsteret (`'''$VAR'''` inn i eit
`python3 -c`-skript) — `grep -rn "'''\$" src/assets/scripts/` gir eitt
treff, akkurat denne linja.

**Kvifor det ikkje skjedde før JSON_SCHEMA-flagget** (sjå
`specs/done/new-modell-json-schema-flagg.md`): linja `raw = '''$LINKML_YAML'''`
fanst frå før, men vart berre trafikkert med `--input-format empty`-stubben
(ingen `pattern:`-felt, ingen bakover-skråstrekar) inntil JSON Schema-vegen
gjorde det til ein realistisk, oppmuntra arbeidsflyt med skjema som faktisk
inneheld regex-mønster.

## Alvorlegare enn berre ei åtvaring — latent, stille datakorrupsjon

`\d` er **ikkje** eit gyldig Python-escape, så verdien vert bevart
bokstaveleg (kun ei åtvaring, ingen skade — verifisert: `repr()` av strengen
over viser `'\\d'`, altså framleis éin bakover-skråstrek + `d`). Men Python
**har** ei liste gyldige escape-sekvensar (`\n`, `\t`, `\r`, `\\`, `\'`,
`\"`, `\xHH`, `\uXXXX` m.fl.) som **vert tolka**, ikkje bevart bokstaveleg —
**heilt utan åtvaring**:

```bash
python3 -c "
s = '''value: a\nb'''
print(repr(s))
"
# → 'value: a\nb'   (ein FAKTISK linjeskift-teikn, ikkje bokstavane \, n)
```

Dersom eit framtidig JSON Schema har eit `pattern`, `description`, `example`
eller anna fritekstfelt som inneheld `\n`, `\t`, `\r`, `\\`, `\'` eller `\"`
(alle plausible i regex-mønster og fritekst — t.d. eit mønster som
ekskluderer linjeskift, `[^\n]+`), vil `raw = '''$LINKML_YAML'''` **stille
endre verdien** til noko anna enn det MCP-serveren faktisk genererte, utan
nokon feilmelding. Dette er eit reelt, om enn i dag ikkje-utløyst
(`grep`-a alle `src/tmp/*.schema.json` sine `pattern`-felt — ingen
inneheld i dag `\n`/`\t`/`\r`/`\\`/quote-sekvensar), datakorrupsjonshol i
sjølve mekanismen — ikkje berre eit kosmetisk åtvaringsproblem.

## Løysing

Ikkje undertrykk åtvaringa (t.d. med `-W ignore`) — det ville late det
underliggande korrupsjonsholet stå ope. Fjern i staden heile
interpolasjons-mekanismen: skriv `$LINKML_YAML` til ei mellombels fil, og
lat Python **lese fila** i staden for å ha innhaldet embedda som
kjeldekode-literal. Filinnhald gjennom `open().read()` er ikkje underlagt
Python sin strenglitteral-parsing i det heile — ingen escape-tolking, uansett
kva teikn originalteksten inneheld.

```bash
RAW_SCHEMA_TMP=$(mktemp)
trap 'rm -f "$RAW_SCHEMA_TMP"' EXIT
printf '%s' "$LINKML_YAML" > "$RAW_SCHEMA_TMP"

read CONTAINER_CLASS CONTAINER_SLOT < <(python3 -c "
import sys
import datetime
from pathlib import Path
import yaml

sys.path.insert(0, '$REPO_ROOT/src/assets/scripts')
from utils.codeowners import load_codeowners, find_owner_org

with open('$RAW_SCHEMA_TMP', encoding='utf-8') as f:
    raw = f.read()
lines = raw.splitlines(keepends=True)
...
")
```

`$RAW_SCHEMA_TMP` (ein `mktemp`-generert sti, t.d. `/tmp/tmp.Xy12Ab`) er
trygg å interpolere som Python-strenglitteral — han inneheld berre
alfanumeriske teikn og skråstrekar, aldri bakover-skråstrekar eller
spesialteikn frå skjemainnhaldet. `trap ... EXIT` ryddar opp fila uansett om
scriptet lukkast eller feilar undervegs (`set -euo pipefail` er alt aktivt i
scriptet).

**Merk:** `$REPO_ROOT` og `$DOMAIN`/`$NAME` (brukt lenger nede i same
`-c`-skript, t.d. `Path('src/linkml/$DOMAIN/$NAME')`) er framleis trygge å
interpolere direkte som i dag — dei er brukarstyrte make-parametrar
(katalog-/filnamn), ikkje fritekst henta frå eit vilkårleg JSON Schema, og
inneheld difor aldri regex-spesialteikn i praksis. Denne spec-en avgrensar
fiksen til `$LINKML_YAML`, den einaste variabelen med reelt ukontrollert
innhald.

## Prioritert handlingsliste

| # | Steg | Fil |
|---|---|---|
| 1 | Skriv `$LINKML_YAML` til mellombels fil (`mktemp` + `trap ... EXIT`) i staden for å interpolere han som Python-strenglitteral | `src/assets/scripts/scaffolding/new-modell.sh` |
| 2 | Endre `raw = '''$LINKML_YAML'''` til `with open('$RAW_SCHEMA_TMP', encoding='utf-8') as f: raw = f.read()` | same fil |
| 3 | Regresjonstest: `make new-modell DOMAIN=<test> NAME=<test> JSON_SCHEMA=src/tmp/bvrfriv_lm_v1.schema.json` — stadfest ingen `SyntaxWarning`, og at genererte `pattern:`-felt i output-skjemaet er byte-for-byte identiske med før fiksen (t.d. `grep pattern` mot både gammal og ny output) | manuell test |
| 4 | Regresjonstest for `--input-format empty`-vegen (utan `JSON_SCHEMA`) — stadfest uendra åtferd | manuell test |
| 5 | Ryddig opprydding av testartefakt (scratch-katalog sletta etter test) | — |

## Avhengigheiter

- Ingen nye verktøy — `mktemp`/`trap` er alt etablert mønster andre stader i
  `src/assets/scripts/` (t.d. `generate-readme-tables.sh`).
- Ingen endring i MCP-serveren, `converter.py` eller request/response-scripta
  — feilen ligg utelukkande i korleis `new-modell.sh` handterer resultatet
  etterpå.

## Utført

Alle fem handlingsliste-punkta gjennomførte, nøyaktig etter planen — ingen
avvik.

- **Steg 1-2:** `raw = '''$LINKML_YAML'''` erstatta med
  `RAW_SCHEMA_TMP=$(mktemp)` + `trap 'rm -f "$RAW_SCHEMA_TMP"' EXIT` +
  `printf '%s' "$LINKML_YAML" > "$RAW_SCHEMA_TMP"`, og Python-sida les no
  fila (`with open('$RAW_SCHEMA_TMP', encoding='utf-8') as f: raw = f.read()`)
  i staden for å ha innhaldet som strenglitteral.
- **Steg 3:** `make new-modell DOMAIN=zztest NAME=zztest-verify
  JSON_SCHEMA=src/tmp/bvrfriv_lm_v1.schema.json` — ingen `SyntaxWarning`.
  Stadfesta at alle fem `pattern:`-felta i det genererte skjemaet er
  byte-for-byte identiske med kjelde-JSON-schema-en sine regex-uttrykk
  (`^(\d+\.)?(\d+\.)?(\*|\d+)$`, `^[\d+() -]+$`, `^[0-9]{5,15}$`,
  `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`, `^[2389][0-9]{8}$`) —
  ingen datakorrupsjon.
- **Steg 4:** `make new-modell DOMAIN=zztest NAME=zztest-verify3` (utan
  `JSON_SCHEMA`) — uendra åtferd, `make lint` framleis «No problems found».
- **Steg 5:** Stadfesta at `trap ... EXIT` faktisk ryddar opp
  (`ls /tmp/tmp.*` → 0 filer etter køyring). Testkatalogane
  (`src/linkml/zztest/`) og `.github/valid-scopes.txt` attende til
  utgangspunktet (42 scopes) etter oppryddinga.

**Endra filer:** `src/assets/scripts/scaffolding/new-modell.sh` (einaste
endring).
