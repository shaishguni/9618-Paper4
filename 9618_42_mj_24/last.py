class node:
    def __init__(self,data,nextNode):
        self.data = data
        self.nextNode = nextNode

linkedlist = [node(1,1),node(5,4) , node(6,7),node(7,-1), node(2,2) , node(0,6),node(56,3), node(0,9), node(0,-1)]
emptyList = 0

def outputNodes(arr , currentPointer,emptyList):
    while currentPointer != -1:
        print(arr[currentPointer].data)
        currentPointer = arr[currentPointer].nextNode

class node:
    def __init__(self,data,nextNode):
        self.data = data
        self.nextNode = nextNode

linkedlist = [node(1,1),node(5,4) , node(6,7),node(7,-1), node(2,2) , node(0,6),node(56,3), node(0,9), node(0,-1)]
emptyList = 0

def outputNodes(arr , currentPointer,emptyList):
    while currentPointer != -1:
        print(arr[currentPointer].data)
        currentPointer = arr[currentPointer].nextNode


def addNode(arr, data):
    global emptyList, startPointer

    if emptyList == -1:
        print("No more space")
    else:
        newNode = emptyList
        emptyList = arr[newNode].nextNode

        arr[newNode].data = data
        arr[newNode].nextNode = startPointer

        startPointer = newNode