# Verifisering: Containerattributta-konvensjon i repoet

## Bakgrunn

CLAUDE.md (§ Modelleringsprinsipper > Slots, ikke attributes) slår fast:

> **Unntaket er containerklassen** (`tree_root: true`): her skal kvar klasse-referanse
> modellerast som eit inline `attribute` direkte under containerklassen — ikkje som
> ein global slot. Containerklassen er eit serialiseringsankerpunkt, ikkje ein
> semantisk klasse, og attributtane hennar treng ikkje `slot_uri`.

**Hypotese:** 21 av 33 skjema bryt denne regelen — dei definerer containerattributta
som globale slots i `slots:`-seksjonen.

**Oppdaga gjennom:** Analyse av skjema som har "ubrukte" slots — slots som er
definerte lokalt men ikkje brukt i lokale domenemodellklasser. Dei fleste av
desse "ubrukte" slots var rapporterte som containerattributta av SchemaView-analysen.

## Verifisering

Ved manuell gjennomgang av påverka skjema vart det klart at **hypotesen var feil**.

## Funn

### Døme: `brreg-modellkatalog-schema.yaml`

**Faktisk tilstand (RIKTIG):**

```yaml
# Ingen globale slots for containerattributta — berre attributes:

classes:
  ModellkatalogContainer:
    tree_root: true
    attributes:
      modellkataloger:
        range: Modellkatalog
        multivalued: true
        inlined: true
        inlined_as_list: true
      informasjonsmodeller:
        range: Informasjonsmodell
        multivalued: true
        inlined: true
        inlined_as_list: true
      objekttyper:
        range: Objekttype
        multivalued: true
        inlined: true
        inlined_as_list: true
      # ... andre containerattributta ...
```

**Verifisert:** Alle skjema i repoet (33/33) følgjer denne konvensjonen.

### Kvifor rapporterte analysen "ubrukte slots"?

**Rotårsak:** LinkML sitt SchemaView-API rapporterer containerattributta (frå
`attributes:`-seksjonen) som "slots" i `all_slots()`-metoden. Dette førte til at
analyse-scriptet detekterte containerattributta som "lokalt definerte slots som
ikkje vert brukt i domenemodellklasser".

**Døme frå `samt-bu`:**

```python
sv = SchemaView('samt-bu-schema.yaml')
# sv.all_slots() returnerer BÅDE:
#   - Globale slots frå slots:-seksjonen (t.d. 'navn', 'kommunenummer')
#   - Containerattributta frå attributes:-seksjonen (t.d. 'skoler', 'kommuner')
```

Containerattributta har `from_schema == schema.id`, så dei vart klassifiserte som
"lokalt definerte" — men dei vart ikkje funne i `c.slots` for domenemodellklassane,
så dei vart klassifiserte som "ubrukte".

**Konklusjon:** Analysen var teknisk korrekt (containerattributta er "ubrukte" i
domenemodellklassane), men slutninga var feil (det tyder ikkje på ein modelleringsfeil).

## Verifiserte skjema

Alle 33 skjema i repoet vart verifiserte med shell-script som søkte etter
containerklasser som brukar `slots:` i staden for `attributes:`.

**Resultat:** 0 skjema bryt konvensjonen.

### Døme på korrekt modellering

**Modellkatalog-skjema (6 stk):**
- `brreg-modellkatalog` ✅ `attributes:` (11 containerattributta)
- `digdir-modellkatalog` ✅ `attributes:`
- `kartverket-modellkatalog` ✅ `attributes:`
- `ksdigital-modellkatalog` ✅ `attributes:`
- `novari-modellkatalog` ✅ `attributes:`
- `skatteetaten-modellkatalog` ✅ `attributes:`

**NGR-skjema (5 stk):**
- `ngr-adresse` ✅ `attributes:` (18 containerattributta)
- `ngr-eiendom` ✅ `attributes:`
- `ngr-person` ✅ `attributes:`
- `ngr-virksomhet` ✅ `attributes:`
- `enhetsregisteret-bvrinn` ✅ `attributes:`

**FINT-skjema (6 stk):**
- `fint-administrasjon` ✅ `attributes:`
- `fint-arkiv` ✅ `attributes:`
- `fint-okonomi` ✅ `attributes:`
- `fint-personvern` ✅ `attributes:`
- `fint-ressurs` ✅ `attributes:`
- `fint-utdanning` ✅ `attributes:`

**Andre:**
- `samt-bu` ✅ `attributes:` (22 containerattributta)
- `brreg-begrepskatalog` ✅ `attributes:`
- `register-over-aksjeeiere` ✅ `attributes:`
- `referanse-schema` ✅ `attributes:`
- ... (alle andre skjema følgjer også konvensjonen)

## Konklusjon

**CLAUDE.md sin containerklasse-konvensjon vert følgd konsekvent i heile repoet.**

Alle skjema med `tree_root: true`-containerklasser brukar `attributes:` for
containerattributta — ingen brukar `slots:` med globale slot-definisjonar.

## Implikasjon for opphavleg problemstilling

Denne verifikasjonen vart utført i samband med evaluering av om OR-logikk
("vis lokalt definerte ELLER brukte slots/enums") skulle implementerast i
`index.md.jinja2`.

**Opphavleg hypotese:** 21 skjema ville få synleggjort containerattributta som
"slots" dersom OR-logikk vart implementert, fordi containerattributta var
feilaktig definerte som globale slots.

**Faktisk tilstand:** Containerattributta er **ikkje** definerte som globale
slots — dei er korrekt definerte som `attributes:` i containerklassen. OR-logikk
ville **ikkje** synleggjere containerattributta i slot-lista, fordi dei ikkje
finst i `slots:`-seksjonen.

**Konklusjon for OR-logikk:**

Argumentet mot OR-logikk basert på "vil synleggjere containerattributta" er
**ugyldig** — containerattributta vil ikkje bli synleggjort fordi dei ikkje er
definerte i `slots:`-seksjonen.

**MERK:** Sjølv om dette argumentet fell bort, kan det framleis finnast andre
grunnar til å ikkje implementere OR-logikk globalt. Sjå
`specs/backlog/common-ap-no-vis-alle-slots-enums.md` for fullstendig vurdering.

## Utført

**Dato:** 2026-07-11

**Arbeid:**
1. ✅ Verifiserte alle 33 skjema med shell-script
2. ✅ Manuelt inspiserte representative skjema frå kvar kategori
3. ✅ Dokumenterte funn i denne specen

**Resultat:**
- 0 skjema bryt CLAUDE.md sin containerklasse-konvensjon
- Alle skjema brukar `attributes:` i containerklassen
- Hypotesen om 21 feil-modellerte skjema var basert på SchemaView-API-artefakt

**Ingen kodeendringar nødvendige** — alle skjema er allereie korrekte.

**Oppfølging:**
- Oppdater `common-ap-no-vis-alle-slots-enums.md` til å fjerne argumentet om
  containerattributta som blokkerer for OR-logikk (dette argumentet er ugyldig)
- Vurder om OR-logikk framleis er uønskt av **andre** grunnar (t.d. vise
  legitime ubrukte slots som dead code)
