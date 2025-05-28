import requests

class BaseApi:
    """API基类，提供通用请求处理功能"""
    
    def __init__(self, user_id="123"):
        self.base_api_url = "http://10.30.35.115:8090/api/v2/gateway"
        self.user_id = user_id
        
    def send_request(self, method, endpoint, params=None):
        """发送请求并处理通用响应"""
        api_url = f"{self.base_api_url}/{endpoint}"
        try:
            if method.lower() == 'get':
                response = requests.get(api_url, params=params)
            elif method.lower() == 'post':
                response = requests.post(api_url, json=params)
            else:
                return (False, f"不支持的方法: {method}")
                
            print(f"API请求响应: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                if data["isSuccess"]:
                    return (True, data["data"])
                else:
                    return (False, data["msg"])
            return (False, f"HTTP错误: {response.status_code}")
        except Exception as e:
            return (False, f"请求出错: {str(e)}")