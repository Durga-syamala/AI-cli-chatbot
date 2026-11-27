
import pytest
from unittest.mock import patch

from core.factory import create_provider
from providers.ollama_provider import OllamaProvider
from providers.groq_provider import GroqProvider
from providers.gemini_provider import GeminiProvider
from providers.openrouter_provider import OpenRouterProvider


@pytest.mark.parametrize(
    "provider_name, expected_class",
    [
        ("ollama", OllamaProvider),
        ("groq", GroqProvider),
        ("gemini", GeminiProvider),
        ("openrouter", OpenRouterProvider),
    ]
)
def test_create_provider(provider_name, expected_class):

    with patch.object(
        expected_class,
        "__init__",
        return_value=None
    ):
        provider = create_provider(provider_name)

        assert isinstance(provider, expected_class)


def test_invalid_provider():

    with pytest.raises(ValueError):
        create_provider("invalid_provider")


def test_provider_name_case_insensitive():

    with patch.object(
        OllamaProvider,
        "__init__",
        return_value=None
    ):
        provider = create_provider("OLLAMA")

        assert isinstance(provider, OllamaProvider)
