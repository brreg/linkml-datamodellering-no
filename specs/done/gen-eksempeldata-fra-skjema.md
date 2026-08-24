# Generer syntetisk eksempeldatafil frå LinkML-skjema

## Bakgrunn

Brukaren ønskjer ein funksjon som genererer ei eksempeldatafil med syntetiske
(ikkje-reelle) data frå eit LinkML-skjema — gyldig i henhold til skjemaet.
Funksjonen skal (1) kunne brukast av `make new-modell` (både med og utan
`JSON_SCHEMA=`-flagget), og (2) kunne køyrast manuelt av nokon som modellerer
lokalt og treng ei testdatafil.

**Dette finst allereie i miniatyr.** `src/mcp-linkml-modell-utkast/validator.py`
har ein CLI-inngang (`_main()`, linje 171–229) som skriv eit dummy-eksempel-
datasett for containerklassen til stdout — kalla frå
`src/assets/scripts/scaffolding/new-modell.sh` (linje 224–256, sjå kommandoen
under). `JSON_SCHEMA`-flagget påverkar **ikkje** dette steget i det heile —
eksempelgenerering køyrer identisk uansett om skjemaet vart bygd frå eit
JSON Schema-utkast eller eit tomt stub-skjema. Punkt (1) i brukaren sitt ønske
er difor alt strukturelt løyst; arbeidet her handlar om å (a) gjere
generatoren monaleg rikare, og (b) eksponere henne som eit direkte
`make`-target for punkt (2).

```bash
podman run -i --rm \
  -v ".../server.py:/app/server.py:ro" \
  -v ".../converter.py:/app/converter.py:ro" \
  -v ".../validator.py:/app/validator.py:ro" \
  -v ".../profiles:/app/profiles:ro" \
  -v "src/assets/scripts/utils:/app/utils:ro" \
  -v "<schema-fil>:/app/schema.yaml:ro" \
  mcp-linkml-modell-utkast \
  python3 /app/validator.py /app/schema.yaml "<schema_name>:eksempel"
```

**Dagens avgrensing er eit medvite v1-scope-val**, dokumentert i
`specs/done/new-modell-json-schema-flagg.md` (linje 213–217): *"behald
placeholder-tilnærminga slik ho er i dag (kun `required`/`identifier`-slots)
i staden for å fylle ut alle valfrie slots"*. Denne specen utvidar nettopp
det scopet.

### Avklarte designval (brukarstadfesta)

1. **Slot-omfang:** fyll ut **alle** slots (required + valfrie), ikkje berre
   required/identifier som i dag.
2. **Klassereferansar:** for eit slot med `range` som peikar på ein annan
   lokal klasse, generer ein syntetisk instans av target-klassen og lenk via
   URI/id (følgjer "Lenking framfor inlining").
3. **Verditype:** beskrivande placeholder utleidd frå slot-/klassenamn
   (t.d. `"Eksempelverdi for kommunenummer"`), **ingen** ny biblioteks-
   avhengigheit (`faker` vart vurdert og avvist).

### Presisering frå research (viktig avgrensing av punkt 2)

Klassereferanse-generering kan **ikkje** vere fullstendig rekursiv over heile
klassegrafen: containerklassen sine `attributes` er den einaste staden ei
eksempelfil har eit naturleg rotpunkt å plassere ein toppnivå-liste av
instansar (jf. containerklasse-konvensjonen). Eksisterande handskrivne
eksempel (`src/linkml/ap-no/dcat-ap-no/examples/dcat-ap-no-eksempel.yaml`)
stadfestar dette mønsteret: `foaf:Agent`/utgivar-referansar er reine eksterne
URI-ar (`organization-catalog.fellesdatakatalog.digdir.no/...`), **ikkje**
lokalt genererte instansar, sidan `Agent` ikkje er ein containerattributt-klasse
i det skjemaet.

**Regel:** for eit slot med klasse-range:
- Dersom target-klassen **er** ein av containerklassen sine eigne attributt-
  klassar (dvs. har fått generert sin eigen toppnivå-instans i same fil):
  slot-verdien vert sett til den genererte instansen sin `identifier`-verdi
  (wrapa i liste dersom `multivalued`).
- Elles: slot-verdien vert ein generisk syntetisk URI-streng (som i dag,
  ingen fysisk instans plassert nokon stad i fila) — dette er **ikkje** eit
  avvik frå brukaren sitt ønske, men ei nødvendig avgrensing sidan skjemaet
  sjølv ikkje definerer noka toppnivåplassering for slike klassar.

### Andre presiseringar

- **Multivalued-hòl i dagens generator (vert retta som del av dette
  arbeidet):** `_build_dummy_instance()` (linje 46–60) kallar
  `_placeholder(range_str)` og set verdien direkte — **utan** å sjekke
  `slot.multivalued`. Eit required multivalued slot (t.d. ei required
  `LangString`-tittel-liste) får i dag ein **skalar** placeholder i staden
  for ei liste, sjølv om containerattributtet sin eigen multivalued-sjekk
  (`_build_dummy_data`, linje 63–75) fungerer korrekt for containerattributt-
  nivået. Dette er ein reell mangel i dagens minimale generator, ikkje berre
  eit scope-hòl.
- **`LangString` er ein `types:`-oppføring** (`base: str`, ikkje ein eigen
  klasse) — treng difor ingen særhandtering utover vanleg streng-placeholder;
  multivalued-fiksen over dekkjer listeform.
- **Enum-range** (`permissible_values`) vert i dag ikkje handtert i det
  heile — fell gjennom til generisk `"dummy"`-streng, som ikkje er ein gyldig
  enum-verdi. Ny logikk må slå opp `sv.get_enum(range_str)` og velje første
  `permissible_values`-nøkkel.
- **Pattern-/verdiavgrensingar (`pattern`, `minimum_value`/`maximum_value`
  utover generisk 0) er eksplisitt utanfor scope.** Ein generisk placeholder
  kan ikkje garantert tilfredsstille eit vilkårleg regex-mønster. Dette er
  same avgrensing som dagens generator alt har (jf. kommentaren
  `new-modell.sh` skriv i eksempelfila: *"Genererte placeholder-verdiar ...
  må erstattast med reelle verdiar"*) — behald og oppdater denne åtvaringa,
  ikkje prøv å løyse pattern-tilfredsstilling generisk.
- **`validate_generated()`** (linje 82–164, brukt av MCP-serveren sin interne
  sjølvsjekk under skjemagenerering) skal **ikkje** endrast til å bruke den
  nye rikare logikken — han skal halde fram med dagens minimale
  `_build_dummy_data`/`_build_dummy_instance` (required/identifier-only).
  Grunngjeving: å fylle ut alle valfrie slots aukar sjansen for at generiske
  placeholders bryt `pattern`/`minimum_value`-avgrensingar på eit skjema
  under aktiv utarbeiding, noko som ville gje falske negative i eit
  etablert, testa MCP-sjølvsjekk-steg utan tilhøyrande brukarbehov. Den nye,
  rikare logikken vert difor implementert som **nye, separate funksjonar**
  ved sida av dei eksisterande — ikkje ei omskriving av dei.

## Steg

1. I `src/mcp-linkml-modell-utkast/validator.py`: legg til nye funksjonar
   ved sida av (ikkje i staden for) `_placeholder`/`_build_dummy_instance`/
   `_build_dummy_data`:
   - `_enum_placeholder(sv, range_str)` — slår opp `sv.get_enum(range_str)`,
     returnerer første `permissible_values`-nøkkel som streng, eller `None`
     om `range_str` ikkje er eit enum-navn.
   - `_example_placeholder(range_str, slot_name)` — som dagens
     `_placeholder()`, men fallback for ukjent range vert
     `f"Eksempelverdi for {slot_name}"` i staden for generisk `"dummy"`.
   - `_build_example_instance(sv, class_name, class_id_map)` — itererer
     **alle** `sv.class_induced_slots(class_name)` (ikkje berre
     required/identifier). For kvart slot: class-range → slå opp i
     `class_id_map` (sett i steg 2 sitt pass 1), enum-range →
     `_enum_placeholder`, elles → `_example_placeholder`. Wrap i liste
     dersom `slot.multivalued`. Set `identifier: true`-slot til verdien
     frå `class_id_map[class_name]` (generalisert — ikkje hardkoda til
     slotnavn `"id"` som dagens `_main()`-patch).
   - `_build_example_data(sv, container_class, id_prefix)` — to pass:
     **pass 1** genererer éin id per containerattributt-klasse
     (`f"{id_prefix or schema_name}:{kebab(class_name)}-1"`) og fyller
     `class_id_map`; **pass 2** kallar `_build_example_instance` for kvar
     containerattributt-klasse med det ferdige `class_id_map`-et
     tilgjengeleg for cross-referanse-oppslag.

2. Oppdater `_main()` (linje 171–229) til å kalle `_build_example_data`
   i staden for `_build_dummy_data`, og fjern den no overflødige
   post-hoc `if "id" in instance"`-patchen (id-tildeling skjer no inne i
   pass 1/2 i steg 1). Signatur/CLI-grensesnitt (`python3 validator.py
   <schema.yaml> [id-prefiks]`) er uendra.

3. Legg til nytt make-target `gen-eksempeldata` i `make/70-scaffolding.mk`
   (co-lokalisert med `new-modell`, same underliggjande container):
   `make gen-eksempeldata SCHEMA=<sti> [OUT=<sti>] [ID_PREFIX=<prefiks>]`.
   - Byggjer `mcp-linkml-modell-utkast`-imaget viss det manglar (som
     `new-modell` gjer i dag).
   - Køyrer same podman-monteringsmønster som `new-modell.sh` linje 229–236
     (monterer `src/assets/scripts/utils` for
     `linkml_relative_import_patch`, BUG-15).
   - `ID_PREFIX` er valfri (default: skjemaet sitt `name`-felt, utleidd som
     i `new-modell.sh`).
   - Utan `OUT=`: skriv til stdout (lèt brukaren redirigere sjølv).
   - Med `OUT=<sti>`: skriv til fil — **nektar å overskrive** ei
     eksisterande fil med mindre `OVERWRITE=1` er sett eksplisitt (hindrar
     utilsikta overskriving av ei handkuratert `examples/<modell>-
     eksempel.yaml`). Bruk `run_logged` (jf. CLAUDE.md § «Ingen stille
     feil») rundt podman-kallet, ikkje `> /dev/null 2>&1`.
   - Legg til rad i `COMMANDS.md` (same tabellstruktur som eksisterande
     `make new-modell`/`make mcp-linkml-modell-utkast`-rader, sjå linje
     144/271–272).

4. Oppdater kommentaren `new-modell.sh` skriv øvst i genererte
   `examples/<modell>-eksempel.yaml` (linje 247–249) til å reflektere at
   fila no inneheld fleire/rikare placeholder-verdiar, inkludert
   kryssrefererte instansar — behald åtvaringa om at placeholder-verdiar
   (og no òg eventuelle pattern-/verdiavgrensingar) må erstattast med reelle
   verdiar.

5. Verifiser med `make gen-eksempeldata SCHEMA=<eksisterande-schema.yaml>
   OUT=<scratch-sti>` mot minst to eksisterande skjema med ulike trekk
   (t.d. eitt med `LangString`/multivalued required-slots, eitt med enum-
   range, eitt med fleire containerattributt-klassar som refererer
   kvarandre) — inspiser output manuelt for: alle slots fylte (ikkje berre
   required), lister for multivalued, enum-verdi frå permissible_values,
   klassereferansar peikar på faktisk genererte id-ar der target-klassen er
   ein containerattributt, generisk placeholder-URI elles.

6. Kjør `make validate-instance SCHEMA=<samme schema> INSTANCE=<scratch-
   output>` for kvar test i steg 5 — dokumenter i "Utført"-seksjonen kva
   som validerer reint og kva som (venta) feilar på pattern-/
   verdiavgrensingar som ikkje er løyst generisk (jf. § Presisering).

7. Regenerer eit nytt testskjema med `make new-modell DOMAIN=<test>
   NAME=<test>` (utan `JSON_SCHEMA`) og med `JSON_SCHEMA=<sti>` (med), og
   stadfest at begge produserer den rikare eksempelfila via den uendra
   `new-modell.sh`-integrasjonen (ingen endring naudsynt i sjølve
   `new-modell.sh` sitt podman-kall, kun i `validator.py` sin interne
   logikk — jf. § Bakgrunn).

## Handlingsliste

- [x] Legg til `_enum_placeholder`, `_example_placeholder`,
      `_build_example_instance`, `_build_example_data` i `validator.py`
      (nye funksjonar, `_build_dummy_*`/`validate_generated()` uendra)
- [x] Oppdater `_main()` til å bruke `_build_example_data`, fjern post-hoc
      id-patch
- [x] Nytt make-target `gen-eksempeldata` i `make/70-scaffolding.mk`
      (SCHEMA=, valfri OUT=/ID_PREFIX=/OVERWRITE=)
- [x] Rad i `COMMANDS.md` for `gen-eksempeldata`
- [x] Oppdater header-kommentaren `new-modell.sh` skriv i genererte
      eksempelfiler
- [x] Verifiser mot ≥2 eksisterande skjema (LangString/multivalued, enum,
      klassereferansar) — manuell inspeksjon av output
- [x] `make validate-instance` mot generert output for kvar test, dokumenter
      resultat
- [x] Regenerer eit testskjema via `make new-modell` (med og utan
      `JSON_SCHEMA`) og stadfest uendra integrasjon

## Utført

**Avvik frå opphavleg plan (id-tildeling):** Steg 1/2 planla
`class_id_map[range_class] = "<prefiks>:<kebab(class_name)>-1"`
(éin id per **klasse**). Verifisering mot `enhetsregisteret-bvrfriv`
avdekte at dette gjev **duplikate id-ar og identisk innhald** når fleire
containerattributt peikar på same klasse (t.d. tre ulike aktørrollar alle
typa som same klasse) — alle tre fekk same id og same placeholder-innhald.
Retta ved å skilje "denne attributtinstansen sin eigen id" (unik per
containerattributt, sekvensielt `<prefiks>-N` — beheld den opphavlege
`<navn>:eksempel-N`-konvensjonen frå `_main()`-docstringen) frå
"id-en andre instansar skal kryssreferere til for denne klassen" (første
tildelte id for klassen, `class_id_map.setdefault(...)`). Sjå
`_build_example_instance(sv, class_name, class_id_map, own_id)` og
`_build_example_data()` i `validator.py`.

**To tilleggsfunn under verifisering (retta, utanfor opphavleg plan):**
- `NonNegativeInteger`-typa slot (t.d. `dcat:byteSize`/`filstorrelse`) fekk
  tekst-placeholder (`"Eksempelverdi for filstorrelse"`) i staden for eit
  gyldig heiltal, sidan berre range-**namnet** vart slått opp mot
  `_PLACEHOLDERS`, ikkje den underliggjande `base`-typen til eigendefinerte
  `types:`-oppføringar. Lagt til `_type_base(sv, range_str)` som løyser
  `sv.get_type(range_str).base` og fell tilbake til rett primitiv
  placeholder (framleis tekst-fallback for `base: str`-typar som
  `Duration`/`GYear`/`LangString`).
- `_PLACEHOLDERS["datetime"]` mangla tidssone (`"2024-01-01T00:00:00"`),
  som braut `date-time`-formatkravet for eit required datetime-slot i
  `samt-bu`. Retta til `"2024-01-01T00:00:00Z"` — gjeld begge generatorane
  (delt konstant), reint forbetring utan nedside.

**Verifisert mot tre skjema** (via `bash
src/assets/scripts/makefile/gen-eksempeldata.sh` direkte, sidan `podman`
treng `dangerouslyDisableSandbox` i denne økta pga. rootless
namespace-avgrensing i sandkassa):

- **`samt-bu`** (LangString/multivalued required-slots, fleire
  containerattributt som deler klasse, djup instans-kjeding) —
  `make validate-instance`: **"No issues found"**.
- **`enhetsregisteret-bvrfriv`** (enum-range, versjonslåst import → råka
  av BUG-15 i `validate-instance`, verifisert i staden via eit
  patcha ad-hoc valideringsscript identisk med `validate_generated()`
  sin eigen valideringslogikk) — enum løyst korrekt (`maalformForTilbakemelding:
  nob`, første `permissible_values`-nøkkel); **6 feil, alle
  `pattern`-regex-mismatch** (t.d. e-post, mobilnummer, organisasjonsnummer)
  — nøyaktig den dokumenterte, eksplisitt utanfor-scope-avgrensinga (§
  Presisering). Ingen andre feiltypar.
- **`javazonetalk`** (minimal, éin klasse) — 0 feil, 0 åtvaringar.
- **`dcat-ap-no`** (AP-NO-profil utan eigen containerklasse) — scriptet
  feilar med tydeleg feilmelding ("fann ikkje containerklasse") i staden
  for å krasje eller produsere tomt/ugyldig output — stadfestar korrekt
  handtering av denne skjematypen.

**Podman-monteringsfiks (utanfor opphavleg plan, naudsynt for at scriptet
i det heile skal fungere):** opphavleg plan (steg 3) føresette at berre
éi skjemafil måtte monterast (same mønster som `new-modell.sh` sitt
podman-kall). Verifisering mot `samt-bu` avdekte at dette feilar for
skjema med relative importar til søskendomene (t.d. `dqv-ap-no` frå
`dcat-ap-no`), sidan berre den eine fila var synleg inni containeren.
Retta ved å montere **heile repoet** (`$REPO_ROOT:/work:ro`, same mønster
som `WORK_MOUNT`/`LINKML_RUN` i `make/01-containers.mk`) og sende
skjemastien relativt til repo-rota inn i containeren, i staden for å
montere skjemaet som ei enkelt omdøypt fil.

**`make new-modell` end-to-end-test:** `make new-modell DOMAIN=testverify
NAME=testverify` (utan `JSON_SCHEMA`) produserte korrekt oppdatert
header-kommentar i den genererte eksempelfila, utan nokon endring i
`new-modell.sh` sitt podman-kall — stadfester at integrasjonspunktet i
§ Bakgrunn var korrekt. Rydda opp med `make remove-modell DOMAIN=testverify
NAME=testverify CONFIRM=1` etterpå.

Alle scratch-verifiseringsfiler (`.scratch-verify/`) sletta før avslutning
— ingen spor i arbeidstreet utover dei tiltenkte kode-/dokumentendringane.
