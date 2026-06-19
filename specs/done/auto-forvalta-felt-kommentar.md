# Kommentar om automatisk forvalta felt i LinkML-skjema

## Bakgrunn

Tre felt i kvar skjema-YAML-fil vert no forvalta automatisk av CI:

| Felt | Forvaltingsmekanisme |
|---|---|
| `version` | release-please oppdaterer via JSONPath (`$.version`) i `release-please-config.json` |
| `annotations.endringsdato` | `update-schema-dates.py` set til releasedato etter kvar release |
| `annotations.utgivelsesdato` | `update-schema-dates.py` set til releasedato ved første release |

Ein bidragsytar som opnar ei skjemafil ser desse felta og kan forvente å redigere
dei manuelt — det gjer dei ikkje. Utan eit tydeleg signal er dette ein usynleg
konvensjon som krev at ein har lest dokumentasjon ein kanskje aldri har sett.

---

## Kartlegging av annotations-tilstand

Alle 22 skjema registrerte i `release-please-config.json` er kartlagde.
Kolonnane viser tilstedevær av toppnivå-`annotations:`-blokk og kvart underfelt.

| Skjema | `ann` | `utgiver` | `endringsdato` | `utgivelsesdato` | `status` |
|---|:---:|:---:|:---:|:---:|:---:|
| ap-no/cpsv-ap-no | ✓ | ✓ | ✓ | ✓ | ✓ |
| ap-no/dcat-ap-no | ✓ | ✓ | ✓ | ✓ | ✓ |
| ap-no/dqv-ap-no | ✓ | ✓ | ✓ | ✓ | ✓ |
| ap-no/modelldcat-ap-no | ✓ | ✓ | ✓ | ✓ | ✓ |
| ap-no/skos-ap-no | ✓ | ✓ | ✓ | ✓ | ✓ |
| fair/fair-metadata | ✓ | ✓ | ✓ | ✓ | ✓ |
| fint/fint-administrasjon | ✓ | ✓ | ✓ | ✓ | ✓ |
| fint/fint-arkiv | ✓ | ✓ | ✓ | ✓ | ✓ |
| fint/fint-common | ✓ | ✓ | ✓ | ✓ | ✓ |
| fint/fint-okonomi | ✓ | ✓ | ✓ | ✓ | ✓ |
| fint/fint-personvern | ✓ | ✓ | ✓ | ✓ | ✓ |
| fint/fint-ressurs | ✓ | ✓ | ✓ | ✓ | ✓ |
| fint/fint-utdanning | ✓ | ✓ | ✓ | ✓ | ✓ |
| ngr/ngr-adresse | ✓ | ✓ | ✓ | ✓ | ✓ |
| ngr/ngr-eiendom | ✓ | ✓ | ✓ | ✓ | ✓ |
| ngr/ngr-person | ✓ | ✓ | ✓ | ✓ | ✓ |
| ngr/ngr-virksomhet | ✓ | ✓ | ✓ | ✓ | ✓ |
| samt/samt-bu | ✓ | ✓ | ✓ | ✓ | ✓ |
| **begrepskatalog/brreg-begrepskatalog** | ✓ | ✓ | **✗** | **✗** | ✓ |
| **modellkatalog/brreg-modellkatalog** | ✓ | ✓ | **✗** | **✗** | ✓ |
| **oreg/register-over-aksjeeiere** | ✓ | ✓ | **✗** | **✗** | ✓ |
| **referanse/referanse** | **✗** | **✗** | **✗** | **✗** | **✗** |

### Gruppe A — Fullstendige (18 skjema)

Alle auto-forvalta felt er til stades. Ingen annotations-tiltak nødvendig.

### Gruppe B — Manglande datofelt (3 skjema)

`brreg-begrepskatalog`, `brreg-modellkatalog` og `register-over-aksjeeiere` har
`annotations:`-blokk med `utgiver` og `status`, men manglar `endringsdato` og
`utgivelsesdato`.

`update-schema-dates.py` vil leggje til begge felta automatisk ved neste release.
Men inntil ein release skjer ligg desse skjemaa i ein inkonsistent tilstand:
`utgiver` og `status` er dokumentert som silver-krav, medan datofelta ikkje er det.

**Anbefalt tiltak:** legg til `endringsdato` og `utgivelsesdato` manuelt no, med
`"TODO"` som verdi eller dagens dato — så er blokka komplett og `update-schema-dates.py`
tek over ved neste release.

### Gruppe C — Manglande heile annotations-blokk (1 skjema)

`referanse/referanse-schema.yaml` har ingen toppnivå-`annotations:`-blokk.
Skjemaet er eit annotert referanse-/tutorial-skjema utan `manifest.yaml` og
utan `publish_external: true`. Det er registrert i `release-please-config.json`
og får `version:` oppdatert automatisk.

Klasse-nivå-`annotations:` (for `begrepsidentifikator`) finst og skal bevarast.

**Anbefalt tiltak:** legg til full toppnivå-`annotations:`-blokk med alle fire
felt (`utgiver`, `endringsdato`, `utgivelsesdato`, `status`) — same mønster som
dei 18 fullstendige skjemaa. Dette gjer at `update-schema-dates.py` kan oppdatere
datofelta ved neste release, og at skjemaet tener som heilskapleg referanseeksempel
for bidragsytarar.

---

## Risikovurdering: kommentarplassering

### Alternativ A — Inline-kommentar på `version:`-linja

```yaml
version: "1.0.0"  # Automatisk oppdatert av release-please — ikkje rediger manuelt
```

**Risiko: medium.** release-please brukar `yaml` npm-pakken sin `Document`-modus
som *kan* bevare kommentarar, men dette er ikkje garantert på tvers av versjonar
og JSONPath-oppdateringslogikk. Dersom pakken skriv om verdien med enkel strengerstatning
vert inline-kommentaren bevart; dersom den brukar full YAML-reserialiserering kan
kommentaren forsvinne stille.

### Alternativ B — Blokk-kommentar rett over `annotations:`

```yaml
# version, endringsdato og utgivelsesdato vert forvalta automatisk av CI — ikkje rediger manuelt
annotations:
  utgiver: https://...
  endringsdato: "2026-06-10"
  utgivelsesdato: "2023-01-01"
```

**Risiko: låg.** release-please rører ikkje `annotations:`-blokka.
`update-schema-dates.py` si regex `^(annotations:\n)` set inn `endringsdato` rett
etter opningslinjen — ein kommentar *over* `annotations:` (ikkje mellom `annotations:`
og `endringsdato:`) vert ikkje påverka.

Gjeld ikkje for `referanse` (gruppe C, ingen toppnivå-`annotations:`).

### Alternativ C — Filhovud-kommentar (før `id:`)

```yaml
# version, endringsdato og utgivelsesdato vert automatisk oppdatert av CI.
# Sjå CONTRIBUTING.md for detaljar om kva som er manuelt vs. automatisk.
id: https://data.norge.no/ngr/ngr-adresse
name: ngr-adresse
version: "1.0.0"
```

**Risiko: lågast.** Heilt øvst i fila, release-please rører ikkje filhovud-kommentarar.
Synleg uavhengig av om skjemaet har `annotations:` eller ikkje.
`referanse-schema.yaml` har allereie eit slikt hovud og er ein naturleg mal.

---

## Anbefaling

**Bruk alternativ C (filhovud-kommentar) som primærtilnærming**, supplert med
dokumentasjon i `CONTRIBUTING.md` (tiltak 2).

Grunngjeving:
- Lågast risiko for utilsikta sletting av kommentar
- Synleg for alle skjema, ikkje berre dei med `annotations:`
- Konsistent med mønsteret i `referanse-schema.yaml`
- Éin stad per fil — ikkje spreidde kommentarar ved fleire felt

**Format (to liner, kortast mogleg):**

```yaml
# version, endringsdato og utgivelsesdato vert automatisk oppdatert av CI.
# Sjå CONTRIBUTING.md for detaljar om kva som er manuelt vs. automatisk.
```

Lenke til `CONTRIBUTING.md` gjer kommentaren sjølv-forklarande utan å duplisere
logikk i kvar fil.

---

## Tilleggsdokumentasjon

`CONTRIBUTING.md` manglar ein seksjon om automatisk forvalta felt. Ein bidragsytar
som les onboarding-dokumentet vil ikkje vite at desse felta er handterte av CI.

Ny seksjon «Automatisk forvalta felt» bør plasserast mellom «Generer artefakter lokalt»
og «Commit-meldingar» og innehalde:

- Kva tre felt som er auto-forvalta og av kva mekanisme
- Eksplisitt instruksjon om å **ikkje** redigere desse manuelt
- Kort forklaring av kva som utløyser oppdatering (merge av release-PR)

---

## Tiltak

| # | Tiltak | Omfang | Prioritet | Status |
|---|---|---|---|---|
| 1 | Legg til to-linja filhovud-kommentar i alle 22 release-please-forvalta skjema | 22 filer (script) | Høg | ✓ `add-schema-header-comments.py` køyrt; alle 22 oppdatert |
| 2 | Legg til seksjon «Automatisk forvalta felt» i `CONTRIBUTING.md` | 1 fil | Høg | ✓ Seksjon lagt til mellom «Generer artefakter lokalt» og «Commit-meldingar» |
| 3 | Legg til `endringsdato` og `utgivelsesdato` i gruppe B-skjema (3 stk.) | 3 filer | Medium | ✓ Lagt til med verdi `"TODO"` i `brreg-begrepskatalog`, `brreg-modellkatalog`, `register-over-aksjeeiere` |
| 4 | Legg til full toppnivå-`annotations:`-blokk i gruppe C-skjema (`referanse-schema.yaml`) | 1 fil | Medium | ✓ Full blokk lagt til med `utgiver: TODO` og `"TODO"`-datoar |

### Implementeringsnotat for tiltak 1

Kommentaren skal leggjast til som dei **to første linjene** i fila (før `id:`),
unntatt skjema som allereie har ein eksisterande filhovud-kommentarblokk — der
vert dei to linjene sett inn som siste linje(r) i den eksisterande blokka.

Kan implementerast med eit kort Python-script som les `release-please-config.json`,
finn kvar skjemafil, og set inn kommentaren viss han ikkje allereie finst.

### Implementeringsnotat for tiltak 3

For dei tre gruppe B-skjemaa: legg til etter `status:`-linja i `annotations:`-blokka:

```yaml
  endringsdato: "TODO"
  utgivelsesdato: "TODO"
```

`update-schema-dates.py` vil overskrive `"TODO"`-verdiane ved neste release.
Alternativt kan ein sette inn dagens dato direkte.

## Utført

- **Tiltak 1**: Python-script `src/assets/scripts/add-schema-header-comments.py` skriven og køyrt. Alle 22 skjema fekk 2-linja hovudkommentar. `referanse-schema.yaml` sin eksisterande `##`-blokk vart utvida med `##`-prefiks på dei to nye linjene.
- **Tiltak 2**: Seksjon «Automatisk forvalta felt» lagt til i `CONTRIBUTING.md` mellom «Generer artefakter lokalt» og «Commit-meldingar» med tabell og forklaring.
- **Tiltak 3**: `endringsdato: "TODO"` og `utgivelsesdato: "TODO"` lagt til i `brreg-begrepskatalog-schema.yaml`, `brreg-modellkatalog-schema.yaml` og `register-over-aksjeeiere-schema.yaml`. Feltrekkjefølgje: `utgiver → endringsdato → utgivelsesdato → status` (same som gruppe A).
- **Tiltak 4**: Full toppnivå-`annotations:`-blokk lagt til i `referanse-schema.yaml` med `utgiver: TODO`, `endringsdato: "TODO"`, `utgivelsesdato: "TODO"`, `status: UnderDevelopment`. `update-schema-dates.py` vil fylle inn datoane ved neste release.

---

### Implementeringsnotat for tiltak 4

Legg til full toppnivå-`annotations:`-blokk i `referanse/referanse-schema.yaml`
etter `description:`-feltet på toppnivå (same plassering som i andre skjema).
Blokka skal innehalde alle fire silver-felt:

```yaml
annotations:
  utgiver: https://data.norge.no/organizations/991825827
  endringsdato: "TODO"
  utgivelsesdato: "TODO"
  status: http://purl.org/adms/status/UnderDevelopment
```

`update-schema-dates.py` vil oppdatere `endringsdato` og setje endeleg
`utgivelsesdato` ved neste release. `utgiver` og `status` må settast manuelt
til korrekte verdiar for dette skjemaet.
