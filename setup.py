import openai

# Set your OpenAI API key here
#openai.api_key = " " #authentification
with open(r"/Users/kofwanalawson/Downloads/D&D_Key.rtf") as f:
    key = f.read()
openai.api_key  = key

# Define a prompt that outlines the task for the model
prompt = "You are ChatGPT, a helpful AI assistant. Answer the following questions:\n1. What is the capital of France?"

# Use the OpenAI API to generate a response
response = openai.Completion.create(
    engine="text-davinci-003",  # engine selection
    prompt=prompt, # need to provide input
    max_tokens=50  # limiting the length of the generated response
)

# Process and print the generated response
generated_text = response.choices[0].text
print(generated_text)
# had to remove my key and push again ahh