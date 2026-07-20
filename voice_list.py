import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for index, voice in enumerate(voices):
    print(f"Voice {index}")
    print("Name:", voice.name)
    print("ID:", voice.id)
    print("-" * 50)