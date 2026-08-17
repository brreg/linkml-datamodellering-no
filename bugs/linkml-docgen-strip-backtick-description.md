# Bug: LinkML `gen-doc` strippar backticks frå `description`-felt

**ID:** BUG-20
**Status:** `open`
**Komponent:** `linkml` (docgen)
**Oppdaga:** 2026-08-17

## Symptom

Eit `description:`-felt i kjeldeskjemaet som brukar backticks (kode-span) for
å verne ein plassholdar-URL frå å verte tolka som ei ekte lenkje —
t.d. `` `https://psi.norge.no/los/tema/<navn>` `` — mistar backtickane når
`gen-doc` (via `make gen-doc`) genererer den tilhøyrande slot-/klasse-sida.
Resultatet er bar prosa: `https://psi.norge.no/los/tema/<navn>`, utan
kode-span-vern.

Dette gjer at lenkjesjekk-verktøyet (lychee) sin bare-URL-detektor forsøker å
følgje teksten som ei ekte lenkje. Sidan `<navn>` ikkje er eit gyldig
URL-teikn, stoppar ekstraksjonen ved `<`, og lychee sjekkar den trunkerte
`https://psi.norge.no/los/tema/` — som gjev eit reelt 404 (navnerommet krev
eit temanavn etter skråstreken).

## Berørte skjema / sider

Stadfesta i `mkdocs/docs/oreg/lunchregisteret/klasser/tema.md` (og truleg
alle andre sider som viser `tema`-sloten frå `dcat-ap-no-schema.yaml`, sidan
description-teksten er felles via import).

## Rot-årsak

Kjeldeteksten i `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` (slot
`tema`) har korrekt backtick-vern:

```yaml
description: >-
  ... Bruk hovudtema (`https://psi.norge.no/los/tema/<navn>`) og eventuelt
  undertema i tillegg. ...
```

Samanlikning av kjelda mot `generated/oreg/lunchregisteret/docs/tema.md`
(rå gen-doc-output, før vår eigen `mkdocs/publish.sh`-pipeline rører ho)
stadfester at backtickane alt manglar i gen-doc sitt eige output. Våre eigne
Jinja-malar (`src/assets/templates/docgen/class.md.jinja2`,
`slot.md.jinja2`) gjer rein passthrough av `element.description`
(`_{{ element_description_line }}_`) utan noka form for tekstprosessering —
stripping skjer difor før malen får teksten, truleg ein stad i
`linkml`/`linkml-runtime` sin eigen YAML-lasting eller
`SchemaView`-normalisering av description-felt. **Ikkje fullstendig
rotårsak-granska** i `linkml`-pakken sjølv — krev vidare gransking av
`linkml.generators.docgen` og/eller `linkml_runtime.utils.schemaview` for
å stadfeste nøyaktig kva steg som fjernar backtickane.

## Workaround

Eksakt-treff-eksklusjon i `.github/lychee.toml`:

```
"^https://psi\\.norge\\.no/los/tema/$"
```

Denne dekkjer berre den trunkerte, alltid-ugyldige forma (temanavn manglar).
Ho ekskluderer ikkje reelle `los/tema/<faktisk-navn>`-lenkjer andre stader i
dokumentasjonen. Sjå
`specs/done/lenkjesjekk-runde3-fiks-resterande-feil.md` kategori D2 for
full gransking og verifisering (`curl` mot verten, filsamanlikning kjelde vs.
generert output).

## Løysing

Krev anten:
1. Ei upstream-fiksing i `linkml` sin docgen-pipeline som bevarer backticks i
   `description`-felt, eller
2. Ei omformulering av kjelde-descriptions som unngår å leggje eksempel-URL-ar
   med `<plassholdar>`-syntaks i prosatekst (t.d. bruk eit eksplisitt
   tekst-eksempel utan URL-form, eller flytt plassholdaren til eit eige
   kode-eksempel-avsnitt som ikkje går gjennom same rendring).

Når ei av desse er på plass: fjern eksklusjonen frå `.github/lychee.toml` og
oppdater denne fila til `Status: løyst`.
