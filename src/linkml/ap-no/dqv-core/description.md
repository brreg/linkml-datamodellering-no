`dqv-core` inneheld DQV-kjerneklassane (`Kvalitetsdimensjon`, `Kvalitetsmaaling`, `Kvalitetsmerknad` m.fl.) utan referanse til `dcat-ap-no`.

Skjemaet vart delt ut frå [`dqv-ap-no`](../dqv-ap-no/index.md) for å unngå sirkulær import: `dcat-ap-no` importerer `dqv-core` for å gje tilgang til `Kvalitetsmerknad`/`Kvalitetsmaaling` på `Datasett`, medan `dqv-ap-no` importerer både `dcat-ap-no` og `dqv-core` og narrowar `har_maal.range` via `slot_usage`.

**Avvik frå spesifikasjonen:** Sjå `specs/done/avvik-dqv-ap-no.md` for dokumenterte avvik og grunngjevingar.
