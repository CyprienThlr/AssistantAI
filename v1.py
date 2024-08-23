import speech_recognition as sr
import nltk
import spacy
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Hello ! I'm lEXA. How can I help you today ?")


nltk.download('punkt')
nlp = spacy.load('en_core_web_sm')

recognizer = sr.Recognizer()
microphone = sr.Microphone()

with microphone as source:
    print("Listening...")
    audio = recognizer.listen(source)
    command = recognizer.recognize_google(audio)
    print(f"You said: {command}")

doc = nlp(command)
for token in doc:
    print(token.text, token.lemma_, token.pos_)

def process_command(command):
    if "weather" in command:
        speak("Fetching the weather for you.")
        # Logique pour obtenir la météo
    elif "lights" in command:
        speak("Turning the lights on.")
        # Logique pour contrôler les lumières
    else:
        speak("I'm sorry, I didn't understand that.")
