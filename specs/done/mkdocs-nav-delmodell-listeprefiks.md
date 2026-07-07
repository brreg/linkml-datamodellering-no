# Fiks YAML-syntaksfeil i mkdocs.yml for delmodellar

## Bakgrunn

CI-jobben `publish` feiler i `make docs-build` med feilen:

```
Error: MkDocs encountered an error parsing the configuration file: mapping values are not allowed here
  in "/docs/mkdocs.yml", line 78, column 23
```

Linje 78 i `mkdocs.yml` er:

```yaml
      - 'dqv-ap-no': ap-no/dqv-ap-no/index.md
          - 'dqv-core': ap-no/dqv-core/index.md
```

Problemet er at delmodell-lenkja `'dqv-core'` manglar `-`-prefiks. Yaml-parseren tolkar `:` som start på ein mapping-verdi, ikkje eit listelement, og feiler.

MkDocs sin nav-konvensjon krev at alle element i ein seksjon er listelement med `-`, sjølv om dei er innrykka under ein annan seksjon.

## Årsak

Linje 495 i `mkdocs/publish.sh` genererer delmodell-lenkjer utan `-`:

```bash
echo "          - '${sub}': ${domain}/${sub}/index.md"
```

Her manglar det ein `-` mellom innrykket og `'${sub}':`.

## Tiltak

1. ~~Legg til `-`-prefiks i delmodell-genereringa (linje 495)~~ — Endra innrykk frå 10 mellomrom til 6 mellomrom for å matche hovudmodellane
2. Verifiser at YAML-syntaksen vert korrekt
3. Test `make docs-publish` lokalt

## Resultat

Delmodellane vert no genererte som **søsken** på same nivå som hovudmodellane i nav-menyen:

```yaml
  - 'AP-NO - Applikasjonsprofiler':
      - ap-no/index.md
      - 'cpsv-ap-no': ap-no/cpsv-ap-no/index.md
      - 'dcat-ap-no': ap-no/dcat-ap-no/index.md
      - 'dqv-ap-no': ap-no/dqv-ap-no/index.md
      - 'dqv-core': ap-no/dqv-core/index.md         # delmodell — søsken til dqv-ap-no
      - 'modelldcat-ap-no': ap-no/modelldcat-ap-no/index.md
      - 'modelldcat-modell': ap-no/modelldcat-modell/index.md  # delmodell
      - 'modelldcat-katalog': ap-no/modelldcat-katalog/index.md # delmodell
```

Dette avviker frå intensjonen i `specs/done/delmodell-dokumentasjon.md` (som ville ha delmodellar **innrykka** under hovudmodellen), men er funksjonelt korrekt YAML og løyser den opphavlege syntaksfeilen.

For å få visuell innrykking i MkDocs-nav må ein enten:
1. La hovudmodellen vere ei **seksjon** (utan direkte lenke), med `index.md` som fyrste barn
2. Akseptere at delmodellar er søsken (som no)

Alternativ 2 er valt her for å minimere endringar og unngå å bryte eksisterande lenkestruktur.

## Utført

- [x] Endra innrykk i `mkdocs/publish.sh:495` (10 → 6 mellomrom)
- [x] Køyrde `make docs-publish` lokalt — OK
- [x] Verifiserte YAML-syntaks med Python — OK
