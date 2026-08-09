#!/usr/bin/env python3
"""
Batch-variant av flatten-and-validate.bash: validerer FLEIRE skjema, men
sender berre éitt samla JSON-RPC-kall til mcp-linkml-validator (éin podman-
kontainar for heile batchen i staden for éin per skjema).

Bakgrunn: import av linkml/linkml_runtime tek ~5s og vert betalt på nytt for
kvar einaste podman-kontainar. Sidan mcp-linkml-validator sin server.py alt
les JSON-RPC-meldingar i ei løkke frå stdin, kan N valideringskall sendast
til éin kontainar-prosess og dele éin importkostnad i staden for N.

Skjema vert sendt som `schemaPath` (ikkje `schemaText`) — heile repoet vert
montert read-only inn i kontainaren, og SchemaView løyser relative importar
naturleg mot filsystemet. Dette fjernar òg det tidlegare separate
utflatingssteget (`gen-linkml --mergeimports` i eigen kontainar per skjema)
heilt. Sjå specs/backlog/effektiviser-mcp-linkml-validator-koyretid.md
(Tiltak 1 + Tiltak 2).

Bruk:
  # Alle skjema med same policy, instans auto-oppdaga (validate-bronze):
  python3 batch-flatten-and-validate.py --policy bronze --output-dir DIR \\
      schema1.yaml schema2.yaml ...

  # Heterogen liste med ulik policy/instans per skjema (validate-data):
  python3 batch-flatten-and-validate.py --jobs-file jobs.json --output-dir DIR

  jobs.json: [{"schema": "sti", "policy": "bronze", "instance": "sti-eller-null"}, ...]

Output: eitt resultat-JSON-fil per jobb i --output-dir, namngjeve <index>.json
(0-indeksert, same rekkjefølgje som jobbane vart oppgjevne). Innhaldet er
identisk med det éin enkelt `flatten-and-validate.bash`-kall ville printa —
kan sendast rett vidare til save-validation-log.py/
emit-github-validation-annotations.py utan endring.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def load_jobs(args) -> list[dict]:
    if args.jobs_file:
        jobs = json.loads(Path(args.jobs_file).read_text(encoding="utf-8"))
    elif args.jobs_tsv:
        # Enkelt tab-separert format (schema\tpolicy\tinstance) — unngår
        # JSON-quoting i Makefile-kall. Tom instance-kolonne = auto-oppdaga.
        jobs = []
        for line in Path(args.jobs_tsv).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            parts = line.split("\t")
            schema = parts[0]
            policy = parts[1] if len(parts) > 1 and parts[1] else "bronze"
            instance = parts[2] if len(parts) > 2 and parts[2] else None
            jobs.append({"schema": schema, "policy": policy, "instance": instance})
    else:
        if not args.schemas:
            sys.exit("Feil: oppgje anten --jobs-file, --jobs-tsv eller minst eitt skjema som positional argument")
        jobs = [{"schema": s, "policy": args.policy, "instance": None} for s in args.schemas]
    for job in jobs:
        job.setdefault("policy", "bronze")
        job.setdefault("instance", None)
    return jobs


def resolve_example_path(repo_root: Path, schema_rel: str, explicit_instance: str | None) -> Path:
    """Same konvensjon som flatten-and-validate.bash: NAME/DOMAIN frå skjemaets katalogstruktur."""
    schema_path = Path(schema_rel)
    name = schema_path.parent.name
    domain = schema_path.parent.parent.name
    example = repo_root / "src" / "linkml" / domain / name / "examples" / f"{name}-eksempel.yaml"
    if not example.is_file():
        example = repo_root / "examples" / domain / f"{name}-eksempel.yaml"
    if explicit_instance:
        example = repo_root / explicit_instance
    return example


_TREE_ROOT_RE = re.compile(r"^\s+tree_root:\s*true\s*$", re.MULTILINE)


def schema_has_tree_root(repo_root: Path, schema_rel: str) -> bool:
    """tree_root-klassen er alltid definert lokalt i skjemaet (aldri importert), jf.
    CLAUDE.md sin konvensjon — treng difor ikkje løyse importar for å sjekke dette.
    Regex i staden for full YAML-parsing sidan dette er den einaste bruken av PyYAML
    i scriptet — fjernar behovet for PyYAML på hosten (sjå
    specs/backlog/nye-host-python-kall-batching.md)."""
    text = (repo_root / schema_rel).read_text(encoding="utf-8")
    return _TREE_ROOT_RE.search(text) is not None


def build_tool_call(msg_id: int, container_schema_path: str, policy: str, instance_text: str | None) -> dict:
    arguments = {"schemaPath": container_schema_path, "policy": policy}
    if instance_text is not None:
        arguments["instanceText"] = instance_text
    return {
        "jsonrpc": "2.0", "id": msg_id, "method": "tools/call",
        "params": {"name": "validate_linkml_schema", "arguments": arguments},
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
    parser.add_argument("schemas", nargs="*", help="Skjemastiar (brukt saman med --policy)")
    parser.add_argument("--policy", default="bronze", help="Policy for alle skjema (default: bronze)")
    parser.add_argument("--jobs-file", help="JSON-fil med heterogen jobbliste (schema/policy/instance)")
    parser.add_argument("--jobs-tsv", help="Tab-separert jobbliste (schema<TAB>policy<TAB>instance), éi jobb per linje")
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

    jobs = load_jobs(args)

    messages = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}]
    job_msg_id: dict[int, int] = {}  # index -> JSON-RPC id sendt til MCP

    for idx, job in enumerate(jobs):
        schema_rel = job["schema"]
        policy = job["policy"]

        example_path = resolve_example_path(repo_root, schema_rel, job.get("instance"))
        instance_text = None
        if example_path.is_file() and schema_has_tree_root(repo_root, schema_rel):
            instance_text = example_path.read_text(encoding="utf-8")

        msg_id = idx + 2  # id 1 er 'initialize'
        job_msg_id[idx] = msg_id
        messages.append(build_tool_call(msg_id, f"/repo/{schema_rel}", policy, instance_text))

    log(f"→ Validerer {len(jobs)} skjema i éin mcp-linkml-validator-kontainar ...")
    responses = run_mcp_batch(repo_root, validator_dir, args.mcp_image, messages)

    job_results: dict[int, dict] = {}
    for idx, msg_id in job_msg_id.items():
        resp = responses.get(msg_id)
        if resp is None:
            job_results[idx] = {
                "valid": False, "errorCount": 1, "warningCount": 0,
                "issues": [{"severity": "error", "code": "no_mcp_response", "target": "schema",
                            "message": "Ingen svar frå mcp-linkml-validator-batchen (sjå container-logg)"}],
            }
        elif "error" in resp:
            job_results[idx] = {
                "valid": False, "errorCount": 1, "warningCount": 0,
                "issues": [{"severity": "error", "code": "mcp_error", "target": "schema",
                            "message": str(resp["error"])}],
            }
        else:
            job_results[idx] = json.loads(resp["result"]["content"][0]["text"])

    for idx in range(len(jobs)):
        (output_dir / f"{idx}.json").write_text(
            json.dumps(job_results[idx], ensure_ascii=False), encoding="utf-8")

    failed = sum(1 for r in job_results.values() if not r.get("valid", False))
    log(f"→ Ferdig: {len(jobs)} skjema, {failed} ugyldige, output i {output_dir}")


if __name__ == "__main__":
    main()
