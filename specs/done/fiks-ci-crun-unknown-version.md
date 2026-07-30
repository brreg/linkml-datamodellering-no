# Fiks CI-feil: crun: unknown version specified i generate-jobben

## Bakgrunn

Dei to siste CI-kjøringane av `generate`-workflow feila med:

```
Error: OCI runtime error: crun: unknown version specified
→ merge-imports  ngr/ngr-virksomhet (0.4s)
→ merge-imports  ngr/ngr-adresse (0.4s)
make: *** [Makefile:780: domain-ngr] Error 123
```

Feilen oppstår i `generate`-jobben (linje 142-143) når `podman pull` feiler og deretter `podman tag` prøver å tagge eit ikkje-eksisterande image:

```bash
podman pull "$ghcr_tag"
podman tag "$ghcr_tag" "$local_tag"
```

Same problem vart løyst for `mkdocs-local`-imaget i commit `32886b8b`, men ikkje for dei andre imaga i `generate`-jobben.

## Rotårsak

`podman tag` på eit ikkje-eksisterande image gir `crun: unknown version specified`-feil. Dette skjer når:

- `podman pull` feiler (nettverk, autentisering, GHCR-image finst ikkje)
- `podman tag` køyrer uansett og prøver å tagge noko som ikkje finst

## Løysing

Endre `pull_image`-funksjonen i `.github/workflows/generate.yml` (linje 139-146) til å:

1. Sjekke om `podman pull` lukkast
2. Dersom pull feiler: bygg imaget lokalt som fallback
3. Berre køyr `podman tag` dersom pull lukkast

## Steg

1. Les `.github/workflows/generate.yml` linje 136-158
2. Endre `pull_image`-funksjonen til å ha same feilhandtering som i `publish`-jobben (commit 32886b8b)
3. Test at endringane ikkje introduserer syntaksfeil i workflow-fila

## Handlingsliste

- [x] Les `.github/workflows/generate.yml` linje 136-158
- [x] Endre `pull_image`-funksjonen med fallback til lokal bygging
  - Legg til tredje parameter `make_target`
  - Sjekk om `podman pull` lukkast før `podman tag`
  - Dersom pull feiler: køyr `make "$make_target"` for å bygge imaget lokalt
- [x] Commit: `fix(ci): legg til fallback for podman pull i generate-jobben`
- [x] Push og sjå at CI-køyring lukkast

## Utført

Alle tiltak er utførte. `pull_image`-funksjonen i `.github/workflows/generate.yml` har no same feilhandtering som `publish`-jobben (commit 32886b8b): dersom `podman pull` feiler, vert imaget bygd lokalt som fallback. Dette løyser `crun: unknown version specified`-feilen som oppstod når `podman tag` prøvde å tagge eit ikkje-eksisterande image.
