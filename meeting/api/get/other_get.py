from ..api_base import BaseApi

class OtherGet(BaseApi):
    """获取其他设备信息API"""
    
    operations = {
        'roomstatus': {
            'endpoint': 'meeting/room/roomStatus',
            'name': '房间状态'
        },
        'isjoinavailable': {
            'endpoint': 'meeting/join/available',
            'name': '判断当前是否允许加入云会议'
        },
        'querymeetinglist': {
            'endpoint': 'meeting/list',
            'name': '查询会议列表'
        },
        'querydesktopstatus': {
            'endpoint': 'meeting/screen/meetingShare/status',
            'name': '查询桌面状态'
        }
    }

    def get_other_info(self, info_type):
        """通用其他设备信息获取方法"""
        if info_type not in self.operations:
            print(f"不支持的信息类型: {info_type}")
            return None
            
        op = self.operations[info_type]
        # print(f'api: {op["endpoint"]}')
        success, data = self.send_request('get', op['endpoint'])
        
        if success:
            print(f"当前{op['name']}: {data}")
            return data
        else:
            print(f"获取{op['name']}失败: {data}")
            return None
        
    def get_room_status(self):
        """获取房间状态"""
        return self.get_other_info('roomstatus')
    
    def is_join_available(self):
        """判断当前是否允许加入云会议"""
        return self.get_other_info('isjoinavailable')
    
    def query_meeting_list(self):
        """查询会议列表"""
        return self.get_other_info('querymeetinglist')
    
    def query_desktop_status(self):
        """查询桌面状态"""
        return self.get_other_info('querydesktopstatus')