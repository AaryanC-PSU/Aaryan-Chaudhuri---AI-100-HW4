# OpenAI Terminal Chat

For this homework project, I built a terminal-based Python chat app that connects to the OpenAI API. The user can type prompts into the terminal, send them to the AI model, and read the responses directly in the command line. The program keeps running until the user types `exit` or `quit`.

I also added a few extra features beyond the basic requirements, including conversation history, a help menu, model switching, and the ability to save a transcript of the chat.

## My Approach

My intended approach was to start with the main homework requirement first: create a simple terminal loop where the user enters a prompt, the app sends it to OpenAI, and the response prints back in the terminal. After that worked, I organized the code into separate functions so it would be easier to read and maintain.

I used a `.env` file so the API key is not hardcoded into the program. I also added error handling so the program gives a clear message if the API key is missing or if the API request fails. Once the basic version was complete, I added commands like `help`, `history`, `clear`, `save`, and `model` to make the project more useful and complete.

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
