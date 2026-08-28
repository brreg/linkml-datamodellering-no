# Modellkatalog-datadrift: undersøkt og retta (org_uri-basert URI-policy)

## Bakgrunn

Under arbeidet med `fiks-dqv-gap-7a-7b.md` vart det oppdaga at dei 6
modellkatalog-datafilene (`src/linkml/modellkatalog/*/data/*/*.yaml`) er
sterkt utdaterte i forhold til kva `make gen-modellkatalog-instance`
(`generate-modellkatalog.py`) i dag ville produsert frå
`metadata/*-manifest.yaml`. Brukaren bad om å fikse dette. Denne specen
dokumenterer kvifor det **ikkje** er trygt å berre køyre generatoren på nytt,
og kva som må avklarast/rettast først.

## Kva er faktisk gale

Det er **ikkje** berre eit spørsmål om manglande nye modellar. Tre separate,
samanfiltra problem vart avdekte:

### 1 — Full filoverskriving øydela modellelement-data (delvis retta)

`generate-modellkatalog.py` bygde `modellkataloger`/`informasjonsmodeller` frå
botnen og skreiv over heile fila kvar gong. Dette øydela `objekttyper`,
`attributter`, `assosiasjoner`, `kodelister`, `kodeelementer`, `enkeltyper`
(sett av `gen-modelldcat-elements.py`) og `aktoerer` (manuelt vedlikehalde) —
verifisert med ei reell prøvekøyring som ville sletta **~21 000 linjer**
(sjå `novari-modellkatalog.yaml`: -13854 linjer i éin køyring).

**Retta:** `generate-modellkatalog.py` bevarer no alle toppnivånøklar han
ikkje sjølv eig, og felt på `modellkataloger[0]` (t.d. `tema`) han ikkje sjølv
set. Denne fiksen er trygg og står ved lag uavhengig av punkt 2-3 under.

### 2 — Org-URI-basen har endra seg, men er ikkje propagert konsistent

`CODEOWNERS.md` sin `org_uri` for fleire organisasjonar (bl.a. brreg,
kartverket, novari) peikar i dag til `https://data.norge.no/organizations/<orgnr>`,
medan dei committa datafilene brukar eldre, organisasjonsspesifikke domene
(`https://brreg.no/modellkatalogar/...`, `https://data.norge.no/modellkatalog/kartverket-modellkatalog/...`
utan orgnr). Ein full regenerering ville endra `modellkataloger[0].id` (og
alle avleidde `informasjonsmodeller[].id`) til det nye, org_uri-avleidde
mønsteret — dette er **dokumentert, tilsikta åtferd** i `generate-modellkatalog.py`
(«Konverterer standard URI-ar … til org-spesifikke URI-ar», jf. `COMMANDS.md`),
men kolliderer direkte med det ope, uavklara gapet «Standarder for URI-peikarar»
(gap 1 i `standardetterleving.md`) — som eksplisitt seier at URI-konstruksjonspolicyen
for desse katalogane **ikkje** er avklart enno. `brreg-modellkatalog` har til
og med ein `published-uris.lock`-fil som markerer at URI-ar skal låsast ved
publisering (endå ikkje publisert, men mekanismen signaliserer at dette er eit
medvite styrt spørsmål, ikkje noko som skal endrast som eit tilfeldig biprodukt
av ei datasynkronisering).

### 3 — Base-URI-endring lagar orphan/duplikat-element i gen-modelldcat-elements.py

`gen-modelldcat-elements.py` sin `replace_schema_scoped()` fjernar berre
eksisterande element som alt matchar **den nye** `catalog_base`-prefiksen før
han legg til friske. Dersom `catalog_base` endrar seg (jf. punkt 2), matchar
ingen av dei gamle (framleis `brreg.no`-baserte) elementa det nye prefikset —
dei vert **verande som orphanar** i staden for å bli fjerna, samstundes som
`generate-modellkatalog.py` sin eigen regenererte `inneholder_modellelement`
alt brukar den nye URI-en **og** eit anna namnemønster
(`<schema>#<KlasseNavn>` frå `generate-informasjonsmodell.py`) enn det
`gen-modelldcat-elements.py` sine `objekttyper`-element faktisk brukar
(`<schema>/<KlasseNavn>`, ingen `#`). Verifisert direkte i generert output for
`brreg-modellkatalog` (linje 110: `.../ngr-virksomhet/ngr-virksomhet#Virksomhet`
vs. eksisterande objekttype-id `.../ngr-virksomhet/Underenhet`). Å køyre begge
generatorane i rekkjefølgje ville altså **ikkje** sjølvlækt problemet — det
ville lagt att daude referansar og/eller duplikatar.

## Kvifor dette ikkje vart fiksa no

Å køyre regenereringa ville ha:
- endra publiserings-nære URI-ar for fleire reelle organisasjonar sine
  datakatalogar, midt i eit ope, uavklara policy-spørsmål (gap 1)
- introdusert daude/duplikate `objekttyper`/`attributter`/osv.-referansar pga.
  namnemønster-skilnaden i punkt 3, som verken `generate-modellkatalog.py`
  eller `gen-modelldcat-elements.py` løyser åleine

Begge er reelle, ikkje-trivielle datakonsistensrisikoar for eit repo som skal
publisere til Felles datakatalog for fleire eksterne organisasjonar. Dette
krev ei medviten avgjerd, ikkje ei mekanisk køyring.

## Tilrådd vidare arbeid (krev avgjerd før utføring)

1. **Løys gap 1 (URI-konstruksjonspolicy) fyrst** — avklar om
   `https://brreg.no/...`, `https://data.norge.no/organizations/<orgnr>/...`
   eller noko anna skal vere den faste URI-basen for kvar organisasjon sin
   modellkatalog, og lås ho (`published-uris.lock`-mekanismen finst alt for
   brreg).
2. **Rett namnemønster-skilnaden** mellom `generate-modellkatalog.py` sin
   `inneholder_modellelement`-regenerering (`<schema>#<Klasse>`) og
   `gen-modelldcat-elements.py` sine `objekttyper`-id-ar (`<schema>/<Klasse>`)
   slik at dei alltid er konsistente — anten ved at `generate-modellkatalog.py`
   sluttar å regenerere `inneholder_modellelement` sjølv (la
   `gen-modelldcat-elements.py` eige feltet fullt ut, slik docstringen hans
   alt seier), eller ved å harmonisere mønsteret.
3. **Rett `replace_schema_scoped()`** i `gen-modelldcat-elements.py` til å
   fjerne gamle element basert på schema-namn åleine (ikkje prefiks-match mot
   noverande `catalog_base`), slik at ein trygt kan endre `catalog_base` utan
   å skape orphanar.
4. **Deretter**, når 1-3 er avklart/retta: køyr full regenerering
   (`gen-informasjonsmodell-instance` → `gen-modellkatalog-instance` →
   `gen-modelldcat-elements` → `gen-dqv-measurements`) for alle 6 org og
   valider kvar fil.

## Kva som står ved lag frå denne undersøkinga

- `generate-modellkatalog.py` sin fiks for å bevare framande toppnivånøklar
  (frå `fiks-dqv-gap-7a-7b.md`) er **behalde** — han er trygg og reduserer
  blast radius uavhengig av punkt 1-3.
- Ingen datafiler er endra som del av denne specen — alle prøvekøyringar er
  reverterte (`git checkout --`).

## Avgjerd (2026-08-28)

Brukaren valde: **org_uri-basert URI er fasit.** `https://data.norge.no/organizations/<orgnr>/modellkatalogar/<slug>`
er den korrekte, faste URI-basen for kvar organisasjon sin modellkatalog.
Ingen av dei 6 orga er publisert til Felles datakatalog enno (alle
`published-uris.lock`-filer var/er tomme), så inga endring av allereie
publiserte URI-ar var i spel.

## Utført

**Steg 2-3 (generator-fiksar):**
- `generate-modellkatalog.py`: `convert_informasjonsmodell_to_org_format()`
  set ikkje lenger `inneholder_modellelement` sjølv (feltet eig
  `gen-modelldcat-elements.py` fullt ut). `main()` bevarer no eksisterande
  `inneholder_modellelement` per informasjonsmodell, matcha på skjemanamn
  (siste URI-segment) — stabilt sjølv om `catalog_base` endrar seg.
- `gen-modelldcat-elements.py`: `replace_schema_scoped()` identifiserer no
  gamle element via skjemanamnet som eit path-segment (`/<schema_name>/`) i
  staden for eit prefiks-match mot gjeldande `catalog_base` — ein
  base-URI-endring skaper difor ikkje lenger orphan-element.

**Steg 3 (URI-lås):** Oppretta tomme `published-uris.lock`-filer (same
format som brreg sin, "ikkje publisert enno") for `digdir-`, `kartverket-`,
`ksdigital-`, `novari-` og `skatteetaten-modellkatalog` — infrastrukturen er
no på plass for alle 6 org, klar til å låse URI-ar den dagen kvar org faktisk
vert publisert.

**Steg 4 (full regenerering, alle 6 org):**
1. `make gen-modellkatalog-instance` — friske `modellkataloger`/`informasjonsmodeller`
   frå `metadata/*-manifest.yaml`. `digdir` og `ksdigital` hadde allereie
   org_uri-basert URI (ingen endring); `brreg`, `kartverket`, `novari`,
   `skatteetaten` fekk ny, org_uri-avleidd `id`.
2. `make gen-modelldcat-elements` — friske `objekttyper`/`attributter`/
   `assosiasjoner`/`kodelister`/`kodeelementer`/`enkeltyper` for alle
   skjema i alle 6 org, korrekt under den (eventuelt nye) URI-basen.
3. `make gen-dqv-measurements` — friske kvalitetsmålingar under (eventuelt
   ny) URI-base.
4. **Manuell opprydding** av attverande orphan-referansar for dei 4 orga med
   endra base (`brreg`, `kartverket`, `novari`, `skatteetaten`): gamle
   `kvalitetsmaalingar`/`har_kvalitetsmaaling`/`enkeltyper`-oppføringar under
   den GAMLE basen vart fjerna (`merge_enkeltyper()` i
   `gen-modelldcat-elements.py` og id-matching i `gen-dqv-measurements.py`
   fjernar av design ikkje gamle oppføringar ved eit basisskifte — dette var
   ei eingongsopprydding for denne migreringa, ikkje ein generell scriptfiks).
   Verifisert med grep: 0 attverande referansar til gamal URI-base i alle
   6 filer.
5. **Referanseintegritet verifisert**: alle `inneholder_modellelement`-URI-ar
   matchar ein faktisk `id` blant `objekttyper` i same fil — 0 daude
   referansar i 5 av 6 org.
6. Alle 6 datafiler validerte med `make validate-instance` — «No issues
   found».

**Nytt, separat funn (ikkje retta, utanfor scope for denne migreringa):**
`digdir-modellkatalog.yaml` har 3 daude `inneholder_modellelement`-referansar
knytt til ei `katalog`-informasjonsmodell-oppføring som ikkje svarar til
nokon av dei 10 skjema `gen-modelldcat-elements.py` kjenner til for digdir.
Dette var til stades **før** denne migreringa (verifisert i HEAD før
regenerering) og heng ikkje saman med URI-basisendringa — det er ein separat,
låg-prioritert datakvalitetsfeil. Ikkje retta her.

## Kva som IKKJE er gjort

- Løyst det pre-eksisterande `katalog`-avviket i `digdir-modellkatalog.yaml`
  (sjå over).
- Faktisk publisering til Felles datakatalog (framleis eit separat,
  organisasjonsstyrt steg — `published-uris.lock`-filene er framleis tomme).
