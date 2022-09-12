#CarInventoryNode.py
from Car import Car
class CarInventoryNode:
    def __init__(self, car):
        self.car = car
        self.make = car.make
        self.model = car.model
        self.price = car.price
        self.year = car.year
        self.cars = [car]
        self.left = None
        self.right = None
        self.parent = None
        
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def setLeft(self, left):
        #Case 1: Node does not have a left child
        if self.getLeft == None:
            self.left = CarInventoryNode(left)
        else: #Case 2L Node has a left child
            t = CarInventoryNode(left)
            t.left = self.left #Links the left sub tree
            self.left = t
            
    def setRight(self, right):
        #Case 1: Node does not have a right child
        if self.getRight == None:
            self.right = CarInventoryNode(right)
        else: #Case 2L Node has a right child
            t = CarInventoryNode(right)
            t.right = self.right #Links the right sub tree
            self.right = t
        
    def getLeft(self):
        #considers None as a false value
        return self.left
    
    def getRight(self):
        return self.right
    
    #New functions
    def isLeft(self):
        return self.parent and self.parent.left == self
    
    def isRight(self):
        return self.parent and self.parent.right == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.right or self.left)
    
    def hasAnyChildren(self):
        return self.right or self.left
    
    def hasBothChildren(self):
        return self.right and self.left
    
    def hasLeft(self):
        #considers None as a false value
        return self.left 
    
    def hasRight(self):
        return self.right
    
    def replaceNodeData(self,car,lc,rc):
        #changed from self.car = car
        
        self.car = car
        self.cars = car.cars
        self.make = car.make
        self.model = car.model
        self.price = car.price
        self.year= car.year
        self.left = lc
        self.right = rc
        #print("a")
        #print(self)
        
        if self.hasLeft():
            #print("b")
            self.left.parent = self
        if self.hasRight():  
            #print("c")
            self.right.parent = self
            
            
    def getSuccessor(self):
        succ = None
        if self.hasRight():
            #print("b")
            succ = self.right.findMin()
        else:
            #print("c")
            if self.parent:
                #print("d")
                if self.isLeft():
                    #print("e")
                    succ = self.parent
                else:
                    #print("f")
                    self.parent.right = None
                    succ = self.parent.getSuccessor()
                    self.parent.right = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeft():
            current = current.left
        #print(current)
        return current

    def spliceOut(self):
        if self.isLeaf():
            #print("a1")
            if self.isLeft():
                #print("a2")
                self.parent.left = None
            else:
                #print("a3")
                self.parent.right = None
        elif self.hasAnyChildren():
            #print("a4")
            if self.hasLeft():
                #print("a5")
                if self.isLeft():
                    #print("a6")
                    self.parent.left = self.left
                else:
                    #print("a7")
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                #print("a8")
                if self.isLeft():
                    #print("a9")
                    self.parent.left = self.right
                else:
                    #print("a10")
                    self.parent.right = self.right
                self.right.parent = self.parent
    
   
    
    
    #old ones
    def setParent(self,parent):
        self.parent = parent
        
    def getParent(self):
        return self.parent
    
    def __str__(self):
        i = 0
        carstr = ""
        for elements in list(self.cars):
            #"Make: {}, Model: {}, Year: {}, Price: ${}".format(self.make,self.model,self.year,self.price)
            #self.cars[i].make
            carstr = carstr + "Make: {}, Model: {}, Year: {}, Price: ${}".format(self.cars[i].make,self.cars[i].model,self.cars[i].year,self.cars[i].price) + "\n"
            i += 1

        return carstr
