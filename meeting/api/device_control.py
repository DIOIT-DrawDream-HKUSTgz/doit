from .base_api import BaseApi
import requests

class DeviceControl(BaseApi):
    """设备控制API"""
    
    def __init__(self, user="123"):
        super().__init__()
        self.base_api_url = f"http://10.30.35.115:8090/api/v2/gateway/iot"

    def control_device(self, action, param):
        """通用设备控制方法"""
        api_url = f"{self.base_api_url}/control"
        params = {
            "action": action,
            "param": param
        }
        try:
            response = requests.get(api_url, params=params)
            print(f"控制请求响应: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                if data["isSuccess"]:
                    print(f"设备控制成功: {action}={param}")
                    return True
                else:
                    print(f"设备控制失败: {data['msg']}")
            return False
        except Exception as e:
            print(f"设备控制出错: {e}")
            return False

    def control_screen_power(self, status):
        """控制大屏开关
        参数: status - 'open' 或 'close'
        """
        if status not in ['open', 'close']:
            print("无效的状态参数，请使用 'open' 或 'close'")
            return False
        return self.control_device("screen", status)

    def control_screen_volume(self, volume):
        """控制大屏音量
        参数: volume - 音量值，范围0-100
        """
        try:
            volume = int(volume)
            if not (0 <= volume <= 100):
                print("音量需要在0-100范围内")
                return False
        except ValueError:
            print("音量必须是整数")
            return False
        return self.control_device("screenVolume", str(volume))

    def control_screen_voice(self, status):
        """控制大屏声音开关
        参数: status - 'open' 或 'close'
        """
        if status not in ['open', 'close']:
            print("无效的状态参数，请使用 'open' 或 'close'")
            return False
        return self.control_device("screenVoice", status)
    
    def control_screen_brightness(self, brightness):
        """控制大屏亮度
        参数: brightness - 亮度值，范围0-100
        """
        try:
            brightness = int(brightness)
            if not (0 <= brightness <= 100):
                print("亮度需要在0-100范围内")
                return False
        except ValueError:
            print("亮度必须是整数")
            return False
        return self.control_device("screenBrightness", str(brightness))
    
    def control_screen_voice_record(self, status):
        """控制大屏录音开关
        参数: status - 'open' 或 'close'
        """
        if status not in ['open', 'close']:
            print("无效的状态参数，请使用 'open' 或 'close'")
            return False
        return self.control_device("screenVoiceRecord", status)
