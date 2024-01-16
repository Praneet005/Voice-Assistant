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
    elif user_input == "how are you":
        text_to_speech("I am great, thanks for asking.")
    elif user_input == "bye":
        text_to_speech("Goodbye, have a nice day!")
        root.destroy()
    elif user_input == "date":
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        text_to_speech(f"Today's date is {current_date}.")
    elif user_input == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        text_to_speech(f"The current time is {current_time}.")
    elif user_input == "location":
        current_location = get_current_location()
        text_to_speech(f"You are currently located at {current_location}.")
    elif user_input=="thanks":
        text_to_speech("You're Welcome")
    else:
        text_to_speech("Sorry, I do not understand your question")

root = tk.Tk()
root.title("Voice Assistant")

entry = tk.Entry(root, width=50)
entry.pack(pady=50)

ask_button = tk.Button(root, text="Ask", command=handle_user_input)
ask_button.pack()

root.mainloop()
