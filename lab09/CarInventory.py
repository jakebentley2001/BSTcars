#CarInventory.py
from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def _put(self,car,currentNode):
        if car.make == currentNode.make and car.model == currentNode.model:
            currentNode.cars.append(car)
            
        elif car < currentNode: 
            if currentNode.getLeft():
                self._put(car,currentNode.left)
            else:
                #currentNode.left = CarInventoryNode(car,parent = currentNode)
                currentNode.setLeft(CarInventoryNode(car))
                currentNode.getLeft().parent = currentNode

        else:
            if currentNode.getRight():
                self._put(car,currentNode.right)
            else:
                #currentNode.right = CarInventoryNode(car,parent = currentNode)
                currentNode.setRight(CarInventoryNode(car))
                currentNode.getRight().parent = currentNode
  
    def addCar(self, car):
        self.size = self.size + 1
        if self.root:
            self._put(car,self.root)
            
        else:
            self.root = CarInventoryNode(car)
            
          
        
    def _get(self, car, currentNode):
        if not currentNode:
            return None
        elif currentNode.car.make == car.make and currentNode.car.model == car.model:
            if car in currentNode.cars:
                return currentNode
            else:
                return None
        elif car < currentNode.car:
            return self._get(car,currentNode.left)
        else:
            return self._get(car,currentNode.right)
                
            
    #return the True if it exists
    def doesCarExist(self,car):
        if self.root:
            #returns the node with key if it exists, None otherwise
            res = self._get(car,self.root)
            if res:
                return True
            else:
                return False
        else:
            return False     
        
        
    def inOrder(self):
        def inorder(tree):
            ret = ""
            if tree != None:
                ret += inorder(tree.getLeft())
                ret += str(tree)#visit node
                ret += inorder(tree.getRight())
            return ret
        #print(inorder(self.root))
        return inorder(self.root)
        
    def preOrder(self):
        def preorder(tree):
            ret = ""
            if tree != None:
                
                ret = ret + str(tree)#visit node
                ret += preorder(tree.getLeft())
                ret += preorder(tree.getRight())
                
            return ret
        #print(preorder(self.root))
        return preorder(self.root)
        
    def postOrder(self):
        def postorder(tree):
            ret = ""
            if tree != None:
                
                ret += postorder(tree.getLeft())
                ret += postorder(tree.getRight())
                ret = ret + str(tree) #visit node
                
            return ret
        return postorder(self.root)

        
  
    def _get2(self, car, currentNode):
        if not currentNode:
            return None
        elif currentNode.car.make == car.make and currentNode.car.model == car.model:
            return currentNode
            #return currentNode.cars
        elif car < currentNode.car:
            return self._get2(car,currentNode.left)
        else:
            return self._get2(car,currentNode.right)

        
    def getBestCar(self,make,model):
        def doesCarMakeModelExist(make,model):
            searchCar = Car(make,model,0,0)
            if self.root:
            #returns the node with key if it exists, None otherwise
                res = self._get2(searchCar,self.root)
                if res:
                    return res
                else:
                    return None
            else:           
                return None       
        if doesCarMakeModelExist(make,model) != None:
            newestYear = 0
            highestPrice = 0
            i = 0
            x = doesCarMakeModelExist(make,model).cars
            for elements in x:
                if x[i].year > newestYear:
                    newestYear = x[i].year
                    highestPrice = x[i].price
                    i += 1
                elif x[i].year == newestYear:
                    if x[i].price > highestPrice:
                        highestPrice = x[i].price
                        i +=1
                    else:
                        i += 1                     
                else:
                    i += 1                
        else:
            return None    
        return Car(make,model,newestYear,highestPrice) 

    
    
    def getWorstCar(self,make,model):
        def doesCarMakeModelExist(make,model):
            searchCar = Car(make,model,0,0)
            if self.root:
            #returns the node with key if it exists, None otherwise
                res = self._get2(searchCar,self.root)
                if res:
                    return res
                else:
                    return None
            else:           
                return None
        
        if doesCarMakeModelExist(make,model) != None:
            oldestYear = 1000000
            lowestPrice = 1000000
            i = 0
            x = doesCarMakeModelExist(make,model).cars
            for elements in x:
                if x[i].year < oldestYear:
                    oldestYear = x[i].year
                    lowestPrice = x[i].price
                    i += 1
                elif x[i].year == oldestYear:
                    if x[i].price < lowestPrice:
                        lowestPrice = x[i].price
                        i +=1
                    else:
                        i += 1
                        
                else:
                    i += 1
                    
                    
        else:
            return None
        
        
        return Car(make,model,oldestYear,lowestPrice)
    
    
    def getTotalInventoryPrice(self):
        def pricegetter(tree):
            ret = 0
            if tree != None:
                ret += pricegetter(tree.getLeft())
                for elements in tree.cars:
                    ret = ret + elements.price
                ret += pricegetter(tree.getRight())
            return ret
        return pricegetter(self.root)
    
    
    
    
    
    def remove(self,currentNode):
        
        #Case 1: Node to remove is the leaf
        if currentNode.isLeaf():
            #print(1)
            if currentNode == currentNode.parent.left:
                #print(2)
                currentNode.parent.left = None
            else:
                #print(3)
                currentNode.parent.right = None
        
        #Case 3: Node to remove has both children
        elif currentNode.hasBothChildren():
            #print(13)
            #Need to find the successor, remove the successor, and replace
            #the currentNode with the successor's data/ payload
            succ = currentNode.getSuccessor()
            #print(14)
            succ.spliceOut()
            #print(15)
            currentNode.car = succ
            currentNode.cars = succ.cars
            currentNode.make = succ.make
            currentNode.model = succ.model
            currentNode.price = succ.price
            currentNode.year = succ.year
            
            #print(16)
            
            
            
        #Case 2: Node to remove has one child
        else:
            #print(4)
            #Node has leftChild
            if currentNode.hasLeft():
                #print(5)
                if currentNode.isLeft():
                    #print(6)
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.isRight():
                    #print(7)
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else: #Current Node is the root
                    #print(8)
                    #print(currentNode.left.car)
                    #print(currentNode.left.left)
                    #print(currentNode.left.right)
                    currentNode.replaceNodeData(currentNode.left,
                                               currentNode.left.left,
                                               currentNode.left.right)
                    #print(currentNode)
            #Node has rightChild
            else:
                #print(9)
                if currentNode.isLeft():
                    #print(10)
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.isRight():
                    #print(11)
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    #print(12)
                    currentNode.replaceNodeData(currentNode.right.car,
                                                currentNode.right.left,
                                                currentNode.right.right)
                    
  
    
    def removeCar(self,make,model,year,price):
        car = Car(make,model,year,price)
        if self.size > 1:
            nodeToRemove = self._get(car,self.root)
            #print(nodeToRemove)
            if nodeToRemove:
                #error here
                if len(nodeToRemove.cars) == 1:
                    self.remove(nodeToRemove)
                    self.size = self.size -1
                    return True
                else:
                    nodeToRemove.cars.remove(car)
                    self.size = self.size - 1
                    return True
            else:
                return False
        elif self.size == 1 and self.root == car:
            self.root = None
            self.size = self.size - 1
            return True
        else:
            return False
        
    def getSuccessor(self,make,model):
        car = Car(make,model,0,0)
        x = self._get2(car,self.root)
        if x:
            return x.getSuccessor()
        else:
            return None
   
    
