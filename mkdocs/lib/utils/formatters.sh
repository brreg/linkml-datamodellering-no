#!/usr/bin/env bash
# Formateringsfunksjonar for domene- og artefaktlabels
set -euo pipefail

domain_label() {
    case "$1" in
        ap-no)   echo "AP-NO - Applikasjonsprofiler" ;;
        begrepskatalog) echo "Begrepskatalog - Begrepskatalogmodellar" ;;
        modellkatalog)   echo "Modellkatalog - Informasjonsmodellar" ;;
        ngr)     echo "NGR - Nasjonale Grunndata" ;;
        fint)    echo "FINT - Fylkeskommunale integrasjonar" ;;
        samt)    echo "SAMT - Kommunale integrasjonar" ;;
        fair)    echo "FAIR - Metadataoverbygning" ;;
        oreg)    echo "OREG - Offentlege registre" ;;
        *)     echo "$1" | awk '{print toupper($0)}' ;;
    esac
}

artifact_label() {
    case "$1" in
        shapes.ttl)     echo "SHACL shapes" ;;
        ontology.ttl)   echo "OWL ontologi" ;;
        schema.ttl)     echo "RDF/Turtle skjema" ;;
        context.jsonld) echo "JSON-LD kontekst" ;;
        schema.json)    echo "JSON Schema" ;;
        schema.xsd)     echo "XML Schema (XSD)" ;;
        openapi.yaml)   echo "OpenAPI 3.1" ;;
        asyncapi.yaml)  echo "AsyncAPI 3.0" ;;
        model.py)       echo "Python-klasser" ;;
        schema.proto)   echo "Protobuf-skjema" ;;
        erdiagram.md)   echo "ER-diagram (Mermaid)" ;;
        eksempel.ttl)   echo "Eksempeldata (Turtle)" ;;
        *)              echo "$1" ;;
    esac
}
