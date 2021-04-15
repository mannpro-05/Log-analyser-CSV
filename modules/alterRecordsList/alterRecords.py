import csv
'''
'''
def editRecords(data):
    lines = []
    records = open('recordsList.csv', 'r')
    reader = csv.reader(records)
    for row in reader:
        if row != []:
            if row[1] != data["title"]:
                lines.append(row)
    records.close()
    records = open('recordsList.csv', 'w')
    writer = csv.writer(records)
    writer.writerows(lines)
def duplicateRecord(data):
    count = 0
    records = open('recordsList.csv', 'r')
    reader = csv.reader(records)
    for row in reader:
        if row != []:
            if row[1][:len(data["title"])] == data["title"]:
                count+=1
    records = open('recordsList.csv', 'a')
    writer = csv.writer(records)
    writer.writerow(['0',data["title"]+'('+str(count)+')',data["description"],data["columns"]])

def deleteRecord(data):
    lines = []
    records = open('recordsList.csv', 'r')
    reader = csv.reader(records)
    for row in reader:
        if row != []:
            if row[1] != data["title"]:
                lines.append(row)
    records.close()
    records = open('recordsList.csv', 'w')
    writer = csv.writer(records)
    writer.writerows(lines)