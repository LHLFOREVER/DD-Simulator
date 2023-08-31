import openai

openai.api_key = 'Your API key '

def generate_response(user_message):
    prompt = f"User: {user_message}\nChatGPT:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the desired engine
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()
while True:
    user_input = input("Question about D&D: ")
    if user_input.lower() == 'exit':
        break
    response = generate_response(user_input)
    print("D&D query generator:", response)
