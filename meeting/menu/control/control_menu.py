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
            'screenvoicerecord': (self.control_voice_record, "控制屏幕录音"),
            'endmeeting': (self.end_meeting, "结束会议"),
            'closehotcode': (self.close_hot_code, "关闭热码投屏"),
            'endcloudtxmeeting': (self.end_cloud_tx_meeting, "结束腾讯云会议"),
            'invitecloudtxmeeting': (self.invite_cloud_tx_meeting, "邀请加入腾讯云会议"),
            'joincloudtxmeeting': (self.join_cloud_tx_meeting, "加入腾讯云会议"),
            'querymeetinglist': (self.query_meeting_list, "查询会议列表"),
            'quickmeeting': (self.quick_meeting, "快速会议"),
            'desktophotkey': (self.desk_top_hot_key, "热码投屏"),
            'sharedesk': (self.share_desk, "共享桌面"),
            'closesharedesk': (self.close_share_desk, "关闭共享桌面"),
            'startmeeting': (self.start_meeting, "开始会议"),
            'startbyid': (self.start_meeting_by_id, "通过ID启动会议"),
            'startcloudmeeting': (self.start_cloud_meeting, "开始腾讯云会议"),
            'switchmute': (self.switch_mute, "会议开始中点击麦克风修改状态"),
            'switchvideo': (self.switch_video, "会议开始中点击摄像头修改状态"),
        }
        
        super().__init__(
            "控制菜单", 
            "输入命令 (screen/screenVolume/screenVoice/screenBrightness/screenVoiceRecord/endMeeting/closeHotCode/ \n          endCloudTXMeeting/inviteCloudTXMeeting/joinCloudTXMeeting/queryMeetingList/quickmeeting/deskTopHotKey/ \n          shareDesk/closeShareDesk/startMeeting/startById/startCloudMeeting/switchMute/switchVideo/quit/back):", 
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
    
    def end_meeting(self):
        """结束会议"""
        return self.controllers.end_meeting()
    
    def close_hot_code(self):
        """关闭热码投屏"""
        return self.controllers.close_hot_code()
    
    def end_cloud_tx_meeting(self):
        """结束腾讯云会议"""
        return self.controllers.end_cloud_tx_meeting()
    
    def invite_cloud_tx_meeting(self):
        """邀请腾讯云会议"""
        try:
            user_names = input("请输入被邀请人姓名(多个用逗号分隔): ").strip()
            if not user_names:
                print("用户名不能为空")
                return False
            return self.controllers.invite_cloud_tx_meeting(user_names)
        except Exception as e:
            print(f"邀请失败: {e}")
            return False
        
    def join_cloud_tx_meeting(self):
        """加入腾讯云会议"""
        try:
            meetingCode = input("请输入要加入会议名称: ").strip()
            if not meetingCode:
                print("会议号不能为空")
                return False
            password = input("请输入会议密码: ").strip()
            if not password:
                print("会议密码不能为空")
                return False
            return self.controllers.join_cloud_tx_meeting(meetingCode, password)
        except Exception as e:
            print(f"加入会议失败: {e}")
            return False
        
    def query_meeting_list(self):
        """查询会议列表"""
        return self.controllers.query_meeting_list()
    
    def quick_meeting(self):
        """快速会议"""
        return self.controllers.quick_meeting()
    
    def desk_top_hot_key(self):
        """热码投屏"""
        return self.controllers.desk_top_hot_key()
    
    def share_desk(self):
        """共享桌面"""
        return self.controllers.share_desk()
    
    def close_share_desk(self):
        """关闭共享桌面"""
        return self.controllers.close_share_desk()
    
    def start_meeting(self):
        """开始会议"""
        return self.controllers.start_meeting()
    
    def start_meeting_by_id(self):
        """通过ID启动会议"""
        try:
            meeting_id = input("请输入会议ID: ").strip()
            if not meeting_id:
                print("会议ID不能为空")
                return False
            return self.controllers.start_meeting_by_id(meeting_id)
        except Exception as e:
            print(f"启动会议失败: {e}")
            return False
        
    def start_cloud_meeting(self):
        """开始腾讯云会议"""
        return self.controllers.start_cloud_meeting()
    
    def switch_mute(self):
        """会议开始中点击麦克风修改状态"""
        return self.controllers.switch_mute()
    
    def switch_video(self):
        """会议开始中点击摄像头修改状态"""
        return self.controllers.switch_video()