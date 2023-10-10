import openai
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import random
import time

# API key
openai.api_key = 'Enter your API key'

def generate_response(user_message):
    prompt = f"User: {user_message}\nChatGPT:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def save_to_file(question, answer):
    with open("queries_and_answers.txt", "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"Answer: {answer}\n\n")

def get_response():
    user_input = user_input_entry.get()
    if user_input:
        response = generate_response(user_input)
        save_to_file(user_input, response)
        # Add the question and answer to the history Text box
        history_text.config(state=tk.NORMAL)
        history_text.insert(tk.END, f"You: {user_input}\n")
        history_text.insert(tk.END, f"ChatGPT: {response}\n\n")
        history_text.config(state=tk.DISABLED)
        history_text.see(tk.END)

        user_input_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Info", "Please enter a question.")

def roll_dice(dice):
    if dice == "d4":
        return random.randint(1, 4)
    elif dice == "d6":
        return random.randint(1, 6)
    elif dice == "d8":
        return random.randint(1, 8)
    elif dice == "d10":
        return random.randint(1, 10)
    elif dice == "d12":
        return random.randint(1, 12)
    elif dice == "d20":
        return random.randint(1, 20)
    elif dice == "d100":
        return random.randint(1, 100)

def animate_roll(dice):
    for _ in range(5):
        roll = roll_dice(dice)
        dice_result.set(f"Rolling... {roll}")
        app.update()
        time.sleep(0.1)
    
    final_roll = roll_dice(dice)
    dice_result.set(f"Result: {final_roll}")

app = tk.Tk()
app.title("D&D Query Generator")

width = 1000
height = 800
app.geometry(f"{width}x{height}")

bg_image = Image.open("DDD.jpg")
bg_image_resized = bg_image.resize((width, height), Image.ANTIALIAS)
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

history_text = tk.Text(frame, width=80, height=10, wrap=tk.WORD, font=custom_font)
history_text.grid(row=2, column=0, columnspan=2, pady=20)
history_text.config(state=tk.DISABLED)

# Create a dice frame
dice_frame = tk.Frame(frame)
dice_frame.grid(row=3, column=0, columnspan=2, pady=10)

dice_result = tk.StringVar()
dice_result_label = tk.Label(dice_frame, textvariable=dice_result, font=custom_font_large)
dice_result_label.grid(row=0, columnspan=7, pady=10) # Use grid here instead of pack

# Create dice buttons
dice_types = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
for idx, dice in enumerate(dice_types):
    button = tk.Button(dice_frame, text=dice, 
                      command=lambda d=dice: animate_roll(d),
                      activebackground='#ADD8E6', activeforeground='#000000')
    button.grid(row=1, column=idx, padx=5) 

app.mainloop()
