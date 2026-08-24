#!/usr/bin/env python3
"""
Batch-valider FLEIRE (skjema, instans)-par mot mcp-linkml-validator sitt
validate_linkml_instance-verktøy i éin kontainar-prosess, i staden for éin
kontainar per skjema. Same mekanisme som batch-flatten-and-validate.py
(éin JSON-RPC-melding per jobb sendt over éin delt stdin-straum til éin
podman-kontainar), men mot validate_linkml_instance i staden for
validate_linkml_schema — reint instansvalidering, ingen policy-sjekkar.

Skjema vert sendt som `schemaPath` (krev at validate_linkml_instance-
verktøyet støttar dette — lagt til i server.py saman med dette scriptet,
sjå specs/backlog/batch-validate-lint-test-per-skjema.md, Tiltak 3
Kategori C). Fjernar det tidlegare `gen-linkml --mergeimports`-
utflatingssteget test_mcp_validate_instance i tests/test_make.sh gjorde
per skjema, same grunngjeving som effektiviser-mcp-linkml-validator-
koyretid.md sitt Tiltak 2.

Bruk:
  python3 batch-validate-instances.py --output-dir DIR \\
      schema1.yaml=instance1.yaml schema2.yaml=instance2.yaml ...

  Stiane er repo-relative. --repo-root vert montert som /repo:ro i
  kontainaren, så SchemaView løyser relative importar naturleg mot
  filsystemet.

Output: éitt resultat-JSON-fil per jobb i --output-dir, navngjeve
<index>.json (0-indeksert, same rekkjefølgje som jobbane vart oppgjevne).
Innhaldet er identisk med det validate_linkml_instance-verktøyet returnerer.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def build_tool_call(msg_id: int, container_schema_path: str, instance_text: str) -> dict:
    return {
        "jsonrpc": "2.0", "id": msg_id, "method": "tools/call",
        "params": {
            "name": "validate_linkml_instance",
            "arguments": {"schemaPath": container_schema_path, "instanceText": instance_text},
        },
    }


def run_mcp_batch(repo_root: Path, validator_dir: Path, mcp_image: str, messages: list[dict]) -> dict[int, dict]:
    """Sender alle meldingane til éin mcp-linkml-validator-kontainar. Returnerer id -> parsed response."""
    stdin_payload = "\n".join(json.dumps(m) for m in messages) + "\n"
    proc = subprocess.run(
        ["podman", "run", "-i", "--rm",
         "-v", f"{repo_root}:/repo:ro",
         "-v", f"{validator_dir}/server.py:/app/server.py:ro",
         "-v", f"{validator_dir}/policies:/app/policies:ro",
         mcp_image],
        input=stdin_payload, capture_output=True, text=True,
    )
    responses: dict[int, dict] = {}
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            resp = json.loads(line)
        except json.JSONDecodeError:
            continue
        if resp.get("id") is not None:
            responses[resp["id"]] = resp
    if proc.returncode != 0 and not responses:
        log(f"ÅTVARING: mcp-linkml-validator-kontainaren feila (exit {proc.returncode}): {proc.stderr.strip()[:500]}")
    return responses


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("jobs", nargs="+", help="skjema=instans-par, repo-relative stiar")
    parser.add_argument("--output-dir", required=True, help="Katalog for resultat-JSON, éin fil per jobb")
    parser.add_argument("--repo-root", default=os.environ.get("REPO_ROOT", str(Path.cwd())))
    parser.add_argument("--validator-dir", default=os.environ.get(
        "VALIDATOR_DIR", str(Path(__file__).resolve().parent)))
    parser.add_argument("--mcp-image", default=os.environ.get("MCP_IMAGE", "mcp-linkml-validator"))
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    validator_dir = Path(args.validator_dir).resolve()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    jobs = [job.split("=", 1) for job in args.jobs]

    messages = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}]
    job_msg_id: dict[int, int] = {}

    for idx, (schema_rel, instance_rel) in enumerate(jobs):
        instance_text = (repo_root / instance_rel).read_text(encoding="utf-8")
        msg_id = idx + 2  # id 1 er 'initialize'
        job_msg_id[idx] = msg_id
        messages.append(build_tool_call(msg_id, f"/repo/{schema_rel}", instance_text))

    log(f"→ Validerer {len(jobs)} instans(ar) i éin mcp-linkml-validator-kontainar ...")
    responses = run_mcp_batch(repo_root, validator_dir, args.mcp_image, messages)

    job_results: dict[int, dict] = {}
    for idx, msg_id in job_msg_id.items():
        resp = responses.get(msg_id)
        if resp is None:
            job_results[idx] = {
                "valid": False, "errorCount": 1, "warningCount": 0,
                "issues": [{"severity": "error", "code": "no_mcp_response", "target": "instance",
                            "message": "Ingen svar frå mcp-linkml-validator-batchen (sjå container-logg)"}],
            }
        elif "error" in resp:
            job_results[idx] = {
                "valid": False, "errorCount": 1, "warningCount": 0,
                "issues": [{"severity": "error", "code": "mcp_error", "target": "instance",
                            "message": str(resp["error"])}],
            }
        else:
            job_results[idx] = json.loads(resp["result"]["content"][0]["text"])

    for idx in range(len(jobs)):
        (output_dir / f"{idx}.json").write_text(
            json.dumps(job_results[idx], ensure_ascii=False), encoding="utf-8")

    failed = sum(1 for r in job_results.values() if not r.get("valid", False))
    log(f"→ Ferdig: {len(jobs)} instans(ar), {failed} ugyldige, output i {output_dir}")


if __name__ == "__main__":
    main()
