from menu.menu_base import MenuBase

class ControlMenu(MenuBase):
    """控制设备菜单"""
    
    def __init__(self, controllers, parent):
        self.controllers = controllers  # 修改为使用控制器管理器
        
        commands = {
            'screen': (self.control_screen, "控制屏幕电源"),
            'screenvolume': (self.control_volume, "控制屏幕音量"),
            'screenvoice': (self.control_voice, "控制屏幕声音"),
            'screenbrightness': (self.control_brightness, "控制屏幕亮度"),
            'screenvoicerecord': (self.control_voice_record, "控制屏幕录音")
        }
        
        super().__init__(
            "控制菜单", 
            "输入命令 (screen/screenVolume/screenVoice/screenBrightness/screenVoiceRecord/quit/back): ", 
            commands, 
            parent
        )
        
        # 参数选项
        self.switch_options = ['open', 'close']
        
    def control_screen(self):
        """控制屏幕电源"""
        self._setup_param_completer(self.switch_options)
        param = input("输入参数 (open/close): ").strip().lower()
        self.setup_completer()  # 恢复命令补全
        return self.controllers.control_screen_power(param)
        
    def control_volume(self):
        """控制屏幕音量"""
        param = input("输入音量值 (0-100): ").strip()
        return self.controllers.control_screen_volume(param)
        
    def control_voice(self):
        """控制屏幕声音"""
        self._setup_param_completer(self.switch_options)
        param = input("输入参数 (open/close): ").strip().lower()
        self.setup_completer()  # 恢复命令补全
        return self.controllers.control_screen_voice(param)
        
    def control_brightness(self):
        """控制屏幕亮度"""
        param = input("输入亮度值 (0-100): ").strip()
        return self.controllers.control_screen_brightness(param)
        
    def control_voice_record(self):
        """控制屏幕录音"""
        voice_record_options = ['start', 'stop', 'pause', 'resume']
        self._setup_param_completer(voice_record_options)
        param = input("输入参数 (start/stop/pause/resume): ").strip().lower()
        self.setup_completer()  # 恢复命令补全
        return self.controllers.control_screen_voice_record_status(param)
