import requests
api_address="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=bbeb15c3b6614ff496ea61ab795df4d7"
json_data=requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append("Number"+ str(i+1) + json_data["articles"][i]["title"]+".")
    return ar
arr=news()
print(arr)