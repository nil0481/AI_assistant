import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
engine=pyttsx3.init()
voices=engine.getProperty('voices')
print (voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    print (audio)
    engine.say(audio)
    engine.runAndWait()
#if __name__=='main':
def wish():
    hr=datetime.datetime.now().hour
    if hr in range(0,12):
        speak("Good Morning!")
    elif hr in range(12,18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am your assisstant. How may I help you?")
wish()

def take():
    r=sr.Recognizer()
    s=1
    while s:
        with sr.Microphone() as source:
            print ("Say...")
            r.pause_threshold=0.8
            audio=r.listen(source)
          
            try:
                said=r.recognize_google(audio,language="en-in")
                speak ("you said: "+said)
                s=0
            except Exception:
                speak("please say again")
    return said
             
while True:
    said=take().lower()
    if 'wikipedia' in said:
        try:
            said=said.replace("wikipedia","")
            speak("please wait, let me search wikipedia")
            result=wikipedia.summary(said,sentences=2)
            speak(result)
            webbrowser.open("www.google.com")
            break
        except Exception:
            speak("No such wikipedia found")
            break
    elif 'music' in said:
        mdir='D:\Videos'
        song=os.listdir(mdir)
        #print (song)
        os.startfile(os.path.join(mdir,song[random.randint(0,11)]))
   
    
    
    
    