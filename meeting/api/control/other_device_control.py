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
    
    def invite_cloud_tx_meeting(self, user_names):
        """ 邀请加入腾讯云会议"""
        api_url = f"{self.base_api_url}/meeting/inviteUser"
        
        # 如果传入的是列表，转换为逗号分隔的字符串
        if isinstance(user_names, list):
            user_names_str = ",".join(user_names)
        else:
            user_names_str = user_names
        
        params = {
            "userNames": user_names_str
        }
        
        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                print(f"状态码: {response.status_code}")
                data = response.json()
                inner_data = data.get("data", {})
                if inner_data["isSuccess"]==True:
                    # print(data)
                    print(f"邀请成功: {inner_data.get('msg', '')}")
                else:
                    print(f"邀请失败: {inner_data.get('msg', '')}")
            else:
                print("邀请加入腾讯云会议失败，状态码:", response.status_code)
        except Exception as e:
            print(f"请求失败: {e}")
            return False
        
    def join_cloud_tx_meeting(self, Code, pswd):
        """ 加入腾讯云会议"""
        api_url = f"{self.base_api_url}/meeting/join"
        params = {
            "meetingCode": Code,
            "password": pswd
        }
        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                print(f"状态码: {response.status_code}")
                data = response.json()
                print(data)
                if data["isSuccess"]==True:
                    # print(data)
                    print(f"加入会议成功: {data.get('msg', '')}")
                else:
                    print(f"加入会议失败: {data.get('msg', '')}")
            else:
                print("加入腾讯云会议失败，状态码:", response.status_code)
        except Exception as e:
            print(f"请求失败: {e}")
            return False
        