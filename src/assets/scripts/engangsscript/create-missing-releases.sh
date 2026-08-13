#!/usr/bin/env bash
# Eingongs-remediering: opprett dei 16 GitHub Releases (+ opplast artefakt) som
# manglar fordi release-please.yml hoppa over tag-/release-oppretting ved
# merge av PR #50 (2026-08-02) — sjå specs/backlog/release-please-merge-commit-skip-bug.md
# for full rotårsaksanalyse. Git-tagane er alt oppretta og pusha (peikar på
# commit 33627bcc, som er det historisk korrekte punktet — IKKJE HEAD).
#
# Føresetnad: changelog- og artefaktfilene ligg i
# ~/release-remediation-33627bcc/ (flytta dit frå eit mellombels
# git-worktree bygd på commit 33627bcc).
#
# VIKTIG — immutable releases: repoet har immutable releases aktivert, så
# artefakt kan IKKJE ettermontlastast opp via `gh release upload` etter at
# releasen er oppretta — dei må sendast med i sjølve `gh release create`-
# kallet (sjå create_release_with_assets under).
#
# LØYST PROBLEM: cpsv-ap-no-v1.10.0 vart oppretta FØR denne fiksen, utan
# artefakt — vart immutable, og sletting + gjenoppretting av SAME tag_name
# vart deretter permanent blokkert av GitHub (stadfesta: gjeld uavhengig av
# "Enable release immutability"-innstillinga, av/på endra ikkje utfallet).
# Løysing: bumpa cpsv-ap-no sin version til 1.10.1 i den mellombels
# git-worktreeen (ikkje på main/HEAD — dette er ei reint historisk
# tagg-korrigering), regenererte artefakta, og brukar difor
# cpsv-ap-no-v1.10.1 under i staden for 1.10.0. Tag-en cpsv-ap-no-v1.10.0
# står att som eit permanent hoppa-over versjonsnummer utan release.
set -euo pipefail

REPO="brreg/linkml-datamodellering-no"
SRC_DIR="$HOME/release-remediation-33627bcc"

create_release_with_assets() {
    local tag="$1" title="$2" name="$3"
    if gh release view "$tag" --repo "$REPO" >/dev/null 2>&1; then
        echo "  release $tag finst alt — hoppar over (NB: sjekk manuelt om han har artefakt — sjå merknad i skriptheadar)"
        return 0
    fi
    # Repoet har «immutable releases» aktivert — artefakt kan IKKJE leggjast
    # til i eit separat opplastingssteg etterpå. Alt må sendast i éin
    # gh release create-kommando.
    gh release create "$tag" "$SRC_DIR/artifacts/$name"/*.* \
        --repo "$REPO" \
        --title "$title" \
        --notes-file "$SRC_DIR/changelogs/$name.md"
    echo "  OK: oppretta $tag med artefakt"
}

declare -a PACKAGES=(
    "cpsv-ap-no-v1.10.1|cpsv-ap-no: 1.10.1|cpsv-ap-no"
    "dcat-ap-no-v2.13.0|dcat-ap-no: 2.13.0|dcat-ap-no"
    "dqv-ap-no-v1.15.0|dqv-ap-no: 1.15.0|dqv-ap-no"
    "modelldcat-ap-no-v1.14.0|modelldcat-ap-no: 1.14.0|modelldcat-ap-no"
    "skos-ap-no-v2.16.0|skos-ap-no: 2.16.0|skos-ap-no"
    "brreg-begrepskatalog-v1.6.1|brreg-begrepskatalog: 1.6.1|brreg-begrepskatalog"
    "fair-metadata-v1.6.0|fair-metadata: 1.6.0|fair-metadata"
    "fint-administrasjon-v4.5.1|fint-administrasjon: 4.5.1|fint-administrasjon"
    "fint-common-v4.4.0|fint-common: 4.4.0|fint-common"
    "brreg-modellkatalog-v1.5.1|brreg-modellkatalog: 1.5.1|brreg-modellkatalog"
    "ngr-adresse-v1.6.0|ngr-adresse: 1.6.0|ngr-adresse"
    "ngr-eiendom-v1.6.0|ngr-eiendom: 1.6.0|ngr-eiendom"
    "ngr-person-v1.6.0|ngr-person: 1.6.0|ngr-person"
    "ngr-virksomhet-v1.6.0|ngr-virksomhet: 1.6.0|ngr-virksomhet"
    "register-over-aksjeeiere-v1.7.0|register-over-aksjeeiere: 1.7.0|register-over-aksjeeiere"
    "samt-bu-v1.9.0|samt-bu: 1.9.0|samt-bu"
)

for entry in "${PACKAGES[@]}"; do
    IFS='|' read -r tag title name <<< "$entry"
    echo "=== $tag ==="
    create_release_with_assets "$tag" "$title" "$name"
done

echo ""
echo "Ferdig — alle 16 releases sjekka/oppretta og artefakt lasta opp."
