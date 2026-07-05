---
name: verifiser-kontaktinfo-ci
description: Verifiser at kontaktinfo-fiksen fungerer i GitHub Actions og vert publisert til GitHub Pages
metadata:
  type: verification
---

# Verifiser kontaktinfo-fiksen i CI

## Bakgrunn

Kontaktinfo-fiksen (`fix-codeowners-hardcoded-path.md`) er implementert lokalt og fungerer:

```bash
$ bash mkdocs/publish.sh
# Genererer korrekt kontaktinfo for alle skjema:
# - samt/samt-bu: KS Digital
# - oreg/register-over-aksjeeiere: Brønnøysundregistra
# - ap-no/dcat-ap-no: Digitaliseringsdirektoratet
# - fint/fint-administrasjon: Novari IKS
```

Men **GitHub Pages** viser framleis berre "Support: GitHub Issues" fordi endringane ikkje er pusha til `main` enno.

## Verifisering i CI

### Trinn 1: Push til main

```bash
git add mkdocs/publish.sh specs/done/fix-codeowners-hardcoded-path.md specs/done/fix-versjonslog-separator.md
git commit -m "fix(mkdocs): fiks manglande kontaktinfo i CI og versjonslog-renderingsfeil"
git push origin main
```

### Trinn 2: Sjekk GitHub Actions

1. Gå til https://github.com/brreg/linkml-datamodellering-no/actions
2. Finn køyringa av `generate.yml` (trigga av push til main)
3. Sjekk `generate / samt` → `Steg 2: Generer innhald per domene og skjema`
4. Verifiser at ingen Python-feil i `get_contact_info()`

### Trinn 3: Sjekk GitHub Pages

1. Vent til `publish`-jobben er ferdig (Pages-deploy)
2. Gå til https://brreg.github.io/linkml-datamodellering-no/samt/samt-bu/
3. Scroll ned til "Kontakt"-seksjonen
4. Verifiser at det står:
   ```
   Forvaltningsansvarleg: KS Digital
   Kontakt: KS Digital - Kontakt
   Support: GitHub Issues
   ```
   **Ikkje berre:**
   ```
   Support: GitHub Issues
   ```

### Trinn 4: Sjekk andre skjema

Verifiser same resultat for:
- https://brreg.github.io/linkml-datamodellering-no/oreg/register-over-aksjeeiere/ → Brønnøysundregistra
- https://brreg.github.io/linkml-datamodellering-no/ap-no/dcat-ap-no/ → Digitaliseringsdirektoratet
- https://brreg.github.io/linkml-datamodellering-no/fint/fint-administrasjon/ → Novari IKS

## Potensielle feil i CI (ikkje i lokal miljø)

Dersom kontaktinfo framleis vert berre "Support: GitHub Issues" i CI, kan det vere:

### 1. CODEOWNERS.md ikkje inkludert i artifact

Sjekk `.github/workflows/generate.yml` linje 30-40:

```yaml
- uses: actions/upload-artifact@v7
  with:
    name: source
    path: |
      src/
      mkdocs/
      .github/
      Makefile
      README.md
      # <-- CODEOWNERS.md manglar?
```

**Løysing:** Legg til `CODEOWNERS.md` i artifact-lista.

### 2. Python yaml-modul manglar

Sjekk om `pyyaml` er installert i mkdocs-containeren (`mkdocs/Dockerfile.mkdocs`).

**Løysing:** Legg til `pyyaml` i requirements.

### 3. Path-format skilnad Ubuntu vs WSL

Ubuntu: `/home/runner/work/linkml-datamodellering-no/linkml-datamodellering-no`
WSL: `/mnt/c/dev/github/linkml-datamodellering-no`

**Løysing:** Verifiser at `REPO_ROOT` er korrekt sett i `publish.sh` (linje 5).

## Handlingsliste

- [✓] 1. Push commit til main
- [✓] 2. Identifiser rotårsak: `CODEOWNERS.md` mangla i source-artifact
- [✓] 3. Fiks: legg til `CODEOWNERS.md` i `.github/workflows/generate.yml` linje 42
- [ ] 4. Push ny commit og verifiser GitHub Pages viser korrekt kontaktinfo

## Utført

**Rotårsak funne:** `CODEOWNERS.md` var **ikkje inkludert** i `source`-artefaktet i `.github/workflows/generate.yml` (linje 36-41). Dette gjorde at `publish.sh` i CI ikkje hadde tilgang til fila, og `get_contact_info()` fell tilbake på linje 50-52:

```bash
if [ ! -f "$codeowners_file" ]; then
    echo "**Support:** [GitHub Issues](...)"
    return
fi
```

**Løysing:** Lagt til `CODEOWNERS.md` på linje 42 i artifact-path-lista.

**Neste steg:**
- Push ny commit
- Verifiser at GitHub Pages no viser full kontaktinfo (forvaltningsansvarleg, kontakt, support)
