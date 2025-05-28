from api.device_control import DeviceControl
from api.other_device_control import OtherDeviceControl
from api.device_get import DeviceGet
from controllers_manager import ControllersManager
from main_menu import MainMenu

def main():
    # 创建控制器管理器
    controllers = ControllersManager()
    
    # 注册各个控制器
    controllers.register_controller("get", DeviceGet())
    controllers.register_controller("control", DeviceControl())
    controllers.register_controller("other_control", OtherDeviceControl())
    
    # 创建主菜单并传入控制器管理器
    cli = MainMenu(controllers)
    cli.handle_input()

if __name__ == "__main__":
    main()
