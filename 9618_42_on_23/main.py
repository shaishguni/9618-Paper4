# stackVowel = []
# StackConsonant = []
# # Global String
# # GLobal String

# VowelTop = 0 
# ConsonantTop = 0

# def PushData(x: chr):
        
#         global VowelTop
#         global ConsonantTop
#         if x =="a" or x =="e" or x =="i" or x =="0" or x =="u":
#             if VowelTop >=100:
#                 b = 0
#             else:
#                 VowelTop = VowelTop + 1
#                 stackVowel.append(x)
#         else:
#             if ConsonantTop >= 100:
#                 b = 0
#             else:
#                 ConsonantTop = ConsonantTop  + 1 
#                 StackConsonant.append(x)




# def ReadData():
#     f = open("StackData.txt", 'r')

#     for i in f:
#         PushData(i.strip())
#     f.close()



# def PopVowel():
#     global VowelTop
#     if VowelTop <= 0:
#         return "No data"
#     else:
#         VowelTop = VowelTop - 1
#         return stackVowel.pop()


# def PopConsonant():
#     global ConsonantTop
#     if ConsonantTop <= 0:
#         return "No data"
#     else:
#         ConsonantTop = ConsonantTop - 1
#         return StackConsonant.pop()

# ReadData()
# print(StackConsonant)
# print(stackVowel)


# letters = []
# count = 0

# while count < 5:
#     choice = input("Enter 'vowel' for vowel or 'consonant' for consonant: ").lower()
    
#     if choice == 'vowel':
#         result = PopVowel()
#         if result == "No data":
#             print("Vowel stack is empty")
#         else:
#             letters.append(result)
#             count += 1
#     elif choice == 'consonant':
#         result = PopConsonant()
#         if result == "No data":
#             print("Consonant stack is empty")
#         else:
#             letters.append(result)
#             count += 1
#     else:
#         print("Invalid choice. Enter 'v' or 'c'")

# print(''.join(letters))


# def IterativeCalculate(number):
# 	total = 0
# 	to_find = number
# 	while number != 0:
# 		if to_find % number == 0:
# 			total = total + number
# 		number = number - 1
# 	return total

# # output  = IterativeCalculate(10)

# # print(output)


# def RecursiveValue(Number, ToFind):
#     if Number == 0:
#         return 0
#     else:
#         if ToFind % Number == 0:
#             return Number + RecursiveValue(Number - 1, ToFind)
#         else:
#             return RecursiveValue(Number - 1, ToFind)

# output = RecursiveValue(10, 10)
# print(output)

# from datetime import date


# class Character:
#     def __init__(self,CharacterName:str , DateOfBirth:date , Intelligence:float, Speed:int):
#         self.CharacterName = CharacterName
#         self.DateOfBirth = DateOfBirth
#         self.Intelligence = Intelligence
#         self.Speed = Speed

#     def __str__(self):
#         return f"Character Name: {self.CharacterName}, Date of Birth: {self.DateOfBirth}, Intelligence: {self.Intelligence}, Speed: {self.Speed}"

#     def GetIntelligence(self):
#         return self.Intelligence
#     def GetSpeed(self):
#         return self.Speed
#     def SetIntelligence(self, Intelligence):
#         self.Intelligence = Intelligence

#     def Learn(self):
#         self.Intelligence = self.Intelligence *1.1

#     def ReturnAge(self):
#         return 2026 - self.DateOfBirth.year

# FirstCharacter = Character("Royal",date(2019, 1, 1), 70, 30)

# FirstCharacter.Learn()
# print(FirstCharacter)


# class MagicalCharacter(Character):
#     def __init__(self,Element:str , CharacterName:str , DateOfBirth:date , Intelligence:float, Speed:int):
#         super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
#         self.Element = Element

#     def Learn(self):
#         if(self.__Element == "fire" or self.__Element == "water"):
#             super().SetIntelligence(super().GetIntelligence() * 1.2)
#         elif self.__Element == "earth":
#             super().SetIntelligence(super().GetIntelligence() * 1.3)
#         else:
#             super().SetIntelligence(super().GetIntelligence() * 1.1)

#             SecondCharacter = MagicalCharacter("fire", "Merlin", date(2000, 5, 15), 85, 50)
#             SecondCharacter.Learn()
#             print(f"Name: {SecondCharacter.CharacterName}")
#             print(f"Age: {SecondCharacter.ReturnAge()}")
#             print(f"Intelligence: {SecondCharacter.Intelligence}")