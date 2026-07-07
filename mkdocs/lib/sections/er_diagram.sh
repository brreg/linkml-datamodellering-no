#!/usr/bin/env bash
# Generer ER-diagram-seksjon (seksjon 10 i index.md)
set -euo pipefail

generate_er_diagram() {
    local schema="$1"
    local out="$2"

    # Embed PlantUML-diagram (filtrert versjon — kun lokale klasser)
    local plantuml_svg="diagrams/${schema}-filtered.svg"
    local plantuml_full="diagrams/${schema}.svg"

    # Prioriter filtrert versjon
    if [ -f "$out/$plantuml_svg" ]; then
        # Sjekk om filtrert diagram er tomt (< 1000 bytes = ingen lokale klasser)
        local filesize
        filesize=$(stat -c%s "$out/$plantuml_svg" 2>/dev/null || stat -f%z "$out/$plantuml_svg" 2>/dev/null || echo "0")

        echo "---"
        echo ""
        echo "## ER-diagram"
        echo ""

        if [ "$filesize" -lt 1000 ]; then
            # Tomt diagram — vis berre full versjon med forklaring
            echo "[![ER-diagram]($plantuml_full)]($plantuml_full)"
            echo ""
            echo "*Modellen har ingen lokale klasser og ingen diagram med kun lokale klasser. [Vis fullstendig diagram med importerte klasser]($plantuml_full).*"
        else
            # Normalt filtrert diagram
            echo "[![ER-diagram]($plantuml_svg)]($plantuml_svg)"
            echo ""
            echo "*Diagrammet viser kun lokale klasser. Klikk for å zoome. [Vis fullstendig diagram med importerte klasser]($plantuml_full).*"
        fi
        echo ""
    elif [ -f "$out/$plantuml_full" ]; then
        echo "---"
        echo ""
        echo "## ER-diagram"
        echo ""
        echo "[![ER-diagram]($plantuml_full)]($plantuml_full)"
        echo ""
        echo "*Klikk for å zoome.*"
        echo ""
    fi
}
