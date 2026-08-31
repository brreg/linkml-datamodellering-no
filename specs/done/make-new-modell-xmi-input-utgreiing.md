# Utgreiing: `make new-modell` med XML/XMI-input (MagicDraw-eksport → LinkML)

## Bakgrunn

Under arbeidet med
`specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md` (BR sine
XMI-katalogar → felles-modellar for `oreg`-domenet) vart det gjort ei
eingongs, manuell ekstraksjon av klassar/typar frå fire MagicDraw-XMI-filer
med eit Python-script. Brukaren bad om ei utgreiing av om det tilsvarande
kan byggjast inn i verktøykjeda permanent: eit `XML=<sti>`-flagg til
`make new-modell` (i dag `DOMAIN=<domene> NAME=<modell>
[JSON_SCHEMA=<sti>]`, sjå `src/assets/scripts/scaffolding/new-modell.sh`)
som genererer eit LinkML-utkast direkte frå XMI, parallelt med
`JSON_SCHEMA=`-vegen som alt finst for JSON Schema.

Denne specen er **berre ei utgreiing** — ho implementerer ikkje flagget.
Avklaring 31.08.2026 (jf. søsterspecen sitt punkt 11) er å skilje
utgreiinga ut i denne eigne specen, slik at ho kan prioriterast/planleggjast
uavhengig av dei konkrete `brreg-felles-*`-modellane (som vart løyst
manuelt, ikkje via dette flagget).

## Korleis JSON_SCHEMA-vegen fungerer i dag

`new-modell.sh` byggjer ein MCP-førespurnad (`inputFormat: json-schema`)
som `src/mcp-linkml-modell-utkast/server.py` sender vidare til
`converter.py` sin `convert(json_schema, policy, ...)` (705 linjer
totalt). Der gjer tre funksjonar sjølve jobben: `_collect_types`,
`_collect_enums`, `_collect_classes` — dei gjer om JSON Schema sitt
`$defs`-tre til LinkML-shapa dict-ar. Resten av `convert()` (metadata,
prefiks, container-klasse, silver-annotasjonar, lisens-kommentar osv.,
~250 av 705 linjer) er **format-agnostisk** — han bryr seg ikkje om input
kom frå JSON Schema eller noko anna, berre om
`classes`/`types`/`enums`-dict-ane den mottek. `new-modell.sh` etterbehandlar
så resultatet (PascalCase-ing av klassenamn, container-klasse-konvensjon,
versjonslåst `dcat-ap-no`-import, silver-annotasjonar) — heilt uavhengig av
input-format.

## Vurdering: gjennomførbart, med moderat innsats

**Det som er lettare enn JSON Schema:**

- **Typemapping er nesten triviell.** BR sin `Løsningstypekatalog_v1`
  sin `Primitivtyper`-pakke er bokstaveleg tala XSD-innebygde typar
  (`anyURI`, `date`, `dateTime`, `decimal`, `int`, `boolean` osv.) — dette
  er akkurat `xsd:`-URI-ane `linkml:types` alt brukar, og akkurat mønsteret
  (`uri: xsd:string`, `base: str`) alle sju `enhetsregisteret-*`-skjema alt
  nyttar for eigendefinerte typar. Ingen format-inferens (slik JSON Schema
  treng for `format: date-time` osv.) er naudsynt.
- **Enum-ar er direkte:** `uml:Enumeration` sine `ownedLiteral`-born mappar
  1:1 til LinkML `permissible_values`, utan JSON-Schema sine
  `enum`-vs-`const`-vs-`oneOf`-varianter.
- **Kjeldesporing er gratis:** kvart element har eit stabilt `xmi:id` og
  (for kryss-fil-referansar) eit lesbart `referentPath`-attributt
  (t.d. `Strukturtypekatalog_v1::Enkeltyper::Organisasjonsnummer`) — kan
  skrivast direkte inn som kjeldekommentar i generert YAML, noko
  JSON Schema-vegen ikkje har noko tilsvarande for.

**Det som er vanskelegare enn JSON Schema:**

- **Kryss-fil-referansar.** BR sin eksport spreier eitt logisk
  modellprosjekt over fleire XMI-filer
  (`<type href='Strukturtypekatalog_v1.xml#…'>`, stadfesta empirisk under
  arbeidet med søsterspecen — `BRReferansemodell_v3.xml` sine klassar
  refererer typar definerte i `Strukturtypekatalog_v1.xml`). Eit generisk
  `XML=<éin fil>`-flagg ville feile å løyse desse utan tilgang til
  systerfilene. Treng anten fleire `--input-file`-argument (éin per
  XMI-fil i prosjektet) eller ein katalog-parameter (`--input-dir`) som
  skanner alle `.xml`-filer der for id→namn-oppslag før klassane vert
  emittert.
- **Pakkeval.** Ei enkelt XMI-fil kan innehalde fleire logisk usamanhengande
  pakkar som ikkje bør bli éin LinkML-modell (empirisk: `BRReferansemodell_v3.xml`
  inneheld både ein autoritativ `Adresse`/`Aktør`-modell og eit separat,
  uferdig `DigdirStandard`-utkastområde med kolliderande klassenamn). Treng
  eit `--xmi-package <sti>`-filter (t.d.
  `Model/BRReferansemodell_v3/Adresse`) for å kunne generere éin liten
  modell om gongen — utan dette ville flagget motverke prinsippet om mange
  små, målretta felles-modellar (jf. `felles-typar-enhetsregisteret-fra-br-katalogar.md`).
- **Fleirarv.** LinkML støttar berre éin `is_a`, men UML tillèt fleire
  `generalization`-ar (funne i praksis:
  `OffisiellAdresse extends Adresse, GeografiskAdresse` i
  `BRReferansemodell_v3.xml` sin `DigdirStandard`-pakke). Treng ein
  eksplisitt regel: første generalisering → `is_a`, resten → `mixins`, med
  ei åtvaring i output (same mønster som `_merge_allof_members` alt brukar
  for JSON Schema sin `allOf`-samansetjing — presedens finst i
  `converter.py`).
- **Diagram-støy.** Rå XMI-filer er dominerte av MagicDraw sitt
  diagramoppsett (empirisk: éi 4,4 MB fil inneheldt berre 39 reelle
  klassar) — ein XMI-parser må eksplisitt filtrere til
  `packagedElement`-born av typane
  `uml:Class`/`uml:Enumeration`/`uml:PrimitiveType`/`uml:DataType` og
  ignorere `ownedDiagram`/`diagramRepresentation`. Handterbart med stdlib
  `xml.etree.ElementTree` (verifisert i praksis, sjå § Verifisert
  prototype under) — **ingen** nye avhengigheiter naudsynt, konsistent med
  CLAUDE.md sitt prinsipp om ingen lokale avhengigheiter (køyring skjer
  uansett i podman-containeren til `mcp-linkml-modell-utkast`).

## Verifisert prototype

Under arbeidet med søsterspecen vart eit eingongs Python-script skrive og
verifisert mot alle fire XMI-filene: det bygde ein global id→namn-tabell
på tvers av filer (fyrste gjennomgang), følgde deretter
`<type href='<fil>#<id>'>`- og `<type xmi:idref='<id>'>`-referansar
(andre gjennomgang) for å emittere klassar/typar/enum-ar med fullt
oppløyste typenamn og `is_a`-arv. Dette stadfestar at kjernelogikken
(id-oppløysing, pakke-tre-vandring, filtrering av diagramstøy) er
triviell med stdlib åleine — kompleksiteten ligg i integrasjonen mot
`converter.py`/`server.py`-arkitekturen og MCP-grensesnittet, ikkje i
sjølve XMI-parsinga.

## Konklusjon og tilråding

**Gjennomførbart** som eit `--input-format xmi`-tillegg til den
eksisterande `converter.py`/`server.py`-arkitekturen: nye funksjonar
`_collect_types_xmi`/`_collect_classes_xmi`/`_collect_enums_xmi` parallelt
med dei JSON-Schema-spesifikke, resten av `convert()` gjenbrukt uendra.

**Naudsynt for eit fullverdig `make new-modell ... XML=<sti>`:**

1. Støtte for fleire input-filer eller ein input-katalog
   (kryss-fil-referansar)
2. Eit pakke-/sti-filter (`--xmi-package`)
3. Fleirarv → `mixins`-regel med åtvaring
4. Ein kort UML→LinkML-typemapping-tabell (XSD-primitivtypar → `linkml:types`)
5. Endringar i `server.py` sitt `inputFormat`-enum (`json-schema`, `empty`
   → legg til `xmi`) og i `mcp-build-modell-utkast-request.py`/
   `new-modell.sh` for å byggje/sende XMI-input i staden for/i tillegg til
   JSON Schema-strengen

**Estimert omfang:** samanliknbart med det eksisterande JSON-Schema-sporet
i `converter.py` (`_collect_*`-funksjonane er om lag 250 av 705 linjer),
pluss kryss-fil-oppløysinga og pakkefilteret som er heilt ny kompleksitet
utan noko JSON-Schema-motstykke.

**Tilråding:** implementer **ikkje** dette no. Verdien er bevist for eitt
konkret bruksdøme (BR sine fire katalogar, løyst manuelt i søsterspecen),
men repoet har i dag ingen andre kjende XMI-kjelder som ville dra nytte av
eit generisk flagg. Bygg det først når/dersom eit av desse inntreff:

- BR (eller ein annan kjelde) leverer fleire/oppdaterte XMI-katalogar og
  repoet får eit **gjentakande** behov for denne konverteringa (ikkje
  berre eingongs)
- Eit anna domene i repoet får ei tilsvarande MagicDraw/UML-kjelde å
  modellere frå

## Nummererte steg (dersom brukaren seinare vel å prioritere implementering)

1. Avklar med brukaren om triggeren over (gjentakande behov, ny kjelde)
   faktisk har inntruffe, og at implementering skal startast.
2. Legg til `xmi` i `valid_formats`/`inputFormat`-enum i
   `src/mcp-linkml-modell-utkast/server.py`.
3. Implementer `_collect_types_xmi`/`_collect_classes_xmi`/`_collect_enums_xmi`
   i `converter.py`, med kryss-fil-id-oppløysing og pakke-/sti-filter (jf.
   § Vurdering).
4. Implementer fleirarv → `mixins`-regelen med åtvaring i `warnings`-lista
   (same mønster som `_merge_allof_members`).
5. Utvid `mcp-build-modell-utkast-request.py` og `new-modell.sh` med
   `XML=<sti>[,<sti>...]`- og `XML_PACKAGE=<sti>`-parametrar, parallelt med
   `JSON_SCHEMA=`.
6. Test mot dei fire eksisterande XMI-filene i `src/tmp/` (som framleis
   ligg der, jf. avklaring i søsterspecen) som regresjonsgrunnlag —
   samanlikn generert output mot dei manuelt oppretta
   `brreg-felles-*`-skjemaa frå søsterspecen.
7. Oppdater `COMMANDS.md`/`CLAUDE.md` sine referansar til `make new-modell`
   med det nye flagget.
8. Etter gjennomføring: oppdater denne specen sin «Utført»-seksjon, generer
   commit-melding, og flytt specen til `specs/done/`.

## Akseptansekriterium

**For sjølve utgreiinga (denne specen sitt eige leveransemål):**
konklusjon og tilråding er dokumentert (over) — oppfylt ved oppretting av
denne specen.

**For ei eventuell seinare implementering** (berre dersom brukaren
prioriterer § Nummererte steg):

- `make new-modell DOMAIN=felles NAME=<modell> XML=<sti>` genererer eit
  gyldig, lint-reint LinkML-utkast frå ei XMI-fil.
- Genererte klassar/typar har kjeldekommentarar som viser opphavleg
  `referentPath`/`xmi:id`.
- Multiarv frå kjelda vert korrekt omforma til `is_a` + `mixins` med
  synleg åtvaring.

## Relaterte filer

- `src/mcp-linkml-modell-utkast/converter.py`,
  `src/mcp-linkml-modell-utkast/server.py` — eksisterande
  JSON-Schema→LinkML-generator, arkitekturen denne utgreiinga byggjer
  vidare på
- `src/assets/scripts/scaffolding/new-modell.sh`,
  `src/assets/scripts/makefile/mcp-build-modell-utkast-request.py`,
  `src/assets/scripts/makefile/mcp-extract-modell-utkast-response.py` —
  CLI-integrasjonen `JSON_SCHEMA=` går gjennom i dag
- `specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md` —
  søsterspecen der det konkrete bruksbehovet (og den manuelle prototypen)
  kom frå
- `src/tmp/BRProfilV2.xml`, `src/tmp/BRReferansemodell_v3.xml`,
  `src/tmp/Løsningstypekatalog_v1.xml`, `src/tmp/Strukturtypekatalog_v1.xml`
  — verifiseringsgrunnlag for ein eventuell implementering
