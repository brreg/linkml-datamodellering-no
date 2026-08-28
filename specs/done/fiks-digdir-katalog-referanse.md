# Fiks gap 10: daude inneholder_modellelement-referansar i digdir-modellkatalog

## Bakgrunn

`specs/done/modellkatalog-datadrift-undersokt.md` fann 3 daude
`inneholder_modellelement`-referansar i `digdir-modellkatalog.yaml`, knytt
til informasjonsmodell-oppføringa for `modelldcat-katalog`-skjemaet (id
sluttar på `.../katalog`, ikkje `.../modelldcat-katalog`).

## Rotårsak

`modelldcat-katalog-schema.yaml` og `modelldcat-modell-schema.yaml` har
med vilje eit kortare siste-segment i sjølve `id:`-URIen enn LinkML
`name:`-feltet:

| Skjema | `id:` (siste segment) | `name:` |
|---|---|---|
| `modelldcat-katalog` | `katalog` | `modelldcat-katalog` |
| `modelldcat-modell` | `modell` | `modelldcat-modell` |

`entry_name()` i `update-modellkatalog.py` (delt av `gen-modelldcat-elements.py`
og `update-modellkatalog.py`) avleia schema-namnet frå informasjonsmodell-
oppføringa sin eigen `id` (siste path-segment) — som for desse to skjema vert
`katalog`/`modell`, ikkje `modelldcat-katalog`/`modelldcat-modell`. Sidan
`gen-modelldcat-elements.py` looper over skjema via `schema["name"]`
(`modelldcat-katalog`), matcha aldri `"modelldcat-katalog" in entry_by_name`
— oppføringa sin `inneholder_modellelement` vart difor aldri oppdatert, og
sat att med gamle/feil verdiar frå før denne join-logikken fanst.

## Fiks

`entry_name()` avleier no schema-namnet frå
`informasjonsmodellidentifikator` (mkdocs-URL `.../<domain>/<modell>/`,
sett av `generate-informasjonsmodell.py` frå katalogmappenamnet — alltid
identisk med LinkML `name:`), med fallback til den gamle id-baserte
logikken når feltet manglar. Dette er ein presis, ikkje-øydeleggjande fiks:
ingen URI-ar vert endra, berre ein intern oppslagsnøkkel.

## Steg

1. Rett `entry_name()` i `update-modellkatalog.py`.
2. Køyr `make gen-modelldcat-elements ORG=digdir` på nytt og stadfest at
   `modelldcat-katalog`- og `modelldcat-modell`-oppføringane sine
   `inneholder_modellelement` no peikar til dei faktiske objekttypane.
3. Sjekk om andre org/skjema hadde same, hittil usynlege, join-feil (ikkje
   berre digdir) — køyr full referanseintegritets-sjekk for alle 6 org.
4. Valider alle påverka datafiler med `make validate-instance`.
5. Oppdater `standardetterleving.md`: marker gap 10 lukka.

## Utført

1. `entry_name()` i `update-modellkatalog.py` retta til å avleie schema-namn
   frå `informasjonsmodellidentifikator` (fallback til gamal id-basert logikk).
2. `make gen-modelldcat-elements ORG=digdir` køyrd på nytt. Verifisert med
   Python-skript: 0 daude `inneholder_modellelement`-referansar (var 3).
   Både `modelldcat-katalog`- og `modelldcat-modell`-oppføringane har no
   korrekt `inneholder_modellelement` (3 og 25 element).
3. Sjekka alle 6 org for tilsvarande join-feil (skjema prosessert av
   `gen-modelldcat-elements.py` utan tilhøyrande `informasjonsmodeller`-
   oppføring). Fann **eitt nytt, separat problem**, uavhengig av
   `entry_name()`-fiksen:

   **Nytt funn:** 6 `oreg`-skjema (`enhetsregisteret_bvrbekreftelse`,
   `enhetsregisteret_bvrettersendingavvedlegg`, `enhetsregisteret_bvrfriv`,
   `enhetsregisteret_bvrinnfelles`, `enhetsregisteret_bvrstiftelsesdokument`,
   `enhetsregisteret_frivilligorganisasjonapi`) manglar heilt
   `metadata/*-manifest.yaml` (aldri køyrd `make gen-informasjonsmodell-instance`
   for dei). `generate-modellkatalog.py` hoppar difor over dei heilt (ingen
   `informasjonsmodeller`-oppføring), medan `gen-modelldcat-elements.py`
   brukar ein annan org-/skjemaoppslagsmekanisme og PROSESSERER dei likevel
   — dette skapte **orphan-modellelement** (91 objekttyper, 251 attributter,
   108 assosiasjonar, 10 kodelister, 50 kodeelement) i
   `brreg-modellkatalog.yaml` under den førre "modellkatalog-datadrift"-
   regenereringa (verifisert: 0 referansar til desse 6 skjema i HEAD før
   nokon av dagens endringar — orphaninga var eit utilsikta biprodukt av
   gap 9-arbeidet, ikkje noko som fanst frå før).

   **Handtert:** dei orphane objekttyper/attributter/assosiasjonar/
   kodelister/kodeelement-oppføringane for dei 6 skjema er fjerna frå
   `brreg-modellkatalog.yaml` (delte `enkeltyper` er **ikkje** rørt — dei er
   ikkje skjema-skopa i id-en sin, og trygg fjerning krev å vite om dei er
   attgjenbrukte av andre, framleis gyldige skjema). Dette er ei
   eingongsopprydding, ikkje ein permanent fiks av det underliggande gapet
   (manglande metadata for 6 skjema) — sjå eige gap under.
4. Alle 6 org sine datafiler validerte med `make validate-instance` — «No
   issues found».
5. `standardetterleving.md` oppdatert: gap 10 lukka. Nytt gap 11 lagt til
   for det manglande metadata-gapet for dei 6 `oreg`-skjema.

## Ikkje gjort

Generering av manglande `metadata/*-manifest.yaml` for dei 6 `oreg`-skjema
(`make gen-informasjonsmodell-instance` per skjema) — dette ville lagt dei
tilbake i `brreg-modellkatalog.yaml` sin `informasjonsmodeller`-liste på
riktig vis, men er eit separat, ikkje-triviell stykke arbeid (krev å
verifisere kvart skjema sine annotasjonar/CODEOWNERS-oppslag er komplette
først) og var ikkje del av det brukaren bad om her (gap 10). Sjå nytt gap 11
i `standardetterleving.md`.
