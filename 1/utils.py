import json
import string
def anyUpper(s):
    check = False
    for x in s:
        if x.isupper() == False:
            continue
        elif x.isupper() == True:
            check = True
            break
    if(check == True):
        return True
    else:
        return False

