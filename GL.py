"""
# pip install pyttsx3
# pip install speechRecognition
# pip install wikipedia
"""
"""
# pyttsx3 = python text to speech
# speech_recognition = used to convert spoken words into text and work on API's
# automate_wikipedia = used to automate and work with the wikipedia
# webbrowser = used for to automate webbrowsers
# smtplib - sending emails
# os = used to work/interact with operating system
# datetime = used to work with the date and time
"""


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
# import pyaudio
# from distutils.version import LooseVersion

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) # 1 means a female voice, 0 is for male voice

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    """
    12: 00 - noon
    1:00 - morning / 13:00 - afternoon (military time)
    """
    if hour >=0 and hour<=12:
        speak("Good Morning my dear friend")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon my dear friend")
    else:
        speak("Good evening my dear friend")
    speak("Let me know how can I help you, What are you looking for ?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening to you Hans ......")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing your voice ....")
            query = r.recognize_google(audio,language='en-us')
            print(f"My dear friend you said : {query}\n")

        except Exception as e:
            print("Hans say that again please ......")
            return "None"
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hans.radam10@gmail.com', 'EMOME12300.')
    server.sendmail('hans.radam10@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand().lower()

        if 'open wikipedia' in query:
            speak('Searching wikipedia .... ')
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open paint' in query:
            npath = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(npath)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open great learning academy' in query:
            webbrowser.open('https://www.mygreatlearning.com//academy')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'tell me the type' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"My dear friend, the time is{strTime}")

        elif 'open great learning youtube channel' in query:
            webbrowser.open('https://www.youtube.com/c/GreatLearningOfficial')

        elif 'open linkedIn' in query:
            webbrowser.open("www.linkedin.com")

        elif 'email to other friend' in query:
            try:
                speak("What should I send ?")
                content = takecommand()
                to= "hans.radam10@gmail.com"
                sendEmail(to, content)
                speak("Your email has been sent successfully")

            except Exception as e:
                print(e)
                speak("My dear friend .. I am unable to send the email ...."
                      "Please address me the errors")












