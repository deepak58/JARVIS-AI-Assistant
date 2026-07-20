import os
import webbrowser
import datetime
import subprocess


def execute_command(command):

    # ---------- Chrome ----------
    if "open chrome" in command:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        return "Opening Chrome"

    # ---------- YouTube ----------
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    # ---------- Google ----------
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    # ---------- Calculator ----------
    elif "open calculator" in command:
        subprocess.Popen("calc.exe")
        return "Opening Calculator"

    # ---------- Notepad ----------
    elif "open notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"

    # ---------- Paint ----------
    elif "open paint" in command:
        subprocess.Popen("mspaint.exe")
        return "Opening Paint"

    # ---------- File Explorer ----------
    elif "open explorer" in command:
        subprocess.Popen("explorer.exe")
        return "Opening File Explorer"

    # ---------- Time ----------
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"

    # ---------- Date ----------
    elif "date" in command or "today" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today is {today}"

    else:
        return "Sorry, can't here you properly. could you please speak loudly?"