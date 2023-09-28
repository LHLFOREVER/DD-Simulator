import openai
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

# API key
openai.api_key = 'enter API key'

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
bg_image_resized = bg_image.resize((width, height), Image.ANTIALIAS)
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

submit_button = tk.Button(frame, text="Generate", command=get_response, activebackground='#ADD8E6', activeforeground='#000000')
submit_button.grid(row=1, column=0, columnspan=2, pady=20)

history_text = tk.Text(frame, width=80, height=10, wrap=tk.WORD, font=custom_font)
history_text.grid(row=2, column=0, columnspan=2, pady=20)
history_text.config(state=tk.DISABLED)

app.mainloop()

