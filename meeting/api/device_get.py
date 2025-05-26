from .base_api import BaseApi

class DeviceGet(BaseApi):
    """设备信息获取API"""
    
    # 类变量-操作字典
    operations = {
        'brightness': {
            'endpoint': 'screen/brightness',
            'name': '屏幕亮度'
        },
        'status': {
            'endpoint': 'screen/status',
            'name': '屏幕状态'
        },
        'voice': {
            'endpoint': 'screen/voice',
            'name': '音量'
        },
        'recording_status': {
            'endpoint': 'screen/voiceRecordStatus',
            'name': '录音状态'
        }
    }
    
    def get_device_info(self, info_type):
        """通用设备信息获取方法"""
        if info_type not in self.operations:
            print(f"不支持的信息类型: {info_type}")
            return None
            
        op = self.operations[info_type]
        success, data = self.send_request('get', op['endpoint'])
        
        if success:
            print(f"当前{op['name']}: {data}")
            return data
        else:
            print(f"获取{op['name']}失败: {data}")
            return None
    
    def get_screen_brightness(self):
        """获取大屏亮度"""
        return self.get_device_info('brightness')
        
    def get_screen_status(self):
        """获取大屏状态"""
        return self.get_device_info('status')
        
    def get_screen_voice(self):
        """获取大屏音量"""
        return self.get_device_info('voice')
        
    def get_recording_status(self):
        """查询录音状态"""
        return self.get_device_info('recording_status')
