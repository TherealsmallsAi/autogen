from pathlib import Path

from smalls_bot.cli import build_registry
from smalls_bot.models import JobStatus, WorkflowJob
from smalls_bot.workflow_engine import WorkflowEngine


def test_workflow_blocks_unauthorized_target(tmp_path: Path) -> None:
    auth_file = tmp_path / "authorization.txt"
    auth_file.write_text("authorized: https://safe.example", encoding="utf-8")

    engine = WorkflowEngine(build_registry())
    job = WorkflowJob(target="https://nope.example", authorization_file=str(auth_file))
    result = engine.run(job)

    assert result.status == JobStatus.FAILED


def test_workflow_completes_for_authorized_target(tmp_path: Path) -> None:
    auth_file = tmp_path / "authorization.txt"
    auth_file.write_text("authorized: https://safe.example", encoding="utf-8")

    engine = WorkflowEngine(build_registry())
    job = WorkflowJob(target="https://safe.example", authorization_file=str(auth_file))
    result = engine.run(job)

    assert result.status == JobStatus.COMPLETED
    assert any(event["stage"] == "report" for event in result.events)
