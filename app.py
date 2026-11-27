
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from core.factory import create_provider
from core.chatbot import Chatbot
from core.usage_tracker import UsageTracker

load_dotenv()

console = Console()
tracker = UsageTracker()

MODELS = {
    "ollama": "qwen2.5:1.5b",
    "groq": "llama-3.3-70b-versatile",
    "gemini": "gemini-2.5-flash",
    "openrouter": "nvidia/nemotron-3-ultra:free"
}


def main():

    console.print(
        Panel(
            "MULTI LLM CHATBOT\n"
            "Ollama | Groq | Gemini | OpenRouter",
            title="CLI-multi-LLM-chatbot"
        )
    )

    provider_name = Prompt.ask(
        "Select provider",
        choices=list(MODELS.keys()),
        default="ollama"
    )

    model = MODELS[provider_name]

    console.print(f"[green]Selected model: {model}[/green]")

    temperature = float(
        Prompt.ask("Temperature", default="0.7")
    )

    max_tokens = int(
        Prompt.ask("Maximum output tokens", default="1024")
    )

    provider = create_provider(
        provider_name,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens
    )

    bot = Chatbot(provider)

    console.print("\n[green]Chat started![/green]")
    console.print(
        "Commands: /exit, /clear, /usage, /help"
    )

    while True:

        question = Prompt.ask("\n[bold cyan]You[/bold cyan]")

        if question == "/exit":
            break

        elif question == "/clear":
            bot.messages = bot.messages[:1]
            console.print("[yellow]Conversation cleared.[/yellow]")
            continue

        elif question == "/usage":
            tracker.show()
            continue

        elif question == "/help":
            console.print(
                "/exit  - Exit chatbot\n"
                "/clear - Clear conversation\n"
                "/usage - Show usage report"
            )
            continue

        try:
            console.print("\n[bold green]AI[/bold green]: ")
            bot.ask(question)
            tracker.record()

        except Exception as error:
            console.print(f"[red]Error: {error}[/red]")

    tracker.show()
    console.print("Goodbye!")


if __name__ == "__main__":
    main()
