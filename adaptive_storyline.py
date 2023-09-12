import openai

# Replace 'your-api-key' with your actual API key
api_key = 'your-api-key'
openai.api_key = api_key

def generate_story(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=100,  # Adjust the desired length of the response
        n=1,  # Number of responses to generate
        stop=None,  # You can specify stop tokens to end the response
    )
    return response.choices[0].text

# Example usage:
game_state = {}  # Store the game state here
player_action = "The player explores a mysterious cave."

prompt = f"Game State: {game_state}\nPlayer Action: {player_action}\nGenerate the next part of the story:"

generated_text = generate_story(prompt)
print(generated_text)
