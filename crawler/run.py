import requests


url = "http://localhost:6800/schedule.json"
data = {
    "project": "crawler",
    "spider": "tweet_by_keyword",
    "keyword": "端午节",  # 使用模型属性
    "start_time": "2024-05-20",
    "end_time": "2024-05-21",
}
response = requests.post(url, data=data)
print(response.json())