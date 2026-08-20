# Plan: `NAME=<modell>`-parameter for `analyse-similar-*`

## Bakgrunn

Brukaren ønskjer at dei fire `analyse-similar-*`-targeta (`analyse-
similar-classes-domain`, `analyse-similar-classes-all`, `analyse-
similar-slots-domain`, `analyse-similar-slots-all`) skal få ein ny,
valfri parameter **`NAME=<modell>`** som avgrensar samanlikninga til
**berre klassar/slots frå den eine, namngjevne modellen** — sjekka mot
resten av kandidatane **innanfor same domene** for `-domain`-varianten,
og mot resten av kandidatane **på tvers av heile repoet** for
`-all`-varianten. `NAME=` endrar altså **ikkje** kva for kandidatar som
er aktuelle (det styrer `--scope`/target-valet framleis, uendra) — han
avgrensar berre **kven av dei to sidene i kvart par** som må vere målmodellen,
i staden for det noverande full-pairwise-oppsettet der alle skjema
(innanfor scopet) samanliknast mot alle andre.

**Konkret motivasjon (JavaZone-demoen):** rett etter at du har limt inn
nye klassar/slots i eit skjema (demo-scriptet sitt steg 5), vil du vite
«kolliderer *desse* namna med noko *anna* i repoet?» — ikkje det breiare
«finn alle namnekollisjonar i heile/same domene». `NAME=` gjer akkurat
det spørsmålet billegare å stille (mindre støy i output, og — som
biprodukt — færre samanlikningar å rekne ut).

## Noverande arkitektur (kort oppsummering)

`find-similar-names.py` (kalla av alle fire targeta, sjå
`make/91-modell-analyse.mk`):

1. `discover_schemas(domain)` — finn alle `*-schema.yaml` i repoet,
   valfritt avgrensa til éin `--domain`
2. `load_entries(schema, kind)` — hentar (namn, ekstra-info) for kvart
   `classes:`/`slots:`-oppslag i **eitt** skjema
3. `entries` — flat liste av `(namn, ekstra, skjema-sti)` for **alle**
   oppdaga skjema
4. Dobbel løkke over `entries × entries` (kvadratisk), hoppar over par
   frå same skjemafil (`schema_a == schema_b`) og — for `--scope
   domain` — par frå ulikt domene

`NAME=` krev ei **strukturell** endring av steg 4, ikkje berre eit nytt
filter oppå det eksisterande: i staden for full `entries × entries`,
må målet vere **`target_entries × resten_av_entries`** — kvart par MÅ
ha minst éi side frå den namngjevne modellen. Dette er òg billegare å
rekne ut (O(target × resten) i staden for O(n²)).

## Design

### Ny CLI-flagg i `find-similar-names.py`

```
--name <modell>   Avgrens til éin modell (t.d. javazonetalk) — samanliknar
                   berre denne modellen sine klassar/slots mot resten av
                   kandidatane som --scope alt definerer (same domene for
                   "domain", heile repoet for "all"), sjå Samspel under
```

### Namneoppløysing: `NAME` → skjemasti

Repoet sin katalogkonvensjon er `src/linkml/<domain>/<modell>/<modell>-
schema.yaml` (jf. `CONVENTIONS.md`). `NAME` åleine gjev ikkje domenet —
difor:

- **`DOMAIN` + `NAME` gitt saman** (som `new-modell`/`remove-modell`):
  slå opp direkte, `src/linkml/<domain>/<name>/<name>-schema.yaml`. Feil
  tydeleg (`FEIL: fann ikkje <sti>`) dersom fila ikkje finst.
- **`NAME` gitt åleine** (ingen `DOMAIN`): søk
  `src/linkml/*/<name>/<name>-schema.yaml` på tvers av alle domene.
  - **0 treff** → feil: `FEIL: fann ingen modell med namn '<name>' i
    src/linkml/`
  - **1 treff** → bruk han
  - **>1 treff** (usannsynleg, men mogleg — same modellnamn i to
    domene) → feil, be brukaren presisere med `DOMAIN=` òg

### Samspel med `--scope`/`--domain`

**Retta etter tilbakemelding:** `--name` overstyrer **ikkje**
`--scope`. Han legg berre til éin ekstra føresetnad ("minst éi side av
paret må vere målmodellen") oppå det eksisterande scope-filteret, som
elles er heilt uendra:

- **`--scope domain --name <modell>`** (dvs. `analyse-similar-*-domain
  NAME=<modell>`): samanliknar målmodellen **berre mot andre modellar i
  same domene** — identisk domeneavgrensing som `-domain`-varianten
  alltid har hatt, berre no avgrensa til éi namngjeven modell på den
  eine sida av kvart par i staden for alle modellar i domenet mot
  kvarandre
- **`--scope all --name <modell>`** (dvs. `analyse-similar-*-all
  NAME=<modell>`): samanliknar målmodellen **mot heile repoet**, alle
  domene

Dette er ei rein innsnevring av det eksisterande scope-omgrepet — same
`if args.scope == "domain" and schema_domain(schema_a) !=
schema_domain(schema_b): continue`-filteret (linje 109 i noverande
kode) held fram uendra, det vert berre no berre evaluert for
target×resten-par i staden for alle×alle-par (sjå Algoritme-endring
under). `--domain` (utan `--name`) fungerer framleis identisk med i
dag — uendra åtferd for eksisterande bruk.

**Konsekvens for `make`-targeta:** `NAME=` legg til presis den same
avgrensinga som targetet allereie skildrar i namnet sitt (`-domain`
kontra `-all`) — brukaren treng ikkje lære noko nytt scope-omgrep, berre
at `NAME=` no òg finst som eit filter på **kva for eine sida** av kvart
par som må vere målmodellen.

### Algoritme-endring

```python
if args.name:
    target_path = resolve_name(args.name, args.domain)  # ny funksjon, sjå over
    target_entries = [e for e in entries if e[2] == target_path]
    other_entries = [e for e in entries if e[2] != target_path]
    pairs = (
        (a, b) for a in target_entries for b in other_entries
    )
else:
    pairs = (
        (entries[i], entries[j])
        for i in range(len(entries))
        for j in range(i + 1, len(entries))
    )

for name_a, extra_a, schema_a in ...:  # frå pairs, sjå over
    for name_b, extra_b, schema_b in ...:
        if schema_a == schema_b:
            continue
        if args.scope == "domain" and schema_domain(schema_a) != schema_domain(schema_b):
            continue  # UENDRA — gjeld no target×resten-para, ikkje alle×alle
        ...
```

(Illustrativt — eksisterande kode brukar `enumerate`/slicing, ikkje
`range`-indeksering; behald eksisterande stil ved implementering.
**Viktig:** `args.scope`-sjekket (domenefilteret) skal **ikkje**
fjernast eller endrast — han er det som gjer at `--name` respekterer
`-domain`/`-all`-skiljet i staden for alltid å søkje repo-vidt. Same
`schema_a == schema_b`-skip, `seen_pairs`-deduplisering og
terskel-filter som i dag gjeld elles uendra inni løkka.)

### Rapporttittel

Når `--name` er aktiv, byt tittel-linja til å nemne modellen **i
tillegg til** eksisterande scope-tekst (som held fram uendra):

```
# Liknande klassenavn (modell oreg/javazonetalk, same domene, domene oreg, terskel 80%)
# Liknande klassenavn (modell oreg/javazonetalk, alle domene, terskel 80%)
```

i staden for dagens (uendra når `--name` ikkje er gitt)

```
# Liknande klassenavn (same domene, domene oreg, terskel 80%)
# Liknande klassenavn (alle domene, terskel 80%)
```

## Make-targeta

`make/91-modell-analyse.mk` — alle fire targeta får `[NAME=<modell>]`
lagt til i `##`-kommentaren og `--name $(NAME)` vidaresendt når sett:

```make
analyse-similar-classes-domain: ## Finn klasser med liknande navn innanfor same domene [DOMAIN=<domene>] [NAME=<modell>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-classes-domain) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --kind class --scope domain --threshold $(SIMILARITY_THRESHOLD) \
	  $(if $(DOMAIN),--domain $(DOMAIN)) $(if $(NAME),--name $(NAME))
```

(tilsvarande for dei tre andre targeta).

## Bruk (etter implementering)

```bash
# Berre mot andre modellar i SAME DOMENE (oreg) — -domain-varianten:
make analyse-similar-classes-domain NAME=javazonetalk

# Presiser domenet dersom modellnamnet finst i fleire domene:
make analyse-similar-classes-domain DOMAIN=oreg NAME=javazonetalk

# Mot HEILE REPOET, alle domene — -all-varianten:
make analyse-similar-classes-all NAME=javazonetalk

# Same for slots:
make analyse-similar-slots-domain NAME=javazonetalk
make analyse-similar-slots-all NAME=javazonetalk
```

## Handlingsliste

1. [x] Legg til `resolve_name(name, domain)` i `find-similar-names.py`
   (sjå Namneoppløysing over) — eiga, testbar funksjon
2. [x] Legg til `--name`-CLI-flagg
3. [x] Endre hovudløkka til target×resten-samanlikning når `--name` er
   gitt (sjå Algoritme-endring), behald eksisterande full-pairwise-veg
   uendra når `--name` **ikkje** er gitt (bakoverkompatibelt — ingen
   endring i noverande bruk utan `NAME=`)
4. [x] Oppdater rapport-tittel-linja til å nemne modellen når `--name`
   er aktiv
5. [x] Oppdater alle fire targeta i `make/91-modell-analyse.mk`
   (`##`-kommentar + `--name`-vidaresending)
6. [x] Verifiser:
   - `make analyse-similar-classes-domain NAME=javazonetalk` finn same
     treff som full-pairwise ville funne innanfor domenet, men **ikkje**
     noko anna urelatert klassepar (stadfestar target×resten, ikkje full
     pairwise) — stadfesta med 4 treff (t.d. `JavazonetalkContainer` mot
     `GeneratedContainer`/`AksjeeierContainer`/`LunchregisteretContainer`,
     `Javazonetalk` mot `Ansvarsandel`)
   - `make analyse-similar-classes-domain DOMAIN=oreg NAME=javazonetalk`
     gjev identisk resultat (eksplisitt DOMAIN skal ikkje endre noko når
     namnet uansett er unikt) — stadfesta: same 4 treff, berre
     "N klasser sjekka"-nemnaren skil seg (529 mot 63, sidan DOMAIN
     avgrensar `discover_schemas()` sin kandidatpool, ikkje sjølve treffa)
   - `make analyse-similar-classes-all NAME=javazonetalk` finn **minst
     dei same** treffa som `-domain`-varianten, **pluss** treff frå andre
     domene — stadfesta: 29 treff (mot 4 for `-domain`), inkl. treff frå
     `ngr-virksomhet`, `fint-arkiv`, `modellkatalog-*` m.fl.
   - `NAME=finst-ikkje` gjev tydeleg feilmelding
     (`FEIL: fann ingen modell med namn 'finst-ikkje' i src/linkml`),
     ikkje traceback — stadfesta
   - Eksisterande bruk **utan** `NAME=` er heilt uendra — stadfesta
     both direkte (`find-similar-names.py` utan `--name`, identisk
     tittel-/tabellformat) og via `make -n analyse-similar-classes-domain
     DOMAIN=oreg` (ingen `--name`-flagg i den genererte kommandolinja)
7. [ ] Vurder om `javazone-demo-script.sh` sine steg 7/8
   (`analyse-similar-classes-domain`/`-slots-domain`) burde byte til
   `NAME=$NAME` no som parameteren finst — reduserer output frå "alle
   treff i domenet" til "berre treff for javazonetalk". **Ikkje** gjer
   dette som del av same endring utan å spørje brukaren fyrst — reint
   opsjonelt oppfølgingssteg, ikkje utført

## Utført

- `src/assets/scripts/makefile/find-similar-names.py`: ny
  `resolve_name(name, domain)`, nytt `--name`-flagg, hovudløkka bygg no
  `target_entries × other_entries`-par når `--name` er gitt (elles
  uendra full-pairwise), domene-scope-filteret (linje "if args.scope ==
  domain...") står urørt inni løkka — verkar no berre på target×resten-
  para. Rapporttittelen viser `modell <domain>/<name>` når aktiv.
- `make/91-modell-analyse.mk`: alle fire `analyse-similar-*`-targeta har
  no `[NAME=<modell>]` i `##`-kommentaren og `$(if $(NAME),--name
  $(NAME))` vidaresendt.
- **Verifisert** direkte med `python3 find-similar-names.py` (podman
  rootless utilgjengeleg i verktøymiljøet, men scriptet krev ikkje
  LinkML-runtime — reint `pyyaml`, difor testbart direkte): alle
  scenario i handlingsliste punkt 6 stadfesta korrekte, inkludert at
  `-all`-varianten faktisk finn eit strengt supersett av `-domain`
  sine treff når `NAME=` er sett (29 mot 4 par).
- **Verifisert** make-wiring med `make -n` (dry-run, ingen podman-kall):
  `NAME=javazonetalk` gjev `--name javazonetalk` i den genererte
  kommandolinja; utan `NAME` manglar `--name`-flagget heilt (ingen
  regresjon).
- Punkt 7 (bytte demo-scriptet sine steg 7/8 til `NAME=$NAME`) er **ikkje**
  utført — ståande, opsjonelt oppfølgingsspørsmål til brukaren, som
  spesifisert.
