import json
import requests
import time

class MeetingDeviceController:
    def __init__(self, server_ip, user_id="123"):
        self.server_ip = server_ip
        self.base_api_url = f"http://{server_ip}:8090/api/v2/gateway/iot"
        self.meeting_api_url = f"http://{server_ip}:8090/api/v2/gateway/meeting"

    def manual_control(self, action_type):
        if action_type == "start_projection":
            self.control_screen_brightness(80)  # 高亮度
            print("投影开始 - 屏幕亮度已调高")
        elif action_type == "end_projection":
            self.control_screen_brightness(30)  # 低亮度
            print("投影结束 - 屏幕亮度已调低")

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

    def control_screen_brightness(self, brightness_level):
        """控制大屏亮度"""
        api_url = f"{self.base_api_url}/screen/brightness/set"
        payload = {
            "brightness": brightness_level
        }
        try:
            response = requests.get(api_url, params=payload)
            print(f"亮度控制响应: {response.status_code}")
            return response.status_code == 200
        except Exception as e:
            print(f"控制屏幕亮度出错: {e}")
            return False
            
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
    controller = MeetingDeviceController("10.30.35.115")
    
    # 提供简单的命令行界面
    while True:
        cmd = input("输入命令 (start/end/brightness/mic/quit): ")
        if cmd == "start":
            controller.manual_control("start_projection")
        elif cmd == "end":
            controller.manual_control("end_projection")
        elif cmd == "brightness":
            controller.get_screen_brightness()
        elif cmd == "mic":
            controller.switch_microphone_mute()
        elif cmd == "quit":
            break