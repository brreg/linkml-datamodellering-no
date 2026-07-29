# Forslag til meir unike og profesjonelle overskrifter

Utgangspunktet ditt er ryddig og konsistent, men alle nivåa er svært like. Det gjer hierarkiet mindre tydeleg. Her er nokre alternativ.

## Alternativ 1 – Venstrestilt aksentlinje (anbefalt)

Gir eit moderne og profesjonelt uttrykk utan mykje visuell støy.

- H1: bakgrunn + 6px venstrelinje
- H2: berre 4px venstrelinje
- H3: tynn 2px venstrelinje og inga bakgrunn

Fordel: tydeleg hierarki og mindre «boks-preg».

```css
.md-typeset h1 {
  background: var(--ds-color-main1-background-subtle);
  border-left: 9px solid var(--ds-color-main1-border-default);
  padding: 0.75rem 1rem;
}

.md-typeset h2 {
  border-left: 6px solid var(--ds-color-main1-border-default);
  padding-left: 0.75rem;
}

.md-typeset h3 {
  border-left: 3px solid var(--ds-color-main1-border-default);
  padding-left: 0.5rem;
}
```

## Alternativ 2 – Dokumentstil

Inspirert av profesjonelle rapportar.

- H1: full bredde med bakgrunn
- H2: understrek
- H3: fet tekst utan ekstra dekor

Fordel: svært rein og lettlesen.

## Alternativ 3 – Seksjonsmerking

Legg til ein liten visuell markør framfor overskrifta.

```css
.md-typeset h2::before {
  content: "";
  display: inline-block;
  width: 0.5rem;
  height: 0.5rem;
  background: var(--ds-color-main1-border-default);
  margin-right: 0.5rem;
  border-radius: 2px;
}
```

Fordel: gjer dokumentet meir karakteristisk utan å bli prangande.

## Alternativ 4 – Reduksjon av boksar

I staden for bakgrunn på alle nivå:

- H1: bakgrunn + topp/botn-ramme
- H2: berre botn-ramme
- H3: ingen ramme, berre typografi

Fordel: meir luft og mindre visuell tyngde.

## Mi anbefaling

For ein modellkatalog, arkitekturdokumentasjon eller offentleg dokumentasjonsportal ville eg valt alternativ 1 kombinert med:

- H1: bakgrunn + kraftig venstreaksent
- H2: venstreaksent utan bakgrunn
- H3: berre typografisk skilje
- Litt større avstand før H2 og H3

Det gir eit meir moderne uttrykk, reduserer mengda rammer og gjer dokumenthierarkiet enklare å skanne.
