import openai

# Replace 'your-api-key' with your actual API key
api_key = 'your-api-key'
openai.api_key = api_key


# The generate_dnd_story function takes a game_state dictionary 
# and a player_action as input. This makes it more adaptable to different game situations in D&D.

def generate_dnd_story(game_state, player_action):
    # Construct a D&D-specific prompt
    prompt = f"In a world of magic and adventure, your party finds themselves in a {game_state['location']}.\n"
    prompt += f"The party consists of {', '.join(game_state['party_members'])}.\n"
    prompt += f"The player, {game_state['current_player']}, decides to {player_action}\n"
    prompt += "What happens next?"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
    )
    
    return response.choices[0].text

# Example usage:
game_state = {
    'location': 'mysterious cave',
    'party_members': ['wizard', 'rogue', 'fighter'],
    'current_player': 'John',
}

player_action = "explore the dark corners of the cave, searching for hidden treasure."

generated_text = generate_dnd_story(game_state, player_action)
print(generated_text)



# The prompt is constructed to include details about the game state, location,
# party members, and the current player's action. This helps set the context for
# the AI to generate a more relevant and immersive narrative.
# Need to customize the game_state dictionary to reflect the current state of 
# your D&D game, including the location, party members, and the current player.
# The generated text will continue the story in a D&D-like context based on the provided
# game state and player action.
