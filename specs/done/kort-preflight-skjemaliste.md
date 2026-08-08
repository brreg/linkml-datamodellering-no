# Kort preflight-skjemaliste i generate-workflow

## Bakgrunn

Oppfølging av `specs/done/kort-validering-logglinje.md`. I "Generer alle
artefaktar for `<domain>`"-steget i `.github/workflows/generate.yml`
listar preflight-logginga kvart skjema med full sti
(`src/linkml/<domain>/<modell>/<modell>-schema.yaml`). Brukaren ønsker
kortare visning utan `src/linkml/<domain>/`-prefikset, konsistent med dei
andre logglinje-forenklingane i denne økta.

## Steg

1. `.github/workflows/generate.yml`, steget "Generer alle artefaktar for
   `${{ matrix.domain }}`": strip `src/linkml/<domain>/`-prefikset frå
   `$schema` før utskrift med bash parameter-expansion
   (`${schema#src/linkml/${{ matrix.domain }}/}`) — `${{ matrix.domain }}`
   vert bytt ut til bokstaveleg tekst av GitHub Actions FØR shell-en
   tolkar linja, så uttrykket fungerer som vanleg `${var#prefix}`-stripping.
2. `actionlint` mot den endra fila (påkravd etter CI-endring, jf.
   CLAUDE.md) — berre pre-eksisterande `[shellcheck]`-funn i urelaterte
   blokker attstår.
3. Verifiser lokalt ved å simulere `find`-løkka med `domain=ap-no` og
   stadfest at outputen matchar ønskt format
   (`<modell>/<modell>-schema.yaml` per linje).

## Handlingsliste

- [x] Steg 1: generate.yml preflight-logg
- [x] Steg 2: actionlint
- [x] Steg 3: lokal verifisering

## Utført

Verifisert lokalt (simulert `find`-løkka med `domain="ap-no"`):

```
=== ap-no skjema for artefakt generering ===
  - common-ap-no/common-ap-no-schema.yaml
  - cpsv-ap-no/cpsv-ap-no-schema.yaml
  - dcat-ap-no/dcat-ap-no-schema.yaml
  - dqv-ap-no/dqv-ap-no-schema.yaml
  - dqv-ap-no/dqv-core-schema.yaml
  - modelldcat-ap-no/modelldcat-ap-no-schema.yaml
  - modelldcat-ap-no/modelldcat-katalog-schema.yaml
  - modelldcat-ap-no/modelldcat-modell-schema.yaml
  - skos-ap-no/skos-ap-no-schema.yaml
  - xkos-ap-no/xkos-ap-no-schema.yaml
```

- `.github/workflows/generate.yml`: preflight-skjemaliste stripper no
  `src/linkml/<domain>/`-prefikset

`actionlint` køyrt mot fila — ingen `[expression]`-feil, same
pre-eksisterande `[shellcheck]`-stilråd som før endringa (éin av dei
flytta linjenummer pga. ny kommentarlinje, ikkje ny).
