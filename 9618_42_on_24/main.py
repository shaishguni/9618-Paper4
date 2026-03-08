# class EventItem:
#     def __init__(self,EventName:str , Type:str , Difficulty:int):
#         self.EventName = EventName
#         self.Type = Type
#         self.Difficulty = Difficulty

#     def GetName(self):
#         return self.EventName
#     def GetEventType(self):
#         return self.Type
#     def GetDifficulty(self):
#         return self.Difficulty
# Group = []

# Group.append(EventItem("Bridge", "jump", 3))
# Group.append(EventItem("Water wade", "swim", 4))
# Group.append(EventItem("100 mile run", "run", 5))
# Group.append(EventItem("Gridlock", "drive", 2))
# Group.append(EventItem("Wall on wall", "jump", 4))

# class Character():
#     def __init__(self, pName:str, pJump:int, pSwim:int, pRun:int, pDrive:int):
#         self.__CName = pName 
#         self.__Jump = pJump 
#         self.__Swim = pSwim 
#         self.__Run = pRun 
#         self.__Drive = pDrive 
    
#     def GetName(self):
#         return self.__CName
    
#     def CalculateScore(self, Type, Difficulty):
#         if Type == "jump":
#             Chance = self.__Jump
#         elif Type == "swim":
#             Chance = self.__Swim
#         elif Type == "run":
#             Chance = self.__Run
#         else:
#             Chance = self.__Drive
#         if Chance >= Difficulty:
#             return 100
#         else:
#             Difference = Difficulty - Chance
#         if Difference == 1:
#             return 80
#         elif Difference == 2:
#             return 60
#         elif Difference == 3:
#             return 40
#         elif Difference == 4:
#             return 20
#         else:
#             return 0
        
# P1 = Character("Tarz", 5, 3, 5, 1)
# P2 = Character("Geni", 2, 2, 3, 4)

# P1Points = 0
# P2Points = 0
# for x in range(0, 5):
#     P1EventScore = P1.CalculateScore(Group[x].GetEventType(), Group[x].GetDifficulty())
#     P2EventScore = P2.CalculateScore(Group[x].GetEventType(), Group[x].GetDifficulty())
#     if P1EventScore > P2EventScore:
#         P1Points = P1Points + 1
#         print(P1.GetName(), "you win this event")
#     elif P2EventScore > P1EventScore:
#         P2Points = P2Points + 1
#         print(P2.GetName(), "you win this event")
#     else:
#         print("This event is a draw")
#     if P1Points > P2Points:
#         print(P1.GetName(), "you have won with", P1Points)
#     elif P2Points> P1Points:
#         print(P2.GetName(), "you have won with", P2Points)
#     else:
#         print("It's a draw")


# class Queue:
#     def __init__(self):
#         self.QueueArray = []
#         self.HeadPointer = 0 #integer
#         self.TailPointer = 0 #integer
#         for x in range(0, 100):
#             self.QueueArray.append(-1)

# class Queue:
#     def __init__(self):
#         self.QueueArray = []
#         for x in range(0, 100):
#             self.QueueArray.append(-1)

#         self.HeadPointer = -1
#         self.TailPointer = 0
# TheQueue= Queue()


# def Enqueue(AQueue, TheData):
#     if AQueue.HeadPointer == -1:
#         AQueue.HeadPointer = 0
#         AQueue.QueueArray[AQueue.HeadPointer] = TheData
#         AQueue.TailPointer += 1
#         return AQueue, 1
#     elif AQueue.TailPointer > 99:
#         return AQueue, -1
#     else:
#         AQueue.QueueArray[AQueue.TailPointer] = TheData
#         AQueue.TailPointer = AQueue.TailPointer + 1
#         return AQueue, 1
    
# def ReturnAllData(TheQueue):
#     Temp = ""
#     for X in range(TheQueue.HeadPointer, TheQueue.TailPointer):
#         Temp = Temp + str(TheQueue.QueueArray[X]) + " "
#         return Temp
    


# # for x in range(0, 10):
# #     Continue = True
# #     while(Continue == True):
# #         DataInput = int(input("Enter an integer that is 0 or more"))
# #         if DataInput > -1:
# #             Continue = False

# #     TheQueue, ReturnValue = Enqueue(TheQueue, DataInput)

# #     if(ReturnValue == -1):
# #         print("Queue full")
# #     else:
# #         print("Item inserted")

# # print(ReturnAllData(TheQueue))

# def Dequeue(AQueue):
#     if AQueue.HeadPointer == 100 or AQueue.HeadPointer == -1 or AQueue.HeadPointer == AQueue.TailPointer:
#         return AQueue, -1
#     else:
#         Temp = AQueue.QueueArray[AQueue.HeadPointer]
#         AQueue.HeadPointer = AQueue.HeadPointer + 1
#         return AQueue, Temp
    
# TheQueue, ReturnValue = Dequeue(TheQueue)
# if ReturnValue == -1:
#  print("Queue empty")
# else:
#  print(ReturnValue, " is returned")
# TheQueue, ReturnValue = Dequeue(TheQueue)
# if ReturnValue == -1:
#  print("Queue empty")
# else:
#  print(ReturnValue, " is returned")
# print(ReturnAllData(TheQueue))


HighScores:str = [] #String, 7 x 3
HighScores = [['' for x in range(3)] for y in range(7)]

def ReadData():
	Temp = []
	HighScores = []
	try:
		File = open("HighScoreTable.txt")
		Temp = File.read().split("\n")
		File.close()
	except:
		print("No file found")
	NumberRecords = len(Temp)-1
	Counter = 0
	while Counter < NumberRecords:
		HighScores.append([Temp[Counter], Temp[Counter+1], Temp[Counter+2]])
		Counter = Counter + 3

	return HighScores

def OutputHighScores(HighScores):
    for x in range(0, len(HighScores)):
        print(HighScores[x][0], "reached level", HighScores[x][1], "with a score of", HighScores[x][2])


def SortScores(HighScores):
 Counter = 0
 ArrayLength = len(HighScores)
 for x in range(ArrayLength-1):
    for y in range(0, ArrayLength-x-1):
        if int(HighScores[y][1]) < int(HighScores[y + 1][1]):
            HighScores[y], HighScores[y + 1] = HighScores[y + 1], HighScores[y]
        elif int(HighScores[y][1]) == int(HighScores[y+1][1]):
            if int(HighScores[y][2]) < int(HighScores[y+1][2]):
                HighScores[y], HighScores[y + 1] = HighScores[y + 1], HighScores[y]
 return HighScores


HighScores = []
HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)