import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("JARVIS is listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)

except Exception:
    print("Sorry, I did not understand.")