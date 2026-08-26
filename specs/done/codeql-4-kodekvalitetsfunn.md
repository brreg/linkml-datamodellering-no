# Plan: Fiks 4 opne CodeQL-funn

**Kortnavn:** `codeql-4-kodekvalitetsfunn`
**Dato:** 2026-08-26

---

## Bakgrunn

CodeQL-jobben (`.github/workflows/codeql.yml`) har flagga 4 opne funn i
`python`-analysen. Alle fire er kodekvalitetsfunn (ikkje tryggleiksrelaterte
— `security_severity_level` er `null` på alle):

| # | Rule | Fil | Linje | Melding |
|---|---|---|---|---|
| 69 | `py/file-not-closed` | `.scratch-verify/verify_instance.py` | 12 | File is opened but is not closed |
| 68 | `py/implicit-string-concatenation-in-list` | `mkdocs/lib/scripts/generate-modellanalyse-md.py` | 156 | Implicit string concatenation. Maybe missing a comma? |
| 63 | `py/unused-local-variable` | `mkdocs/lib/scripts/generate-modellanalyse-md.py` | 150 | Variable `_schema` is not used |
| 62 | `py/unused-local-variable` | `mkdocs/lib/scripts/generate-modellanalyse-md.py` | 149 | Variable `_domain` is not used |

### Funn per fil

**`.scratch-verify/verify_instance.py`** — sjekka med `git ls-files` og
`grep -rn "scratch-verify"` mot `Makefile`, `*.mk`, `*.py`, `*.sh`, `*.yml`:
scriptet (og dei 3 genererte eksempel-YAML-filene ved sida av) er tracka i
git (kom inn i commit `f8f2f950`, "feat(gen-eksempeldata)"), men er ikkje
referert av noko make-target eller CI-workflow. Eit orphan manuelt
debug-script, ikkje del av pipelinen. Brukar har bekrefta: **fjern heile
katalogen** i staden for å fikse `open()`-kallet — fjernar CodeQL-funnet ved
rota og ryddar vekk daud kode.

**`mkdocs/lib/scripts/generate-modellanalyse-md.py` linje 149-150** —
`_domain = sys.argv[2]` og `_schema = sys.argv[3]` er alt understreka
(konvensjon for "bevisst ubrukt"), men CodeQL flaggar dei likevel. Ein
eksisterande kommentar (linje 145-148) forklarer at verdiane er tekne imot
for symmetri med `generate-validation-md.py` sitt grensesnitt og for
framtidig bruk, men aldri lest. Minimal fiks: ikkje bind verdiane til
variabelnamn i det heile — behald `len(sys.argv) < 4`-valideringa og
kommentaren (justert), men fjern sjølve tilordningane. Ingen
åtferdsendring.

**`mkdocs/lib/scripts/generate-modellanalyse-md.py` linje 156-164** — to
stader med implisitt strengsamanslåing inne i `lines`-lista:
- linje 156-161: éin lang forklaringstekst bygd av 6 tilstøytande
  strenglitteralar (skal vere **éitt** listeelement)
- linje 163-164: éin f-streng bygd av 2 tilstøytande f-strenglitteralar
  (skal òg vere **éitt** listeelement)

Begge er tilsikta (lange linjer delt opp for lesbarheit), ikkje ein
manglande-komma-feil. CodeQL sin regel kan likevel ikkje skilje tilsikta
frå utilsikta implisitt samanslåing, difor flagget. Minimal fiks som
fjernar tvitydigheita utan åtferdsendring: byt tilstøytande
strenglitteralar med eksplisitt `+`-samanslåing mellom kvar del. Talet på
listeelement og innhaldet i kvar streng er identisk før/etter.

## Tiltak

1. **Fjern `.scratch-verify/`** — slett heile katalogen
   (`verify_instance.py` + dei 3 `*-eksempel-generert.yaml`-filene) med
   `git rm -r .scratch-verify/`. Løyser funn #69.
2. **Fjern ubrukte variablar i `generate-modellanalyse-md.py`** — fjern
   linje 149-150 (`_domain = sys.argv[2]`, `_schema = sys.argv[3]`), juster
   kommentaren over til å forklare at `sys.argv[2]`/`sys.argv[3]` ikkje vert
   bundne til namn sidan dei ikkje er i bruk. Løyser funn #62 og #63.
3. **Gjer implisitt strengsamanslåing eksplisitt** i same fil, linje
   156-164 — byt dei to stadene med tilstøytande strenglitteralar (den
   lange forklaringsteksten og f-strengen med `MODELL_ANALYSE_WORKFLOW_URL`)
   til eksplisitt `+`-samanslåing. Løyser funn #68.
4. **Verifiser** — køyr
   `podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/codeql.yml`
   er ikkje relevant her (ingen workflow-endring), men køyr
   `python3 -m py_compile mkdocs/lib/scripts/generate-modellanalyse-md.py`
   (eller tilsvarande via eksisterande make-target som brukar scriptet,
   t.d. `make docs-publish` sitt Steg 2) for å stadfeste at scriptet framleis
   fungerer identisk etter endringane.
5. **Stadfest i CodeQL** — etter push til `main`, sjekk at dei 4 funna vert
   automatisk lukka (`gh api repos/brreg/linkml-datamodellering-no/code-scanning/alerts --jq '.[] | select(.state=="open")'`
   bør ikkje lenger vise #62, #63, #68, #69).

## Utført

Tiltak 1-4 gjennomførte 2026-08-26:

1. `.scratch-verify/` fjerna (`verify_instance.py` + 3 genererte
   eksempel-YAML-filer) — løyser #69.
2. `_domain`/`_schema`-tilordningane fjerna frå
   `generate-modellanalyse-md.py`, kommentar justert — løyser #62, #63.
3. Implisitt strengsamanslåing bytt til eksplisitt `+` i same fil (to
   stader: forklaringstekst og f-streng) — løyser #68.
4. Verifisert: `py_compile` OK, og manuell køyring av scriptet mot ein tom
   analyse-katalog stadfesta at dei to tekststrengane framleis vert sette
   saman til éin identisk linje kvar.

Tiltak 5 (stadfesting i CodeQL) attstår til etter commit/push av brukaren —
ikkje utført av LLM, jf. prinsippet om at LLM aldri kjører
commit/push/add.
