from __future__ import annotations

from dataclasses import dataclass


class LLMClient:
    def complete(self, prompt: str) -> str:
        raise NotImplementedError


@dataclass
class OllamaClient(LLMClient):
    model: str = "llama3.1"

    def complete(self, prompt: str) -> str:
        return f"[ollama:{self.model}] {prompt[:120]}"


@dataclass
class OpenAICompatibleClient(LLMClient):
    base_url: str
    model: str

    def complete(self, prompt: str) -> str:
        return f"[openai-compatible:{self.model}@{self.base_url}] {prompt[:120]}"
