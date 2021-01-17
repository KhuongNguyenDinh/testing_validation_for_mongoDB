import json
import string
import logging
import re
from converter import csv_to_json
from pymongo import MongoClient 
from utils import anyUpper

host = MongoClient("localhost:27017")
database = host.test
collection= database.user

class PreChecker_mongo:
    def __init__(self,client,db,collection):
        self.client = client
        self.db = db
        self.collection = collection
        
    def check_nickname(self):
        y = collection.find()
        for x in y:
            check_nickname = map(lambda x: x in special_chars, x["nickname"])
            print(x["nickname"],"invalid only non_special characters are allowed") if any(check_nickname) else print(x["nickname"],"clean nickname!")

    def check_username(self):
        y = collection.find()
        for x in y:
            if not isinstance(x["username"],str) or len(x["username"]) < 8:
                if not isinstance (x["username"],str): 
                    print("Invalid username:",x["username"],"is not a string")
                elif len(x["username"]) < 8:
                    print("Invalid username:",x["username"],"the username has to be at least 8 character")
            else:
                print(x["nickname"],"clean username!")

    def check_password(self):
        y = collection.find()
        for x in y:
            check_password = map(lambda x: x in special_chars, x["password"])
            if len(x["password"]) < 8 or (anyUpper(x["password"]) == False) or not any(check_password):
                print(x["nickname"],"invalid password")
            else:
                print(x["nickname"],"clean password!")
    
    def check_phone(self):
        y = collection.find()
        for x in y:
            if(x["phone"].isdigit() == False) or len(x["phone"]) != 10:
                if(x["phone"].isdigit() == False):
                    print(x["phone"],"invalid phone number, phone number must be numbers!")
                elif len(x["phone"]) != 10:
                    print(x["phone"],"invalid phone number, phone number must be 10 numbers!")
            else:
                print(x["nickname"],"clean phone number!")    
    
    def check_email(self):
        regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
        y = collection.find()
        for x in y:
            if(re.search(regex,x["email"])):
                print(x["nickname"],"email clean!")
            else:
                print(x["nickname"],"invalid email address!")
                   
    def check_gender(self):
        gender_set = ["M","m","F","f","male","Male","Female","female"]
        y = collection.find()
        for x in y:   
            if  x["gender"] not in gender_set:
                print(x["nickname"],"invalid gender!")
            else:
                print(x["nickname"],"gender clean!")
    
    def check_All(self):
        self.check_nickname()
        self.check_username()
        self.check_password()
        self.check_phone()
        self.check_email()
        self.check_gender()

special_chars = string.punctuation
a = PreChecker_mongo(host,database,collection)
a.check_password()