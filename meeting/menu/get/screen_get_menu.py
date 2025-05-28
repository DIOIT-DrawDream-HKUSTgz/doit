from menu.menu_base import MenuBase

class ScreenGetMenu(MenuBase):
    """获取屏幕信息菜单"""
    
    def __init__(self, controllers, parent):
        self.controllers = controllers  # 修改为使用控制器管理器
        
        commands = {
            'status': (self.get_status, "获取屏幕状态"),
            'voice': (self.get_voice, "获取屏幕音量"),
            'brightness': (self.get_brightness, "获取屏幕亮度"),
            'voicerecordstatus': (self.get_voice_record_status, "获取屏幕录音状态"),
        }
        
        super().__init__(
            "屏幕信息菜单",
            "输入命令 (status/voice/brightness/voiceRecordStatus/quit/back): ",
            commands,
            parent
        )
        
    def get_status(self):
        """获取屏幕状态"""
        return self.controllers.get_screen_status() 
        
    def get_voice(self):
        """获取屏幕音量"""
        return self.controllers.get_screen_voice() 
    
    def get_brightness(self):
        """获取屏幕亮度"""
        return self.controllers.get_screen_brightness()
    
    def get_voice_record_status(self):
        """获取屏幕录音状态"""
        return self.controllers.get_recording_status()
