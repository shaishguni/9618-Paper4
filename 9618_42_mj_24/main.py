# # WordArray = []
# # NumberWords = 0

# # def ReadWords(filename):
# #     global WordArray, NumberWords
# #     WordArray = []
# #     NumberWords = 0
    
# #     try:
# #         with open(filename, 'r') as file:
# #             lines = file.readlines()
# #             MainWord = lines[0].strip()
# #             WordArray.append(MainWord)
            
# #             for i in range(1, len(lines)):
# #                 word = lines[i].strip()
# #                 if word:
# #                     WordArray.append(word)
# #                     NumberWords += 1
# #     except FileNotFoundError:
# #         print("File not found")


# # WordArray = []
# # NumberWords = 0
# # Choice = input("Easy, medium or hard? ").lower()
# # if Choice == "easy":
# #     File = "Easy.txt"
# # elif Choice == "medium":
# #     File = "Medium.txt"
# # else:
# #     File = "Hard.txt"
# #     ReadWords(File)



# # def Play():
# #     global WordArray
# #     global NumberWords
# #     Word = WordArray[0]
# #     print("The word is: ", Word)
# #     print("There are", NumberWords-1,"words that can be made with 3 or more letters")
# #     WordArray[0] = ""
# #     Answer = "yes"
# #     QuantityFound = 0
# #     while Answer != "no":
# #         Answer = input("Enter your word or no to stop ").lower()
# #         Found = False
# #         if Answer != "no":
# #             for x in range(0, NumberWords):
# #                 if Answer == WordArray[x]:
# #                     WordArray[x] = ""
# #                     QuantityFound = QuantityFound + 1
# #                     print("Correct, you have found", QuantityFound, "words")
# #                     Found = True
# #                     if Found == False:
# #                         print("Sorry that was incorrect")
# #                         Correct = (QuantityFound / (NumberWords-1)) * 100
# #                         print("You found", Correct,"%") 

# # def ReadWords(FileName):
# #     global WordArray
# #     global NumberWords
# #     File = open(FileName, 'r')
# #     DataRead = File.read().strip()
# #     File.close()
# #     WordArray = DataRead.split()
# #     NumberWords = len(WordArray)
# #     Play()

# # ReadWords(File)

# # class Node:
# #     def __init__(self,Data:int,LeftPointer:int = -1, RightPointer:int = -1):
# #         self.Data = Data
# #         self.LeftPointer = LeftPointer
# #         self.RightPointer = RightPointer

# #     def GetLeft(self):
# #         return self.LeftPointer
# #     def GetRight(self):
# #         return self.RightPointer
# #     def GetData(self):
# #         return self.Data
    
# #     def SetLeft(self,NewLeft):
# #         self.LeftPointer = NewLeft
# #     def SetRight(self,NewRight):
# #         self.RightPointer = NewRight
# #     def SetData(self,NewData):
# #         self.Data = NewData


# # class TreeClass():
# #     def __init__ (self):
# #         self. Tree = [] 
# #         self. FirstNode:int = -1 
# #         self. NumberNodes:int = 0 
# #         for x in range(20):
# #             self. Tree.append(Node(-1,-1,-1))
# #     def InsertNode(self, NewNode):
# #         if self.NumberNodes == 0:
# #             self.Tree[0] = NewNode
# #             self.FirstNode = 0
# #             self.NumberNodes = self.NumberNodes + 1
# #         else:
# #             self.Tree[self.NumberNodes] = NewNode
# #             NodeAccess = self.FirstNode
# #             Direction = ""
# #             while NodeAccess != -1:
# #                 Previous = NodeAccess
# #                 if NewNode.GetData() < self.Tree[NodeAccess].GetData():
# #                     NodeAccess = self.Tree[NodeAccess].GetLeft()
# #                     Direction = "left"
# #                 elif NewNode.GetData() > self.Tree[NodeAccess].GetData():
# #                     NodeAccess = self.Tree[NodeAccess].GetRight()
# #                     Direction = "right"
# #             if Direction == "left":
# #                 self.Tree[Previous].SetLeft(self.NumberNodes)
# #             else:
# #                 self.Tree[Previous].SetRight(self.NumberNodes)
# #             self.NumberNodes = self.NumberNodes + 1

# #     def OutputTree(self):
# #         if self. NumberNodes == 0:
# #             print("No nodes")
# #         else:
# #             for x in range(0, self. NumberNodes):
# #                 print(self. Tree[x].GetLeft(), " ", self. Tree[x].GetData(), " ",self.Tree[x].GetRight())

# # TheTree = TreeClass()
# # TheTree.InsertNode(Node(10))
# # TheTree.InsertNode(Node(11))
# # TheTree.InsertNode(Node(5))
# # TheTree.InsertNode(Node(1))
# # TheTree.InsertNode(Node(20))
# # TheTree.InsertNode(Node(7))
# # TheTree.InsertNode(Node(15))
# # TheTree.OutputTree()

# NumberArray:int = [100,85,644,22,15,8,1]

# def RecursiveInsertion(IntegerArray, NumberElements):
#     if NumberElements <= 1:
#         return IntegerArray
#     RecursiveInsertion(IntegerArray, NumberElements - 1)
#     LastItem = IntegerArray[NumberElements - 1]
#     CheckItem = NumberElements - 2
#     LoopAgain = True
#     if CheckItem < 0:
#         LoopAgain = False
#     elif IntegerArray[CheckItem] <= LastItem:
#         LoopAgain = False
#     while (LoopAgain):
#         IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
#         CheckItem = CheckItem - 1
#         if CheckItem < 0:
#             LoopAgain = False
#         elif IntegerArray[CheckItem] <= LastItem:
#             LoopAgain = False
#     IntegerArray[CheckItem + 1] = LastItem
#     return IntegerArray


# # SortedArray = RecursiveInsertion(NumberArray, len(NumberArray))
# # print("Recursive", SortedArray)



# def IterativeInsertion(IntegerArray, NumberElements):
#     while NumberElements > 0:
#         LastItem = IntegerArray[NumberElements - 1]
#         CheckItem = NumberElements - 2
#         LoopAgain = True
#         if CheckItem < 0:
#             LoopAgain = False
#         elif IntegerArray[CheckItem] <= LastItem:
#             LoopAgain = False
#         while(LoopAgain):
#             IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
#             CheckItem = CheckItem - 1
#             if CheckItem < 0:
#                 LoopAgain = False
#             elif IntegerArray[CheckItem] <= LastItem:
#                 LoopAgain = False
#             IntegerArray[CheckItem + 1] = LastItem
#         NumberElements = NumberElements - 1
#     return IntegerArray

# Sorted2Array = IterativeInsertion(NumberArray, len(NumberArray))
# # print("iterative", Sorted2Array) 


# def BinarySearch(IntegerArray, First, Last, ToFind):
#     if First > Last:
#         return -1
#     else:
#         Middle = int((Last + First) / 2)
#         if IntegerArray[Middle] == ToFind:
#             return Middle
#         elif IntegerArray[Middle] > ToFind:
#             return BinarySearch(IntegerArray, First, Middle - 1, ToFind)
#         else:
#             return BinarySearch(IntegerArray, Middle + 1, Last, ToFind)
        
# Position = BinarySearch(Sorted2Array, 0, len(NumberArray)-1, 644)
# if Position == -1:
#  print("Not found")
# else:
#  print(Position)