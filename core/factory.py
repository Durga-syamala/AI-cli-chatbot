
from providers.ollama_provider import OllamaProvider
from providers.groq_provider import GroqProvider
from providers.gemini_provider import GeminiProvider
from providers.openrouter_provider import OpenRouterProvider

PROVIDERS = {
    "ollama": OllamaProvider,
    "groq": GroqProvider,
    "gemini": GeminiProvider,
    "openrouter": OpenRouterProvider,
}

def create_provider(name, model=None, **kwargs):

    name = name.lower()

    if name not in PROVIDERS:
        raise ValueError(
            f"Unsupported provider: {name}"
        )

    provider_class = PROVIDERS[name]

    if model:
        return provider_class(model=model, **kwargs)

    return provider_class(**kwargs)