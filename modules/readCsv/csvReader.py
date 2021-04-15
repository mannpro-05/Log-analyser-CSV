import csv
import inspect
from modules import app
from datetime import datetime
'''
Input: it will get the value of the input filed and a the name of the database
Processing: It will search for the value in its respective database and if value is there then it wil return Its Id
else it will retuen the New Id for the new user
Output: It either return the ID of the field or will return the new ID for the new user. 
'''
def findData(name,fName):
    counter=1
    now = datetime.now()
    app.logger.info(
        str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':Name ' + name + ' Fname: ' + fName)

    with open(fName,'r') as file:
        file = csv.reader(file)
        for i in file:
            if i[1] == name:
                return i[0],None
            counter+=1
    return None,counter

'''
Input: it will get the uid(int) of the input filed and the value(String) of that that Id and the name of the database which 
is to be opened.
Processing: It will search for the value in its respective database and will append the corresponding field of the ID to
the value and will also check if that value is already there in the value string or not because we dont want duplicates.
Output: It will return the updated string which will be used in the displaying purpose. 
'''
def findDataDisplay(uid,fName):
    now = datetime.now()
    '''app.logger.info(
        str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
            3] + ':Name ' + uid + ' Fname: ' + fName)'''

    if fName != 'website.csv':
        with open(fName,'r') as file:
            file = csv.reader(file)
            for i in file:
                if i[0] == uid:
                    return i[1]
    else:
        with open(fName, 'r') as file:
            file = csv.reader(file)
            for i in file:
                if i[0] == uid:
                    return i[1]

