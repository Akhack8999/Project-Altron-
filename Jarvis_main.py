import datetime
import webbrowser
import pyttsx3
##from pywhatkit.sc import shutdown
import speech_recognition 
import requests 
import bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
###import speedtest-cli###
import speedtest
from playsound import playsound
import time 


#Paste this just below your import files
for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
        
    from INTRO import play_gif
                          play_gif
                         #paste this just below the password

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
    
  def alarm(query):
      timehere = open("Alarmtext.txt","a")
      timehere.write(query)
      timehere.close()
      os.startfile("alarm.py")
 
