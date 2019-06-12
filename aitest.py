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
       
if 1:
    said=take().lower()
    if 'wikipedia' in said:
        said=said.replace("wikipedia","")
        speak("please wait, let me search wikipedia")
        #print (said)
        result=wikipedia.summary(said,sentences=1)
        speak(result)
        speak("Do you want to open wikipedia?")
        ask=take().lower()
        if 'yes' or 'yep' in ask:
            webbrowser.open("https://en.wikipedia.org/wiki/Special:Search?search="+said+"&go=Go&ns0=1")
         
    elif 'music' in said or 'video' in said or 'song' in said:
        mdir='D:\Videos'
        song=os.listdir(mdir)
        #print (song)
        os.startfile(os.path.join(mdir,song[random.randint(0,10)]))
    elif 'open youtube' in said:
        speak("Opening Youtube")
        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab("youtube.com")
    elif 'open google' in said:
        speak("Opening Google")
        webbrowser.get('chrome').open_new_tab("google.com")
    elif 'time' in said:
        ps=datetime.datetime.now().strftime("%X")
        speak(ps)
    elif 'day' in said or 'date'in said:
        speak (datetime.datetime.now().strftime("%x"))
        speak("It's "+datetime.datetime.now().strftime("%A"))
    elif 'send mail' in said or 'email' in said:
        speak("Opening mail")
        webbrowser.get('chrome').open_new_tab("gmail.com")
        
    
