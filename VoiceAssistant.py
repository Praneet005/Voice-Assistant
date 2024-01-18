import subprocess
import tkinter as tk
from gtts import gTTS
import os
import datetime
import geocoder

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

    subprocess.run(["afplay", "output.mp3"])

    os.remove("output.mp3")

def get_current_location():
    location = geocoder.ip('me')
    return location

def handle_user_input():
    user_input = entry.get().lower()

    if user_input in ["hi", "hello"]:
        text_to_speech("Hello, how may I help you?")
        entry.delete(0, tk.END)
    elif user_input == "how are you":
        text_to_speech("I am great, thanks for asking.")
        entry.delete(0, tk.END)

    elif user_input == "calculate":
        text_to_speech("Choose an operation: addition, subtraction, multiplication, or division.")
        entry.delete(0, tk.END)
        ask_button.config(command=calculate_operation)
        entry.delete(0, tk.END)
    else:
        text_to_speech("Sorry, I do not understand your question")
        entry.delete(0, tk.END)

def calculate_operation():
    operation = entry.get().lower()
    if operation in ["addition", "subtraction", "multiplication", "division"]:
        text_to_speech(f"Enter numbers separated by commas for {operation}:")
        entry.delete(0, tk.END)
        ask_button.config(command=lambda: perform_calculation(operation))
    else:
        text_to_speech("Invalid operation. Please choose from addition, subtraction, multiplication, or division.")

def perform_calculation(operation):
    numbers = entry.get().split(',')
    try:
        numbers = [float(num) for num in numbers]
        result = 0

        if operation == "addition":
            result = sum(numbers)
        elif operation == "subtraction":
            result = numbers[0] - sum(numbers[1:])
        elif operation == "multiplication":
            result = 1
            for num in numbers:
                result *= num
        elif operation == "division":
            if 0 not in numbers[1:]:
                result = numbers[0] / numbers[1]
            else:
                text_to_speech("Error: Division by zero or zero in denominator.")
                return

        text_to_speech(f"The result of {operation} is {result}.")
        ask_button.config(command=handle_user_input)
    except ValueError:
        text_to_speech("Invalid input. Please enter valid numbers separated by commas.")

root = tk.Tk()
root.title("Voice Assistant")

entry = tk.Entry(root, width=50)
entry.pack(pady=50)

ask_button = tk.Button(root, text="Ask", command=handle_user_input)
ask_button.pack()

root.mainloop()
