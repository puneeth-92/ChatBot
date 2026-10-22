from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model_name = "llama3.2:latest"

assistant_type=input("Whom should i pretend like:(Doctor/Friend...) ")

messages=[
    SystemMessage(f"You are a {assistant_type}, reply to users queries with a short and meaningfull response")
]

llm=ChatOllama(model=model_name)

while True:
    user_prompt=input("You: ")
    if user_prompt.lower() =="bye":
        break
    user_inp=HumanMessage(user_prompt)
    messages.append(user_inp)
    response=llm.invoke(messages)
    response=response.content
    print("Assistant: ",response)
    ai_res=AIMessage(response)
    messages.append(ai_res)