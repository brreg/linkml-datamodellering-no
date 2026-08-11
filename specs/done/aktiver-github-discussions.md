# Aktivere GitHub Discussions med velkomsttekst

## Bakgrunn

Brukaren skal aktivere GitHub Discussions for repoet og treng ein
velkomsttekst (nynorsk) til «General»-kategorien, basert på GitHub sin
standardmal. Aktivering av Discussions skjer i GitHub sitt repo-UI
(Settings → Features → Discussions) — dette er ei administrativ handling
utanfor versjonskontroll som brukaren må utføre sjølv, på same måte som
andre GitHub-innstillingar.

`CONTRIBUTING.md` nemner allereie Discussions to stader, men med atterhald
om at det ikkje er aktivert enno:

- linje 218: «Community-driven feilsøking via GitHub Issues og Discussions»
- linje 235 (Bidragsytarar sitt ansvar): «Hjelper andre brukarar i GitHub
  Discussions **(dersom aktivert)**»

README.md har ingen omtale av Discussions i det heile. Når Discussions vert
aktivert bør desse referansane oppdaterast/leggjast til, slik at
dokumentasjonen peikar brukarar dit for spørsmål og idéutveksling — skilt
frå Issues, som er for bug-rapportar og konkrete endringsforslag.

## Avklarte val

1. **Ingen ny fil for velkomsttekst:** Discussions-velkomstteksten er eit
   innlegg i «General»-kategorien, ikkje ein fil GitHub les frå repoet
   (i motsetnad til issue-malar under `.github/ISSUE_TEMPLATE/`). Teksten
   vert difor levert i denne specen for brukaren å lime inn manuelt —
   det vert ikkje oppretta noka `.github/`-fil for han.
2. **Lenkjer leggjast til tre stader** (vurdert mot resten av
   dokumentasjonen):
   - `README.md`, seksjonen «Avgrensingar» — ny linje for spørsmål/idear,
     ved sida av den eksisterande «Rapporter nye problem»-linja for bugs.
   - `CONTRIBUTING.md` linje 218 — legg til lenkje til Discussions-fana.
   - `CONTRIBUTING.md` linje 235 og «Få hjelp»-lista (linje 267-272) —
     fjern atterhaldet «(dersom aktivert)» og legg til eit punkt i
     «Få hjelp» for Discussions.
3. **GOVERNANCE.md RFC-prosessen** (linje 269-277) vert **ikkje** endra —
   RFC-prosessen brukar eksplisitt GitHub Issue med merkelapp `RFC` for
   sporbarheit og 14-dagars varslingsfrist, og det er utanfor scope for
   denne oppgåva å endre den prosessen.

## Velkomsttekst (nynorsk)

Teksten under er ferdig utforma for å limast inn når brukaren set opp
velkomstinnlegget for «General»-kategorien i Discussions-UI-et.

```markdown
<!--
    ✏️ Valfritt: Tilpass innhaldet under for å fortelje fellesskapet kva du ønskjer å bruke Discussions til.
-->
## 👋 Velkommen!

Vi brukar Discussions som ein stad for å samle norske offentlege verksemder og andre
som jobbar med informasjonsmodellering rundt dette repoet. Her håpar vi de vil:

* Stille spørsmål om LinkML-skjema, AP-NO-profilar eller korleis de kjem i gang med
  ein ny domenemodell.
* Dele idear til nye modellar, forbetringar eller gjenbruk på tvers av verksemder.
* Fortelje om korleis de brukar (eller vurderer å bruke) skjema herifrå — anten som
  datatilbydar eller som grunnlag for eigne modellar.
* Bidra med innsikt frå eige fagfelt, slik at modellane held seg i tråd med praksis.
* Vere opne og inkluderande overfor andre. Dette er eit felles grunnlag vi
  forvaltar saman 💪.

**📚 Nyttige ressursar for nye brukarar og bidragsytarar:**

* [README](https://github.com/brreg/linkml-datamodellering-no#readme) — oversikt over repoet, skjemabiblioteket og korleis komme i gang lokalt.
* [SCOPE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/SCOPE.md) — kva repoet er (og ikkje er), og kva som høyrer heime her.
* [CONTRIBUTING.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CONTRIBUTING.md) — korleis bidra: PR-prosess, kodegjennomgang og kva du kan forvente av support i PoC-fasen.
* [Ny domenemodell](https://brreg.github.io/linkml-datamodellering-no/kom-i-gang/ny-domenemodell/) — steg-for-steg-rettleiing for å leggje til ein ny LinkML-modell.
* [Dokumentasjonsportalen](https://brreg.github.io/linkml-datamodellering-no/) — full oversikt over alle domene, skjema og genererte artefakter.

Kom gjerne i gang med å presentere deg sjølv og verksemda di, og fortel litt om
kva de jobbar med eller ønskjer å få ut av samarbeidet.

<!--
  Til forvaltarane, nokre tips 💡 for å komme i gang med Discussions. Kommentarane vert liggande i Markdown for no, men de kan fjerne dei når de er klare for at alle skal sjå dei.

  📢 **Fortel fellesskapet** at Discussions er tilgjengeleg — lenk til det frå README eller relevante kanalar (Slack, e-postlister, samarbeidsfora for norske offentlege verksemder).

  🔗 Vurder å **lenkje relevante issue-malar** (t.d. spørsmål om ein spesifikk domenemodell eller AP-NO-profil) til Discussions, slik at issues held fram med å vere feilrapportar og endringsforslag, medan generelle spørsmål og idear hamnar her.

  ➡️ De kan **konvertere issues til discussions**, enkeltvis eller i bulk via label. Sjå særleg etter issues merkte «spørsmål» eller «diskusjon».
-->
```

## Steg

1. Legg til ei ny linje i `README.md` § «Avgrensingar», etter
   «Rapporter nye problem»-linja, som peikar til Discussions for
   spørsmål og idear (skilt frå bug-rapportering).
2. Oppdater `CONTRIBUTING.md` linje 218: legg til lenkje til
   `https://github.com/brreg/linkml-datamodellering-no/discussions`.
3. Oppdater `CONTRIBUTING.md` linje 235: fjern «(dersom aktivert)»,
   legg til lenkje.
4. Legg til eit punkt i «Få hjelp»-lista i `CONTRIBUTING.md`
   (linje 267-272) som peikar til Discussions for generelle spørsmål,
   skilt frå punktet om å opne ein issue.
5. Brukaren aktiverer Discussions manuelt i GitHub-UI (Settings →
   Features → Discussions) og limer inn velkomstteksten frå denne
   specen i «General»-kategoriens velkomstinnlegg. **Denne handlinga kan
   ikkje utførast av LLM** — det er ei GitHub-repo-innstilling, ikkje ei
   endring i versjonskontrollert kode.

## Handlingsliste

- [x] `README.md` § Avgrensingar oppdatert med Discussions-lenkje
- [x] `CONTRIBUTING.md` linje 218 oppdatert med lenkje
- [x] `CONTRIBUTING.md` linje 235 oppdatert (fjern atterhald, legg til lenkje)
- [x] `CONTRIBUTING.md` «Få hjelp»-liste oppdatert med Discussions-punkt
- [ ] Brukaren aktiverer Discussions i GitHub-UI og limer inn
      velkomstteksten — **manuelt steg, utanfor LLM sitt handlingsrom**

## Utført

Dokumentasjonslenkjene er lagde til (sjå handlingslista over). Velkomstteksten
er utvida med ein «📚 Nyttige ressursar»-bolk som peikar nye brukarar/bidragsytarar
til README, SCOPE.md, CONTRIBUTING.md, «Ny domenemodell»-rettleiinga og
dokumentasjonsportalen. Det siste punktet — aktivering av Discussions i
GitHub-UI og innliming av velkomstteksten — er ei GitHub-repo-innstilling
brukaren må gjere sjølv, og vert difor ståande ukrysse av i denne specen.
