# Nytt make-target: bygg alle container-image

## Bakgrunn

Repoet har i dag 10 separate `build-docker-*`-target (definerte i
`make/80-images.mk`, `make/50-docs.mk` og `make/60-mcp.mk`), eitt per
verktøy-image:

- `build-docker-linkml`
- `build-docker-python`
- `build-docker-avrotize`
- `build-docker-asyncapi`
- `build-docker-plantuml`
- `build-docker-gource`
- `build-docker-mkdocs`
- `build-docker-mcp-validator`
- `build-docker-mcp-modell-utkast`
- `build-docker-mcp-begrep-utkast`

Det finst ikkje noko samla target for å byggje alle desse på éin gong (t.d.
ved første oppsett av repoet, eller etter ei endring som påverkar fleire
Dockerfile-ar). Brukaren må i dag køyre alle 10 targeta manuelt.

To Dockerfile-ar er *ikkje* kopla til noko build-target i dag, og skal
**ikkje** inkluderast:
- `src/assets/containers/Dockerfile.asyncapi-cli` (avløyst av
  `Dockerfile.asyncapi-cli-minimal`, som `build-docker-asyncapi` allereie
  brukar)
- `src/assets/scripts/demo/Dockerfile.fun-tools` (demo-føremål, ikkje del av
  det ordinære byggeoppsettet)

## Steg

1. Legg til target `build-docker-all` i `make/80-images.mk` som avheng av
   alle 10 eksisterande `build-docker-*`-target (reint prerequisite-target,
   ingen eigen oppskrift).
2. Legg `build-docker-all` til `.PHONY`-lista i `Makefile`.
3. Dokumenter targetet i `COMMANDS.md` (verktøytabellen der dei andre
   `build-docker-*`-targeta står oppførte).
4. Valider: `make help` skal vise det nye targetet, og
   `make -n build-docker-all` skal liste alle 10 underliggjande
   `podman build`-kall utan feil.

## Handlingsliste

- [x] `make/80-images.mk`: legg til `build-docker-all`-target
- [x] `Makefile`: legg til i `.PHONY`
- [x] `COMMANDS.md`: dokumenter nytt target
- [x] Valider med `make help` og `make -n build-docker-all`

## Utført

- `make/80-images.mk`: nytt target `build-docker-all` (éin fysisk linje —
  `help.sh` krev target og `## `-skildring på same linje, sjå kommentar i
  scriptet), pluss oppdatert fil-toppkommentar
- `Makefile`: `build-docker-all` lagt til `.PHONY`-lista
- `COMMANDS.md`: ny rad i container-image-bygging-tabellen
- Validert: `make help` viser `build-docker-all` under "Container images",
  `make -n build-docker-all` listar alle 10 `podman build`-kall
