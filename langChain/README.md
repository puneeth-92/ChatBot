Ollama Roleplay Chatbot

A simple, interactive AI chatbot built using Python, LangChain, Ollama, and Llama 3.2. It allows users to choose a role for the AI, such as a doctor, friend, or teacher, and interact with it through a command-line interface.

The chatbot uses LangChain to manage conversation messages and maintain chat history during execution, enabling context-aware responses.

Features

- 🎭 Custom AI Roles — Choose how the AI should behave by specifying a role.
- 🧠 Context-Aware Conversations — Maintains user messages and AI responses throughout the session.
- 💻 Local AI Execution — Runs Llama 3.2 locally using Ollama.
- 🔗 LangChain Integration — Uses LangChain message classes and ChatOllama to interact with the model.
- 💬 Concise Responses — Uses system prompting to encourage short, meaningful answers.
- 🔄 Interactive Chat — Continue conversations until you type bye.

Tech Stack

- Language: Python
- LLM Framework: LangChain
- AI Runtime: Ollama
- Language Model: Llama 3.2
- Interface: Command-Line Interface (CLI)

Prerequisites

Before running the project, ensure you have:

- Python 3.9 or later
- Ollama installed
- The Llama 3.2 model downloaded

Installation and Setup

1. Download the model

ollama pull llama3.2

2. Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate

3. Install the required Python libraries

pip install langchain-ollama langchain-core

4. Run the chatbot

python bot.py

Usage

1. Start the application.
2. Enter the role you want the AI to adopt, such as Friend, Teacher, or Doctor.
3. Type your messages and interact with the chatbot.
4. The chatbot uses previous messages to maintain conversational context.
5. Type bye to end the conversation.

Project Structure

ollama-roleplay-chatbot/
├── bot.py # Main chatbot implementation
├── README.md # Project documentation
└── .venv/ # Python virtual environment

Memory

The chatbot maintains conversation history using LangChain’s message classes. This allows the AI to refer to earlier messages during the current session.

Note: Conversation history is stored temporarily in memory and is not saved after the program terminates.

Future Improvements

- Add a graphical user interface.
- Allow users to switch roles during conversations.
- Implement persistent chat history using SQLite or JSON.
- Add error handling for model and connection issues.
- Introduce conversation summarization for longer sessions.

👨‍💻 Author

Puneeth J

⸻

Built with Python, LangChain, and Ollama to explore local LLM integration and conversational AI.
