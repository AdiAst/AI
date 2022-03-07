import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak :")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print('You Said: {}'.format(text))
    except:
        print("Sorry Please speak Again")
