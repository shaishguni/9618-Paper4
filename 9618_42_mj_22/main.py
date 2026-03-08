# global StackData
# global StackPointer

# StackData = []
# StackPointer = 0

# def PrintArray():
#     for i in range(len(StackData)):
#         print(StackData[i])



# def Push(number):
#     global stackData
#     global StackPointer
#     if StackPointer >= 10:
#         return False
#     else:
#         StackData.append(number)
#         StackPointer += 1
#         return True



# for i in range(0,11):
#     number:int = input("Enter a number: ")
#     if Push(number) == True:
#         print("Number Inserted.")
#     else:
#         print("Stack Full")
# print("Before Pop: ")
# PrintArray()

# def Pop():
#     global StackPointer,StackData
#     if StackPointer <=0:
#         return -1
#     else:
#         StackData.pop()
#         StackPointer -= 1
# print("After Pop:")
# Pop()
# Pop()
# PrintArray()


'''
ArrayLength 10
 FOR X 0 TO ArrayLength - 1
 FOR Y 0 TO ArrayLength - 2
 FOR Z 0 TO ArrayLength - Y - 2
 IF ArrayData[X, Z] > ArrayData[X, Z + 1] THEN
 TempValue ArrayData[X, Z]
 ArrayData[X, Z] ArrayData[X, Z+1]
 ArrayData[X, Z + 1] TempValue
 ENDIF
 NEXT Z
 NEXT Y
 NEXT X

'''

# import random
# def Printarray(ArrayData):
# 	for x in range(0, 10):
# 		for y in range(0, 10):
# 			print(ArrayData[x][y], " ", end='')
# 		print("")
# #main
# ArrayData = [[0]*10 for _ in range(10)] #integer
# for x in range(0, 10):
# 	for y in range(0, 10):
# 		ArrayData[x][y] = random.randint(1, 100)
# print("Before")
# Printarray(ArrayData)
# ArrayLength = 10
# for X in range(0, ArrayLength):
# 	for Y in range(0, ArrayLength):
# 		for Z in range(0, ArrayLength - Y - 1):
# 			if(ArrayData[X][Z] > ArrayData[X][Z+1]):
# 				TempNumber = ArrayData[X][Z]
# 				ArrayData[X][Z] = ArrayData[X][Z+1]
# 				ArrayData[X][Z+1] = TempNumber
# print("After")
# Printarray(ArrayData)



# def BinarySearch(SearchArray, Lower, Upper, SearchValue):
# 	if Upper >= Lower:
# 		Mid = int((Lower + (Upper - 1)) / 2)
# 		if SearchArray[0][Mid] == SearchValue:
# 			return Mid
# 		elif SearchArray[0][Mid] > SearchValue:
# 			return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
# 		else:
# 			return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
# 	return -1



# SearchValue = int(input("Enter a number to search: "))
# Result = BinarySearch(ArrayData, 0, ArrayLength-1, SearchValue)
# if Result != -1:
# 	print("Number found at index: ", Result)
# else:
#     print("Number not found in the array.")



class Card:
    def __init__(self,Number:int ,Colour:str):
        self.number   = Number
        self.colour   = Colour

    def __str__(self):
        return f" {self.number} {self.colour}"
    
    def GetNumber(self):
        return self.number
    def GetColour(self):
        return self.colour
    


card = []

try:
    with open("CardValues.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            NumberRead = lines[i].strip()
            ColourRead = lines[i + 1].strip()
            try:
                card.append(Card(int(NumberRead), ColourRead))
            except ValueError:
                print(f"Skipping invalid data: '{NumberRead}' is not a valid integer")
except FileNotFoundError:
    print("File not found.")

# for i in range(len(card)):
#     print(card[i])

def ChooseCard():
        global NumbersChosen
        flagContinue = True
        while flagContinue == True:
            CardSelected = int(input("Select a Card from 1 to 30: "))
            if CardSelected < 1 or CardSelected > 30:
                print("Number must be between 1 and 30")
            elif NumbersChosen[CardSelected - 1] == True:
                print("Already taken")
            else:
                print("Valid")
                flagContinue = False
                NumbersChosen[CardSelected - 1] = True
                return CardSelected - 1

NumbersChosen = [False for i in range(30)]

P1 = [] 
for x in range(0, 4):
    ReturnNumber = ChooseCard()
    P1.append(card[ReturnNumber])
for x in range(0, 4):
 print(P1[x].GetColour())
 print(P1[x].GetNumber()) 