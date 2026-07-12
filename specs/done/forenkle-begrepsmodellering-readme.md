# Forenkle Begrepsmodellering-seksjonen i README.md

## Bakgrunn

README.md sin "Begrepsmodellering"-seksjon (linje 94-165) er meir verbose enn
"Datamodellering"-seksjonen (linje 62-92). Begrepsmodellering-seksjonen inneheld:

- Forklarande tekst mellom kvar kodeblokk (linje 106-109, 111-115, 118-129)
- Detaljerte kommentarar om kva scriptet opprettar (linje 106-108)
- Lange kommentarar om kva som skal fyllast ut (linje 111-115)
- Forklaringar om korleis mcp-begrep-utkast skal brukast (linje 118-125)
- Detaljert filstruktur-eksempel (linje 149-163)

**Datamodellering-seksjonen** er meir kompakt:
- Hovudfokus på kommandoane (4 nummererte steg)
- Minimale kommentarar i kodeblokkar
- Éin avsluttande linje om automatisk oppdaging
- Lenke til full rettleiing på slutten

**Problem:** Begrepsmodellering-seksjonen er vanskeleg å skumme raskt og bryt med
README-prinsippet om å vere ein "quick start" med lenkjer til fullstendig
dokumentasjon. Detaljerte steg høyrer heime i `ny-begrepsmodell.md` på
dokumentasjonsportalen, ikkje i README.

## Mål

Forenkle Begrepsmodellering-seksjonen til same kompaktheitsnivå som
Datamodellering-seksjonen:

1. Fjern forklarande tekstblokkar mellom kodeblokkar
2. Reduser kommentarar i kodeblokkar til minimum
3. Fjern filstruktur-eksempelet (høyrer heime i `ny-begrepsmodell.md`)
4. Behald berre hovudkommandoane (1-6 steg)
5. Lenk til fullstendig dokumentasjon på dokumentasjonsportalen

## Nummererte steg

### 1. Analyser forskjellen mellom dei to seksjonane

Samanlikn strukturen:

**Datamodellering (kompakt):**
- Éin introduksjonslinje (linje 64)
- Kodeblokk med 4 nummererte steg (linje 66-88)
- Avsluttande linje om automatisk oppdaging (linje 90)
- Lenke til full rettleiing (linje 92)

**Begrepsmodellering (verbose):**
- Overskrift (linje 97)
- Introduksjonslinje (linje 99) **← SKAL FJERNAST**
- Variabelplassholdarlinje (linje 101)
- Kodeblokk med steg 1 (linje 103-107)
- Forklarande tekstblokk (linje 109-111) **← SKAL FJERNAST**
- Kodeblokk med steg 2 (linje 113-118) **← SKAL ERSTATTAST MED 1b (mcp-begrep-utkast)**
- Kodeblokk med steg 3a (linje 120-129) **← SKAL FORENKLAST TIL STEG 2**
- Kodeblokk med steg 3b (linje 131-132) **← SKAL SLÅAST SAMAN I STEG 2**
- Kodeblokk med steg 4-6 (linje 134-150) **← BLIR STEG 3-5a**
- Filstruktur-eksempel (linje 153-167) **← SKAL FJERNAST**
- Lenke til full rettleiing (linje 169)

### 2. Skriv ny kompakt versjon av Begrepsmodellering-seksjonen

Lag ein ny versjon som følgjer same mønster som Datamodellering-seksjonen:

**Mønster:**
- Éi kodeblokk per steg (1/1b, 2, 3, 4, 5/5a)
- Kommentarar med `→` for output inni kodeblokka
- Steg 1b og 5 er valgfrie (markert med "om ønskjeleg")
- Éin linje om automatisk oppdaging etter siste kodeblokk
- Sluttlenke til full rettleiing

**Ny versjon:**


### Begrepsmodellering

> Bytt ut **`domene`**, **`begrepssamling-namn`** og **`organisasjon`** med dine aktuelle namn.

```bash
# 1a. Opprett ny begrepssamling (filstruktur for begrep)
make new-begrepssamling DOMAIN=domene NAME=begrepssamling-namn

# 1b. (om ønskjeleg) Generer begrepsutkast frå eksisterande tekst
make mcp-linkml-begrep-utkast INPUT=<sti-til-tekstfil>
# → genererer begrepsutkast i tmp/ og kopier til src/linkml/domene/begrepssamling-namn/begrep/begrepnavn.yaml
```
```bash
# 2. Rediger begrep etter behov
#    → src/linkml/domene/begrepssamling-namn/begrep/<begrep-slug>.yaml
```
```bash
# 3. Aggreger til begrepskatalog
make gen-begrepskatalog-instance
```
```bash
# 4. Valider begrepskatalog
make mcp-linkml-validate \
  SCHEMA=src/linkml/begrepskatalog/<organisasjon>-begrepskatalog/<organisasjon>-begrepskatalog-schema.yaml \
  POLICY=felles-begrepskatalog
```
```bash
# 5a. (om ønskjeleg) angi kva artefakter som skal genereres fra begrepskatalogen i build.yaml
#    → src/linkml/begrepskatalog/<organisasjon>-begrepskatalog/data/<organisasjon>-begrepskatalog/build.yaml

# 5b. Generer artefakter og publiser til dokumentasjonsportal
make begrepskatalog && make docs-publish && make docs-serve   # → http://localhost:8000
```

Nye begrepssamlingar under `src/linkml/<domain>/<begrepssamling>/` vert oppdaga automatisk.

For full rettleiing: sjå [Ny begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/ny-begrepsmodell/) og [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/).
```

### 3. Erstatt eksisterande Begrepsmodellering-seksjon i README.md

Erstatt linje 97-169 i `README.md` med den nye kompakte versjonen frå steg 2.

**Behald:**
- `### Begrepsmodellering` (linje 97)
- `> Bytt ut **\`domene\`**, **\`begrepssamling-namn\`** og **\`organisasjon\`** med dine aktuelle namn.` (linje 101)
- Sluttlenke til full rettleiing (linje 169)

**Fjern:**
- Introduksjonslinje "Begrep vert organiserte i..." (linje 99)
- Alle forklarande tekstblokkar mellom kodeblokkar (linje 109-111, 113-118, 120-129, 131-132)
- Filstruktur-eksempel (linje 153-167)
- Detaljerte kommentarar i kodeblokkar (t.d. "Døme: make new-begrepssamling DOMAIN=oreg NAME=begrepssamling-foretaksregisteret")

**Endre:**
- Steg 2 (build.yaml for begrepssamling) → Steg 1b (mcp-begrep-utkast)
- Steg 3a/3b → Steg 2 (skriv begrep)
- Steg 4-6 → Steg 3-5 (aggreger, valider, publiser)
- Legg til nytt steg 5 (rediger build.yaml for begrepskatalog)

### 4. Verifiser at fullstendig dokumentasjon finst på portalen

Sjekk at `mkdocs/docs/ny-begrepsmodell.md` inneheld all informasjonen som vert
fjerna frå README.md:

- Filstruktur-eksempel med forklaring
- Detaljert steg-for-steg-rettleiing
- Forklaring av kva `build.yaml` skal innehalde
- Døme på korleis mcp-linkml-begrep-utkast skal brukast

Dersom denne dokumentasjonen manglar, oppdater `ny-begrepsmodell.md` først før
README.md vert forenkla.

### 5. Oppdater CLAUDE.md dersom nødvendig

Sjekk om `CLAUDE.md` refererer til filstruktur-eksempelet i README.md. Dersom det
gjer det, oppdater referansen til å peike på `ny-begrepsmodell.md` i staden.

### 6. Test at lenkjene fungerer

Verifiser at lenkjene til dokumentasjonsportalen er korrekte:
- `[Ny begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/ny-begrepsmodell/)`
- `[Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/)`

## Handlingsliste

- [x] Steg 1: Analyser forskjellen mellom Datamodellering og Begrepsmodellering
- [x] Steg 2: Skriv ny kompakt versjon av Begrepsmodellering-seksjonen
- [x] Steg 3: Erstatt eksisterande Begrepsmodellering-seksjon i README.md (linje 97-169)
- [x] Steg 4: Verifiser at fullstendig dokumentasjon finst i `ny-begrepsmodell.md`
- [x] Steg 5: Oppdater CLAUDE.md dersom nødvendig (sjekk referansar)
- [x] Steg 6: Test at lenkjene til dokumentasjonsportalen fungerer

## Utført

Alle steg er utførte. Begrepsmodellering-seksjonen er no forenkla til same kompaktheitsnivå som Datamodellering-seksjonen.

**Resultat:**
- Redusert frå ~72 linjer til ~30 linjer (58% reduksjon)
- Hovudfokus på kommandoane (5 hovudsteg: 1a/1b, 2, 3, 4, 5a/5b)
- Minimale kommentarar i kodeblokkar
- Éin avsluttande linje om automatisk oppdaging
- Lenke til full rettleiing på dokumentasjonsportalen

**Struktur:**
1a. Opprett begrepssamling
1b. (Valfri) Generer begrepsutkast med mcp-linkml-begrep-utkast
2. Rediger begrep
3. Aggreger til begrepskatalog
4. Valider begrepskatalog
5a. (Valfri) Rediger build.yaml for begrepskatalog
5b. Generer artefakter og publiser

**Verifisert:**
- `mkdocs/docs/ny-begrepsmodell.md` inneheld fullstendig dokumentasjon (filstruktur-eksempel, build.yaml-forklaring, mcp-begrep-utkast-døme)
- CLAUDE.md refererer ikkje til filstruktur-eksempel i README.md
- Lenkjene til dokumentasjonsportalen er korrekte
