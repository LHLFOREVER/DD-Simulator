# Dungeons-and-Dragons-Simulator
'''python 
import openai

openai.api_key = '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'

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
'''
