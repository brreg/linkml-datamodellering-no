# Bidra til linkml-datamodellering-no

## Føresetnader

- [Podman](https://podman.io/) (rootless) installert i WSL2
- GNU Make
- Git

Ingen avhengigheiter skal installerast lokalt — alt køyrer som containere.

## Kjem i gang

```bash
git clone git@github.com:brreg/linkml-datamodellering-no.git
cd linkml-datamodellering-no

# Bygg container-images (éin gong)
make linkml-build-docker
make python-build-docker
make mcp-val-build
```

## Validering

Valider eit skjema og tilhøyrande eksempel etter kvar endring:

```bash
./tests/validate_schema.bash src/linkml/<domene>/<modell>/<modell>-schema.yaml examples/<domene>/<modell>-eksempel.yaml
```

Valider mot kvalitetsprofil (bronze = minimumskrav):

```bash
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=silver
```

## Ny domenemodell

Sjå `specs/ny-domenemodell.md` for steg-for-steg-rettleiing.

## Generer artefaktar lokalt

```bash
make <domene>          # t.d. make ngr, make ap-no, make fair
make docs-serve        # start lokal dokumentasjonsportal på http://localhost:8000
```

## Pull request

1. Lag ein ny branch frå `main`
2. Gjer endringar og valider lokalt (sjå over)
3. Send inn pull request mot `main` — CI køyrer validering automatisk

Rapporter sikkerheitssårbarheiter via e-post (sjå [SECURITY.md](SECURITY.md)) — ikkje som public issue.
