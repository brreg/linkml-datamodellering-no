# Kom i gang

!!! note "Beskrivelse"

    Denne sida er inngangsporten til rettleiingane for å komme i gang med repoet —
    anten du skal registrere ein ny organisasjon, modellere ein ny domenemodell,
    modellere ein ny begrepskatalog, eller berre slå opp ein kommando.

Vel rettleiinga som passar til det du skal gjere:

| Rettleiing | Når brukar du ho? |
|---|---|
| [Bli modelleigar](../ny-org.md) | Din organisasjon skal ta i bruk repoet for første gong, saman med Brønnøysundregistra og andre verksemder. |
| [Ny domenemodell](../ny-domenemodell.md) | Du skal opprette ein heilt ny LinkML-domenemodell — frå filstruktur til RDF-eksport klar for Felles Datakatalog. |
| [Ny begrepskatalog](../ny-begrepsmodell.md) | Du skal opprette ei ny samling begrep — frå filstruktur til RDF-eksport klar for Felles Begrepskatalog. |
| [Byggmanifest (build.yaml)](../build-config.md) | Du treng referanse for kva `build.yaml` styrer — kva artefakter som vert genererte, publiseringsflagg og valideringspolicy. |
| [Kommandooversikt](../kommandoar.md) | Du treng ei fullstendig liste over alle `make`-kommandoar repoet tilbyr. |

## Føresetnader

Alle kommandoar køyrer i containerar via [Podman](https://podman.io/) — ingen
lokal installasjon av Python eller LinkML-verktøy er nødvendig. Sjå
["Kom i gang"-seksjonen på framsida](../index.md#kom-i-gang) for full
oppskrift på lokalt oppsett (WSL2, Podman, GNU make) og dei to typiske
løypene — datamodellering og begrepsmodellering — steg for steg.

## Sjå òg

- [Arkitektur](../arkitektur/index.md) — korleis skjemaa heng saman
- [Publisering](../publisering/index.md) — korleis genererte artefakt vert tilrettelagt for hausting til nasjonale katalogar
- [Automasjon](../automasjon/index.md) — tekniske detaljar om genereringspipelinen og monitorering
