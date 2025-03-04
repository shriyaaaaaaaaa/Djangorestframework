import requests
import json

URL = "http://127.0.0.1:8000/student/"

def get_data(id = None):     #if id is not passed then it will be none and gets all the data
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers={"content-Type":"application/json"}
    r = requests.get(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)
    
#get_data()  # get all data
# get_data(1)  # get data of id=1

def post_data():
    data={
        'name':'Ravi',
        'roll':20,
        'city':'delhi'
    }
    headers={"content-Type":"application/json"}
    json_data = json.dumps(data)
    r = requests.post(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)

#post_data()
    
def update_data():
    data = {
        'id':2,
        'name':'Ravi',
        'city':'Delhi'
    }
    headers={"content-Type":"application/json"}
    json_data = json.dumps(data)
    r = requests.put(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)
#update_data()
    
def delete_data():
    data = {'id':2}
    json_data = json.dumps(data)
    headers={"content-Type":"application/json"}
    r = requests.delete(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)
    
delete_data()

