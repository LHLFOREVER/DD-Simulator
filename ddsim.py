import openai

with open(r"c:\Users\adith\OneDrive\Documents\College\Alpha\DS440\ddsim.txt") as f:
    key = f.read()
openai.api_key  = key

def prompt_user(message):
    prompt = f"User: {message}\nChatGPT:"
    model = "text-davinci-003"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 50
    )
    return response.choices[0].text.strip()

while True:
    user_input = input("What is your question?: ")
    if user_input.lower() == 'exit':
        break
    response = prompt_user(user_input)
    print("D&D query generator:", response)

