# Plan: konsekvent `annotations.begrepsidentifikator` på alle klassar

## Bakgrunn

Brukaren ønskjer `annotations.begrepsidentifikator` konsekvent påført alle
klassar, og bad om ein plan for korleis dette kan gjennomførast — ikkje
utføring no. Dette er gap 5 i `standardetterleving.md`, og heng saman med
Digdir-regel 13 (Felles modelleringsregler).

## Presisert omfang

Per eksisterande regel i `.claude/rules/linkml-schema.md`:

> «AP-NO-profil-skjema skal ikkje ha `begrepsidentifikator` på klassane sine.
> Klassane der er definerte av W3C/EU-standardar (DCAT, SKOS o.l.), ikkje av
> norske omgrep i Felles begrepskatalog.»

Dette avgrensar omfanget til **domenemodell-skjema** — 29 skjemafiler under
`ngr/`, `fint/`, `oreg/`, `samt/`, `fair/`. AP-NO-profilane
(`src/linkml/ap-no/**`) og `referanse/`-testfikstura er eksplisitt
ekskluderte.

## Kartlagt status (2026-08-28)

Programmatisk gjennomgang av dei 29 domenemodell-skjemaa (463 ikkje-abstrakte
klassar totalt):

| Status | Tal klassar |
|---|---|
| **Manglar `begrepsidentifikator` heilt** | 327 |
| **Har `TODO`-plasshaldar** (frå `mcp-linkml-generator`-scaffolding) | 133 |
| **Har reell, registrert URI** | **3** (alle i `samt-bu`) |

Berre `samt-bu-schema.yaml` sine `Skole`/`Kommune`/`Fylke` har faktiske,
registrerte konsept-URI-ar i Felles Begrepskatalog i dag. Alt anna er anten
fråverande eller ein bokstaveleg `TODO`-streng.

### Fordelt på utgivarorganisasjon

| Organisasjon | Tal klassar i omfang | Skjema |
|---|---|---|
| Novari IKS | 188 | `fint-administrasjon`, `-arkiv`, `-common`, `-okonomi`, `-personvern`, `-ressurs`, `-utdanning` |
| Brønnøysundregistra | 177 | `enhetsregisteret-bvr*` (7 skjema), `register-over-aksjeeiere`, `javazonetalk`, `fair-metadata` |
| Kartverket | 58 | `ngr-adresse`, `ngr-eiendom` |
| Skatteetaten | 32 | `ngr-person` |
| KS Digital | 8 | `samt-bu` (5 attståande av 8) |
| Digitaliseringsdirektoratet | 0 | (ingen domenemodellar i omfang — berre AP-NO/modellkatalog, alt ekskludert) |

## Kritisk avgrensing — dette kan ikkje fullautomatiserast

`begrepsidentifikator` skal peike til eit **reelt, registrert konsept** i
Felles Begrepskatalog (`https://concept-catalog.fellesdatakatalog.digdir.no/collections/<UUID>/concepts/<UUID>`).
Å dikte opp UUID-ar ville vore verre enn inga URI — det ville sett falske,
daude lenkjer.

For å få ein reell URI må ein anten:

1. **Finne eit eksisterande konsept** som alt dekkjer omgrepet — søkbart via
   den offentlege lese-API-en (`https://data.norge.no/api/concepts/<id>`,
   søk via `data.norge.no/concepts` / SPARQL), **eller**
2. **Registrere eit nytt konsept** — dette krev innlogging med ID-porten hjå
   organisasjonen sin eigen samling i Felles Begrepskatalog
   (`registrering-begrep-api.fellesdatakatalog.digdir.no`), eit **menneskeleg,
   autentisert steg** som verken eg eller CI kan utføre. Dette er i tråd med
   «Pull, ikkje push»-prinsippet i CLAUDE.md — repoet skal ikkje sjølv skyve
   noko til eksterne register.

Konsekvens: eg kan gjere **søkje- og skrive-tilbake**-stega (3 og 5 under),
men **registrering av nye konsept (steg 4) må ei menneskeleg begrepsansvarleg
person hjå kvar organisasjon utføre**. Planen er difor lagt opp slik at det
eg kan gjere maskinelt er tydeleg skilt frå det som krev menneskeleg
handling.

## Føresetnad — organisasjonssamling i Felles Begrepskatalog

Før noko konsept kan registrerast, må organisasjonen ha ei eiga samling
oppretta i Felles Begrepskatalog (analogt med korleis publisering av
datasett krev eit registrert høstingsendepunkt, jf.
`specs/done/publisering-felles-begrepskatalog.md`). **Ukjend per i dag kva
organisasjonar som alt har dette** — første steg i planen er å avklare
dette per organisasjon, ikkje anta det finst.

## Framgangsmåte — fem fasar

### Fase 0 — Avklar føresetnad per organisasjon (menneskeleg, éin gong)

For kvar av dei fem organisasjonane med domenemodellar i omfang: stadfest om
dei har ei registrert samling i Felles Begrepskatalog, og identifiser kven
som er den formelle begrepsansvarlege kontaktpersonen. Utan dette kan ikkje
fase 4 (registrering) starte for den organisasjonen.

### Fase 1 — Byggje søkjeverktøy — **✅ utført 2026-08-28**

`mcp-linkml-begrep-utkast` genererte tidlegare berre utkast til **lokale**
begrep for `brreg-begrepskatalog` (mellombelse `begrep.brreg.no`-URI-ar) —
han søkte ikkje mot den nasjonale katalogen. Eit nytt MCP-verktøy,
**`sok_begrepskatalog`**, er no lagt til same server:

- `src/mcp-linkml-begrep-utkast/concept_search.py` — søkjelogikken (stdlib
  `urllib` åleine, ingen nye avhengigheiter)
- `src/mcp-linkml-begrep-utkast/server.py` — MCP-verktøydefinisjon
  (`TOOL_SOK_BEGREPSKATALOG`) og dispatch-handtering
  (`_handle_sok_begrepskatalog`)
- Kopla inn i `Dockerfile.mcp-linkml` og `Makefile` sin
  `LINKML_BEGREP_RUN`-monteringsliste
- Dokumentert i `src/mcp-linkml-begrep-utkast/README.md`

**Verkemåte** (stadfesta med `.claude/rules`-prinsippet «berre presise
treff, aldri tvinge fram svake treff», jf. `class_uri`-gjennomgangen):

1. Prøver først eksakt namnetreff på `skos:prefLabel`/`skos:altLabel` via
   SPARQL mot `sparql.fellesdatakatalog.digdir.no` — den pålitelege metoden
   som vart identifisert under Prioritet 1-arbeidet.
2. Fell tilbake til fritekstsøk mot
   `search.api.fellesdatakatalog.digdir.no/search/concepts` berre dersom
   ingen eksakt treff finst.
3. Returnerer **aldri** eit automatisk valt svar — kvart kandidat-treff må
   stadfestast av eit menneske (eller av meg, i ein LLM-styrt økt) mot
   klassen si eiga skildring før `uri`-en vert brukt som
   `begrepsidentifikator`.

**Verifisert** (bygd container + manuelle JSON-RPC-kall via
`podman run`, sjå commit-historikk for eksakte testmeldingar):

- `sok_begrepskatalog(term="kommune")` → eksakt treff, identisk URI og
  definisjon som alt brukt i `samt-bu-schema.yaml` sin `Kommune`-klasse.
- `sok_begrepskatalog(term="privat virksomhet")` → ingen eksakt treff, fell
  korrekt tilbake til fritekstsøk, returnerer synleg svake/irrelevante
  kandidatar (stadfestar at `PrivatVirksomhet` framleis manglar eit godt
  treff, konsistent med den manuelle undersøkinga i Prioritet 1).
- Manglande `term`-parameter → korrekt `-32602`-feil.
- `make mcp-linkml-begrep-utkast-smoke` — grøn.

### Fase 2 — Køyr søkjefasen, produser gap-liste — **✅ utført 2026-08-28**

Køyrde `concept_search.py` sitt eksakt-namnetreff-steg mot alle 326 klassar
som manglar `begrepsidentifikator` og har ei reell skildring (dei
resterande 137 av 463 er anten alt løyste, sjå Prioritet 1, eller manglar
skildring heilt og er difor ikkje søkbare enno). Full gap-liste, metode og
avgrensingar (inkl. ein datakvalitetsfeil oppdaga og retta i
`concept_search.py` undervegs — sjå detaljar der) er skrivne til
[`begrepsidentifikator-gap-liste-fase2.md`](begrepsidentifikator-gap-liste-fase2.md):

- **121 treff** (39 utan tvetydigheit, 53 med fleire kandidatar som krev
  eit medvite val — vel aldri automatisk) — klar for Fase 3.
- **205 ingen treff** — kandidatar for Fase 4 (nyregistrering).
- **130 ikkje søkte** — manglar reell skildring, treng det først.
- Fritekstsøk-fallback vart medvite **ikkje** køyrd i bulk (for støyete til
  å vere nyttig utan menneskeleg vurdering per treff) — tilgjengeleg
  individuelt via `sok_begrepskatalog` for enkeltklassar i Fase 3/4.

### Fase 3 — Menneskeleg stadfesting av treff (menneskeleg, per organisasjon)

Begrepsansvarleg hjå kvar organisasjon stadfester (eller avviser) kandidat-
treffa frå fase 2. Stadfesta treff kan gå rett til fase 5.

### Fase 4 — Registrer nye konsept (menneskeleg, per organisasjon)

For klassar utan treff: begrepsansvarleg registrerer nytt konsept i
organisasjonen sin samling via Digdir sitt registreringsgrensesnitt. Dette
er det klart største arbeidet i planen — potensielt fleire hundre nye
konsept — og bør **prioriterast og fordelast over tid**, ikkje forsøkt i
éin operasjon (sjå prioriteringsforslag under).

### Fase 5 — Skriv URI-ane attende til skjema (eg kan gjere dette)

Når ein URI er stadfesta (frå fase 3 eller 4), oppdaterer eg
`annotations.begrepsidentifikator` i skjemaet, validerer med
`make mcp-linkml-valider-modell POLICY=bronze` (regel 13-sjekken), og
oppdaterer `standardetterleving.md` gap 5 etter kvart som organisasjonar
fullfører sin del.

## Relatert tiltak — `class_uri` i `mcp-linkml-modell-utkast`

Same underliggjande problem for eit anna felt (`class_uri`, ikkje
`begrepsidentifikator`) er flytta til ein eigen spec:
[`mcp-modell-utkast-ekstern-class-uri.md`](mcp-modell-utkast-ekstern-class-uri.md).
Den specen føreslår eit tiltak som bør gjerast **etter** Fase 1 under, sidan
han kan gjenbruke søkjeverktøyet som vert bygd der.

## Prioriteringsforslag

Ikkje alle 463 klassar er like viktige å starte med. Forslag til rekkjefølgje:

1. **Fullfør `samt-bu`** (5 attståande av 8) — alt i gang, viser mønsteret,
   lågast innsats for å bli heilt ferdig med eitt skjema. **Delvis utført
   2026-08-28**, sjå eige avsnitt under.
2. **Skjema med `TODO`-plasshaldar** (133 klassar, 7 `oreg`-skjema) —
   annotasjonsfeltet finst alt strukturelt, berre verdien manglar. Byrjar
   ikkje frå botnen.
3. **Små, avgrensa skjema** (`fair-metadata` 5, `javazonetalk` 7) — låg
   innsats, gjev raskt heile skjema "ferdige" som bevis på konseptet.
4. **Store domenemodellar** (`fint-*` 188, NGR-familien 90,
   `register-over-aksjeeiere` 18) — planlegg som eit fleire-omgangar-arbeid
   per organisasjon, ikkje éin sprint.

## Prioritet 1 utført — `samt-bu` (2026-08-28)

Køyrde Fase 1+2 manuelt (utan å byggje det permanente verktøyet frå Fase 1
enno) mot dei to offentlege, uautentiserte lese-endepunkta som vart
identifiserte under research:

- **Søk (fritekst):** `POST https://search.api.fellesdatakatalog.digdir.no/search/concepts`
- **Presist oppslag (`skos:prefLabel`/`skos:altLabel`):** SPARQL mot
  `https://sparql.fellesdatakatalog.digdir.no` — vesentleg meir treffsikker
  enn fritekstsøket for å stadfeste/avkrefte eit *presist* namnetreff.

**Resultat — 4 av 5 fekk stadfesta, presist treff:**

| Klasse | Skildring i skjemaet | Funne konsept | `begrepsidentifikator` |
|---|---|---|---|
| `Fylke` | «...undernasjonalt, regionalt geografisk område» | `fylkeskommune` — «fylke som administrativ enhet» (same konsept-batch som `Kommune`, id-sekvensen `...f0` rett før `Kommune` sin `...f1`) | `.../collections/974761076/concepts/20b2e0f0-9fe1-11e5-a9f8-e4115b280940` |
| `Basisgruppe` | «Skoleklasse som hovedsaklig samler elever i ulike fag» | `skoleklasse` — «organisering av skoleelever på same alder... felles gruppeidentitet for eit skoleår» | `.../collections/964338531/concepts/3d7b34e4-37e3-4983-9d9b-c3adca56d6fa` |
| `Elev` | «En person som går på skole» | `skoleelev` (altLabel: elev) — «person som mottar undervisning... særlig i skole» | `.../collections/964338531/concepts/e6bfeb15-5a47-4e68-83cd-03b0710f89d6` |
| `Rektor` | «Høgaste akademiske leder av en skole» | `skoleleder` (altLabel: rektor) — «person som er skoleeiers ansvarlige representant på en skole» | `.../collections/964338531/concepts/29a768dc-ff38-4332-ac32-2aa0f1a7cb71` |

Alle fire er no skrivne til `annotations.begrepsidentifikator` i
`samt-bu-schema.yaml`. `make lint` og `make validate-instance` (mot
`samt-bu-eksempel.yaml`) er grøne.

**Ikkje funne — `PrivatVirksomhet`:** ingen presist treff i den harde
SPARQL-søket (verken `privat virksomhet` eksakt, eller brei
"privat"/"virksomhet"-søk). Dette krev truleg eit **nytt** konsept
registrert (Fase 4, menneskeleg) — ikkje eit hol i søkjemetoden. Attstår
til organisasjonen (KS Digital) prioriterer det.

**Merknad — metodenyanse oppdaga:** fritekstsøket
(`/search/concepts`) rangerer ikkje alltid det mest grunnleggjande omgrepet
øvst (t.d. gav søk på «kommune» **ikkje** sjølve `kommune`-konseptet blant
dei 10 øvste treffa, sjølv om det konseptet finst og er akkurat det
`Kommune`-klassen alt brukar). Presist SPARQL-oppslag på eksakt
`prefLabel`/`altLabel` var langt meir pålitande for å stadfeste/avkrefte
eit namnetreff, og bør vere primærmetoden i det permanente verktøyet frå
Fase 1 — fritekstsøket eignar seg betre som eit sekundært, breiare
kandidatsøk når det eksakte oppslaget ikkje gir treff.

## Rollefordeling — samandrag

| Steg | Kven |
|---|---|
| Fase 0: avklar org-samling | Menneskeleg (repo-eigar/kontakt per org) |
| Fase 1: byggje søkjeverktøy | Eg (kodeendring) — **✅ utført** |
| Fase 2: køyr søk, lag gap-liste | Eg (les-operasjon mot offentleg API) — **✅ utført** |
| Fase 3: stadfest treff | Menneskeleg (begrepsansvarleg per org) |
| Fase 4: registrer nye konsept | Menneskeleg (begrepsansvarleg per org, ID-porten) |
| Fase 5: skriv URI attende, valider | Eg (kodeendring) |

## Ikkje gjort i denne specen

Fase 3 (menneskeleg stadfesting av dei 121 treffa) og Fase 4 (nyregistrering
for dei 205 utan treff, inkl. `PrivatVirksomhet` frå Prioritet 1) er ikkje
starta. Fase 0 (avklar org-samling-status per organisasjon) er ikkje
gjennomført. Dei 130 klassane utan reell skildring er ikkje søkte — dei
treng skildring først. Individuelt fritekstsøk for klassar utan eksakt
treff (205 + 130) er heller ikkje gjort i bulk.

## Utført

Plan skriven 2026-08-28. Kartlegging av faktisk status (463 klassar i
omfang, 3 reelle/133 TODO/327 manglar, fordelt på 5 organisasjonar) og
femfase-framgangsmåte med tydeleg rollefordeling mellom automatiserbare og
menneskelege steg. Det relaterte `class_uri`-tiltaket for
`mcp-linkml-modell-utkast` er flytta til ein eigen spec,
`mcp-modell-utkast-ekstern-class-uri.md`, sidan det gjeld eit anna felt og
verktøy.

**Fase 1 utført 2026-08-28:** nytt MCP-verktøy `sok_begrepskatalog` lagt til
`mcp-linkml-begrep-utkast` — søkjer Felles Begrepskatalog (eksakt SPARQL-
oppslag, fritekst-fallback), returnerer aldri eit automatisk valt svar. Bygd,
testa (container + manuelle JSON-RPC-kall) og dokumentert. Sjå eige avsnitt
under Fase 1.

**Prioriteringsforslag tiltak 1 (`samt-bu`) delvis utført same dag:** 4 av 5
attståande klassar (`Fylke`, `Basisgruppe`, `Elev`, `Rektor`) fekk stadfesta,
presise `begrepsidentifikator`-URI-ar via offentlege, uautentiserte
lese-API-ar (fritekstsøk + SPARQL-oppslag mot Felles Begrepskatalog), skrivne
inn og validerte. `PrivatVirksomhet` fann ikkje noko presist treff og
attstår til menneskeleg nyregistrering (Fase 4).

**Fase 2 utført 2026-08-28:** batch-søk (`_exact_label_match`) køyrt mot
alle 326 søkbare klassar. Undervegs vart ein reell datakvalitetsfeil
oppdaga og retta i `concept_search.py` — den harvesta SPARQL-grafa
inneheldt namnetreff frå andre vokabular enn Felles Begrepskatalog
(LOS-ord, interne "subjects"-taggar), som feilaktig ville gitt 17 ugyldige
`begrepsidentifikator`-kandidatar. Etter fiksen: 121 treff (53 med fleire
kandidatar, krev medvite val), 205 utan treff, 130 ikkje søkte (manglar
skildring). Full gap-liste i eigen fil,
`specs/backlog/begrepsidentifikator-gap-liste-fase2.md`.
