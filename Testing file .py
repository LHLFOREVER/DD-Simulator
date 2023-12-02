# Main file
import openai
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import time
import random
import DDDictionary
from DDDictionary import *
import sqlite3
import pygame
openai.api_key = "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"

pygame.mixer.init()
#123
# Sound Functions
def play_sound(sound_file):
    pygame.mixer.Sound(sound_file).play()

def play_background_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1) 

class AutoGenFramework:
    def __init__(self, model="text-davinci-003"):
        self.model = model

    def generate_response(self, user_message):
        prompt = f"User: {user_message}\nChatGPT:"
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=400
        )
        return response.choices[0].text.strip()
auto_gen = AutoGenFramework()

def query_database(query):
    # Assuming you're looking for species information
    connection = sqlite3.connect('new_DD_database.db')
    cursor = connection.cursor()
    
    # Modify the query based on your schema and what information you want to retrieve
    cursor.execute("SELECT Race FROM Species WHERE Race LIKE ?", ('%' + query + '%',))
    result = cursor.fetchall()

    connection.close()
    if result:
        # If there are multiple matches, you can decide how to handle them, here we just join them
        return ', '.join([r[0] for r in result])
    else:
        return "No species found matching the query."
def query_person(query):
    connection = sqlite3.connect('new_DD_database.db')
    cursor = connection.cursor()

    # Convert query to lowercase for case-insensitive matching
    query = query.lower()
    sql_query = "SELECT * FROM Person WHERE lower(Status) LIKE ?"
    print(f"Executing SQL: {sql_query}, with query: {query}")

    cursor.execute(sql_query, ('%' + query + '%',))
    result = cursor.fetchall()
    print("Query Result:", result)  # Debugging: Print the result
    connection.close()
    return result
    

# Function to query the Person table
'''
def query_person(query):
    connection = sqlite3.connect('new_DD_database.db')
    cursor = connection.cursor()
    
    # Let's say you want to check if the 'query' is a valid status in the DDDictionary.py 'Person' list
    if query in DDDictionary.Person['Status']:
        # Modify the SQL query to use the 'Status' from the DDDictionary.py
        cursor.execute("SELECT * FROM Person WHERE Status = ?", (query,))
    else:
        return "Status not found in DDDictionary."

    result = cursor.fetchone()
    connection.close()
    if result:
        return f"Person: {result}"
    else:
        return "No person found matching your query."


'''
# Function to query the Enemy table
def query_enemy(query):
    connection = sqlite3.connect('new_DD_database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Enemy WHERE Name LIKE ?", ('%' + query + '%',))
    result = cursor.fetchone()
    connection.close()
    if result:
        return f"Enemy: {result}"
    else:
        return "No enemy found matching your query."

# Add more functions to query other tables as needed...

# Modified get_response Function to query the database based on table names



def save_to_file(question, answer):
    with open("queries_and_answers.txt", "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"Answer: {answer}\n\n")

def format_person_results(results):
    formatted_results = []
    for result in results:
        # Adjust the indexes according to the structure of 'result'
        formatted_result = f"Person ID {result[0]}, Status: {result[1]}, Affiliation: {result[2]}, HP: {result[3]},STR: {result[4]}, DEX: {result[5]},VIT: {result[6]}, INT: {result[7]}, SPD: {result[8]}, Species: {result[9]} , Level: {result[10]}, Experience: {result[11]}."
        formatted_results.append(formatted_result)
    return ' '.join(formatted_results)


def get_response():
    user_input = user_input_entry.get().strip()
    if user_input:
        if "query" in user_input.lower():
            query_term = user_input.lower().replace("query", "").strip()
            db_results = query_person(query_term)
            formatted_db_results = format_person_results(db_results)

            # Creating a D&D context prompt for ChatGPT
            chatgpt_prompt = f"In a D&D game setting, there are knights found in the database: {formatted_db_results} Can you describe a scenario or story involving these knights in a D&D adventure?"
            chatgpt_response = auto_gen.generate_response(chatgpt_prompt)

            # Combine database results and ChatGPT response
            final_response = f"{formatted_db_results}\n\n{chatgpt_response}"

            # Display the combined response in the GUI
            history_text.config(state=tk.NORMAL)
            history_text.insert(tk.END, f"You: {user_input}\n")
            history_text.insert(tk.END, f"ChatGPT: {final_response}\n\n")
            history_text.config(state=tk.DISABLED)
        else:
            # If no database-related keyword is detected, use the OpenAI API
            response = auto_gen.generate_response(user_input)
            # Display the ChatGPT response in the GUI
            history_text.config(state=tk.NORMAL)
            history_text.insert(tk.END, f"You: {user_input}\n")
            history_text.insert(tk.END, f"ChatGPT: {response}\n\n")
            history_text.config(state=tk.DISABLED)

        history_text.see(tk.END)
        user_input_entry.delete(0, tk.END)
        if "person" in user_input.lower():
            response = query_person(user_input)
        elif "enemy" in user_input.lower():
            response = query_enemy(user_input)
        # Add more conditions for other tables
        else:
            # If no database-related keyword is detected, use the OpenAI API
            response = auto_gen.generate_response(user_input)

        save_to_file(user_input, response)
        history_text.config(state=tk.NORMAL)
        history_text.insert(tk.END, f"You: {user_input}\n")
        history_text.insert(tk.END, f"ChatGPT: {response}\n\n")
        history_text.config(state=tk.DISABLED)
        history_text.see(tk.END)
        user_input_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Info", "Please enter a question.")



        

"""def get_response():
    user_input = user_input_entry.get()
    if user_input:
        response = "I don't understand that."
        # You could use a more sophisticated NLP solution here to determine intent
        if "person" in user_input.lower():
            response = query_person(user_input)
        elif "enemy" in user_input.lower():
            response = query_enemy(user_input)
        # Add more conditions for other tables
        else:
            # If no database-related keyword is detected, use the OpenAI API
            response = auto_gen.generate_response(user_input)

        save_to_file(user_input, response)
        history_text.config(state=tk.NORMAL)
        history_text.insert(tk.END, f"You: {user_input}\n")
        history_text.insert(tk.END, f"ChatGPT: {response}\n\n")
        history_text.config(state=tk.DISABLED)
        history_text.see(tk.END)
        user_input_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Info", "Please enter a question.")"""

def roll_dice(dice):
    return random.randint(1, int(dice[1:]))

def animate_roll(dice):
    for _ in range(5):
        roll = roll_dice(dice)
        dice_result.set(f"Rolling... {roll}")
        app.update()
        time.sleep(0.1)
    
    final_roll = roll_dice(dice)
    dice_result.set(f"Result: {final_roll}")

def generate_dnd_story(game_state, player_action):
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
def add_person_to_database():
    connection = sqlite3.connect('new_DD_database.db')
    # Prompt the user for person details
    status = simpledialog.askstring("Input", "Enter status (Nobility, Knight, Civilian, Criminal):")
    if status not in DDDictionary.Person['Status']:
        messagebox.showerror("Error", "Invalid status entered.")
        return
   
    affiliation = simpledialog.askstring("Input", "Enter affiliation (e.g., Farmer's Guild, Merchant's Guild):")
    if affiliation not in DDDictionary.Affiliation['Group']:
        messagebox.showerror("Error", "Invalid affiliation entered.")
        return
   
    species = simpledialog.askstring("Input", "Enter species (e.g., Elf, Dwarf, Human):")
    if species not in DDDictionary.Species['Race']:
        messagebox.showerror("Error", "Invalid species entered.")
        return
   
    level = simpledialog.askinteger("Input", "Enter level (numeric):")
    experience = simpledialog.askinteger("Input", "Enter experience (numeric):")
   
    # Connect to the database and insert the new person
    cursor = connection.cursor()
   
    cursor.execute('''
        INSERT INTO Person (Status, Affiliation, HP, STR, DEX, VIT, INT, SPD, Species, Level, Experience)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (status, affiliation, 1, 1, 1, 1, 1, 1, species, level, experience))
   
    connection.commit()
    connection.close()
   
    messagebox.showinfo("Success", "New person added to the database.")
    success_message = f"New person added: Status: {status}, Affiliation: {affiliation}, Species: {species}, Level: {level}, Experience: {experience}"
    messagebox.showinfo("Success", success_message)
    return success_message




# Tkinter App Setup
app = tk.Tk()
app.title("D&D Query Generator")

width = 1000
height = 800
app.geometry(f"{width}x{height}")

bg_image = Image.open("DDD.jpg")
bg_image_resized = bg_image.resize((width, height))
bg_photo = ImageTk.PhotoImage(bg_image_resized)

canvas = tk.Canvas(app, width=width, height=height)
canvas.pack(fill="both", expand=True)

canvas.create_image(width/2, height/2, image=bg_photo)
frame = tk.Frame(canvas)
canvas_window = canvas.create_window(width/2, height/2, window=frame)

custom_font = ("Arial", 14)
custom_font_large = ("Arial", 16)

label = tk.Label(frame, text="Question about D&D:", font=custom_font_large)
label.grid(row=0, column=0, padx=10, pady=10)

user_input_entry = tk.Entry(frame, width=50, font=custom_font)
user_input_entry.grid(row=0, column=1, padx=10, pady=10)

submit_button = tk.Button(frame, text="Generate", command=get_response, activebackground='red', activeforeground='#000000')
submit_button.grid(row=1, column=0, columnspan=2, pady=20)
# ... [Your existing GUI setup code]

add_person_button = tk.Button(frame, text="Add Person", command=add_person_to_database)
add_person_button.grid(row=4, column=0, pady=10)  # Adjust the row and column indices as per your GUI layout

# ... [Rest of your GUI mainloop here]


history_text = tk.Text(frame, width=80, height=10, wrap=tk.WORD, font=custom_font)
history_text.grid(row=2, column=0, columnspan=2, pady=20)
history_text.config(state=tk.DISABLED)

# Dice Frame
dice_frame = tk.Frame(frame)
dice_frame.grid(row=3, column=0, columnspan=2, pady=10)

dice_result = tk.StringVar()
dice_result_label = tk.Label(dice_frame, textvariable=dice_result, font=custom_font_large)
dice_result_label.grid(row=0, columnspan=7, pady=10)

dice_types = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
for idx, dice in enumerate(dice_types):
    button = tk.Button(dice_frame, text=dice, 
                      command=lambda d=dice: animate_roll(d),
                      activebackground='#ADD8E6', activeforeground='#000000')
    button.grid(row=1, column=idx, padx=5) 
def on_closing():
    pygame.mixer.quit()
    app.destroy()
#play_background_music("background_music.mp3")
app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
