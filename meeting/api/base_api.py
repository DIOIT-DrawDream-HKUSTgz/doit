class BaseApi:
    """API基类，包含通用请求方法和基础功能"""
    
    def __init__(self, base_url=None):
        self.base_url = base_url or "http://10.30.35.115:8090/api/v2/gateway/iot"
        
    def send_request(self, method, endpoint, data=None):
        """
        发送API请求
        
        参数:
            method: 请求方法 ('get', 'post', 'put', 'delete')
            endpoint: API端点
            data: 请求数据
            
        返回:
            tuple: (成功状态, 响应数据)
        """
        import requests
        
        api_url = f"{self.base_url}/{endpoint}"
        try:
            if method.lower() == 'get':
                response = requests.get(api_url, params=data)
            elif method.lower() == 'post':
                response = requests.post(api_url, json=data)
            else:
                print(f"不支持的请求方法: {method}")
                return False, None
                
            print(f"获取响应: {response.status_code}")
            if response.status_code == 200:
                resp_data = response.json()
                if resp_data.get("isSuccess", False):
                    return True, resp_data.get("data")
                else:
                    return False, resp_data.get("msg", "未知错误")
            return False, f"HTTP错误: {response.status_code}"
        except Exception as e:
            print(f"请求失败: {str(e)}")
            return False, str(e)
