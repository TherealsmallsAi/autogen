from __future__ import annotations

import asyncio

from .models import WorkflowJob


class JobQueue:
    def __init__(self) -> None:
        self._queue: asyncio.Queue[WorkflowJob] = asyncio.Queue()

    async def enqueue(self, job: WorkflowJob) -> None:
        await self._queue.put(job)

    async def dequeue(self) -> WorkflowJob:
        return await self._queue.get()

    def size(self) -> int:
        return self._queue.qsize()
