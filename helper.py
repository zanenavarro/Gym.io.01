import json
import discord
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

"""
Function : alternateList(listIn)
Argument : list of 2 lists
Output   : returns one list, alternating between both lists given 
"""
def alternateList(listIn):
    list_final = []
    num_alternate = len(listIn[1]) + len(listIn[0]) #getting num of lsits to combine
    for i in range(num_alternate):
        length_CABLE= 0     
        length_WEIGHT = 0
        if((i % 2 == 0) and (len(listIn) >= 2)):
            if(listIn[1]):
                list_final.append(listIn[1][length_WEIGHT])
                listIn[1].pop(length_WEIGHT)

        else:      
            if(listIn[0]):
                list_final.append(listIn[0][length_CABLE])
                listIn[0].pop(length_CABLE)

    return list_final


"""
Function: 
Goal: 
Output: 
"""


        
        
# dict1 =  {
#     "cable":
#         "dict2",
#     "weight":
#         "dict1"
#     }
# dict2 = {
#     "cable":
#         "dict1",
#     "weight":
#         "dict2"
#     }

# main = {
#     "cable":
#         "dict1",
#     "weight":
#         "dict2"
#     }
# listData = [dict1,dict2]


# print(listData[1]["weight"])


