# Smalls Bot Architecture (v1 MVP)

## Safety-first core

- **Authorization Gate (hard-stop):** every run requires written authorization evidence.
- **Human-in-the-loop checkpoints:** report generation and escalation are non-automated.
- **Non-offensive defaults:** passive recon planning only.

## Components

1. **CLI (`smalls-bot`)**
   - `run`: execute a workflow
   - `list-agents`: inspect registry
2. **Workflow engine**
   - stage orchestration and audit event log
3. **Agent registry**
   - plug-in agents by role
4. **Queue layer**
   - in-memory async queue in MVP
5. **LLM integration layer**
   - local open-source model runtime adapters

## Planned next phases

- Multi-agent job planner/executor separation
- Redis-backed queue for distributed workers
- Web dashboard streaming job events
- Optional PostgreSQL/pgvector memory backend
- Policy-as-code guardrails and scope verifier
