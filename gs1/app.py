#we will send the request and receive a response

import requests
import json

URL = "http://127.0.0.1:8000/student/"   #specify the  url where request is sent

r = requests.get(url=URL)  # send the request, r specifies the response

#r=requests.get(url="http://127.0.0.1:8000/student/")


data = r.json()  # get the json data
print(data)  # print the data