# Automasjon

!!! note "Beskrivelse"

    Denne seksjonen går eit nivå djupare enn [Arkitektur](../arkitektur/index.md) og
    [Publisering](../publisering/index.md): her finn du presise kjelde-til-artefakt-sporingar
    for korleis kvar automatisk genererte fil og portalside faktisk vert bygd, og korleis du
    kan overvake at automasjonen faktisk fungerer som forventa.

| Side | Innhald |
|---|---|
| [Artefaktgenerering — kjelder og pipeline](../artefakt-generering.md) | For kvart automatisk generert artefakt i repoet: kva `make`-target/kommando/container genererer det, og kva skjemafelt eller `build.yaml`-nøkkel som styrer innhaldet. |
| [Generering av modell-dokumentasjon](../index-md-struktur.md) | Korleis `index.md`-sida for kvar enkelt modell (t.d. denne portalen sine `<domain>/<modell>/index.md`-sider) vert bygd opp og generert av `mkdocs/publish.sh`. |
| [Generering av modellmanifest](../modellmanifest-generering.md) | Korleis `<modell>-manifest.yaml` (Informasjonsmodell-instans ihht ModelDCAT-AP-NO) vert automatisk generert frå seks ulike kjelder. |
| [README-tabellgenerering](../readme-tabellgenerering.md) | Korleis dei tre auto-genererte tabellane i `README.md` (domene, skjema, begrepskatalogar/modellkatalogar) vert haldne konsistente med `generated/`-strukturen. |
| [Monitorering av automasjon](../monitorering.md) | Korleis du overvakar at generering og publisering av artefakt fungerer som forventa — GitHub Actions-loggar, valideringsresultat og feilsøking. |

## Sjå òg

- [Arkitekturoversikt](../arkitektur-oversikt.md) — den heilskaplege flyten desse sidene er detaljar av
- [Kom i gang](../kom-i-gang/index.md) — praktiske steg-for-steg-rettleiingar
