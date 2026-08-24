# Arkitektur

!!! note "Beskrivelse"

    Denne sida gir oversikt over korleis repoet er bygd opp — frå importhierarkiet
    mellom skjema, via valideringsreglar, til dei strukturelle vala som er tekne
    i AP-NO-profilane og korleis andre repo kan gjenbruke dei.

| Side | Innhald |
|---|---|
| [Arkitekturoversikt](arkitektur-oversikt.md) | Heilskapleg diagram frå kjeldeskjema, via MCP-serverar og CI, til publiserte artefakt og dei nasjonale katalogane som hentar frå dei. |
| [Importhierarki](importhierarki.md) | Det komplette importhierarkiet for alle skjema i repoet — kva som importerer kva, og kvifor. |
| [Valideringsreglar](valideringsregler.md) | Bronse/sølv/gull-policyane og publiseringspolicyane — full sjekkliste med Digdir-regel- og FAIR-mapping. |
| [AP-NO arkitektur og avvik](ap-no-arkitektur.md) | Korleis AP-NO-skjemaa (DCAT, SKOS, CPSV, DQV m.fl.) er bygde opp i dette repoet, og kvar og kvifor dei medvite avvik frå spesifikasjonane. |
| [Standardetterleving](standardetterleving.md) | Kartlegging av korleis repoet realiserer og etterlever Digdirs Rammeverk for informasjonsforvaltning — veiledere, standardar/spesifikasjonar og felles informasjonsmodellar. |
| [Bruk frå eksternt repo](ekstern-bruk.md) | Korleis eit anna repo kan importere AP-NO-profilane og bruke repoet sine reusable GitHub Actions-workflowar utan å leve inni monorepoet. |

## Relatert dokumentasjon

- [Kom i gang](../kom-i-gang/index.md) — praktiske steg-for-steg-rettleiingar for å ta i bruk repoet
- [Publisering](../publisering/index.md) — korleis genererte artefakt vert tilrettelagt for hausting til nasjonale katalogar
- [Automasjon](../automasjon/index.md) — dei tekniske genereringsdetaljane bak kvart artefakt og kvar portalside, og korleis du overvakar automasjonen
