# Fleire modellar knytte til same register under `oreg`

## Bakgrunn

`src/linkml/oreg/` inneheld per i dag éin modell: `register-over-aksjeeiere/`.
Behovet er å leggje til fleire modellar som høyrer til same offentlege register
(t.d. fleire delmodellar frå Enhetsregisteret eller Aksjeregisteret).

Spørsmålet er om ein bør innføre eit ekstra katalognivå mellom domenet `oreg` og
kvar enkelt modell — eller om det finst ei betre løysing.

---

## Teknisk avgrensing

Makefile-oppdaginga av skjema er hardkoda til djupne 3 frå `src/linkml/`:

```makefile
SCHEMAS := $(shell find $(SCHEMA_DIR) -mindepth 3 -maxdepth 3 -name '*-schema.yaml' ...)
schema_domain = $(word 3,$(subst /, ,$(1)))   # t.d. "oreg"
schema_name   = $(word 4,$(subst /, ,$(1)))   # t.d. "register-over-aksjeeiere"
```

`publish.sh` traverserer tilsvarande `generated/<domene>/<skjema>/`.

Eit ekstra katalognivå (register-nivå) ville bryte begge desse mekanismane utan
koordinerte endringar.

---

## Vurderte alternativ

### Alternativ A — Namngjevingsprefiks (tilrådd)

Modellar som høyrer til same register får registeret som prefiks i modellnamnet:

```
src/linkml/oreg/
  aksjeregisteret-eigarskap/
  aksjeregisteret-aksjar/
  enhetsregisteret-grunndata/
  enhetsregisteret-roller/
```

**Fordelar:**
- Ingen strukturelle endringar i Makefile, `publish.sh` eller andre skript.
- Konsistent med korleis NGR brukar prefiks (`ngr-adresse`, `ngr-eiendom`,
  `ngr-person`, `ngr-virksomhet`) for å gruppere modellar under eitt domene.
- Portalen grupperer automatisk alle `oreg`-modellar under «OREG – Offentlege
  registre» i navigasjonsmenyen; registertilhøyring kjem fram av modellnamnet.
- Skalerer utan grense — ingen ny konfig ved kvart nytt register.

**Ulemper:**
- Flat katalogstruktur — ein kan ikkje `ls oreg/aksjeregisteret/` for å sjå
  alle aksjeregister-modellar. Gruppering skjer berre via namngjeving.
- Krev disiplin i namngjevinga; ingen teknisk handhevingsmekanisme.

**Namngjevingskonvensjon:**
```
<register>-<modellkonsept>/
```
Der `<register>` er eit kortnamn på registeret i kebab-case
(t.d. `aksjeregisteret`, `enhetsregisteret`, `folkeregisteret`).

---

### Alternativ B — Ekstra katalognivå med Makefile-endringar

Innfør eit register-nivå mellom domene og modell:

```
src/linkml/oreg/
  aksjeregisteret/
    eigarskap/
    aksjar/
  enhetsregisteret/
    grunndata/
    roller/
```

**Fordelar:**
- Klar fysisk gruppering; `ls oreg/aksjeregisteret/` viser alle modellar.
- Nyttig ved mange modellar (10+) per register.

**Ulemper:**
- Krev endringar i `Makefile` (`-maxdepth 4`, ny `schema_domain`-funksjon som
  slår saman nivå 3 og 4).
- Krev endringar i `publish.sh` (traversering av to nivå under kvart domene).
- Krev endringar i `tests/validate_schema.bash` og andre skript som antek
  ei fast stiarstruktur.
- Modellnamna misser registerprefiks — `generated/oreg/aksjeregisteret/eigarskap/`
  er mindre lesbart og skapar namnekollisjonsrisiko på tvers av register.
- Høg kompleksitet for liten gevinst når ein startar med 2–5 modellar per register.

---

### Alternativ C — Eige domene per register

Kvart register får sitt eige toppnivå-domene:

```
src/linkml/aksjeregisteret/
src/linkml/enhetsregisteret/
```

**Fordelar:**
- Ingen strukturelle endringar.
- Fullstendig separasjon mellom registre.

**Ulemper:**
- Mister samlekategorien «Offentlege registre» i portalen.
- Domenelistene veks ukontrollert.
- Svakare semantisk skilnad mellom domene-typar (AP-NO-profil vs. domenemodell
  vs. register) i katalogstrukturen.

---

## Tilråding

Bruk **alternativ A** — namngjevingsprefiks — som ein direkte parallell til
korleis NGR-domenet handterer fleire modellar i dag.

Omdøyp eksisterande modell:

```
src/linkml/oreg/register-over-aksjeeiere/
→ src/linkml/oreg/aksjeregisteret-eigarskap/
```

(eller ein anna kortnamnskonvensjon etter brukarval)

Alternativ B bør vurderast på nytt dersom eit enkelt register veks til meir enn
10 modellar, og kostnadane ved Makefile/publish.sh-endringar då er meir forsvarleg.

---

## Tiltak

- [ ] Bli einige om kortnamn for kvart register (t.d. `aksjeregisteret`,
      `enhetsregisteret`, `folkeregisteret`).
- [ ] Omdøyp `register-over-aksjeeiere/` til `aksjeregisteret-<konsept>/`
      (oppdater `name`, `id`, `default_prefix` og `title` i skjemaet).
- [ ] Oppdater `description.md`, `manifest.yaml` og `examples/`-mappe tilsvarande.
- [ ] Dokumenter namngjevingskonvensjonen i `CLAUDE.md` under «Namngjeving /
      Katalogstruktur».
