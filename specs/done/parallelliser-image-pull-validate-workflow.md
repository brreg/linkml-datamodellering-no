# Parallelliser og samordne image-henting i generate/validate-workflowane

## Bakgrunn

`validate.yml` sin `validate`-jobb (`validate / ${{ matrix.domain }}`) har to
separate, sekvensielle steg for å hente containerbilete frå GHCR før
validering kan starte:

- «Hent mcp-linkml-validator frå GHCR» (linje 197–202)
- «Hent linkml-local frå GHCR» (linje 204–209)

Kvart steg gjer `podman pull` + `podman tag` etter kvarandre, sjølv om dei to
imaga er heilt uavhengige av kvarandre og trygt kan hentast samtidig.

`generate.yml` sin `generate`-jobb løyser det same problemet — pulle fleire
uavhengige images frå GHCR før domenearbeid kan starte — i eitt steg,
«Last images inn i podman frå GHCR» (linje 208–245). Der vert kvart image
pulla i eit bakgrunnsjobb (`&`), med ein `pull_image()`-funksjon som:

1. Prøver `podman pull` av GHCR-taggen
2. Ved suksess: `podman tag`-ar biletet til den lokale taggen (`localhost/$img:latest`)
3. Ved feil: fell tilbake til lokalt bygg via `make $make_target`

Etterpå ventar steget på alle bakgrunnsjobbane (`wait`) før det går vidare.

Brukar bad om at tiltaket gjer generate- og validate-workflowane **mest
mogleg like** på dette punktet, og at eg evaluerer om ein gjenbrukbar
GitHub Action er mogleg — sjå evalueringa under.

## Evaluering: gjenbrukbar action

**Konklusjon: ja, det er mogleg og reint teknisk uproblematisk.** Repoet har
alt konvensjonen for dette — tre eksisterande composite actions i
`.github/actions/` (`discover-domains`, `ensure-image`, `upgrade-crun`),
alle med `runs: using: composite` og eksplisitte `inputs:`/`outputs:`.
`ensure-image` løyser eit ganske likt problem (bygg-eller-hent éitt image)
og er alt brukt av begge workflowane sin `ensure-images`/`build-image`-jobb.
Ein ny action `.github/actions/pull-images` for å **parallelt pulle ei liste
med images** (i staden for éitt image per matrix-jobb) er eit naturleg
tillegg til same mønster.

Praktisk er det uproblematisk fordi:

- Begge domene-jobbane lastar ned eit `source`-artifact som alt inkluderer
  heile `.github/`-katalogen før dei køyrer sine steg (sjå
  `actions/download-artifact@v8` + `uses: ./.github/actions/upgrade-crun`
  tidlegare i same jobb) — ein lokal `uses: ./.github/actions/pull-images`
  fungerer difor utan endring i artifact-oppsettet.
- Composite actions har tilgang til same `github`-kontekst som kallaren
  (t.d. `github.repository_owner`), så han treng ikkje sendast inn som
  eksplisitt input.

**Éin ting å vege opp mot:** CLAUDE.md sin DRY-regel seier eksplisitt at
terskelen for abstraksjon er **tre eller fleire identiske tilfelle** — "To
like tilfelle krev ingen abstraksjon." I dag finst mønsteret berre i desse
to workflowane, så ei streng lesing av regelen tilseier at duplisering
åleine ikkje er nok grunngjeving. Motivasjonen her er likevel ikkje berre
DRY isolert — det er eit eksplisitt ønske frå brukaren om **strukturell
konsistens** mellom generate og validate for eit ikkje-trivielt
(~35 linjer, med reell logikk: parallellisering + fallback-bygg) stykke
CI-oppførsel som elles lett driv frå kvarandre over tid (t.d. om nokon
rettar ein bug i eitt av dei to kopiane, men gløymer det andre). Det er den
grunngjevinga som veg tyngst her, ikkje talet på kopiar i seg sjølv.

**Vurdering: anbefalt**, gitt at brukaren (som her) eksplisitt har bede om
det — jf. CLAUDE.md sitt krav om at DRY-omskriving av eksisterande kode
krev løyve frå brukaren fyrst.

### Foreslått kontrakt

`.github/actions/pull-images/action.yml`:

```yaml
name: 'Last images inn i podman frå GHCR (parallelt)'
description: >-
  Pullar ei liste med images frå GHCR parallelt, taggar dei lokalt som
  localhost/<namn>:latest, og fell tilbake til lokalt bygg (make <target>)
  for kvart image som ikkje let seg pulle. Krev at podman alt er innlogga
  mot GHCR før dette steget køyrer.
inputs:
  images:
    description: 'JSON-array [{name, make_target}, ...]'
    required: true
  image_tags:
    description: 'JSON-map {namn: hash-tag} for GHCR-taggar'
    required: true
runs:
  using: 'composite'
  steps:
    - name: Pullar images frå GHCR (parallelt)
      shell: bash
      run: |
        pull_image() {
          local local_tag="$1" ghcr_tag="$2" make_target="$3"
          local start=$(date +%s%3N)
          echo "→ Prøver å pulle $ghcr_tag"
          if podman pull "$ghcr_tag" 2>&1; then
            podman tag "$ghcr_tag" "$local_tag"
            local elapsed=$(( $(date +%s%3N) - start ))
            printf "✓ Henta %s frå GHCR (%d.%ds)\n" "$local_tag" $((elapsed / 1000)) $((elapsed % 1000 / 100))
          else
            echo "⚠ GHCR-pull feila for $local_tag — byggjer lokalt"
            set -x
            make "$make_target"
            set +x
          fi
        }

        declare -a PIDS=()
        while IFS=$'\t' read -r img make_target; do
          tag=$(echo '${{ inputs.image_tags }}' | jq -r --arg n "$img" '.[$n]')
          pull_image "localhost/$img:latest" "ghcr.io/${{ github.repository_owner }}/$img:$tag" "$make_target" &
          PIDS+=($!)
        done < <(echo '${{ inputs.images }}' | jq -r '.[] | [.name, .make_target] | @tsv')

        wait
        echo "=== Alle pull-jobbar fullførte ==="
        podman images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}\t{{.Created}}"
```

Begge workflowane kallar han **identisk** (same steg-namn, same action),
berre med ulik kjelde til `images`:

```yaml
# generate.yml, i generate-jobben:
- name: Last images inn i podman frå GHCR
  if: steps.cache-generated.outputs.cache-hit != 'true'
  uses: ./.github/actions/pull-images
  with:
    images: ${{ steps.detect-images.outputs.images }}
    image_tags: ${{ needs.checkout-source.outputs.image_tags }}

# validate.yml, i validate-jobben:
- name: Last images inn i podman frå GHCR
  if: steps.cache-validated.outputs.cache-hit != 'true'
  uses: ./.github/actions/pull-images
  with:
    images: ${{ needs.checkout-source.outputs.images }}
    image_tags: ${{ needs.checkout-source.outputs.image_tags }}
```

### Naudsynt justering: `images`-outputet i generate.yml sitt detect-steg

For at begge kallarane skal kunne gje `pull-images` same input-form
(`[{name, make_target}, ...]`) må generate.yml sitt «Detekter påkrevde
images»-steg (id: `detect-images`) endrast: i dag eksporterer det
`REQUIRED_IMAGES` som ei mellomromseparert liste med berre **namn**
(`images=${REQUIRED_IMAGES[*]}`), og make_target vert slått opp separat
inne i det gamle pull-steget. Steget må i staden byggje eit JSON-array med
namn + make_target før det eksporterer, t.d.:

```bash
images_json=$(jq -c --argjson names "$(printf '%s\n' "${REQUIRED_IMAGES[@]}" | jq -R . | jq -s .)" \
  '[.[] | select(.name as $n | $names | index($n))] | map({name, make_target})' \
  "$IMAGES_MANIFEST")
echo "images=$images_json" >> "$GITHUB_OUTPUT"
```

Dette er same filtreringsmønster (`select(.name as $n | ... | index($n))`)
som `validate.yml` sitt `checkout-source`-steg alt brukar — ingen ny
teknikk, berre same idiom brukt konsekvent begge stader.

### Merknad om taggkonvensjon: `mcp-linkml-validator`

I dag taggar validate.yml sitt eksisterande steg `mcp-linkml-validator` UTAN
`localhost/`-prefiks (`mcp-linkml-validator:latest`), medan generate.yml sin
generiske løkke taggar ALLE image (inkl. `mcp-linkml-validator`) MED
`localhost/`-prefiks (`localhost/mcp-linkml-validator:latest`). Dette
fungerer i generate.yml i dag fordi podman resolver eit ukvalifisert
biletnamn (`mcp-linkml-validator`, brukt som `MCP_IMAGE`-default i
`flatten-and-validate.bash` og `MCP_IMAGE`-verdien i `make/00-settings.mk`)
til det lokale `localhost/`-namnerommet når ingen anna registry matchar.

Konsekvens: den delte action-en (som taggar med `localhost/`-prefiks, jf.
generate.yml sin eksisterande, fungerande konvensjon) gjer
`mcp-linkml-validator`-tagginga i validate.yml *konsistent* med
generate.yml — men dette er ei åtferdsendring for korleis biletet vert
referert internt i validate-jobben, og må verifiserast eksplisitt (sjå
Steg 5 under).

## Steg

1. Opprett `.github/actions/pull-images/action.yml` med kontrakten skissert
   over.
2. Juster generate.yml sitt «Detekter påkrevde images»-steg til å
   eksportere `[{name, make_target}, ...]` i staden for ei rein namneliste.
3. Erstatt generate.yml sitt eksisterande «Last images inn i podman frå
   GHCR»-steg (linje 208–245) med eit `uses: ./.github/actions/pull-images`-
   kall.
4. Erstatt validate.yml sine to steg «Hent mcp-linkml-validator frå GHCR» og
   «Hent linkml-local frå GHCR» (linje 197–209) med eitt
   `uses: ./.github/actions/pull-images`-kall, same steg-namn som i
   generate.yml («Last images inn i podman frå GHCR»).
5. Køyr begge jobbane (t.d. via ein test-PR eller `workflow_dispatch`) og
   verifiser at:
   - Begge/alle images vert pulla parallelt i kvar jobb (sjekk
     tidsstempel/loggrekkjefølgje)
   - `mcp-linkml-validator`-biletet vert korrekt funne av
     `flatten-and-validate.bash` i validate-jobben etter tagg-endringa til
     `localhost/mcp-linkml-validator:latest`
   - Fallback til lokalt bygg (`make <target>`) fungerer dersom GHCR-pull
     feilar (kan simulerast lokalt, treng ikkje testast i CI)
6. Køyr `actionlint` mot begge workflow-filene etter endringa (obligatorisk
   per CLAUDE.md § «Actionlint etter CI-endring»):
   ```bash
   podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/generate.yml
   podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/validate.yml
   ```

## Utanfor scope

`reusable-validate.yml` (den offentlege reusable workflowen for **eksterne**
repo som konsumerer denne valideringstenesta) har eit liknande, men
sjølvstendig, sekvensielt pull-steg (linje 54–60). Han brukar ikkje
`images.json`/`checkout-source`-infrastrukturen i det heile (han køyrer
utanfor dette repoet sin eigen CI-kontekst, mot berre to faste image), så
han er ikkje ein naturleg kandidat for den same delte action-en og er
halden utanfor denne planen.

## Handlingsliste

- [x] Opprett `.github/actions/pull-images/action.yml`
- [x] Juster generate.yml sitt detect-images-steg til å eksportere
      `{name, make_target}`-par i staden for rein namneliste
- [x] Byt ut generate.yml sitt eksisterande pull-steg med
      `uses: ./.github/actions/pull-images`
- [x] Byt ut validate.yml sine to sekvensielle pull-steg med
      `uses: ./.github/actions/pull-images`
- [ ] Verifiser tagg-konvensjonen for `mcp-linkml-validator` (sjå merknad
      over) fungerer korrekt for nedstraums bruk i
      `flatten-and-validate.bash` og `run-validation.sh` — **krev ei reell
      CI-køyring**, sjå «Utført» under
- [x] Køyr actionlint mot både `generate.yml` og `validate.yml`
- [ ] Verifiser med reelle køyringar (PR/workflow_dispatch) at begge
      jobbane framleis passerer for alle domene — **ikkje utført enno**,
      krev at brukaren pushar/opnar PR sidan LLM ikkje skal utføre
      git-operasjonar

## Utført

- Oppretta `.github/actions/pull-images/action.yml` — parallell
  `podman pull` + `podman tag`, med fallback til `make <target>` per image
  dersom pull feilar. YAML-syntaks verifisert med `python3 -c "import yaml;
  yaml.safe_load(...)"` (actionlint lintar ikkje `action.yml`-filer, berre
  `.github/workflows/*.yml`).
- `generate.yml`: «Detekter påkrevde images»-steget eksporterer no
  `images` som JSON-array `[{name, make_target}, ...]` (filtrert frå
  `images.json` med same `select(.name as $n | ... | index($n))`-idiom som
  `validate.yml` alt brukar), i staden for ei mellomromseparert namneliste.
  «Last images inn i podman frå GHCR»-steget kallar no
  `uses: ./.github/actions/pull-images` med `images`/`image_tags` som
  input.
- `validate.yml`: dei to stega «Hent mcp-linkml-validator frå GHCR» og
  «Hent linkml-local frå GHCR» er erstatta med eitt steg, «Last images inn
  i podman frå GHCR», som kallar same `uses: ./.github/actions/pull-images`
  — identisk steg-namn og action i begge workflowane.
- `actionlint` køyrd mot begge endra workflow-filer: berre pre-eksisterande
  `[shellcheck]`-stilråd (ikkje i dei endra kodeblokkene), ingen
  `[expression]`/schemafeil.
- **Ikkje utført:** reell CI-verifisering (PR/workflow_dispatch) av at
  begge jobbane framleis passerer, og at `mcp-linkml-validator` sin nye
  `localhost/`-prefiks-tagg fungerer korrekt i `flatten-and-validate.bash`.
  Dette krev at brukaren sjølv pushar endringane og observerer ei reell
  køyring, sidan LLM ikkje skal utføre `git push`/trigge CI.
