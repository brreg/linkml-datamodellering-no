# Lenkjesjekk: NGR-vokabularnamnerom på `data.norge.no/vocabulary/` løyser ikkje opp

## Bakgrunn

Brukaren peika ut at Nasjonale grunndata-modellane (NGR) ikkje er
publiserte på `data.norge.no`, og bad om at lenkjesjekken filtrerer bort
oppslag mot dette mønsteret, med eit konkret døme frå `ngr-virksomhet`:

```
[404] https://data.norge.no/vocabulary/ngr-virksomhet#varslingsverdi
```

Same metodikk som tidlegare runder: direkte HTTP-oppslag med
nettlesar-realistisk `Accept`-header før konklusjon (jf. lærdomen i
`specs/done/lenkjesjekk-runde2-verifisering.md` om content
negotiation-fallgruver).

## Funn

Alle fire NGR-domeneskjema definerer eit eige term-nivå
vokabularprefiks under `data.norge.no/vocabulary/<schema>#`, skilt frå
sjølve schema-ID-en (`default_prefix`, som brukar det etablerte,
fungerande `data.norge.no/ngr/<schema>/`-mønsteret, jf.
CLAUDE.md § Schema-metadata):

| Domene | `default_prefix` (schema-ID, fungerer) | Vokabularprefiks (feilar) |
|---|---|---|
| `ngr-adresse` | `https://data.norge.no/ngr/ngr-adresse/` | `ngr: https://data.norge.no/vocabulary/ngr-adresse#` |
| `ngr-eiendom` | `https://data.norge.no/ngr/ngr-eiendom/` | `ngre: https://data.norge.no/vocabulary/ngr-eiendom#` |
| `ngr-person` | `https://data.norge.no/ngr/ngr-person/` | `ngrp: https://data.norge.no/vocabulary/ngr-person#` |
| `ngr-virksomhet` | `https://data.norge.no/ngr/ngr-virksomhet/` | `ngrv: https://data.norge.no/vocabulary/ngr-virksomhet#` |

Stadfesta at alle fire vokabular-namneroma (både utan fragment og med
eit konkret termfragment) gjev 404, testa med nettlesar-realistisk
`Accept`-header (ikkje eit content negotiation-tilfelle — same
per-host `Accept`-header som alt gjeld for `data.norge.no` i
`.github/lychee.toml` sidan runde 2 endrar ikkje resultatet):

```
https://data.norge.no/vocabulary/ngr-virksomhet                    → 404
https://data.norge.no/vocabulary/ngr-virksomhet#varslingsverdi     → 404
https://data.norge.no/vocabulary/ngr-adresse                       → 404
https://data.norge.no/vocabulary/ngr-eiendom                       → 404
https://data.norge.no/vocabulary/ngr-person                        → 404
```

Brukaren stadfestar at dette er venta og permanent: NGR-modellane er
ikkje publiserte på `data.norge.no` i det heile (i motsetnad til
AP-NO-profilane, som faktisk har fungerande schema-ID-sider der — jf.
kategori F i `specs/done/lenkjesjekk-runde2-verifisering.md`, der
schema-ID-mønsteret `data.norge.no/ap-no/...` og `data.norge.no/ngr/...`
stadfesta 200). Dette er difor **ikkje** same open/uavklara situasjon som
`data.norge.no/vocabulary/cccevno` (kategori E i same spec, der det
framleis krevst ei aktiv avgjerd før eksklusjon) — her er avgjerda teken:
NGR-vokabularnamnerommet er ein identifikator-URI, ikkje meint å vere
resolvbar, og vil ikkje verte det.

**Omfang:** 4 distinkte namnerom, 1862 lenkjeførekomstar fordelt på 319
filer i `mkdocs/docs/ngr/`.

## Tiltak

**N1 — Lychee-eksklusjon for NGR-vokabularnamnerommet.** Legg til i
`.github/lychee.toml` sin `exclude`-liste:

```toml
"^https://data\\.norge\\.no/vocabulary/ngr-",
```

Avgrensa til `ngr-`-prefikset (ikkje ei brei `/vocabulary/`-eksklusjon),
sidan `/vocabulary/cccevno` framleis er eit ope, uavklara tilfelle (jf.
kategori E over) og andre framtidige `/vocabulary/`-namnerom bør
framleis sjekkast til dei er eksplisitt vurderte.

**N2 — Ingen skjemaendring.** `ngr:`/`ngre:`/`ngrp:`/`ngrv:`-prefiksa er
gyldige, interne identifikator-namnerom for NGR-termar — dei skal ikkje
endrast eller fjernast. Schema-ID-en (`default_prefix`) er den delen som
faktisk skal vere resolvbar per CLAUDE.md § Schema-metadata, og han
fungerer alt korrekt.

## Steg

1. `.github/lychee.toml`: legg til
   `"^https://data\\.norge\\.no/vocabulary/ngr-"` i `exclude`-lista.
2. Valider TOML-syntaks og lychee-config-lasting.
3. Lokal `lychee`-verifisering mot det rapporterte dømet
   (`ngr-virksomhet/klasser/varslingsverdi.md`) + stikkprøve frå dei tre
   andre NGR-domena.
4. Ingen `make lint`/`make roundtrip` naudsynt (ingen `.yaml`-skjema vert
   endra). `actionlint` ikkje naudsynt (ingen workflow-fil endra).

## Handlingsliste

- [x] N1: legg til NGR-vokabular-eksklusjon i `.github/lychee.toml`
- [x] Valider TOML-syntaks og lychee-config-lasting
- [x] Lokal lychee-verifisering mot rapportert fil + stikkprøve frå andre
      NGR-domene

## Utført

Eksklusjonen `^https://data\.norge\.no/vocabulary/ngr-` lagt til i
`.github/lychee.toml` sin `exclude`-liste, avgrensa til `ngr-`-prefikset
(ikkje ei brei `/vocabulary/`-eksklusjon — `cccevno` er framleis eit
separat, ope tilfelle).

**Endra filer:**
- `.github/lychee.toml`: 1 ny eksklusjon (N1)

**Validering:**
- `.github/lychee.toml` stadfesta gyldig TOML (`tomllib`, 14
  eksklusjonar totalt) og gyldig lychee-config (containerkøyring)
- Lokal `lychee`-køyring mot det rapporterte dømet
  (`ngr-virksomhet/klasser/varslingsverdi.md`) + `index.md` for dei tre
  andre NGR-domena: **0 feil**
- Full sveip av heile `mkdocs/docs/ngr/**/*.md`: **0 feil** av 6192
  totale lenkjesjekkar, 666 korrekt ekskluderte. Éin attverande
  `[TIMEOUT]` (`brreg.no/kontakt/modellforvaltning`) er urelatert til
  denne fiksen — alt eit kjent, ope punkt i
  `specs/backlog/avvik-peikarar-til-offentlege-ressursar.md` avvik 3.
- Ingen `.yaml`-skjema endra → `make lint`/`make roundtrip` ikkje
  naudsynt. `actionlint` ikkje naudsynt (ingen workflow-fil endra).
