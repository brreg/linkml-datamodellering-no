# Gource-video av git-historikken

[Gource](https://gource.io/) er eit visualiseringsverktøy som animerer git-historikken som ein
tre-struktur der filer og katalogar veks fram ettersom dei vert endra. Resultatet er ein video
som eignar seg for demoar, presentasjonar og dokumentasjon av prosjektutviklinga.

Ingen avhengigheiter skal installerast lokalt — alt køyrer som containerar med podman.

---

## Containeroppsett

Gource er ein grafisk applikasjon og treng ein virtuell framebuffer (Xvfb) for å køyre
hovudlaust. Utputt vert røyrlagt (pipe) til FFmpeg som kodar til MP4 (H.264, `yuv420p`,
`+faststart`) — den kombinasjonen spelar overalt: nettlesar, mobil, Windows Media Player,
QuickTime og VLC.

**`src/assets/containers/Dockerfile.gource`:**
```dockerfile
FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gource ffmpeg xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /repo
```

Bygg imaget (éin gong):
```bash
podman build -f src/assets/containers/Dockerfile.gource -t localhost/gource-local:latest
```

---

## Generere video

```bash
podman run --rm \
  -v "$(pwd):/repo:ro" \
  -v "$(pwd)/tmp:/out" \
  localhost/gource-local \
  bash -c "
    xvfb-run -a gource /repo \
      --viewport 1920x1080 \
      --output-framerate 60 \
      --seconds-per-day 1 \
      --auto-skip-seconds 1 \
      --title 'linkml-datamodellering-no' \
      --hide mouse,progress \
      --bloom-multiplier 0.5 \
      --background-colour 111111 \
      --font-size 18 \
      --output-ppm-stream - \
    | ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - \
        -an -vcodec libx264 -preset fast -crf 22 -pix_fmt yuv420p \
        -movflags +faststart \
        /out/gource.mp4
  "
```

Videoen hamnar i `tmp/gource.mp4`. `tmp/` er allereie i `.gitignore`.

---

## Hastigheit vs. kvalitet

Gource er CPU-bunde og single-threaded. Dei tre største lekkane:

| Faktor | Sakte (standard) | Rask (preview) | Effekt |
|---|---|---|---|
| Oppløysing | `1920x1080` | `1280x720` | ~2,5× færre pikslar per bilete |
| Bildefrekvens | `60` fps | `30` fps | 2× færre bilete totalt |
| FFmpeg-preset | `fast` | `ultrafast` | 3–5× raskare koding, noko større fil |
| Bloom | `0.5` | `0` | Fjerner ekstra renderingspass |

Kombinert gir preview-innstillingane om lag **8–10× raskare** rendering enn standardinnstillingane, på kostnad av oppløysing og mjukheit.

---

## Makefile-mål

```makefile
GOURCE_IMAGE      := localhost/gource-local:latest
GOURCE_DOCKERFILE := src/assets/containers/Dockerfile.gource

define GOURCE_RUN
podman run --rm \
  -v "$(CURDIR):/repo:ro" \
  -v "$(CURDIR)/tmp:/out" \
  $(GOURCE_IMAGE) \
  bash -c " \
    xvfb-run -a gource /repo \
      --seconds-per-day 1 \
      --auto-skip-seconds 1 \
      --title 'linkml-datamodellering-no' \
      --hide mouse,progress \
      --background-colour 111111 \
      --font-size 18 \
      --output-ppm-stream - \
      $(GOURCE_EXTRA_FLAGS) \
    | ffmpeg -y -r $(GOURCE_FPS) -f image2pipe -vcodec ppm -i - \
        -an -vcodec libx264 $(GOURCE_FFMPEG_PRESET) -pix_fmt yuv420p \
        -movflags +faststart \
        /out/$(GOURCE_OUTFILE)"
endef

gource-build:
	podman build -f $(GOURCE_DOCKERFILE) -t $(GOURCE_IMAGE)

# Rask preview: 720p, 30fps, ingen bloom, ultrafast encoding
gource-preview: gource-build
	@mkdir -p tmp
	$(MAKE) _gource-render \
	  GOURCE_OUTFILE=gource-preview.mp4 \
	  GOURCE_EXTRA_FLAGS="--viewport 1280x720 --bloom-multiplier 0" \
	  GOURCE_FPS=30 \
	  GOURCE_FFMPEG_PRESET="-preset ultrafast -crf 28"
	@echo "Preview: tmp/gource-preview.mp4"

# Endeleg video: 1080p, 60fps, bloom, høg kvalitet
gource-video: gource-build
	@mkdir -p tmp
	$(MAKE) _gource-render \
	  GOURCE_OUTFILE=gource.mp4 \
	  GOURCE_EXTRA_FLAGS="--viewport 1920x1080 --bloom-multiplier 0.5" \
	  GOURCE_FPS=60 \
	  GOURCE_FFMPEG_PRESET="-preset fast -crf 22"
	@echo "Video: tmp/gource.mp4"

_gource-render:
	$(GOURCE_RUN)
```

---

## Viktige parametrar

| Parameter | Standardverdi | Forklaring |
|---|---|---|
| `--seconds-per-day` | `1` | Kor fort kvart dag passerer. Lågare = raskare video. |
| `--auto-skip-seconds` | `1` | Hoppar over periodar utan aktivitet lenger enn dette. |
| `--viewport` | `1920x1080` | Oppløysing på output-videoen. |
| `--output-framerate` | `60` | Bilete per sekund — 60 gir mjuk animasjon. |
| `--hide` | `mouse,progress` | Skjuler musepeikaren og framdriftsindikator. |
| `--bloom-multiplier` | `0.5` | Lyseffekt rundt aktive noder. `0` = av, `2` = kraftig. |
| `--background-colour` | `111111` | Bakgrunnsfarge (hex utan `#`). |
| `--crf` (ffmpeg) | `22` | Kvalitet: 0 = tapsfri, 51 = lågast. 18–28 er praktisk område. |
| `-an` (ffmpeg) | — | Ingen lydspor. Gource produserer ikkje lyd; eksplisitt flagg unngår åtvaringar frå spelarar. |
| `-movflags +faststart` (ffmpeg) | — | Flyttar MP4-metadata til starten av fila. Nødvendig for avspilling i nettlesar før heile fila er lasta ned. |
| `--start-date` | — | Start frå ein gitt dato, t.d. `"2025-01-01"`. |
| `--stop-date` | — | Stopp ved ein gitt dato. |

---

## Tilpassing

### Avatarbilde for bidragsytarar

Legg `.jpg`-bilete i `tmp/avatars/<namn>.jpg` der `<namn>` svarar til git-brukarnamnet:

```bash
mkdir -p tmp/avatars
cp mitt-bilete.jpg tmp/avatars/"Audun Vindenes Egge.jpg"
```

Legg til `--user-image-dir /avatars` og monter katalogen:
```bash
-v "$(pwd)/tmp/avatars:/avatars:ro"
```

### Filtre på katalogar

For å vise berre `src/linkml/`-endringar:
```bash
--file-filter '^src/linkml/.*'
```

### Kortare video med tilpassa hastigheit

Repoet har commits frå april 2026 til dato (~4 veker). Med `--seconds-per-day 0.3` vert
videoen om lag 10 sekund. For ein lengre og meir detaljert video:
```bash
--seconds-per-day 2
```
gir om lag 60 sekund.

---

## Valgfritt: GitHub Actions-workflow

For automatisk generering ved release:

```yaml
# .github/workflows/gource.yml
name: Gource-video
on:
  workflow_dispatch:
  release:
    types: [published]

jobs:
  gource:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0        # heile historikken, ikkje berre siste commit

      - name: Installer Gource og FFmpeg
        run: sudo apt-get update && sudo apt-get install -y gource ffmpeg xvfb

      - name: Generer video
        run: |
          mkdir -p tmp
          xvfb-run -a gource \
            --viewport 1280x720 \
            --output-framerate 30 \
            --seconds-per-day 1 \
            --auto-skip-seconds 1 \
            --title 'linkml-datamodellering-no' \
            --hide mouse,progress \
            --bloom-multiplier 0 \
            --output-ppm-stream - \
          | ffmpeg -y -r 30 -f image2pipe -vcodec ppm -i - \
              -an -vcodec libx264 -preset ultrafast -crf 28 -pix_fmt yuv420p \
              -movflags +faststart \
              tmp/gource.mp4

      - name: Last opp som release-artefakt
        uses: softprops/action-gh-release@v2
        with:
          files: tmp/gource.mp4
```

> **Merk:** GitHub Actions-runnerar har `gource` og `ffmpeg` tilgjengeleg utan container.
> `fetch-depth: 0` er kritisk — utan det får Gource berre siste commit.
