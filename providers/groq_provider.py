
import os
from groq import Groq
from providers.base import BaseProvider


class GroqProvider(BaseProvider):

    def __init__(
        self,
        model="llama-3.3-70b-versatile",
        **kwargs
    ):
        super().__init__(model, **kwargs)

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def stream(self, messages):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_completion_tokens=self.max_tokens,
            stream=True
        )

        for chunk in response:
            if chunk.choices:
                content = chunk.choices[0].delta.content

                if content:
                    yield content

    def chat(self, messages):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_completion_tokens=self.max_tokens
        )

        return response.choices[0].message.content or ""
