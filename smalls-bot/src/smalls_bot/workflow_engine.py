from __future__ import annotations

from pathlib import Path

from .agent_registry import AgentRegistry
from .models import JobStatus, WorkflowJob


class WorkflowEngine:
    def __init__(self, registry: AgentRegistry) -> None:
        self.registry = registry

    def run(self, job: WorkflowJob) -> WorkflowJob:
        job.status = JobStatus.RUNNING
        job.log("start", "Workflow started")

        auth_text = Path(job.authorization_file).read_text(encoding="utf-8")
        context = {"target": job.target, "authorization_text": auth_text}

        guard = self.registry.get("authorization_guard")
        auth_result = guard.run(context)
        job.log("authorization", auth_result["reason"], auth_result)

        if not auth_result.get("authorized"):
            job.status = JobStatus.FAILED
            job.log("end", "Authorization check failed")
            return job

        recon = self.registry.get("recon_planner")
        recon_result = recon.run(context)
        job.log("recon", "Recon plan generated", recon_result)

        context["findings"] = [
            {
                "severity": "info",
                "title": "Workflow scaffold generated a passive recon plan",
                "requires_human_review": True,
            }
        ]
        report_agent = self.registry.get("report_writer")
        report = report_agent.run(context)
        job.log("report", "Draft report prepared", report)

        job.status = JobStatus.COMPLETED
        job.log("end", "Workflow completed")
        return job
