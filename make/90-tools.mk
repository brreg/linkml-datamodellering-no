# ==============================================================================
# make/90-tools.mk
#
# Verktøy og utilitetar:
# - Gource: git-historikk-visualisering (preview, video, render)
# - check-prereqs: sjekk at alle nødvendige verktøy er installerte
#
# Relaterte script:
# - src/assets/scripts/makefile/check-prereqs.bash
# ==============================================================================

# ---------------------------------------------------------------------------
# Gource – visualisering av git-historikk
# ---------------------------------------------------------------------------

GOURCE_IMAGE      := localhost/gource-local:latest
GOURCE_DOCKERFILE := src/assets/containers/Dockerfile.gource

define GOURCE_RUN
podman run --rm \
  -v "$(CURDIR):/repo:ro" \
  -v "$(CURDIR)/tmp:/out" \
  $(GOURCE_IMAGE) \
  bash -c " \
    git config --global --add safe.directory /repo && \
    xvfb-run -a -s '-screen 0 1920x1080x24' \
      gource /repo \
        --seconds-per-day 1 \
        --auto-skip-seconds 1 \
        --title 'linkml-datamodellering-no' \
        --hide mouse,progress \
        --background-colour 111111 \
        --font-size 18 \
        --output-ppm-stream /out/gource.ppm \
        $(GOURCE_EXTRA_FLAGS) && \
    ffmpeg -y -r $(GOURCE_FPS) \
        -f image2pipe -vcodec ppm \
        -i /out/gource.ppm \
        -an -vcodec libx264 $(GOURCE_FFMPEG_PRESET) \
        -pix_fmt yuv420p -movflags +faststart \
        /out/$(GOURCE_OUTFILE) && \
    rm /out/gource.ppm"
endef

gource-preview: build-docker-gource ## Generer Gource preview-video (720p, rask encoding)
	$(call print_header,gource-preview)
	@mkdir -p tmp
	@$(MAKE) --no-print-directory _gource-render \
	  GOURCE_OUTFILE=gource-preview.mp4 \
	  GOURCE_EXTRA_FLAGS="--viewport 1280x720" \
	  GOURCE_FPS=30 \
	  GOURCE_FFMPEG_PRESET="-preset ultrafast -crf 28"
	@echo "Preview: tmp/gource-preview.mp4"

gource-video: build-docker-gource ## Generer Gource produksjonsvideo (1080p, høg kvalitet)
	$(call print_header,gource-video)
	@mkdir -p tmp
	@$(MAKE) --no-print-directory _gource-render \
	  GOURCE_OUTFILE=gource.mp4 \
	  GOURCE_EXTRA_FLAGS="--viewport 1920x1080 --bloom-multiplier 0.5" \
	  GOURCE_FPS=60 \
	  GOURCE_FFMPEG_PRESET="-preset fast -crf 22"
	@echo "Video: tmp/gource.mp4"

_gource-render:
	$(GOURCE_RUN)

# ---------------------------------------------------------------------------
# Verktøy-sjekk
# ---------------------------------------------------------------------------

check-prereqs: ## Sjekk at alle nødvendige verktøy er installerte
	$(call print_header,check-prereqs)
	@bash src/assets/scripts/makefile/check-prereqs.bash
