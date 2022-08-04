from operator import index
from helper import *
import random
from datetime import datetime
# get current datetime
dt = datetime.now()

# get day of week as an integer
day_num = dt.weekday()

chest = "chest"
back = "back"
shoulders = "shoulders"
legs = "legs"
abdominals = "abdominals"
biceps = "biceps"
adductor = "adductor"
abductors = "abductors"
triceps = "triceps"
cable = "cable"
weight = "weight"


push_list = [chest,shoulders]
pull_list = [back,biceps]
legs_list = [legs]
pull = 1
push = 0
legs = 2

pplDict = {
    "push":push_list,
    "pull":pull_list,
    "legs":legs_list
}

def rand_item(mainList,numTimes):
    finalList = []
    #mainList[]
    for i in range(numTimes):
        for itemList in mainList:
            if(type(itemList) != str):
                index = random.randint(0,len(itemList)-1)
                finalList.append(itemList[index])     
                itemList.pop(index)
    #print(finalList)
    return finalList 
#breaking up num to compare for todays day of week
first_half = [0,1,6]
second_half = [2,3,4,5]

#idea for num times can be how hard workout is
def week_based(mainList,numTimes):
    finalList = []
    for i in range(numTimes):
        for itemList in mainList:
            index = 0
            if(day_num in first_half):
                #print("sun-mon")
                index = 0
            elif(day_num in second_half):
                index = -1
                #print("tuesaday-satrurday")
            try:
                finalList.append(itemList[index])     
                itemList.pop(index)
            except IndexError:
                print("num chosen either too big or too low for lsit")
    return finalList

#returns list of exercises based on either weekly alg or future fucntiojnality coming...
def push_pull(decision):
    dataDict = openJson()
    list_exercises = []
    decisionList = []
    #
    if((decision == "push") or (decision == "pull") or (decision == "legs")):
        listDecision = pplDict[decision]
        for i in range(len(listDecision)):
            exercise_str = listDecision[i]
            if(len(dataDict[exercise_str]) > 0):
                
                #handling chest (no sub categories)
                if (len(dataDict[exercise_str]) == 2): 
                    
                    list_temp= alternateList([dataDict[exercise_str][cable],dataDict[exercise_str][weight]])
                    if(len(list_temp) != 0):
                        list_exercises.append(list_temp)
 
                else:
                    for exerciseType, exerciseList in dataDict[exercise_str].items():
                        list_temp = alternateList([exerciseList[cable],exerciseList[weight]])
                        if(len(list_temp) != 0):
                            list_exercises.append(list_temp)
                        
        #decisionList = rand_item(list_exercises,3)
        decisionList = week_based(list_exercises,3)
        #if(decisionList)
    
                    
                    #for exercise, weightHow in dataDict.items():
        
    else:
        print("incorrect input")
    # print(list_exercises)
    return decisionList


## argument is lsit of 2 list
#returns list of items alternating btwn each
def alternateList(listIn):
    list_final = []
    num_alternate = len(listIn[1]) + len(listIn[0]) #getting num of lsits to combine
    #print(num_alternate)
    for i in range(num_alternate):
        length_CABLE= 0     
        length_WEIGHT = 0
        #print(i)
        if((i % 2 == 0) and (len(listIn) >= 2)):
            if(listIn[1]):
            #try:
                #print(listIn[1][length_WEIGHT])
            # if(listIn[1]):
                #try:
                list_final.append(listIn[1][length_WEIGHT])
                listIn[1].pop(length_WEIGHT)
                #except KeyError:
                   # print(listIn)

        else:      
            if(listIn[0]):
                #try:
                list_final.append(listIn[0][length_CABLE])
                listIn[0].pop(length_CABLE)
                #except KeyError:
                #    print(listIn)
    return list_final

def main_menu():
    print("this is main menu")
    ExerciseList = push_pull("push")
    print(ExerciseList)




main_menu()
















