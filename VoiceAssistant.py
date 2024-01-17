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
        
    elif user_input == "bye":
        text_to_speech("Goodbye, have a nice day!")
        root.destroy()
        entry.delete(0, tk.END)

    elif user_input == "date":
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        text_to_speech(f"Today's date is {current_date}.")
        entry.delete(0, tk.END)

    elif user_input == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        text_to_speech(f"The current time is {current_time}.")
        entry.delete(0, tk.END)
    
    elif user_input == "location":
        current_location = get_current_location()
        text_to_speech(f"You are currently located at {current_location}.")
        entry.delete(0, tk.END)

    elif user_input == "thanks":
        text_to_speech("You're Welcome")
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
        text_to_speech(f"Enter the first number for {operation}:")
        entry.delete(0, tk.END)
        ask_button.config(command=lambda: get_first_number(operation))
    else:
        text_to_speech("Invalid operation. Please choose from addition, subtraction, multiplication, or division.")

def get_first_number(operation):
    first_number = entry.get()
    try:
        float(first_number)
        text_to_speech(f"Enter the second number for {operation}:")
        entry.delete(0, tk.END)
        ask_button.config(command=lambda: perform_calculation(operation, float(first_number)))
    except ValueError:
        text_to_speech("Invalid input. Please enter a valid number.")

def perform_calculation(operation, first_number):
    second_number = entry.get()
    try:
        float(second_number)
        result = 0
        if operation == "addition":
            result = first_number + float(second_number)
        elif operation == "subtraction":
            result = first_number - float(second_number)
        elif operation == "multiplication":
            result = first_number * float(second_number)
        elif operation == "division":
            if float(second_number) != 0:
                result = first_number / float(second_number)
            else:
                text_to_speech("Error: Division by zero.")
                return

        text_to_speech(f"The result of {operation} is {result}.")
        ask_button.config(command=handle_user_input)
    except ValueError:
        text_to_speech("Invalid input. Please enter a valid number.")

root = tk.Tk()
root.title("Voice Assistant")

entry = tk.Entry(root, width=50)
entry.pack(pady=50)

ask_button = tk.Button(root, text="Ask", command=handle_user_input)
ask_button.pack()

root.mainloop()
