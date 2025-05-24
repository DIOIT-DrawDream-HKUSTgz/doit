from menu.menu_base import MenuBase

class ScreenGetMenu(MenuBase):
    """屏幕信息获取菜单"""
    
    def __init__(self, get_controller, parent):
        self.get_controller = get_controller
        
        commands = {
            'brightness': (self.get_brightness, "获取屏幕亮度"),
            'status': (self.get_status, "获取屏幕状态"),
            'voice': (self.get_voice, "获取屏幕声音"),
            'voicerecordstatus': (self.get_voice_record_status, "获取录音状态")
        }
        
        super().__init__(
            "屏幕菜单", 
            "输入命令 (brightness/status/voice/voiceRecordStatus/quit/back): ", 
            commands, 
            parent
        )
        
    def get_brightness(self):
        """获取屏幕亮度"""
        self.get_controller.get_screen_brightness()
        
    def get_status(self):
        """获取屏幕状态"""
        self.get_controller.get_screen_status()
        
    def get_voice(self):
        """获取屏幕声音"""
        self.get_controller.get_screen_voice()
        
    def get_voice_record_status(self):
        """获取录音状态"""
        self.get_controller.get_recording_status()