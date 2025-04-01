import json
import requests
import time
class MeetingDeviceIot:
    def __init__(self, user_id="123"):
        self.base_api_url = f"http://10.30.35.115:8090/api/v2/gateway/iot"
        self.meeting_api_url = f"http://10.30.35.115:8090/api/v2/gateway/meeting"

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

    def switch_microphone_mute(self):
        """切换麦克风静音状态"""
        api_url = f"{self.meeting_api_url}/switchMute"
        try:
            response = requests.get(api_url)
            print(f"麦克风控制响应: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                if data["isSuccess"]:
                    print("麦克风状态已切换")
                    return True
                else:
                    print(f"麦克风控制失败: {data['msg']}")
            return False
        except Exception as e:
            print(f"控制麦克风出错: {e}")
            return False

if __name__ == "__main__":
    ControllerIot = MeetingDeviceIot()
    
    # 提供简单的命令行界面
    while True:
        cmd = input("输入命令 (iot/quit): ").strip().lower()
        if cmd == "iot":
            cmd = input("输入命令 (screen/quit): ").strip().lower()
            if cmd == "screen":
                cmd = input("输入命令 (brightness/status/voice/voiceRecordStatus/quit): ").strip().lower()
                if cmd == "brightness":
                    ControllerIot.get_screen_brightness()
                elif cmd == "status":
                    ControllerIot.get_screen_status()
                elif cmd == "voice":
                    ControllerIot.get_screen_voice()
                elif cmd == "voiceRecordStatus":
                    ControllerIot.get_recording_status()
                elif cmd == "..":
                    continue
                elif cmd == "quit":
                    break  
            elif cmd == "..":
                continue
            elif cmd == "quit":
                break
        elif cmd == "quit":
            break