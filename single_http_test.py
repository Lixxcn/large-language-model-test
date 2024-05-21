import requests
import os

api_key = os.getenv("DASHSCOPE_API_KEY")
url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
headers = {'Content-Type': 'application/json',
           'Authorization':f'Bearer {api_key}'}
body = {
    'model': 'qwen-turbo',
    "input": {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": input("请输入：")
            }
        ]
    },
    "parameters": {
        "result_format": "message"
    }
}

response = requests.post(url, headers=headers, json=body)
print(response.json())