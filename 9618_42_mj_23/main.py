# global Animals

# Animals:str = ["horse","lion","rabbit","mouse","bird","deer","whale","elephant","kangaroo","tiger"]

# OCEDURE SortDescending()
#  DECLARE ArrayLength : INTEGER
#  DECLARE Temp : STRING
#  ArrayLength LENGTH(Animals)
#  FOR X 0 TO ArrayLength - 1
#  FOR Y ……………… TO ArrayLength - X - 1
#  IF MID(Animals[Y], 0, 1) < MID(Animals[………………], 0, 1) THEN
#  Temp Animals[………………]
#  Animals[Y] Animals[Y + 1]
#  Animals[Y + 1] ………………
#  ENDIF
#  NEXT Y
#  NEXT X
#  ENDPROCEDURE
# def SortDescending():
#     global Animals
#     ArrayLength = len(Animals)
#     for X in range(ArrayLength - 1):
#         for Y in range(ArrayLength - X - 1):
#             if Animals[Y][0] < Animals[Y + 1][0]:
#                 Temp = Animals[Y]
#                 Animals[Y] = Animals[Y + 1]
#                 Animals[Y + 1] = Temp

# SortDescending()
# for i in range(len(Animals)):
#     print(Animals[i])




# class SaleData:
#     def __init__(self, name:str, amount:int):
#         self.name = name
#         self.amount = amount

# CircularQueue = [] #SaleData, 5 items
# global NumberOfItems 
# global Head 
# global Tail 


# NumberOfItems:int = 0
# Head:int = 0
# Tail:int = 0
# for x in range(0, 5):
#     CircularQueue.append((SaleData("",-1)))


# def Enqueue(name:str, amount:int):
#    global NumberOfItems
#    global Tail
#    if NumberOfItems < 5:
#         CircularQueue[Tail] = SaleData(name, amount)
#         Tail = (Tail + 1) % 5
#         NumberOfItems += 1
#         return 1
#    else:
#         return -1
   

# def Dequeue():
#     global Head
#     global NumberOfItems
#     if NumberOfItems == 0:
#         return None
#     else:
#         record = CircularQueue[Head]
#         Head = (Head + 1) % 5
#         NumberOfItems -= 1
#         return record
    

# def EnterRecord():
#     ID = input("Enter ID")
#     QuantityP = input("Enter quantity")
#     Record = SaleData(ID, QuantityP)
#     if Enqueue(Record.name, Record.amount) == -1:
#         print("Full")
#     else:
#         print("Stored")

# EnterRecord()
# EnterRecord()
# EnterRecord()
# EnterRecord()
# EnterRecord()
# EnterRecord()
# ReturnValue = Dequeue()
# if ReturnValue.name == "":
#  print("No items")
# else:
#  print(ReturnValue.name, " ", ReturnValue.amount)
# EnterRecord()
# for x in range(0, 5):
#  print(CircularQueue[x].name, " ", CircularQueue[x].amount)


class Employee:
    # HourlyPay: float
    # EmployeeNumber: string
    # JobTitle: string

    def __init__(self, EmpNumP, PayP, JobP):
        self.HourlyPay = PayP
        self.EmployeeNumber = EmpNumP
        self.JobTitle = JobP
        self.PayYear2022 = []  # array 52 elements (float)

        for x in range(0, 52):
            self.PayYear2022.append(0.00)

    def GetEmployeeNumber(self):
        return self.EmployeeNumber

    def SetPay(self, WeekNumber, Hours):
        self.PayYear2022[WeekNumber - 1] = Hours * self.HourlyPay

    def GetTotalPay(self):
        TotalPay = 0
        for X in range(0, 52):
            TotalPay = TotalPay + self.PayYear2022[X]
        return TotalPay


class Manager(Employee):  # BonusValue: float

    def __init__(self, EmpNumP, PayP, JobP, BonusP):
        super().__init__(EmpNumP, PayP, JobP)
        self.BonusValue = BonusP

    def SetPay(self, WeekNumber, Hours):
        Hours = Hours * (1 + self.BonusValue / 100)
        super().SetPay(WeekNumber, Hours)


# ---------------- MAIN PROGRAM ----------------
EmployeeArray = []

try:
    with open("Employees.txt", 'r') as File:
        for x in range(0, 8):
            Pay = float(File.readline().strip())
            ID = File.readline().strip()
            Temp = File.readline().strip()

            try:
                Bonus = float(Temp)
                Title = File.readline().strip()
                EmployeeArray.append(Manager(ID, Pay, Title, Bonus))
            except:
                Title = Temp
                EmployeeArray.append(Employee(ID, Pay, Title))

except IOError:
    print("Could not find file")


def EnterHours():
    try:
        with open("HoursWeek1.txt", 'r') as File:
            for X in range(0, 8):
                EmpID = File.readline().strip()
                Hours = float(File.readline().strip())

                for Y in range(0, len(EmployeeArray)):
                    if EmployeeArray[Y].GetEmployeeNumber() == EmpID:
                        EmployeeArray[Y].SetPay(1, Hours)

    except IOError:
        print("Could not find file")


EnterHours()

for Y in range(0, len(EmployeeArray)):
    print(EmployeeArray[Y].GetEmployeeNumber(), " ", EmployeeArray[Y].GetTotalPay())
