# Undersøking: kan `/sandbox` brukast saman med WSL2 i dette miljøet?

## Bakgrunn og motivasjon

Brukaren testa `/sandbox` (Claude Code sin OS-nivå-sandkasse for Bash-verktøyet)
i denne WSL2-økta og fekk problem knytt til read-only mounts. Denne spesifikasjonen
dokumenterer funn frå (a) det konkrete miljøet, (b) offisiell Anthropic-dokumentasjon,
og (c) kjende GitHub-issue om WSL2-samspel, samt rangerte tilrådingar.

Dette gjeld Claude Code-verktøyet sjølv, ikkje LinkML-modellering — spesifikasjonen
ligg likevel i `specs/backlog/` per den etablerte arbeidsflyten i `CLAUDE.md`.

**Status:** `bubblewrap` og `socat` er no verifiserte installerte, og brukaren har aktivert
`/sandbox` i denne økta. Sjå «Empirisk verifisering» nedanfor for testresultat — kravet om
skriving avgrensa til repoet er stadfesta å fungere. Ingen filer i repoet er endra av
undersøkingsarbeidet sjølv (testartefaktar oppretta under verifiseringa vart sletta att).

## Verifiserte miljøfunn (denne WSL2-instansen)

| Fakta | Verdi |
|---|---|
| Distro | Ubuntu 24.04.3 LTS (Noble Numbat) |
| Kernel | 6.6.87.2-microsoft-standard-WSL2 |
| WSL-versjon | 2.6.3.0 |
| Claude Code-versjon | 2.1.224 |
| `bubblewrap` (bwrap) | **Ikkje installert** (tilgjengeleg i apt: 0.9.0-1ubuntu0.1) |
| `socat` | **Ikkje installert** (tilgjengeleg i apt: 1.8.0.0-4ubuntu0.1) |
| `sysctl kernel.apparmor_restrict_unprivileged_userns` | Nøkkelen finst ikkje i dette miljøet — den kjende Ubuntu 24.04-AppArmor-restriksjonen er difor **ikkje** eit hinder her |
| Prosjektrota (`/mnt/c/dev/git/...`) sitt filsystem | `v9fs` (9p / drvfs — Windows-disk montert inn i WSL2) |
| Heimeområdet (`~`) sitt filsystem | `ext4` (WSL2 sitt native filsystem, på `/dev/sdd`) |

**Viktig konsekvens:** både `bubblewrap` og `socat` manglar i dette miljøet akkurat no.
Per offisiell dokumentasjon viser `/sandbox`-panelet då *berre* ei "Dependencies"-fane —
sandkassa kan ikkje ha kome forbi avhengigheitssjekken til det punktet der eit
mount-problem i det heile kunne oppstå. Anten (a) vart pakkane installert og sidan
fjerna/ikkje-persistert mellom økter, eller (b) det brukaren opplevde var i eit anna
WSL2-miljø/ei anna økt enn denne.

## Korleis `/sandbox` fungerer (verifisert mot offisiell dokumentasjon)

Kjelde: <https://code.claude.com/docs/en/sandboxing.md>

- **Mekanisme:** `bubblewrap` (bwrap) på både Linux og WSL2 — same implementasjon,
  ikkje ein eigen WSL2-variant. macOS brukar Seatbelt i staden. WSL1 er ikkje støtta
  (manglar kjernefunksjonar bwrap krev).
- **Avhengigheiter:** `bubblewrap` + `socat` (nettverksrelé). `ripgrep` er bundla.
  Eit valfritt seccomp-filter (`npm install -g @anthropic-ai/sandbox-runtime`) blokkerer
  Unix-socket-tilgang i tillegg.
- **Standardåtferd:** skriving er avgrensa til arbeidskatalogen + øktas temp-katalog.
  Lesing er tillate på heile maskina *unntatt* eksplisitt sperra stiar — mellom anna
  `settings.json` på alle nivå, `.mcp.json`, og den administrerte innstillingskatalogen.
  Desse sperrene handhevast som filsystem-mount-restriksjonar av bwrap.
- **Konfigurasjon:** `settings.json`-nøkkelen `sandbox.filesystem.{allowWrite,denyWrite,
  denyRead,allowRead,disabled}` og `sandbox.network.*`. `sandbox.filesystem.disabled: true`
  (krev v2.1.216+, oppfylt her) slår av filsystem-isolering heilt medan nettverksisolering
  står ved lag.
- **WSL2-spesifikt i dokumentasjonen:** eit eige avsnitt nemner at WSL2 rutar oppstart
  av Windows-binærfiler (`cmd.exe`, alt under `/mnt/c/`) via ein Unix-socket til
  Windows-verten, styrt av `allowAllUnixSockets`/`excludedCommands`. Dokumentasjonen
  nemner **ikkje** eksplisitt generelle read-only-mount-problem mot 9p/drvfs-stiar
  (`/mnt/c/...`) utover dette — det er **ikkje** eit offisielt dokumentert avgrensing.

## Kjende, verifiserte GitHub-issue

| Issue | Status | Relevans |
|---|---|---|
| [anthropics/claude-code#80212](https://github.com/anthropics/claude-code/issues/80212) | **Open** (bug) | På WSL2, når miljøvariabelen `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` er sett, tvingar Claude Code sandkassa på uansett `sandbox.enabled`. bwrap prøver då å bind-mounte den *Windows-sida* administrerte innstillingsstien (`C:\Program Files\ClaudeCode\...` → `/mnt/c/Program Files/ClaudeCode`), som ikkje finst når Claude Code berre er installert i WSL. `mkdir` feilar med "Permission denied" sidan vanlege WSL-brukarar ikkje kan opprette mapper under `Program Files` via drvfs. Dokumenterte workarounds i saka: `unset CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`, eller opprett mappa manuelt frå ein Windows-adminshell. |
| [anthropics/claude-code#31708](https://github.com/anthropics/claude-code/issues/31708) | Lukka (`not_planned`) | Anna symptom: sandkassa aktiverer seg ikkje i det heile trass i at alle avhengigheiter er installerte og `sandbox.enabled: true` er sett — ikkje eit read-only-mount-problem, men nemnt for fullstendigheit sidan det òg er WSL2-spesifikt. |
| [containers/bubblewrap#413](https://github.com/containers/bubblewrap/issues/413) | Open | Generell bwrap-avgrensing (ikkje WSL2-spesifikk): bwrap kan ikkje mounte noko *inni* eit område som alt er gjort read-only i same bwrap-kall (`mkdir: Read-only file system`). Kan i prinsippet ramme samspelet mellom fleire `denyRead`/`denyWrite`/protected-path-reglar som overlappar. |
| [microsoft/WSL#3549](https://github.com/microsoft/WSL/issues/3549) | Lukka (`completed`, auto-lukka pga. inaktivitet) | Opphavleg om WSL1 (`lxfs`). Ein WSL-kjerneutviklar stadfestar i kommentarfeltet at scenarioet "vil oppføre seg korrekt på WSL2 `/usr`, som er ext4" — dvs. read-only-remount-konflikta som denne saka gjaldt, er **ikkje** eit kjent problem på WSL2 sitt native ext4-filsystem. Saka seier ingenting eksplisitt om drvfs/9p (`/mnt/c`). |

## Sannsynleg årsak — vurdering (ikkje offisielt stadfesta for denne konfigurasjonen)

Ingen av kjeldene ovanfor dokumenterer eksplisitt "read-only mount-feil ved prosjekt
plassert generelt under `/mnt/c`" som eit kjent, generelt problem. Basert på verifiserte
fakta er den mest sannsynlege forklaringa likevel ei kombinasjon av:

1. **9p/drvfs har svakare støtte for mount-operasjonar enn ext4.** `/mnt/c` er montert
   som `v9fs` med faste `uid`/`gid` og avgrensa NTFS-til-POSIX-tilordning. bwrap sine
   bind-mount- og remount-read-only-operasjonar (jf. #80212 og bubblewrap#413) er meir
   utsett for å feile mot slike filsystem enn mot native ext4 — dette er ein rimeleg
   generalisering av det #80212 viser for eitt spesifikt tilfelle (Windows-managed-
   settings-stien), men er **ikkje** stadfesta av Anthropic for alle stiar under `/mnt/c`.
2. **Dette repoet (og truleg brukaren sitt `.claude/settings.json`/`.mcp.json`) ligg
   sjølv på `/mnt/c`.** Sandkassa handhevar skriveforbod mot nett desse filene som ein
   fast del av standardpolicyen — dersom bwrap sitt bind-mount av akkurat desse filene
   støyter på drvfs-avgrensingar, ville det gje seg utslag nett som "read-only mount"-feil.
3. **Manglande avhengigheiter i denne konkrete økta** (bwrap/socat ikkje installert)
   tyder på at feilen brukaren såg truleg oppstod i eit miljø/på eit tidspunkt der
   avhengigheitene *var* til stades — elles ville `/sandbox` ha stoppa på
   "Dependencies"-fana før noko mount-forsøk vart gjort.

## Brukarkrav: skriving avgrensa til repoet, sperra elles

Brukaren ønskjer at Claude skal kunne skrive til `c:/dev/github/linkml-datamodellering-no`
(dette repoet), men skal vere **sperra for skriving utanfor denne katalogen**. Spørsmålet
er om `/sandbox` kan realisere nett dette.

**Svar: ja, dette er i praksis standardåtferda til `/sandbox`** slik ho er dokumentert
ovanfor under «Korleis `/sandbox` fungerer» — "skriving er avgrensa til arbeidskatalogen +
øktas temp-katalog". Dersom Claude Code sin arbeidskatalog er sett til repo-rota (som han
er i denne økta, jf. miljøseksjonen ovanfor), sperrar sandkassa automatisk skriving til alt
anna enn repoet og den økt-spesifikke temp-katalogen (`/tmp/claude-.../scratchpad`) —
ingen ekstra konfigurasjon er strengt naudsynt for grunnkravet.

**For eksplisitt å feste dette** (t.d. dersom arbeidskatalogen kan variere, eller ein vil
dokumentere avgrensinga eksplisitt i staden for å stole på implisitt "cwd"-åtferd), kan
`sandbox.filesystem.allowWrite`/`denyWrite` setjast i `settings.json`:

```json
{
  "sandbox": {
    "filesystem": {
      "allowWrite": ["/mnt/c/dev/github/linkml-datamodellering-no"]
    }
  }
}
```

**Ikkje verifisert enno — treng avklaring før dette kan stolast på som handheva grense:**

1. **Om `allowWrite` *legg til* eller *erstattar* standardlista** (arbeidskatalog + temp).
   Dersom han erstattar, må temp-katalogen (naudsynt for Claude Code sin eigen drift,
   t.d. scratchpad) leggjast til eksplisitt i same liste, elles kan verktøy som skriv
   dit feile.
2. **Avhengigheitene manglar framleis i denne økta** (`bubblewrap`, `socat` — jf.
   miljøtabellen ovanfor). Sperra handhevast *ikkje* før desse er installerte — fram til
   då er "sperra for skriving utanfor repoet" eit ønskt, ikkje eit verkeleg, tilstand.
   Tiltak 2 under gjeld difor som forkrav for dette brukarkravet, ikkje berre for det
   opphavlege feilsøkingsspørsmålet.
3. **Repoet ligg på `/mnt/c` (9p/drvfs)**, filsystemtypen der dei kjende bwrap-mount-
   issuea (#80212, bubblewrap#413) oppstår. Dette gjeld i utgangspunktet *skrivesperra*
   utanfor repoet (som er det ein *vil* skal feile/nektast), ikkje skrivetilgangen
   *innanfor* repoet — men bør stadfestast empirisk før ein stolar på grensa, sidan
   same underliggjande mount-mekanisme handterer begge.

**Tilråding:** installer `bubblewrap` + `socat` (tiltak 2 under), aktiver `/sandbox` med
standardkonfigurasjon (ingen `allowWrite`/`denyWrite` naudsynt sidan arbeidskatalogen
alt er repo-rota), og verifiser empirisk med eit lite testskript at (a) skriving til ei
fil inni repoet lukkast, og (b) skriving til ei fil utanfor repoet (t.d. `/mnt/c/dev/`
eller `~/`) vert nekta.

## Empirisk verifisering (bwrap/socat installerte, `/sandbox` aktivert)

Etter at brukaren stadfesta `bubblewrap` og `socat` installerte og aktiverte `/sandbox`
("✓ Sandbox enabled with auto-allow for bash commands"), vart kravet frå førre seksjon
testa direkte med Bash-verktøyet i denne økta.

| Test | Sti | Resultat |
|---|---|---|
| Skriv inni repoet | `.../linkml-datamodellering-no/sandbox-test-inside.txt` | ✅ Lukkast |
| Skriv i foreldrekatalogen | `/mnt/c/dev/sandbox-test-outside.txt` | ✅ Sperra — `Read-only file system` |
| Skriv i heimekatalogen | `~/sandbox-test-home.txt` | ✅ Sperra — `Read-only file system` |
| Skriv til øktas scratchpad (`/tmp/claude-.../scratchpad`) | — | ✅ Lukkast (naudsynt for normal drift) |

**Konklusjon: brukarkravet er oppfylt.** Med arbeidskatalogen sett til repo-rota sperrar
`/sandbox` skriving til alt anna enn repoet + øktas temp-katalog, heilt utan ekstra
`sandbox.filesystem.allowWrite`-konfigurasjon. Dette avkreftar òg uvissepunkt 3 frå førre
seksjon: sjølv om repoet ligg på `/mnt/c` (9p/drvfs), fungerer skrivesperra korrekt der.

**Uventa biverknad oppdaga under testinga (ikkje ein tryggleiksfeil, men verdt å merke seg):**
`git status` viser no fleire ekstra `??`-oppføringar i repo-rota og under `.claude/` —
`.bashrc`, `.bash_profile`, `.zshrc`, `.zprofile`, `.profile`, `.gitconfig`, `.gitmodules`,
`.idea`, `.vscode`, `.ripgreprc`, og under `.claude/`: `agents`, `commands`, `hooks`,
`skills`, `routines`, `workflows`, `output-styles`, `launch.json`, `loop.md`,
`scheduled_tasks.json`. Desse dukka **ikkje** opp i `git status` før `/sandbox` vart
aktivert i denne økta.

Undersøkt nærare: stiane viser seg som teikneiningar (`crw-rw-rw-`, eigar `nobody:nogroup`,
major/minor `1,3` — same signatur som `/dev/null`) via `ls -la`, men både lesing (`cat`) og
skriving gjev **`Permission denied`** — dette er altså **ikkje** ei stille datalekkasje eller
eit maskert `/dev/null`-sluk som svelgjer skriving stille (det vart konkret testa: `echo >>`
mot ein av desse stiane feila eksplisitt, ikkje stilt). `git add` på ein slik sti feilar òg
eksplisitt (`can only add regular files...`), så det er ikkje risiko for utilsikta commit.

Mest sannsynlege forklaring: `/sandbox` handhevar ei fast liste over verna stiar som dekkjer
både vanlege shell-/IDE-konfigurasjonsfiler *og* Claude Code sine eigne kontrollplan-filer
under `.claude/` (agentdefinisjonar, kommandoar, hooks, skills, rutinar, workflows,
plansette oppgåver) — truleg med vilje, for å hindre at ein sandkassa (potensielt
kompromittert) prosess kan lese eller skrive til desse og dermed rømme sandkassa via t.d.
ein manipulert hook. `settings.json`, `settings.local.json`, `scheduled_tasks.lock` og
`.mcp.json` var **framleis lesbare** i same test — dei er altså ikkje omfatta av same sperre.

**Praktisk konsekvens:** ingen risiko for datatap eller sperra funksjonalitet er stadfesta,
men brukaren bør vere merksam på at `git status` viser støy frå desse verna stiane medan
`/sandbox` er aktivt, og heller bruke eksplisitte filnamn enn brei `git add -A`/`git add .`
(alt anbefalt praksis i CLAUDE.md-arbeidsflyten for git).

## Tilrådde tiltak (rangert etter sannsynlegheit for å løyse problemet)

1. **Flytt prosjektet til WSL2 sitt native filsystem** (t.d. `~/dev/...` i staden for
   `/mnt/c/dev/...`). Fjernar 9p/drvfs heilt frå likninga for både prosjektfilene og
   `.claude/settings.json`/`.mcp.json` som sandkassa sperrar mot skriving. Høgast
   forventa treffsikkerheit, sidan WSL2-utviklarane sjølv stadfestar at read-only-
   mount-mekanismen fungerer korrekt på ext4. Ulempe: filene vert ikkje lenger direkte
   synlege frå Windows Utforskar (krev `\\wsl$\...` eller VS Code Remote-WSL for
   Windows-sida tilgang).
2. **Installer manglande avhengigheiter og prøv på nytt.** Uansett kva anna som gjerast,
   er `bubblewrap` og `socat` eit hardt krav — utan dei kjem ein aldri forbi
   "Dependencies"-fana. Dette åleine kan òg avklare om det opphavlege problemet i det
   heile reproduserer i denne økta.
3. **Dersom feilen ligg i `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`:** test om variabelen er
   sett i miljøet, og prøv mellombels å fjerne han — dette er den einaste presist
   dokumenterte, opne WSL2-sandkasse-feilen (#80212) som direkte matchar eit
   mount/mkdir-symptom.
4. **Dersom prosjektet må bli verande på `/mnt/c`, og problemet held fram:**
   `sandbox.filesystem.disabled: true` (støtta frå v2.1.216, oppfylt av installert
   versjon 2.1.224) gjev opp filsystem-isolering heilt, men held nettverksisolering ved
   lag via `sandbox.network.allowedDomains`. Kan berre setjast frå brukar- eller
   administrerte innstillingar, ikkje frå prosjektet sin `.claude/settings.json`.
5. **Ikkje relevant her, men verdt å sjekke ved andre WSL2-oppsett:** AppArmor-
   restriksjonen på unprivileged user namespaces (Ubuntu 24.04+). I dette miljøet finst
   ikkje `kernel.apparmor_restrict_unprivileged_userns`-nøkkelen, så restriksjonen er
   ikkje aktiv — men sjekk `sysctl kernel.apparmor_restrict_unprivileged_userns` på nytt
   dersom bwrap feilar med namespace-relaterte feilmeldingar etter installasjon.

## Merknad om forholdet til `CLAUDE.md`

`CLAUDE.md` seier "Ingen avhengigheter skal installeres lokalt. Alt skal kjøres som
containere med podman i WSL2." Dette gjeld repoets eigne verktøykjede (LinkML,
Makefile-targets). `/sandbox` er ein eigenskap ved *Claude Code CLI-verktøyet sjølv*,
som køyrer som vertsprosess i WSL2 og ikkje kan sandkasse seg sjølv frå inni ein
podman-container — `bubblewrap`/`socat` er difor eit unntak frå regelen, ikkje eit brot
på henne, sidan dei ikkje er ein del av repoets bygg- eller valideringskjede.

## Attverande uvisse

- Ingen av kjeldene stadfestar eksplisitt at generelt `/mnt/c`-plasserte prosjekt
  (utan `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` sett) feilar med read-only-mount-feil i
  `/sandbox`. Punkt 1–2 i "Sannsynleg årsak" er ei grunngjeven, men ikkje offisielt
  stadfesta, hypotese.
- Utan den eksakte feilmeldinga brukaren fekk, kan ein ikkje avgjere om tiltak 1 eller
  3 direkte adresserer *det spesifikke* problemet — begge bør likevel provast, sidan
  dei er billige å teste og dekkjer dei to mest sannsynlege forklaringane.

## Utført

Brukaren installerte og stadfesta `bubblewrap` og `socat` (tiltak 2), aktiverte `/sandbox`,
og bad om empirisk verifisering av brukarkravet frå seksjonen ovanfor (repo skriveleg,
alt anna sperra).

- Testa skriving inni repoet, i foreldrekatalogen, i heimekatalogen og til øktas
  scratchpad — sjå tabell i «Empirisk verifisering». Alle fire testane gav forventa
  resultat: **brukarkravet er stadfesta oppfylt**, heilt utan ekstra
  `sandbox.filesystem.allowWrite`-konfigurasjon
- Dette avkrefta uvissepunkt 3 under «Brukarkrav»: skrivesperra fungerer korrekt sjølv
  om repoet ligg på `/mnt/c` (9p/drvfs)
- Oppdaga og undersøkte ein uventa, men ufarleg, biverknad: `/sandbox` vernar (nektar
  lesing/skriving av) shell-/IDE-konfigurasjonsfiler og Claude Code sine eigne
  kontrollplan-filer under `.claude/`, som gjev støy i `git status` medan sandkassa er
  aktiv. Stadfesta at dette er eksplisitt `Permission denied` (ikkje ei stille
  datalekkasje), og at `git add` på slike stiar feilar reint
- Testartefaktar oppretta under verifiseringa (`sandbox-test-inside.txt` m.fl.) vart
  sletta att — ingen varige endringar i repoet frå sjølve testinga

Attverande punkt frå «Sannsynleg årsak» og «Attverande uvisse» gjeld framleis som
generell bakgrunnskunnskap, men er ikkje lenger blokkerande — brukaren sitt konkrete
krav er verifisert løyst.
