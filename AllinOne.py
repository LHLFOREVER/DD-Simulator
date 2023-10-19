# Main file

import openai
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

from DDDictionary import Environment

import random
from DDDictionary import Person, Status, Species, Attributes, Affiliation

# API key
openai.api_key = ''

def generate_response(user_message):
    prompt = f"User: {user_message}\nChatGPT:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def get_response():
    user_input = user_input_entry.get()
    if user_input:
        response = generate_response(user_input)

        # Add the question and answer to the history Text box
        history_text.config(state=tk.NORMAL)
        history_text.insert(tk.END, f"You: {user_input}\n")
        history_text.insert(tk.END, f"ChatGPT: {response}\n\n")
        history_text.config(state=tk.DISABLED)
        history_text.see(tk.END)

        user_input_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Info", "Please enter a question.")


app = tk.Tk()
app.title("D&D Query Generator")

width = 1000
height = 800
app.geometry(f"{width}x{height}")

bg_image = Image.open("DDD.jpg")

# Resize the image to fit the canvas
bg_image_resized = bg_image.resize((width, height))#, Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image_resized)

canvas = tk.Canvas(app, width=width, height=height)
canvas.pack(fill="both", expand=True)
custom_font = ("Arial", 14)
custom_font_large = ("Arial", 16)

# Place the resized image on the canvas
canvas.create_image(width/2, height/2, image=bg_photo)

# Attach a frame to the canvas
frame = tk.Frame(canvas)
canvas_window = canvas.create_window(width/2, height/2, window=frame)


label = tk.Label(frame, text="Question about D&D:", font=custom_font_large)
label.grid(row=0, column=0, padx=10, pady=10)

user_input_entry = tk.Entry(frame, width=50, font=custom_font)
user_input_entry.grid(row=0, column=1, padx=10, pady=10)

submit_button = tk.Button(frame, text="Generate", command=get_response, activebackground='red', activeforeground='#000000')
submit_button.grid(row=1, column=0, columnspan=2, pady=20)

history_text = tk.Text(frame, width=80, height=10, wrap=tk.WORD, font=custom_font)
history_text.grid(row=2, column=0, columnspan=2, pady=20)
history_text.config(state=tk.DISABLED)

app.mainloop()

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


#-----------------------------------------------------------------------------------------

# Adaptive_Storyline.py

# The generate_dnd_story function takes a game_state dictionary 
# and a player_action as input. This makes it more adaptable to different game situations in D&D.

def generate_dnd_story(game_state, player_action):
    # Construct a D&D-specific prompt
    prompt = f"In a world of magic and adventure, your party finds themselves in a {game_state['location']}.\n"
    prompt += f"The party consists of {', '.join(game_state['party_members'])}.\n"
    prompt += f"The player, {game_state['current_player']}, decides to {player_action}\n"
    prompt += "What happens next?"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
    )
    
    return response.choices[0].text

# Example usage:
game_state = {
    'location': random.choice(Environment['Region']),  # Use a random location from the dictionary
    'party_members': [random.choice(Person['Species']) for _ in range(3)],  # Random party members
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

#--------------------------------------------------------------------------------
#simulated NPCs.py


# Initial prompt to generate an NPC
npc_prompt = "Create an NPC for a Dungeons & Dragons game. This NPC is a wise old wizard who resides in a tower deep within the enchanted forest."

# Dictionary to store NPC information
npc_information = {}

# Generate initial NPC information
def generate_initial_npc():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=npc_prompt,
        max_tokens=100
    )
    
    npc_information["description"] = response.choices[0].text.strip()

# Respond to player interaction
def respond_to_player(player_input):
    dialogue_prompt = f"Player: '{player_input}'\nNPC: '{npc_information['description']}'"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=dialogue_prompt,
        max_tokens=100
    )

    npc_response = response.choices[0].text.strip().split("NPC: ")[0]
    return npc_response

# Generate initial NPC
generate_initial_npc()

# Simulate player interactions
player_question = "What kind of magic spells do you specialize in?"
dynamic_npc_response = respond_to_player(player_question)

print("Initial NPC Description:", npc_information["description"])
print("Player Question:", player_question)
print("Dynamic NPC Response:", dynamic_npc_response)
