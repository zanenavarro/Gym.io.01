import json

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

dataFilename = "data.json"
userIn = "12"
type_ex = input("type:")
dataDict = {}
list_ex = []
while(userIn != "0"):
    userIn = input("exercise:")
    list_ex.append(userIn)
dataDict = openJson()
try: 
    dataDict[type_ex] = list_ex
except:
    dataDict[type_ex] = {}

writeJson(dataDict)
