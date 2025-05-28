from api.control.device_control import DeviceControl
from api.control.other_device_control import OtherDeviceControl
from api.get.device_get import DeviceGet
from api.get.other_get import OtherGet
from controllers_manager import ControllersManager
from main_menu import MainMenu

def main():
    # 创建控制器管理器
    controllers = ControllersManager()
    
    controllers.register_controller("get", DeviceGet())
    controllers.register_controller("room_get", OtherGet())
    controllers.register_controller("control", DeviceControl())
    controllers.register_controller("other_control", OtherDeviceControl())

    cli = MainMenu(controllers)
    cli.handle_input()

if __name__ == "__main__":
    main()
