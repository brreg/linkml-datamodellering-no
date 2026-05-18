#!/usr/bin/env bash
IMAGE="docker.io/linkml/linkml:latest"

CONTAINER_NAME="linkml-interactive"

# finnes immage $IMAGE_LOADER lokalt i podman?
if podman image exists "$IMAGE"; then
    echo "Image $IMAGE finnes lokalt."
else
# puller "$IMAGE"
    podman pull "$IMAGE"
fi    



# kjører "$IMAGE" med interaktive shell
podman run  --rm --replace\
    --name "$CONTAINER_NAME" \
    -v $PWD:/work \
    -w /work \
    -ti \
    "$IMAGE"

# kjører validering
# podman run --rm --replace \
#   -v "$PWD:/work" \
#   docker.io/linkml/linkml:latest \
#   linkml-validate --schema model/data-toolbox-demo.yaml data/data.yaml


# kommandoer du kan benytte i interaktivt shell i immaget:
#gen-project --help

