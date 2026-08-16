# Lenkjesjekk: `schema.fintlabs.no` er ei stor kjelde til gjenståande feil

## Bakgrunn

Etter at `specs/done/lenkjesjekk-runde2-verifisering.md` sine fiksar var
implementerte, peika brukaren ut at FINT-domenet ("for fint") framleis er
ei stor kjelde til attverande lenkjesjekk-feil, med tre konkrete døme frå
`fint-arkiv`:

```
[404] https://schema.fintlabs.no/arkiv/nokkelord (nokkelord.md)
[404] https://schema.fintlabs.no/:nummerkode (nummerkode.md)
[404] https://schema.fintlabs.no/nummerkode (nummerkode.md)
[404] https://schema.fintlabs.no/arkiv/offentlighetsvurdertDato (offentlighetsvurdertdato.md)
```

Same metodikk som `specs/done/lenkjesjekk-runde2-verifisering.md`: direkte
HTTP-oppslag mot fleire URL-ar og fleire `Accept`-headerar før konklusjon
(jf. lærdomen frå den spec-en om at content negotiation kan gje falske
positivar).

## Funn

### Rotårsak: heile `schema.fintlabs.no` krev autentisering

`schema.fintlabs.no` er `default_prefix`/`fint:`-namnerommet for **alle**
FINT-domeneskjema (stadfesta i `fint-common-schema.yaml:15` og
`fint:`-prefiksdefinisjonen i `fint-administrasjon`, `fint-arkiv`,
`fint-okonomi`, `fint-personvern`, `fint-ressurs`, `fint-utdanning`), med
per-domene underprefiks (`ark:` → `/arkiv/`, `adm:` → `/administrasjon/`,
`okn:` → `/okonomi/`, `pvn:` → `/personvern/`, `res:` → `/ressurs/`,
`utd:` → `/utdanning/`). Alle `slot_uri`/`class_uri`-verdiar i desse
skjemaa nyttar eit av desse prefiksa, og gen-doc skriv den fullt utleia
URI-en inn i genererte `klasser/*.md`-sider.

Direkte oppslag stadfestar at **heile verten** er utilgjengeleg for
uinnlogga klientar, uavhengig av sti eller `Accept`-header:

```
https://schema.fintlabs.no/                          → 403 Forbidden
https://schema.fintlabs.no/arkiv/                     → 403 Forbidden
https://schema.fintlabs.no/arkiv/nokkelord            → 404 Not Found
https://schema.fintlabs.no/nummerkode                 → 404 Not Found
https://schema.fintlabs.no/administrasjon/anvist      → 404 Not Found
https://schema.fintlabs.no/okonomi/fakturagrunnlag    → 404 Not Found
```

Testa med tomt, `text/html`, `application/json` og `text/turtle`
`Accept`-headerar — **identisk resultat i alle fire tilfelle**, som
utelukkar content negotiation som forklaring (i motsetnad til
`xmlns.com`/`data.norge.no` i runde 2). Responsen sin `Via:`-header
avslører kvifor:

```
Via: 1.1 schema.fintlabs.no (Access Gateway-ag-34F4C66E92BF4ABF-187991050)
```

Dette er signaturen til eit kommersielt API-tilgangsgateway-produkt
("Access Gateway"). `schema.fintlabs.no` er altså ei portvakt-verne
API-flate, ikkje ei offentleg vokabular-dokumentasjonsside — same mønster
som `concept-catalog.fellesdatakatalog.digdir.no` (jf.
`specs/done/lenkjesjekk-3817-feil-evaluering.md` § kategori 6) og
`purl.org/adms/publishertype/PrivateIndividual` (jf.
`specs/done/lenkjesjekk-runde2-verifisering.md` § kategori B). Stadfesta
òg via Wayback Machine: **null arkiverte snapshot** nokosinne, verken for
rota (`schema.fintlabs.no`) eller for eit enkelt termoppslag
(`schema.fintlabs.no/arkiv/nokkelord`) — verten har aldri vore offentleg
gjennomsøkbar. FINT-organisasjonen sitt eige marknadsføringsdomene
(`https://fintlabs.no/`, utan `schema.`-subdomenet) er derimot levande
(200 OK) — dette stadfestar at det er nettopp `schema.`-subdomenet, som
FINT brukar til maskin-til-maskin API-identifikatorar, som er
tilgangssperra, ikkje FINT-organisasjonen sin nettstad generelt.

**Omfang:** 8330 lenkjeførekomstar fordelt på 934 filer i
`mkdocs/docs/fint/` (alle 6 FINT-domene + `fint-common`) refererer
`schema.fintlabs.no` i ei eller anna form. Dette er den klart største
enkeltkjelda til attverande lenkjesjekk-feil av alle kategoriane
undersøkt i runde 1 og runde 2.

### Biverknad: dobbel skråstrek-/kolon-feil i "native"-mapping (kosmetisk, ikkje ein eigen lenkjefeil)

`nummerkode.md` har **to** ulike, feilrapporterte URL-ar for same slot:

```
https://schema.fintlabs.no/nummerkode       (frå "self"-mapping, fint:nummerkode korrekt utleia)
https://schema.fintlabs.no/:nummerkode      (frå "native"-mapping — stray kolon)
```

Den andre kjem frå gen-doc sin **"Mappings"-tabell** (`native`-rad), som
tydeleg utleiar CURIE-en feil når prefikset er tomt/identisk med
`default_prefix` — resultatet er ein URI med ein overflødig `:` rett før
lokalnamnet. Dette er ein LinkML-docgen-eigenheit (malen/verktøyet sin
eigen CURIE-utleiingslogikk), **ikkje** noko feil i sjølve
`fint-common-schema.yaml` (slot-definisjonen på line 206–207 er korrekt:
`slot_uri: fint:nummerkode`). Sidan heile verten uansett er
utilgjengeleg (jf. rotårsaka over), er dette kosmetisk for
lenkjesjekk-formål — same eksklusjon dekkjer begge variantane av URL-en.
Verdt å merke som eit separat, lågare-prioritert dokumentasjonskvalitets-
funn dersom nokon seinare vil gjere "Mappings"-tabellen meir lesbar, men
ikkje noko å løyse som del av denne lenkjesjekk-fiksen.

## Tiltak

**F1 — Lychee-eksklusjon for heile verten (hovudtiltak).** Legg til i
`.github/lychee.toml` sin `exclude`-liste:

```toml
"^https://schema\\.fintlabs\\.no/",
```

Grunngjeving: same mønster som dei to eksisterande presedensane i denne
fila (`concept-catalog.fellesdatakatalog.digdir.no` og
`purl.org/adms/publishertype/PrivateIndividual`) — ein stadfesta,
portvakt-verna API-identifikator-vert utan offentleg, uinnlogga
tilgang. I motsetnad til `xmlns.com`/`data.norge.no` i runde 2 er dette
**ikkje** eit content negotiation-tilfelle (stadfesta med 4 ulike
`Accept`-headerar, identisk resultat) — ein per-host `headers`-oppføring
ville ikkje hjelpt her, sidan verten konsekvent avviser uinnlogga
oppslag uansett kva som vert spurt om.

**F2 — Ingen skjemaendring.** `slot_uri`/`class_uri`-verdiane i alle
FINT-skjemaa er semantisk korrekte identifikatorar for FINT sitt eige
API-namnerom — dei skal ikkje endrast. `default_prefix`/`fint:`-mønsteret
følgjer CLAUDE.md § Schema-metadata sin konvensjon for absolutt
HTTPS-URI, og FINT-namngjevingsunntaket (camelCase) er alt dokumentert
under § Slotnamn.

**F3 — Ingen tiltak for "native"-mapping-kolonartefakten.** Dekt av same
eksklusjon som F1 (begge variantar av `nummerkode`-URL-en matchar
regex-en). Ingen separat gransking av gen-doc-malen si CURIE-utleiing er
naudsynt for lenkjesjekk-formål.

## Steg

1. `.github/lychee.toml`: legg til `"^https://schema\\.fintlabs\\.no/"` i
   `exclude`-lista (etter dei to eksisterande vert-spesifikke
   eksklusjonane, for konsistent gruppering).
2. Valider TOML-syntaks (`python3 -c "import tomllib; ..."`) og faktisk
   lychee-config-lasting (containerkøyring).
3. Lokal `lychee`-verifisering mot dei fire opphavleg rapporterte filene
   (`nokkelord.md`, `nummerkode.md`, `offentlighetsvurdertdato.md`) +
   eit stikkprøve-utval frå andre FINT-domene (t.d. `fint-administrasjon`,
   `fint-okonomi`) for å stadfeste at eksklusjonen dekkjer heile
   `schema.fintlabs.no`-flata, ikkje berre `fint-arkiv`.
4. `actionlint` ikkje naudsynt (ingen `.github/workflows/*.yml` vert
   endra).
5. Ingen `make lint`/`make roundtrip` naudsynt (ingen `.yaml`-skjema vert
   endra — reint lychee-konfig-tiltak).

## Handlingsliste

- [x] F1: legg til `schema.fintlabs.no`-eksklusjon i `.github/lychee.toml`
- [x] Valider TOML-syntaks og lychee-config-lasting
- [x] Lokal lychee-verifisering mot dei rapporterte filene + stikkprøve
      frå andre FINT-domene

## Utført

Eksklusjonen `^https://schema\.fintlabs\.no/` lagt til i
`.github/lychee.toml` sin `exclude`-liste, med grunngjeving i ein
kommentar (same struktur som dei andre vert-eksklusjonane i fila).

**Biverknad retta samtidig:** dei tre eksisterande kommentarane i
`lychee.toml` som viste til `specs/backlog/lenkjesjekk-runde2-verifisering.md`
peika til feil katalog — den spec-en vart flytta til `specs/done/` i førre
arbeidsøkt. Oppdatert alle tre referansane til `specs/done/...` for at
kommentarane skal peike til rett stad.

**Endra filer:**
- `.github/lychee.toml`: 1 ny eksklusjon (F1) + 3 retta stale
  `specs/backlog/` → `specs/done/`-referansar

**Validering:**
- `.github/lychee.toml` stadfesta gyldig TOML (`tomllib`, 13 eksklusjonar
  totalt) og gyldig lychee-config (containerkøyring)
- Lokal `lychee`-køyring mot dei tre opphavleg rapporterte filene
  (`nokkelord.md`, `nummerkode.md`, `offentlighetsvurdertdato.md`):
  **0 feil** (var 5 feil i utdraget, inkl. begge `nummerkode`-variantane)
- Stikkprøve mot `index.md` for dei resterande 5 FINT-domena
  (`fint-administrasjon`, `fint-okonomi`, `fint-personvern`,
  `fint-ressurs`, `fint-utdanning`) + `fint-common`: **0 feil**
- Full sveip av heile `mkdocs/docs/fint/**/*.md` (934 filer): **0 feil**
  av 15163 totale lenkjesjekkar, 2393 korrekt ekskluderte — stadfestar at
  eksklusjonen dekkjer heile det påstadde omfanget (8330
  lenkjeførekomstar)
- Ingen `.yaml`-skjema endra → `make lint`/`make roundtrip` ikkje naudsynt
- `actionlint` ikkje naudsynt (ingen `.github/workflows/*.yml` endra)
