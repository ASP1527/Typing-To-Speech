import os
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


ended = False

while not ended:
    print("Type: ")
    text = input()
    text = text.lower()
    if text == "end":
        ended = True
    if text != "" and not ended:
        speak(text)
        os.remove('voice.mp3')
