from modules.readCsv import csvReader
'''
1.Input: data -> It is a json data which is coming from the querying form.
2.Processing: A mappingDict is created which will map the userName to its corresponding ID same is for other fields.
3.Output: It would be a dictionary witch will have the ID of it's corresponding fields.
'''
def mappingList(data):
    finalList = {}
    if data["username"] == data["usergroup"] == data["website"] == "":
        finalList["getAllData"] = True
    else:
        finalList["getAllData"] = False
    uid,temp = csvReader.findData(data["username"], 'userName.csv')
    gid,temp = csvReader.findData(data["usergroup"], 'userGroup.csv')
    wid,temp = csvReader.findData(data["website"], 'website.csv')
    if uid != None:
        finalList["userName"] = uid
    elif data["username"] == "":
        pass
    else:
        return {}
    if gid != None:
        finalList["userGroup"] = gid

    elif data["usergroup"] == "":
        pass
    else:
        return {}
    if wid != None:
        finalList["website"] = wid

    elif data["website"] == "":
        pass
    else:
        return {}
    return finalList


