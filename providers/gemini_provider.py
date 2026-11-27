
import os
from google import genai
from google.genai import types
from providers.base import BaseProvider

class GeminiProvider(BaseProvider):

    def __init__(self, model="gemini-2.5-flash",
                 **kwargs):
        super().__init__(model, **kwargs)
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def _contents(self, messages):
        contents = []

        for msg in messages:
            if msg["role"] == "system":
                continue

            role = (
                "model" if msg["role"] == "assistant"
                else "user"
            )

            contents.append(
                types.Content(
                    role=role,
                    parts=[
                        types.Part.from_text(text=msg["content"])
                    ]
                )
            )

        return contents

    def _system_instruction(self, messages):
        for msg in messages:
            if msg["role"] == "system":
                return msg["content"]
        return None

    def stream(self, messages):
        response = self.client.models.generate_content_stream(
            model=self.model,
            contents=self._contents(messages),
            config=types.GenerateContentConfig(
                temperature=self.temperature,
                max_output_tokens=self.max_tokens,
                system_instruction=self._system_instruction(
                    messages
                )
            )
        )

        for chunk in response:
            if chunk.text:
                yield chunk.text

    def chat(self, messages):
        response = self.client.models.generate_content(
            model=self.model,
            contents=self._contents(messages),
            config=types.GenerateContentConfig(
                temperature=self.temperature,
                max_output_tokens=self.max_tokens,
                system_instruction=self._system_instruction(
                    messages
                )
            )
        )

        return response.text or ""