import requests
import json
import os

def send_json_request(json_file_path, url):
    """
    读取指定的JSON文件并将其内容发送到指定URL，然后返回响应
    
    参数:
        json_file_path: JSON文件路径
        url: 目标URL
    
    返回:
        响应对象
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(json_file_path):
            print(f"错误：文件 {json_file_path} 不存在")
            return None
        
        # 读取JSON文件
        with open(json_file_path, 'r') as file:
            payload = json.load(file)
        
        # 发送POST请求
        headers = {'Content-Type': 'application/json'}
        print(f"发送请求到 {url}")
        print(f"请求内容: {json.dumps(payload, indent=2, ensure_ascii=False)}")
        
        response = requests.put(url, json=payload, headers=headers)
        
        # 打印响应信息
        print(f"响应状态码: {response.status_code}")
        print("响应内容:")
        
        try:
            # 尝试将响应解析为JSON并美化输出
            response_json = response.json()
            print(json.dumps(response_json, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            # 如果不是有效的JSON，则直接输出文本
            print(response.text)
            
        return response
    
    except Exception as e:
        print(f"发生错误: {e}")
        return None

if __name__ == "__main__":
    # 配置
    json_file_path = "e:/code/Programme/doit/ue4/test1.json"
    url = "http://localhost:30010/remote/object/property"
    
    # 发送请求
    response = send_json_request(json_file_path, url)