import requests

def getNewsExamApi():

    url ="http://localhost:8080/newsExam" 

    response = requests.get(url)
    newsExamDto = response.json()

    if(newsExamDto["code"] == 1):
        return newsExamDto["data"]
    else:
        print(newsExamDto["msg"])   
         
