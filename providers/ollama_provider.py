#qwen2.5:1.5b
import ollama
from providers.base import BaseProvider

class OllamaProvider(BaseProvider):

    def __init__(self, model="llama3.2", **kwargs):
        super().__init__(model, **kwargs)
        self.client = ollama.Client(
            host="http://localhost:11434"
        )

    def stream(self, messages):
        response = self.client.chat(
            model=self.model,
            messages=messages,
            stream=True,
            options={
                "temperature": self.temperature,
                "num_predict": self.max_tokens
            }
        )

        for chunk in response:
            content = chunk.message.content
            if content:
                yield content

    def chat(self, messages):
        response = self.client.chat(
            model=self.model,
            messages=messages,
            options={
                "temperature": self.temperature,
                "num_predict": self.max_tokens
            }
        )
        return response.message.content