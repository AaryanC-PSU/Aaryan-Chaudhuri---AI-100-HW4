import os
from datetime import datetime

from dotenv import load_dotenv
from openai import OpenAI


DEFAULT_MODEL = "gpt-5"
TRANSCRIPT_FILE = "chat_history.txt"
SYSTEM_MESSAGE = (
    "You are a helpful AI assistant. Keep answers clear, useful, and concise."
)


def load_settings():
    """Load required and optional settings from the .env file."""
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing OPENAI_API_KEY. Copy .env.example to .env and add your API key."
        )

    model = os.getenv("OPENAI_MODEL", DEFAULT_MODEL)
    return api_key, model


def create_history():
    """Create the starting message history for the chat session."""
    return [{"role": "system", "content": SYSTEM_MESSAGE}]


def ask_openai(client, model, history):
    """Send the current conversation history to OpenAI and return the reply."""
    response = client.chat.completions.create(
        model=model,
        messages=history,
    )

    answer = response.choices[0].message.content
    if not answer:
        return "The model returned an empty response."

    return answer


def print_help():
    print("\nCommands:")
    print("  help           Show this help menu")
    print("  history        Show the current conversation history")
    print("  clear          Clear the conversation history")
    print("  save           Save the conversation to chat_history.txt")
    print("  model          Show the current model")
    print("  model <name>   Change the model for this session")
    print("  exit / quit    End the program")


def print_history(history):
    visible_messages = [message for message in history if message["role"] != "system"]

    if not visible_messages:
        print("\nNo conversation history yet.")
        return

    print("\nConversation history:")
    for number, message in enumerate(visible_messages, start=1):
        speaker = "You" if message["role"] == "user" else "AI"
        print(f"\n{number}. {speaker}: {message['content']}")


def save_history(history, filename=TRANSCRIPT_FILE):
    visible_messages = [message for message in history if message["role"] != "system"]

    if not visible_messages:
        print("\nNothing to save yet.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"OpenAI Terminal Chat Transcript\nSaved: {timestamp}\n\n")

        for message in visible_messages:
            speaker = "You" if message["role"] == "user" else "AI"
            file.write(f"{speaker}: {message['content']}\n\n")

    print(f"\nConversation saved to {filename}.")


def handle_command(command, history, model):
    """Handle built-in commands. Return the updated history, model, and exit flag."""
    lowered = command.lower()

    if lowered in {"exit", "quit"}:
        print("Goodbye!")
        return history, model, True

    if lowered == "help":
        print_help()
        return history, model, False

    if lowered == "history":
        print_history(history)
        return history, model, False

    if lowered == "clear":
        print("\nConversation history cleared.")
        return create_history(), model, False

    if lowered == "save":
        save_history(history)
        return history, model, False

    if lowered == "model":
        print(f"\nCurrent model: {model}")
        return history, model, False

    if lowered.startswith("model "):
        new_model = command.split(maxsplit=1)[1].strip()

        if not new_model:
            print("\nPlease enter a model name.")
            return history, model, False

        print(f"\nModel changed from {model} to {new_model}.")
        return history, new_model, False

    return history, model, None


def run_chat(client, model):
    history = create_history()

    print("OpenAI terminal chat")
    print(f"Model: {model}")
    print('Type "help" for commands or "exit" / "quit" to stop.')

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            print("Please enter a prompt or command.")
            continue

        history, model, should_exit = handle_command(user_input, history, model)

        if should_exit is True:
            break

        if should_exit is False:
            continue

        history.append({"role": "user", "content": user_input})

        try:
            answer = ask_openai(client, model, history)
        except Exception as error:
            history.pop()
            print(f"Error: Could not get a response from OpenAI. {error}")
            continue

        history.append({"role": "assistant", "content": answer})
        print(f"\nAI: {answer}")


def main():
    try:
        api_key, model = load_settings()
    except ValueError as error:
        print(f"Error: {error}")
        return

    client = OpenAI(api_key=api_key)
    run_chat(client, model)


if __name__ == "__main__":
    main()
