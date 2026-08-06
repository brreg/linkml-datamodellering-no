# Fjern foreldra bvrinn-eksempel.yaml

## Bakgrunn

`make linkml-convert` (via `src/assets/scripts/makefile/convert-examples.sh`) feila for
`oreg/bvrinn` med `FileNotFoundError: /work/src/linkml/oreg/bvrinn/bvrinn-schema.yaml`.

**Rotårsak, stadfesta ved kodelesing og git-historikk:**

`convert-examples.sh` reknar ut skjemastien frå eksempelfilnamnet
(`profil=$(basename "$example" -eksempel.yaml)`), og antar at dette alltid matchar
modellkatalognamnet. Det stemmer normalt, men
`src/linkml/oreg/enhetsregisteret-bvrinn/examples/` inneheld to eksempelfiler:

- `bvrinn-eksempel.yaml` — foreldra rest, lagt til i commit `7b0256ac`/`a99b5d95`
  ("finjusterer mcp-generate og make test kommandoane") frå ei tidleg testøkt der
  modellen enno heitte berre "bvrinn". Innhaldet (`Containerklasse: bvrinner:`)
  matchar ikkje dagens skjema.
- `enhetsregisteret-bvrinn-eksempel.yaml` — korrekt namngitt (matchar
  katalognamnet), lagt til i commit `00a1ea26`/`98f3d076`, med innhald som matchar
  dagens skjemaklassar (`innrapporteringer`, `virksomhetsinformasjonHovedenheter` osv.).

Den gamle `bvrinn-eksempel.yaml` vart aldri fjerna då det korrekte eksempelet vart
lagt til. Systematisk sjekk av heile repoet stadfestar at dette er det einaste
tilfellet av eksempelfilnamn som ikkje matchar katalognamnet — ikkje eit
systematisk problem i `convert-examples.sh` sin logikk.

## Steg

1. **Slett** `src/linkml/oreg/enhetsregisteret-bvrinn/examples/bvrinn-eksempel.yaml`
   (foreldra, ikkje referert nokon annan stad — stadfesta med grep).
2. **Test:** køyr `LOGLVL=DEBUG make linkml-convert DOMAIN=oreg` (eller tilsvarande)
   og stadfest at:
   - `oreg/bvrinn` ikkje lenger dukkar opp i discovery-lista
   - `oreg/enhetsregisteret-bvrinn` framleis vert korrekt konvertert til RDF/Turtle

## Handlingsliste

- [x] Slett `bvrinn-eksempel.yaml`
- [x] Køyr `make domain-oreg` og stadfest fiksen

## Utført

Sletta `src/linkml/oreg/enhetsregisteret-bvrinn/examples/bvrinn-eksempel.yaml`.

Verifisert med `LOGLVL=DEBUG make domain-oreg`:
- `linkml-convert`-discovery viser no korrekt `oreg/enhetsregisteret-bvrinn,oreg/register-over-aksjeeiere`
  — `oreg/bvrinn` er borte, og `FileNotFoundError` for `oreg/bvrinn/bvrinn-schema.yaml` oppstår ikkje lenger
- Ingen andre referansar til `bvrinn-eksempel.yaml` fanst i repoet (stadfesta med grep før sletting)

**Følgjefunn (utanfor scope for denne specen):** køyringa avdekte ein separat,
førebels ukjend feil i sjølve `enhetsregisteret-bvrinn-eksempel.yaml`-konverteringa
(`ValueError: Unknown CURIE prefix: @base`), som tidlegare var skjult fordi
pipelinen alltid feila på `bvrinn`-oppføringa først. Ikkje handtert her — rapportert
til brukar, avventar eiga avklaring/spec.
