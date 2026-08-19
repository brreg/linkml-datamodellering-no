# Plan: Konsolider dei to JSON-RPC-implementasjonane for `generate_linkml`

## Bakgrunn

Oppfølging av samtalen om `make mcp-linkml-modell-utkast` vs.
`make new-modell`. Begge kallar til slutt same MCP-verktøy
(`generate_linkml` i `src/mcp-linkml-modell-utkast/server.py`), men har
**to heilt separate, ikkje-delte** implementasjonar av å byggje
JSON-RPC-requesten og hente ut svaret:

| | `mcp-linkml-modell-utkast` (make-target) | `new-modell` (scaffold) |
|---|---|---|
| Byggjer request | `src/assets/scripts/makefile/mcp-build-modell-utkast-request.py` | Inline python i `new-modell.sh` |
| Hentar ut svar | `src/assets/scripts/makefile/mcp-write-modell-utkast-response.py` (skriv rett til fil) | Inline python i `new-modell.sh` (skriv til stdout, feiltakast stille via `except: pass`) |
| `inputFormat` | `json-schema` (frå ei eksisterande fil) | `empty` |
| Felt sett | `inputFormat`, `inputContent`, hardkoda `schemaId`/`schemaName`, `profile` | `inputFormat`, `schemaId`, `schemaName`, `schemaTitle`, `profile`, `validate` (ingen `inputContent`) |

Brukaren bad om å konsolidere desse to.

**Avgrensing:** `new-modell.sh` sin **etterfølgjande post-prosessering**
(PascalCase-namngjeving av stub-klassen, fjerning av `id`-slot,
annotasjons-utfylling via CODEOWNERS-oppslag, dcat-ap-no-import-innsetjing,
lisens-kommentar) er **unik forretningslogikk** for scaffolding-bruket,
ikkje duplisert JSON-RPC-mekanikk — ho vert **ikkje** rørt. Konsolideringa
gjeld berre dei to laga som faktisk er identiske i føremål: (1) byggje
`initialize`+`tools/call generate_linkml`-meldingane, og (2) lese
JSON-RPC-svar frå stdin og ekstrahere `linkmlSchema`-teksten.

## Plan

### 1 — Generaliser `mcp-build-modell-utkast-request.py`

Byt frå positional args (`<schema> [format] [profile]`) til `argparse`
med flagg som dekker superset av felta begge kallarane treng:

```
--input-format {json-schema,empty}   (kravd)
--input-file <sti>                   (kravd berre for json-schema; les innhaldet som inputContent)
--schema-id <uri>                    (default: https://example.org/generated, som i dag)
--schema-name <namn>                 (default: generated, som i dag)
--schema-title <tittel>              (default: tom streng)
--profile <profil>                   (default: bronze, som i dag)
--no-validate                        (flagg; validate er True som standard, matchar server sin eigen default)
```

### 2 — Generaliser og omdøyp `mcp-write-modell-utkast-response.py` → `mcp-extract-modell-utkast-response.py`

Ny åtferd: les JSON-RPC-svar frå stdin, ekstraher `linkmlSchema`, **skriv
til stdout** (ikkje til fil) — feil går til stderr med `exit 1` (i staden
for `new-modell.sh` sin noverande `except: pass`, som slukar feil
stille). Filskriving vert kallaren sitt ansvar (matchar alt korleis
`new-modell.sh` brukar resultatet — han fangar det opp i ein
bash-variabel og transformerer det vidare).

### 3 — Oppdater kallarane

**`make/60-mcp.mk`** (`mcp-linkml-modell-utkast`):
```makefile
@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-modell-utkast-request.py \
	--input-format "$(or $(FORMAT),json-schema)" --input-file "$(SCHEMA)" \
	--profile "$(or $(PROFILE),bronze)" \
	| $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE) \
	| $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-extract-modell-utkast-response.py \
	> "$(basename $(SCHEMA))-schema.yaml"
```
Output-stien (`$(basename $(SCHEMA))-schema.yaml`) vert no rekna ut av
Make sjølv (GNU Make sin `basename`-funksjon), i staden for av
skriveskriptet — identisk resultat som før (`tmp/modellnavn.json` →
`tmp/modellnavn-schema.yaml`).

**`new-modell.sh`**: byt ut heile den inline request-bygg/podman/ekstraher-
blokka (linje 44-79) med kall til dei to konsoliderte skripta, same
podman-oppsett som før:
```bash
LINKML_YAML=$(python3 ".../mcp-build-modell-utkast-request.py" \
    --input-format empty --schema-id "$SCHEMA_ID" --schema-name "$SCHEMA_NAME" \
    --schema-title "TODO: tittel for $NAME" --profile silver --no-validate \
  | podman run -i --rm ... "$LINKML_GEN_IMAGE" \
  | python3 ".../mcp-extract-modell-utkast-response.py")
```

**`make/01-containers.mk`**: oppdater kommentaren som nemner
`mcp-write-modell-utkast-response.py` til det nye namnet.

## Sideeffekt (ikkje eit mål i seg sjølv, men verdt å nemne)

`new-modell.sh` sin noverande inline-ekstraksjon slukar feil stille
(`except Exception: pass` — eit unntak frå «Ingen stille feil»-prinsippet
i CLAUDE.md, sidan feil ville gjort `$LINKML_YAML` tom og synt som
«mcp-linkml-modell-utkast returnerte tomt svar» utan årsak). Den nye,
delte ekstraksjonsskripta feilar høgt (`exit 1` + melding til stderr) —
kombinert med `set -euo pipefail` i `new-modell.sh` gjev dette faktiske
feilmeldingar i staden for eit uforklart tomt resultat.

## Filer som vert påverka

- `src/assets/scripts/makefile/mcp-build-modell-utkast-request.py` (generalisert)
- `src/assets/scripts/makefile/mcp-write-modell-utkast-response.py` → omdøypt til `mcp-extract-modell-utkast-response.py` (generalisert)
- `make/60-mcp.mk`
- `src/assets/scripts/scaffolding/new-modell.sh`
- `make/01-containers.mk` (kommentar)

## Handlingsliste

1. [x] Generaliser `mcp-build-modell-utkast-request.py` til argparse-flagg
2. [x] Omdøyp og generaliser `mcp-write-modell-utkast-response.py` →
   `mcp-extract-modell-utkast-response.py`
3. [x] Oppdater `make/60-mcp.mk` sin `mcp-linkml-modell-utkast`-oppskrift
4. [x] Oppdater `new-modell.sh` til å bruke dei konsoliderte skripta
5. [x] Oppdater kommentar i `make/01-containers.mk`
6. [x] Verifiser: `make mcp-linkml-modell-utkast SCHEMA=<eit reelt json-schema-eksempel>`
   og `make new-modell DOMAIN=<domene> NAME=<eit testnamn>` (så rydd opp
   testkatalogen etterpå) gjev identisk resultat som før konsolideringa

## Utført

**Byggjeskript** (`mcp-build-modell-utkast-request.py`): omskrive til
`argparse` med `--input-format`, `--input-file`, `--schema-id`,
`--schema-name`, `--schema-title`, `--profile`, `--no-validate`. Defaultar
(`schema-id=https://example.org/generated`, `schema-name=generated`,
`profile=bronze`) matchar nøyaktig det som var hardkoda før, slik at
`mcp-linkml-modell-utkast` sitt kall ikkje treng spesifisere dei.

**Ekstraksjonsskript**: `mcp-write-modell-utkast-response.py` omdøypt til
`mcp-extract-modell-utkast-response.py` og endra frå å skrive til fil
(basert på ein sti-parameter) til å skrive rein `linkmlSchema`-tekst til
**stdout** — filskriving/vidare prosessering er no kallaren sitt ansvar.
Feilhandtering skjerpa: `exit 1` + melding til stderr i staden for
`new-modell.sh` sin gamle `except Exception: pass` (som slukte feil
stille, eit avvik frå CLAUDE.md sitt «ingen stille feil»-prinsipp).

**`make/60-mcp.mk`**: `mcp-linkml-modell-utkast`-oppskrifta bruker no dei
nye flagga, og reknar ut output-stien med GNU Make sin eigen
`$(basename $(SCHEMA))`-funksjon (identisk resultat som det gamle
skriveskriptet sin `Path.stem`-baserte utrekning). Pipeline+redirect er
halde som **éi** samanhengande recipe-linje (ikkje delt med `;`) slik at
`pipefail` framleis fangar feil korrekt — ein tidleg utkastversjon braut
dette ved å blande ein `OUT=`-variabel og eit etterfølgjande
`log_info`-kall inn i same `;`-kjede, som ville fått Make til berre å sjå
exit-status til det siste (alltid vellykka) kallet; retta før commit.

**`new-modell.sh`**: heile den inline request-bygg/podman/ekstraher-blokka
(tidlegare 36 linjer) bytt ut med kall til dei to delte skripta — same
podman-oppsett (volum-mount av server/converter/validator/profiles)
uendra. Den unike post-prosesseringa (PascalCase-namngjeving,
CODEOWNERS-baserte annotasjonar, dcat-ap-no-import, lisenskommentar) er
**heilt urørt**, som planlagt.

**`make/01-containers.mk`**: kommentaren som nemner skriveskriptet ved
namn er oppdatert til det nye namnet.

**Verifisert med reelle køyringar** (testartefakt rydda opp etterpå,
`.github/valid-scopes.txt` regenerert til opphavleg 37 scopes,
`git status` reint):
- `make mcp-linkml-modell-utkast SCHEMA=src/tmp/test-konsolidering.json`
  (kopi av eit eksisterande JSON Schema-eksempel) — genererte korrekt
  skjema (985 linjer) **og** automatisk roundtrip-test gjekk grønt
- `make new-modell DOMAIN=oreg NAME=test-konsolidering-tmp` — genererte
  korrekt skjema med rett PascalCase-klassenamn, CODEOWNERS-utleidde
  annotasjonar (`utgiver`, `endringsdato`, `utgivelsesdato`), versjonslåst
  dcat-ap-no-import, eksempelfil, `build.yaml`, `description.md` — byte-for-
  byte konsistent med korleis skriptet oppførte seg før konsolideringa
