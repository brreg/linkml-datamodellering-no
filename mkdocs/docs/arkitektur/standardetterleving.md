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
| [Tilgjengeliggjøring av åpne data](https://www.digdir.no/informasjonsforvaltning/tilgjengeliggjore-apne-data/2721) | ✅ | Delvis utført — nokre tiltak krev fagkunnskap frå den enkelte codeowner. |
| [Beskrivelse av kvalitet på datasett](https://www.digdir.no/informasjonsforvaltning/beskrivelse-av-kvalitet-pa-datasett/2570) | ✅ | Kvantifiserbare kvalitetsmål (DQV-AP-NO) implementert og utført. |
| [Internkontroll i praksis for informasjonssikkerheit](https://www.digdir.no/informasjonssikkerhet/internkontroll-i-praksis-informasjonssikkerhet/2601) | ⚪ | Organisatorisk styringsaktivitet — avgrensa direkte relevans for eit skjemabibliotek. Repoet har tilstøytande infrastruktur (trafikklyssystem-mapping, CODEOWNERS, SBOM/sikker CI). |
| [Veileder for informasjonsmodellar (ModellDCAT-AP-NO)](https://www.digdir.no/informasjonsforvaltning/veileder-informasjonsmodeller/2571) | ✅ | I hovudsak utført. |
| [Veileder for høsting og deling av språkdata](https://www.digdir.no/datadeling/sprakdata-korleis-kan-vi-hauste-og-dele/2367) | ⚪ | Relevant (`brreg-begrepskatalog` er eit omgrepsapparat), men eit eksplisitt bidrag til Språkbanken er ei publiseringsavgjerd for den enkelte codeowner, ikkje eit arkitekturgap. |

## Pilar 2 — Standarder og spesifikasjoner

| Ressurs | Status | Vurdering |
|---|---|---|
| DCAT-AP-NO | ✅ | Utført. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| SKOS-AP-NO Begrep | ✅ | I hovudsak utført. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| [Termlosen](https://www.digdir.no/informasjonsforvaltning/termlosen/2020) (omgrepsanalyse) | ✅ | I hovudsak utført. |
| [Forvaltningsstandard for begrepsharmonisering/-differensiering](https://www.digdir.no/standarder/forvaltningsstandard-omgrepsharmonisering-og-omgrepsdifferensiering/1683) | ⚪ | Prosessuell standard — `skos-ap-no-schema` sin `GeneriskRelasjon`-klasse gir den tekniske føresetnaden. |
| [TBX-AP-NO](https://www.digdir.no/standarder/tbx-ap-no-forvaltningsstandard-tilgjengeleggjering-av-omgrepsbeskrivingar-basert-pa-tbx/1684) | 🟡 | **Reelt gap:** ingen TBX-eksport for begrepskatalog-data (TBX er tilrådd, ikkje obligatorisk). |
| [Retningslinjer ved tilgjengeliggjøring av offentlege data](https://www.digdir.no/informasjonsforvaltning/retningslinjer-ved-tilgjengeliggjoring-av-offentlige-data/2722) | ✅ | Utført. |
| DQV-AP-NO | ✅ | Løyst. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| ModelDCAT-AP-NO | ✅ | Utført — delt i modell-/katalog-skjema. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| [Los](https://www.digdir.no/informasjonsforvaltning/los/2136) (klassifiseringsvokabular) | ✅ | Utført. |
| Standarder for URI-peikarar til offentlege ressursar | 🟡 | Delvis utført — 2 av 5 tiltak attståande, sjå [`avvik-peikarar-til-offentlege-ressursar.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/backlog/avvik-peikarar-til-offentlege-ressursar.md). |
| XKOS-AP-NO | ✅ | I hovudsak utført. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |
| CPSV-AP-NO *(ikkje lista på rammeverksida, same standardfamilie)* | ✅ | Utført. Sjå [AP-NO arkitektur og avvik](ap-no-arkitektur.md). |

## Pilar 3 — Informasjonsmodellar

| Ressurs | Status | Vurdering |
|---|---|---|
| [Ni designprinsipper for informasjonsmodellar](https://www.digdir.no/informasjonsforvaltning/prinsipper-informasjonsmodeller/3030) | ✅ | I hovudsak utført. |
| [Felles modelleringsregler for offentleg forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029) (15 reglar) | ✅ | Alle 15 reglar dekt av MCP-validatoren. Full sjekkliste med regel- og FAIR-mapping: [Valideringsreglar](valideringsregler.md). |
| [Person og Enhet — felles informasjonsmodell](https://www.digdir.no/informasjonsforvaltning/person-og-enhet-felles-informasjonsmodell/2018) | ⚪ | Sterkt samsvar i sak (alle kjernefelt representerte, oftast med større presisjon), men ingen 1:1-mapping — repoet sine `ngr-person`/`enhetsregisteret-bvrinn` er kjeldeautoritative registermodellar, ikkje ei forenkling. Tilsikta avvik, ikkje eit gap. |
| [Adresse — felles informasjonsmodell](https://www.digdir.no/informasjonsforvaltning/adresse-felles-informasjonsmodell/2019) | ⚪ | Sterkt strukturelt og semantisk samsvar med `ngr-adresse` (same autoritative kjelde: Kartverket/Matrikkelen/Posten). Eitt mindre presisjonsavvik, sjå gap-liste under. |

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
| 1 | Avklar `begrep.brreg.no`/`brreg.no/modellkatalogar/`-URI-ar og dokumenter URI-konstruksjonspolicy | [Standarder for URI-peikarar](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/backlog/avvik-peikarar-til-offentlege-ressursar.md) | Ope frå før |
| 2 | Vurder TBX-eksport for `brreg-begrepskatalog` | TBX-AP-NO | Middels — reelt, men valfritt format |
| 3 | Legg til `class_uri` på `Representasjonspunkt` i `ngr-adresse-schema.yaml` | Adresse — felles informasjonsmodell | Låg — presisjonsfiks |
| 4 | Dokumenter kryssreferanse til Digdirs Person/Enhet-modell i `description.md` for `ngr-person`/`enhetsregisteret-bvrinn` | Person og Enhet — felles informasjonsmodell | Låg — dokumentasjon |

Ingen av desse fire er brot på rammeverket — TBX og URI-policy er reelle,
avgrensa utvidingspunkt; dei to siste er presisjonsfiksar utan funksjonell
konsekvens.

---

## Sjå også

- [Valideringsreglar](valideringsregler.md) — full sjekkliste for dei 15 Digdir-modelleringsreglane og FAIR-prinsippa, med regel-for-regel-mapping til bronse/sølv/gull-policyane
- [AP-NO arkitektur og avvik](ap-no-arkitektur.md) — korleis DCAT-, SKOS-, ModelDCAT-, CPSV-, DQV- og XKOS-AP-NO er bygde opp i repoet
- [Publisering](../publisering/publisering-oversikt.md) — Digdir sin datatilbydar-sjekkliste og "Orden i eget hus"-trafikklyssystemet sett opp mot publiseringsflyten
- [Fullstendig kartlegging (kjeldespec)](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/rammeverk-informasjonsforvaltning.md) — den underliggande analysen denne sida er basert på, inkludert klasse-for-klasse-samanlikning for Person/Enhet og Adresse
- 18 detaljerte `avvik-*.md`-kartlegginger i [`specs/done/`](https://github.com/brreg/linkml-datamodellering-no/tree/main/specs/done) — éin per standard/veiledar
