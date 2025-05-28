from menu.menu_base import MenuBase
from menu.screen_get_menu import ScreenGetMenu

class GetMenu(MenuBase):
    """获取信息菜单"""
    
    def __init__(self, get_controller, parent):
        self.get_controller = get_controller
        self.screen_menu = None
        
        commands = {
            'screen': (self.handle_screen, "获取屏幕相关信息")
        }
        
        super().__init__("获取菜单", "输入命令 (screen/quit/back): ", commands, parent)
        
        self.screen_menu = ScreenGetMenu(get_controller, self)
        
    def handle_screen(self):
        """处理屏幕信息命令"""
        return self.screen_menu.handle_input()