# Undersøking: kan `/sandbox` brukast saman med WSL2 i dette miljøet?

## Bakgrunn og motivasjon

Brukaren testa `/sandbox` (Claude Code sin OS-nivå-sandkasse for Bash-verktøyet)
i denne WSL2-økta og fekk problem knytt til read-only mounts. Denne spesifikasjonen
dokumenterer funn frå (a) det konkrete miljøet, (b) offisiell Anthropic-dokumentasjon,
og (c) kjende GitHub-issue om WSL2-samspel, samt rangerte tilrådingar.

Dette gjeld Claude Code-verktøyet sjølv, ikkje LinkML-modellering — spesifikasjonen
ligg likevel i `specs/backlog/` per den etablerte arbeidsflyten i `CLAUDE.md`.

**Status:** reint undersøkings-/tilrådingsarbeid. Ingen filer i repoet er endra.
Alle konkrete tiltak under krev at brukaren sjølv vel og utfører dei (miljøkonfigurasjon,
ikkje repo-innhald).

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
