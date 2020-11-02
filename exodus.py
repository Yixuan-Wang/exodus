import json
import requests

with open("config.json", "r", encoding="utf-8") as file_config:
    config = json.load(file_config)

API = "https://pkuhelper.pku.edu.cn/services/pkuhole/api.php?action={action}{extras}&PKUHelperAPI=3.0&jsapiver=null-445638&user_token={token}"

req_attention_list = requests.get(API.format(action="getattention", extras="", token=config["token"]))
attention_list = json.loads(req_attention_list.content)["data"]

for hole in attention_list:
    print(hole['pid'])
    req_replies = requests.get(API.format(action="getcomment", extras=f"&pid={hole['pid']}", token=config["token"]))
    hole["replies"] = json.loads(req_replies.content)["data"]

with open("attention_list.json", "w", encoding="utf-8") as file_attention:
    json.dump(attention_list, file_attention, ensure_ascii=False)
