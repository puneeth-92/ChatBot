Ollama Roleplay Chatbot

A simple, interactive AI chatbot built using Python, Ollama, and Llama 3.2. It allows users to choose a role for the AI, such as a doctor, friend, or teacher, and interact with it through a command-line interface.

The chatbot maintains conversation history during execution, enabling context-aware responses.

Features

* 🎭 Custom AI Roles — Choose how the AI should behave by specifying a role.
* 🧠 Context-Aware Conversations — Maintains chat history to provide relevant responses.
* 💻 Local AI Execution — Runs Llama 3.2 locally using Ollama.
* 💬 Concise Responses — Uses system prompting to encourage short, meaningful answers.
* 🔄 Interactive Chat — Continue conversations until you choose to exit.

Tech Stack

* Language: Python
* AI Runtime: Ollama
* Language Model: Llama 3.2
* Interface: Command-Line Interface (CLI)

Prerequisites

Before running the project, ensure you have:

* Python 3.9 or later
* Ollama installed
* The Llama 3.2 model downloaded

Installation and Setup

1. Download the model

ollama pull llama3.2

2. Install the required Python library

pip install ollama

3. Run the chatbot

python bot.py

Usage

1. Start the application.
2. Enter the role you want the AI to adopt, such as Friend, Teacher, or Doctor.
3. Type your messages and interact with the chatbot.
4. Type bye to end the conversation.

Project Structure

ollama-roleplay-chatbot/
├── bot.py       # Main chatbot implementation
└── README.md    # Project documentation

Future Improvements

* Add a graphical user interface.
* Allow users to switch roles during conversations.
* Implement persistent chat history.
* Add error handling for model and connection issues.

👨‍💻 Author

Puneeth J

⸻

Built with Python and Ollama to explore local LLM integration and conversational AI.
