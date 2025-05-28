from menu.menu_base import MenuBase

class OtherGetMenu(MenuBase):
    """获取其他设备信息菜单"""
    
    def __init__(self, controllers, parent):
        self.controllers = controllers  # 修改为使用控制器管理器
        
        commands = {
            "roomstatus": (self.get_room_status, "获取房间状态"),
            "isjoinavailable": (self.is_join_available, "判断当前是否允许加入云会议"),
            "querymeetinglist": (self.query_meeting_list, "查询会议列表"),
            "querydesktopstatus": (self.query_desktop_status, "查询桌面状态"),
        }
        
        super().__init__(
            "屏幕信息菜单",
            "输入命令 (roomStatus/isJoinAvailable/queryMeetingList/queryDesktopStatus/quit/back): ",
            commands,
            parent
        )
    
    def get_room_status(self):
        """获取房间状态"""
        return self.controllers.get_room_status()
    
    def is_join_available(self):
        """判断当前是否允许加入云会议"""
        return self.controllers.is_join_available()
    
    def query_meeting_list(self):
        """查询会议列表"""
        return self.controllers.query_meeting_list()
    
    def query_desktop_status(self):
        """查询桌面状态"""
        return self.controllers.query_desktop_status()