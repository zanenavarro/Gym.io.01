from operator import index
from helper import *
import random
from datetime import datetime
import os
import discord
from env import *



"""
To Do:
- push_pull_leg function (DONE) 
- HIIT circuit generator
- setting difficulty 
- discord integration
- 




"""
# get current datetime
dt = datetime.now()

# get day of week as an integer
day_num = dt.weekday()



TOKEN = DISCORD_TOKEN

channels = {
        "gymio": "997997118520303696",
        "brrrrrrrr": "803697560459280395"
}

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
     
PPLDict = {     
    "push":push_list,     
    "pull":pull_list,     
    "legs":legs_list     
}


functions= {

        "help": "!help",
        "push": "!push",
        "pull": "!pull",
        "legs": "!legs",
        "add" : "!add" 

}  
class MyClient(discord.Client):

    #global functions 
    

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
        # !push , !pull , !legs
        if((message.content == functions["pull"]) or (message.content == functions["push"]) or (message.content == functions["legs"])):
            
            listExercises = self.push_pull(message.content)
            self.messageList(self,listExercises,message)
            

        # help function
        # if((message.content == functions["help"])):
        #     for key,values in functions.items():
        #         message_send = "Function List:\n"
        #         message_send = message_send +"\t"+key+" : "+values+"\n"
        #     await message.channel.send("`"+message_send+"`")     
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
            listDecision = PPLDict[decision]
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


    
    def main_menu():
        print("PPL test:")
        ExerciseList = push_pull("legs")
        print(ExerciseList)
    
    async def messageList(self,listExercises,message):
        exercises = "\n".join(listExercises)
        await message.channel.send("`"+exercises+"`")
        #for index, exercise in enumerate(listExercises):









client = MyClient()
client.get_channel(channels["gymio"])
client.run(TOKEN)


main_menu()
















