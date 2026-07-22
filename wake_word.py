import speech_recognition as sr

from config import WAKE_WORDS


def wait_for_wake_word():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8

    while True:
        try:
            with sr.Microphone() as source:
                print("Waiting for Jarvis...")

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                try:
                    audio = recognizer.listen(
                        source,
                        timeout=3,
                        phrase_time_limit=5
                    )

                except sr.WaitTimeoutError:
                    continue

            try:
                text = recognizer.recognize_google(
                    audio,
                    language="en-IN"
                ).lower().strip()

                print("Wake check:", text)

                if any(wake_word in text for wake_word in WAKE_WORDS):
                    return True

            except sr.UnknownValueError:
                continue

            except sr.RequestError as error:
                print("Wake-word service error:", repr(error))

        except KeyboardInterrupt:
            raise

        except Exception as error:
            print("Wake-word error:", repr(error))