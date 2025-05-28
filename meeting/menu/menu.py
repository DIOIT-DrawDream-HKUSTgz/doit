from menu.menu_base import MenuBase
from menu.get.screen_get_menu import ScreenGetMenu
from menu.get.other_get_menu import OtherGetMenu

class GetMenu(MenuBase):
    """获取信息菜单"""
    
    def __init__(self, controllers, parent):
        self.controllers = controllers 
        self.screen_menu = None
        self.other_menu = None
        
        commands = {
            'screen': (self.handle_screen, "获取屏幕相关信息"),
            'other' : (self.handle_other, "获取房间相关信息"),
        }
        
        super().__init__("获取菜单", "输入命令 (screen/other/quit/back): ", commands, parent)
        
        self.screen_menu = ScreenGetMenu(controllers, self)
        self.other_menu = OtherGetMenu(controllers, self)
        
    def handle_screen(self):
        """处理屏幕信息命令"""
        return self.screen_menu.handle_input()
    def handle_other(self):
        """处理房间信息命令"""
        return self.other_menu.handle_input()
