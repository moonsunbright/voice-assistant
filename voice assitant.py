import pyttsx3 as p 
import speech_recognition as sr
from news import *
import randfacts
import datetime
engine=p.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0and hour<12:
        return("morning")
    elif hour>=12 and hour<4:
        return("afternoon")
    else:
        return("evening")
    
today_date=datetime.datetime.now()
r=sr.Recognizer() 

speak("hello sir!, good "+ wishme()+",i am your voice assistant. HOw are you?")
speak("today is"+today_date.strftime("%d")+"of"+today_date.strftime("\B")+"And its currently"+(today_date.strftime("%I"))+today_date.strftime("%H")+today_date.strftime("%p"))
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak ("i am having a good day sir")
speak("what can i do for you?")

with sr. Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text2= r.recognize_google(audio)

if "news" in text2:
    print("Sure sir, Now i will read news for you")
    speak("Sure sir, Now i will read news for you")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
        
elif "fact" or "facts" in text2:
    speak("Sure Sir..") 
    x=randfacts.getFact() 
    print(x)
    speak("Did you know that,"+x)  
    