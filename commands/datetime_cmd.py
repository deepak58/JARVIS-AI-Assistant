import datetime


def handle_datetime(command):
    command = command.lower()

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"

    if "date" in command or "today" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today is {today}"

    return None