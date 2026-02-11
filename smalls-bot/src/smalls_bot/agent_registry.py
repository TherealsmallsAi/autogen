from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class Agent(Protocol):
    name: str

    def run(self, context: dict) -> dict:
        ...


@dataclass
class AgentRegistry:
    _agents: dict[str, Agent]

    def __init__(self) -> None:
        self._agents = {}

    def register(self, agent: Agent) -> None:
        self._agents[agent.name] = agent

    def get(self, name: str) -> Agent:
        if name not in self._agents:
            raise KeyError(f"Agent '{name}' is not registered")
        return self._agents[name]

    def list_agents(self) -> list[str]:
        return sorted(self._agents.keys())
