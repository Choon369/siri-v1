import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ... ")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"sir said: {query}\n")
    except Exception as e:
        print("say that again plz...")
        return "None"
    return query





def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING")
    elif hour>=12 and hour <17:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am Siri sir ,How may I help you")


if __name__ == '__main__':
    wishme()
    while True :
        query = takecommand().lower()

        if 'wikipedia'in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results =wikipedia.summary(query,sentences=3)
            speak("Accordinf=g to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")