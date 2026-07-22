from commands.datetime_cmd import handle_datetime
from commands.browser import handle_browser
from commands.apps import handle_apps
from commands.system import handle_system_command
from memory import add_app, get_apps


ACTION_WORDS = {
    "open": "open",
    "launch": "open",
    "start": "open",
    "run": "open",

    "close": "close",
    "exit": "close",
    "quit": "close",
    "terminate": "close"
}


AVAILABLE_APPS = [
    "chrome",
    "calculator",
    "paint",
    "notepad",
    "explorer",
    "youtube",
    "google"
]

def parse_app_commands(command):
    """
    Converts a sentence into action/application pairs.

    Example:
    "open notepad close paint and calculator"

    Returns:
    [
        ("open", "notepad"),
        ("close", "paint"),
        ("close", "calculator")
    ]
    """

    command = command.lower().strip()

    # Remove punctuation and joining words
    command = command.replace(",", " ")
    command = command.replace(" and then ", " ")
    command = command.replace(" then ", " ")
    command = command.replace(" and ", " ")

    words = command.split()

    parsed_commands = []
    current_action = None

    for word in words:

        # Update the active action
        if word in ACTION_WORDS:
            current_action = ACTION_WORDS[word]
            continue

        # Check whether the word is an application name
        if word in AVAILABLE_APPS:
            action = current_action or "open"
            parsed_commands.append((action, word))

    return parsed_commands


def execute_app_commands(command):
    parsed_commands = parse_app_commands(command)

    print("Parsed commands:", parsed_commands)

    responses = []

    for action, app in parsed_commands:
        print("Processing:", action, app)

        # Browser commands such as YouTube and Google
        browser_response = handle_browser(
            command,
            action,
            app
        )

        if browser_response:
            add_app("chrome")
            responses.append(browser_response)
            continue

        # Normal desktop applications
        app_response = handle_apps(
            command,
            action,
            app
        )

        if app_response:
            responses.append(app_response)

    if responses:
        return ". ".join(responses)

    return None


def execute_command(command):
    command = command.lower().strip()

    print("Full command:", command)

    # ---------- Wake Response ----------
    if command in [
        "jarvis",
        "hey jarvis",
        "hi jarvis"
    ]:
        return "Yes Deepak?"

    # ---------- What Is Open ----------
    if "what is open" in command:
        running_apps = get_apps()

        if running_apps:
            return "Currently open: " + ", ".join(running_apps)

        return "No applications are recorded as open."


    # ---------- Date and Time ----------
    datetime_response = handle_datetime(command)

    if datetime_response:
        return datetime_response

    system_response = handle_system_command(command)

    if system_response:
        return system_response

    # ---------- Application Commands ----------
    app_response = execute_app_commands(command)

    if app_response:
        return app_response

    return "Sorry, I could not understand that command."