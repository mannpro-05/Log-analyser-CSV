import csv
import inspect
from modules import app
from datetime import datetime
from modules.displayModule import displayFunctions
import json
'''
1.Input: The first one is the formdata which is the data coming out of the form and second one is mappingList which is a 
dict which contains the ID's of the corresponding fields.
2.Processing:The function will do a lot of filtering(according to data,time,username.usergrtoup etc) based on the data 
which is received form the formData.
3.Output:It would be a json format data witch will contain all the data which is to be displayed after the processing
/filtering part is complete. 
'''

def groupingDisplay(formData = {}):
    tempRows ={}
    finalVal = []
    now = datetime.now()
    app.logger.info(
        str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
            3] + ':Arr ' + json.dumps(formData) + ' Fname: ')
    with open('finalData.csv', 'r') as finalData:
        finalData = csv.reader(finalData)
        for rows in finalData:
            tempRows["uid"] = rows[1]
            tempRows["userName"] = rows[1]
            tempRows["userGroup"] = rows[2]
            tempRows["website"] = rows[3]
            tempRows["timestamp"] = rows[0]

            now = datetime.now()
            app.logger.info(
                str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
                    3] + ':tempRows ' + json.dumps(tempRows) + ' Rows: ' + ','.join(rows))
            opt = displayFunctions.getAllData \
                (tempRows, formData["fields"])
            if opt:
                while ("" in opt[0]):
                    opt[0].remove("")
                finalVal.append(opt[0])
                temp = opt[1]
        return displayFunctions.outputReturn(temp, finalVal)

def recordsDisplay():
    recordsList = []
    data = {}
    finaData = {}
    with open('recordsList.csv','r') as records:
        records = csv.reader(records)
        for i in records:
            if i != []:
                recordsList.append(i)
        data["DATA"] = recordsList
        data["COLUMNS"] =  [{"title": "RecordID"}, {"title": "Title"}, {"title": "Description"},
                       {"title": "Column Name"},{"title": ""},{"title": ""},{"title": ""}]
        finaData["data"] = data
        return finaData

