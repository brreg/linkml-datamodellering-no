# Fiks: allOf-komponerte definisjonar vert stille droppa av JSON Schema → LinkML-konverteraren

## Bakgrunn

Under `make new-modell DOMAIN=oreg NAME=enhetsregisteret-bvrstiftelsesdokument JSON_SCHEMA=src/tmp/bvrstiftelsesdokument_lm_v0.schema.json`
feila `make lint` med:

```
error  Class 'AnnenAdresse' slot 'stedsadresse' range 'Stedsadresse' is not defined.  (no_undeclared_ranges)
error  Class 'AnnenAdresse' slot 'utenlandskAdresse' range 'InternasjonalAdresse' is not defined.  (no_undeclared_ranges)
```

Kjeldeskjemaet (`src/tmp/bvrstiftelsesdokument_lm_v0.schema.json`) definerer `Stedsadresse`
og `InternasjonalAdresse` med JSON Schema sitt vanlege "utvid ein foreldretype"-mønster:

```json
"Stedsadresse": {
  "title": "Stedsadresse",
  "allOf": [
    {"$ref": "#/definitions/GeografiskAdresse"},
    {"type": "object", "required": ["stedsnavn", "poststed"],
     "properties": {"stedsnavn": {"$ref": "#/definitions/Tekst50"},
                     "poststed": {"$ref": "#/definitions/Poststed"}}}
  ]
}
```

**Rotårsak** ligg i `src/mcp-linkml-modell-utkast/converter.py::_collect_classes()`
(line 223–251). Ein `$defs`/`definitions`-oppføring vert berre rekna som ei klasse
når han har `type: object` **eller** ein `properties`-nøkkel direkte på toppnivå:

```python
if defn.get("type") == "object" or "properties" in defn:
    classes[...] = {...}
```

Ei `allOf`-komponert def som `Stedsadresse` har ingen av delane på eige toppnivå —
`type`/`properties` ligg inni `allOf`-lista. Definisjonen vert difor **stille hoppa over**:
ingen klasse, inga åtvaring.

Samstundes handterer `_resolve_type()` sin `$ref`-gren (line 126–131) referansar
til slike definisjonar heilt fint — slotet `stedsadresse` (`{"$ref": "#/definitions/Stedsadresse"}`)
vert korrekt omsett til `range: Stedsadresse`. Resultatet er eit internt inkonsistent
LinkML-skjema: slots som peikar på klassar som aldri vart generert. Feilen syner seg
først seinare, i `make lint`, utan nokon peikepinn tilbake til den faktiske årsaka.

Dette bryt "Ingen stille feil"-prinsippet i CLAUDE.md. Konstruksjonar konverteraren
ikkje kan modellere fullt ut skal degradere synleg — slik `anyOf` med fleire ikkje-null-typar
og eksterne `$ref` alt gjer i dag (sjå `README.md` § Avgrensingar) — ikkje forsvinne.

Feilen vart retta manuelt for `enhetsregisteret-bvrstiftelsesdokument` i ei tidlegare
økt (la til `Stedsadresse`/`InternasjonalAdresse` som `is_a: GeografiskAdresse`-klassar
for hand i `src/linkml/oreg/enhetsregisteret-bvrstiftelsesdokument/enhetsregisteret-bvrstiftelsesdokument-schema.yaml`).
Denne spec-en fiksar konverteraren sjølv, slik at framtidige JSON Schema-import med
same `allOf`-mønster ikkje krev same manuelle reparasjon.

**Avgrensing:** dette gjeld `allOf` **på definisjonsnivå** (komponerer ei heil klasse).
Eigenskapsnivå `allOf`/`oneOf` (éin enkelt property-verdi brukar `allOf`/`oneOf` i staden
for `$ref`) er ei anna, alt dokumentert avgrensing (`README.md` § Avgrensingar,
`_resolve_type()` line 119–123) og er **ikkje** i scope her.

## Steg

1. **Utvid `_collect_classes()` til å attkjenne allOf-komponerte definisjonar**
   - Ny gren: når ein def manglar `type: object`/`properties` på toppnivå, men har `allOf`,
     gå gjennom `allOf`-lista.
   - Skil mellom medlemmer som er ein lokal `$ref` til ein annan definisjon (potensiell
     foreldreklasse) og medlemmer som er eit inline objektskjema (`properties`/`required`
     direkte på medlemen).
   - Slå saman alle inline-medlemmers `properties`/`required` til klassen sine eigne
     (same logikk som den eksisterande `properties in defn`-grena brukar for enkeltskjema).
   - Om nøyaktig éin `$ref`-medlem peikar til ei anna def som sjølv vert til ein klasse:
     registrer denne som `is_a`-forelder. Klassen sine eigne `properties`/`required` skal
     **ikkje** innehalde forelderen sine felt — dei vert arva via `is_a` i LinkML.
   - Om fleire `$ref`-medlemmer finst (multippel arv, som LinkML ikkje støttar direkte
     via `is_a`): behald berre den første som `is_a`, flat ut felta frå dei resterande
     direkte inn i klassen (som om dei var inline-medlemmer), og legg til ei åtvaring som
     forklarer nedgraderinga.
   - Om ein `$ref`-medlem peikar til noko som ikkje vert ein klasse (t.d. ein primitiv
     `type`-def, eller manglar i `$defs`): flat ut medlemen (utan felt å hente) og legg
     til ei åtvaring.
   - Utvid returtypen frå `_collect_classes()` med eit nytt valfritt felt,
     `"is_a": <klassenamn | None>`, ved sida av eksisterande `"properties"`, `"required"`,
     `"description"`.

2. **Emitter `is_a` i den genererte LinkML-klassa**
   - I `convert()` (rundt line 385–415, der `classes_out[cls_name] = entry` vert bygd):
     når `cls_data.get("is_a")` er sett, legg `entry["is_a"] = cls_data["is_a"]` inn i
     klasse-entryen — plassert etter `description`/`class_uri`, før `slots`, for å matche
     rekkjefølgja i handskrivne skjema i repoet (t.d. `Stedsadresse`/`InternasjonalAdresse`
     i `enhetsregisteret-bvrstiftelsesdokument-schema.yaml`).
   - `slots`-lista for ei `is_a`-klasse skal berre innehalde klassen sine **eigne** slots
     (ikkje `id` eller andre slots alt deklarerte på forelderklassen) — matchar
     CLAUDE.md § "Slots, ikke attributes" og det manuelle føredømet frå denne økta.

3. **Aldri stille dropp — berre degraderte tilfelle skal gje åtvaring**
   - Uansett kva gren som treff (rein `is_a`, fleire foreldre flata ut, eller
     ureferrerbar `$ref`), skal ei def med `allOf` alltid ende opp som **ei klasse**
     i output — aldri forsvinne.
   - Berre dei degraderte tilfella (fleire `$ref`-foreldre, eller `$ref` til noko som
     ikkje vert ein klasse) skal gje ei åtvaring. Det vanlege eittparent-tilfellet skal
     konvertere stille, på same måte som `$ref`- og `array`-handteringa gjer i dag.

4. **Regresjonstest med det faktiske skjemaet som avdekte feilen**
   - Legg til nye testar i `tests/test_mcp_linkml_generator.py::TestConversion`:
     - `test_allof_med_ref_gir_is_a_klasse` — konverterer eit minimalt JSON Schema med
       same struktur som `Stedsadresse`/`GeografiskAdresse`-paret i
       `src/tmp/bvrstiftelsesdokument_lm_v0.schema.json`
       (`allOf: [{$ref: Base}, {type: object, properties: {...}, required: [...]}]`), og
       assert at:
       - Klassa finst i `schema["classes"]`
       - `schema["classes"]["Stedsadresse"]["is_a"] == "GeografiskAdresse"`
       - Klassen sine eigne `slots` inneheld dei nye felta, men ikkje forelderen sine
       - `warnings == []` (det vanlege tilfellet skal vere stille)
     - `test_allof_med_fleire_ref_gir_åtvaring` — same mønster med to `$ref`-medlemmer,
       assert at ei åtvaring vert generert **og** at klassa likevel finst.
   - Køyr `make mcp-linkml-modell-utkast-test` og stadfest at alle eksisterande testar
     framleis passerer.

5. **Verifiser mot det faktiske regresjonsskjemaet**
   - Køyr `make mcp-linkml-modell-utkast SCHEMA=src/tmp/bvrstiftelsesdokument_lm_v0.schema.json`
     og stadfest at det genererte skjemaet no inneheld `Stedsadresse`/`InternasjonalAdresse`
     som `is_a: GeografiskAdresse`-klassar utan manuell etterredigering.
   - Køyr `make lint` på det ferske resultatet og stadfest at det ikkje lenger gir
     `no_undeclared_ranges`-feil for desse to klassane.
   - Samanlikn med den handretta fiksen frå denne økta i
     `src/linkml/oreg/enhetsregisteret-bvrstiftelsesdokument/enhetsregisteret-bvrstiftelsesdokument-schema.yaml`
     — resultatet bør no vere strukturelt likt (same `is_a`, same felt) utan at den
     committa fila treng endrast.

6. **Oppdater dokumentasjon**
   - `src/mcp-linkml-modell-utkast/README.md` § "Avgrensingar" og § "Typeomsetting":
     legg til ei linje som forklarer at `allOf` **på definisjonsnivå** (komponerer ein
     heil klasse) no vert støtta og mappa til `is_a` (+ åtvaring ved fleire foreldre),
     medan `allOf`/`oneOf` **på eigenskapsnivå** (éin enkelt property-verdi) framleis
     fell tilbake til `range: string` + åtvaring som før.
   - `specs/done/json-schema-roundtrip-test.md` § "Forbehold" nemner `allOf` som eit
     kjent, ekskludert avvik i roundtrip-samanlikninga. Vurder om roundtrip-testen no
     bør utvidast til å samanlikne `allOf`-komponerte klassar òg, sidan dei faktisk vert
     generert etter denne fiksen. Kan takast som eige, seinare steg dersom det er for
     stort å ta her — noter i så fall eksplisitt som "ikkje utført" i Utført-avsnittet.

## Ikkje i scope

- Eigenskapsnivå `allOf`/`oneOf` (`_resolve_type()` line 119–123) — uendra åtferd
  (`range: string` + åtvaring).
- `oneOf`-komponerte definisjonar utan direkte `properties` på toppnivå (ein ulik,
  sjeldnare variant enn `allOf` — same symptom, men ikkje det som vart rapportert her).
  Kan handterast som eiga oppfølging om det dukkar opp i praksis.
- `mixins:`-støtte for meir enn éin `$ref`-forelder — vurdert, men ikkje innført i denne
  runden sidan det ikkje finst presedens for `mixins:` i eksisterande skjema i repoet.
  Multiple `$ref`-foreldre vert i staden flata ut med åtvaring (steg 1).

## Utført

1. **`_collect_classes()` attkjenner allOf-komponerte definisjonar** — implementert i
   `src/mcp-linkml-modell-utkast/converter.py`. Ny hjelpefunksjon `_is_class_like()` og
   `_merge_allof_members()` skil `$ref`-medlemmer (potensielle `is_a`-foreldre) frå
   inline objektskjema-medlemmer, med éin-nivås flating og åtvaring for fleire
   `$ref`-foreldre eller `$ref` til noko ikkje-klasseaktig. `_collect_classes()` tek no
   `warnings`-lista som parameter (kalt frå `convert()`).
2. **`is_a` vert emittert i `convert()`** — klasse-entryen får `is_a` rett etter
   `class_uri`. `id`-slotet (og andre eventuelle arva slots) vert ikkje deklarert på
   nytt for `is_a`-klassar.
3. **Aldri stille dropp** — stadfesta ved regresjonstestane i steg 4: ei def med `allOf`
   vert alltid til ei klasse, uansett kva gren som treff.
4. **Regresjonstestar lagt til** i `tests/test_mcp_linkml_generator.py::TestConversion`:
   `test_allof_med_ref_gir_is_a_klasse`, `test_allof_med_fleire_ref_gir_åtvaring`, og
   (i tillegg til opphavleg plan) `test_allof_med_ref_til_ikkje_klasse_gir_åtvaring` for
   den tredje grena (`$ref` til noko ikkje-klasseaktig). Alle 47 testar i
   `make mcp-linkml-modell-utkast-test` passerer.
5. **Verifisert mot det faktiske regresjonsskjemaet** — `make mcp-linkml-modell-utkast
   SCHEMA=src/tmp/bvrstiftelsesdokument_lm_v0.schema.json` genererer no
   `Stedsadresse`/`InternasjonalAdresse` som `is_a: GeografiskAdresse`-klassar utan
   manuell etterredigering, strukturelt identisk med den handretta fiksen frå tidlegare
   økt. Den automatiske `roundtrip-json-schema`-testen (køyrt av same make-target)
   passerer. `make lint` på det ferske resultatet gir null feil. Den committa
   `enhetsregisteret-bvrstiftelsesdokument-schema.yaml` er upåverka (`make lint` framleis
   grøn) sidan han alt hadde den handretta versjonen.
6. **Dokumentasjon oppdatert** — `src/mcp-linkml-modell-utkast/README.md` § "Typeomsetting"
   og § "Avgrensingar" forklarer no `allOf`-på-definisjonsnivå → `is_a`-mappinga, og
   skil ho tydeleg frå den framleis uendra eigenskapsnivå-avgrensinga.
   `specs/done/json-schema-roundtrip-test.md` er **ikkje** endra (arkiverte spec-ar i
   `specs/done/` skal stå urørte, jf. CLAUDE.md sitt DRY-unntak) — roundtrip-testen sitt
   `allOf`-unntak står difor framleis som før. Å utvide roundtrip-samanlikninga til òg å
   sjekke `allOf`-komponerte klassar er **ikkje utført** i denne omgangen; kan takast som
   eiga oppfølging om det trengst.
