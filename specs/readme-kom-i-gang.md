# Plan: Skil «Kom i gang» i README etter brukstilfelle

## Mål

Dagens «Kom i gang»-seksjon i `README.md` er generisk og tek utgangspunkt
i datamodellering. Ein brukar som berre vil opprette og publisere ein begrepskatalog
må lese heile seksjonen for å finne ut kva som er relevant for dei.

Planen skil seksjonen i to klart åtskilde spor:

- **Datamodellering** — nytt LinkML-skjema, validering, generering av artefakter
- **Begrepsmodellering** — ny begrepskatalog, datafil, validering, publisering til Felles Begrepskatalog

---

## Noverande struktur

```
## Kom i gang
  Føresetnader
  Steg 0–4 (generisk, orientert mot datamodellering)
  Lenke til Ny domenemodell
```

---

## Ny struktur

```
## Kom i gang
  Føresetnader (felles)
    make check-prereqs
    make linkml-build-docker && make python-build-docker && make mcp-val-build && make mcp-gen-build && make mcp-begrep-build

  ### Datamodellering
    Steg 1–3 (utan container-bygg)
    Lenke til Ny domenemodell og Publiser til Felles Datakatalog

  ### Begrepsmodellering
    Steg 1–4 (utan container-bygg)
    Lenke til Ny begrepskatalog og Publiser til Felles Begrepskatalog
```

---

## Innhald i kvart spor

### Føresetnader (felles)

```bash
# Sjekk at alt er på plass
make check-prereqs

# Bygg container-images (éin gong)
make linkml-build-docker && make python-build-docker && make mcp-val-build && make mcp-gen-build && make mcp-begrep-build
```

### Datamodellering

```bash
# 1. Lag eit nytt tomt LinkML-skjema (skjema + filstruktur)
make new-model NAME=modellnavn DOMAIN=domene

# 1b. (om ønskjeleg) Generer frå eksisterande JSON Schema
make mcp-generate SCHEMA=tmp/modellnavn.json

# 2. Rediger modellfila ihht dine behov
#    → src/linkml/domene/schema.yaml

# 3. Valider mot minimumskrav
make mcp-validate \
  SCHEMA=src/linkml/domene/modellnavn/modellnavn-schema.yaml \
  POLICY=felles-datakatalog

# 4. Generer artefakter og publiser til dokumentasjonsportal
make domene && make publish && make docs-serve   # → http://localhost:8000
```

Lenke til [Ny domenemodell](https://brreg.github.io/linkml-datamodellering-no/ny-domenemodell/)
og [Publiser til Felles Datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-modell/).

### Begrepsmodellering

```bash
# 1. Opprett ny begrepskatalog (skjema + filstruktur)
make new-model NAME=katalognavn DOMAIN=begrep

# 2. Rediger datafila med reelle begrep
#    → data/begrep/katalognavn.yaml

# 3. Valider skjema og datafil
make mcp-validate \
  SCHEMA=src/linkml/begrep/katalognavn/katalognavn-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=data/begrep/katalognavn.yaml

# 4. Generer og publiser til dokumentasjonsportal
make begrep && make publish && make docs-serve   # → http://localhost:8000
```

Lenke til [Ny begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/ny-begrepsmodell/)
og [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/).

---

## Tekniske merknader

### `new-model` for begrep

`make new-model NAME=katalognavn DOMAIN=begrep` fungerer allereie og opprettar
rett filstruktur. Sporet treng ikkje nye make-reglar — berre ein tydelegare
presentasjon i README.

### Føresetnader (felles)

Container-bygging og `make check-prereqs` er felles for begge spor og vert
plassert éin gong øvst — ingen duplisering i kvart spor.

---

## Filendring

Éin fil: `README.md`

- `## Kom i gang` → felles føresetnader + `### Datamodellering` + `### Begrepsmodellering`
- Ingen endringar utanfor denne seksjonen
