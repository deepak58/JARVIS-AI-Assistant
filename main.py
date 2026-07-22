from services.voice import speak, listen
from commands.router import execute_command
from wake_word import wait_for_wake_word
from config import WAKE_RESPONSES
import random
import time


def conversation_mode():

    speak(random.choice(WAKE_RESPONSES))

    time.sleep(0.5)
    last_command_time = time.time() 

    while True:

        command = listen()

        print("COMMAND RECEIVED:", repr(command))


        # No voice detected
        if command == "":

            # If inactive for 30 seconds
            if time.time() - last_command_time > 30:

                speak("Okay Deepak. I am going back to sleep. Call me when you need me.")

                return

            continue


        # Update last activity time
        last_command_time = time.time()

        exit_phrases = {
            "bye",
            "goodbye",
            "good bye",
            "stop listening",
            "exit conversation",
            "bye bye",
            "bye-bye"
        }
        if command in exit_phrases:
            speak("Goodbye Deepak.")
            return


        response = execute_command(command)

        print("RESPONSE RECEIVED:", repr(response))

        if response:
            speak(response)

def main():

    speak("Hello Deepak. I am Jarvis. System online.")

    while True:
        wait_for_wake_word()
        time.sleep(0.8)
        conversation_mode()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nJARVIS stopped by user.")

    except Exception as error:
        print("\nUnexpected error:", repr(error))

    finally:
        print("Closing Jarvis.")