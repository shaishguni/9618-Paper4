class Node:
    def __init__(self,Data:int ):
        self.LeftPointer  = -1
        self.Data  = Data
        self.RightPointer  = -1

    def GetLeft(self):
        return self.LeftPointer
    def getRight(self):
        return self.RightPointer
    def getData(self):
        return self.Data
    
    def setLeft(self,parm):
        self.LeftPointer = parm
    def setRight(self,parm):
        self.RightPointer = parm
    def setData(self,parm):
        self.Data = parm

class TreeClass:
    def __init__(self):
        self.Tree:int = []
        self.FirstNode:int = -1
        self.NumberNode:int = 0

        for i in range(0,19):
            self.Tree.append(Node(-1))

    def Insert(self, NewNode):
        if self.NumberNode ==0:
            self.Tree[self.NumberNode] = NewNode
            self.NumberNode += 1
            self.FirstNode  = 0 
        else:
            self.Tree[self.NumberNode] = NewNode
            node  = self.FirstNode
            Direction  = ""
            while node != -1:
                previous = node 
                if self.Tree[node].getData() > NewNode.getData():
                    node = self.Tree[node].GetLeft()
                    Direction = "Left"
                else:
                    node  = self.Tree[node].getRight()
                    Direction = "Right"
            if Direction == "Left":
                self.Tree[previous].setLeft(self.NumberNode)
            else:
                self.Tree[previous].setRight(self.NumberNode)
            self.NumberNode += 1
    
    def Output(self):
        if self.NumberNode == 0:
            print("No Nodes")
        else:
            for i in range(0,self.NumberNode):
                print(self.Tree[i].GetLeft(), self.Tree[i].getData(), self.Tree[i].getRight())

TheTree = TreeClass()

TheTree.Insert(Node(10))
TheTree.Insert(Node(11))
TheTree.Insert(Node(5))
TheTree.Insert(Node(1))
TheTree.Insert(Node(20))
TheTree.Insert(Node(7))
TheTree.Insert(Node(15))

TheTree.Output()