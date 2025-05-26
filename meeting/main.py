from api import DeviceGet, DeviceControl
from main_menu import MainMenu

if __name__ == "__main__":
    controller_get = DeviceGet()
    controller = DeviceControl()
    
    cli = MainMenu(controller_get, controller)
    cli.handle_input()
