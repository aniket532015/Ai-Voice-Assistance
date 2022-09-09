

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time
import subprocess
import ecapture as ec
import wolframalpha

import requests
import subprocess


print('Loading your AI personal assistant which will assist you to work without moving - Madmax Made by Aniket and Team')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voice[1].id')
#engine.setProperty("rate",120)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"User-->:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
            time.sleep(7)
        return statement

speak("Loading your AI personal assistant which will assist you to work without moving - Madmax made by sir-Aniket and team")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak('your personal assistant Madmax is shutting down,Good bye')
            print('your personal assistant Madmax is shutting down,Good bye')
            break



      

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print("time is ",strTime)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Madmax version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo' 
                  'get top headline news from times of india ')


        elif "made" in statement or "created" in statement or "discovered" in statement:
            speak("I was built by Sir-Aniket in 2022 for semester 4 project")
            print("I was built by Sir-Aniket in 2022 for semester 4 project")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            print("Takeing Photo Please wait 5 second")
            ec.capture(0,"robo camera","img.jpg")
          
           

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

    
        
        elif "open presentation" in statement or "open ppt" in statement:
            speak("It is opening")
            path=(r"C:\Users\akani\OneDrive\Desktop\Project.pptx")
            subprocess.Popen([path],shell=True)
            time.sleep(5)

        elif "off" in statement or "out" in statement:
            print("Turning off your pc")
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            time.sleep(6)
            subprocess.call(["shutdown", "/l"])
            
        elif "favourite" in statement or "realax" in statement:
            print("just wait a movement it will open soon and playing your favourite song which will relax you")
            speak("just wait a movement it will open soon and playing your favourite song which will relax you")
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=Z1ijuWA9Sfs&list=RDZ1ijuWA9Sfs&start_radio=1")
            
        elif "resume" in statement:
            print("Opening your resume Please wait a minute")
            speak("Opening your resume Please wait a minute")
            f=(r"C:/Users/akani/OneDrive/Desktop/Resume-Aniket-Kumar.pdf")
            subprocess.Popen([f],shell=True)
        
        elif "linkedin" in statement:
            print("opening your LinkedIn Profile")
            speak("opening your LinkedIn Profile")
            webbrowser.open_new_tab("https://www.linkedin.com/in/aniket-kumar-840b571b8/")
            
        elif "github" in statement:
            print("opening your GitHub Account")
            speak("opening your GitHub Account")
            webbrowser.open_new_tab("https://github.com/aniket532015")
      

time.sleep(5)












