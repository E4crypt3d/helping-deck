from datetime import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import json
with open("config.json",'r') as file:
    config = json.load(file)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(speech):
    engine.say(speech)
    engine.runAndWait()

def user_command():
    r = sr.Recognizer()
    r.pause_threshold = 1
    r.dynamic_energy_adjustment_damping = 0.80
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
    except sr.UnknownValueError:
        query = "Sorry Sir I could not understand that"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "None"
    except Exception as e:
        speak("No Results found.!")
        return "None"
    return query
    
def wishing():
    time = int(datetime.now().hour)
    if time>=4 and time<12:
        speak("Good Morning Sir!")
    elif time>=12 and time<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    
def wikipedia_search(query):
    speak("Searching Wikipedia")
    query = str(query).replace('wikipedia','')
    try:
        wiki = wikipedia.summary(query, sentences=2)
        speak("According to the Wikipedia")
        print("According to the Wikipedia")
        print(wiki)
        speak(wiki)
    except wikipedia.exceptions.DisambiguationError as e:
        say = str(e).split(':')
        speak(say[0])
        print(e)
    return "None"
if __name__ == '__main__':
    wishing()
    while True:
        query = user_command().lower()
        
        if "wikipedia" in query or 'search' in query:
            wikipedia_search(query)
            
        elif "exit" in query or 'close' in query:
            speak("Exiting now. Have a good day sir")
            print("Bye take care")
            exit()
            
        elif "open google" in query:
            speak("opening google")
            webbrowser.open('https://www.google.com')
            
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open('https://www.youtube.com')
            
        elif "play my playlist" in query or "play music" in query:
            speak("playing music")
            webbrowser.open(config['music_playlist'])
        elif "open stack overflow" in query:
            speak("opening stackoverflow")
            webbrowser.open('https://stackoverflow.com')
            
        elif "open my website" in query or "open just coded blog":
            speak("opening Just Coded blog")
            webbrowser.open(config['your_website'])
            
        elif "open vs code" in query or "open code" in query:
            speak("opening visual code studio")
            os.startfile(config['vscode_path'])
            
        elif "open sublime" in query or "open sublime text" in query:
            speak("opening sublime text")
            os.startfile(config['sublime_path'])
        else:
            speak(query)