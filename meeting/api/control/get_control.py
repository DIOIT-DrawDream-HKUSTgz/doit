from ..api_base import BaseApi
import requests

class GetControl(BaseApi):
    """GET控制API"""
    
    def __init__(self, user="123"):
        super().__init__()
        self.base_api_url = f"http://10.30.35.115:8090/api/v2/gateway"

    def end_meeting(self):
        """ 结束会议"""

        api_url = f"{self.base_api_url}/meeting/close"
        # params = {}
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print("结束会议成功", data.get("msg", ""))
            else:
                print("结束会议失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
    
    def close_hot_code(self):
        """ 关闭热码投屏"""

        api_url = f"{self.base_api_url}/meeting/close/osDeskTopHotKey"
        # params = {}
        try:
            response = requests.get(api_url)
            print(f"状态码: {response.status_code}")
            if response.status_code == 200:
                # print("热码投屏已关闭")
                # data = response.json()
                if ("isSuccess"):
                    print("热码投屏已关闭")
                else:
                    print("热码投屏关闭失败")
            else:
                print("热码投屏关闭失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
        
    def end_cloud_tx_meeting(self):
        """ 结束腾讯云会议"""

        api_url = f"{self.base_api_url}/meeting/cloud/close"
        try:
            print("test")
            response = requests.get(api_url)
            print(f"状态码: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                # print(data)
                print(f"结束腾讯云会议成功: {data.get('msg', '')}")
            else:
                print("结束腾讯云会议失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
    
    def query_meeting_list(self):
        """ 查询会议列表"""

        api_url = f"{self.base_api_url}/meeting/list"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print("查询会议列表成功:", data)
            else:
                print("查询会议列表失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
        
    def quick_meeting(self):
        """ 快速会议"""

        api_url = f"{self.base_api_url}/meeting/meetingCode/quickMeeting"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print("快速会议成功")
            else:
                print("快速会议失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False

    def desk_top_hot_key(self):
        """ 桌面热码投屏"""

        api_url = f"{self.base_api_url}/meeting/osDeskTopHotKey"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print(data)
                print("桌面热码投屏成功:")
            else:
                print("桌面热码投屏失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
    
    def share_desk(self):
        """ 共享桌面"""

        api_url = f"{self.base_api_url}/meeting/screen/meetingShare"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print(f"分享桌面成功: {data.get('msg', '')}")
                print(data)
            else:
                print("分享桌面失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
        
    def close_share_desk(self):
        """ 关闭共享桌面"""

        api_url = f"{self.base_api_url}/meeting/screen/meetingShare/close"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print(f"关闭共享桌面成功: {data.get('msg', '')}")
                print(data)
            else:
                print("关闭共享桌面失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
    
    def start_meeting(self):
        """ 开始会议"""

        api_url = f"{self.base_api_url}/meeting/start"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                # print(data)
                print(f"开始会议成功: {data.get('msg', '')}")
            else:
                print("开始会议失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
        
    def start_meeting_by_id(self, ID):
        """通过ID启动会议"""
        api_url = f"{self.base_api_url}/meeting/startById"
        params = {
            "infoMeetingId": ID
        }
        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                print(f"通过ID启动会议成功: {data.get('msg', '')}")
            else:
                print("通过ID启动会议失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
        
    def start_cloud_meeting(self):
        """ 启动腾讯云会议"""
        api_url = f"{self.base_api_url}/meeting/startMeeting/cloud"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print(f"启动腾讯云会议成功: {data.get('msg', '')}")
            else:
                print("启动腾讯云会议失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
        
    def switch_mute(self):
        """会议开始中点击麦克风修改状态"""
        api_url = f"{self.base_api_url}/meeting/switchMute"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print(f"切换静音状态成功: {data.get('msg', '')}")
            else:
                print("切换静音状态失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False
        
    def switch_video(self):
        """会议开始中点击摄像头修改状态"""
        api_url = f"{self.base_api_url}/meeting/switchVideo"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print(f"切换摄像头状态成功: {data.get('msg', '')}")
            else:
                print("切换摄像头状态失败，状态码:", response.status_code)
            return True
        except Exception as e:
            print(f"请求失败: {e}")
            return False