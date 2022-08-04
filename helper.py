import json

dataFilename = "data.json"

def writeJson(dataDict):
    s = json.dumps(dataDict,indent=4)
    with open(dataFilename,'w') as file:
        file.write(s)  
    file.close()  

def printDict():
    dataDict = openJson()
    #pprint.pprint(dataDict)

#returns dict from json.dict
def openJson():
    with open(dataFilename, 'r') as myfile:
        openData = json.load(myfile)
    return openData
dict1 =  {
    "cable":
        "dict2",
    "weight":
        "dict1"
    }
dict2 = {
    "cable":
        "dict1",
    "weight":
        "dict2"
    }

main = {
    "cable":
        "dict1",
    "weight":
        "dict2"
    }
listData = [dict1,dict2]


print(listData[1]["weight"])


