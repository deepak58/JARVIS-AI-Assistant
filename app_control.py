import subprocess


def close_application(app_name):

    apps = {
        "calculator": "CalculatorApp.exe",
        "chrome": "chrome.exe",
        "paint": "mspaint.exe",
        "notepad": "notepad.exe"
    }

    if app_name in apps:
        subprocess.run(
            f"taskkill /f /im {apps[app_name]}",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return f"Closing {app_name}"

    return "I cannot find that application"


def close_all():

    apps = [
        "chrome.exe",
        "CalculatorApp.exe",
        "mspaint.exe",
        "notepad.exe"
    ]

    for app in apps:
        subprocess.run(
            f"taskkill /f /im {app}",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    return "Closing all applications"

def shutdown_pc():

    return "Shutdown command received. Confirmation required."