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
 

  if __name__ == "__main__":
      while True:
          query = takeCommand().lower()
          if "wake up" in query:
              from GreetMe import greetMe
              greetMe()
  
              while True:
                  query = takeCommand().lower()
                  if "go to sleep" in query:
                      speak("Ok sir , You can call me anytime")
                      break 
                    
                  # Jarvis: version 2.0
                  
                    elif "change password" in query:
                      speak("What's the   new password")
                      new_pw = input("Enter the new password\n")
                      new_password = open("password.txt","w")
                      new_password.write(new_pw)
                      new_password.close()
                      speak("Done sir")
                      speak(f"Your new password is{new_pw}")
                    
                    elif "schedule my day" in query:
                        tasks = [] #Empty list 
                        speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        query = takeCommand().lower()
                        if "yes" in query:
                            file = open("tasks.txt","w")
                            file.write(f"")
                            file.close()
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            i = 0
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                        elif "no" in query:
                            i = 0
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                 elif "show my schedule" in query:
                     file = open("tasks.txt","r")
                     content = file.read()
                     file.close()
                     mixer.init()
                     mixer.music.load("notification.mp3")
                     mixer.music.play()
                     notification.notify(
                         title = "My schedule :-",
                         message = content,
                         timeout = 15
                         )
                         
                  elif "focus mode" in query:
                                      a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                                      if (a==1):
                                          speak("Entering the focus mode....")
                                          os.startfile("D:\\Coding\\Youtube\\Jarvis\\FocusMode.py")
                                          exit()
                  
                                      
                                      else:
                                          pass       
                   
                  elif "show my focus" in query:
                                      from FocusGraph import focus_graph
                                      focus_graph()    
                                      
                                      
                                      
                  elif "translate" in query:
                                      from Translator import translategl
                                      query = query.replace("jarvis","")
                                      query = query.replace("translate","")
                                      translategl(query)
                         
                         
  ##############################################

