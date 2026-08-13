# new-modell: relativ SCHEMA-sti, gyldig eksempelfil og varselfritt utkast (bronze)

## Bakgrunn

Tre problem vart oppdaga ved å køyre `make new-modell NAME=oljefondregisteret
DOMAIN=oreg` etterfølgt av `make mcp-linkml-valider-modell SCHEMA=... POLICY=bronze`:

### Problem 1 — absolutt sti i "Neste steg"

`new-modell.sh` sitt avsluttande "Neste steg"-punkt 4 skriv ut
`$SCHEMA_FILE`, som er absolutt (`$REPO_ROOT/src/linkml/$DOMAIN/$NAME/...`):

```
4. Valider: make mcp-linkml-valider-modell SCHEMA=/mnt/c/dev/github/linkml-datamodellering-no/src/linkml/oreg/oljefondregisteret/oljefondregisteret-schema.yaml POLICY=bronze
```

`mcp-linkml-valider-modell` (`make/40-validation.mk` →
`flatten-and-validate.bash`) forventar derimot ei sti **relativ til
repo-rota** (`SCHEMA` vert brukt direkte som `$REPO_ROOT/$SCHEMA` og til å
utleie `DOMAIN`/`NAME` via `basename`/`dirname`) — ei absolutt sti gir feil
dobbelprefiksing. Kommandoen i "Neste steg" er difor feil slik ho står, og må
rettast manuelt av brukaren før ho fungerer (stadfesta i samtalen: brukaren
måtte sjølv byte til `SCHEMA=src/linkml/oreg/oljefondregisteret/...`).

### Problem 2 — genererte eksempelfila valideringsfeilar mot bronze

Sjølve valideringa feilar med:

```json
{
  "severity": "error",
  "code": "jsonschema validation",
  "target": "OljefondregisteretContainer[0]",
  "message": "Additional properties are not allowed ('OljefondregisteretContainer' was unexpected) in /"
}
```

**Rotårsak:** `new-modell.sh` genererer eksempelfila slik:

```yaml
$CONTAINER_CLASS:
  $CONTAINER_SLOT:
    - id: $SCHEMA_ID/eksempel-1
```

— altså instansdata **pakka inn** under containerklassenamnet som
toppnivå-nøkkel. `mcp-linkml-validator` sin `validate_instance()`
(`src/mcp-linkml-validator/server.py:980`) kallar
`linkml.validator.validate(instance, schema, target_class=<containerklasse>)`
— når `target_class` er sett, skal `instance` **vere** ein instans av den
klassen direkte (attributta til klassen som toppnivånøklar), ikkje pakka inn
under klassenamnet éin gong til.

Stadfesta empirisk ved å samanlikne mot **alle** eksisterande
eksempelfiler i repoet (`ngr-virksomhet`, `fint-administrasjon`,
`modellkatalog/*`, `oreg/enhetsregisteret-bvrinn`, `samt-bu`, m.fl.) — utan
unntak brukar dei containerattributtet direkte som toppnivånøkkel:

```yaml
hovedenheter:      # ← IKKJE "VirksomhetContainer:\n  hovedenheter:"
  - id: ...
```

`new-modell.sh` sin genererte eksempelfil er det einaste tilfellet i repoet
som pakkar inn under containerklassenamnet — og er difor strukturelt feil,
ikkje eit spesialtilfelle som krev spesialhandtering i validatoren.

**Same bug i `new-begrepskatalog.sh`:** identisk mønster
(`BegrepContainer:\n  begrep: []` i staden for `begrep: []`) — sjå
`src/assets/scripts/scaffolding/new-begrepskatalog.sh:122-128`. Same
rotårsak, bør rettast samstundes for konsistens. `new-modellkatalog.sh` har
**ikkje** denne bugen (brukar alt korrekt uinnpakka format,
`modellkataloger:` direkte). `new-begrepssamling.sh` genererer ikkje ei
tilsvarande containerinnpakka eksempelfil (anna filformat, éin fil per
begrep) og er ikkje omfatta.

### Problem 3 — dei to gjenverande åtvaringane skal òg fiksast

**Utvida omfang (brukarønske):** i tillegg til dei to feila over skal
`class_names_pascal_case`- og `all_slots_have_slot_uri`-åtvaringane fiksast i
sjølve genereringa i `new-modell.sh`, slik at ein fersk `make new-modell`
gir eit varsel- og feilfritt utkast (ikkje berre `"valid": true`, men òg
`"warningCount": 0`).

**`class_names_pascal_case`:** stub-klassen får namnet sitt direkte frå
`schemaName` (`new-modell.sh` sender `$SCHEMA_NAME="${NAME//-/_}"`, t.d.
`oljefondregisteret`) via `mcp-linkml-modell-utkast` sin
`_collect_classes()` (`src/mcp-linkml-modell-utkast/converter.py:243`), som
brukar `_sanitize_identifier(schema_name)` **utan** case-endring. Same
konverter har alt ein `_to_pascal_case()`-hjelpefunksjon
(`converter.py:81-87`) som brukast for containerklassenamnet
(`OljefondregisteretContainer`), men **ikkje** for sjølve stub-klassen.

**`all_slots_have_slot_uri`:** `id`-sloten
(`converter.py:446-450`, `identifier: true, range: uriorcurie`) får aldri
`slot_uri`. Verifisert empirisk (grep gjennom heile `src/linkml/`) at
**ingen** av dei ~10 skjemaa i repoet som definerer sin eigen lokale `id`
(`common-ap-no`, `fair-metadata`, `fint-common`, alle NGR-modellane,
`referansemodell-*`) set `slot_uri` på han — dette er altså ein etablert,
gjennomgåande konvensjon i repoet, ikkje eit unntak. Grunnen til at
åtvaringa likevel dukkar opp berre for `new-modell` sitt utkast: dei andre
skjemaa importerer typisk `common-ap-no` og brukar/arvar dette `id`-sloten
derifrå, medan `_check_all_slots_have_slot_uri()`
(`src/mcp-linkml-validator/server.py:201-207`) sjekkar
`schema.slots` — berre **lokalt definerte** slots, ikkje slots arva via
import. Stub-skjemaet frå `new-modell` importerer berre `linkml:types`
(med vilje — domenespesifikke importar er eit TODO-steg brukaren gjer
sjølv), så `id` er lokalt definert der, og vert difor flagga.

**Vedtak (revidert):** legg **ikkje** til `slot_uri` på den lokale
`id`-sloten. Legg i staden til eit import av `common-ap-no` i
`imports:`-lista, versjonslåst via git-tag, og **fjern** den lokalt
genererte `id`-sloten frå `slots:`-seksjonen slik at klassen sin
`slots: [id]`-referanse løyser seg mot `common-ap-no` sitt delte
`id`-slot i staden (som verken er lokalt definert i stub-en, og difor
ikkje vert fanga av `_check_all_slots_have_slot_uri()` sin lokale sjekk).
Dette er den same løysinga andre skjema i repoet alt brukar (arv via
import), berre brukt eitt steg tidlegare i livssyklusen — frå første
utkast, ikkje først når brukaren legg til ein AP-NO-profil sjølv.

Importen skal vere versjonslåst via git-tag, på forma:

```yaml
imports:
- linkml:types
- https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/common-ap-no-v1.0.0/src/linkml/ap-no/common-ap-no/common-ap-no-schema  # TODO: byt til ein reell AP-NO-profil (t.d. dcat-ap-no) etter behov
```

(Stadfesta: git-tagen `common-ap-no-v1.0.0` finst og matchar innhaldet i
`src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml`, versjon
`"1.0.0"`.)

**Merk — avvik frå dokumentert praksis:** `mkdocs/docs/arkitektur/importhierarki.md`
§ «Import på tvers av domenemodellar» seier eksplisitt at
**«AP-NO/FINT/FAIR-skjema følgjer standardar og endrar seg sjeldan — treng
ikkje versjonslåsing»**, og at domenemodellar normalt importerer AP-NO-profilar
via **relativ sti** (`../../ap-no/dcat-ap-no/dcat-ap-no-schema`) —
versjonslåst `raw.githubusercontent.com`-import er der dokumentert som
mønsteret for import **mellom domenemodellar** (t.d. NGR frå SAMT), ikkje
for AP-NO-import. Brukaren har eksplisitt bedt om versjonslåst import for
`common-ap-no` her likevel — truleg fordi eit fersk scaffolda utkast er
tenkt portabelt (kan i prinsippet kopierast ut av repoet, jf. README sitt
punkt om å "bootstrappe eit eksternt repo"), der ei relativ sti ville brote
med det same. Dette er difor eit **medvite unntak**, ikkje ein feil i
gjennomføringa — men verdt å notere tydeleg i koden/kommentaren, sidan det
avvik frå det som elles er dokumentert praksis for AP-NO-import internt i
dette repoet.

### Problem 4 — same `.yaml`-suffiks-bug fleire andre stader i repoet

Etter at `.yaml`-suffiks-funnet (sjå «Ekstra funn undervegs» i `## Utført`
under) vart stadfesta empirisk for `common-ap-no`-importet i `new-modell.sh`,
vart heile repoet kartlagt for same mønster: alle `.sh`/`.py`-script og
alle `.md`-dokument som nemner `raw.githubusercontent.com` saman med eit
`-schema`-namn, for å avgjere kva for førekomstar som faktisk er
**LinkML `imports:`-direktiv** (der SchemaView-oppløysaren legg til `.yaml`
uansett — desse må ALDRI ha `.yaml` i kjeldeteksten) versus **reine
fil-lenkjer** (nedlastingslenkjer til raw-innhald, t.d. i
`finnes_i_format:`/`dct:source`-metadata eller "last ned eksempelfil"-lenkjer
— desse SKAL ha `.yaml`, sidan dei ikkje vert tolka av SchemaView).

**Stadfesta buggy (LinkML-import med feilaktig `.yaml`-suffiks):**

| Fil | Type | Detalj |
|---|---|---|
| `mkdocs/lib/sections/kom_i_gang.sh:41` | **Script** | Genererer «Kom i gang»-seksjonen (§ Importer i eigne LinkML-skjema) for **kvart einaste publiserte skjema** i dokumentasjonsportalen — høgast treffgrad av alle funna, sidan dette vert vist for eksterne brukarar på kvar einaste modell-side |
| `mkdocs/docs/arkitektur/importhierarki.md` | Statisk doc | Alt flagga i `## Utført` over (§ «Import på tvers av domenemodellar», rundt linje 118-124) — ikkje retta då, teke med her for å samle alle funna i éin plan |
| `CONVENTIONS.md:65` | Statisk doc | Dokumenterer eksplisitt URL-mønsteret «brukt i quickstart-eksempel i dokumentasjonsportalen» — altså direkte knytt til `kom_i_gang.sh` sitt (buggy) eksempel, må rettast saman med det |

**Kontrollert og stadfesta korrekte (ingen `.yaml`, ingen endring nødvendig):**

| Fil | Kvifor korrekt |
|---|---|
| `bootstrap.sh:69` | LinkML-import utan `.yaml`-suffiks — alt riktig |
| `mkdocs/docs/arkitektur/ekstern-bruk.md` (tabell + kodeeksempel, linje 60-78) | LinkML-import utan `.yaml` — alt riktig, autoritativ kjelde for ekstern bruk |
| `SCOPE.md:144` | LinkML-import utan `.yaml` — alt riktig |
| `README.md:163` | LinkML-import utan `.yaml` — alt riktig |
| `src/assets/scripts/scaffolding/new-begrepskatalog.sh`, `new-modellkatalog.sh` | Brukar relative importstiar utan `.yaml` (ikkje versjonslåste URL-ar i det heile) — korrekt format |
| `mkdocs/lib/sections/eksempeldatafil.sh:43` | Direkte nedlastingslenkje til `<modell>-eksempel.yaml` (fil-lenkje, ikkje eit LinkML-import) — skal ha `.yaml` |
| `src/assets/scripts/makefile/generate-informasjonsmodell.py` | Byggjer `dct:source`/artefakt-URL-ar for ModelDCAT-metadata (fil-lenkjer, ikkje LinkML-import) — skal ha ekte filetternamn |
| `mkdocs/docs/automasjon/modellmanifest-generering.md:145` (`finnes_i_format:`) | Same som over — metadata-fil-lenkjer, ikkje LinkML-import — skal ha `.yaml` |
| `mkdocs/lib/sections/avhengigheiter.sh` | Parsar eksisterande (alt korrekte) `imports:`-lister frå skjema på disk for å byggje avhengigheitstre — genererer ikkje nye importeksempel |

**Konklusjon:** tre stader treng retting (éin script, to statiske
dokument), alle med same fiks: fjern `.yaml`-suffikset frå den siste
path-komponenten i importURL-en.

## Steg

1. **Rett SCHEMA-sti i "Neste steg"** — legg til `SCHEMA_FILE_REL="src/linkml/$DOMAIN/$NAME/$NAME-schema.yaml"`
   i `new-modell.sh` og bruk han (ikkje `$SCHEMA_FILE`) i validerings-linja
   under "Neste steg".

2. **Rett eksempelfil-generering i `new-modell.sh`** — fjern
   `$CONTAINER_CLASS:`-innpakkingslina, la `$CONTAINER_SLOT:` stå som
   toppnivånøkkel (fjern tilhøyrande innrykk på linene under).

3. **Rett same bug i `new-begrepskatalog.sh`** — same prinsipp: fjern
   `BegrepContainer:`-innpakkinga, la `begrep: []` (og eventuelt dei andre
   containerattributta, dersom fleire vert inkluderte i malen) stå direkte.

4. **Fiks dei to åtvaringane i `new-modell.sh`** — utvid steget som alt
   parsar `$LINKML_YAML` med `python3`/`yaml` (der `CONTAINER_CLASS` og
   `CONTAINER_SLOT` vert henta ut i dag) til òg å **transformere** skjemaet
   før det vert skrive til `$SCHEMA_FILE`, i staden for å skrive
   `$LINKML_YAML` verbatim:
   - Skil ut dei tre header-kommentarlinene (`# Generert av ...`) frå resten
     av `$LINKML_YAML` før parsing (dei går tapt ved `yaml.safe_load`/
     `yaml.dump`-runde), og set dei attende framfor det transformerte
     resultatet.
   - Finn stub-klassen (den ikkje-`tree_root`-klassa — for eit `empty`-utkast
     finst det alltid nøyaktig éi), og endre nøkkelnamnet hennar til
     PascalCase (same logikk som `_to_pascal_case()` i
     `mcp-linkml-modell-utkast/converter.py:81-87`:
     `"".join(p.capitalize() for p in name.replace("_","-").split("-") if p)`).
   - Oppdater containerklassen sitt attributt (`range: <gamalt namn>`) til
     å peike på det nye, PascalCase-namnet.
   - **Fjern** `id`-oppføringa frå den dumpa `slots:`-seksjonen i dict-et
     (behald `- id` i klassen sin `slots:`-liste — han løyser seg no mot
     det importerte `common-ap-no`-slotet i staden). Dersom `slots:` vert
     tom etter fjerninga, fjern heile `slots:`-nøkkelen frå dict-et (unngå
     å dumpe eit tomt `slots: {}`).
   - Etter `yaml.dump()`: gjer ei målretta tekst-erstatning av lina
     `- linkml:types` (den einaste importlina på dette tidspunktet) med dei
     to linene:
     ```yaml
     - linkml:types
     - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/common-ap-no-v1.0.0/src/linkml/ap-no/common-ap-no/common-ap-no-schema  # TODO: byt til ein reell AP-NO-profil (t.d. dcat-ap-no) etter behov
     ```
     (Kommentaren på import-lina kan ikkje uttrykkjast via `yaml.dump()`
     med standard PyYAML — difor tekstbasert etter dumping, ikkje via
     dict-et, same tilnærming som header-handteringa over.)
   - Fjern/juster den eksisterande TODO-footer-lina "Legg til
     domene-spesifikke imports etter 'linkml:types'" i `new-modell.sh`
     sidan importet no alt er lagt til automatisk med eiga inline
     TODO-forklaring — footeren skal ikkje lenger instruere brukaren til å
     gjere noko som alt er gjort. Behald dei tre andre TODO-punkta.
     Kommentaren "Gi stub-klassen eit meiningsfult norsk namn (PascalCase)"
     kan forenklast til berre "eit meiningsfult norsk namn" — casing er alt
     korrekt, men namnet er framleis generisk og bør framleis vurderast av
     brukaren.
   - Skriv det transformerte skjemaet (header + omdumpa/tekst-justert YAML)
     til `$SCHEMA_FILE` i staden for det rå `$LINKML_YAML`.
   - `CONTAINER_CLASS`/`CONTAINER_SLOT` som alt vert brukt til å byggje
     eksempelfila, må hentast frå det **transformerte** skjemaet (det nye
     PascalCase-namnet), ikkje det opphavlege.

5. **Regenerer og verifiser** — køyr `make new-modell NAME=<test> DOMAIN=oreg`
   på nytt, deretter
   `make mcp-linkml-valider-modell SCHEMA=src/linkml/oreg/<test>/<test>-schema.yaml POLICY=bronze`.
   Forventa resultat: `"valid": true`, `"errorCount": 0`, `"warningCount": 0`.

6. **Oppdater dokumentasjon** — `mkdocs/docs/kom-i-gang/ny-domenemodell.md`
   § «`examples/tilskudd-eksempel.yaml`» (rundt linje 133-142) og
   tilhøyrande skjema-eksempel (rundt linje 50-115) viser i dag det
   feilaktige innpakka eksempelformatet, lågbokstav-klassenamn, `imports: [linkml:types]`
   utan `common-ap-no`, og `id` utan tilhøyrande import — må oppdaterast til
   å matche den retta genereringa:
   - Skjema-eksempelet skal vise PascalCase-klassenamn (`Tilskudd`, ikkje
     `tilskudd`), det nye to-lineimportet (`linkml:types` +
     versjonslåst `common-ap-no`-URL med inline TODO-kommentar), og at
     `slots:`-seksjonen ikkje lenger inneheld ei lokal `id`-oppføring.
   - TODO-tabellen: fjern rada om å gi stub-klassen PascalCase-namn (casing
     er alt korrekt — behald berre poenget om eit meir *meiningsfullt*
     namn), og oppdater importrada til å forklare det nye
     `common-ap-no`-importet og TODO-kommentaren som følgjer med.

7. **Rydd opp testartefaktar** — fjern alle midlertidige testmodellar
   oppretta under steg 5, og revert `.github/valid-scopes.txt` til rett
   tilstand via `make update-valid-scopes`.

8. **Rett `mkdocs/lib/sections/kom_i_gang.sh:41`** — fjern `.yaml` frå
   slutten av importlina:
   ```bash
   echo "  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/$version_path/src/linkml/$domain/$schema/$schema-schema"
   ```
   Verifiser med `make docs-build` (eller tilsvarande lokal generering) at
   § «Kom i gang» på minst éin modell-side viser importlina utan `.yaml`.

9. **Rett `CONVENTIONS.md:65`** — fjern `.yaml` frå eksempel-URL-en i
   § «Bruksområde» (Versjonerte GitHub raw-URL-ar), slik at han igjen
   samsvarar med det `kom_i_gang.sh` faktisk genererer etter steg 8.

10. **Rett `mkdocs/docs/arkitektur/importhierarki.md`** — fjern `.yaml`
    frå eksempel-URL-en i § «Import på tvers av domenemodellar»
    (linje ~124, `ngr-adresse-schema.yaml` → `ngr-adresse-schema`).

## Handlingsliste

**Runde 1** (Problem 1-3, punkt 1-7 utført og opphavleg arkivert i
`specs/done/` — spec reopna for runde 2 nedanfor, difor er "flytt til
`specs/done/`" no punkt 11 i staden for det opphavlege punkt 8, sjå
`## Utført` for det historiske forløpet).
**Runde 2** (Problem 4, punkt 8-11): utført.

- [x] 1: `new-modell.sh` — relativ `SCHEMA_FILE_REL` i "Neste steg"-meldinga
- [x] 2: `new-modell.sh` — fjern containerklasse-innpakking i eksempelfil-heredoc
- [x] 3: `new-begrepskatalog.sh` — same retting av eksempelfil-heredoc
- [x] 4: `new-modell.sh` — PascalCase-namngjeving av stub-klasse + versjonslåst `common-ap-no`-import (fjern lokal `id`-slot, footer-TODO justert)
- [x] 5: Regenerer testmodell + verifiser `"valid": true`, `"warningCount": 0` mot bronze-policy
- [x] 6: Oppdater `mkdocs/docs/kom-i-gang/ny-domenemodell.md` sitt eksempeloppsett og TODO-tabell
- [x] 7: Rydd opp testartefaktar, `make update-valid-scopes`
- [x] 8: `mkdocs/lib/sections/kom_i_gang.sh` — fjern `.yaml` frå quickstart-importlina
- [x] 9: `CONVENTIONS.md` — fjern `.yaml` frå eksempel-URL i § «Bruksområde»
- [x] 10: `mkdocs/docs/arkitektur/importhierarki.md` — fjern `.yaml` frå eksempel-URL i § «Import på tvers av domenemodellar»
- [x] 11: Flytt spec til `specs/done/` med oppdatert `## Utført`-seksjon

## Utført

**1: Relativ SCHEMA-sti.** Lagt til `SCHEMA_FILE_REL="src/linkml/$DOMAIN/$NAME/$NAME-schema.yaml"`
i `new-modell.sh`, brukt i "Neste steg"-punkt 4 i staden for `$SCHEMA_FILE`.
Punkt 2 sin tekst justert til å reflektere det nye automatiske
`common-ap-no`-importet (sjå punkt 4).

**2: Uinnpakka eksempelfil.** `$CONTAINER_CLASS:`-innpakkingslina fjerna frå
`EXAMPLE_FILE`-heredocen; `$CONTAINER_SLOT:` står no direkte som
toppnivånøkkel, i tråd med alle andre eksempelfiler i repoet.

**3: Same retting i `new-begrepskatalog.sh`.** `BegrepContainer:`-innpakkinga
fjerna, `begrep: []` står no direkte.

**4: PascalCase + versjonslåst `common-ap-no`-import.** Steget som hentar ut
`CONTAINER_CLASS`/`CONTAINER_SLOT` er utvida til éin samla python3-transformasjon
som: skil ut og bevarer dei tre header-kommentarlinene, omdøyper stub-klassen
til PascalCase (og oppdaterer containerklassen sin `range`-referanse
tilsvarande), fjernar den lokale `id`-slot-oppføringa (og heile `slots:`-nøkkelen
dersom han vert tom), og set inn eit versjonslåst `common-ap-no`-import med
inline TODO-kommentar via målretta tekst-erstatning etter `yaml.dump()`.
Footer-TODO-blokka er redusert frå fire til to linjer (import- og
PascalCase-punkta er no overflødige, sidan begge er løyst automatisk).

**Ekstra funn undervegs — dobbel `.yaml`-ending:** første testkøyring feila
med `HTTP Error 404: .../common-ap-no-schema.yaml.yaml` — LinkML sin
importoppløysar legg alltid til `.yaml` på importstrengen, uavhengig av om
strengen alt endar på `.yaml`. Retta ved å fjerne den eksplisitte
`.yaml`-suffiksen frå importURL-en i `new-modell.sh` (importet skal altså
enda på `.../common-ap-no-schema`, **ikkje** `.../common-ap-no-schema.yaml`).
**Merk:** `mkdocs/docs/arkitektur/importhierarki.md` sitt eksisterande
dokumenterte eksempel på versjonslåst import (§ «Import på tvers av
domenemodellar») har same `.yaml`-suffiks-feil og ville gitt identisk 404 om
nokon kopierte det direkte — dette vart oppdaga i denne økta, men er **ikkje**
retta her (utanfor opphavleg spec-omfang, som gjaldt `new-modell.sh`). Bør
rettast i eiga oppfølging.

**5: Verifisering.** Regenererte ein fersk testmodell (`oreg/verifiseringstest`)
frå bunnen av med den ferdig retta `new-modell.sh`. Resultat frå
`make mcp-linkml-valider-modell SCHEMA=src/linkml/oreg/verifiseringstest/verifiseringstest-schema.yaml POLICY=bronze`:
```json
{"valid": true, "errorCount": 0, "warningCount": 0, "issues": []}
```
`make lint` køyrd som tilleggssjekk — einaste utslaget er
`canonical_prefixes`-åtvaringa for `dct`-prefikset, som er identisk og
pre-eksisterande i `common-ap-no-schema.yaml` sjølv (ikkje ein regresjon;
`dct:` er repoet sin bevisste standardprefiks per `CONVENTIONS.md`, ikkje
noko denne spec-en skal endre).

**6: Dokumentasjon.** `mkdocs/docs/kom-i-gang/ny-domenemodell.md` sitt
`tilskudd-schema.yaml`-eksempel oppdatert: PascalCase-klassenamn
(`Tilskudd`, `TilskuddContainer` først i fila), to-line import
(`linkml:types` + versjonslåst `common-ap-no`-URL med TODO-kommentar), ingen
lokal `id`-slot (med forklarande setning om at han vert arva). TODO-tabellen
oppdatert: PascalCase-rada fjerna (erstatta med eit poeng om eit meir
meiningsfullt namn), importrada omskriven til å forklare
`common-ap-no`-bytet. Eksempelfil-seksjonen (`tilskudd-eksempel.yaml`)
oppdatert til uinnpakka format.

**7: Opprydding.** `src/linkml/oreg/verifiseringstest/` sletta,
`make update-valid-scopes` køyrd (37 scopes — nettoendring null for
testmodellen). Under oppdateringa vart det synleg at to urelaterte forhold
alt fanst i arbeidstreet før denne økta starta (ikkje forårsaka av arbeidet
i denne spec-en):
- `src/linkml/oreg/spikerregisteret/` (committa i `48a985b6`) manglar no frå
  filsystemet — vises som ei ikkje-stega sletting i `git status`. Årsak
  ukjend; ikkje noko denne økta har gjort. Bør undersøkjast av brukaren.
- `src/linkml/oreg/oljefondregisteret/` (brukaren sin eigen manuelle
  testmodell frå tidlegare i samtalen, aldri committa) ligg framleis att på
  disk med det **gamle** (før-fiks) skjemaformatet, og vart difor teke med
  i den regenererte `valid-scopes.txt`. Modellen vil framleis feile bronze-
  validering slik han står — anten regenerer på nytt med `make new-modell`
  eller slett katalogen manuelt.

**8: Flytting (runde 1).** Fila vart flytta til `specs/done/` etter runde 1.
Reopna til `specs/backlog/` etter kartlegginga i Problem 4, sidan nytt,
uutført omfang vart lagt til.

---

**Runde 2 (Problem 4) — Utført:**

**8: `mkdocs/lib/sections/kom_i_gang.sh`.** Fjerna `.yaml` frå slutten av
importlina i `generate_quickstart()` (linje 41). Verifisert isolert ved å
`source`-e fila og kalle `generate_quickstart "ap-no" "dcat-ap-no"` direkte
— output viser no `.../dcat-ap-no-schema` utan `.yaml`-suffiks.

**9: `CONVENTIONS.md`.** Fjerna `.yaml` frå eksempel-URL-en i § «Bruksområde»
(linje 65), slik at han igjen samsvarar med det `kom_i_gang.sh` faktisk
genererer.

**10: `mkdocs/docs/arkitektur/importhierarki.md`.** Fjerna `.yaml` frå
`ngr-adresse-schema.yaml` → `ngr-adresse-schema` i eksempelet under
§ «Import på tvers av domenemodellar».

**11: Flytting (runde 2).** Denne fila vert flytta til `specs/done/` på
nytt som siste steg.
