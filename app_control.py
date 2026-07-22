import subprocess
import os
from memory import clear_apps


apps = {

    "chrome": {
        "open": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "process": "chrome.exe"
    },

    "calculator": {
        "open": "calc.exe",
        "process": "CalculatorApp.exe"
    },

    "paint": {
        "open": "mspaint.exe",
        "process": "mspaint.exe"
    },

    "notepad": {
        "open": "notepad.exe",
        "process": "notepad.exe"
    },

    "explorer": {
        "open": "explorer.exe",
        "process": "explorer.exe"
    }

}



def open_application(app_name):

    if app_name in apps:

        path = apps[app_name]["open"]

        if app_name == "chrome":

            os.startfile(path)

        else:

            subprocess.Popen(path)


        return f"Opening {app_name}"


    return "I cannot find that application"




def close_file_explorer():

    script = """
    $shell = New-Object -ComObject Shell.Application
    $shell.Windows() | ForEach-Object {
        if ($_.FullName -like "*explorer.exe*") {
            $_.Quit()
        }
    }
    """

    subprocess.run(
        ["powershell", "-Command", script],
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


    return "Closing File Explorer"




def close_application(app_name):

    if app_name == "explorer":

        return close_file_explorer()


    if app_name in apps:

        process = apps[app_name]["process"]

        subprocess.run(
            f"taskkill /f /im {process}",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


        return f"Closing {app_name}"


    return "I cannot find that application"




def close_all():

    for app in apps:

        if app != "explorer":

            process = apps[app]["process"]

            subprocess.run(
                f"taskkill /f /im {process}",
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

    clear_apps()
    return "Closing all applications"




def shutdown_pc():

    return "Shutdown command received. Confirmation required."