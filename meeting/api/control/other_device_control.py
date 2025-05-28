from ..api_base import BaseApi
import requests

class OtherDeviceControl(BaseApi):
    """其他设备控制API"""
    
    def __init__(self, user="123"):
        super().__init__()
        self.base_api_url = f"http://10.30.35.115:8090/api/v2/gateway"

    def control_screen_voice_record_status(self, status):
        """录音控制
        参数: status - 'start' 或 'stop' 或 'pause' 或 'resume'
        """
        if status not in ['start', 'stop', 'pause', 'resume']:
            print("无效的状态参数，请使用 'start' 或 'stop' 或 'pause' 或 'resume'")
            return False

        api_url = f"{self.base_api_url}/iot/voiceRecordControl"
        params = {
            "status": status
        }
        try:
            response = requests.get(api_url, params=params)
            print(f"录音控制响应: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                if data.get("isSuccess"):
                    print(f"录音控制成功: {status}")
                    return True
                else:
                    # print(data.get("code"))
                    if data.get("code") == -1:
                        print(f"当前无会议") 
                        return True  
                    else:
                        print(f"录音控制失败: {data.get('msg')}")
            return False
        except Exception as e:
            print(f"录音控制出错: {e}")
            return False
