import speech_recognition as sr


def wait_for_wake_word():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Waiting for Jarvis...")

        recognizer.adjust_for_ambient_noise(source)

        while True:

            try:
                audio = recognizer.listen(
                    source,
                    timeout=8,
                    phrase_time_limit=5
                )

                text = recognizer.recognize_google(
                    audio,
                    language="en-IN"
                )

                text = text.lower()

                print("Wake check:", text)

                if "jarvis" in text:
                    return True

            except:
                pass