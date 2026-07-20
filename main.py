import speech_recognition as sr
import pyttsx3
from commands import execute_command
from wake_word import wait_for_wake_word

def speak(text):
    print("JARVIS:", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 155)

    engine.say(text)
    engine.runAndWait()

    engine.stop()

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=8)

        except sr.WaitTimeoutError:
            speak("Deepak, are you there?")

            try:
                audio = recognizer.listen(source, timeout=5)

            except sr.WaitTimeoutError:
                speak("Okay Deepak, I think you are busy with something else now. I am going offline. Call me when you need.")
                return "shutdown"

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", command)
        return command.lower()

    except:
        return ""


speak("Hello Deepak. I am Jarvis. System online.")

while True:

    wait_for_wake_word()

    speak("Yes Deepak?")

    command = listen()
    print("CHECK:", command) #we can delete this later
    if command == "shutdown":
       break
    elif any(phrase in command for phrase in ["biogas","goodbye","good bye","bye jarvis","jarvis stop","jarvis exit","stop","exit","buy jarvis","buy jar","goodbye"]):
         speak("Goodbye Deepak.")
         break

    else:
        response = execute_command(command)
        speak(response)