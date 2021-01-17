import json
import string
import logging
import re
from converter import csv_to_json
from pymongo import MongoClient
from pprint import pprint

###################################################################

json_path = input(str("what json file you want to run? : "))
# json_path = "user.json"
# csv_path = "user.csv"
# csv_path = f.readline().rstrip()
#rstrip remove the newline of the character
###################################################################
special_chars = string.punctuation


#check status of mongoDB
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)
#a = input("which file you want to run? : ")
class PreChecker():
    def _init_(self,csv_path,json_path):
        self.csv_path = csv_path
        self.json_path = json_path

    def convert_csv(self):
        csv_path = input(str("what csv file you want to convert? : "))
        csv_to_json(csv_path,json_path)

    # def check_user(self):
    #     with open(json_path) as f:
    #         y = json.load(f)
    #     for x in y:
    #         print(x["username"],x["password"])

    def check_firstname(self):
        with open(json_path) as f:
            y = json.load(f)
        for x in y:
            if not isinstance(x["name"],str) or x["name"][0].isupper() == False:
                print(x["name"],"first letter of the first name is not uppercase and invalid format!")
            else:
                print(x["name"],"clean!")
            
    def check_lastname(self):
        with open(json_path) as f:
            y = json.load(f)
        for x in y:
            if not isinstance(x["name"],str) or x["name"][0].isupper() == False:
                print(x["name"],"first letter of the last name is not uppercase and invalid format!")
            else:
                print(x["name"],"clean!")

    def check_nickname(self):
        with open(json_path) as f:
            y = json.load(f)
        for x in y:
            check_nickname = map(lambda x: x in special_chars, x["nickname"])
            print(x["nickname"],"invalid only non_special characters are allowed") if any(check_nickname) else print(x["nickname"],"clean nickname!")

    def check_username(self):
        with open(json_path) as f:
            y = json.load(f)
        for x in y:
            if not isinstance(x["username"],str) or len(x["username"]) < 8:
                if not isinstance (x["username"],str): 
                    print("Invalid username:",x["username"],"is not a string")
                elif len(x["username"]) < 8:
                    print("Invalid username:",x["username"],"the username has to be at least 8 character")
            else:
                print(x["nickname"],"clean username!")

    def check_password(self):
        with open(json_path) as f:
            y = json.load(f)
        for x in y:
            check_nickname = map(lambda x: x in special_chars, x["password"])
            print(x["nickname"],"invalid nickname") if any(check_nickname) else print(x["nickname"],"clean nickname")
    
    def check_phone(self):
        with open(json_path) as f:
            y = json.load(f)
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
        with open(json_path) as f:
            y = json.load(f)
        for x in y:
            if(re.search(regex,x["email"])):
                print(x["nickname"],"email clean!")
            else:
                print(x["nickname"],"invalid email address!")
                   
    def check_gender(self):
        gender_set = ["M","m","F","f","male","Male","Female","female"]
        with open(json_path) as f:
            y = json.load(f)
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

# # print(json_path)
# # convert_csv()
a = PreChecker()
# a.convert_csv()
# a.check_nickname()
# a.check_username()
# a.check_password()
# a.check_phone()
a.check_All()
# a.check_gender()
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",format="%(asctime)-15s %(levelname)-8s %(message)s")
    logging.info("Check successfully!")