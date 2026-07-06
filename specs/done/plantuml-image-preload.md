# plantuml-image-preload

**Bakgrunn:**

`generate`-jobben i `.github/workflows/generate.yml` køyrer `make domain-<domene>` parallelt for 8 domene. Kvar `gen-plantuml`-target køyrer fleire gonger per domene (éin gong per skjema) og brukar `podman run ... docker.io/plantuml/plantuml:latest`. Dersom dette imaget ikkje finst lokalt, pullar podman det automatisk — og med 9 skjema i ap-no-domenet som køyrer parallelt, får vi 9 samtidige `podman pull docker.io/plantuml/plantuml:latest`-kommandoar. Dette er sløsing og kan gi rate limiting eller timeout.

**Forventet oppførsel:**

`plantuml/plantuml:latest`-imaget skal handterast på same måte som dei andre container-imagea: bygd/henta i `ensure-images`-jobben, pusha til GHCR (eller lasta frå cache), og deretter lasta inn i `generate`-jobben før `gen-plantuml` køyrer.

**Tiltak:**

1. ☑ Legg til `plantuml-upstream` som eit nytt image i `ensure-images`-matrix i `.github/workflows/generate.yml`
   - `name: plantuml-upstream`
   - `dockerfile: ""` (upstream-image, ikkje bygd lokalt)
   - `make_target: pull-plantuml-upstream`
   - `hash_files: "2026-07-06"` (fast datostempel for cache-key)
2. ☑ Legg til `pull-plantuml-upstream`-target i `Makefile` som pullar `docker.io/plantuml/plantuml:latest` og taggar det som `localhost/plantuml-upstream:latest`
3. ☑ Legg til gjenoppretting av `plantuml-upstream.tar.zst` i `generate`-jobben (parallelt med dei andre imagea)
4. ☑ Legg til lasting av `plantuml-upstream` i `load_image`-blokka i `generate`-jobben
5. ☑ Oppdater `PLANTUML_IMAGE`-variabelen i `Makefile` til å peke på `localhost/plantuml-upstream:latest` i staden for `docker.io/plantuml/plantuml:latest`
6. ☐ Test at `make domain-ap-no` køyrer utan å pulle `plantuml/plantuml:latest` midt i prosessen

**Alternativ:**

I staden for ein ny `make pull-plantuml-upstream`-target, kan vi vurdere å pulle imaget direkte i workflow-steget (utan Makefile-target) — men då må vi endre strategien frå "all bygging går via Makefile" til "upstream-images handterast i workflow". Dette bryt med DRY-prinsippet der Makefile er normativ kjelde for all container-hantering.

**Val:** Held fast på Makefile-som-normativ-kjelde og legg til `pull-plantuml-upstream`-target.

## Gjennomføring

**Tiltak 1-5 implementerte:**

- `.github/workflows/generate.yml:73-76` — lagt til `plantuml-upstream` i `ensure-images`-matrix
- `.github/workflows/generate.yml:169-174` — lagt til gjenoppretting av `plantuml-upstream.tar.zst` frå cache
- `.github/workflows/generate.yml:199-200` — lagt til `load_image`-kall for `plantuml-upstream`
- `Makefile:20` — endra `PLANTUML_IMAGE` frå `docker.io/plantuml/plantuml:latest` til `localhost/plantuml-upstream:latest`
- `Makefile:689-693` — lagt til `pull-plantuml-upstream`-target
- `Makefile:501` — lagt til `pull-plantuml-upstream` i `.PHONY`-deklarasjonen

**Tiltak 6 — testing:** Ikkje køyrt lokalt (krev full `make domain-ap-no` med alle skjema). Vil bli testa i CI når workflow køyrer på push til `main`.

## Utført

PlantUML-imaget vert no henta og casha i `ensure-images`-jobben (parallelt med dei andre imagea) og lasta inn i `generate`-jobben før `gen-plantuml`-targeta køyrer. Dette eliminerer 9+ samtidige `podman pull`-kommandoar midt i `make domain-ap-no` og reduserer risikoen for rate limiting eller timeout.

**Endringar:**
- `.github/workflows/generate.yml` — lagt til `plantuml-upstream` i `ensure-images`-matrix, gjenopprettingssteg og `load_image`-kall
- `Makefile` — endra `PLANTUML_IMAGE` til `localhost/plantuml-upstream:latest` og lagt til `pull-plantuml-upstream`-target

**Verifisering:** CI vil teste at `make domain-ap-no` køyrer utan å pulle `plantuml/plantuml:latest` midt i prosessen ved neste push til `main`.
