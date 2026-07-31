# Tillegg til spesifikasjon – forklarande ingress under nivå 2-overskrifter

## Formål

Store modellsider inneheld mange seksjonar med ulik målgruppe og ulik detaljgrad. For å redusere kognitiv belastning bør kvar nivå 2-seksjon få ein kort forklarande ingress rett under overskrifta.

Ingressen skal:

- forklare kva seksjonen viser
- forklare eventuelle avgrensingar
- beskrive forholdet til importerte modellar ved behov
- vere kort nok til å kunne skumlesast

Anbefalt lengde er 1–3 setningar.

---

## Om denne modellen

Anbefalt tekst:

Denne sida dokumenterer LinkML-modellen cpsv-ap-no, inkludert klassar, eigenskapar, datatypar, valideringsresultat og genererte artefakt. Informasjonen er generert automatisk frå schemaet og tilhøyrande byggeprosess.

---

## Modellmetadata

Anbefalt tekst:

Denne seksjonen viser sentrale metadata for modellen, inkludert versjon, status, lisens, identifikatorar og avhengigheiter. Verdiane er henta direkte frå schemaet.

---

## Avhengigheiter

Anbefalt tekst:

Denne modellen importerer og gjenbruker komponentar frå andre schema. Importerte klassar og eigenskapar kan vere synlege i diagram, valideringsrapportar og andre analysar sjølv om dei ikkje blir lista som lokale element i denne modellen.

---

## ER-diagram

Anbefalt tekst:

Diagrammet viser struktur og relasjonar mellom dei lokale klassane i modellen. Importerte klassar er som standard filtrerte bort for å gjere diagrammet enklare å lese.

---

## Datamodell

Anbefalt tekst:

Dette er den autoritative kjelda for modellen. Alle tabellar, diagram og artefakt på denne sida er genererte frå dette schemaet.

---

## Classes

Anbefalt tekst:

Denne oversikta viser berre klassar som er definerte lokalt i cpsv-ap-no. Klassar frå importerte modellar er ikkje inkluderte i teljinga, men kan vere refererte frå lokale klassar og kan inngå i valideringsresultat og diagram.

---

## Slots

Anbefalt tekst:

Denne oversikta viser eigenskapar som er brukte av lokale klassar i modellen. Nokre eigenskapar kan vere importerte frå andre schema sjølv om dei blir brukte lokalt.

---

## Enumerations

Anbefalt tekst:

Denne seksjonen viser kontrollerte verdiområde som er definerte eller brukte av modellen. Importerte enumerasjonar blir dokumenterte separat der det er relevant.

---

## Types

Anbefalt tekst:

Typar definerer primitive verdiformat som datoar, URI-ar, språkstrengar og andre grunnleggjande datatypar brukt i modellen. Mange av desse kjem frå LinkML eller importerte skjema.

---

## Subsets

Anbefalt tekst:

Subsets representerer klassifiseringar eller kravsnivå som blir brukte i modellen. For AP-NO-modellar vil dette typisk vere Obligatorisk, Anbefalt og Valgfri.

---

## Generated artifacts

Anbefalt tekst:

Denne seksjonen listar maskinlesbare artefakt som er genererte frå schemaet. Artefakta blir brukte til validering, integrasjon, dokumentasjon og kodegenerering.

---

## Valideringsresultat

Anbefalt tekst:

Valideringsrapporten viser i kva grad modellen etterlever definerte modelleringsreglar og kvalitetskrav. Resultata kan omfatte både lokale og importerte element avhengig av kva reglar som er evaluerte.

---

## Versjonslogg

Anbefalt tekst:

Versjonsloggen viser endringar mellom publiserte versjonar av modellen. Innhaldet blir generert frå prosjektets release-historikk.

---

## Kontakt

Anbefalt tekst:

Her finn du informasjon om forvaltningsansvarleg, kontaktpunkt og kanal for feilrapportering eller forslag til forbetringar.

---

## Utført

Alle ingressar lagt til i `src/assets/templates/docgen/index.md.jinja2` og `mkdocs/lib/sections/*.sh`:

**Jinja2-template (`index.md.jinja2`):**
- **Modellmetadata** — forklarer at seksjonen viser metadata henta frå schemaet
- **Classes** — presiserer at teljinga berre omfattar lokale klassar
- **Slots** — forklarer at eigenskapar kan vere importerte sjølv om dei vert brukte lokalt
- **Enumerations** — forklarer at seksjonen viser kontrollerte verdiområde
- **Types** — forklarer at typar kjem frå LinkML eller importerte schema
- **Subsets** — forklarer at subsets representerer kravsnivå

**Seksjonsscript (`mkdocs/lib/sections/`):**
- **Om denne modellen** (`om_denne_modellen.sh`) — forklarer at sida dokumenterer LinkML-modellen
- **Avhengigheiter** (`avhengigheiter.sh`) — forklarer at importerte komponentar kan vere synlege i diagram og rapportar
- **ER-diagram** (`er_diagram.sh`) — forklarer at diagrammet viser lokale klassar og at importerte er filtrerte bort
- **Datamodell** (`datamodell.sh`) — forklarer at schemaet er den autoritative kjelda
- **Generated artifacts** (`generated_artifacts.sh`) — forklarer at artefakta blir brukte til validering og integrasjon
- **Valideringsresultat** (`valideringsresultat.sh` og `generate-validation-md.py`) — forklarer at rapporten viser regeletterfølging
- **Versjonslog** (`versjonslog.sh`) — forklarer at loggen viser endringar mellom versjonar
- **Kontakt** (`kontakt.sh`) — forklarer at seksjonen inneheld kontaktinformasjon

Ingressane følgjer anbefalt lengde (1–3 setningar) og er plasserte rett under overskrifta før hovudinnhaldet. Alle ingressar brukar Markdown blockquote (`>`) for å skilje dei visuelt frå resten av innhaldet.
