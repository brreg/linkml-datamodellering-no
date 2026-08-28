# Standardetterleving

!!! note "Beskrivelse"

    Denne sida kartlegg korleis repoet realiserer og etterlever
    [Digdirs Rammeverk for informasjonsforvaltning](https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626)
    — dei norske veiledarane, standardane og felles informasjonsmodellane som
    styrer korleis offentleg sektor skal modellere og dele data. Repoet har
    som eksplisitt mål å vere eit nasjonalt verktøy for dette rammeverket
    (jf. [SCOPE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/SCOPE.md)).

Rammeverket er strukturert i tre pilarar pluss fire kjerneprinsipp. Tabellane
under viser status per ressurs, med lenkje til meir detaljert kartlegging der
dette finst.

**Statusteikn:** ✅ kartlagt og i hovudsak dekt · 🟡 kartlagt, delvis attståande
tiltak · ⚪ kartlagt, avgrensa/ingen teknisk relevans for eit delt verktøyrepo

---

## Pilar 1 — Veiledere

| Ressurs | Status | Vurdering |
|---|---|---|
| [Orden i eget hus](https://www.digdir.no/informasjonsforvaltning/orden-i-eget-hus/2115) | ✅ | Repoet understøttar kartleggings-/beskrivingsstega med skjemabibliotek, validering og publisering — sjølve forankring/prioritering/tilgangsvurdering er verksemda sitt ansvar. Sjå [Publisering — Digdir sin datatilbydar-sjekkliste](../publisering/publisering-oversikt.md). |
| [Modenhetsmodell for orden i eget hus](https://www.digdir.no/informasjonsforvaltning/modenhetsmodell-orden-i-eget-hus/2124) | ⚪ | Sjølvvurderingsverktøy for ei einskild verksemd — ikkje direkte aktuelt for eit delt verktøyrepo, men repoet hevar modenheita for verksemder som tek det i bruk. |
| [Tilgjengeliggjøring av åpne data](https://www.digdir.no/informasjonsforvaltning/tilgjengeliggjore-apne-data/2721) | ✅ | Utført for kjernekrava (lisens, format, nedlasting, faste identifikatorar). Alle 6 organisasjonar har no eigen modellkatalog med reelle oppføringar (var 2 av 21 skjema ved førre kartlegging). Attverande, låg prioritet: ingen live spørjbar API (berre statiske filer), inga aktiv brukaroppmuntring/-undersøking — sjå [`avvik-veileder-apne-data.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/avvik-veileder-apne-data.md). |
| [Beskrivelse av kvalitet på datasett](https://www.digdir.no/informasjonsforvaltning/beskrivelse-av-kvalitet-pa-datasett/2570) | ✅ | Kvantifiserbare kvalitetsmål (DQV-AP-NO) implementert og utført. `make gen-dqv-measurements` verifisert fungerande for alle 7 datafiler (begrepskatalog + 6 modellkatalogar): nøkkelnamn-mismatchen `data_policy`/`validation_policy` er retta, `kvalitetsmaalingar`-attributtet er lagt til dei 5 modellkatalog-skjema som mangla det, og `brreg-begrepskatalog.yaml` har fått attende sin `samlingar:`-container (gjenoppretta frå historiske, verifiserte verdiar). Rotårsaka — at både `collect-concepts.py` og `generate-modellkatalog.py` gjorde full filoverskriving og difor viska ut DQV-data ved kvar regenerering — er retta til å bevare eksisterande `kvalitetsmaalingar`/`samlingar` på tvers av køyringar. Sjå [`fiks-dqv-measurements-data-policy-nokkel.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/fiks-dqv-measurements-data-policy-nokkel.md) og [`fiks-dqv-gap-7a-7b.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/fiks-dqv-gap-7a-7b.md). |
| [Internkontroll i praksis for informasjonssikkerheit](https://www.digdir.no/informasjonssikkerhet/internkontroll-i-praksis-informasjonssikkerhet/2601) | ⚪ | Organisatorisk styringsaktivitet — avgrensa direkte relevans for eit skjemabibliotek. Repoet har tilstøytande infrastruktur (trafikklyssystem-mapping, CODEOWNERS, SBOM/sikker CI). |
| [Veileder for informasjonsmodellar (ModellDCAT-AP-NO)](https://www.digdir.no/informasjonsforvaltning/veileder-informasjonsmodeller/2571) | ✅ | Utført — 23 informasjonsmodellar registrerte på tvers av 6 organisasjonskatalogar, versjon/status synkronisert, og modellelement (Objekttype/Attributt/Assosiasjon/Kodeliste) eksponert for maskinhausting. Sjå [`avvik-veileder-modelldcat-ap-no.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/avvik-veileder-modelldcat-ap-no.md). |
| [Veileder for høsting og deling av språkdata](https://www.digdir.no/datadeling/sprakdata-korleis-kan-vi-hauste-og-dele/2367) | ⚪ | Relevant (`brreg-begrepskatalog` er eit omgrepsapparat), men eit eksplisitt bidrag til Språkbanken er ei publiseringsavgjerd for den enkelte codeowner, ikkje eit arkitekturgap. |

## Pilar 2 — Standarder og spesifikasjoner

| Ressurs | Status | Vurdering |
|---|---|---|
| DCAT-AP-NO | ✅ | Utført — DA1-DA5 (bugfix, seks nye valfrie slots) implementerte og verifiserte. Eitt attverande punkt: DA6 (verifiser at `data.norge.no/organizations/<orgnr>`-mønsteret vert korrekt oppløyst av Felles datakatalog) er ikkje utført. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| SKOS-AP-NO Begrep | ✅ | I hovudsak utført (SK1-SK4 + SK5 Forslag A). Attverande: SK5 Forslag B (full språktagging av `LangString` på tvers av AP-NO) er medvite deferert, ingen spec oppretta enno; Avvik 8/9 (`relasjontype`/`verdiomrade`-range) er ikkje adresserte. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| [Termlosen](https://www.digdir.no/informasjonsforvaltning/termlosen/2020) (omgrepsanalyse) | ✅ | Utført — TL1-TL3 implementerte: `relasjontype.range` endra til `Konsept` (strukturert Termlosen-typologi for assosiative relasjonar), `kjelde_tekst` lagt til for ikkje-URI-kjelder (trykte lover/standardar), og dei tre manglande samsvarsprediketa (`breitt_samsvar`/`smalt_samsvar`/`relatert_samsvar`) lagt til på `Begrep`. Illustrasjon av omgrepssamanhengar er dekt av generert `gen-doc`/`gen-erdiagram`-dokumentasjon. Éin avgrensa punkt medvite utsett: TL4 (SHACL-regex-sjekk for dårlege definisjonsmønster som «som er»/«betegnar») er ikkje implementert — kryssreferert til det tilsvarande utsette punktet SK5 Forslag B for SKOS-AP-NO. Prosess- og tekstkvalitetskrav (arbeidsgruppestorleik, definisjonsutforming) er medvite halde utanfor skjemaet, sidan dei ikkje er datastrukturkrav. Sjå [`avvik-termlosen.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/avvik-termlosen.md). |
| [Forvaltningsstandard for begrepsharmonisering/-differensiering](https://www.digdir.no/standarder/forvaltningsstandard-omgrepsharmonisering-og-omgrepsdifferensiering/1683) | ⚪ | Prosessuell standard — `skos-ap-no-schema` sin `GeneriskRelasjon`-klasse gir den tekniske føresetnaden. |
| [TBX-AP-NO](https://www.digdir.no/standarder/tbx-ap-no-forvaltningsstandard-tilgjengeleggjering-av-omgrepsbeskrivingar-basert-pa-tbx/1684) | 🟡 | **Reelt gap:** ingen TBX-eksport for begrepskatalog-data (TBX er tilrådd, ikkje obligatorisk). |
| [Retningslinjer ved tilgjengeliggjøring av offentlege data](https://www.digdir.no/informasjonsforvaltning/retningslinjer-ved-tilgjengeliggjoring-av-offentlige-data/2722) | ✅ | Utført — alle 4 tiltak (RÅ1-RÅ4) implementerte og validerte (inkl. `distribusjon_lisens` silver-sjekk). Avvik 7 (strukturgap for ikkje-opna datasett) hadde ingen tilrådd tiltak i den opphavlege kartlegginga og er difor ikkje adressert. |
| DQV-AP-NO | ✅ | Løyst — alle 6 tiltak (DQ1-DQ6) utførte (`Standard` flytta til `dcat-ap-no`, `har_verdi` delt i typa varianter, `DqvMotivasjon`-enum lagt til). Éin kjend avgrensing: `har_maal.range` er `uriorcurie` (ikkje `KatalogisertRessurs` som opphavleg planlagt) pga. LinkML-avgrensing på slot_usage-narrowing — instansdata er upåverka. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| ModelDCAT-AP-NO | ✅ | Utført — delt i modell-/katalog-skjema (MC8-MC11 dedup fullført, ingen duplikate klasser att). Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| [Los](https://www.digdir.no/informasjonsforvaltning/los/2136) (klassifiseringsvokabular) | ✅ | Utført — alle 5 tiltak (LO1-LO5), inkl. datafeil-/dokumentasjonsavvik, retta. |
| Standarder for URI-peikarar til offentlege ressursar | 🟡 | Delvis utført — 4 av 6 punkt framleis opne: (1) `begrep.brreg.no`-instans-URI-ar løyser ikkje opp, (2) `brreg.no/modellkatalogar/`-URI-ar løyser truleg ikkje opp, (3) schema-ID-ar manglar content negotiation (returnerer HTML, ikkje RDF), (4) ingen dokumentert URI-konstruksjonspolicy. Sjå [`avvik-peikarar-til-offentlege-ressursar.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/backlog/avvik-peikarar-til-offentlege-ressursar.md). |
| XKOS-AP-NO | ✅ | I hovudsak utført — 11 av 13 avvik retta (XK1-XK11). Det gjenverande punktet er eit dokumentert designval (bruk av `dct:temporal` framfor `schema:validFrom`/`schema:validThrough`), ikkje eit uløyst avvik. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| CPSV-AP-NO *(ikkje lista på rammeverksida, same standardfamilie)* | ✅ | Utført — alle 5 avvik retta: `Regel`-klassen fekk korrekt obligatorisk-nivå på `tittel`/`beskrivelse`/`identifikator_literal`, og ny `LovpaalagdTjeneste`-klasse (`cpsvno:StatutoryService`) med `realiserer`-slot lagt til. 19 klassar totalt. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |

## Pilar 3 — Informasjonsmodellar

| Ressurs | Status | Vurdering |
|---|---|---|
| [Ni designprinsipper for informasjonsmodellar](https://www.digdir.no/informasjonsforvaltning/prinsipper-informasjonsmodeller/3030) | ✅ | 7 av 9 prinsipp fullt dekt. To attverande punkt: `begrepsidentifikator` manglar konsekvent på domenemodell-klassar utanfor `oreg/*` (P3 Terminologi, sjå gap 5), og ingen eksplisitt `owl:sameAs`/kryssreferanse for semantisk overlappande klassar på tvers av NGR/DCAT/FINT (P6 Gjenbruk, sjå gap 6, låg prioritet). FINT-skjema over 50-klassegrensa (P7) er eit akseptert avvik, ikkje eit gap. Full prinsipp-for-prinsipp-vurdering: [`avvik-prinsipper-informasjonsmodeller.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/avvik-prinsipper-informasjonsmodeller.md). |
| [Felles modelleringsregler for offentleg forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029) (15 reglar) | ✅ | Alle 15 reglar er adresserte av MCP-validatoren — 11 med automatisk bronse/sølv-sjekk, 4 (Visualisering, Sammenhenger, Gjenbruk, Datatyper) via verktøy/konvensjon/manuell gjennomgang. Faktisk etterleving varierer: `begrepsidentifikator` (regel 13) manglar på 30/43 skjema (sjå gap 5 under). Full sjekkliste: [Valideringsreglar](valideringsregler.md). |
| [Person og Enhet — felles informasjonsmodell](https://www.digdir.no/informasjonsforvaltning/person-og-enhet-felles-informasjonsmodell/2018) | ⚪ | Sterkt samsvar i sak (alle kjernefelt representerte, oftast med større presisjon), men ingen 1:1-mapping — repoet sine `ngr-person`/`enhetsregisteret-bvrinn` er kjeldeautoritative registermodellar, ikkje ei forenkling. Tilsikta avvik, ikkje eit gap. |
| [Adresse — felles informasjonsmodell](https://www.digdir.no/informasjonsforvaltning/adresse-felles-informasjonsmodell/2019) | ⚪ | Sterkt strukturelt og semantisk samsvar med `ngr-adresse` (same autoritative kjelde: Kartverket/Matrikkelen/Posten). Eitt attverande presisjonsavvik: `Representasjonspunkt` har eit lokalt `class_uri` (`ngr:Representasjonspunkt`) i staden for ein standard geometrivokabular-URI, sjølv om skjemaet alt importerer både `locn:` og `geo:` (geosparql) — sjå gap 3 under. |

## Kjerneprinsipp

| Prinsipp | Vurdering |
|---|---|
| **Orden i eget hus** | Repoet gir verktøya (skjemabibliotek, validering, publisering) som kartleggings-/beskrivingssteget i veilederen treng, men kan ikkje utføre forankring, prioritering eller tilgangsvurdering for ei einskild verksemd — det er per design, sidan repoet er eit delt verktøy (jf. [SCOPE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/SCOPE.md)). |
| **«Kun én gang»-prinsippet** | Sterkt implementert gjennom import-hierarkiet (klasser/slots definert éin stad, importert nedover — sjå [Importhierarki](importhierarki.md)) og lenkingsprinsippet (URI-referansar mellom instansar i staden for duplisering). |
| **Maskinell datautveksling** | Kjernen i verktøykjeda: LinkML genererer RDF/TTL, JSON-LD, JSON Schema, SHACL, OWL, PlantUML/ER-diagram og fleire andre format frå éi kjelde. |
| **Felles standardar** | Repoet er i stor grad ein samling implementasjonar av DCAT-AP-NO, SKOS-AP-NO, ModelDCAT-AP-NO, DQV-AP-NO, XKOS-AP-NO, CPSV-AP-NO og Los. |

---

## Attverande gap

| # | Gap | Kjelde | Prioritet |
|---|---|---|---|
| 1 | Løys 4 opne punkt: `begrep.brreg.no`- og `brreg.no/modellkatalogar/`-URI-ar løyser ikkje opp, schema-ID-ar manglar content negotiation (HTML i staden for RDF), ingen dokumentert URI-konstruksjonspolicy | [Standarder for URI-peikarar](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/backlog/avvik-peikarar-til-offentlege-ressursar.md) | Ope frå før |
| 2 | Vurder TBX-eksport for `brreg-begrepskatalog` | TBX-AP-NO | Middels — reelt, men valfritt format |
| 3 | Bruk ein standard geometrivokabular-URI (`locn:geometry`/`geo:Geometry`) på `Representasjonspunkt` i `ngr-adresse-schema.yaml` i staden for det lokale `ngr:`-prefikset | Adresse — felles informasjonsmodell | Låg — presisjonsfiks |
| 4 | Dokumenter kryssreferanse til Digdirs Person/Enhet-modell i `description.md` for `ngr-person`/`enhetsregisteret-bvrinn` | Person og Enhet — felles informasjonsmodell | Låg — dokumentasjon |
| 5 | Legg til `annotations.begrepsidentifikator` på nøkkelklassar i `ngr-*`, `fint-*` og AP-NO-profilane (finst i dag berre i `oreg/*` og `samt-bu`, 13/43 skjema totalt) | Ni designprinsipper (P3) / Felles modelleringsregler (regel 13) | Middels — krev begrepskatalog-avklaring per klasse |
| 6 | Dokumenter `owl:sameAs`/`skos:exactMatch`-kryssreferanse for semantisk overlappande klassar (t.d. NGR `Virksomhet`/DCAT `Aktor`/FINT-tilsvarande) | Ni designprinsipper (P6 Gjenbruk og utveksling) | Låg — relevant fyrst ved konkret modell-integrasjon |
| 7 | ~~Nøkkelnamn-mismatch, manglande `samlingar`-container og manglande `kvalitetsmaalingar`-attributt i DQV-verktøykjeda~~ | Beskrivelse av kvalitet på datasett | **Lukka** |
| 8 | Vurder å faktorisere `ModellkatalogContainer` (nær-identisk på tvers av 6 modellkatalog-skjema) til eit delt importert basisskjema (DRY) | Ni designprinsipper (P7 Modularitet) | Låg — funksjonelt ufarleg, reint vedlikehaldspoeng |
| 9 | ~~Dei 6 modellkatalog-datafilene var utdaterte, og generatorane hadde eit namnemønster-avvik (`<schema>#Klasse` vs. `<schema>/Klasse`) som ville skapt daude referansar ved regenerering~~ | [`modellkatalog-datadrift-undersokt.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/modellkatalog-datadrift-undersokt.md) | **Lukka — org_uri-basert URI er no fasit for alle 6 org** |
| 10 | `digdir-modellkatalog.yaml` har 3 daude `inneholder_modellelement`-referansar til ei `katalog`-informasjonsmodell-oppføring utan tilhøyrande skjema i `gen-modelldcat-elements.py` (funne under gap 9-arbeidet, uavhengig av URI-migreringa) | ModelDCAT-AP-NO / modellkatalog | Låg — datakvalitetsfeil, ikkje strukturelt |

Gap 1, 2, 5, 6 og 10 er reelle, avgrensa utvidingspunkt eller feil; gap 3 og 4
er presisjonsfiksar utan funksjonell konsekvens. Gap 7 (nøkkelnamn-mismatch i
`gen-dqv-measurements.py`, manglande `samlingar`-container i
`brreg-begrepskatalog.yaml`, og manglande `kvalitetsmaalingar`-attributt i 5
modellkatalog-skjema) og gap 9 (modellkatalog-datadrift og URI-policy) er
lukka — sjå `specs/done/fiks-dqv-measurements-data-policy-nokkel.md`,
`specs/done/fiks-dqv-gap-7a-7b.md` og `specs/done/modellkatalog-datadrift-undersokt.md`.
Gap 8 er eit nytt, lågt prioritert
vedlikehaldspoeng avdekt undervegs i den fiksen.

---

## Sjå også

- [Valideringsreglar](valideringsregler.md) — full sjekkliste for dei 15 Digdir-modelleringsreglane og FAIR-prinsippa, med regel-for-regel-mapping til bronse/sølv/gull-policyane
- [AP-NO arkitektur og avvik](ap-no-arkitektur.md) — korleis DCAT-, SKOS-, ModelDCAT-, CPSV-, DQV- og XKOS-AP-NO er bygde opp i repoet
- [Publisering](../publisering/publisering-oversikt.md) — Digdir sin datatilbydar-sjekkliste og "Orden i eget hus"-trafikklyssystemet sett opp mot publiseringsflyten
- [Fullstendig kartlegging (kjeldespec)](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/rammeverk-informasjonsforvaltning.md) — den underliggande analysen denne sida er basert på, inkludert klasse-for-klasse-samanlikning for Person/Enhet og Adresse
- 18 detaljerte `avvik-*.md`-kartlegginger i [`specs/done/`](https://github.com/brreg/linkml-datamodellering-no/tree/main/specs/done) — éin per standard/veiledar
