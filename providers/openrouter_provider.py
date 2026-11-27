
import os
from openai import OpenAI
from providers.base import BaseProvider

class OpenRouterProvider(BaseProvider):

    def __init__(self, model="openai/gpt-4o-mini",
                 **kwargs):
        super().__init__(model, **kwargs)

        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    def stream(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stream=True
        )

        for chunk in response:
            content = chunk.choices[0].delta.content

            if content:
                yield content

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        return response.choices[0].message.content or ""