import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 150)

engine.say("Hello Deepak. I am Jarvis. My system is online.")

engine.runAndWait()