import json
import requests
import time
class MeetingDeviceGet:
    def __init__(self, user_id="123"):
        self.base_api_url = f"http://10.30.35.115:8090/api/v2/gateway/iot"

    def get_screen_brightness(self):
        """获取大屏亮度"""
        api_url = f"{self.base_api_url}/screen/brightness"
        try:
            response = requests.get(api_url)
            print(f"获取亮度响应: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                if data["isSuccess"]:
                    brightness = data["data"]
                    print(f"当前屏幕亮度: {brightness}")
                    return brightness
                else:
                    print(f"获取亮度失败: {data['msg']}")
            return None
        except Exception as e:
            print(f"获取屏幕亮度出错: {e}")
            return None

    def get_screen_status(self):
        """获取大屏状态"""
        api_url = f"{self.base_api_url}/screen/status"
        try:
            response = requests.get(api_url)
            print(f"获取屏幕状态响应: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                if data["isSuccess"]:
                    status = data["data"]
                    print(f"当前屏幕状态: {status}")
                    return status
                else:
                    print(f"获取屏幕状态失败: {data['msg']}")
            return None
        except Exception as e:
            print(f"获取屏幕状态出错: {e}")
            return None
        
    def get_screen_voice(self):
        """获取大屏音量"""
        api_url = f"{self.base_api_url}/screen/voice"
        try:
            response = requests.get(api_url)
            print(f"获取音量响应: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                if data["isSuccess"]:
                    voice = data["data"]
                    print(f"当前音量: {voice}")
                    return voice
                else:
                    print(f"获取音量失败: {data['msg']}")
            return None
        except Exception as e:
            print(f"获取音量出错: {e}")
            return None
    
    def get_recording_status(self):
        """查询录音状态"""
        api_url = f"{self.base_api_url}/screen/voiceRecordStatus"
        try:
            response = requests.get(api_url)
            print(f"获取录音状态响应: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                if data["isSuccess"]:
                    status = data["data"]
                    print(f"当前录音状态: {status}")
                    return status
                else:
                    print(f"获取录音状态失败: {data['msg']}")
            return None
        except Exception as e:
            print(f"获取录音状态出错: {e}")
            return None
        
class MeetingDeviceControl:
    def __init__ (self, user="123"):
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
    
class MeetingOtherDeviceControl:
    def __init__(self, user="123"):
        self.base_api_url = f"http://http://10.30.35.115:8090/api/v2/gateway"

    def control_screen_voice_record_status(action, self, status):
        """录音控制
        参数: status - 'start' 或 'stop' 或 'pause' 或 'resume'
        """
        if status not in ['start', 'stop', 'pause', 'resume']:
            print("无效的状态参数，请使用 'start' 或 'stop' 或 'pause' 或 'resume'")
            return False
        
