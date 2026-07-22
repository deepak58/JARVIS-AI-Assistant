import gc
import time

import pyttsx3
import speech_recognition as sr

from config import LISTEN_TIMEOUT, VOICE_RATE


def speak(text):
    if text is None:
        return

    text = str(text).strip()

    if not text:
        return

    print("JARVIS:", text)

    engine = None

    try:
        engine = pyttsx3.init("sapi5")

        engine.setProperty("rate", VOICE_RATE)
        engine.setProperty("volume", 1.0)

        voices = engine.getProperty("voices")

        if voices:
            engine.setProperty("voice", voices[0].id)

        engine.say(text)
        engine.runAndWait()

    except Exception as error:
        print("TTS Error:", repr(error))

    finally:
        if engine is not None:
            try:
                engine.stop()
            except Exception:
                pass

        del engine
        gc.collect()
        time.sleep(0.2)


def listen():
    recognizer = sr.Recognizer()

    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8

    try:
        with sr.Microphone() as source:
            print("Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:
                audio = recognizer.listen(
                    source,
                    timeout=LISTEN_TIMEOUT,
                    phrase_time_limit=10
                )

            except sr.WaitTimeoutError:
                return ""

    except KeyboardInterrupt:
        raise

    except Exception as error:
        print("Microphone Error:", repr(error))
        return ""

    try:
        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        command = command.lower().strip()

        print("You said:", command)

        return command

    except sr.UnknownValueError:
        print("Voice not understood.")
        return ""

    except sr.RequestError as error:
        print("Google recognition error:", repr(error))
        return ""

    except KeyboardInterrupt:
        raise

    except Exception as error:
        print("Voice error:", repr(error))
        return ""