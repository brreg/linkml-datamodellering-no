# Plan: Fyll inn Los-tema for alle Informasjonsmodell-oppføringar i modellkatalogane

## Bakgrunn

`generate / modellkatalog`-jobben i `.github/workflows/generate.yml` har
feila på `main` sidan commit `7ee7b0e0` (MD2–MD4/MD6-utrullinga), og
`publish`-jobben er dermed hoppa over sidan (dokumentasjonsportalen er ikkje
republisert). Rot-årsak stadfesta via reproduksjon lokalt og i CI-logg
(`gh api .../actions/jobs/<id>/logs`): `make domain-gen-data
DOMAIN=modellkatalog` kallar `linkml-convert --output-format ttl` på alle 6
org-katalogdatafilene, og dette krasjar med

```
ValueError: File "<katalog>.yaml", line N, col 5: Unknown CURIE prefix: @base
```

Verifisert ved å monkey-patche `Namespaces.uri_for` at den faktiske verdien
som feiler er den **lokale `tema: - TODO`**-plasshaldaren — `tema` har
`range: uriorcurie`, og strengen `"TODO"` har ingen kolon, så
`rdflib_dumper` sin CURIE-oppslagslogikk tolkar det som ein CURIE utan
prefix og feilar når det ikkje finst noko standard-namnerom («@base») å
slå opp mot. Dette er **ikkje** ein ny `linkml`/`linkml-runtime`-bug — det er
ein eksisterande data-fullstendigheitsmangel frå MD2 (`update-modellkatalog.py`
sin `make_stub()` set `tema: ["TODO"]` for nye skjema, jf. kommentar i
skriptet: «For nye skjema vert det oppretta ein stub med TODO-verdiar for
desse»). Alle 23 skjema (alle 6 org-katalogar) har framleis denne
plasshaldaren ufylt.

Brukar avklarte (2026-06-21) at riktig løysing er å fylle inn reelle
Los-tema-URI-ar (ikkje fjerne `modellkatalog` frå generate-workflowen, og
ikkje eit mellombels CI-skip).

## Steg

### Steg 1 — Lag forslag til Los-tema per skjema ✓

Brukte `mcp__linkml-begrep-utkast__list_los_tema` og skjemaa sine
`tittel`/`beskrivelse`-felt til å foreslå eitt hovudtema per skjema for alle
23 skjema. Lagt fram i chat. Brukar godkjente forslaget med éi endring:
`fint-ressurs` og `ngr-person` (opphavleg usikre, foreslått «Digitalisering»
og «Personvern») skulle begge vere **Offentlig forvaltning**.

### Steg 2 — Skriv inn godkjende Los-tema ✓

Erstatta `tema: - TODO` med godkjent Los-tema-URI for alle 23
`Informasjonsmodell`-oppføringar i alle 6 `<org>-modellkatalog.yaml`.
4 oppføringar (`ngr-virksomhet`, `register-over-aksjeeiere` i brreg, samt
dei to allereie nemnde) hadde allereie reelle tema-verdiar frå før (ikkje
sett av denne specen) — urørte.

### Steg 3 — Verifiser ✓

1. `make mcp-validate SCHEMA=... POLICY=felles-datakatalog INSTANCE=...` for
   alle 6 katalogar: `errorCount: 0`.
2. `make domain-gen-data DOMAIN=modellkatalog` — **avdekte ein ny, separat
   feil** før den lykkast (sjå «Utført» nedanfor).
3. `make roundtrip SCHEMA=...` for alle 6: `roundtrip-json`/`roundtrip-ttl`
   OK.
4. CI-stadfesting (push til main + `gh run list`/`gh run view`) er **ikkje**
   utført som del av denne sesjonen — brukar bør overvake neste
   `generate`-køyring etter push/merge for å stadfeste at `generate /
   modellkatalog` og `publish` lykkast i praksis.

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit | Status |
|---|---|---|---|---|
| 1 | Forslag til Los-tema per skjema | (chat, ingen fil) | — | ✓ |
| 2 | Skriv inn godkjende tema | alle 6 `<org>-modellkatalog.yaml` | Steg 1 godkjent | ✓ |
| 3 | Verifiser lokalt (CI-stadfesting utstår til neste push) | — | Steg 2 | ✓ (delvis — sjå pkt. 4 over) |

## Avhengigheiter

- Uavhengig av MD5 (`specs/done/eksponer-modellelement-maskinhosting.md`) —
  ingen overlapp i felt, men feilen blei oppdaga som ein konsekvens av at
  MD5 sin proof-of-concept-runde avdekte at `generate / modellkatalog`
  allereie var rødt på `main`.
- Krev ikkje `linkml-local`-imaget for sjølve tema-utfyllinga (berre for
  verifiseringssteget).

---

## Utført

Alle 3 tiltak fullførte og verifiserte lokalt (2026-06-21).

1. **23 Los-tema-forslag** lagt fram og godkjent (med 2 korrigeringar til
   «Offentlig forvaltning» — `fint-ressurs`, `ngr-person`).
2. **Alle 23 `tema: - TODO`-plasshaldarar erstatta** med godkjende
   `https://psi.norge.no/los/tema/<namn>`-URI-ar i dei 6
   `<org>-modellkatalog.yaml`-filene (target-baserte regex-erstattingar,
   verifisert at ingen «- TODO» står igjen under `tema:`-felt).
3. **Ny feil oppdaga og fiksa under verifisering** (ikkje del av opphavleg
   plan): `make domain-gen-data DOMAIN=modellkatalog` feila på nytt etter
   tema-fiksen, men med ein **annan** feil:
   ```
   ValueError: https://brreg.no/.../ngr-virksomhet/TilstandType/OPPLØST is not a valid URI or CURIE
   ```
   Rot-årsak: `gen-modelldcat-elements.py` (MD5,
   `specs/done/eksponer-modellelement-maskinhosting.md`) bygger
   `Kodeelement`-id-ar direkte frå enum sine `permissible_values`
   (`{kodeliste_id}/{value}`) utan å translitterere særnorske bokstavar —
   `ngr-virksomhet-schema.yaml` sin `TilstandType`-enum har verdien
   `OPPLØST`, som inneholder `Ø` og dermed ikkje er ein gyldig URI/CURIE for
   `linkml_runtime.utils.metamodelcore`. Dette bryt CLAUDE.md sin
   identifikatorkonvensjon («Særnorske bokstavar skal translittererast i
   alle identifikatorar»). **Fiksa** ved å leggje til
   `transliterate_uri_segment()` i `gen-modelldcat-elements.py` (samme
   æ/ø/å-tabell som CLAUDE.md) og bruke den når `Kodeelement`-id-en byggjast
   — `kode`-feltet (verdien sjølv) er **urørt** (held original
   `OPPLØST`-skrivemåte, berre URI-lokaldelen blir translitterert til
   `OPPLOeST`). Køyrde `gen-modelldcat-elements ORG=brreg` på nytt for å
   regenerere `Kodeelement`-id-ane med fiksen.
4. **Full verifisering etter fiksen:** `make domain-gen-data
   DOMAIN=modellkatalog` køyrer no feilfritt for alle 6 katalogar (genererte
   `.ttl`-filer 272–12642 linjer, alle ikkje-tomme), `make mcp-validate
   POLICY=felles-datakatalog` gjev `errorCount: 0` for alle 6, `make
   roundtrip` gjev `roundtrip-json`/`roundtrip-ttl` OK for alle 6.
5. **Ikkje verifisert i denne sesjonen:** at `generate / modellkatalog`- og
   `publish`-jobbane i `.github/workflows/generate.yml` faktisk lykkast på
   GitHub Actions — dette krev eit push/merge til `main`. Brukar bør
   overvake neste `generate`-køyring (`gh run list --workflow=generate.yml`)
   for å stadfeste.

**Filer endra:** 6× `<org>-modellkatalog.yaml` (tema-felt),
`src/assets/scripts/gen-modelldcat-elements.py` (transliterering av
Kodeelement-id, + regenererte `Kodeelement`-id-ar for brreg).
