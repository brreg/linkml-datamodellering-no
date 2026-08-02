# Vis policy og versjon i TOC-menyen

## Bakgrunn

Brukarar navigerer via TOC-menyen (Table of Contents) i mkdocs-portalen. I dag ser ein:

```
- Modellmetadata
- Valideringsresultat
```

For å sjå modellversjon eller valideringspolicy må ein skrolle ned til respektive seksjonar og lese innhaldet. Dette gjer det vanskeleg å få rask oversikt over kva versjon/policy som gjeld når ein blar mellom ulike modellar.

## Føremål

Gjere modellversjon og valideringspolicy synleg i TOC-menyen utan å måtte skrolle ned til seksjonsinnhald.

## Foreslått løysing

Legg til metadata i overskriftene slik at TOC viser:

```
- Modellmetadata (v1.9.0)
- Valideringsresultat (silver)
```

eller alternativt (dersom begge set i same overskrift er ønskjeleg):

```
- Datamodell (v1.9.0)
- Valideringsresultat (silver)
```

## Evaluering

### Fordelar

1. **Raskare informasjon:** Modellversjon og valideringspolicy synlege i TOC utan skrolling
2. **Enklare samanlikning:** Når ein har fleire modellar opne i faner, ser ein raskt versjon/policy i menyen
3. **Konsistent plassering:** Informasjonen er alltid i same plass i TOC-menyen
4. **Minimalt redundans:** Informasjonen eksisterer allereie i seksjonsinnhald — dette er kun synleggjering i TOC
5. **Ingen endring i innhald:** Seksjonsinnhald beheld all detaljar (tabellane osv.)

### Ulemper / Risikoar

1. **Lengre TOC-linjer:** Kan gjere TOC-menyen meir rotuleg dersom mange overskrifter får suffiks
2. **Redundans i visuell presentasjon:** Samme informasjon både i TOC-linje og i seksjonsinnhald
3. **Inkonsistent med andre seksjonar:** Andre seksjonar (`## Classes`, `## Slots`) har ikkje metadata i overskrifta
4. **Badge-alternativ:** Versjon og policy er allereie synlege i badge-radene øvst på sida:
   ```
   [![Versjon](https://img.shields.io/badge/versjon-1.9.0-blue)]()
   [![Validering](https://img.shields.io/badge/silver-16_feil-yellow)]()
   ```
   Dette gjev same informasjon utan å endre overskrifter

### Alternativ løysing: Utvid badge-rad

I staden for å endre overskrifter, kan badge-rada gjeras meir framtredande:

- Plasser badge-rada direkte under hovudoverskrifta (`# samt-bu`)
- Bruk større badge-font (via custom CSS)
- Legg til anker i badges som hopper til relevante seksjonar

Dette gjev same rask tilgang til info utan å endre TOC-strukturen.

### Alternativ løysing: Sticky header med metadata

Lag ein sticky header på kvar modellside som viser versjon/policy medan ein skrollar. Dette gjev alltid synleg info utan å endre TOC.

## Tilråding

**IKKJE IMPLEMENTER** metadatasuffiks i overskriftene av følgjande grunnar:

1. **Badge-rada gjev same informasjon** — allereie tilgjengeleg øvst på sida utan skrolling
2. **Inkonsistent med andre seksjonar** — Classes, Slots, Types har ikkje suffiks, berre talet i parentes
3. **Visuell rotugling i TOC** — suffiks på berre to av ti seksjonar bryt mønsteret
4. **Redundans** — same info både i badge, i TOC-linje og i seksjonsinnhald

**Alternativ tiltak (dersom rask tilgang til policy/versjon er eit problem):**

- Utvid badge-rada med tydelegare design (font/farge)
- Legg til anker frå badges til respektive seksjonar (`#metadata`, `#valideringsresultat`)
- Vurder sticky header med versjon/policy for modellar med mykje innhald

## Konklusjon

Etter evaluering er tilrådinga å **IKKJE implementere** suffiks i overskriftene. Badge-rada gjev allereie rask tilgang til versjon og policy utan å måtte skrolle, og å legge til suffiks i overskriftene vil skape inkonsistens i TOC-menyen og redundans i visuell presentasjon.

Dersom det oppstår konkret tilbakemelding frå brukarar om at badge-rada ikkje er synleg nok, kan ein vurdere alternativ løysing (større badge-font, sticky header osv.) i staden for å endre overskriftsstrukturen.

## Utført

Specen konkluderer med å ikkje implementere endringa. Ingen kodefiler vert endra.

**Dato:** 2026-08-02  
**Beslutning:** Beheld noverande overskriftsstruktur. Badge-rada gjev allereie synleg versjon/policy-informasjon.
