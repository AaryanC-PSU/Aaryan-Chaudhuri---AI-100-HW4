# OpenAI Terminal Chat

This project is a terminal-based Python chat app that connects to the OpenAI API. Users can type prompts, receive AI responses, keep a conversation history, switch models during a session, and save the chat transcript.

## Features

- Loads the API key from a `.env` file
- Shows a clear error if the API key is missing
- Runs continuously until the user types `exit` or `quit`
- Keeps conversation context during the session
- Supports built-in commands such as `help`, `history`, `clear`, `save`, and `model`
- Saves transcripts to `chat_history.txt`
- Keeps secrets out of Git with `.gitignore`

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

3. Open `.env` and add your OpenAI API key:

   ```text
   OPENAI_API_KEY=your_real_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

4. Run the program:

   ```bash
   python main.py
   ```

## Commands

```text
help           Show the help menu
history        Show the current conversation history
clear          Clear the conversation history
save           Save the conversation to chat_history.txt
model          Show the current model
model <name>   Change the model for this session
exit / quit    End the program
```
