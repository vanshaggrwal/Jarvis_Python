import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.in")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)




if __name__ == "__main__":
    speak("Intializing Jarvis....")
    while True:
        r=sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio =r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio =r.listen(source,timeout=2,phrase_time_limit=1)
                    command=r.recognize_google(audio)
                    processCommand(command)
            
        except Exception as e:
            print("Error; {0}".format(e))


