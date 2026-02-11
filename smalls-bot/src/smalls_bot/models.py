from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class WorkflowJob:
    target: str
    authorization_file: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    status: JobStatus = JobStatus.PENDING
    events: list[dict[str, Any]] = field(default_factory=list)

    def log(self, stage: str, detail: str, data: dict[str, Any] | None = None) -> None:
        self.events.append(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "stage": stage,
                "detail": detail,
                "data": data or {},
            }
        )
