import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    
    
except Exception as e:
    print(e)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hr = int(datetime.datetime.now().hour)
    if (hr>=0 and hr<12):
        speak(f"GOOD MORNING SIR")
    elif(hr>=12 and hr<=16):
        speak(f"GOOD AFTERNOON SIR")
    else:
        speak(f"GOOD EVENING SIR")
    speak("THANKS FOR GETTING ME BACK TO WORK , HOW CAN I HELP YOU")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        query = r.listen(source)
    try:
        print("Recognizing...")
        audio = r.recognize_google(query,language="en-in")
        return audio
    except Exception as e:
        print(e)
    return "None"
        


if __name__ == "__main__":
    wishMe()
    command=takeCommand()
    speak(command)
