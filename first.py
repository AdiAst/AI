import re
import speech_recognition as sr
import random
import pyjokes
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 160)
voices = engine. getProperty('voices')
engine. setProperty('voice', voices[0]. id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def code():
    result = random.randint(1, 350000)
    return talk("Here Your Number", result)


def onRunning():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            if 'listen' in text:
                Mitha()
            elif 'thank you' or 'quit' in text:
                talk("My Pleasure")
            else:
                talk("Sorry Please speak Again")
                onRunning()
        except:
            talk("Sorry Please speak Again")
            onRunning()


def Mitha():
    with sr.Microphone() as source:
        talk("Yes Sir!!")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(text)
            if 'joke' in text:
                talk(pyjokes.get_joke())
                onRunning()
            elif 'random number' in text:
                code()
                onRunning()
            elif 'back' in text:
                onRunning()
            else:
                talk("Command not Found")
                Mitha()
        except:
            talk("Command not Found")
            Mitha()


onRunning()
