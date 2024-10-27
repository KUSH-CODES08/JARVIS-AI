#pip install speechrecognition to recognize the  speech
#pip install webbrowser to open the links 
#pip install pyttsx3 to initializ the engine  and to speak the command
#pip install openAI

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI


recognizer=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processcommand(c):
     
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")    
        
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)
        
    # else:
    #     #Let OpenAI handle the problem
    #     output=aiprocess(c)        
    #     speak(output)
    
# def aiprocess(command):
#     client = OpenAI(api_key="your_api_key")


#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud "},
#             {
#                 "role": "user",
#                 "content": command
#             }
#         ]
#     )

#     return completion.choices[0].message 
    
if  __name__ =="__main__":
    speak("Initializing Jarvis... ") 
    while True: 
        #Listen for the waKE WORD "JARVIS"
        # obtain audio from the microphone
        r=sr.Recognizer()
         
        print("Recognizing...")
        #recognize speech using sphinx    
        
    
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word= r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")
                #Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processcommand(command)
        except Exception as e:
        
            print("Error ;{0}".format(e))    
        
        
        