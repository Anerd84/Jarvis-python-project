import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import random
import shutil
import subprocess
import wolframalpha
import tkinter
import json
import operator
import winshell
import pyjokes
import feedparser
import ctypes
import requests
import pywhatkit as kit
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    t1 = datetime.datetime.now().strftime("%H:%M;%S")
    if(hour >= 0 and hour < 12):
        speak(f"Good morning , its {t1}")
    elif(hour >= 12 and hour < 18):
        speak(f"good afternoon,its {t1}")

    else:
        speak(f"good evening its {t1}")

    speak("helo! i am Your Assistant Jarvious 1.0 ")
    assname = "Jarvis 1 point 0"
def username():
    speak("What should i call you sir")
    uname = take_comand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    speak("Please tell me how can i help you sir ")
def take_comand():
    r = sr.Recognizer()
    myMic = sr.Microphone(device_index = 0)
    with myMic as source:
        print("Listening....")
        r.energy_threshold = 150
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognzing.....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print("say it again please...")
        return "None"
    return query
     
    speak("How can i Help you, Sir")
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('aakashmundara@gmail.com','123564aambedkar')
    server.sendmail('aakashmundara@gamil.com',to,content)
    server.close()
wishMe()
username()
def sendingWhatsAppmsg(number , message):
    kit.send_msg_instantly(f"+91{number}",message)
   
while True:
    query = take_comand().lower()
    if 'wikipedia' in query:
        speak("searching wikipedia")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        speak("according to wikipedia")
        speak(results)
        print(results)
    elif 'open youtube' in query:
        webbrowser.open('https://www.youtube.com')
    elif 'open stackoverflow ' in query:
        webbrowser.open("www.stackoverflow.com")
    elif 'open google' in query:
        speak("What should i search for you sir")
        cm = take_comand().lower()
        kit.search(cm)
        #webbrowser.open(f"{cm}")
        #webbrowser.open('https://www.google.com')
    elif 'open whatsapp' in query:
        webbrowser.open('https://www.whatsapp.com')
    elif 'play music' in query:
        music_dir = 'D:\\Aakash\\My Songs'
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        print(songs)
        os.startfile(os.path.join(music_dir,rd))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M;%S")
        speak(f"sir, the time is {strTime}")
    elif 'email to aashu' in query:
        try:
            speak("what should i say sir ")
            content = take_comand()
            to = "aakashmundara@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent sir!")
        except Exception as e:
            print(e)
            speak("sory sir ! I am not able to sent your email at this moment")
    elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
    elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
    elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
    elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = take_comand()
            speak("Thanks for naming me")
 
    elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
    elif "who made you" in query or "who created you" in query:
            speak("I have been created by Aakash and Swayam.")
             
    elif 'joke' in query:
            speak(pyjokes.get_joke())
             
    elif "calculate" in query:
             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
    elif "temperature" in query:
        search = "temperature in rohtak"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"current {search} is {temp}")
 
    elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
 
    elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
    elif "why you came to world" in query:
            speak("Thanks to Aakash and Swayam. further It's a secret")
 
    elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
    elif "who are you" in query:
            speak("I am your virtual assistant created by Aakash and Swayam")
 
    elif 'reason for you' in query:
            speak("I was created as a Minor project only ")
 
    elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")
 
      #  elif 'open bluestack' in query:
       #     appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
        #    os.startfile(appli)
 
    elif 'news' in query:
             
        try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
        except Exception as e:
                 
                print(str(e))
 
         
    elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
    elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
    elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
    elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
    elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
    elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
 
    elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
    elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
    elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
    elif "write a note" in query:
            speak("What should i write, sir")
            note = take_comand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = take_comand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime =datetime.datetime.now().strftime("%H:%M;%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
    elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
 
    elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
            with open("Voice.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)
                     
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
    elif "jarvis" in query:
             
            wishMe()
            speak("Jarvis 1 point o in your service Mister")
            speak(assname)
 
             
    elif "send WhatsApp message " in query:
        speak("tell me contact  number sir")
        number = input("enter the number: ")
        speak("what is your msg sir")
        message = take_comand().lower()
        sendingWhatsAppmsg(number , message)
        speak("i have sent the msg sir")
              
 
    elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
 
    elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
 
        # most asked question from google Assistant
    elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
    elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
    elif "i love you" in query:
            speak("It's hard to understand")
 
    elif "what is" in query or "who is" in query:
             
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
 
        # elif "" in query:
            # Command go here
            # For adding more commands

    
