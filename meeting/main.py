from api import MeetingDeviceGet, MeetingDeviceControl
from main_menu import MainMenu

if __name__ == "__main__":
    controller_get = MeetingDeviceGet()
    controller = MeetingDeviceControl()
    
    cli = MainMenu(controller_get, controller)
    cli.handle_input()
