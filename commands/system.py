import subprocess

from app_control import close_all, shutdown_pc


def contains_any(command, phrases):
    return any(phrase in command for phrase in phrases)

def handle_system_command(command):
    command = command.lower().strip()

    # ---------- Wake Response ----------

    if any(phrase in command for phrase in [
         "wake up",
         "jarvis wake up",
         "wake up jarvis",
         "are you awake"
    ]):
        return "I'm awake, Deepak."

    # ---------- Close Everything ----------
    if contains_any(command, [
        "close everything",
        "close all applications",
        "close all apps",
        "close every application"
    ]):
        return close_all()

    # ---------- Lock ----------
    if contains_any(command, [
        "lock computer",
        "lock my computer",
        "lock the computer",
        "lock pc",
        "lock my pc",
        "lock the pc",
        "lock system",
        "lock my system"
    ]):
        subprocess.run(
            ["rundll32.exe", "user32.dll,LockWorkStation"],
            check=False
        )

        return "Locking your computer."

    # ---------- Sleep ----------
    if contains_any(command, [
        "sleep computer",
        "sleep my computer",
        "put computer to sleep",
        "put my computer to sleep",
        "sleep pc",
        "sleep my pc",
        "put pc to sleep",
        "put my pc to sleep"
    ]):
        subprocess.Popen(
      [
        "powershell",
        "-Command",
        "Start-Sleep -Seconds 2; "
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
      ],
      stdout=subprocess.DEVNULL,
      stderr=subprocess.DEVNULL
       )

        return "Putting your computer to sleep."

    # ---------- Restart ----------
    if contains_any(command, [
        "restart computer",
        "restart my computer",
        "restart the computer",
        "restart pc",
        "restart my pc",
        "restart the pc",
        "reboot computer",
        "reboot my computer",
        "reboot pc"
    ]):
        return "Restart command received. Confirmation required."

    # ---------- Shutdown ----------
    if contains_any(command, [
        "shutdown computer",
        "shutdown my computer",
        "shutdown the computer",
        "shut down computer",
        "shut down my computer",
        "shut down the computer",
        "shutdown pc",
        "shutdown my pc",
        "shut down pc",
        "shut down my pc",
        "turn off computer",
        "turn off my computer",
        "turn off pc"
    ]):
        return shutdown_pc()

    return None