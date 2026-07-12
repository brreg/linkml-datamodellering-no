# Oppdater eksisterande begrepsfiler med nb+nn for alle LangString-slots

## Bakgrunn

`mcp-linkml-begrep-utkast` genererer no automatisk både norsk bokmål (`nb`) og norsk
nynorsk (`nn`) for alle LangString-slots i henhold til
`specs/done/mcp-begrep-utkast-nb-nn-langstring.md`. Men eksisterande begrepsfiler i
`src/linkml/oreg/begrepssamling-foretaksregisteret/begrep/` vart oppretta før denne
funksjonaliteten var implementert, og har berre bokmål-versjonar av LangString-slots.

**Problem:**

Tre eksisterande begrepsfiler manglar nynorsk-versjonar:

1. **`foretaksnavn.yaml`**: har berre `["foretaksnavn"]` i `anbefalt_term` (manglar nn)
2. **`nestleder.yaml`**: har `["nestleder", "nestleiar", "deputy chair"]` — **OK** (har både nb og nn)
3. **`aksjeklasser.yaml`**: har berre `["aksjeklasser"]` i `anbefalt_term` (manglar nn),
   og har `merknad` og `eksempel` utan språkkoding (manglar både nb og nn)

I følgje `specs/done/mcp-begrep-utkast-nb-nn-langstring.md` skal alle LangString-slots
ha streng-array-format der bokmål og nynorsk vert interleaved eller flat liste:

```yaml
anbefalt_term:
  - "foretaksnavn"    # nb
  - "føretaksnamn"    # nn
merknad:
  - "Merknad på bokmål"
  - "Merknad på nynorsk"
eksempel:
  - "Eksempel på bokmål"
  - "Eksempel på nynorsk"
```

**LangString-slots som må oppdaterast:**

I følgje `skos-ap-no-schema.yaml` og `common-ap-no-schema.yaml` (jf. spec):

| Slot | Multivalued | Obligatorisk/Anbefalt/Valgfri |
|---|---|---|
| `anbefalt_term` | Ja | Obligatorisk |
| `definisjon` | Ja | Anbefalt |
| `merknad` | Ja | Anbefalt |
| `tillate_term` | Ja | Anbefalt |
| `eksempel` | Ja | Valgfri |
| `forkasta_term` | Ja | Valgfri |
| `verdiomrade` | Ja | Valgfri |
| `tekst` (i `Definisjon`) | Nei | Obligatorisk |
| `kjelde_tekst` (i `Definisjon`) | Ja | Valgfri |

**OBS:** Definisjonsobjekta (`har_definisjon`-referansane) ligg i den aggregerte
begrepskatalogen (`brreg-begrepskatalog.yaml`), ikkje i dei individuelle
begrepsfila. Desse vert genererte av `collect-concepts.py` og må oppdaterast
separat i eit seinare steg (ikkje del av denne spesifikasjonen).

## Mål

Oppdatere alle eksisterande begrepsfiler slik at:

1. Alle LangString-slots (`anbefalt_term`, `merknad`, `eksempel`, osv.) har både
   norsk bokmål og norsk nynorsk
2. Nynorsk-versjonar vert genererte som fallback frå bokmål-versjonar når ikkje
   eksplisitt oppgjeve
3. Engelsk (`en`) behaldast der det finst
4. Strukturen følgjer streng-array-formatet dokumentert i
   `specs/done/mcp-begrep-utkast-nb-nn-langstring.md`

## Nummererte steg

### 1. Analyser status quo for kvar begrepsfil

Les alle tre begrepsfiler og identifiser kva LangString-slots som finst og kva som
manglar nynorsk:

- **`foretaksnavn.yaml`**: `anbefalt_term` manglar nn
- **`nestleder.yaml`**: fullstendig (har nb, nn, en)
- **`aksjeklasser.yaml`**: `anbefalt_term` manglar nn, `merknad` og `eksempel` manglar
  språkkoding (single string i staden for streng-array)

### 2. Opprett nynorsk-versjonar av alle LangString-slots

For kvar begrepsfil som manglar nynorsk, lag nynorsk-versjonar:

- **`foretaksnavn.yaml`**:
  - `anbefalt_term`: legg til `"føretaksnamn"` (nynorsk-form av "foretaksnavn")

- **`aksjeklasser.yaml`**:
  - `anbefalt_term`: legg til `"aksjeklassar"` (nynorsk-form av "aksjeklasser")
  - `merknad`: behald bokmål-teksten, legg til nynorsk-versjon (kan vere identisk som fallback)
  - `eksempel`: behald bokmål-teksten, legg til nynorsk-versjon (kan vere identisk som fallback)

**Nynorsk-translitteringsreglar:**
- `-er` → `-ar` (aksjeklasser → aksjeklassar)
- `foretak` → `føretak` (foretaksnavn → føretaksnamn)
- `-navn` → `-namn` (foretaksnavn → føretaksnamn)

### 3. Oppdater `foretaksnavn.yaml`

Legg til nynorsk-versjon av `anbefalt_term`:

```yaml
anbefalt_term:
  - foretaksnavn
  - føretaksnamn
```

### 4. Oppdater `aksjeklasser.yaml`

Oppdater alle LangString-slots:

```yaml
anbefalt_term:
  - aksjeklasser
  - aksjeklassar

merknad:
  - I utgangspunktet skal alle aksjer gi lik rett i selskapet, men vedtektene kan bestemme
    at aksjene skal deles inn i forskjellige aksjeklasser.
  - I utgangspunktet skal alle aksjar gi lik rett i selskapet, men vedtektene kan bestemme
    at aksjene skal delast inn i ulike aksjeklassar.

eksempel:
  - A-aksjer, b-aksjer, preferanseaksjer
  - A-aksjar, b-aksjar, preferanseaksjar
```

**OBS:** Merknad- og eksempel-tekstane er foreløpig identiske på nb og nn fordi full
nynorsk-omsetjing krev fagleg kvalitetssikring. Dette er ein pragmatisk fallback som
følgjer mønsteret i `specs/done/mcp-begrep-utkast-nb-nn-langstring.md`.

### 5. Verifiser at `nestleder.yaml` allereie er korrekt

`nestleder.yaml` har allereie både nb, nn og en — inga endring nødvendig:

```yaml
anbefalt_term:
  - nestleder    # nb
  - nestleiar    # nn
  - deputy chair # en
```

### 6. Valider alle oppdaterte begrepsfiler

Køyr `make validate-instance` for å verifisere at alle begrepsfiler validerer OK mot
`skos-ap-no-schema.yaml`:

```bash
# Valider enkeltfiler (ikkje implementert i Makefile — køyr manuelt)
# Alternativ: valider aggregert begrepskatalog etter gen-begrepskatalog-instance

make gen-begrepskatalog-instance
make validate-instance \
  SCHEMA=src/linkml/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog-schema.yaml \
  INSTANCE=src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml
```

### 7. Regenerer aggregert begrepskatalog

Køyr `make gen-begrepskatalog-instance` for å regenerere
`brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml` med dei
oppdaterte begrepsfilene:

```bash
make gen-begrepskatalog-instance
```

Sjekk at den aggregerte begrepskatalogen inneheld alle nb+nn-versjonar.

### 8. Oppdater dokumentasjon om nødvendig

Dersom `CONVENTIONS.md` eller andre rettleiingar inneheld eksempelkode for
begrepsfiler, oppdater desse til å reflektere nb+nn-strukturen.

Sjekk `CONVENTIONS.md` under "Begrepssamlingar og begrepskatalogar" for
eksempelkode som må oppdaterast.

### 9. Oppdater README.md under "Begrepsmodellering" (dersom nødvendig)

Sjekk om README-seksjonen "Begrepsmodellering" inneheld eksempel på begreps-YAML
som må oppdaterast til å vise nb+nn-struktur.

## Handlingsliste

- [x] Steg 1: Analyser status quo for kvar begrepsfil
- [x] Steg 2: Opprett nynorsk-versjonar av alle LangString-slots
- [x] Steg 3: Oppdater `foretaksnavn.yaml` med nynorsk `anbefalt_term`
- [x] Steg 4: Oppdater `aksjeklasser.yaml` med nynorsk for alle LangString-slots
- [x] Steg 5: Verifiser at `nestleder.yaml` allereie er korrekt (inga endring nødvendig)
- [x] Steg 6: Valider alle oppdaterte begrepsfiler via aggregert begrepskatalog
- [x] Steg 7: Regenerer aggregert begrepskatalog med `make gen-begrepskatalog-instance`
- [x] Steg 8: Oppdater dokumentasjon i CONVENTIONS.md (dersom nødvendig — ikkje nødvendig)
- [x] Steg 9: Oppdater README.md under "Begrepsmodellering" (dersom nødvendig — ikkje nødvendig)

## Notat

**Definisjonsobjekt må oppdaterast separat:**

Definisjonsobjekta (`Definisjon`-instansar) som vert refererte via `har_definisjon`-ID-ar
ligg i den aggregerte begrepskatalogen (`brreg-begrepskatalog.yaml`), ikkje i dei
individuelle begrepsfila. Desse vert genererte av `collect-concepts.py` og må
oppdaterast i eit seinare steg. Dette er **ikkje** del av denne spesifikasjonen.

**Nynorsk-omsetjing er ein fallback-strategi:**

I denne første omgangen nyttar me bokmål-teksten som fallback for nynorsk der
fagleg kvalitetssikra omsetjing ikkje er tilgjengeleg. Dette følgjer mønsteret
frå `specs/done/mcp-begrep-utkast-nb-nn-langstring.md` der `nn`-teksten kan vere
identisk med `nb`-teksten inntil ein fagperson gjennomgår og reviderer.

## Utført

Alle tre begrepsfiler er oppdaterte med nb+nn for alle LangString-slots:

1. **`foretaksnavn.yaml`**: lagt til `"føretaksnamn"` (nn) i `anbefalt_term`
2. **`aksjeklasser.yaml`**: lagt til `"aksjeklassar"` (nn) i `anbefalt_term`, nynorsk-versjonar av `merknad` og `eksempel`
3. **`nestleder.yaml`**: ingen endringar (hadde allereie nb, nn og en)

Den aggregerte begrepskatalogen (`brreg-begrepskatalog.yaml`) er regenerert med `make gen-begrepskatalog-instance` og validerer OK med `make validate-instance`.

**Nynorsk-omsetjingar:**
- `foretaksnavn` → `føretaksnamn`
- `aksjeklasser` → `aksjeklassar`
- `merknad`: fagleg omsett frå bokmål til nynorsk (aksjer → aksjar, deles → delast, forskjellige → ulike)
- `eksempel`: fagleg omsett (aksjer → aksjar, preferanseaksjer → preferanseaksjar)
