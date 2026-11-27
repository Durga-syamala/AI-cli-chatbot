
class Chatbot:

    def __init__(self, provider):
        self.provider = provider

        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]

    def ask(self, question):

        self.messages.append({
            "role": "user",
            "content": question
        })

        answer = ""

        try:
            for chunk in self.provider.stream(
                self.messages
            ):
                print(chunk, end="", flush=True)
                answer += chunk

            print()

            self.messages.append({
                "role": "assistant",
                "content": answer
            })

            return answer

        except Exception:
            self.messages.pop()
            raise