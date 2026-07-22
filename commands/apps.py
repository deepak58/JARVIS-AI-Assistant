from app_control import open_application, close_application
from memory import add_app, remove_app


def handle_apps(command, action, app):
    if not app:
        return None

    if app in ["youtube", "google"]:
        return None

    if action == "open":
        response = open_application(app)

        if response:
            add_app(app)

        return response

    if action == "close":
        response = close_application(app)
        remove_app(app)
        return response

    return None