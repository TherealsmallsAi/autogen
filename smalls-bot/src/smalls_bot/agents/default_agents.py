from __future__ import annotations


class AuthorizationGuardAgent:
    name = "authorization_guard"

    def run(self, context: dict) -> dict:
        authorization_text = context.get("authorization_text", "")
        target = context.get("target", "")
        if target and target in authorization_text:
            return {"authorized": True, "reason": "Target appears in authorization file."}
        return {
            "authorized": False,
            "reason": "Target missing from authorization artifact. Workflow halted.",
        }


class ReconPlannerAgent:
    name = "recon_planner"

    def run(self, context: dict) -> dict:
        target = context["target"]
        return {
            "plan": [
                f"Collect passive DNS and certificate metadata for {target}",
                "Run approved, rate-limited discovery checks",
                "Map exposed services for human review",
            ]
        }


class ReportAgent:
    name = "report_writer"

    def run(self, context: dict) -> dict:
        findings = context.get("findings", [])
        return {
            "report": {
                "summary": "MVP scan completed with human-review checkpoints.",
                "finding_count": len(findings),
                "next_action": "Security engineer review required before any active testing.",
            }
        }
