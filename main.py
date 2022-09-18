import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
import random
import pyperclip
import re
import string
import requests
import json
import time as _time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

print("stating......")
NAME="user" #change it to your prefered NAME
songs_dir="<file>" #add your music file directory here
ainame="windows" # chang your personal assistant name here
engine=pyttsx3.init("sapi5") # micorphone driver sapi5
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) #choosing male or female voice
def speak(text): #speaks the sent text
  engine.say(text)
  engine.runAndWait()

def wishMe(): #this code wishes the user and the global variable is set as NAME
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good morning.. "+NAME)
  elif hour>=12 and hour<6:
    speak("Good afternoon.. "+NAME)
  else:
    speak("Good evening "+NAME)

  #speak("I am your personal assistant how may I help you")
def create(name_acc,password):
    a=str(name_acc)
    b=str(password)
    d = os.path.dirname(__file__)
    f=open(d+"\password.txt", "a+")
    w=str(a+" -> "+b)
    f.write(w)
    f.close()



#this function take the voice and convert into command from the microphone
def takeCommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("listening")
    audio = r.listen(source)
    try:
      print("Recognising")
      query=r.recognize_google(audio,language='en-in')
      print(f"user said: {query}\n")
    except Exception as e:
      print("could not understand..")
      query="hello"
    return query
def myvol(to):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if to == 100:
        volume.SetMasterVolumeLevel(-0.0, None) #max
    if to> 50 and to<100:
        volume.SetMasterVolumeLevel(-5.0, None) #72%
    if to==50:
        volume.SetMasterVolumeLevel(-10.0, None) #51%

# Main program starts here
speak("starting....")
wishMe()
def main():
    query=takeCommand()
    comm=query.lower()
    if ainame in comm:
        command=comm.replace(ainame,"")
        if "wikipedia" in command:#searching in wikipedia
          speak("searching..")
          command=command.replace("wikipedia","")
          print(command)
          results=wikipedia.wikipedia.summary(command,sentences=2)
          speak(results)
          page=wikipedia.wikipedia.page(results)# gets the page of wikki search
          url=page.url# gets the url of the wikkipedia
          speak("To know more check "+url)
          print(url)

        elif "open youtube" in command:# to open youtube
            speak("opening youtube")
            webbrowser.open("https://youtube.com")

        elif "open gmail" in command:# to open gmail
            speak("opening gmail")
            url = "https://mail.google.com/"
            webbrowser.open(url)

        elif "open protonmail" in command:# to open protonmail
            speak("opening proton mail")
            url = "https://protonmail.com/"
            webbrowser.open(url)

        elif "open whatsapp" in command:# to open whatsapp
            speak("opening whatsapp web in browser")
            url = "https://web.whatsapp.com/"
            webbrowser.open(url)

        elif "open project" in command:# to open project on github
            speak("opening Amith Shankar in github")
            url = "https://github.com/AmithShankar"
            webbrowser.open(url)

        elif "on youtube" in command: # to play music on youtube
            song=command.replace("on youtube","")
            if "play" in song:
                song=command.replace("play","")
            speak("playing"+song)
            pywhatkit.playonyt(song)

        elif 'time' in command:# to tell the time
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif 'joke' in command:# search for pyjokes
            speak(pyjokes.get_joke())

        elif "play music" in command:# plays music on default music player
            if songs_dir=="<file>":
                speak("please specify your music directory in the code")
            else:
                speak("playing music on default music player")
                songs=os.listdir(songs_dir)# lists all the music from the directory
                print(len(songs))
                ma=int(len(songs))#suffles the music
                i=random.randint(0,ma)
                os.startfile(os.path.join(songs_dir,songs[i])) #This opens the file

        elif "search" in command:# this performs woogle searching
            ui=command.replace("search","")
            webbrowser.open("https://whoogle.sdf.org/search?q="+ui)

            #can also replace the open with empty string and add the desired extension to the website in order to go the website of choice

        elif "generate password" in command:#generates password
            try:
                num = [int(word) for word in command.split() if word.isdigit()] # finds the integer value in the text
                lon = num[0]# limits the integer value to the first one
                letters = string.ascii_lowercase + string.digits + string.punctuation
                password = ''.join(random.choice(letters) for i in range(lon)) #gets the digit form the user
                print(password)
                pyperclip.copy(password)
                speak("password generated check password.txt file for the password also clipboard")
                name_acc=re.findall("for (\w+)",command)
                create(name_acc,password)
            except:
                letters = string.ascii_lowercase + string.digits + string.punctuation
                password = ''.join(random.choice(letters) for i in range(8)) # if user dosent specify the size of password 8 is used as default
                print(password)
                pyperclip.copy(password)
                speak("password generated with default size check password.txt file for the password also clipboard")
                name_acc=re.findall("for (\w+)",command)#searches for the account name
                create(name_acc,password)# create the file
        elif "volume" in command:
            io=command.replace("set volume to","")
            to=int(io)
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            if volume.GetMute==0:
                myvol(to)
            else:
                volume.SetMute(0,None)#to make surte the the speakeres are not muted
                myvol(to)

        elif "mute" in command:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            volume.SetMute(1,None)
        elif "news headlines" in command:
            try:
                url = ('https://newsapi.org/v2/top-headlines?''country=in&'
                       'apiKey=a1061e9ef7a84860a763d1eda933c048')
                response = requests.get(url)
                news = json.loads(response.text)
                i=0
                for new in news['articles']:
                    # print(str(new['title']), "\n\n")
                    news_title = (str(new['title']))
                    speak(news_title)
                    _time.sleep(1)
                    i=i+1
                    if i==3:
                        break
            except:
                speak("No internet connection")
        elif "news description" in command:
            try:
                url = ('https://newsapi.org/v2/top-headlines?''country=in&'
                       'apiKey=a1061e9ef7a84860a763d1eda933c048')
                response = requests.get(url)
                news = json.loads(response.text)
                for new in news['articles']:
                    # print(str(new['title']), "\n\n")
                    news_title = (str(new['description']))
                    speak(news_title)
                    _time.sleep(1)
                    i=i+1
                    if i==3:
                        break
            except:
                speak("No internet connection")

        elif "exit" in command:
            speak("bye.....")
            return 0 # changes the value of the while loop and stops the program

while True:
    a=main()
    if a==0: # if the function returns 0 the break statement stops the code from executing
        break
