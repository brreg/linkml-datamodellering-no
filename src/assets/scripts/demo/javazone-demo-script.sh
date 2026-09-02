#!/usr/bin/env bash
# Steg-for-steg demo-script for JavaZone-presentasjonen — sjå
# specs/backlog/javazone-demo-plan.md for full kontekst og grunngjeving.
#
# Køyr FRÅ REPO-ROTA: bash src/assets/scripts/demo/javazone-demo-script.sh [DOMAIN=<domene>] [NAME=<navn>] [QUICK=<true|false>]
#   Same ARG=verdi-stil som resten av repoet sine make-kommandoar.
#   DOMAIN — default: oreg
#   NAME   — default: javazonetalk
#   QUICK  — default: true. Ved "true" hoppar scriptet over steg 1-4 (make
#            help, check-prereqs, new-modell og live-redigeringa) heilt —
#            ingen prompt, ingen diffvising for desse stega — og genererer
#            i staden $SCHEMA direkte i nøyaktig den tilstanden fila skal
#            vere i etter steg 4. Presentasjonen (med Enter-pausar) startar
#            då på steg 5. Sett QUICK=false for den fulle, uavkorta demoen.
#            Sjå specs/backlog/javazone-demo-quick-flag.md.
# Kvart steg viser tittel + kommando, ventar på Enter, køyrer så kommandoen.
# Steg 4 og 6 har ingen enkelt kommando — dei set i staden inn kjende,
# ferdigskrivne YAML-blokkar direkte i $SCHEMA (ingen manuell copy-paste)
# og viser resultatet som ein "git diff --no-index", éin pause per del,
# same "Enter"-mønster som resten av steg-funksjonane. Sjå
# specs/backlog/javazone-demo-auto-innsetjing.md for grunngjeving og
# teknisk tilnærming.
#
# Kommandolinjene er farga som i src/assets/scripts/makefile/help.sh:
# CLR_STEP (cyan) for "make <target>", CLR_OK (grøn) for obligatoriske
# argument, CLR_WARN (gul) for valfrie argument — same konvensjon som
# "Konvensjon:"-linja i `make help`.
#
# Ikkje "set -e" — eit feila steg skal ikkje krasje heile demoen midt i
# ein presentasjon; feilen vert vist, og du vel sjølv om du held fram.
set -uo pipefail

DOMAIN="oreg"
NAME="javazonetalk"
QUICK="true"
for arg in "$@"; do
    case "$arg" in
        DOMAIN=*) DOMAIN="${arg#DOMAIN=}" ;;
        NAME=*) NAME="${arg#NAME=}" ;;
        QUICK=*)
            QUICK="${arg#QUICK=}"
            case "$QUICK" in
                true|false) ;;
                *)
                    echo "Feil: QUICK må vere 'true' eller 'false' (fekk '$QUICK')." >&2
                    exit 1
                    ;;
            esac
            ;;
        *)
            echo "Feil: ukjent argument '$arg'." >&2
            echo "Bruk: bash $0 [DOMAIN=<domene>] [NAME=<navn>] [QUICK=<true|false>]" >&2
            exit 1
            ;;
    esac
done
SCHEMA="src/linkml/$DOMAIN/$NAME/$NAME-schema.yaml"

# TRAILING_MARKER — den siste kommentarlinja `new-modell.sh` alltid
# skriv til eit ferskt skjema (sjå
# src/assets/scripts/scaffolding/new-modell.sh), rett etter slots-
# seksjonen. Fungerer som eit stabilt, garantert unikt ankerpunkt for
# steg 4 sine slots-/enums-innsetjingar (sjå insert_before_line under) —
# uavhengig av DOMAIN/NAME, sidan teksten er identisk for alle nye
# modellar.
TRAILING_MARKER="# TODO: Gi stub-klassen eit meir meiningsfullt navn."

CLR_STEP=$'\033[0;36m'
CLR_OK=$'\033[0;32m'
CLR_WARN=$'\033[0;33m'
CLR_DBG=$'\033[2m'
CLR_ERR=$'\033[0;31m'
CLR_RST=$'\033[0m'

if [ ! -f Makefile ]; then
    echo "Feil: køyr dette scriptet frå repo-rota (der Makefile ligg)." >&2
    exit 1
fi

# Repeterte øvingskøyringar med same DOMAIN/NAME feilar elles i steg 3
# (new-modell) med "katalogen finst allereie") dersom du ikkje svarte
# "j" på oppryddingsspørsmålet sist gong.
if [ -d "src/linkml/$DOMAIN/$NAME" ]; then
    echo "${CLR_WARN}src/linkml/$DOMAIN/$NAME finst frå ei tidlegare køyring.${CLR_RST}"
    read -rp "Fjerne eksisterande modell før demoen startar? (j/N) " svar
    if [[ "$svar" =~ ^[jJ]$ ]]; then
        rm -rf "src/linkml/$DOMAIN/$NAME" "generated/$DOMAIN/$NAME"
        echo "Rydda opp."
    fi
fi

# Terminalpynt (figlet/toilet/cowsay/lolcat/boxes) — containerisert, ikkje
# installert lokalt. Byggjer biletet lat, berre viss det manglar (same
# mønster som resten av repoet sine make-target). Krev nettverk fyrste
# gong (sjå offline-sjekklista i specs/backlog/javazone-demo-plan.md).
FUN_IMAGE="localhost/demo-fun-tools"
FUN_DOCKERFILE="$(dirname "$0")/Dockerfile.fun-tools"
if ! podman image exists "$FUN_IMAGE" 2>/dev/null; then
    echo "${CLR_DBG}Byggjer ${FUN_IMAGE} (figlet/toilet/cowsay/lolcat/boxes) — berre fyrste gong …${CLR_RST}"
    podman build --format docker -f "$FUN_DOCKERFILE" -t "$FUN_IMAGE" "$(dirname "$FUN_DOCKERFILE")" \
        || echo "${CLR_WARN}Klarte ikkje byggje ${FUN_IMAGE} — held fram utan terminalpynt.${CLR_RST}"
fi
fun() { podman run --rm -i "$FUN_IMAGE" "$@" 2>/dev/null; }

# fun_width GOLV — breidd til figlet/glow -w. Aldri smalare enn GOLV,
# sjølv om terminalen er smalare (elles bryt figlet-bannerteksten og
# analyse-tabellane stygt midt i linja). Breiare dersom terminalen
# faktisk er breiare enn GOLV (t.d. på storskjerm under demoen).
fun_width() {
    local floor="$1" cols
    cols="$(tput cols 2>/dev/null || echo "$floor")"
    if [ "$cols" -lt "$floor" ]; then
        echo "$floor"
    else
        echo "$cols"
    fi
}

# run_help — pipar make help gjennom less -R (-R for å tolke fargekodane
# til help.sh i staden for å vise dei som rå escape-sekvensar, i motsetnad
# til "more"). -F: hopp over pageringa heilt viss output alt er kort nok
# til å få plass på éin skjerm. -X: ikkje tøm skjermen ved avslutning, så
# du framleis ser output etter at less lukkar. Elles ventar less på 'q'
# ved "(END)" — det er ikkje eit heng, berre less sin normale
# avslutningsmekanisme, difor hintet under.
# Eigen funksjon av same grunn som run_analyse_*: step() sin
# eksekveringsmodell er direkte argv, ikkje shell-pipe.
run_help() {
    echo "${CLR_DBG}(trykk 'q' for å lukke less og halde fram i scriptet)${CLR_RST}"
    make help | less -R -F -X
}

# run_validate — same less-pipe-mønster som run_help, for mcp-linkml-
# valider-modell sitt (potensielt lange) valideringsresultat.
run_validate() {
    echo "${CLR_DBG}(trykk 'q' for å lukke less og halde fram i scriptet)${CLR_RST}"
    make mcp-linkml-valider-modell SCHEMA="$SCHEMA" | less -R -F -X
}

# run_view_schema — same less-mønster som run_help/run_validate, brukt av
# QUICK=true-greina til å vise det stille-genererte $SCHEMA rett før
# steg 5, sidan QUICK=true (i motsetnad til QUICK=false) ikkje har vist
# innhaldet undervegs via diff.
run_view_schema() {
    echo "${CLR_DBG}(trykk 'q' for å lukke less og halde fram i scriptet)${CLR_RST}"
    less -R -F -X "$SCHEMA"
}

# insert_before_line SCHEMA ANKERLINJE INNHALD
# Set inn INNHALD (kan vere fleire linjer) rett før den fyrste linja i
# SCHEMA som er eksakt lik ANKERLINJE. Reint tekstbasert (ingen
# YAML-parsing) — trygt her sidan både innhaldet og målplasseringa er
# statisk kjend på førehand (scriptet sitt eige, ferdigskrivne innhald,
# ikkje brukargenerert). Sjå
# specs/backlog/javazone-demo-auto-innsetjing.md.
insert_before_line() {
    local schema="$1" anchor="$2" content="$3" line
    line=$(grep -n -F -x -m1 "$anchor" "$schema" | cut -d: -f1)
    if [ -z "$line" ]; then
        echo "${CLR_ERR}Fann ikkje ankerlinja '${anchor}' i ${schema}${CLR_RST}" >&2
        return 1
    fi
    awk -v line="$line" -v content="$content" '
        NR == line { print content }
        { print }
    ' "$schema" > "${schema}.tmp" && mv "${schema}.tmp" "$schema"
}

# block_end_line SCHEMA STARTLINJE
# Finn siste linjenummer i blokka som startar på STARTLINJE: skann
# framover til neste linje på same 2-mellomrom-innrykk (neste
# klasse-/slot-nøkkel, t.d. "  Sesjon:") eller neste 0-innrykk
# toppnivåfelt (t.d. "slots:"), og returner linja rett før. Går til
# filslutt dersom ingen av delane finst (siste blokk i fila).
block_end_line() {
    local schema="$1" start="$2"
    awk -v start="$start" '
        NR > start && (/^[A-Za-z]/ || /^  [A-Za-z0-9_]+:/) { print NR - 1; found = 1; exit }
        END { if (!found) print NR }
    ' "$schema"
}

# replace_block SCHEMA NOKKELLINJE NYTT-INNHALD
# Byter ut heile blokka som startar på NOKKELLINJE (t.d. "  Foredrag:")
# med NYTT-INNHALD. Brukt av steg 6 for å erstatte blokkar scriptet
# sjølv sette inn i steg 4 — trygg reinstreng-basert erstatting sidan
# innhaldet er deterministisk (skrive av scriptet, ikkje av brukaren),
# ikkje generell YAML-parsing.
replace_block() {
    local schema="$1" key_line="$2" content="$3" start end
    start=$(grep -n -F -x -m1 "$key_line" "$schema" | cut -d: -f1)
    if [ -z "$start" ]; then
        echo "${CLR_ERR}Fann ikkje blokka '${key_line}' i ${schema}${CLR_RST}" >&2
        return 1
    fi
    end=$(block_end_line "$schema" "$start")
    awk -v start="$start" -v end="$end" -v content="$content" '
        NR == start { print content; next }
        NR > start && NR <= end { next }
        { print }
    ' "$schema" > "${schema}.tmp" && mv "${schema}.tmp" "$schema"
}

# show_diff FØR ETTER — same less-pipe-mønster som run_help/run_validate.
show_diff() {
    local before="$1" after="$2"
    echo "${CLR_DBG}(trykk 'q' for å lukke less og halde fram i scriptet)${CLR_RST}"
    # ASCII-prefiks ("for"/"etter", ikkje "før") — git sin core.quotepath
    # escapar ikkje-ASCII-teikn i filsti-labelen (t.d. "ø" -> "f\303\270r/…"),
    # som gjer diff-headeren uleseleg.
    git diff --no-index --color=always --src-prefix=for/ --dst-prefix=etter/ \
        -- "$before" "$after" | less -R -F -X
}

# do_insert ANKERLINJE INNHALD
# Ventar på Enter, set så INNHALD inn i $SCHEMA rett før ANKERLINJE
# (insert_before_line), og viser resultatet som diff (show_diff). Brukt
# av steg 4 — éin pause per del, som før, men utan manuell copy-paste.
do_insert() {
    local anchor="$1" content="$2" before
    prompt_enter
    before="$(mktemp)"
    cp "$SCHEMA" "$before"
    if insert_before_line "$SCHEMA" "$anchor" "$content"; then
        show_diff "$before" "$SCHEMA"
    else
        echo "${CLR_ERR}(innsetjing feila — sjå output over, avgjer sjølv om du held fram)${CLR_RST}"
    fi
    rm -f "$before"
}

# extract_block SCHEMA STARTLINJE
# Skriv ut blokka som startar på STARTLINJE (til og med block_end_line
# sitt sluttpunkt) til stdout. Brukt av do_replace for å isolere kvar
# blokk sitt før-/etter-innhald til eiga diff (sjå grunngjeving der).
extract_block() {
    local schema="$1" start="$2" end
    end=$(block_end_line "$schema" "$start")
    sed -n "${start},${end}p" "$schema"
}

# do_replace NOKKELLINJE1 INNHALD1 [NOKKELLINJE2 INNHALD2 ...]
# Same mønster som do_insert, men byter ut éin eller fleire kjende
# blokkar (replace_block). Kvar blokk vert diffa isolert — berre
# blokka sitt eige før-/etter-innhald, ikkje heile fila — og alle
# blokkdiffane vert samla og viste i éin `less`-visning (éin pause,
# som før). Isolasjonen er naudsynt fordi git sitt kontekstvindauge
# (3 linjer, standard) elles anten ikkje når fram til nøkkellinja
# (om endringa ligg langt nede i ei kort blokk) eller lek inn i
# naboblokka (om nøkkellinja ligg nær toppen) — begge deler kan ikkje
# unngåast samstundes med éin diff over heile fila, sidan ulike
# blokker treng ulikt "før"/"etter"-kontekstbehov. Sjå
# specs/done/javazone-demo-har-foredrag-diff.md.
do_replace() {
    local before ok=1 combined=""
    prompt_enter
    before="$(mktemp)"
    cp "$SCHEMA" "$before"
    while [ "$#" -ge 2 ]; do
        local key="$1" content="$2"
        local old_start old_tmp new_start new_tmp block_diff
        old_start=$(grep -n -F -x -m1 "$key" "$before" | cut -d: -f1)
        if [ -z "$old_start" ]; then
            echo "${CLR_ERR}Fann ikkje blokka '${key}' i ${before}${CLR_RST}" >&2
            ok=0
            shift 2
            continue
        fi
        old_tmp="$(mktemp)"
        extract_block "$before" "$old_start" > "$old_tmp"

        if ! replace_block "$SCHEMA" "$key" "$content"; then
            ok=0
            rm -f "$old_tmp"
            shift 2
            continue
        fi

        new_start=$(grep -n -F -x -m1 "$key" "$SCHEMA" | cut -d: -f1)
        new_tmp="$(mktemp)"
        extract_block "$SCHEMA" "$new_start" > "$new_tmp"

        # sed henta ut alt frå fyrste "@@" — dropper "diff --git"/"index"/
        # "---"/"+++"-headera, som elles ville vist meiningslause
        # mktemp-filnamn (old_tmp/new_tmp er ikkje ekte stiar i skjemaet).
        block_diff=$(git diff --no-index --color=always -- "$old_tmp" "$new_tmp" | sed -n '/@@/,$p')
        combined+="${CLR_DBG}${key}${CLR_RST}"$'\n'"${block_diff}"$'\n\n'

        rm -f "$old_tmp" "$new_tmp"
        shift 2
    done
    rm -f "$before"
    if [ "$ok" -eq 1 ]; then
        echo "${CLR_DBG}(trykk 'q' for å lukke less og halde fram i scriptet)${CLR_RST}"
        printf '%s' "$combined" | less -R -F -X
    else
        echo "${CLR_ERR}(erstatting feila — sjå output over, avgjer sjølv om du held fram)${CLR_RST}"
    fi
}

# Pipar analyse-*-targeta sin markdown-tabell gjennom glow for pen
# rendering — eigne funksjonar sidan step() sin eksekveringsmodell er
# direkte argv (ikkje shell-pipe). Fell tilbake til rå make-output dersom
# demo-fun-tools-biletet ikkje finst, slik at analyseresultatet aldri går
# tapt berre fordi pynt-biletet manglar.
run_analyse_similar_classes() {
    if podman image exists "$FUN_IMAGE" 2>/dev/null; then
        make analyse-similar-classes-domain DOMAIN="$DOMAIN" NAME="$NAME" | fun glow -w "$(fun_width 140)" -
    else
        make analyse-similar-classes-domain DOMAIN="$DOMAIN" NAME="$NAME"
    fi
}
run_analyse_similar_slots() {
    if podman image exists "$FUN_IMAGE" 2>/dev/null; then
        make analyse-similar-slots-domain DOMAIN="$DOMAIN" NAME="$NAME" | fun glow -w "$(fun_width 140)" -
    else
        make analyse-similar-slots-domain DOMAIN="$DOMAIN" NAME="$NAME"
    fi
}
run_analyse_unused_slots() {
    if podman image exists "$FUN_IMAGE" 2>/dev/null; then
        make analyse-ubrukte-slots SCHEMA="$SCHEMA" | fun glow -w "$(fun_width 140)" -
    else
        make analyse-ubrukte-slots SCHEMA="$SCHEMA"
    fi
}
run_analyse_isolated_classes() {
    if podman image exists "$FUN_IMAGE" 2>/dev/null; then
        make analyse-isolerte-klasser SCHEMA="$SCHEMA" | fun glow -w "$(fun_width 140)" -
    else
        make analyse-isolerte-klasser SCHEMA="$SCHEMA"
    fi
}

# NB: figlet -w må ALDRI setjast breiare enn den faktiske terminalbreidda
# (i motsetnad til glow-tabellane). Figlet-bokstavar er fleire linjer
# høge — bryt den ekte terminalen ei figlet-linje midt i eit teikn (fordi
# -w var breiare enn terminalen), vert det avbrotne stykket vist som om
# det var neste rad, og bokstavane frå ulike rader flettar seg saman til
# uleseleg rot. Difor "small"-fonten her (smalare per teikn) + rein
# tput cols (aldri kunstig breiare), ikkje fun_width sitt golv.
if podman image exists "$FUN_IMAGE" 2>/dev/null; then
    fun figlet -w "$(tput cols 2>/dev/null || echo 100)" "LinkML-datamodellering-no Demo" | fun lolcat -f
fi

echo "${CLR_DBG}DOMAIN=${DOMAIN} NAME=${NAME}${CLR_RST}"
if [ "$DOMAIN" != "oreg" ] || [ "$NAME" != "javazonetalk" ]; then
    echo "${CLR_WARN}Merk: demoen er verifisert med DOMAIN=oreg NAME=javazonetalk."
    echo "Med andre verdiar — spesielt tipset i steg 4 om å bruke klassenavnet"
    echo "'Aktivitet' — er det ikkje sikkert du får eit like tydeleg treff i"
    echo "steg 6/7, sidan det tipset er tunt til at 'Aktivitet' alt finst i"
    echo "oreg-domenet. Vurder eit anna navn som alt finst i ditt valde domene"
    echo "(sjå 'make analyse-similar-classes-domain DOMAIN=${DOMAIN}' på"
    echo "førehand for å finne eit godt kandidatnavn).${CLR_RST}"
fi

# color_box_frame — fargar berre ramma i "boxes -d stone"-output, ikkje
# teksten inni. "stone"-designet (sjå /etc/boxes/boxes-config i
# demo-fun-tools-biletet) har eit fast, enkelt oppsett — topp-/botnlinje
# er reint "+---+", innhaldslinja er "| tittel |" med 1 mellomrom
# padding — så det held å fargeleggje heile topp-/botnlinja og berre
# fyrste/siste teikn (border-"|") på innhaldslinja, resten står att
# ufarga. Skulle formatet ein gong endre seg (ny boxes-versjon/design),
# fell dette trygt tilbake til å skrive linja ufarga via siste { print }.
color_box_frame() {
    awk -v c="$CLR_STEP" -v r="$CLR_RST" '
        /^\+-*\+$/ { print c $0 r; next }
        /^\|.*\|$/ {
            n = length($0)
            print c substr($0, 1, 1) r substr($0, 2, n - 2) c substr($0, n, 1) r
            next
        }
        { print }
    '
}

# print_heading VERKTOY TITTEL
# Køyrer overskrifta gjennom eit valt "fun"-verktøy (til utprøving/pynt).
# Fell tilbake til den vanlege farga overskrifta berre dersom
# demo-fun-tools-biletet manglar — elles vert overskrifta vist éin gong,
# ikkje dobbelt.
# toilet: ingen -f (fontnavn) — apt-pakken "toilet" åleine har berre den
# innebygde standardfonten, ekstra .tlf-fontar krev pakken "toilet-fonts"
# som ikkje er installert. Eit ugyldig fontnavn feilar ikkje synleg (toilet
# fell tilbake til degradert output), og feilen vert i tillegg svelgd av
# fun() sin 2>/dev/null.
print_heading() {
    local tool="$1" title="$2"
    echo ""
    if podman image exists "$FUN_IMAGE" 2>/dev/null; then
        case "$tool" in
            figlet) fun figlet "$title" ;;
            toilet) fun toilet "$title" ;;
            cowsay) echo "$title" | fun cowsay ;;
            boxes)  echo "$title" | fun boxes -d stone | color_box_frame ;;
            lolcat) echo "$title" | fun lolcat -f ;;
        esac
    else
        echo "${CLR_STEP}=== ${title} ===${CLR_RST}"
    fi
}

# Demo-klokka startar her (ikkje ved scriptstart) — biletbygginga over
# skjer normalt berre éin gong, utanfor sjølve presentasjonen, og skal
# difor ikkje telje med i dei 10 minutta.
DEMO_START=$(date +%s)

# elapsed — MM:SS sidan DEMO_START, vist i kvart "Trykk Enter"-prompt
# slik at du kan halde deg innanfor dei 10 minutta du har til demoen.
elapsed() {
    local diff=$(( $(date +%s) - DEMO_START ))
    printf '%02d:%02d' "$(( diff / 60 ))" "$(( diff % 60 ))"
}

# prompt_enter [MELDING] — same "Trykk Enter"-prompt som før, med
# elapsed-tid som prefiks.
prompt_enter() {
    read -rp "${CLR_DBG}[$(elapsed)]${CLR_RST} ${1:-Trykk Enter for å halde fram … }"
}

# step VERKTOY TITTEL FARGA-KOMMANDOLINJE [KOMMANDO ...]
# FARGA-KOMMANDOLINJE er ferdig-farga tekst til vising (kan vere tom
# streng), KOMMANDO er den faktiske argv-lista som vert køyrd.
step() {
    local tool="$1" title="$2" display="$3"
    shift 3
    print_heading "$tool" "$title"
    if [ -n "$display" ]; then
        echo ""
        echo "\$ ${display}"
    fi
    prompt_enter
    if [ "$#" -gt 0 ]; then
        "$@" || echo "${CLR_ERR}(steget feila — sjå output over, avgjer sjølv om du held fram)${CLR_RST}"
    fi
}
echo ""
echo ""
# Innhaldet scriptet set inn i $SCHEMA i steg 4 (klasser/slots/enums) —
# definert éin gong her slik at både den interaktive (QUICK=false) og
# den stille (QUICK=true) vegen til same sluttresultat brukar identisk
# innhald (DRY). Sjå specs/backlog/javazone-demo-quick-flag.md.
classes_content=$(cat <<EOF
  Foredragsholder:
    description: Ein person som melder inn/held eit foredrag.
    class_uri: ${NAME}:Foredragsholder
    slots:
    - id
    - navn
    - organisasjon

  Konferanse:
    description: Konferansen eit foredrag er meldt inn til.
    class_uri: ${NAME}:Konferanse
    slots:
    - id
    - tittel
    - sted
    - har_timeplaner

  Foredrag:
    description: Eit forslag til foredrag sendt inn til vurdering.
    class_uri: ${NAME}:Foredrag
    slots:
    - id
    - tittel
    - lengde_i_minutt
    - sammendrag
    - malgruppe
    - har_foredragsholdere
    - innsendingsstatus

  Sesjon:
    description: Ei tidsavgrensa økt der eit foredrag vert halde.
    class_uri: ${NAME}:Sesjon
    slots:
    - id
    - tid_start
    - tid_slutt
    - har_foredrag
    - har_sesjonslokale

  Timeplan:
    description: Ei tidsplanoppføring som viser alle foredrag pr dag.
    class_uri: ${NAME}:Timeplan
    slots:
    - id
    - dato
    - har_sesjoner

  Sesjonslokale:
    description: Eit rom eller sal der sesjonar vert haldne.
    class_uri: ${NAME}:Sesjonslokale
    slots:
    - id
    - navn
    - antall_plasser
EOF
)

slots_content=$(cat <<EOF
  navn:
    description: Navnet på foredragshaldaren.
    range: string

  organisasjon:
    description: Organisasjonen foredragshaldaren representerer.
    range: string

  sted:
    description: Staden konferansen vert halden.
    range: string

  lengde_i_minutt:
    description: Lengda på foredraget, i minutt.
    range: integer

  sammendrag:
    description: Eit samandrag av foredraget.
    range: string

  malgruppe:
    description: Målgruppa foredraget rettar seg mot.
    range: string

  har_foredragsholdere:
    description: Referanse til foredragshaldarane som har sendt inn foredraget.
    range: Foredragsholder
    multivalued: true

  foredrag_tidsrom:
    description: Tidsrommet foredraget vert halde i, t.d. "10:00-10:30".
    range: string

  lokasjon:
    description: Rommet eller salen foredraget vert halde i.
    range: string

  har_timeplaner:
    description: Referanse til timeplanoppføringane for konferansen.
    range: Timeplan
    multivalued: true

  innsendingsstatus:
    description: Status for foredragsinnsendinga.
    range: InnsendingStatus

  antall_plasser:
    description: Talet på sitjeplassar i sesjonslokalet.
    range: integer

  har_foredrag:
    description: Referanse til foredraget denne tidsplanoppføringa gjeld for.
    range: Foredrag
    multivalued: true

  tid_start:
    description: Tidspunktet sesjonen startar.
    range: datetime

  tid_slutt:
    description: Tidspunktet sesjonen sluttar.
    range: datetime

  har_sesjonslokale:
    description: Referanse til sesjonslokalet timeplanen gjeld for.
    range: Sesjonslokale

  har_sesjoner:
    description: Referanse til sesjonane i timeplanen.
    range: Sesjon
    multivalued: true

  dato:
    description: Dato for ei timeplan oppføring.
    range: datetime
EOF
)

enums_content=$(cat <<EOF
enums:
  InnsendingStatus:
    description: Status for ei foredragsinnsending.
    permissible_values:
      INNSENDT:
        description: Innsendt
      GODKJENT:
        description: Godkjent
      AVVIST:
        description: Avvist
EOF
)

if [ "$QUICK" = "false" ]; then
    step boxes "1. Sjå tilgjengelege kommandoar" \
        "${CLR_STEP}make help${CLR_RST} | less -R" \
        run_help
    echo ""
    echo ""
    step boxes "2. Sjekk at miljøet er klart" \
        "${CLR_STEP}bash src/assets/scripts/makefile/check-prereqs.bash${CLR_RST}" \
        bash src/assets/scripts/makefile/check-prereqs.bash
    echo ""
    step boxes "3. Opprett ein ny, tom modell" \
        "${CLR_STEP}make new-modell${CLR_RST} ${CLR_OK}DOMAIN=${DOMAIN}${CLR_RST} ${CLR_OK}NAME=${NAME}${CLR_RST} ${CLR_WARN}SKIP_EXAMPLE=1${CLR_RST}" \
        make new-modell DOMAIN="$DOMAIN" NAME="$NAME" SKIP_EXAMPLE=1
    # echo ""
    # echo ""
    # read -rp "Trykk Enter når du er ferdig … "
     echo ""
     echo ""
    print_heading boxes "4a. Rediger klasser"

    cat <<EOF

Set inn under '${CLR_DBG}classes:${CLR_RST}' i ${CLR_DBG}${SCHEMA}${CLR_RST} — seks klasser,
knytt saman, slik at ER-diagrammet i steg 11 viser reelle relasjonar
(scriptet set dei inn automatisk, diffen vert vist etterpå):

EOF

    do_insert "slots:" "$classes_content"
     echo ""
     echo ""
    print_heading boxes "4b. Rediger slots"
    echo ""
    cat <<EOF
Set inn under '${CLR_DBG}slots:${CLR_RST}' (${CLR_DBG}id${CLR_RST} og ${CLR_DBG}tittel${CLR_RST} finst alt via
common-ap-no-importen — dei atten andre er nye, sett inn automatisk,
diffen vert vist etterpå):

EOF

    do_insert "$TRAILING_MARKER" "$slots_content"
    echo ""
    echo ""
    print_heading boxes "4c. Rediger enumerations"
    echo ""
    cat <<EOF
Set inn heilt til slutt i skjemaet (nytt toppnivå-felt '${CLR_DBG}enums:${CLR_RST}',
same nivå som '${CLR_DBG}classes:${CLR_RST}' og '${CLR_DBG}slots:${CLR_RST}',
diffen vert vist etterpå):

EOF

    do_insert "$TRAILING_MARKER" "$enums_content"
else
    print_heading boxes "1-4. Generer skjema (QUICK)"
    echo ""
    echo "\$ ${CLR_STEP}make new-modell${CLR_RST} ${CLR_OK}DOMAIN=${DOMAIN}${CLR_RST} ${CLR_OK}NAME=${NAME}${CLR_RST} ${CLR_WARN}SKIP_EXAMPLE=1${CLR_RST}"
    echo "${CLR_DBG}QUICK=true — hoppar over steg 1-4 (make help / check-prereqs / new-modell / live-redigering).${CLR_RST}"
    echo "${CLR_DBG}Genererer ${SCHEMA} direkte, ferdig i tilstanden han skal vere i etter steg 4 …${CLR_RST}"
    if ! make new-modell DOMAIN="$DOMAIN" NAME="$NAME" SKIP_EXAMPLE=1; then
        echo "${CLR_ERR}(new-modell feila — sjå output over, held fram likevel; seinare steg vil truleg feile òg)${CLR_RST}"
    fi
    insert_before_line "$SCHEMA" "slots:" "$classes_content"
    insert_before_line "$SCHEMA" "$TRAILING_MARKER" "$slots_content"
    insert_before_line "$SCHEMA" "$TRAILING_MARKER" "$enums_content"
    prompt_enter "Trykk Enter for å sjå det genererte skjemaet … "
    run_view_schema
    #echo "${CLR_OK}Ferdig — held fram frå steg 5.${CLR_RST}"
fi
echo ""
echo ""
step boxes "5. Valider skjemaet" \
    "${CLR_STEP}make mcp-linkml-valider-modell${CLR_RST} ${CLR_OK}SCHEMA=${SCHEMA}${CLR_RST} | less -R" \
    run_validate
echo ""
echo ""

print_heading boxes "6. Adresser funn frå valideringa"
cat <<EOF

Steg 5 sin rapport har to slag funn:

1. ${CLR_DBG}Strukturelle DCAT-AP-NO/DQV-AP-NO-krav${CLR_RST} frå silver-policyen
   (containerklassen manglar attributt for Katalog/Datasett/Kvalitetsmaal/
   Kvalitetsmaaling) — uavhengige av kva som vart sett inn i steg 4, og utanfor
   denne demoen sitt scope (krev ein full DCAT-datasett-modell). Ikkje
   noko å fikse no — nemn dei berre som forventa.

2. ${CLR_DBG}To adresserbare bronse-funn${CLR_RST} frå klassane/slotsa i steg 4:
   - annotations.begrepsidentifikator manglar på alle seks nye klassane
   - slot_uri manglar på dei nye globale slotsa

Scriptet byter automatisk ut '${CLR_DBG}Foredrag:${CLR_RST}'
(begrepsidentifikator) og '${CLR_DBG}har_foredrag:${CLR_RST}'
(slot_uri) i éin omgang — viser mønsteret for begge funna, same retting
gjeld for dei fem andre klassane og resten av dei nye slotsa. Diffen
vert vist etterpå:

EOF
new_foredrag=$(cat <<EOF
  Foredrag:
    description: Eit forslag til foredrag sendt inn til vurdering.
    class_uri: ${NAME}:Foredrag
    annotations:
      begrepsidentifikator: https://concept-catalog.fellesdatakatalog.digdir.no/collections/964338531/concepts/e6bfeb15-5a47-4e68-83cd-03b0710f89d6
    slots:
    - id
    - tittel
    - lengde_i_minutt
    - sammendrag
    - malgruppe
    - har_foredragsholdere
    - innsendingsstatus
EOF
)
# block_end_line reknar den tomme linja rett før neste klassenøkkel
# ("  Sesjon:") som del av Foredrag-blokka. $() strip automatisk alle
# linjeskift på slutten av heredoc-fangsten over, så den tomme linja må
# leggjast attende eksplisitt — elles vil do_replace sin isolerte
# blokkdiff (sjå der) vise "annotations:"-tillegget og det tapte
# linjeskiftet som to separate hunkar i staden for éin, sidan dei ni
# uendra "slots:"-linjene mellom er breiare enn git sitt standard
# kontekstvindauge på 3 linjer.
new_foredrag+=$'\n'
# slot_uri plassert rett etter nøkkellinja (ikkje sist): sjølv med
# do_replace sin isolerte blokkdiff (som hindrar lekkasje til naboblokka)
# krevst det framleis at den faktiske endringa ligg innanfor git sitt
# standard "før"-kontekstvindauge (3 linjer) frå nøkkellinja, elles vert
# ikkje "har_foredrag:"-linja sjølv vist i diffen.
new_har_foredrag=$(cat <<EOF
  har_foredrag:
    slot_uri: ${NAME}:har_foredrag
    description: Referanse til foredraget denne tidsplanoppføringa gjeld for.
    range: Foredrag
    multivalued: true
EOF
)
new_har_foredrag+=$'\n'
do_replace "  Foredrag:" "$new_foredrag" "  har_foredrag:" "$new_har_foredrag"
echo ""
echo ""
step boxes "7. Valider skjemaet" \
    "${CLR_STEP}make mcp-linkml-valider-modell${CLR_RST} ${CLR_OK}SCHEMA=${SCHEMA}${CLR_RST} | less -R" \
    run_validate

echo ""
echo ""
step boxes "8. Finn isolerte klasser i modellen" \
    "${CLR_STEP}make analyse-isolerte-klasser${CLR_RST} ${CLR_WARN}SCHEMA=${SCHEMA}${CLR_RST}" \
    run_analyse_isolated_classes
echo ""
step boxes "9. Finn ubrukte slots i modellen" \
    "${CLR_STEP}analyse-ubrukte-slots${CLR_RST} ${CLR_WARN}SCHEMA=${SCHEMA}${CLR_RST}" \
    run_analyse_unused_slots
echo ""

# step boxes "10. Finn liknande klassenavn på tvers av domenet" \
#     "${CLR_STEP}make analyse-similar-classes-domain${CLR_RST} ${CLR_WARN}DOMAIN=${DOMAIN}${CLR_RST} ${CLR_WARN}NAME=${NAME}${CLR_RST}" \
#     run_analyse_similar_classes
# echo ""
# step boxes "11. Finn liknande slotnavn på tvers av domenet" \
#     "${CLR_STEP}make analyse-similar-slots-domain${CLR_RST} ${CLR_WARN}DOMAIN=${DOMAIN}${CLR_RST} ${CLR_WARN}NAME=${NAME}${CLR_RST}" \
#     run_analyse_similar_slots
# echo ""
step boxes "10. Generer JSON Schema frå den redigerte modellen" \
    "${CLR_STEP}make gen-jsonschema${CLR_RST} ${CLR_WARN}SCHEMA=${SCHEMA}${CLR_RST}" \
    make gen-jsonschema SCHEMA="$SCHEMA"
echo ""
echo ""
step boxes "11. Generer PlantUML-diagram" \
    "${CLR_STEP}make gen-plantuml${CLR_RST} ${CLR_WARN}SCHEMA=${SCHEMA}${CLR_RST}" \
    make gen-plantuml SCHEMA="$SCHEMA"
echo ""
echo ""
step boxes "12. Generer ModelDCAT-metadata" \
    "${CLR_STEP}make gen-informasjonsmodell-instance${CLR_RST} ${CLR_WARN}SCHEMA=${SCHEMA}${CLR_RST}" \
    make gen-informasjonsmodell-instance SCHEMA="$SCHEMA"
echo ""
echo ""
echo ""
#echo "${CLR_STEP}Demo ferdig.${CLR_RST}"
if podman image exists "$FUN_IMAGE" 2>/dev/null; then
    fun figlet -w "$(tput cols 2>/dev/null || echo 100)" "LinkML-datamodellering-no Demo" | fun lolcat -f
fi
echo ""
echo ""
if podman image exists "$FUN_IMAGE" 2>/dev/null; then
    printf 'https://brreg.github.io/linkml-datamodellering-no/' \
        | fun cowsay -n
fi
echo ""
echo ""
echo ""
echo ""
# read -rp "Vil du rydde demofilene? (j/N) " svar
#  if [[ "$svar" =~ ^[jJ]$ ]]; then
#     rm -rf "src/linkml/$DOMAIN/$NAME" "generated/$DOMAIN/$NAME"
#      echo "Rydda opp."
#  fi
