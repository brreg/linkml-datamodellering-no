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
- Introduksjonslinje med forklaring (linje 96)
- Variabelplassholdarlinje (linje 98)
- Kodeblokk med steg 1 (linje 100-104)
- Forklarande tekstblokk (linje 106-108) **← SKAL FJERNAST**
- Kodeblokk med steg 2 (linje 110-115) **← SKAL FORENKLAST**
- Kodeblokk med steg 3 (linje 117-129) **← SKAL FORENKLAST**
- Kodeblokk med steg 4-6 (linje 131-147)
- Filstruktur-eksempel (linje 149-163) **← SKAL FJERNAST**
- Lenke til full rettleiing (linje 165)

### 2. Skriv ny kompakt versjon av Begrepsmodellering-seksjonen

Lag ein ny versjon som følgjer same mønster som Datamodellering-seksjonen:

```markdown
### Begrepsmodellering

> Bytt ut **`domene`**, **`begrepssamling-namn`** og **`organisasjon`** med dine aktuelle namn.

```bash
# 1. Opprett ny begrepssamling (filstruktur for begrep)
make new-begrepssamling DOMAIN=domene NAME=begrepssamling-namn
# → oppretter begrep/-mappe og build.yaml med aggregation-metadata
```
```bash
# 2. Rediger build.yaml etter behov
#    → src/linkml/domene/begrepssamling-namn/build.yaml
#    Sett aggregation.organization og aggregation.catalog_name
```
```bash
# 3. Skriv begrep (manuelt eller med mcp-linkml-begrep-utkast)
#    → src/linkml/domene/begrepssamling-namn/begrep/<begrep-slug>.yaml
```
```bash
# 4. Aggreger til begrepskatalog
make gen-begrepskatalog-instance
```
```bash
# 5. Valider begrepskatalog
make mcp-linkml-validate \
  SCHEMA=src/linkml/begrepskatalog/<organisasjon>-begrepskatalog/<organisasjon>-begrepskatalog-schema.yaml \
  POLICY=felles-begrepskatalog
```
```bash
# 6. Generer artefakter og publiser til dokumentasjonsportal
make begrepskatalog && make docs-publish && make docs-serve   # → http://localhost:8000
```

Nye begrepssamlingar under `src/linkml/<domain>/<begrepssamling>/` vert oppdaga automatisk.

For full rettleiing: sjå [Ny begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/ny-begrepsmodell/) og [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/).
```

### 3. Erstatt eksisterande Begrepsmodellering-seksjon i README.md

Erstatt linje 94-165 i `README.md` med den nye kompakte versjonen frå steg 2.

Bevar:
- Introduksjonslinjer (linje 96, 98)
- Lenke til full rettleiing (linje 165)

Fjern:
- Forklarande tekstblokkar mellom kodeblokkar
- Filstruktur-eksempel (linje 149-163)
- Detaljerte kommentarar i kodeblokkar

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

- [ ] Steg 1: Analyser forskjellen mellom Datamodellering og Begrepsmodellering
- [ ] Steg 2: Skriv ny kompakt versjon av Begrepsmodellering-seksjonen
- [ ] Steg 3: Erstatt eksisterande Begrepsmodellering-seksjon i README.md (linje 94-165)
- [ ] Steg 4: Verifiser at fullstendig dokumentasjon finst i `ny-begrepsmodell.md`
- [ ] Steg 5: Oppdater CLAUDE.md dersom nødvendig (sjekk referansar)
- [ ] Steg 6: Test at lenkjene til dokumentasjonsportalen fungerer

## Forventet resultat

Begrepsmodellering-seksjonen skal vere like kompakt som Datamodellering-seksjonen:
- ~25 linjer totalt (frå ~72 linjer)
- Hovudfokus på kommandoane (6 nummererte steg)
- Minimale kommentarar i kodeblokkar
- Éin avsluttande linje om automatisk oppdaging
- Lenke til full rettleiing på dokumentasjonsportalen
