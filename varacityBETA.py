import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
import pyjokes
from AppOpener import run
import smtplib
import pyaudio
import ssl
import random
import subprocess
import pywhatkit as pwt
import requests
from bs4 import BeautifulSoup
import addemail
import csv





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

             

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            
        print("Say that again please... or try again")  
        return "None"
    return query

username= ('mehul')

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:  (yaha se queries hogi)
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif  'open youtube' in query:
            webbrowser.open("youtube.com")

       # elif 'open google' in query:
       #     run("Google Chrome")



        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "M:\Microsoft VS Code files\Code.exe"
            
            os.startfile(codePath)

        elif 'dimag kharab' in query:
            speak ("wha  rrra dooo,  wha  rrra dooo, wha  rrra dooo  ")       
        elif 'joke' in query:
            joke1 = pyjokes.get_joke (language='en', category= 'all')
            print (joke1)
            
            speak (joke1)
        
        elif 'hai'  in query:
            speak ("Hi, it's really good to hear from you")

        elif 'sleep' in query:
            speak("thanks....  my  processors..on fire ")
            veracityexefile=('M:\\Veracity_files\\vearcityexe.py') 
            os.startfile(veracityexefile)
            exit()


        elif "introduce yourself"  in query:
            speak (' hii..i am Veracity,    and i can do many task...well you can ask me to play music and stuff .though')
                      
        elif "how are you" in query:
            speak ("I am good,........ well ... still have some glitches")
        elif "homework" in query:
            webbrowser.open('https://mayoor.edunexttechnologies.com/Index')
            speak('seems you have some mood to ..... finally....study....you know')

        

        elif 'send an email' in query or 'send email' in query:
            
            
            smtp_port = 587    # Standard secure SMTP port
            smtp_server = "smtp.gmail.com"  # Google SMTP Server
            sndr= 'testmailmehul@gmail.com'
            simple_email_context = ssl.create_default_context() #python supports to attach files
            
            csv_file='emails.csv'
            speak ('to whome should is send the email ?')
            names = takeCommand()
            def fetch_email_by_name(names, csv_file):
                with open('D:\\Veracity_files\\emails.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['Name'] == names:
                            return row['Email']
                return None

            email_to = fetch_email_by_name(names, csv_file)

            if email_to:
                print (email_to)

            else : 

               speak ('What should I say ?')
               content = takeCommand()
            try:   
                
                    pswd = "bwptdfcskbqmiszt"
                    print("Connecting to server...")
                    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
                    TIE_server.starttls(context=simple_email_context)
                    TIE_server.login('testmailmehul@gmail.com', pswd )
                    print("Connected to server :-)")

                    print()
                    print(f"Sending email to - {names}")
                    TIE_server.sendmail(sndr, email_to , content)
                    speak(f"Email successfully sent to - {names}")
                    print(f"Email successfully sent to - {names}")
            except Exception as e:
                   def get_user_input():
                     name = input("Enter name: ")

                     email = input("Enter email: ")
                     return name, email

                   def write_to_csv(name, email):
                         with open('emails.csv', 'a', newline='') as csvfile:
                            fieldnames = ['Name', 'Email']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write data to CSV file    
                            writer.writerow({'Name': name, 'Email': email})
                   def search_receiver_name(csv_file, receiver_name ):
                      with open(csv_file, 'r') as file:
                         csv_reader = csv.DictReader(file)
                         for row in csv_reader:
                             if row['Name'] == receiver_name:
                                return row['Email']
                      return None
                        
                   speak ("please enter the details ")
                   name, email = get_user_input()
                   csv_file = 'emails.csv'
                   write_to_csv(name, email)
                   speak ("data is saved")
                   print ("saved to csv file (emails.csv)")
                # if nothing in exception then "print (e)" 
                
            finally:
                TIE_server.quit()  

        
        elif  'music'  in query or 'songs' in query or 'hit it' in query:
            
            ms = random.randint(0,3)

            music_dir =  "M:\songs"
            song = os.listdir(music_dir)
            speak("would you ...like...")
            
            os.startfile(os.path.join(music_dir, song[ms]))

            #stopping the music 

        elif 'stop'  in query:
            os.system('taskkill /f /im Music.UI.exe')

        elif 'tired' in query:
            speak('well..... i ..am....a bit sleepy...the battery is draining')
            speak('Am i..pugged in?')

        elif 'spotify' in query:
            os.startfile('Spotify')

        elif 'search youtube' in query or 'search video on youtube' in query or 'youtube search'in query or 'search a video on youtube' in query or 'search video' in query:
            speak('what should i search ? ')
            ytrec= takeCommand()
            pwt.playonyt({'ytrec'})

        elif 'play' in query:
            query=query.replace ('play', '')
            pwt.playonyt(query)

        elif 'what is' in query or 'what the hell is' in query or 'what do you mean by' in query or 'who is' in query or 'who the hell is'in query:
          
          try:
            query = query.replace ('what is ','')
            query = query.replace ('what the hell is ','')
            query = query.replace ('what do you mean by ','')
            query = query.replace ('who is ','')
            query = query.replace('who the hell is', '')
            speak ('This is what i found')

            searching=f'https://www.google.com/search?q={query}'
            pwt.search(query)
            result = wikipedia.summary(query,2)
            speak (result)

          except Exception as e:
            speak ('error while searching ')
        
        elif "where is" in query or 'there is' in query or 'locate'in query:
            query = query.replace("where is", "")
            query = query.replace('there is','' )
            query = query.replace('locate', '' )
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open('https://www.google.com/maps/place/' + location +'')

        elif "what's my name" in query or 'my name' in query:

            speak (f'your name is {username}')


        elif 'private window' in query or 'incognito' in query:
            incog= ('M:\Veracity_files\incognito.lnk')
            os.startfile(incog) 

        
            
            


        



                
                
                



           

            
            
            
                       


           
                     

            

            


            








        
            







            
                

    

            




    
