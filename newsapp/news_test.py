import json
import requests

# response.json()
# json문자열 => json.loads() = dict
# dict => json.dumps() = json


url ="http://localhost:8080/news" 

response = requests.get(url)
newsDto = response.json()

if(newsDto["code"] == 1):
    print(newsDto["data"][0])





