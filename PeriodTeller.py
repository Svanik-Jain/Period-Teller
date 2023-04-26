import pyttsx3
from datetime import datetime
import signal

SayTimes = ["7:30:00","8:10:00","8:45:00","9:05:00","9:40:00","10:15:00","10:50:00","11:25:00","12:00:00","12:35:00","13:10:00","13:45:00","14:20:00"]
TextToSpeech = pyttsx3.init()
period = 0
stop = False

def stopTheCode(signal,frame):
    global stop
    stop = True

signal.signal(signal.SIGINT, stopTheCode)

stop = False

while True:
    TimeNow = datetime.now()
    CurrentTime = TimeNow.strftime("%H:%M:%S")
    period = 0
    for timeI in SayTimes:
        period += 1
        if(timeI == "8:45:00"or timeI == "11:25:00"):
            period -=1
        if(CurrentTime == "8:45:00" or CurrentTime == "11:25:00"):
            TextToSpeech.say(f"The time is {CurrentTime} and the break has started.")
            TextToSpeech.runAndWait()
            break
        elif(CurrentTime == "14:20"):
            TextToSpeech.say(f"The time is {CurrentTime} and the school is over.")
            TextToSpeech.runAndWait()
            break
        elif(CurrentTime==timeI):
            TextToSpeech.say(f"The time is {CurrentTime} and the period number is {period}.")
            TextToSpeech.runAndWait()
            break
    if(stop):
        break
