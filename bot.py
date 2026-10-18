import ollama
model="llama3.2:latest"
print(f"Hello this is {model}\n")
assistant_type=input("Whome should i pretend like:(Doctor/Friend...) ")

messages=[
    {
        "role":"system",
        "content":f"You are a {assistant_type}, reply to users queries with a short and meaningfull response"
    }
]

while True:
    user_prompt=input("You: ")
    if user_prompt=="bye":
        break
    user_role={"role":"user", "content":user_prompt}
    messages.append(user_role)

    response=ollama.chat(model=model, messages=messages)
    response=response.message.content
    print("Assistant: ",response)
    assistant_role={"role":"assistant", "content":response}
    messages.append(assistant_role)