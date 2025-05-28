from menu.menu_base import MenuBase

class ScreenGetMenu(MenuBase):
    """获取屏幕信息菜单"""
    
    def __init__(self, controllers, parent):
        self.controllers = controllers  # 修改为使用控制器管理器
        
        commands = {
            # 假设有这些命令
            'status': (self.get_status, "获取屏幕状态"),
            'volume': (self.get_volume, "获取屏幕音量"),
            # 其他命令...
        }
        
        super().__init__(
            "屏幕信息菜单",
            "输入命令 (status/volume/quit/back): ",
            commands,
            parent
        )
        
    def get_status(self):
        """获取屏幕状态"""
        return self.controllers.get_screen_status()  # 使用controllers代替之前的单一控制器
        
    def get_volume(self):
        """获取屏幕音量"""
        return self.controllers.get_screen_volume()  # 使用controllers代替之前的单一控制器
        
    # 其他方法...