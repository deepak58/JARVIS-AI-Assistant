running_apps = []


def add_app(app_name):
    if app_name not in running_apps:
        running_apps.append(app_name)


def remove_app(app_name):
    if app_name in running_apps:
        running_apps.remove(app_name)


def get_apps():
    return running_apps

def clear_apps():
    running_apps.clear()