# Full gjennomgang: alvorsgrad-koherens og overlapp i validator-policyane

## Bakgrunn

Brukaren har bede om ein full gjennomgang av alle valideringsreglane i
`src/mcp-linkml-validator/policies/README.md`, med fire konkrete mål:

1. Vurder om det finst overlappande policyar, eller policyar/reglar som ikkje
   lenger er naudsynte.
2. Vurder alvorsgrada til kvar regel opp mot bronse/sølv/gull, med mål om
   mest mogleg **logisk samanheng** mellom regel og nivå.
3. Sørg for at bronse-/sølv-/gull-tabellane **tydeleg** viser i kva tilfelle
   ein regel vert oppgradert frå `warning` til `error`.
4. Skriv funn og forslag til `specs/` — **ikkje** stogg for avklaringar
   undervegs.

Gjennomgangen er basert på full lesing av `bronze.yaml`, `silver.yaml`,
`gold.yaml`, `felles-datakatalog.yaml`, `felles-begrepskatalog.yaml`,
`server.py` (sjekk-registeret og `_merge_policies`) og heile
`policies/README.md`.

## Korleis oppgradering fungerer i dag (for kontekst)

`_merge_policies(parent, child)` i `server.py` slår saman `checks`-dictar
med `{**parent, **child}` — ein child-policy (t.d. `gold`) **overstyrer**
ein foreldre-sjekk (t.d. frå `bronze`) berre dersom han **eksplisitt
redeklarerer same nøkkelnavn**. Ein bronse-åtvaring som ikkje vert
redeklarert i `gold.yaml`, forblir difor stille verande som `warning` på
gullnivå — sjølv om `gold.yaml` sin eigen kommentar seier «Alle brot gir
feil». Dette er sjølve mekanismen bak funn A1 under.

## Konklusjon: ingen policyar bør fjernast

Dei fem policyane dekkjer fem ikkje-overlappande føremål og bør **alle
behaldast**:

| Policy | Føremål | Overlappar med? |
|---|---|---|
| `bronze` | Generisk LinkML-modelleringskvalitet, domeneuavhengig | — (grunnlaget for dei andre) |
| `silver` | Bronse + DCAT-AP-NO/DQV-AP-NO-domenekonformitet | Ingen — eige spesifikasjonsomfang |
| `gold` | Sølv + full FAIR-interoperabilitet, alle brot er `error` | Ingen — reint strenghetsnivå over sølv |
| `felles-datakatalog` | Bronse + ModelDCAT-AP-NO for modellkatalogpublisering | Ingen — heilt anna klassesett (Modellkatalog/Informasjonsmodell) enn silver/gold sitt (Katalog/Datasett) |
| `felles-begrepskatalog` | Bronse + SKOS-AP-NO-Begrep for begrepskatalogpublisering | Ingen — heilt anna klassesett (Begrep/Samling) |

`felles-datakatalog`/`felles-begrepskatalog` arvar **berre** `bronze`, ikkje
`silver`/`gold` — eit medvite og fornuftig val (eit skjema som publiserer
til Felles Datakatalog treng ikkje samstundes vere DCAT-AP-NO-konformt),
men det er **ikkje eksplisitt forklart** nokon stad i README kvifor dette
er rett arvekjede. Sjå forslag i «Steg» under.

Det finst derimot **fire konkrete, verifiserte problem** i korleis
enkeltreglar heng saman på tvers av nivåa — presentert som Funn A-C under.

## Funn A — Brot på «alle bronse-/sølv-åtvaringar skal bli feil på gull»

### A1: `no_inlined_on_primitive_range` vert aldri oppgradert til `error`

`bronze.yaml` sin `no_inlined_on_primitive_range`-sjekk (Digdir-regel 8,
FAIR I1) er `severity: warning`. Han finst **ikkje** i `gold.yaml` sin
`checks:`-blokk, og er difor framleis `warning` på gullnivå — i strid med
`gold.yaml` sin eigen kommentar («Alle brot gir feil — gullstatus er
krevjande å oppnå») og innleiingssetninga i README sin gull-tabell («Alle
brot gir `error` — også dei som er åtvarslane på bronse»). README sin
gull-tabell (§ gold) listar heller ikkje denne regelen i det heile — han
er usynleg der, ikkje berre uoppgradert, sidan tabellen berre viser
sjekkar som faktisk finst i `gold.yaml`. Dette er den einaste bronse-
åtvaringa dette gjeld for; alle andre 10 bronse-åtvaringar (inkl. dei to
eg la til i førre økt: `schema_har_erdiagram_aktivert`,
`local_types_have_standard_uri`) er korrekt redeklarerte som `error` i
`gold.yaml`.

**Tilråding:** legg til `no_inlined_on_primitive_range` i `gold.yaml` med
`severity: error`, same mønster som dei andre bronse-oppgraderingane.

### A2: Digdir-regel-dekningstabellen i README manglar regel 6 for sølv/gull

`## Nivå for skjemakvalitet`-tabellen (README, rundt line 59-61) listar
Digdir-reglar for kvart nivå:

```
bronze: 1, 2, 3, 4, 5, 6, 7, 8, 13, 15
silver: 1-5, 7-11, 13-15        ← hoppar over 6
gold:   1-5, 7-11, 13-15        ← hoppar over 6
```

Sidan `silver`/`gold` **arvar** heile `bronze` (inkl. `class_count_limit`,
regel 6 — Modularitet, som er dokumentert eksplisitt i sjølve gull-tabellen
lenger nede, line 181: «Skjema har ikkje fleire enn 50 klasser … [6 —
Modularitet] … arva frå bronse, oppgradert til error»), er
sølv-/gull-radene i denne oppsummeringstabellen **feil** — dei to tabellane
i same fil motseier kvarandre. Korrekt rekkjevidde for begge er
`1-11, 13-15` (unionen av bronse sine reglar og sølv sine eigne nye
reglar 9, 10, 11, 14).

**Tilråding:** rett `silver`- og `gold`-radene i nivå-tabellen til
`1-11, 13-15`.

## Funn B — Overlappande/redundante sjekkar

### B1: `f2_title` (gold `fair_checks`) duplikat av bronse sitt `required: schema: [title]`

`bronze.yaml` sin `required: schema: [id, name, title]` gjer
`schema.title` obligatorisk (`error`) alt på bronsenivå, via den generiske
`_check()`-mekanismen i `validate_schema()` (kode
`missing_required_metadata`, target `schema:<navn>`). Dette vert arva
uendra av `silver` og `gold`. `gold.yaml` sin `fair_checks.f2_title`
(`check: schema_field_present, field: title`) sjekkar **nøyaktig det same
vilkåret** (er `schema.title` sett), men via ein heilt annan kodeveg
(`_check_schema_field_present`, kode `fair_f2`, target `schema`). Eit
skjema som manglar `title` på gullnivå vil difor få **to separate issues**
for éin og same defekt — ein reell duplikat-rapportering, ikkje berre eit
dokumentasjonsproblem.

Gull sin eigen kommentar (line 299-301) stadfestar at akkurat dette
mønsteret **alt er kjent og løyst éin gong før**: «F1
(schema_id_is_http_uri), F3 (all_classes_have_class_uri) og I1
(all_slots_have_slot_uri) er flytta til bronze.yaml og arva herifrå. Dei er
oppgradert til error via checks-blokka ovanfor» — altså vart tre
tilsvarande duplikatar rydda vekk ved eit tidlegare høve, men `f2_title`
(og `f4_version`, sjå B2) vart ikkje fanga opp av same opprydding.

**Tilråding:** fjern `f2_title` frå `gold.yaml` sin `fair_checks:` — kravet
er alt `error` via arva `required:`-liste frå bronse. Legg til éin
kommentarlinje i `fair_checks:`-blokka som listar `f2_title` saman med dei
tre allereie nemnde (F1/F3/I1) som «flytta til bronze.yaml».

### B2: `f4_version` (gold `fair_checks`) duplikat av bronse sitt `recommended: schema: [version]`, med motstridande alvorsgrad

Same mønster som B1, men verre: `bronze.yaml` sin `recommended: schema:
[description, version]` gjer `schema.version` **anbefalt** (`warning`,
kode `missing_recommended_metadata`) — denne lista vert **ikkje**
oppgradert nokon stad (verken silver eller gold sine eigne
`recommended:`-lister inneheld `version` eksplisitt, og
`_merge_policies` sin `required`/`recommended`-samanslåing har ingen
«oppgrader recommended til required»-mekanisme — han slår berre saman
listene, aldri flyttar eit felt mellom dei to listene). Samstundes krev
`gold.yaml` sin `fair_checks.f4_version` det same feltet som **obligatorisk**
(`error`, kode `fair_f4`). Resultatet: eit skjema utan `version` på
gullnivå får **både** ein `warning` (frå den arva `recommended`-lista) og
ein `error` (frå `f4_version`) for same defekt — eit forvirrande
dobbeltsignal med ulik alvorsgrad for identisk vilkår.

**Tilråding:** flytt `version` frå bronse sin `recommended:`-liste til
`required:`-lista **på gullnivå** (legg `version` eksplisitt til i
`gold.yaml` sin eigen `required: schema:`-liste), og fjern `f4_version` frå
`fair_checks:`. Merk: sidan `_merge_policies` slår saman `required`/
`recommended` per nivå (ikkje flyttar felt mellom dei), vil `version`
framleis stå i BÅDE `required` og `recommended` etter samanslåing dersom
han berre vert lagt til i `required` på gullnivå — dette er harmlaust
(eit felt som er til stades tilfredsstiller begge sjekkane samstundes,
og eit felt som manglar vil då berre gje éin `error`, ikkje éin `error` +
éin `warning`, sidan... **NB:** dette krev verifisering — sjå «Opne
vurderingar» punkt 3 under, då dette er den einaste tilrådinga i denne
specen som ikkje er full verifisert mot faktisk kode-åtferd.

### B3: `r12_provenance` (gold) er i praksis eit no-op for AP-NO-konforme skjema

`gold.yaml` sin `fair_checks.r12_provenance` krev at skjemaet har **éin
eller annan** slot med URI blant `prov:wasAttributedTo`,
`prov:wasGeneratedBy`, `dct:creator`, `dct:publisher` eller
`dct:contributor` (via `schema_has_slot_with_uri`, som søkjer **på tvers av
heile skjemaet**, ikkje ei bestemt klasse). Eit kvart skjema som alt
tilfredsstiller `silver` sine obligatoriske krav om `dct:publisher` på
`Katalog`, `Datasett` **og** `Datatjeneste` (tre separate `error`-sjekkar,
alle inherited av gull) vil **automatisk** tilfredsstille `r12_provenance`
òg, sidan dei same `dct:publisher`-slotane tel. Sjekken har difor **null
marginal verdi** for eit AP-NO-konformt skjema — han fangar berre opp
skjema som held gull-nivå elles, men **ikkje** følgjer AP-NO-domenemønsteret
i det heile (ingen Katalog/Datasett/Datatjeneste-klassar), noko som er eit
smalt og uklart scope for kva regelen faktisk skal beskytte mot.

**Tilråding:** ikkje eit hastefunn å fjerne, men verdt å presisere i
skildringa at regelen berre er meiningsfull for skjema **utanfor**
AP-NO-domenemønsteret (sidan silver/gold sine klassespesifikke
`dct:publisher`-krav alt dekkjer AP-NO-tilfellet). Alternativt: fjern
`dct:publisher` frå `match_any_uri`-lista i `r12_provenance` for å tvinge
fram eit **anna** proveniens-signal (prov:*/dct:creator/dct:contributor)
utover det AP-NO-kravet alt sikrar — men dette ville skjerpe kravet for
alle domenemodellar, ikkje berre AP-NO-modellar, og bør difor helst
avklarast med brukaren før det vert gjort (sjå «Opne vurderingar»).

### B4: Tre ulike «lisens»-sjekkar med potensielt forvirrande namnelikskap

- `schema_has_license` (bronze/gold): er `schema.license`-**feltet** sett
  (skjemaet sjølv er lisensiert)?
- `r11_license` (gold `fair_checks`): finst det **ein slot** i modellen
  med URI `dct:license` **kvar som helst** (kan modellerte instansar
  uttrykkje lisensinformasjon)?
- `distribusjon_lisens` (silver/gold): har klassen `Distribusjon`
  spesifikt ein slot med `dct:license`?

Desse tre sjekkar reelt ulike ting (skjema-artefaktets eigen lisens vs.
generell modellert lisens-eigenskap vs. distribusjon-spesifikk
lisens-eigenskap) og er **ikkje redundante** i streng forstand — men eit
skjema som består `distribusjon_lisens` vil **alltid** automatisk bestå
`r11_license` òg (same logikk som B3: ein spesifikk klassesjekk
impliserer ein generell skjema-breie sjekk av same URI). Dette er ikkje
eit funksjonelt problem, men eit **namngjevings-/dokumentasjonsproblem**:
tre sjekkar med «lisens» i skildringa kan lett mistolkast som duplikat ved
første augekast.

**Tilråding:** legg til éi kort forklarande linje i README under gull-
tabellen som skil dei tre frå kvarandre eksplisitt (sjå forslag til
tabellstruktur under).

### B5: To parallelle mekanismar for feltnærvær-sjekk — kartlegging og evaluering av refaktorering

**Oppdatert etter brukarønske om djupare kartlegging** («eg ønsker i
utgangspunktet å gjennomføre denne refaktoreringa … men vi må kartlegge
det godt først»). Denne seksjonen er utvida med (1) stadfesting av at
duplikat-problemet **alt oppstår i produksjon i dag** (ikkje berre eit
hypotetisk B1/B2-scenario), (2) den arkitektoniske rotårsaka til kvifor
to mekanismar finst, (3) eit tredje, tilstøytande funn kartlegginga
avdekte, og (4) to konkrete refaktoreringsalternativ med omfang og risiko
for kvart.

#### B5.1 — Duplikatet er reprodusert live, uavhengig av B1/B2

Repoet har to uavhengige måtar å uttrykkje «dette feltet skal/bør vere
til stades» på:

1. Den generiske `required:`/`recommended:`-lista i kvar policy — handtert
   av ein anonym closure i `validate_schema()` (`server.py`, funksjonen
   `_check()` definert lokalt rundt line 896), kodane
   `missing_required_metadata` (alltid `error`)/
   `missing_recommended_metadata` (alltid `warning`). Gjeld tre scope:
   `schema`, `class`, `slot`.
2. Eksplisitte `checks:`-oppføringar med `check: schema_field_present`
   (brukt for `default_prefix`, `license`) — handtert av
   `_check_schema_field_present`, kode `_fair_code(config)`. Gjeld berre
   `schema`-scope (funksjonen tek imot `schema`, ikkje klasser/slots).

Desse er **ikkje** berre eit teoretisk duplikat-risiko (som i B1/B2) —
problemet er verifisert å oppstå **i dag**, i produksjonskoden, heilt
uavhengig av gold.yaml sine `fair_checks`. `felles-datakatalog.yaml` og
`felles-begrepskatalog.yaml` har begge sin eigen
`recommended: schema: [description, title, version]`, medan `title` alt
er `required` via arva `bronze.yaml`-liste (dei to policyane arvar
`bronze` direkte). Kryssøyrt mot ein reell valideringskøyring (verifisert
i denne gjennomgangen, sjå kommando under) gjev eit skjema som manglar
`title` under `felles-datakatalog`-policyen **begge** desse issues
samstundes:

```json
{"severity": "error",   "code": "missing_required_metadata",   "message": "Manglar obligatorisk metadata: title"}
{"severity": "warning", "code": "missing_recommended_metadata","message": "Manglar anbefalt metadata: title"}
```

Verifisert med:
```bash
podman run --rm -v "$(pwd):/work:ro" mcp-linkml-validator python3 -c "
import sys; sys.path.insert(0, '/work/src/mcp-linkml-validator')
from server import validate_schema
print(validate_schema('id: https://example.org/schema\nname: T\ndescription: D\nprefixes: {ex: https://example.org/}\ndefault_prefix: ex\n', 'felles-datakatalog'))"
```
— gjev nøyaktig dei to `title`-issues over, i tillegg til andre forventa
funn. Same mønster gjeld for `felles-begrepskatalog.yaml` (identisk
`required`/`recommended`-oppsett).

#### B5.2 — Kvifor to mekanismar finst: ein reell arkitektonisk grunn, ikkje berre historisk tilfelle

`_merge_policies()` slår saman `required`/`recommended`-listene med
`list(dict.fromkeys(parent_liste + child_liste))` — ei **union**, aldri
ei overstyring. Konsekvensen er at denne mekanismen **strukturelt ikkje
kan uttrykkje alvorsgrad-progresjon** for eitt felt (t.d. «warning på
bronse, error på gull») utan at det gamle warning-utfallet held fram å
fyre parallelt med det nye error-utfallet, sidan feltet då må stå i
**begge** listene samstundes ein eller annan stad i arvekjeda. Det finst
ingen «flytt frå recommended til required på nivå X»-operasjon i
merge-logikken.

`checks:`-dictmekanismen (`{**parent_checks, **child_checks}`, nøkla på
sjekknavn) har derimot **nettopp** denne evna innebygd — det er slik heile
bronse→sølv→gull-stigen for alle andre ~30 sjekkar allereie fungerer
(same nøkkelnavn, overstyrt `severity:` per nivå, jf. `schema_has_license`
som går warning→error). Dette er truleg **den eksakte grunnen** til at
`schema_field_present` vart innført som eigen sjekktype for
`default_prefix`/`license` i staden for å leggje dei i
`required`/`recommended`-listene: dei to felta treng
nivå-progresjon (`license` er warning på bronse/sølv, error på gull), noko
listemekanismen ikkje kan uttrykkje. `id`/`name`/`title` (alltid `error`,
aldri progresjon) og `description` (alltid `warning`, aldri progresjon —
sjølv på gull) fekk derimot aldri behov for denne evna, og vart difor
verande i den enklare, eldre listemekanismen. **Konklusjon: dei to
mekanismane er ikkje reint tilfeldig historisk duplisert arbeid — den eine
(`checks:`) er strengt meir uttrykksfull enn den andre
(`required`/`recommended`), og den mindre uttrykksfulle mekanismen er
nøyaktig der duplikat-risikoen (B1/B2/B5.1) oppstår, kvar gong nokon
prøver å simulere progresjon med han ved å leggje same felt i begge
lister på ulike nivå.**

#### B5.3 — Tilstøytande funn frå kartlegginga: `tree_root`-unntaket er inkonsekvent

Dei fleste klasse-sjekkane (`all_classes_have_identifier`,
`all_classes_have_class_uri`, `all_classes_have_concept_ref`) hoppar
eksplisitt over `tree_root`-klassen (containerklassen). Den generiske
`required`/`recommended`-closuren gjer **ikkje** det — han køyrer
uendra over `schema.classes` utan filter. Verifisert: eit `bronze`-skjema
med `recommended: class: [description]` (arva frå bronse) gjev
`missing_recommended_metadata`-åtvaring for **containerklassen** dersom
han manglar `description`, medan containeren er eksplisitt friteken for
identifikator-/class_uri-/begrepsidentifikator-krava. Dette er ikkje
naudsynt feil (containerar treng kanskje ikkje skildring, men det er
uklart om fritakinga er tilsikta), men er ein **inkonsekvens ein
konsolidering må ta eit medvite val om** — anten (a) halde fram med at
containeren IKKJE er friteken frå felt-nærvær-krav (noverande åtferd,
ingen endring naudsynt), eller (b) leggje til same `tree_root`-filter i
den nye, samla mekanismen for konsistens med resten av klasse-sjekkane.

#### B5.4 — To refaktoreringsalternativ

**Alternativ 1 — Minimal, låg-risiko patch (kan gjerast no, uavhengig av
Alternativ 2):** i `_check()`-closuren, hopp over eit `recommended`-felt
som alt finst i `required_fields`-lista for same scope:

```python
def _check(obj, obj_label, required_fields, recommended_fields):
    for field in required_fields:
        if not getattr(obj, field, None):
            issues.append(issue("error", "missing_required_metadata", obj_label, ...))
    for field in recommended_fields:
        if field in required_fields:
            continue  # alt handtert som obligatorisk — unngå dobbeltsignal
        if not getattr(obj, field, None):
            issues.append(issue("warning", "missing_recommended_metadata", obj_label, ...))
```

Fjernar B5.1-duplikatet **umiddelbart**, med éin lokal kodeendring og
ingen YAML-endringar. Løyser **ikkje** den strukturelle progresjons-
avgrensinga i B5.2 (framleis uråd å seie «warning på bronse, error på
gull» for eit `required`/`recommended`-felt), men fjernar den einaste
kjende, verifiserte skadeverknaden av avgrensinga.

**Alternativ 2 — Full konsolidering til éin mekanisme (det brukaren
opphavleg spurde om):** fjern `required:`/`recommended:` som eigne
policy-nøklar, og uttrykk alle felt-nærvær-krav (`id`, `name`, `title`,
`description`, `version`, `default_prefix`, `license`) som vanlege
`checks:`-oppføringar. Krev:

- **Ny/generalisert sjekk-type i `server.py`:** `_check_schema_field_present`
  handterer i dag berre `schema`-scope. Treng anten (a) to nye
  sjekktypar `class_field_present`/`slot_field_present` som itererer
  `schema.classes`/`schema.slots` (same mønster som `_check()` gjer i
  dag), eller (b) éin generalisert `_check_field_present(sv, schema,
  config, issues)` parametrisert med `config["scope"]` ∈
  {schema, class, slot} — sistnemnde er mest i tråd med DRY-prinsippet i
  CLAUDE.md (éi kjelde for logikken, ikkje to nesten-like funksjonar).
- **Fjern `_check()`-closuren og dei tre kalla til han** i
  `validate_schema()` (schema/class/slot), og fjern
  `policy.get("required"/"recommended")`-oppslaga.
- **Migrer alle 5 policy-YAML-filene:** kvar `required`/`recommended`-
  oppføring vert til ei `checks:`-oppføring. Konkret omfang (talt frå
  dagens filer):
  - `bronze.yaml`: 3 required (id, name, title) + 4 recommended
    (description×3 scope, version) = 7 nye `checks:`-oppføringar.
  - `silver.yaml`, `gold.yaml`, `felles-datakatalog.yaml`,
    `felles-begrepskatalog.yaml`: kvar sine `required`/`recommended`-
    lister er i dag reint **redundante delmengder** av det som alt er
    arva frå bronse (ingen nye felt) — dei kan **fjernast heilt** frå
    desse fire filene ved konsolidering, ikkje migrerast, sidan felta dei
    listar (`id`, `name`, `description`, `title`, `version`) alt får
    `checks:`-oppføringar frå bronse-nivået og vert arva som normalt via
    `{**parent, **child}`.
  - **Untak:** `felles-datakatalog.yaml`/`felles-begrepskatalog.yaml` sin
    eigen `recommended: [title, version]` er i dag den **einaste kjelda**
    til B5.1-duplikatet (title er alt required via bronse) — desse to
    linjene fjernast heilt ved konsolidering, ikkje migrerast, nett fordi
    dei var feilen.
- **Testpåverknad — verifisert, lite omfang:** berre 2 stader i
  `tests/test_mcp_policies.py` assertar direkte på kodane
  `missing_required_metadata`/`missing_recommended_metadata` (line 295,
  305). Desse må oppdaterast til å forvente den nye
  `checks:`-genererte koden i staden (t.d. `schema_field_present`-varianten
  sin `_fair_code`-baserte kode, eller ein ny dedikert kode dersom
  Alternativ 2 vel eit anna kodenamn). Låg risiko, låg innsats.
- **README-påverknad:** ingen — README dokumenterer **utfall**
  («schema.title til stades — error»), ikkje mekanisme, og treng ikkje
  endrast av denne refaktoreringa i seg sjølv (kvar rad si Alvor-verdi er
  uendra).
- **Ekstra avgjerd naudsynt undervegs:** B5.3 sitt `tree_root`-spørsmål må
  avgjerast eksplisitt for den nye `class_field_present`-sjekktypen (skal
  han filtrere `tree_root` som dei andre klasse-sjekkane, eller halde
  fram med noverande, ufiltrerte åtferd?).

**Tilråding:** gjennomfør **Alternativ 1 no**, som ein del av denne
specen sine steg (låg risiko, løyser den verifiserte skadeverknaden
umiddelbart). Gjennomfør **Alternativ 2 som eiga, seinare spec** — han er
større enn resten av denne gjennomgangen til saman (nytt sjekk-register i
`server.py`, endringar i alle fem policy-YAML-filer, eit eksplisitt
`tree_root`-vedtak), og fortener eigen fokusert plan, testrunde og
brukar-gjennomgang framfor å blandast inn i denne meir generelle
koherens-gjennomgangen. Kartlegginga over (omfang, testpåverknad,
designval) bør vere tilstrekkeleg grunnlag til å starte den specen direkte
utan ny kartleggingsrunde.

## Funn C — Manglande metadata-konsistens (digdir_rule/fair_principle)

Fleire sjekkar manglar `digdir_rule:`/`fair_principle:`-felt sjølv om dei
konseptuelt høyrer til ein regel/eit prinsipp som **er** dokumentert i
README sin dekningsgrad-tabell:

| Sjekk | Manglar | README hevdar |
|---|---|---|
| `controlled_vocabulary_annotations` (bronze/gold) | `digdir_rule`, `fair_principle` | Regel 8 (line 21, dekningsgrad-tabellen) |
| `katalog_kontaktpunkt`, `katalogpost_endringsdato`, `datasett_kontaktpunkt`, `datatjeneste_kontaktpunkt` m.fl. (silver — alle `class_has_slot_with_uri`-sjekkane) | `fair_principle` (nokre manglar òg `digdir_rule`) | README sine sølv-/gull-tabellar viser FAIR-kolonneverdiar (t.d. `[F2, R1.2]`) for desse radene som **ikkje finst** som `fair_principle:`-felt i YAML |
| `container_katalog`, `container_datasett`, `container_kvalitetsmaal`, `container_kvalitetsmaaling` m.fl. | `digdir_rule`, `fair_principle` | README viser «—» for desse (korrekt — ingen påstand gjort), men dette er inkonsekvent med at andre containerkrav (`container_har_modellkatalog` i felles-datakatalog) heller ikkje har det, medan klassekrava (`katalog_tittel` osv.) **skal** ha FAIR-kolonneverdiar per README |

Kort sagt: **README sine FAIR-/Digdir-kolonner for AP-NO-klassekrava (silver-tabellen) er handskrivne og ikkje forankra i noko `fair_principle:`/`digdir_rule:`-felt i YAML.** Dette er ikkje feil i seg sjølv (informasjonen kan vere korrekt), men det tyder at README og YAML kan gli frå kvarandre over tid utan at nokon merkar det — akkurat den typen drift denne specen er meint å fange opp.

**Tilråding:** legg til dei manglande `digdir_rule:`/`fair_principle:`-felta på dei ~15 `class_has_slot_with_uri`-sjekkane i `silver.yaml` som README alt hevdar FAIR-verdiar for (`katalog_kontaktpunkt`, `katalog_tittel`, `katalog_utgiver`, `datasett_kontaktpunkt`, `datasett_tema`, `datasett_tittel`, `datasett_utgiver`, `datatjeneste_kontaktpunkt`, `datatjeneste_tittel`, `datatjeneste_utgiver`, `aktor_navn` m.fl. — sjå README-tabellen for eksakte verdiar). Lågare prioritet enn Funn A/B sidan det er reint dokumentasjons-/sporbarheitsarbeid, ikkje ei åtferdsendring.

## Forslag: tydeleg oppgraderingsvising i bronse-/sølv-/gull-tabellane

I dag viser gull-tabellen kvar rad si skildring med fri tekst («arva frå
bronse, oppgradert til error» / «arva frå sølv, oppgradert til error»).
Dette fungerer, men er **inkonsekvent handheva** (Funn A1 syner at éi rad
manglar heilt), og er ikkje skanbart ved eit blikk. Forslag:

1. **Legg til ein eksplisitt «Opphav»-kolonne** i bronse-/sølv-/gull-
   tabellane med standardiserte verdiar:
   - `Ny på bronse` / `Ny på sølv` / `Ny på gull` — sjekken finst ikkje på
     noko lågare nivå.
   - `Arva uendra (warning)` — sjekken finst på eit lågare nivå med same
     alvorsgrad, IKKJE oppgradert. **Denne verdien skal berre finnast i
     sølv-tabellen** (bronse-åtvaringar arva uendra til sølv utan at sølv
     legg noko til) — dersom han dukkar opp i **gull**-tabellen (eller
     manglar heilt, som for `no_inlined_on_primitive_range` i dag), er det
     eit teikn på nett den typen inkonsekvens Funn A1 fann, og bør
     handterast som eit avvik å rette, ikkje ein normaltilstand.
   - `Oppgradert til error (frå warning på <nivå>)` — eksplisitt when og
     frå kva nivå.
2. **Legg til éi samla verifiseringslinje** nedst i kvar av sølv- og
   gull-tabellen: talet på arva bronse-/sølv-åtvaringar vs. talet som
   faktisk er oppgraderte, slik at eit avvik som A1 hadde vore synleg ved
   berre å telje («bronse har 11 åtvaringar; gull oppgraderer 11 av 11» —
   som ville synt 10/11 i dag, eit umiddelbart raudt flagg).

## Forslag: sjølvhandhevande koherensetest

For å hindre at Funn A1 (eller tilsvarande) oppstår att stille, still, ved
neste nye bronse-/sølv-sjekk: legg til ein ny test i
`tests/test_mcp_policies.py` som **programmatisk** samanliknar
`load_policy("bronze")` og `load_policy("silver")` sine `checks:`-nøklar
mot `load_policy("gold")` sine, og feilar dersom ein nøkkel med
`severity: warning` i bronse/sølv **ikkje** har ei tilsvarande
`severity: error`-oppføring i gull — med ei eksplisitt, kommentert
allowlist for tilsikta unntak (t.d. dersom `r12_provenance`-typen
regel-scoping frå Funn B3 seinare gjer at nokon bronse-sjekk medvite
**ikkje** skal oppgraderast). Dette gjer koherens-kravet brukaren spør om
**handheva av testsuiten**, ikkje berre av denne eine gjennomgangen.

## Opne vurderingar (presenterte for brukaren, ikkje avklarte før skriving — jf. instruks)

1. **B2 sin eksakte implementasjon** — **retta etter B5-kartlegginga:**
   den opphavlege gjetninga her («truleg ikkje») var feil. B5.1 stadfesta
   **live** at eit felt i BÅDE `required` og `recommended` samstundes
   **faktisk** produserer to separate issues (éin `error`, éin `warning`)
   for same manglande felt — closuren har ingen sperre mot dette. Å
   berre leggje `version` til i `gold.yaml` sin `required:`-liste (utan
   Funn B5 sin Alternativ 1-fiks) ville difor **skapt eit nytt
   B5.1-tilfelle**, ikkje løyst B2 reint. **Rett rekkjefølgje:** gjennomfør
   steg 7 (B5 Alternativ 1) **før** steg 4 (B2), slik at
   `_check()`-closuren alt hoppar over duplikat når B2 sin
   `required`-tilføying vert gjort.
2. **B3 sitt forslag om å stramme inn `r12_provenance`** (fjerne
   `dct:publisher` frå `match_any_uri`) er ei reell kravskjerping for
   ikkje-AP-NO-domenemodellar på gullnivå, og bør vurderast separat frå
   dei reint dokumentasjons-/koherensretta endringane i denne specen.
   Tilrådinga i denne specen er å **berre presisere skildringa**, ikkje
   endre `match_any_uri`, med mindre brukaren eksplisitt ønskjer det
   strengare.
3. **Funn C sitt omfang** (~15 manglande `fair_principle:`/`digdir_rule:`-
   felt) er reint dokumentasjonsarbeid utan åtferdsendring — trygt å gjere
   samstundes med A/B, men lågare prioritet dersom tida er avgrensa.

## Steg

1. Legg til `no_inlined_on_primitive_range` i `gold.yaml` sin `checks:`
   med `severity: error` (Funn A1).
2. Rett `silver`/`gold`-radene i README sin «Nivå for skjemakvalitet»-
   tabell til Digdir-regel `1-11, 13-15` (Funn A2).
3. Fjern `f2_title` frå `gold.yaml` sin `fair_checks:`, med ein
   kommentarlinje som listar han saman med F1/F3/I1 (Funn B1).
4. Flytt `version` til `required:` på gullnivå og fjern `f4_version` frå
   `fair_checks:` — **utfør etter steg 7** (B5 Alternativ 1), elles
   skaper denne endringa sjølv eit nytt dobbeltsignal-tilfelle
   (Funn B2, jf. «Opne vurderingar» punkt 1).
5. Presiser skildringa av `r12_provenance` i `gold.yaml` og README til å
   nemne at han er dekka automatisk for AP-NO-konforme skjema (Funn B3).
6. Legg til éi forklarande linje i README under gull-tabellen som skil
   `schema_has_license`/`r11_license`/`distribusjon_lisens` frå kvarandre
   (Funn B4).
7. **Funn B5 — to delar, avklart av brukaren:**
   - **(a) Alternativ 1 — gjennomførast no, som del av denne specen:** i
     `_check()`-closuren i `validate_schema()` (`server.py`), hopp over
     eit `recommended`-felt som alt finst i `required_fields` for same
     scope, slik at eit felt aldri gjev både `error` og `warning`
     samstundes. Fjern dei to duplikat-produserande linjene (`title`,
     `version`) frå `felles-datakatalog.yaml`/`felles-begrepskatalog.yaml`
     sine `recommended:`-lister (dei er reint duplikat av arva
     `required`/`recommended` frå bronse — `description` er den einaste
     verdien som faktisk trengst der). Legg til ein kommentar i
     `bronze.yaml` sitt `required:`/`recommended:`-felt som peikar til
     denne specen sitt Funn B5.
   - **(b) Alternativ 2 — eiga spec skriven no, implementering utsett:**
     skriv ein ny, sjølvstendig spec i `specs/backlog/` for full
     konsolidering av `required:`/`recommended:` inn i
     `checks:`-mekanismen, basert direkte på kartlegginga i B5.4
     (omfang, testpåverknad, `tree_root`-avgjerd). Denne nye specen skal
     **ikkje** implementerast som del av handlingslista under — han er
     eit eige, seinare arbeidsstykke.
8. Legg til manglande `digdir_rule:`/`fair_principle:`-felt på dei ~15
   `class_has_slot_with_uri`-sjekkane i `silver.yaml` (Funn C).
9. Legg til «Opphav»-kolonne i bronse-/sølv-/gull-tabellane i README, med
   dei standardiserte verdiane skissert over.
10. Legg til éi samla oppgraderingslinje («bronse har N åtvaringar; gull
    oppgraderer M av N») nedst i gull-tabellen i README.
11. Skriv ein ny koherenstest i `tests/test_mcp_policies.py` som
    programmatisk validerer at kvar bronse-/sølv-`warning` har ei
    `error`-oppføring i gull, med kommentert allowlist for unntak.
12. Køyr `make mcp-linkml-valider-modell-test` og verifiser at ingen
    eksisterande testar (inkl. `_GOLD_PASS`/`_SILVER_PASS`-fixturane)
    brekk av steg 1-4 sine åtferdsendringar — spesielt steg 1
    (`no_inlined_on_primitive_range` vert no `error` på gull) kan i
    prinsippet slå ut på fixturar som har `inlined`/`inlined_as_list` sett
    feilaktig.
13. Køyr `make mcp-linkml-valider-modell SCHEMA=... POLICY=gold` mot eit
    utval reelle gull-policy-skjema (same 11 som i
    `specs/done/utvid-dekningsgrad-regel-5-12-14-15.md`) for å
    stadfeste om steg 1 eller 4 introduserer nye feil for eksisterande
    skjema, og rapporter eventuelle funn til brukaren utan å automatisk
    rette dei (same mønster som tidlegare regresjonssjekkar i denne
    policy-serien).

## Handlingsliste

- [x] Steg 1: `no_inlined_on_primitive_range` → error på gull
- [x] Steg 2: Rett Digdir-regel-rekkjevidde for sølv/gull i nivå-tabellen
- [x] Steg 3: Fjern duplikat `f2_title`
- [x] Steg 4: Fjern duplikat `f4_version` (etter verifisering)
- [x] Steg 5: Presiser `r12_provenance`-skildring
- [x] Steg 6: Forklarande linje for dei tre «lisens»-sjekkane
- [x] Steg 7a: Funn B5 Alternativ 1 — fiks dobbeltsignal-bugen no (kodeendring + fjern duplikatlinjer i dei to felles-*-policyane)
- [x] Steg 7b: Funn B5 Alternativ 2 — skriv oppfølgingsspec i specs/backlog/ (full konsolidering, ikkje implementert no)
- [x] Steg 8: Manglande digdir_rule/fair_principle-felt i silver.yaml
- [x] Steg 9: «Opphav»-kolonne i README-tabellane
- [x] Steg 10: Oppgraderingslinje i gull-tabellen
- [x] Steg 11: Sjølvhandhevande koherenstest
- [x] Steg 12: Testverifisering
- [x] Steg 13: Regresjonssjekk mot reelle gull-skjema

## Utført

**Dato:** 2026-08-31

Alle steg gjennomførte, i rekkjefølgja 1 → 7a → 4 → 3 → 5 → 6 → 8 → 2 → 9 →
10 → 7b → 11 → 12 → 13 (7a før 4, jf. avhengigheita retta i «Opne
vurderingar» punkt 1).

**Nye funn gjort under implementeringa (utover det som var kartlagt i
gjennomgangen):**

- **`schema.description` var ALT hevda som `error` på gullnivå i README
  («arva frå bronse, oppgradert til error»), men koden gav framleis berre
  `warning`** — stadfesta live på same måte som B2, og retta på same måte
  (lagt til i `gold.yaml` sin `required:`-liste, verna av steg 7a sin
  dedup-fiks). Dette var ikkje eksplisitt lista i «Funn B» frå før, men er
  same mønster som B1/B2 og er retta i same veg.
- **Silver-tabellen i README mangla ei rad heilt** for
  `distribusjon_lisens` (`Distribusjon har slot med dct:license`), sjølv
  om sjekken finst i `silver.yaml` og vert vist oppgradert i gull-tabellen.
  Lagt til.

**Endringar:**

- **`server.py`:** `_check()`-closuren hoppar no over eit
  `recommended`-felt som alt er `required` for same scope (Funn B5
  Alternativ 1).
- **`bronze.yaml`:** ny kommentar om required/recommended-mekanismens
  avgrensing (Funn B5); `controlled_vocabulary_annotations` fekk
  `digdir_rule`/`fair_principle` (Funn C).
- **`silver.yaml`:** 14 checks fekk manglande/utvida `digdir_rule`/
  `fair_principle`-felt for å matche det README alt hevda (Funn C).
- **`gold.yaml`:** `no_inlined_on_primitive_range` lagt til som error
  (A1); `f2_title`/`f4_version` fjerna, erstatta av `description`/
  `version` i `required:`-lista (B1/B2 + det nye description-funnet);
  `controlled_vocabulary_annotations` fekk digdir_rule/fair_principle;
  `r12_provenance` sin skildring presisert (B3).
- **`felles-datakatalog.yaml`/`felles-begrepskatalog.yaml`:** fjerna
  `title`/`version` frå `recommended:`-listene (kjelda til det live
  stadfesta B5.1-duplikatet).
- **`policies/README.md`:** Digdir-regel-rekkjevidde retta for sølv/gull
  (A2); ny «Oppgraderer til»-kolonne i bronse-/sølv-tabellane og
  «Opphav»-kolonne i gull-tabellen; ny forklarande boks om dei tre
  «lisens»-sjekkane (B4); ny oppgraderingsstatus-linje under gull-tabellen
  (talfesta 14/14 og 12/12); manglande `distribusjon_lisens`-rad lagt til
  i sølv-tabellen; `r12_provenance`-rad presisert.
- **`tests/test_mcp_policies.py`:** ny `TestPolicyKoherens`-klasse med
  programmatisk koherenstest (Funn A1/«Forslag: sjølvhandhevande
  koherensetest»); dei to testane som assertar på dei no fjerna
  `fair_f2`/`fair_f4`-kodane oppdaterte til å forvente
  `missing_required_metadata` i staden.
- **`specs/backlog/konsolider-feltnaervaer-sjekk-i-checks-mekanismen.md`:**
  ny, sjølvstendig spec for Funn B5 Alternativ 2 (full konsolidering),
  **ikkje implementert** — eige, seinare arbeidsstykke.

**Verifisering:**

- `make mcp-linkml-valider-modell-test`: 44/45 grøne. Den attverande
  feilen (`TestGold.test_gyldig_skjema_har_ingen_feil`, `errorCount 2`) er
  stadfesta identisk og urelatert (`class_missing_required_slot` for
  `Datasett`/`dct:accessRights` og `dcatap:applicableLegislation` —
  same pre-eksisterande fixture-avvik dokumentert i tidlegare
  specar i denne serien).
- **Programmatisk verifisert:** bronse har 14 `warning`-sjekkar (12 i
  `checks:` + `description`/`version` via `required`), og alle 14 er no
  oppgraderte til `error` i gull. Sølv legg til 12 eigne nye
  `warning`-sjekkar, og alle 12 er oppgraderte. `TestPolicyKoherens`
  handhevar dette automatisk framover.
- **Regresjonssjekk mot alle 11 reelle gull-policy-skjema** (same sett
  som i `specs/done/utvid-dekningsgrad-regel-5-12-14-15.md`), før (via
  `git stash`) og etter: identisk `errorCount`/`warningCount` for alle 11
  (dcat-ap-no 20, cpsv-ap-no 24, dqv-core 12, dqv-ap-no 4,
  modelldcat-katalog 7, modelldcat-ap-no 4, modelldcat-modell 31,
  skos-ap-no 11, xkos-ap-no 8, fair-metadata 20, referansemodell-gold 4 —
  alle `warningCount: 0`). Ingen regresjon.
- **Driftsmerknad:** regresjonssjekken vart avbroten éin gong av eit
  2-minutts kommandotidsavbrot midt i ein `git stash`-økt (stash vart
  verande på stacken i staden for poppa). Oppdaga og retta umiddelbart
  (`git stash pop` + stadfesta alle endringar attende via `git status`/
  `grep` før arbeidet heldt fram) — ingen arbeid gjekk tapt. Genererte
  `validation/*.json`-biprodukt frå regresjonssjekken er rydda vekk att.
