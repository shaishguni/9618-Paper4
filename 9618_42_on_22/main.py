# global Jobs , NumberOfJobs
# Jobs = [[],[]]
# NumberOfJobs = 0

# def Initialise():
#     global Jobs , NumberOfJobs
#     Jobs = []
#     for i in range(0, 100):
#         Jobs.append([-1,-1])
#     NumberOfJobs = 0

# # 
# def AddJob(JobNumber, Priority):
#     global NumberOfJobs , Jobs
#     if NumberOfJobs < 100:
#         Jobs[NumberOfJobs][0] = JobNumber
#         Jobs[NumberOfJobs][1] = Priority
#         NumberOfJobs += 1
#         print("Added")
#     else:
#         print( "Not Added")

# Initialise()
# AddJob(12,10)
# AddJob(526,9)
# AddJob(33,8)
# AddJob(12,9)
# AddJob(78,1)


# def InsertionSort():
#     global Jobs
#     global NumberOfJobs
#     for i in range(1, NumberOfJobs):
#         Current1 = Jobs[i][0]
#         Current2 = Jobs[i][1]
#         while i > 0 and Jobs[i-1][1] > Current2:
#             Jobs[i][0] = Jobs[i-1][0]
#             Jobs[i][1] = Jobs[i-1][1]
#             i = i - 1
#         Jobs[i][0] = Current1
#         Jobs[i][1] = Current2

# def PrintArray():
#  global Jobs
#  global NumberOfJobs
#  for i in range(0, NumberOfJobs):
#     print(str(Jobs[i][0]), " priority ", str(Jobs[i][1]))


# InsertionSort()
# PrintArray()


# class Character:
#     def __init__(self,Name:str,XCoordinate:int,YCoordinate:int):
#         self.Name = Name
#         self.XCoordinate = XCoordinate
#         self.YCoordinate = YCoordinate
    
#     def __str__(self):
#         return f"{self.Name}  ({self.XCoordinate}, {self.YCoordinate})"
    
#     def GetName(self):
#         return self.Name
    
#     def GetXCoordinate(self):
#         return self.XCoordinate
    
#     def GetYCoordinate(self):
#         return self.YCoordinate
    
#     def ChangePosition(self, XChange , YChange):
#         self.XCoordinate += XChange
#         self.YCoordinate += YChange
    

# Characters = []

# try:
#     with open("Characters.txt","r") as f:
#         while True:
#             name = str(f.readline().strip())
#             if not name:
#                 break
#             else: 
#                 x = int(f.readline().strip())
#                 y = int(f.readline().strip())
#                 data = Character(name, x, y)
#                 Characters.append(data)
#     f.close()
# except FileNotFoundError or EOFError:
#     print("Error reading file")

# # for character in Characters:
# #     print(character)

# found = False
# index = 0 
# while not found:
#     name = input("Enter the name of the character you want to move: ")
#     for i in range(len(Characters)):
#         if Characters[i].GetName() == name:
#             found = True
#             index = i
#             print("Character found at index ", index)
#             break
#     if not found:
#         print("Character not found, please try again")
#         break



# Valid  = False

# while not Valid:
#     Move:str = input("Enter your movement , (W,A,S,D) : ")
#     if Move == "W":
#         Characters[index].ChangePosition(0,1)
#         Valid = True
#     elif Move == "A":
#         Characters[index].ChangePosition(-1,0)
#         Valid = True
#     elif Move == "S":
#         Characters[index].ChangePosition(0,-1)
#         Valid = True
#     elif Move == "D":
#         Characters[index].ChangePosition(1,0)
#         Valid = True
#     else:
#         print("Invalid input, please try again")

# print (f"{Characters[index].GetName()} is now at position ({Characters[index].GetXCoordinate()}, {Characters[index].GetYCoordinate()})")


Queue:int = [-1 for I in range(100)] #Integer
HeadPointer = -1
TailPointer = 0

def Enqueue(Value:int):
    global Queue , HeadPointer , TailPointer
    if TailPointer < 100:
        Queue[TailPointer] = Value
        TailPointer += 1
        return True
    else:
        return False
    

inserted = False
for Count in range(1, 21):
    inserted = Enqueue(Count)
    if(inserted == False):
        print("Unsuccessful")
    else:
        print("Successful")

def RecursiveOutput(Start: int) -> int:
    Total:int = 0
    for Count in range(Start-1 , HeadPointer, -1):
        Total = Total + Queue[Count]
        return Total


print(str(RecursiveOutput(TailPointer - 1)))