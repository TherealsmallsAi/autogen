from __future__ import annotations

import argparse
import json
import sys

from .agent_registry import AgentRegistry
from .agents.default_agents import AuthorizationGuardAgent, ReconPlannerAgent, ReportAgent
from .models import WorkflowJob
from .workflow_engine import WorkflowEngine


def build_registry() -> AgentRegistry:
    registry = AgentRegistry()
    registry.register(AuthorizationGuardAgent())
    registry.register(ReconPlannerAgent())
    registry.register(ReportAgent())
    return registry


def cmd_list_agents() -> int:
    registry = build_registry()
    for name in registry.list_agents():
        print(name)
    return 0


def cmd_run(target: str, authorization_file: str) -> int:
    registry = build_registry()
    engine = WorkflowEngine(registry)
    job = WorkflowJob(target=target, authorization_file=authorization_file)
    result = engine.run(job)
    print(json.dumps({"job_id": result.id, "status": result.status.value, "events": result.events}, indent=2))
    return 0 if result.status.value == "completed" else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Smalls Bot safe MVP CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list-agents", help="List registered agents")

    run_parser = subparsers.add_parser("run", help="Run workflow")
    run_parser.add_argument("--target", required=True, help="Authorized target URL or hostname")
    run_parser.add_argument("--authorization-file", required=True, help="Path to written authorization artifact")

    args = parser.parse_args()
    if args.command == "list-agents":
        return cmd_list_agents()
    if args.command == "run":
        return cmd_run(args.target, args.authorization_file)

    print("Unknown command", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
