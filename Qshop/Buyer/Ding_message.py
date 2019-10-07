import json
import requests
url="https://oapi.dingtalk.com/robot/send?access_token=43f4b33c22ae840d54ee6de90c43b6dbdd12c45b2a07686ec5820e806dd913d2"
headers = {
    "Content-Type": "application/json",
    "Charset": "utf-8"
}

requests_data = {
    "msgtype": "text",
    "text": {
        "content": "excuse me"
    },
    "at": {
        "atMobiles": [
        ],
        "isAtAll": True
    }
}

sendData = json.dumps(requests_data)

response = requests.post(url = url,headers = headers, data = sendData)

content = response.json()

print(content)