import openai

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Initial prompt to generate an NPC
npc_prompt = "Create an NPC for a Dungeons & Dragons game. This NPC is a wise old wizard who resides in a tower deep within the enchanted forest."

# Dictionary to store NPC information
npc_information = {}

# Generate initial NPC information
def generate_initial_npc():
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choosing the appropriate GPT-3.5 engine
        prompt=npc_prompt,
        max_tokens=100  # response length
    )
    
    npc_information["description"] = response.choices[0].text.strip()

# Respond to player interaction
def respond_to_player(player_input):
    dialogue_prompt = f"Player: '{player_input}'\nNPC: '{npc_information['description']}'"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate GPT-3.5 engine
        prompt=dialogue_prompt,
        max_tokens=100  # response length
    )

    npc_response = response.choices[0].text.strip().split("NPC: ")[1]
    return npc_response

# Generate initial NPC
generate_initial_npc()

# Simulate player interactions
player_question = "What kind of magic spells do you specialize in?"
dynamic_npc_response = respond_to_player(player_question)

print("Initial NPC Description:", npc_information["description"])
print("Player Question:", player_question)
print("Dynamic NPC Response:", dynamic_npc_response)
