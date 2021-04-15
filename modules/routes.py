from flask import *
from modules import app
from modules import displayModes
from modules.alterRecordsList import alterRecords
from datetime import datetime
import inspect
import json
import csv

'''
1. Input: None
2. Processing: None
3. Output: renders the create table page.
'''
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        now = datetime.now()
        app.logger.info(
            str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3])
        title = request.form['title']
        description = request.form['description']
        columns = request.form['columns']
        return render_template('table.html', title=title, description = description, columns = columns)
    now = datetime.now()
    app.logger.info(
        str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3])
    return render_template('table.html',title= 'temp')



'''
1. Input: json data from the create table page
2. Processing: It will check if the entered record is unique or not. if it is unique it will store it in the database.
3. Output: returns finalData in the same sequence as the current columns order entered if the data is unique else send 
an error message to the forntend.
'''
@app.route('/customTableDisplay', methods=['GET','POST'])
def customTableDisplay():
    print("hello")
    if request.method == 'POST':
        data = request.get_json()
        file = open("recordsList.csv")
        reader = csv.reader(file)
        for i in reader:
            if i != []:
                if i[1] == data["title"]:
                    return {'message':'err','error':'The title already exist. Please enter another value in the title field.'}
        lines = len(list(reader))
        file.close()
        with open('recordsList.csv','a', newline='') as record:
            record = csv.writer(record)
            record.writerow([lines, data["title"], data["description"], data["fields"]])
        if data["fields"] != '':
            data["fields"] = data["fields"].split(',')
        now = datetime.now()
        app.logger.info(
            str(now.strftime("%H:%M %Y-%m-%d")) + ' ' + __file__ + ' ' + inspect.stack()[0][3] + ':' + json.dumps(data))
        temp = displayModes.groupingDisplay(data)
        return temp
'''
1. Input: None
2. Processing: None
3. Output: renders the records page.
'''
@app.route('/records')
def records():
    return render_template('records.html')

'''
1. Input: None
2. Processing: None
3. Output: returns all of the records in the recordsList Database.
'''

@app.route('/getRecords', methods=["GET","POST"])
def getRecords():
    if request.method == 'POST':
        return displayModes.recordsDisplay()


@app.route('/updateRecords', methods=["GET","POST"])
def updateRecords():
    if request.method == 'POST':
        data = request.get_json()
        if data["buttonId"] == '0':
            alterRecords.editRecords(data)
            return data
        elif data["buttonId"] == '1':
            alterRecords.duplicateRecord(data)
            return 'hello'
        else:
            alterRecords.deleteRecord(data)
            return 'hello'
