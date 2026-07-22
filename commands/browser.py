import os
import subprocess


CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def handle_browser(command, action, app):
    if action != "open":
        return None

    if app == "youtube":
        subprocess.Popen([CHROME_PATH, "https://www.youtube.com"])
        return "Opening YouTube"

    if app == "google":
        subprocess.Popen([CHROME_PATH, "https://www.google.com"])
        return "Opening Google"

    return None