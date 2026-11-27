
from abc import ABC, abstractmethod
from typing import Iterator

class BaseProvider(ABC):

    def __init__(self, model, temperature=0.7,
                 max_tokens=1024):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    @abstractmethod
    def stream(self, messages: list) -> Iterator[str]:
        """Return generated text chunks."""
        pass

    @abstractmethod
    def chat(self, messages: list) -> str:
        """Return a complete response."""
        pass