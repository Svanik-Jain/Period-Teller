import pyttsx3
from datetime import datetime

TimeNow = datetime.now()
SayTimes = ["7:30","8:10","8:45","9:05","9:40","10:15","10:50","11:25","12:00","12:35","13:10","13:45","14:20"]
TextToSpeech = pyttsx3.init()
period = 0
CurrentTime = TimeNow.strftime("%H:%M")

for timeI in SayTimes:
    period += 1
    if(timeI == "8:45"or timeI == "11:25"):
        period -=1
    if(CurrentTime == "8:45" or CurrentTime == "11:25"):
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
    
