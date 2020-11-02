import json
import requests

with open("config.json", "r", encoding="utf-8") as file_config:
    config = json.load(file_config)

API = "https://pkuhelper.pku.edu.cn/services/pkuhole/api.php"

DEFAULT_PARAMS = {
    "PKUHelperAPI": "3.0",
    "jsapiver": "null-445638",
    "user_token": config["token"]
}

req_attention_list = requests.get(API, params={"action":"getattention", **DEFAULT_PARAMS})
attention_list = json.loads(req_attention_list.content)["data"]

for hole in attention_list:
    print(hole['pid'])
    req_replies = requests.get(API, params={"action":"getcomment", "pid":hole["pid"], **DEFAULT_PARAMS})
    hole["replies"] = json.loads(req_replies.content)["data"]

with open("attention_list.json", "w", encoding="utf-8") as file_attention:
    json.dump(attention_list, file_attention, ensure_ascii=False)
