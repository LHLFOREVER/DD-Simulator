import openai
import tkinter as tk
from tkinter import simpledialog, messagebox

#API key
openai.api_key = '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'

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
        history_text.config(state=tk.NORMAL)  # Enable editing
        history_text.insert(tk.END, f"You: {user_input}\n")
        history_text.insert(tk.END, f"ChatGPT: {response}\n\n")
        history_text.config(state=tk.DISABLED)  # Disable editing
        history_text.see(tk.END)  # Scroll to the end

        # Clear the input field for the next question
        user_input_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Info", "Please enter a question.")

app = tk.Tk()
app.title("D&D Query Generator")

frame = tk.Frame(app)
frame.pack(pady=20, padx=20)

label = tk.Label(frame, text="Question about D&D:")
label.grid(row=0, column=0, padx=10, pady=10)

user_input_entry = tk.Entry(frame, width=50)
user_input_entry.grid(row=0, column=1, padx=10, pady=10)

submit_button = tk.Button(frame, text="Generate", command=get_response)
submit_button.grid(row=1, column=0, columnspan=2, pady=20)

# Create a Text widget for the history
history_text = tk.Text(app, width=80, height=10, wrap=tk.WORD)
history_text.pack(pady=20)
history_text.config(state=tk.DISABLED)  # Set initial state to DISABLED so user can't edit the contents directly

app.mainloop()
