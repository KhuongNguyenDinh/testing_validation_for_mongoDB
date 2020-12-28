import json
from converter import csv_to_json
from pymongo import MongoClient
from pprint import pprint
#client of mongoDB and port
def read_mongo(database,collection,column):
    client = MongoClient('localhost:27017')
    db = client[database]
    col = db[collection]
    x = col.find()
    for data in x:
        print(data[column])
#check status of mongoDB
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)
def convert_csv():
    #csv path
    csv_path = r'C:/Users/dkhuo/Desktop/khuong_solo_thesis/1/user.csv'
    #json path
    json_path = r'C:/Users/dkhuo/Desktop/khuong_solo_thesis/1/user.json'
    csv_to_json(csv_path,json_path)

def read_local_test():
    with open("C:/Users/dkhuo/Desktop/khuong_solo_thesis/1/1.json") as f:
        y = json.load(f)
    for x in y:
        if not isinstance(x["name"],str) or x["name"][0].isupper() == False:
            print(x["name"]," First letter is not uppercase and invalid format!")
        elif float(x["age"])%1 != 0 or int(x["age"]) <= 0:
            print(x["name"], " Invalid Age!")
        elif x["major"] not in ["cs","ce"]:
            print(x["name"]," Invalid major")
        else:
            print(x["name"],"passed")

def check_user():
    with open("C:/Users/dkhuo/Desktop/khuong_solo_thesis/1/user.json") as f:
        y = json.load(f)
    for x in y:
        print(x["username"],x["password"])
#read_local_test()
# convert_csv()
check_user()
# read_mongo("multi","userProfile","password")
