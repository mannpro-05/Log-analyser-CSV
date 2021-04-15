from modules.readCsv import csvReader
from modules import app
import json
import inspect
from datetime import datetime



def getAllData(rows,fields):
    temp = {}
    opt = []
    if fields != '':
        for i in fields:
            now = datetime.now()
            app.logger.info(
                str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
                    3] + i + rows[i])
            if i == "uid" or i == 'timestamp':
                opt.append(rows[i])
                temp[i] = rows[i]
            else:
                data = csvReader.findDataDisplay(rows[i], (i + '.csv'))
                if data != None:
                    opt.append(data)
                    temp[i] = data
        return opt, temp
    else:
        temp["uid"] = ""
        temp["userName"] = ""
        temp["userGroup"] = ""
        temp["website"] = ""
        temp["timestamp"] = ""
        for key, val in rows.items():
            now = datetime.now()
            app.logger.info(
                str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][
                    3] + ':' + 'key:' + key + 'value:' + val)

            if key == 'timestamp' or key == 'uid':
                opt.append(rows[key])
                temp[key] = rows[key]
            else:
                data = csvReader.findDataDisplay(rows[key], (key + '.csv'))
                opt.append(data)
                temp[key] = data
        return opt, temp



'''
Input: username, group, webname, timestamp will be the strings which will contain the data which is to be displayed on
the webpage!
Processing: It will convert the input strings into JSON format data in a specific format such that it fits in the frontend
Output: It will return the JSON format data.
'''
def outputReturn(temp, fdata):
    data = {}
    finalJson = {}
    columns = []
    now = datetime.now()
    app.logger.info(str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':temp' + json.dumps(temp) +' Fdata:' + ','.join([str(i) for i in fdata]))
    if temp != {}:
        for key,val in temp.items():
            if temp[key] != "":
                columns.append({"title":key})
        now = datetime.now()
        app.logger.info(
            str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':temp' + ','.join([str(i) for i in columns]) + ' Fdata:' + ','.join([str(i) for i in fdata]))
        data["COLUMNS"] = columns
        now = datetime.now()
        app.logger.info(
            str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ' Fdata:' + ','.join([str(i) for i in fdata]))
        data["DATA"] = fdata
        finalJson["data"] = data
        now = datetime.now()
        app.logger.info(
            str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':temp' + json.dumps(
                finalJson) + ' Fdata:' + ','.join([str(i) for i in fdata]))

        return finalJson
    data["DATA"] = []
    data["COLUMNS"] = [{"title": "UserID"}, {"title": "UserName"}, {"title": "UserGroup"},
                       {"title": "WebsiteName"},{"title":"TimeStamp"}]
    finalJson["data"] = data
    return finalJson