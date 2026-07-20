import speech_recognition as sr


def wait_for_wake_word():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Waiting for Jarvis...")

        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source)

                text = recognizer.recognize_google(
                    audio,
                    language="en-IN"
                )

                text = text.lower()

                print("Heard:", text)

                if "jarvis" in text:
                    return True

            except:
                pass