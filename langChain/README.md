Local AI Chatbot

A simple Python chatbot built using LangChain and Ollama. Choose an assistant personality, such as a friend or doctor, and chat with a locally running LLM.

Features

- 🤖 Choose an assistant personality.
- 💬 Maintains conversation history during the session.
- 🖥️ Runs locally using Ollama.
- 🔗 Uses LangChain to manage messages and interact with the model.

Tech Stack

- Python
- LangChain
- Ollama
- Llama 3.2

Installation

1. Install Ollama

Download Ollama from ollama.com.

2. Download the model

ollama pull llama3.2

3. Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate

4. Install dependencies

pip install langchain-ollama langchain-core

Usage

Run the Python script:

python hello.py

Choose an assistant personality when prompted:

Whom should I pretend like: (Doctor/Friend/...)

Start chatting with the assistant. Type bye to exit.

Memory

The chatbot maintains conversation history in memory while the program is running. Previous conversations are not saved after the program terminates.

License

This project is open-source and available for learning and experimentation.
