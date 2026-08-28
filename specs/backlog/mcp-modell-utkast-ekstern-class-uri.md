# Oppdater `mcp-linkml-modell-utkast` til å søkje `class_uri` frå eksterne kjelder

## Bakgrunn

Under `class_uri`-gjennomgangen (`specs/done/undersokelse-class-uri-kryssreferansar.md`)
retta me 24 klassar i 10 skjema til verifiserte eksterne vokabular-ekvivalentar,
og la ein ny konvensjonsregel i `.claude/rules/linkml-schema.md`: ekstern
ekvivalent er føretrekt bruk av `class_uri`, lokalt prefiks berre som
fallback.

Denne fiksen retta berre **eksisterande** klassar. Skaffoldingsverktøyet
som genererer **nye** skjema (`mcp-linkml-modell-utkast`) følgjer ikkje den
nye regelen — det genererer i dag alltid eit lokalt `class_uri`, aldri eit
forslag til ekstern vokabular-ekvivalent. Utan denne fiksen vil kvart nytt
skjema oppretta via `make mcp-linkml-modell-utkast SCHEMA=<sti>` (eller
`make new-modell JSON_SCHEMA=<sti>`, same konverteringsmotor) automatisk
skape nye, retrofit-trengande `class_uri`-tilfelle — akkurat det me nettopp
brukte tre forskingsagentar på å rydde opp i for dei 296 eksisterande
klassane.

Denne specen vart opphavleg skriven som eit avsnitt i
`specs/backlog/plan-konsekvent-begrepsidentifikator.md`, men er flytta til
ein eigen spec sidan ho gjeld eit anna felt (`class_uri`, ikkje
`annotations.begrepsidentifikator`) og eit anna verktøy.

## Kjelde til fiksen

`src/mcp-linkml-modell-utkast/converter.py`, linje 487:

```python
entry["class_uri"] = f"{prefix_name}:{_transliterate(cls_name)}"
```

Dette set alltid `class_uri` til skjemaet sitt eige lokale prefiks, uansett
klassenamn eller skildring.

## Forslag til fiks

1. Ved generering: for kvar klasse, søk klassenamnet (+ eventuell
   skildring/JSON Schema-`description`) mot dei same vokabulara som vart
   brukt i `class_uri`-gjennomgangen — EU sine kjernevokabular (Core Person,
   Core Location `locn:`, Core Business/Registered Organization `rov:`),
   W3C (`org:`, `foaf:`, `prov:`, `vcard:`, `time:`), og `schema.org` — i
   tillegg til allereie kjende, i-repoet-brukte AP-NO-vokabular der
   relevant.
2. **Ikkje** godta svake/omtrentlege treff automatisk — same prinsipp som i
   `.claude/rules/linkml-schema.md` sin nye regel: berre eit presist treff
   skal setjast automatisk. Uklare/moderate treff bør markerast med ein
   `# TODO: vurder ekstern class_uri-kandidat: <prefix:Klasse>`-kommentar i
   staden for å bli sett direkte, slik at eit menneske stadfestar før
   commit.
3. Fell tilbake til dagens åtferd (lokalt prefiks) når ingen treff finst —
   dette er den korrekte, tilsikta bruken av fallback-mønsteret, ikkje eit
   mellombels hol.
4. Dette krev ei liknande, men **separat**, søkje-evne frå det som er
   planlagt i `plan-konsekvent-begrepsidentifikator.md` sin Fase 1 (som
   søkjer Felles Begrepskatalog for `begrepsidentifikator`) —
   `class_uri`-kandidatar hentast frå RDF-vokabularregister (W3C/EU), ikkje
   frå Digdir sin konseptkatalog. Vurder om dei to søkjefunksjonane kan dele
   eit felles hjelpebibliotek (`src/assets/scripts/utils/`) for å unngå
   duplisering (DRY-prinsippet i CLAUDE.md), sjølv om kjeldene dei søkjer
   mot er ulike.
5. Oppdater `annotations.begrepsidentifikator: TODO`-generering (same fil)
   til òg å kunne kalle søkjeverktøyet frå `plan-konsekvent-begrepsidentifikator.md`
   sin Fase 1 når det finst, av same grunn — nye skjema bør ikkje starte med
   same TODO-gjeld som dei 133 `oreg`-klassane har i dag.

## Rekkjefølgje

Dette tiltaket bør gjerast **etter** Fase 1 i
`plan-konsekvent-begrepsidentifikator.md` (søkjeverktøyet for
`begrepsidentifikator`) er bygd, sidan punkt 5 over kan gjenbruke det
direkte.

## Ikkje gjort

Dette er ein spec/plan, ikkje ei utføring. Ingen kode i
`src/mcp-linkml-modell-utkast/` er endra enno.

## Utført

_(fyllast ut når fiksen er implementert)_
